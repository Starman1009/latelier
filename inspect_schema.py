import json, re

with open('data-recipes.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.MASTER_RECIPES\s*=\s*(\[.*?\]);', text, re.DOTALL)
if m:
    recipes = json.loads(m.group(1))
    sample = recipes[0]
    print("Schema keys:", list(sample.keys()))
    print("Sample keys count:", len(sample.keys()))
