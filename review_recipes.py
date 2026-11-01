"""Read-only recipe audit: flags uncertainty; never manufactures replacement values."""
import json, collections
from pathlib import Path

def audit():
    data=json.loads(Path('recipes.json').read_text(encoding='utf-8'))
    names=collections.Counter(str(r.get('dish','')).casefold() for r in data if isinstance(r,dict))
    findings=[]
    for index,r in enumerate(data):
        issues=[]
        if not isinstance(r,dict):
            findings.append({'index':index,'issues':['invalid_record']}); continue
        if not r.get('servings') and not r.get('yield'): issues.append('missing_original_yield')
        if not r.get('technique'): issues.append('missing_instructions')
        elif len(r['technique']) in (800,1000,1200): issues.append('possible_instruction_truncation')
        if names[str(r.get('dish','')).casefold()]>1: issues.append('duplicate_title_requires_review')
        if str(r.get('id','')).startswith('mol-'): issues.append('experimental_synthesis_not_verified')
        if not str(r.get('source','')).startswith(('http://','https://')): issues.append('source_url_unavailable')
        for c in r.get('components',[]):
            q=c.get('qty')
            if not isinstance(q,(int,float)) or q<=0: issues.append('invalid_quantity')
            if q==50: issues.append('possible_50_quantity_fallback')
            if c.get('unit') not in ('g','ml','pcs'): issues.append('unit_requires_review')
        findings.append({'id':r.get('id'),'dish':r.get('dish'),'issues':sorted(set(issues))})
    counts=collections.Counter(issue for r in findings for issue in r['issues'])
    report={'records':len(data),'issue_counts':dict(counts),'duplicate_titles':{n:c for n,c in names.items() if c>1},'findings':findings,'policy':'Flags are review leads, not proof that quantities are wrong. Original catalog remains unchanged; legacy entries are excluded from the new generator.'}
    Path('data-review.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({'records':len(data),'issue_counts':dict(counts)},indent=2))
if __name__=='__main__': audit()
