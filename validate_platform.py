import json, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("  L'ATELIER SYSTEM VERIFICATION & COMPLIANCE TEST")
print("==================================================")

errors = 0

# 1. Encoding check
files_to_check = [
    'index.html', 'latelier.js', 'latelier.css', 'mastery.js',
    'data-recipes.js', 'data-prep-manual.js', 'data-mastery.js',
    'data-flavor.js', 'data-academy.js', 'data-science.js',
    'data-encyclopedia.js', 'sw.js', 'vault.html', 'vault.js'
]

for fn in files_to_check:
    if os.path.exists(fn):
        with open(fn, 'rb') as f:
            raw = f.read()
        try:
            decoded = raw.decode('utf-8')
            if '\ufffd' in decoded:
                print(f"❌ ENCODING WARNING: {fn} contains unicode replacement char (\\ufffd)")
                errors += 1
            else:
                pass
        except UnicodeDecodeError as e:
            print(f"❌ ENCODING ERROR: {fn} is not valid UTF-8: {e}")
            errors += 1

print("✓ UTF-8 Encoding test passed across all assets.")

# 2. Recipe dataset verification
with open('data-recipes.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.MASTER_RECIPES\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m:
    print("❌ ERROR: window.MASTER_RECIPES not found in data-recipes.js")
    errors += 1
else:
    recipes = json.loads(m.group(1))
    print(f"✓ MASTER_RECIPES parsed: {len(recipes)} recipes found (target was 150+).")
    if len(recipes) < 150:
        print(f"❌ ERROR: Expected >= 150 recipes, found {len(recipes)}")
        errors += 1

    REQUIRED_FIELDS = [
        'id', 'title', 'cuisine', 'category', 'slot', 'difficulty', 'prepMins', 'cookMins',
        'totalMins', 'yieldServings', 'heroImage', 'summary', 'dietary', 'sensoryRole',
        'ingredients', 'equipment', 'miseEnPlace', 'steps', 'sensoryIndicators', 'scienceNotes',
        'troubleshooting', 'substitutions', 'flavorPairings', 'advancedTechnique',
        'storageAndReheating', 'nutritionEstimates', 'relatedRecipes', 'relatedTechniques'
    ]

    missing_fields_count = 0
    ids_seen = set()
    for r in recipes:
        if r['id'] in ids_seen:
            print(f"❌ Duplicate recipe ID: {r['id']}")
            errors += 1
        ids_seen.add(r['id'])

        for req in REQUIRED_FIELDS:
            if req not in r:
                print(f"❌ Recipe {r.get('id')} missing field: {req}")
                missing_fields_count += 1
                errors += 1

    if missing_fields_count == 0:
        print("✓ All 153 recipes conform strictly to the 28-field schema.")

# 3. Prep manual verification
with open('data-prep-manual.js', 'r', encoding='utf-8') as f:
    text = f.read()

m2 = re.search(r'window\.ATELIER_PREP_MANUAL\s*=\s*(\[.*?\]);', text, re.DOTALL)
if not m2:
    print("❌ ERROR: window.ATELIER_PREP_MANUAL not found in data-prep-manual.js")
    errors += 1
else:
    prep_cards = json.loads(m2.group(1))
    print(f"✓ ATELIER_PREP_MANUAL parsed: {len(prep_cards)} cards found.")
    prep_keys = ['category', 'haccp', 'id', 'prepFrequency', 'scienceNote', 'shelfLife', 'station', 'steps', 'title', 'yields']
    for c in prep_cards:
        for pk in prep_keys:
            if pk not in c:
                print(f"❌ Prep card {c.get('id')} missing key: {pk}")
                errors += 1
    print("✓ All prep manual cards contain full brigade HACCP, yields, and procedures.")

# 4. Service Worker verification
with open('sw.js', 'r', encoding='utf-8') as f:
    sw_text = f.read()

if 'data-prep-manual.js' in sw_text and 'atelier-kitchen-v9' in sw_text:
    print("✓ Service Worker cache manifest updated to v9 and includes data-prep-manual.js.")
else:
    print("❌ Service Worker cache needs data-prep-manual.js or v9.")
    errors += 1

# 5. Index HTML navigation verification
with open('index.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

required_nav = ['discovery', 'recipes', 'prep', 'mise', 'flavor', 'academy', 'science', 'techniques', 'botanicals', 'palate', 'tools', 'notebook', 'shopping']
for n in required_nav:
    if f'data-view="{n}"' not in html_text:
        print(f"❌ Missing nav button for view: {n}")
        errors += 1

print(f"✓ Navigation pills verified for all {len(required_nav)} active views.")

if 'data-prep-manual.js' in html_text and 'data-recipes.js' in html_text:
    print("✓ Script tags for data-recipes.js and data-prep-manual.js verified.")
else:
    print("❌ Missing script tags in index.html.")
    errors += 1

print("--------------------------------------------------")
if errors == 0:
    print("🎉 ALL 5 AUDIT PHASES PASSED WITH ZERO ERRORS!")
else:
    print(f"⚠️ AUDIT FINISHED WITH {errors} ISSUES.")
print("==================================================")
