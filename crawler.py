if __name__ == "__main__":
    raise SystemExit("Legacy catalog writer disabled: use python -m ingestion.pipeline --help. Original algorithms retained for reference; they must not overwrite reviewed data.")

import sys
import os
import re
import json
import argparse
import unicodedata
import requests
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me, scrape_html

RECIPES_FILE = "recipes.json"

# Common culinary density conversions (volume to metric grams/ml)
CONVERSIONS = {
    "cup": 240.0,
    "cups": 240.0,
    "c.": 240.0,
    "tablespoon": 15.0,
    "tablespoons": 15.0,
    "tbsp": 15.0,
    "tbs": 15.0,
    "teaspoon": 5.0,
    "teaspoons": 5.0,
    "tsp": 5.0,
    "ounce": 28.35,
    "ounces": 28.35,
    "oz": 28.35,
    "fluid ounce": 30.0,
    "fl oz": 30.0,
    "pound": 453.59,
    "pounds": 453.59,
    "lb": 453.59,
    "lbs": 453.59,
    "stick": 113.4,  # Standard butter stick
    "sticks": 113.4,
}

HERO_KEYWORDS = [
    "Duck", "Beef", "Wagyu", "Strip", "Ribeye", "Tenderloin", "Scallop", "Lobster", 
    "Halibut", "Salmon", "Tuna", "Hamachi", "Oyster", "Caviar", "Foie Gras",
    "Asparagus", "Chanterelle", "Morel", "Truffle", "Parsnip", "Celery Root",
    "Chocolate", "Citrus", "Lemon", "Coffee", "Apple", "Squab", "Pork"
]

def clean_quantity(text):
    """Normalize vulgar fractions like ½, ⅓, etc."""
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
    """Convert unformatted text like '1 1/2 cups heavy cream' to 360 ml"""
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

    # Department classification
    n_lower = name.lower()
    if any(k in n_lower for k in ["salmon", "tuna", "hamachi", "oyster", "scallop", "lobster", "halibut", "fish", "caviar", "shrimp"]):
        dept = "seafood"
    elif any(k in n_lower for k in ["duck", "beef", "wagyu", "steak", "squab", "pork", "veal", "chicken", "foie gras"]):
        dept = "butchery"
    elif any(k in n_lower for k in ["butter", "cream", "milk", "cheese", "egg", "yolk", "yogurt", "parmigiano"]):
        dept = "dairy"
    elif any(k in n_lower for k in ["flour", "sugar", "tapioca", "starch", "yeast", "gelatin", "sesame"]):
        dept = "drygoods"
    elif any(k in n_lower for k in ["shallot", "onion", "garlic", "chive", "thyme", "asparagus", "mushroom", "celery", "lemon", "apple"]):
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
    """Categorize course slot automatically"""
    text = (dish_name + " " + ingredients_text).lower()
    if any(k in text for k in ["tart", "chocolate", "souffle", "doughnut", "cake", "ice cream", "mousse", "sweet"]):
        return "dessert"
    if any(k in text for k in ["granita", "sorbet", "palate cleanser"]):
        return "predessert"
    if any(k in text for k in ["duck", "beef", "strip", "wagyu", "ribeye", "squab", "roast", "calotte"]):
        return "climax"
    if any(k in text for k in ["lobster", "scallop", "halibut", "pasta", "agnolotti", "risotto", "dashi"]):
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
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    resp = requests.get(url, headers=headers, timeout=12)
    if resp.status_code != 200:
        return None
        
    try:
        scraper = scrape_html(resp.text, org_url=url)
    except:
        scraper = scrape_me(url)

    dish = scraper.title()
    raw_ings = scraper.ingredients()
    instructions = scraper.instructions()
    
    if not dish or not raw_ings:
        return None

    ings_text = " ".join(raw_ings)
    parsed_components = [parse_ingredient_line(line) for line in raw_ings]
    slot = detect_slot(dish, ings_text)
    hero = detect_hero(dish, ings_text)
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', dish.lower()).strip('-')

    return {
        "id": slug[:40],
        "dish": dish,
        "restaurant": "Fine Dining Curated",
        "chef": "Executive Kitchen",
        "location": "Global",
        "source": url,
        "slot": slot,
        "hero": hero,
        "sensoryRole": f"Palate progression item highlighting {', '.join(hero)} balancing fat and acidity.",
        "components": parsed_components,
        "technique": instructions[:800] if instructions else "Execute with strict temperature monitoring and rest intervals.",
        "plating": "Present on heated/chilled stoneware with offset tweezers and deliberate negative space.",
        "pairing": {
            "wine": "Sommelier Reserve Selection",
            "zeroProof": "Infused Botanical Gastronomy Reduction"
        }
    }

def search_and_download(query, max_results=3):
    print(f"\n[+] Searching the web for: '{query}'...")
    try:
        from ddgs import DDGS
    except ImportError:
        from duckduckgo_search import DDGS
        
    results = DDGS().text(f"{query} recipe", max_results=max_results)
    recipes_added = []
    
    for r in results:
        url = r.get("href")
        if not url:
            continue
        print(f" -> Attempting parse: {url}")
        try:
            recipe = scrape_url_to_recipe(url)
            if recipe:
                recipes_added.append(recipe)
                print(f"    ✓ Successfully parsed: {recipe['dish']} ({recipe['slot'].upper()})")
        except Exception as e:
            continue
            
    return recipes_added

def save_to_database(new_recipes):
    if not new_recipes:
        print("[!] No new recipes found to save.")
        return
        
    existing = []
    if os.path.exists(RECIPES_FILE):
        try:
            with open(RECIPES_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except:
            existing = []
            
    existing_ids = {r["id"] for r in existing}
    added_count = 0
    
    for r in new_recipes:
        if r["id"] not in existing_ids:
            existing.append(r)
            existing_ids.add(r["id"])
            added_count += 1
            
    with open(RECIPES_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
        
    print(f"\n[✓] Database Updated: Added {added_count} new unique dishes to {RECIPES_FILE} (Total: {len(existing)})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="L'Atelier Automated Recipe Ingestion Engine")
    parser.add_argument("--search", type=str, help="Search term (e.g., 'Thomas Keller lobster' or 'duck breast')")
    parser.add_argument("--url", type=str, help="Direct recipe URL to scrape and append")
    args = parser.parse_args()

    if args.url:
        rec = scrape_url_to_recipe(args.url)
        if rec:
            save_to_database([rec])
        else:
            print("[!] Could not parse a recipe from that URL.")
    elif args.search:
        downloaded = search_and_download(args.search)
        save_to_database(downloaded)
    else:
        print("Usage: python crawler.py --search \"Dish or Chef\" OR python crawler.py --url \"https://...\"")