import json, re

with open('data-prep-manual.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.ATELIER_PREP_MANUAL\s*=\s*(\[.*?\]);', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print(f"Total prep cards loaded: {len(data)}")
    categories = set(c['category'] for c in data)
    print("Categories:", categories)
    for c in data[:5]:
        print("-", c['id'], "|", c['title'], "|", c['category'])
else:
    print("Could not find window.ATELIER_PREP_MANUAL")
