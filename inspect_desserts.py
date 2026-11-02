import json, re

with open('data-recipes.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.MASTER_RECIPES\s*=\s*(\[.*?\]);', text, re.DOTALL)
if m:
    recipes = json.loads(m.group(1))
    desserts = [r for r in recipes if r.get('category') == 'dessert']
    print(f"Total Desserts: {len(desserts)}")
    for d in desserts:
        print(f"  {d['id']}: {d['title']}")
