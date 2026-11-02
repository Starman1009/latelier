"""Encrypt user-provided manuals. Password read from stdin; never stored in source."""
import base64, hashlib, json, os, re, sys
from pathlib import Path
import pymupdf
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT=Path(__file__).resolve().parent
NAMES=['SAUCE','LINESET','PROTEIN','PRODUCE','BAKE','BRUNCH','DESSERTS','OVENS','PANFRY','ENTREE','SALADS','APPETIZERS']
def build(password):
    out=ROOT/'private-vault';out.mkdir(exist_ok=True)
    salt=os.urandom(16); key=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=600000).derive(password.encode())
    def seal(data,path):
        nonce=os.urandom(12);path.write_bytes(nonce+AESGCM(key).encrypt(nonce,data,b'latelier-vault-v1'))
    manuals=[];seen={};aliases=[]
    for name in NAMES:
        path=Path.home()/'Downloads'/f'{name} USA P10 2026.pdf'
        if name=='APPETIZERS':path=path.with_name('APPETIZERS USA P10 2026 (1).pdf')
        raw=path.read_bytes();digest=hashlib.sha256(raw).hexdigest()
        doc=pymupdf.open(stream=raw,filetype='pdf');mid=hashlib.sha256(raw).hexdigest()[:24];pages=[]
        for n,page in enumerate(doc):
            text=page.get_text(sort=True)
            links=[x['uri'] for x in page.get_links() if x.get('uri','').startswith(('https://','http://'))]
            links+=re.findall(r'https?://[^\s<>]+',text)
            title=next((x.strip() for x in text.splitlines() if x.strip()),f'Page {n+1}')
            pages.append({'number':n+1,'title':title,'text':text,'links':list(dict.fromkeys(links))})
        seal(raw,out/(mid+'.bin'));manuals.append({'id':mid,'name':path.name,'pages':pages,'sha256':digest,'bytes':len(raw)})
        seen[digest]=mid
    duplicate=Path.home()/'Downloads'/'DESSERTS USA P10 2026 (1).pdf'
    digest=hashlib.sha256(duplicate.read_bytes()).hexdigest()
    if digest not in seen:raise ValueError('Dessert copies differ; must import both explicitly')
    aliases.append({'name':duplicate.name,'sameAs':seen[digest]})
    payload={'manuals':manuals,'aliases':aliases}
    seal(json.dumps(payload,ensure_ascii=False).encode(),out/'index.bin')
    (out/'config.json').write_text(json.dumps({'version':1,'salt':base64.b64encode(salt).decode(),'iterations':600000}),encoding='utf-8')
    print(json.dumps({'manuals':len(manuals),'duplicateAliases':len(aliases),'pages':sum(len(m['pages']) for m in manuals),'links':sum(len(p['links']) for m in manuals for p in m['pages'])}))
if __name__=='__main__':build(sys.stdin.readline().rstrip('\r\n'))
