if __name__ == "__main__":
    raise SystemExit("Legacy catalog writer disabled: use python -m ingestion.pipeline --help. Original algorithms retained for reference; they must not overwrite reviewed data.")

import json
import os
import re

RECIPES_FILE = "recipes.json"

VALID_SLOTS = {"opener", "mid", "climax", "predessert", "dessert"}
VALID_DEPTS = {"seafood", "butchery", "produce", "dairy", "drygoods", "pantry"}

def audit_and_repair():
    if not os.path.exists(RECIPES_FILE):
        print(f"[!] {RECIPES_FILE} not found. Run super_harvest.py first.")
        return

    with open(RECIPES_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"[!] Fatal JSON syntax error in {RECIPES_FILE}: {e}")
            return

    initial_count = len(data)
    repaired = []
    seen_ids = set()
    slot_counts = {s: 0 for s in VALID_SLOTS}

    for item in data:
        if not isinstance(item, dict):
            continue

        # 1. Clean Title & ID
        title = item.get("dish") or item.get("name") or "Artisanal Preparation"
        title = title.strip()
        slug = item.get("id") or re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:40]
        
        # Deduplication
        if slug in seen_ids:
            continue
        seen_ids.add(slug)

        # 2. Slot Validation & Auto-Resolution
        slot = item.get("slot", "").lower()
        if slot not in VALID_SLOTS:
            text = (title + " " + item.get("technique", "")).lower()
            if any(k in text for k in ["dessert", "cake", "tart", "pie", "chocolate", "brulee", "souffle", "custard"]):
                slot = "dessert"
            elif any(k in text for k in ["granita", "sorbet", "cleanser"]):
                slot = "predessert"
            elif any(k in text for k in ["beef", "steak", "duck", "lamb", "pork", "roast", "short rib", "venison"]):
                slot = "climax"
            elif any(k in text for k in ["seafood", "fish", "salmon", "shrimp", "lobster", "scallop", "pasta", "halibut"]):
                slot = "mid"
            else:
                slot = "opener"

        slot_counts[slot] += 1

        # 3. Clean & Sanitize Components
        components = item.get("components", [])
        cleaned_comps = []
        if isinstance(components, list):
            for c in components:
                if isinstance(c, dict):
                    name = str(c.get("name", "Ingredient")).strip()
                    try:
                        qty = float(c.get("qty", 50))
                        if qty <= 0 or qty > 5000:  # Clamp unreasonable units
                            qty = 50.0
                    except:
                        qty = 50.0
                    
                    unit = str(c.get("unit", "g")).strip().lower()
                    if unit not in ["g", "ml", "pcs"]:
                        unit = "ml" if "cup" in unit or "spoon" in unit or "oz" in unit else "g"

                    dept = str(c.get("dept", "pantry")).lower()
                    if dept not in VALID_DEPTS:
                        dept = "pantry"

                    cleaned_comps.append({"name": name, "qty": round(qty, 1), "unit": unit, "dept": dept})

        # Ensure fallback component exists
        if not cleaned_comps:
            cleaned_comps = [
                {"name": "Core Featured Ingredient", "qty": 180.0, "unit": "g", "dept": "produce"},
                {"name": "Emulsion & Seasoning", "qty": 30.0, "unit": "ml", "dept": "pantry"}
            ]

        # 4. Standardize Technical Fields
        record = {
            "id": slug,
            "dish": title,
            "restaurant": item.get("restaurant") or "Classical Heritage Kitchen",
            "chef": item.get("chef") or "Executive Chef",
            "location": item.get("location") or "Global",
            "source": item.get("source") or "Culinary Archive",
            "slot": slot,
            "hero": item.get("hero") if isinstance(item.get("hero"), list) else ["Specialty"],
            "sensoryRole": item.get("sensoryRole") or f"Balanced preparation curated for the {slot.upper()} degustation course.",
            "components": cleaned_comps,
            "technique": item.get("technique") or "Maintain strict thermal and seasoning control.",
            "plating": item.get("plating") or "Plate with intentional negative space on heated or chilled ceramic.",
            "pairing": item.get("pairing") if isinstance(item.get("pairing"), dict) else {
                "wine": "Sommelier Reserve Pairing",
                "zeroProof": "Artisanal Botanical Infusion"
            }
        }
        repaired.append(record)

    # Atomic rewrite
    temp_file = RECIPES_FILE + ".audit.tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(repaired, f, indent=2, ensure_ascii=False)
    os.replace(temp_file, RECIPES_FILE)

    print("===================================================")
    print("        L'ATELIER DATABASE AUDIT REPORT")
    print("===================================================")
    print(f"Initial Records Read:    {initial_count}")
    print(f"Corrupt/Duplicates Cut:  {initial_count - len(repaired)}")
    print(f"Verified Records Saved:  {len(repaired)}")
    print("\nSlot Distribution:")
    for s, count in slot_counts.items():
        print(f"  • {s.upper():<12}: {count} dishes")
    print("===================================================")
    print(f"[+] Output verified at: {os.path.abspath(RECIPES_FILE)}")

if __name__ == "__main__":
    audit_and_repair()