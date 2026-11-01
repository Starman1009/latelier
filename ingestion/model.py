"""Loss-aware normalization to the L'Atelier master record."""
import hashlib
import html
import math
import re
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urlsplit, urlunsplit
from .ingredients import parse_ingredient

PROVENANCE = {'verified_sourced','adapted_publisher','user_created','gc_ms_synthesis'}
SLOTS = {'opener','mid','climax','predessert','dessert'}
SCHEMA_VALIDATOR=Draft202012Validator(json.loads(Path(__file__).with_name('recipe.schema.json').read_text(encoding='utf-8')))

def canonical_url(value):
    try:
        u=urlsplit(str(value))
        if u.scheme not in ('http','https') or not u.hostname or u.username or u.password:
            return None
        return urlunsplit((u.scheme,u.netloc.lower(),u.path or '/',u.query,''))
    except ValueError:
        return None

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]
    def handle_data(self, data): self.parts.append(data)
    def handle_starttag(self,tag,attrs):
        if tag in ('br','p','li'): self.parts.append('\n')

def plain(value):
    parser=Text(); parser.feed(str(value or ''))
    return html.unescape(''.join(parser.parts)).strip()

def texts(value):
    if value is None: return []
    if isinstance(value,str): return [plain(value)] if value.strip() else []
    if isinstance(value,list): return [v for item in value for v in texts(item)]
    if isinstance(value,dict):
        if value.get('itemListElement'): return texts(value['itemListElement'])
        return texts(value.get('text') or value.get('name'))
    return []

def minutes(value):
    if not isinstance(value,str): return None
    m=re.fullmatch(r'P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?',value)
    if not m or not any(m.groups()): return None
    d,h,mi,s=(int(x or 0) for x in m.groups())
    return d*1440+h*60+mi+s/60

def base_yield(value):
    raw='; '.join(texts(value)) if not isinstance(value,(int,float)) else str(value)
    # No midpoint or guessed servings for ranges or counts of cookies/loaves.
    match=re.fullmatch(r'(?:serves?\s+)?(\d+(?:\.\d+)?)\s*(?:servings?|people|persons?)?',raw,re.I)
    n=float(match[1]) if match else None
    return {'servings':n if n and math.isfinite(n) else None,'raw_yield':raw or None}

def empty_record(title, source, publisher, license_name=None):
    url=canonical_url(source)
    identity=url or (publisher+'|'+title)
    slug=re.sub('[^a-z0-9]+','-',title.lower()).strip('-')[:64] or 'recipe'
    return {
        'id':slug+'-'+hashlib.sha256(identity.encode()).hexdigest()[:12],
        'dish':title,'restaurant':publisher or None,'chef':None,'location':None,'source':url,
        'provenance':'adapted_publisher','yield':{'servings':None,'raw_yield':None},
        'timing':{'prep_mins':None,'cook_mins':None,'total_mins':None},
        'difficulty':None,'slot':None,'hero':[],
        'dietary':{'gluten_free':None,'dairy_free':None,'vegetarian':None,'vegan':None,'allergens':None},
        'sensoryRole':None,'components':[],'equipment':[],'technique':'','plating':None,
        'pairing':{'wine':None,'zeroProof':None},
        'review':{'status':'needs_review','issues':[],'reviewer':None,'reviewed_at':None},
        'rights':{'license':license_name,'redistribution_confirmed':False},
        'retrieved_at':datetime.now(timezone.utc).isoformat(),'cookable':False,
        'occasions':[], 'schema_version':2
    }

def from_schema(data,url,publisher,license_name=None):
    r=empty_record(plain(data.get('name')),url,publisher,license_name)
    r['chef']='; '.join(texts(data.get('author'))) or None
    r['location']='; '.join(texts(data.get('recipeCuisine'))) or None
    r['yield']=base_yield(data.get('recipeYield'))
    r['timing']={k:minutes(data.get(v)) for k,v in [('prep_mins','prepTime'),('cook_mins','cookTime'),('total_mins','totalTime')]}
    r['components']=[parse_ingredient(line) for line in texts(data.get('recipeIngredient'))]
    steps=texts(data.get('recipeInstructions'))
    r['technique']='\n'.join(f'{i+1}. {step}' for i,step in enumerate(steps))
    r['equipment']=texts(data.get('tool'))
    # Preserve source classifications separately; they are not automatically
    # sufficient to assign our course slots or prove allergy suitability.
    r['source_categories']=texts(data.get('recipeCategory'))
    r['source_dietary']=texts(data.get('suitableForDiet'))
    r['source_record']=data
    return finalize(r)

def from_meal(m):
    data={'name':m.get('strMeal'),'recipeCuisine':m.get('strArea'),
          'recipeIngredient':[str(m.get('strMeasure'+str(i)) or '').strip()+' '+str(m.get('strIngredient'+str(i)) or '').strip() for i in range(1,21) if str(m.get('strIngredient'+str(i)) or '').strip()],
          'recipeInstructions':m.get('strInstructions'),'recipeCategory':m.get('strCategory')}
    r=from_schema(data,'https://www.themealdb.com/meal/'+str(m['idMeal']),'TheMealDB')
    r['publisher_url']=canonical_url(m.get('strSource'))
    r['provider_id']=str(m['idMeal'])
    return r

def issues(r):
    found=[]
    if not r.get('dish'): found.append('missing_title')
    y=r.get('yield',{}).get('servings')
    if not isinstance(y,(int,float)) or isinstance(y,bool) or not math.isfinite(y) or y<=0: found.append('missing_valid_yield')
    if not r.get('technique','').strip(): found.append('missing_instructions')
    if not r.get('components'): found.append('missing_ingredients')
    if any(c.get('quantity_status') not in ('specified','to_taste') or not c.get('name') for c in r.get('components',[])): found.append('ambiguous_ingredients')
    if r.get('provenance')!='user_created' and not canonical_url(r.get('source')): found.append('missing_source_url')
    if r.get('provenance')=='gc_ms_synthesis': found.append('experimental_only')
    return found

def finalize(r):
    r['review']['issues']=list(dict.fromkeys(r['review'].get('issues',[])+issues(r)))
    r['cookable']=not r['review']['issues'] and r['review']['status']=='approved'
    return r

def validate(r):
    """Structural validation plus semantic cookability invariants. No coercion."""
    structural=[str(error.json_path)+': '+error.message for error in SCHEMA_VALIDATOR.iter_errors(r)]
    if structural:return structural
    required=set(empty_record('','', ''))
    errors=['missing:'+k for k in sorted(required-set(r))]
    if errors:return errors
    if r['provenance'] not in PROVENANCE: errors.append('invalid_provenance')
    if r['slot'] is not None and r['slot'] not in SLOTS: errors.append('invalid_slot')
    if not isinstance(r['yield'],dict) or set(r['yield'])!={'servings','raw_yield'}:errors.append('invalid_yield_shape')
    if not isinstance(r['components'],list):return errors+['invalid_components']
    for c in r['components']:
        if not isinstance(c,dict) or not {'name','qty','unit','original_measure','dept','preparation','quantity_status'}<=set(c):errors.append('invalid_component');continue
        q=c['qty']
        if q is not None and (isinstance(q,bool) or not isinstance(q,(int,float)) or not math.isfinite(q) or q<=0):errors.append('invalid_quantity')
    for value in r['timing'].values():
        if value is not None and (isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0):errors.append('invalid_time')
    if not errors:
        problems=issues(r)
        if r['cookable'] and (problems or r['review']['issues'] or r['review']['status']!='approved'):errors.append('false_cookable_claim')
        if r['provenance']=='verified_sourced' and (r['review']['status']!='approved' or not r['review'].get('reviewer') or not r['review'].get('reviewed_at')):errors.append('undocumented_verification')
    return errors

class RecipeJSONLD(HTMLParser):
    def __init__(self):super().__init__();self.active=False;self.buffer=[];self.documents=[];self.errors=[]
    def handle_starttag(self,tag,attrs):
        if tag=='script' and dict(attrs).get('type','').lower()=='application/ld+json':self.active=True;self.buffer=[]
    def handle_data(self,data):
        if self.active:self.buffer.append(data)
    def handle_endtag(self,tag):
        if tag=='script' and self.active:
            import json
            try:self.documents.append(json.loads(''.join(self.buffer)))
            except ValueError:self.errors.append('invalid_jsonld')
            self.active=False
    def recipes(self):
        def visit(node):
            if isinstance(node,list):
                for child in node:yield from visit(child)
            elif isinstance(node,dict):
                types=node.get('@type',[]);types=[types] if isinstance(types,str) else types
                if any(t in ('Recipe','https://schema.org/Recipe','http://schema.org/Recipe') for t in types):yield node
                for key in ('@graph','mainEntity','itemListElement'):
                    if key in node:yield from visit(node[key])
        for doc in self.documents:yield from visit(doc)
