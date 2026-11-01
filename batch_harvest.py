if __name__ == "__main__":
    raise SystemExit("Legacy catalog writer disabled: use python -m ingestion.pipeline --help. Original algorithms retained for reference; they must not overwrite reviewed data.")

import sys
import os
import re
import json
import time
import unicodedata
import requests
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me, scrape_html

RECIPES_FILE = "recipes.json"

# Automated target queries spanning Michelin institutions and homecook-friendly fine dining
TARGET_QUERIES = [
    # --- The French Laundry & Thomas Keller (Classical Modern) ---
    "Thomas Keller Salmon Cornets recipe",
    "Thomas Keller Oysters and Pearls recipe",
    "Thomas Keller Butter Poached Lobster recipe",
    "Thomas Keller Sweet Potato Agnolotti recipe",
    "Thomas Keller Calotte de Boeuf Bordelaise recipe",
    "Thomas Keller Coffee and Doughnuts beignets recipe",
    
    # --- Le Bernardin & Eric Ripert (Oceanic Mastery) ---
    "Eric Ripert Pounded Tuna Foie Gras recipe",
    "Eric Ripert Steamed Halibut Wild Mushroom Dashi recipe",
    "Eric Ripert Striped Bass Savoy Cabbage recipe",
    "Eric Ripert Barely Cooked Salmon recipe",
    
    # --- Eleven Madison Park & Daniel Humm ---
    "Eleven Madison Park Hamachi Crudo recipe",
    "Eleven Madison Park Roast Duck Lavender Honey recipe",
    "Eleven Madison Park Celery Root Pave recipe",
    
    # --- Osteria Francescana & Massimo Bottura ---
    "Massimo Bottura Memory of a Mortadella Sandwich recipe",
    "Massimo Bottura Five Ages of Parmigiano Reggiano recipe",
    "Massimo Bottura Oops I Dropped the Lemon Tart recipe",
    
    # --- Alinea & Grant Achatz (Modernist) ---
    "Alinea Squab on Cedar branches recipe",
    "Grant Achatz Dark Chocolate Passionfruit recipe",
    
    # --- Accessible Fine Dining for Home Cooks (Low Tech, High Execution) ---
    "Classic Cacio e Pepe mantecatura technique recipe",
    "Pan seared diver scallops lemon brown butter recipe",
    "Classic French Steak Frites with Bearnaise sauce recipe",
    "Classic French 3-ingredient Lemon Posset dessert recipe",
    "Beef carpaccio arugula shaved parmesan truffle oil recipe",
    "Braised beef short ribs red wine reduction recipe",
    "Pan seared duck breast cherry gastrique recipe",
    "Traditional French chocolate souffle recipe"
]

CONVERSIONS = {
    "cup": 240.0, "cups": 240.0, "c.": 240.0,
    "tablespoon": 15.0, "tablespoons": 15.0, "tbsp": 15.0, "tbs": 15.0,
    "teaspoon": 5.0, "teaspoons": 5.0, "tsp": 5.0,
    "ounce": 28.35, "ounces": 28.35, "oz": 28.35,
    "fluid ounce": 30.0, "fl oz": 30.0,
    "pound": 453.59, "pounds": 453.59, "lb": 453.59, "lbs": 453.59,
    "stick": 113.4, "sticks": 113.4
}

HERO_KEYWORDS = [
    "Duck", "Beef", "Wagyu", "Strip", "Ribeye", "Tenderloin", "Scallop", "Lobster", 
    "Halibut", "Salmon", "Tuna", "Hamachi", "Oyster", "Caviar", "Foie Gras",
    "Asparagus", "Chanterelle", "Morel", "Truffle", "Parsnip", "Celery Root",
    "Chocolate", "Citrus", "Lemon", "Coffee", "Apple", "Squab", "Pork", "Short Rib"
]

def clean_quantity(text):
    result = []
    for char in text:
        try:
            name = unicodedata.name(char)
            if "VULGAR FRACTION" in name:
                result.append(str(unicodedata.numeric(char)))
            else:
                result.append(char)
        except ValueError:
            result.append(char)
    return "".join(result)

def parse_ingredient_line(raw):
    raw_clean = clean_quantity(raw.strip())
    pattern = r'^([\d\.\s\/\-]+)?\s*([a-zA-Z\.]+)?\s*(.*)$'
    match = re.match(pattern, raw_clean)
    
    qty = 50.0
    unit = "g"
    name = raw.strip()
    
    if match:
        num_str, unit_str, rest = match.groups()
        if num_str:
            num_str = num_str.strip()
            if "/" in num_str:
                parts = num_str.split()
                val = 0.0
                for p in parts:
                    if "/" in p:
                        n, d = p.split("/")
                        val += float(n) / float(d)
                    else:
                        val += float(p)
                qty = val
            else:
                try:
                    qty = float(num_str.split("-")[0])
                except:
                    qty = 50.0
        
        if unit_str:
            u_clean = unit_str.lower().rstrip('.')
            if u_clean in CONVERSIONS:
                qty = round(qty * CONVERSIONS[u_clean], 1)
                unit = "ml" if u_clean in ["cup", "cups", "tablespoon", "tablespoons", "tbsp", "teaspoon", "tsp", "fl oz"] else "g"
                name = rest.strip()
            else:
                name = f"{unit_str} {rest}".strip()

    n_lower = name.lower()
    if any(k in n_lower for k in ["salmon", "tuna", "hamachi", "oyster", "scallop", "lobster", "halibut", "fish", "caviar", "shrimp"]):
        dept = "seafood"
    elif any(k in n_lower for k in ["duck", "beef", "wagyu", "steak", "squab", "pork", "veal", "chicken", "foie gras", "short rib"]):
        dept = "butchery"
    elif any(k in n_lower for k in ["butter", "cream", "milk", "cheese", "egg", "yolk", "yogurt", "parmigiano", "pecorino"]):
        dept = "dairy"
    elif any(k in n_lower for k in ["flour", "sugar", "tapioca", "starch", "yeast", "gelatin", "sesame", "pasta", "spaghetti"]):
        dept = "drygoods"
    elif any(k in n_lower for k in ["shallot", "onion", "garlic", "chive", "thyme", "asparagus", "mushroom", "celery", "lemon", "apple", "peppercorn"]):
        dept = "produce"
    else:
        dept = "pantry"

    return {
        "name": name if name else raw.strip(),
        "qty": qty if qty > 0 else 50.0,
        "unit": unit,
        "dept": dept
    }

def detect_slot(dish_name, ingredients_text):
    text = (dish_name + " " + ingredients_text).lower()
    if any(k in text for k in ["posset", "tart", "chocolate", "souffle", "doughnut", "cake", "ice cream", "mousse", "sweet", "beignet"]):
        return "dessert"
    if any(k in text for k in ["granita", "sorbet", "palate cleanser"]):
        return "predessert"
    if any(k in text for k in ["duck", "beef", "strip", "wagyu", "ribeye", "squab", "roast", "calotte", "short rib", "steak frites"]):
        return "climax"
    if any(k in text for k in ["lobster", "scallop", "halibut", "pasta", "agnolotti", "risotto", "dashi", "cacio e pepe", "bass"]):
        return "mid"
    return "opener"

def detect_hero(dish_name, ingredients_text):
    text = dish_name + " " + ingredients_text
    found = []
    for h in HERO_KEYWORDS:
        if re.search(r'\b' + re.escape(h) + r'\b', text, re.IGNORECASE):
            found.append(h)
    return found if found else ["Culinary Special"]

def scrape_url_to_recipe(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return None
        try:
            scraper = scrape_html(resp.text, org_url=url)
        except:
            scraper = scrape_me(url)

        dish = scraper.title()
        raw_ings = scraper.ingredients()
        instructions = scraper.instructions()
        
        if not dish or not raw_ings or len(raw_ings) < 3:
            return None

        ings_text = " ".join(raw_ings)
        parsed_components = [parse_ingredient_line(line) for line in raw_ings]
        slot = detect_slot(dish, ings_text)
        hero = detect_hero(dish, ings_text)
        slug = re.sub(r'[^a-zA-Z0-9]+', '-', dish.lower()).strip('-')[:45]

        # Homecook Accessibility Tagging
        is_homecook = any(k in dish.lower() for k in ["cacio e pepe", "scallop", "posset", "carpaccio", "steak frites", "short rib"])

        return {
            "id": slug,
            "dish": dish,
            "restaurant": "Home Bistro Collection" if is_homecook else "3-Star Michelin Archive",
            "chef": "Artisanal Kitchen",
            "location": "Global",
            "source": url,
            "slot": slot,
            "hero": hero,
            "sensoryRole": f"Palate progression course featuring {', '.join(hero)}. Engineered for pristine balance of acidity, richness, and texture.",
            "components": parsed_components,
            "technique": instructions[:1200] if instructions else "Monitor core temperature and execute gentle emulsion control.",
            "plating": "Plate on pre-heated or chilled porcelain with intentional negative space and clean lines.",
            "pairing": {
                "wine": "Sommelier Reserve Pairing",
                "zeroProof": "Infused Botanical Gastronomy Reduction"
            }
        }
    except Exception:
        return None

def run_batch_harvest():
    try:
        from ddgs import DDGS
    except ImportError:
        from duckduckgo_search import DDGS

    existing = []
    if os.path.exists(RECIPES_FILE):
        try:
            with open(RECIPES_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except:
            existing = []

    existing_ids = {r["id"] for r in existing}
    initial_count = len(existing)
    print(f"===========================================================")
    print(f"  L'ATELIER BATCH HARVESTER INITIALIZED")
    print(f"  Starting Database Size: {initial_count} recipes")
    print(f"  Target Queue: {len(TARGET_QUERIES)} fine dining & homecook searches")
    print(f"===========================================================\n")

    ddgs_client = DDGS()
    total_added = 0

    for idx, query in enumerate(TARGET_QUERIES, 1):
        print(f"[{idx}/{len(TARGET_QUERIES)}] Crawling: '{query}'...")
        try:
            results = ddgs_client.text(f"{query}", max_results=3)
            for r in results:
                url = r.get("href")
                if not url:
                    continue
                recipe = scrape_url_to_recipe(url)
                if recipe and recipe["id"] not in existing_ids:
                    existing.append(recipe)
                    existing_ids.add(recipe["id"])
                    total_added += 1
                    print(f"   [+] Stored: {recipe['dish'][:35]}... ({recipe['slot'].upper()})")
                    # Incrementally flush to disk so no data is lost
                    with open(RECIPES_FILE, "w", encoding="utf-8") as f:
                        json.dump(existing, f, indent=2, ensure_ascii=False)
                    break # Take the best match per query
            time.sleep(1.2) # Polite request pacing
        except Exception as e:
            print(f"   [!] Skipped query: {e}")
            time.sleep(2)

    print(f"\n===========================================================")
    print(f"  HARVEST COMPLETE!")
    print(f"  New Unique Recipes Ingested: {total_added}")
    print(f"  Final Database Corpus Size: {len(existing)} recipes")
    print(f"  File Location: {os.path.abspath(RECIPES_FILE)}")
    print(f"===========================================================")

if __name__ == "__main__":
    run_batch_harvest()