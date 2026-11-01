"""Run with python -m ingestion.pipeline --help. No deployment dependency."""
import argparse
import asyncio
import bz2
import csv
import gzip
import hashlib
import json
import os
import random
import re
import shutil
import sqlite3
import string
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urljoin, urlsplit
from urllib.robotparser import RobotFileParser
import requests
from .model import RecipeJSONLD, canonical_url, empty_record, finalize, from_meal, from_schema, texts, validate
from .ingredients import parse_ingredient

ROOT=Path(__file__).resolve().parents[1]
USER_AGENT='LAtelierRecipeResearch/2.0 (local recipe curation; respects robots.txt)'

class Store:
    def __init__(self,path):
        Path(path).parent.mkdir(parents=True,exist_ok=True)
        self.db=sqlite3.connect(path)
        self.db.executescript('''CREATE TABLE IF NOT EXISTS urls(url TEXT PRIMARY KEY,status TEXT,attempts INTEGER DEFAULT 0,error TEXT,updated REAL);
        CREATE TABLE IF NOT EXISTS records(id TEXT PRIMARY KEY,source TEXT,digest TEXT,data TEXT);
        CREATE TABLE IF NOT EXISTS duplicates(id TEXT,existing_id TEXT,reason TEXT,PRIMARY KEY(id,existing_id));''')
    def seen(self,url):
        row=self.db.execute('SELECT status FROM urls WHERE url=?',(url,)).fetchone()
        return row and row[0] in ('processed','no_recipe','blocked')
    def mark(self,url,status,error=None):
        self.db.execute('INSERT INTO urls VALUES(?,?,1,?,?) ON CONFLICT(url) DO UPDATE SET status=excluded.status,attempts=attempts+1,error=excluded.error,updated=excluded.updated',(url,status,error,time.time()));self.db.commit()
    def add(self,r,review_update=False):
        errors=validate(r)
        if errors:raise ValueError(', '.join(errors))
        content=json.dumps([r['dish'],r['components'],r['technique']],sort_keys=True,ensure_ascii=False)
        digest=hashlib.sha256(content.encode()).hexdigest()
        duplicate=self.db.execute('SELECT id FROM records WHERE digest=? AND id!=?',(digest,r['id'])).fetchone()
        if duplicate:
            self.db.execute('INSERT OR IGNORE INTO duplicates VALUES(?,?,?)',(r['id'],duplicate[0],'identical_content'))
        # A recrawl must never silently overwrite a reviewed record.
        old=self.db.execute('SELECT data FROM records WHERE id=?',(r['id'],)).fetchone()
        if old and json.loads(old[0])['review']['status']=='approved' and not review_update:return
        self.db.execute('INSERT OR REPLACE INTO records VALUES(?,?,?,?)',(r['id'],r['source'],digest,json.dumps(r,ensure_ascii=False)));self.db.commit()
    def records(self):
        for row in self.db.execute('SELECT data FROM records ORDER BY id'):yield json.loads(row[0])
    def close(self):self.db.close()

class Fetcher:
    """Async host-isolated pooled HTTP; no browser impersonation or block bypass."""
    def __init__(self,hosts,store):
        self.hosts=set(hosts);self.store=store;self.locks={};self.sessions={};self.robots={};self.blocked=set()
    def session(self,host):
        if host not in self.sessions:
            s=requests.Session();s.headers.update({'User-Agent':USER_AGENT,'Accept-Language':'en','Accept':'application/json, application/xml, text/html;q=0.9, */*;q=0.5'});self.sessions[host]=s
        return self.sessions[host]
    def raw(self,url):
        # Redirects remain explicit so requests never leaves the configured host list.
        for _ in range(6):
            host=urlsplit(url).hostname
            if host not in self.hosts or urlsplit(url).scheme!='https':raise ValueError('URL outside configured HTTPS hosts')
            with self.session(host).get(url,timeout=(10,35),allow_redirects=False,stream=True) as response:
                if response.is_redirect:
                    target=urljoin(url,response.headers['Location'])
                    if urlsplit(target).hostname!=host:raise ValueError('Cross-host redirect requires a separate source configuration')
                    url=target;continue
                body=bytearray()
                for chunk in response.iter_content(65536):
                    body.extend(chunk)
                    if len(body)>16*1024*1024:raise ValueError('Response too large; use bulk local import')
                return response.status_code,response.headers,bytes(body),url
        raise ValueError('Too many redirects')
    async def get(self,url):
        host=urlsplit(url).hostname
        if host not in self.hosts or urlsplit(url).scheme!='https':raise ValueError('Unapproved source host')
        async with self.locks.setdefault(host,asyncio.Lock()):
            if host in self.blocked:raise ValueError('Host stopped after access refusal')
            if host not in self.robots:
                status,headers,body,_=await asyncio.to_thread(self.raw,'https://'+host+'/robots.txt')
                robot=RobotFileParser()
                if status==404:robot.parse([])
                elif status==200:robot.parse(body.decode('utf-8','replace').splitlines())
                else:raise ValueError('Cannot establish robots policy; retry later')
                self.robots[host]=robot
            robot=self.robots[host]
            if not robot.can_fetch(USER_AGENT,url):raise PermissionError('Disallowed by robots.txt')
            delay=max(random.uniform(.8,2.2),robot.crawl_delay(USER_AGENT) or 0)
            for attempt in range(5):
                await asyncio.sleep(delay)
                status,headers,body,final=await asyncio.to_thread(self.raw,url)
                if status==403:
                    self.blocked.add(host);raise PermissionError('403: host stopped; no identity rotation')
                if status==429 or status>=500:
                    retry=headers.get('Retry-After','')
                    if retry.isdigit() and int(retry)>60:raise ValueError('Retry-After exceeds this run; resume later')
                    delay=max(2**(attempt+1),int(retry) if retry.isdigit() else 0)
                    continue
                if status!=200:raise ValueError('HTTP '+str(status))
                return body,final
            raise ValueError('Retry budget exhausted')
    def close(self):
        for s in self.sessions.values():s.close()

def open_text(path):
    path=Path(path)
    opener=gzip.open if path.suffix=='.gz' else bz2.open if path.suffix=='.bz2' else open
    return opener(path,'rt',encoding='utf-8-sig')

def json_array(stream):
    """Streaming top-level JSON array, retaining at most one record + 64K."""
    decoder=json.JSONDecoder();buffer='';started=False;need_value=True;ended=False
    while True:
        chunk=stream.read(65536);buffer+=chunk
        while True:
            buffer=buffer.lstrip()
            if not started:
                if not buffer:break
                if buffer[0]!='[':raise ValueError('Expected a JSON array; use JSONL for line records')
                buffer=buffer[1:];started=True;continue
            if ended:
                if buffer.strip():raise ValueError('Trailing data')
                break
            if not buffer:break
            if buffer[0]==']':
                if need_value and getattr(stream,'_atelier_had_value',False):raise ValueError('Trailing comma')
                ended=True;buffer=buffer[1:];continue
            if not need_value:
                if buffer[0]!=',':raise ValueError('Expected comma')
                buffer=buffer[1:];need_value=True;continue
            try:item,end=decoder.raw_decode(buffer)
            except json.JSONDecodeError:
                if not chunk:raise
                break
            if not isinstance(item,dict):raise ValueError('Each recipe must be an object')
            yield item;buffer=buffer[end:];need_value=False
            stream._atelier_had_value=True
        if not chunk:
            if not ended:raise ValueError('Truncated JSON array')
            return

def bulk_rows(path,fmt):
    if fmt=='parquet':
        try:import pyarrow.parquet as pq
        except ImportError:raise RuntimeError('Parquet requires optional pyarrow: pip install pyarrow')
        for batch in pq.ParquetFile(path).iter_batches(batch_size=256):yield from batch.to_pylist()
        return
    with open_text(path) as stream:
        if fmt=='json':yield from json_array(stream)
        elif fmt=='jsonl':
            for line in stream:
                if line.strip():yield json.loads(line)
        elif fmt=='csv':yield from csv.DictReader(stream)

def corpus_record(row,publisher,license_name):
    # Recipe1M/RecipeBox/RecipeNLG and named-column Kaggle exports. Never eval strings.
    def field(name,alternate):
        value=row.get(name,row.get(alternate))
        if isinstance(value,str) and value.lstrip().startswith('['):
            try:return json.loads(value)
            except ValueError:return [value]
        return value
    url=row.get('url') or row.get('link') or row.get('source')
    if isinstance(url,str) and not url.startswith(('http://','https://')) and '.' in url.split('/')[0]:url='https://'+url
    mapped={'name':row.get('title') or row.get('name'), 'recipeIngredient':field('ingredients','recipeIngredient'),
            'recipeInstructions':field('instructions','directions') or row.get('recipeInstructions'),
            'recipeYield':row.get('recipeYield') or row.get('yield'),
            'prepTime':row.get('prepTime'),'cookTime':row.get('cookTime'),'totalTime':row.get('totalTime'),
            'author':row.get('author'),'recipeCuisine':row.get('recipeCuisine')}
    return from_schema(mapped,url,publisher,license_name)

def wiki_rows(path):
    # Official pages-articles XML (.bz2/.gz supported). Complex templates are not
    # guessed: retained as raw source for review, with no automatic promotion.
    with open_text(path) as stream:
        for event,elem in ET.iterparse(stream,events=('end',)):
            if elem.tag.split('}')[-1]!='page':continue
            title=next((x.text for x in elem if x.tag.endswith('title')), '') or ''
            if title.startswith('Cookbook:'):
                body=next((x.text for x in elem.iter() if x.tag.endswith('text')), '') or ''
                sections=re.split(r'(?m)^==+\s*(.*?)\s*==+\s*$',body)
                ingredients=[];method=[]
                for i in range(1,len(sections),2):
                    heading,content=sections[i].lower(),sections[i+1]
                    if heading=='ingredients':ingredients=[line.lstrip('* ').strip() for line in content.splitlines() if line.startswith('*')]
                    if heading in ('procedure','preparation','method','directions'):method=[line.lstrip('# ').strip() for line in content.splitlines() if line.startswith('#')]
                if ingredients or method:
                    r=from_schema({'name':title.removeprefix('Cookbook:'),'recipeIngredient':ingredients,'recipeInstructions':method},'https://en.wikibooks.org/wiki/'+quote(title.replace(' ','_'),safe=':'),'Wikibooks contributors','CC-BY-SA-4.0; verify page exceptions')
                    r['raw_wikitext']=body;r['review']['issues'].append('wikitext_requires_review')
                    r['attribution_url']=r['source']+'?action=history'
                    yield r
            elem.clear()

async def crawl_page(url,source,fetcher,store):
    url=canonical_url(url)
    if not url or store.seen(url):return
    try:
        body,final=await fetcher.get(url)
        parser=RecipeJSONLD();parser.feed(body.decode('utf-8','replace'))
        count=0
        for node in parser.recipes():
            r=from_schema(node,final,source['publisher'],source.get('license'))
            # Multiple Recipe objects on one page remain distinct.
            r['id']+='-'+hashlib.sha256(r['dish'].encode()).hexdigest()[:8]
            r['rights']['redistribution_confirmed']=source.get('redistribution_confirmed',False)
            store.add(r);count+=1
        if parser.errors and not count:raise ValueError('Malformed recipe JSON-LD')
        store.mark(url,'processed' if count else 'no_recipe')
    except PermissionError as e:store.mark(url,'blocked',str(e))
    except (ValueError,requests.RequestException,ET.ParseError) as e:store.mark(url,'failed',str(e))

async def spider(source,fetcher,store,limit):
    queue=list(source.get('sitemaps',[]));visited=set();selected=set()
    while queue and len(visited)<100 and len(selected)<limit:
        sitemap=queue.pop(0)
        if sitemap in visited:continue
        visited.add(sitemap)
        try:
            body,_=await fetcher.get(sitemap)
            if body[:2]==b'\x1f\x8b':body=gzip.decompress(body)
            tree=ET.fromstring(body)
            urls=[e.text.strip() for e in tree.iter() if e.tag.split('}')[-1]=='loc' and e.text]
            if tree.tag.split('}')[-1]=='sitemapindex':queue.extend(u for u in urls if urlsplit(u).hostname in fetcher.hosts)
            else:
                for url in urls:
                    url=canonical_url(url)
                    if url and urlsplit(url).hostname in fetcher.hosts and not store.seen(url) and re.search(r'/recipes?/|/\d{4}/\d{2}/|-recipe(?:-|/|$)',url):selected.add(url)
                    if len(selected)>=limit:break
            store.mark(sitemap,'sitemap_read')
        except (ValueError,PermissionError,requests.RequestException,ET.ParseError) as e:store.mark(sitemap,'failed',str(e))
    # Bounded tasks; per-host locks serialize requests and preserve pacing.
    pending=iter(sorted(selected))
    async def worker():
        for url in pending:await crawl_page(url,source,fetcher,store)
    await asyncio.gather(*(worker() for _ in range(4)))

async def mealdb(fetcher,store,limit,extended):
    base='https://www.themealdb.com/api/json/v1/1/'
    ids=set();count=0
    async def read(endpoint):
        body,_=await fetcher.get(base+endpoint);return json.loads(body).get('meals') or []
    for letter in string.ascii_lowercase:
        rows=await read('search.php?f='+letter)
        for m in rows:
            url=base+'lookup.php?i='+str(m['idMeal']);ids.add(str(m['idMeal']))
            if store.seen(url):continue
            store.add(from_meal(m));store.mark(url,'processed');count+=1
            if count>=limit:return
    if extended:
        for kind,field in [('c','strCategory'),('a','strArea')]:
            for group in await read('list.php?'+kind+'=list'):
                for m in await read('filter.php?'+kind+'='+quote(group[field])):ids.add(str(m['idMeal']))
        for mid in sorted(ids):
            url=base+'lookup.php?i='+mid
            if store.seen(url):continue
            for row in await read('lookup.php?i='+mid):store.add(from_meal(row))
            store.mark(url,'processed');count+=1
            if count>=limit:return

def atomic_json(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+'.tmp')
    with temp.open('w',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
    if path.exists():
        backup=ROOT/'backups'/f'{path.name}.{time.time_ns()}.bak'
        backup.parent.mkdir(exist_ok=True);shutil.copy2(path,backup)
    os.replace(temp,path)

def migrate(path):
    # Backup BEFORE transformation. The original is the authority for recovery.
    path=Path(path);backup=ROOT/'backups'/f'{path.name}.pre-schema-v2.{time.time_ns()}.bak'
    backup.parent.mkdir(exist_ok=True);shutil.copy2(path,backup)
    old=json.loads(path.read_text(encoding='utf-8-sig'));out=[]
    for index,item in enumerate(old):
        if item.get('schema_version')==2:out.append(item);continue
        r=empty_record(item.get('dish',''),item.get('source'),item.get('restaurant',''))
        r.update({k:v for k,v in item.items() if k in r and k not in ('yield','timing','dietary','components','provenance','source')})
        r['id']=str(item.get('id') or r['id']);r['legacy_original_source']=item.get('source')
        r['provenance']='gc_ms_synthesis' if r['id'].startswith('mol-') else 'adapted_publisher'
        r['review']['issues']=['legacy_unverified'];r['legacy']=True
        for c in item.get('components',[]):
            comp=parse_ingredient(f"{c.get('qty','')} {c.get('unit','')} {c.get('name','')}")
            # Retain the original amount as evidence, not as a verified measure.
            comp.update(name=c.get('name',''),qty=c.get('qty'),unit=c.get('unit') or 'unspecified',dept=c.get('dept') or 'pantry',quantity_status='legacy_unverified')
            r['components'].append(comp)
        finalize(r)
        errors=validate(r)
        if errors:raise ValueError(f'Record {index}: {errors}; original remains unchanged')
        out.append(r)
    atomic_json(path,out)
    return {'records':len(out),'backup':str(backup),'sha256':hashlib.sha256(backup.read_bytes()).hexdigest()}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--db',default=str(ROOT/'.ingestion/seen_urls.db'))
    sub=p.add_subparsers(dest='command',required=True)
    imp=sub.add_parser('import');imp.add_argument('path');imp.add_argument('--format',choices=['json','jsonl','csv','parquet','wikimedia'],required=True);imp.add_argument('--publisher',required=True);imp.add_argument('--license',required=True)
    cr=sub.add_parser('crawl');cr.add_argument('source');cr.add_argument('--limit',type=int,default=25);cr.add_argument('--extended',action='store_true');cr.add_argument('--url',action='append',default=[])
    exp=sub.add_parser('export');exp.add_argument('path');exp.add_argument('--approved-only',action='store_true')
    sub.add_parser('accept-reviewed').add_argument('path',help='A manually reviewed master-schema JSON array; documented reviewer and rights required')
    mig=sub.add_parser('migrate');mig.add_argument('path')
    val=sub.add_parser('validate');val.add_argument('path')
    sub.add_parser('report')
    args=p.parse_args()
    if args.command=='migrate':print(json.dumps(migrate(args.path),indent=2));return
    if args.command=='validate':
        errors=[];seen=set()
        for index,r in enumerate(bulk_rows(args.path,'json')):
            problems=validate(r)
            if r.get('id') in seen:problems.append('duplicate_id')
            seen.add(r.get('id'))
            if problems:errors.append({'index':index,'issues':problems})
        print(json.dumps({'records':len(seen),'errors':errors},indent=2));raise SystemExit(bool(errors))
    store=Store(args.db)
    try:
        if args.command=='import':
            rows=wiki_rows(args.path) if args.format=='wikimedia' else (corpus_record(row,args.publisher,args.license) for row in bulk_rows(args.path,args.format))
            count=0
            for r in rows:store.add(r);count+=1
            print(json.dumps({'imported':count,'status':'needs_review'}))
        elif args.command=='crawl':
            if args.limit<1 or args.limit>10000:raise ValueError('Limit must be 1–10000')
            sources=json.loads((ROOT/'ingestion/sources.json').read_text())
            source=sources[args.source]
            if not source.get('enabled'):raise ValueError('Source disabled pending access/rights review; see sources.json')
            fetcher=Fetcher(source['hosts'],store)
            async def run():
                if args.source=='themealdb':await mealdb(fetcher,store,args.limit,args.extended)
                elif args.url:
                    for url in args.url[:args.limit]:await crawl_page(url,source,fetcher,store)
                else:await spider(source,fetcher,store,args.limit)
            try:asyncio.run(run())
            finally:fetcher.close()
            print(json.dumps({'records_in_queue':store.db.execute('SELECT count(*) FROM records').fetchone()[0],
                              'url_status':dict(store.db.execute('SELECT status,count(*) FROM urls GROUP BY status')),
                              'recent_failures':list(store.db.execute("SELECT url,error FROM urls WHERE status IN ('failed','blocked') ORDER BY updated DESC LIMIT 5"))},indent=2))
        elif args.command=='accept-reviewed':
            reviewed=list(bulk_rows(args.path,'json'))
            for r in reviewed:
                errors=validate(r)
                if errors or not r.get('cookable') or not r['review'].get('reviewer') or not r['review'].get('reviewed_at') or not r['rights']['redistribution_confirmed']:
                    raise ValueError('Reviewed file contains an incomplete or undocumented record: '+str(r.get('id')))
            for r in reviewed:store.add(r,review_update=True)
            print(json.dumps({'accepted':len(reviewed)}))
        elif args.command=='export':
            rows=store.records()
            if args.approved_only:rows=(r for r in rows if r['cookable'] and r['rights']['redistribution_confirmed'] and not validate(r))
            rows=list(rows)
            if Path(args.path).resolve()==(ROOT/'recipes.json').resolve():
                if not args.approved_only:raise ValueError('Review exports must not replace the public catalog')
                if not rows:raise ValueError('No approved recipes to merge; catalog unchanged')
                existing=json.loads((ROOT/'recipes.json').read_text(encoding='utf-8'))
                merged={r['id']:r for r in existing};merged.update({r['id']:r for r in rows});rows=list(merged.values())
                if any(validate(r) for r in rows):raise ValueError('Catalog validation failed; unchanged')
            atomic_json(args.path,rows)
        elif args.command=='report':
            print(json.dumps({'records':store.db.execute('SELECT count(*) FROM records').fetchone()[0], 'urls':dict(store.db.execute('SELECT status,count(*) FROM urls GROUP BY status')), 'duplicates':store.db.execute('SELECT count(*) FROM duplicates').fetchone()[0]},indent=2))
    finally:store.close()

if __name__=='__main__':main()
