import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

from build_mega_recipes import MEGA_RECIPES
from recipes_data_part2 import PART_2_RECIPES
from recipes_data_part3 import PART_3_RECIPES
from recipes_data_part4 import PART_4_RECIPES
from recipes_data_part5 import PART_5_RECIPES
from recipes_data_part6 import PART_6_RECIPES

REQUIRED_FIELDS = [
    'id', 'title', 'cuisine', 'category', 'slot', 'difficulty', 'prepMins', 'cookMins',
    'totalMins', 'yieldServings', 'heroImage', 'summary', 'dietary', 'sensoryRole',
    'ingredients', 'equipment', 'miseEnPlace', 'steps', 'sensoryIndicators', 'scienceNotes',
    'troubleshooting', 'substitutions', 'flavorPairings', 'advancedTechnique',
    'storageAndReheating', 'nutritionEstimates', 'relatedRecipes', 'relatedTechniques'
]

def run_merge():
    with open('data-recipes.js', 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'window\.MASTER_RECIPES\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not m:
        print("ERROR: Could not locate window.MASTER_RECIPES in data-recipes.js")
        return

    existing = json.loads(m.group(1))
    print(f"Existing recipes count: {len(existing)}")
    existing_ids = {r['id'] for r in existing}

    all_candidates = MEGA_RECIPES + PART_2_RECIPES + PART_3_RECIPES + PART_4_RECIPES + PART_5_RECIPES + PART_6_RECIPES
    print(f"Total candidate recipes created: {len(all_candidates)}")

    added_count = 0
    validated_count = 0

    for r in all_candidates:
        # Validate fields
        missing = [f for f in REQUIRED_FIELDS if f not in r]
        if missing:
            print(f"Recipe {r.get('id')} missing fields: {missing}")
            continue

        validated_count += 1
        if r['id'] not in existing_ids:
            existing.append(r)
            existing_ids.add(r['id'])
            added_count += 1
        else:
            print(f"Skipping existing id: {r['id']}")

    print(f"Successfully validated {validated_count} candidate recipes.")
    print(f"Added {added_count} brand-new unique recipes.")
    print(f"Total recipes now in master library: {len(existing)}")

    # Replace in file
    updated_js = re.sub(
        r'window\.MASTER_RECIPES\s*=\s*\[.*?\];',
        'window.MASTER_RECIPES = ' + json.dumps(existing, indent=2, ensure_ascii=False) + ';',
        content,
        flags=re.DOTALL
    )

    with open('data-recipes.js', 'w', encoding='utf-8') as f:
        f.write(updated_js)

    print("data-recipes.js updated and written successfully!")

if __name__ == '__main__':
    run_merge()
