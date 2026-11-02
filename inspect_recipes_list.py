import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data-recipes.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.MASTER_RECIPES\s*=\s*(\[.*?\]);', text, re.DOTALL)
recipes = json.loads(m.group(1))

print(f"Total current recipes: {len(recipes)}")
existing_ids = {r['id']: r['title'] for r in recipes}

print("\nCurrent desserts:")
for r in recipes:
    if r.get('category') == 'dessert' or r.get('slot') in ['dessert', 'predessert']:
        print(f"  {r['id']}: {r['title']}")

print("\nCurrent breakfast / brunch:")
for r in recipes:
    if r.get('category') in ['breakfast', 'brunch']:
        print(f"  {r['id']}: {r['title']}")
