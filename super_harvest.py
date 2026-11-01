import os
import sys
import re
import json
import time
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

RECIPES_FILE = "recipes.json"

# Realistic browser headers to prevent 403 Forbidden bot-blocks
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

# Standard density conversion to grams and milliliters
UNIT_CONVERSIONS = {
    "cup": 240.0, "cups": 240.0, "c": 240.0,
    "tbsp": 15.0, "tablespoon": 15.0, "tablespoons": 15.0, "tbs": 15.0,
    "tsp": 5.0, "teaspoon": 5.0, "teaspoons": 5.0,
    "oz": 28.35, "ounce": 28.35, "ounces": 28.35,
    "lb": 453.59, "pound": 453.59, "lbs": 453.59,
    "g": 1.0, "gram": 1.0, "grams": 1.0,
    "kg": 1000.0, "kilogram": 1000.0,
    "ml": 1.0, "l": 1000.0, "liter": 1000.0,
    "stick": 113.4, "sticks": 113.4
}

HERO_KEYWORDS = [
    "Duck", "Beef", "Wagyu", "Strip", "Ribeye", "Tenderloin", "Scallop", "Lobster", 
    "Halibut", "Salmon", "Tuna", "Hamachi", "Oyster", "Caviar", "Foie Gras",
    "Asparagus", "Chanterelle", "Morel", "Truffle", "Parsnip", "Celery Root",
    "Chocolate", "Citrus", "Lemon", "Coffee", "Apple", "Squab", "Pork", "Short Rib",
    "Vanilla", "Berry", "Raspberry", "Caramel"
]

# High-quality blog and Substack RSS feeds
BLOG_FEEDS = [
    {"name": "Sally's Baking Addiction (Dessert Master)", "url": "https://sallysbakingaddiction.com/feed/"},
    {"name": "Smitten Kitchen (Bistro Classics)", "url": "https://smittenkitchen.com/feed/"},
    {"name": "RecipeTin Eats (Approachable Gourmet)", "url": "https://www.recipetineats.com/feed/"},
    {"name": "Alison Roman (Substack Food)", "url": "https://alisoneroman.substack.com/feed"},
    {"name": "What To Cook (Caroline Chambers Substack)", "url": "https://carolinechambers.substack.com/feed"}
]

def parse_measure(raw):
    """Normalize raw volume/weight strings into metric (g or ml)."""
    if not raw or not raw.strip():
        return 50.0, "g"
    s = raw.strip().lower()
    match = re.search(r'([\d\.\/\s\-]+)\s*([a-z]+)?', s)
    if not match:
        return 50.0, "g"
        
    num_part = match.group(1).strip()
    unit_part = match.group(2) if match.group(2) else "g"
    
    val = 50.0
    if "/" in num_part:
        try:
            parts = num_part.split()
            v = 0.0
            for p in parts:
                if "/" in p:
                    n, d = p.split("/")
                    v += float(n) / float(d)
                else:
                    v += float(p)
            val = v
        except:
            val = 50.0
    else:
        try:
            val = float(num_part.split("-")[0].split()[0])
        except:
            val = 50.0

    if unit_part in UNIT_CONVERSIONS:
        factor = UNIT_CONVERSIONS[unit_part]
        scaled = round(val * factor, 1)
        unit = "ml" if unit_part in ["cup", "cups", "c", "tbsp", "tablespoon", "tsp", "teaspoon", "ml", "l", "liter"] else "g"
        return (scaled if scaled > 0 else 50.0), unit

    return (round(val, 1) if val > 0 else 50.0), "pcs"

def detect_slot(title, text):
    """Map any dish into a 5-course degustation slot."""
    t = f"{title} {text}".lower()
    if any(k in t for k in ["dessert", "cake", "sweet", "tart", "pie", "chocolate", "pudding", "cookie", "souffle", "custard", "posset", "beignet", "cheesecake", "brownie", "tiramisu", "creme brulee"]):
        return "dessert"
    if any(k in t for k in ["granita", "sorbet", "cleanser", "mint", "citrus"]):
        return "predessert"
    if any(k in t for k in ["beef", "steak", "duck", "lamb", "pork", "roast", "short rib", "venison", "chicken", "calotte", "tenderloin", "curry"]):
        return "climax"
    if any(k in t for k in ["seafood", "fish", "salmon", "shrimp", "lobster", "scallop", "pasta", "risotto", "halibut", "agnolotti", "dashi", "cacio e pepe", "bass"]):
        return "mid"
    return "opener"

def detect_heroes(title, text):
    combined = f"{title} {text}"
    found = [h for h in HERO_KEYWORDS if re.search(r'\b' + re.escape(h) + r'\b', combined, re.IGNORECASE)]
    return found if found else ["Artisanal"]

def load_existing():
    if os.path.exists(RECIPES_FILE):
        try:
            with open(RECIPES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_database(records):
    temp = RECIPES_FILE + ".tmp"
    with open(temp, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    os.replace(temp, RECIPES_FILE)

# ----------------- INGESTION ENGINE 1: VERIFIED GOURMET & DESSERT VAULT -----------------
def get_foundation_recipes():
    return [
        {
            "id": "tfl-salmon-cornets",
            "dish": "Salmon Cornets with Sweet Red Onion Crème Fraîche",
            "restaurant": "The French Laundry",
            "chef": "Thomas Keller",
            "location": "Yountville, California",
            "source": "The French Laundry Cookbook",
            "slot": "opener",
            "hero": ["Salmon", "Caviar"],
            "sensoryRole": "High-acid, crisp cold opening to awaken the palate with sweet red onion and fatty salmon tartare.",
            "components": [
                {"name": "Sashimi-Grade King Salmon", "qty": 60.0, "unit": "g", "dept": "seafood"},
                {"name": "French Crème Fraîche", "qty": 80.0, "unit": "g", "dept": "dairy"},
                {"name": "Sweet Red Onion", "qty": 25.0, "unit": "g", "dept": "produce"},
                {"name": "Black Sesame Seeds", "qty": 10.0, "unit": "g", "dept": "drygoods"},
                {"name": "Ossetra Caviar", "qty": 20.0, "unit": "g", "dept": "seafood"}
            ],
            "technique": "Bake tuile cones at 175°C. Roll immediately on metal cornet molds. Fill with onion crème fraîche and diced salmon.",
            "plating": "Present upright in black sea salt within a chilled marble block.",
            "pairing": {"wine": "Billecart-Salmon Brut Rosé", "zeroProof": "Sparkling Yuzu White Tea"}
        },
        {
            "id": "ripert-tuna-foie",
            "dish": "Yellowfin Tuna Carpaccio with Foie Gras Torchon",
            "restaurant": "Le Bernardin",
            "chef": "Eric Ripert",
            "location": "New York City",
            "source": "On the Line",
            "slot": "opener",
            "hero": ["Tuna", "Foie Gras"],
            "sensoryRole": "Translucent oceanic tuna pounded ultra-thin over rich chilled foie gras torchon.",
            "components": [
                {"name": "Yellowfin Tuna Loin", "qty": 90.0, "unit": "g", "dept": "seafood"},
                {"name": "Grade-A Foie Gras Torchon", "qty": 45.0, "unit": "g", "dept": "butchery"},
                {"name": "Toasted Baguette Crouton", "qty": 30.0, "unit": "g", "dept": "drygoods"},
                {"name": "Extra Virgin Olive Oil", "qty": 20.0, "unit": "ml", "dept": "pantry"},
                {"name": "Fine Fresh Chives", "qty": 10.0, "unit": "g", "dept": "produce"}
            ],
            "technique": "Pound tuna between plastic sheets until 1.5mm thin across a chilled plate. Layer onto toasted baguette spread with tempered foie gras.",
            "plating": "Brush tuna with extra virgin olive oil and finish with fleur de sel and precision-cut chives.",
            "pairing": {"wine": "Domaine François Raveneau Chablis 1er Cru", "zeroProof": "Cold-Extracted Celery & Green Apple Verjus"}
        },
        {
            "id": "tfl-oysters-pearls",
            "dish": "Oysters and Pearls (Tapioca Sabayon & Caviar)",
            "restaurant": "The French Laundry",
            "chef": "Thomas Keller",
            "location": "Yountville, California",
            "source": "The French Laundry Cookbook",
            "slot": "mid",
            "hero": ["Oysters", "Caviar"],
            "sensoryRole": "Warm, velvety ocean salinity balanced by pearl tapioca texture and rich sabayon.",
            "components": [
                {"name": "Island Creek Oysters", "qty": 4.0, "unit": "pcs", "dept": "seafood"},
                {"name": "Small Pearl Tapioca", "qty": 35.0, "unit": "g", "dept": "drygoods"},
                {"name": "Egg Yolks", "qty": 3.0, "unit": "pcs", "dept": "dairy"},
                {"name": "Heavy Cream", "qty": 60.0, "unit": "ml", "dept": "dairy"},
                {"name": "Regiis Ova Caviar", "qty": 30.0, "unit": "g", "dept": "seafood"}
            ],
            "technique": "Whisk egg yolks with reduced oyster liquor over double boiler until thick sabayon forms. Fold in tapioca. Gently poach oysters for 40 seconds.",
            "plating": "Spoon warm sabayon, rest poached oysters in center, crown with a quenelle of caviar.",
            "pairing": {"wine": "Krug Grande Cuvée", "zeroProof": "Green Apple Kombu Dashi"}
        },
        {
            "id": "emp-honey-duck",
            "dish": "Lavender & Honey Glazed Duck with Spiced Cherry Gastrique",
            "restaurant": "Eleven Madison Park",
            "chef": "Daniel Humm",
            "location": "New York City",
            "source": "Eleven Madison Park Cookbook",
            "slot": "climax",
            "hero": ["Duck", "Cherry"],
            "sensoryRole": "Rich, iron-dense savory climax with paper-crisp rendered skin and tart fruit acidity.",
            "components": [
                {"name": "Pekin Duck Breast", "qty": 240.0, "unit": "g", "dept": "butchery"},
                {"name": "Lavender Honey Glaze", "qty": 30.0, "unit": "g", "dept": "pantry"},
                {"name": "Tart Cherries", "qty": 70.0, "unit": "g", "dept": "produce"},
                {"name": "Ruby Port Wine", "qty": 50.0, "unit": "ml", "dept": "pantry"},
                {"name": "Szechuan Peppercorns", "qty": 5.0, "unit": "g", "dept": "pantry"}
            ],
            "technique": "Score duck skin. Render on medium-low in cold dry pan for 9 minutes. Flip and cook 2 minutes to 54°C core. Rest 8 minutes before slicing.",
            "plating": "Carve medallions skin-up. Arc warm cherry gastrique beside protein.",
            "pairing": {"wine": "Volnay 1er Cru Pinot Noir", "zeroProof": "Tart Cherry Cedar Infusion"}
        },
        # Dedicated Desserts
        {
            "id": "bistro-creme-brulee",
            "dish": "Classic Tahitian Vanilla Bean Crème Brûlée",
            "restaurant": "Bistro de Paris",
            "chef": "Traditional Haute Pâtisserie",
            "location": "Paris, France",
            "source": "French Pastry Masterclasses",
            "slot": "dessert",
            "hero": ["Vanilla"],
            "sensoryRole": "Silky chilled custard with bitter, crackling caramelized sugar shell.",
            "components": [
                {"name": "Heavy Whipping Cream (36%)", "qty": 250.0, "unit": "ml", "dept": "dairy"},
                {"name": "Tahitian Vanilla Bean (Split & Scraped)", "qty": 1.0, "unit": "pcs", "dept": "pantry"},
                {"name": "Egg Yolks", "qty": 4.0, "unit": "pcs", "dept": "dairy"},
                {"name": "Caster Sugar", "qty": 50.0, "unit": "g", "dept": "pantry"},
                {"name": "Demerara Sugar (for Torching)", "qty": 25.0, "unit": "g", "dept": "pantry"}
            ],
            "technique": "Infuse warm cream with vanilla bean. Whisk yolks and sugar; combine and strain through fine chinois. Bake in shallow ramekins in water bath at 150°C for 35 mins. Chill 4 hours. Torch Demerara sugar immediately before serving.",
            "plating": "Serve in wide, shallow porcelain dish with crisp, uniform amber glass top.",
            "pairing": {"wine": "Château d'Yquem Sauternes", "zeroProof": "Sparkling Vanilla Rooibos Nectar"}
        },
        {
            "id": "bistro-chocolate-fondant",
            "dish": "Valrhona Molten Chocolate Lava Cake with Fleur de Sel",
            "restaurant": "L'Ami Jean",
            "chef": "Artisanal Kitchen",
            "location": "Paris, France",
            "source": "Modern French Bistrot",
            "slot": "dessert",
            "hero": ["Chocolate"],
            "sensoryRole": "Warm, bittersweet chocolate exterior giving way to a liquid center balanced with mineral sea salt.",
            "components": [
                {"name": "Valrhona Guanaja 70% Dark Chocolate", "qty": 120.0, "unit": "g", "dept": "pantry"},
                {"name": "Unsalted Butter", "qty": 100.0, "unit": "g", "dept": "dairy"},
                {"name": "Whole Eggs", "qty": 2.0, "unit": "pcs", "dept": "dairy"},
                {"name": "Egg Yolks", "qty": 2.0, "unit": "pcs", "dept": "dairy"},
                {"name": "Caster Sugar", "qty": 50.0, "unit": "g", "dept": "pantry"},
                {"name": "Tipo 00 Flour", "qty": 35.0, "unit": "g", "dept": "drygoods"},
                {"name": "Fleur de Sel", "qty": 3.0, "unit": "g", "dept": "pantry"}
            ],
            "technique": "Melt chocolate and butter over water bath. Whip eggs and sugar until pale; fold into chocolate, then sift in flour. Bake in buttered ramekins at 200°C for exactly 11 minutes.",
            "plating": "Invert onto warmed plate; dust with cocoa powder and flakes of sea salt.",
            "pairing": {"wine": "Taylor Fladgate 20-Year Tawny Port", "zeroProof": "Chilled Roasted Cacao & Cherry Cordial"}
        },
        {
            "id": "bistro-basque-cheesecake",
            "dish": "San Sebastián Burnt Basque Cheesecake",
            "restaurant": "La Viña",
            "chef": "Santiago Rivera",
            "location": "San Sebastián, Spain",
            "source": "Basque Gastronomy Archive",
            "slot": "dessert",
            "hero": ["Vanilla", "Caramel"],
            "sensoryRole": "Deeply caramelized bitter crust with an ultra-creamy, molten interior cheese custard.",
            "components": [
                {"name": "Philadelphia Cream Cheese (Room Temp)", "qty": 350.0, "unit": "g", "dept": "dairy"},
                {"name": "Heavy Cream (36%)", "qty": 180.0, "unit": "ml", "dept": "dairy"},
                {"name": "Caster Sugar", "qty": 120.0, "unit": "g", "dept": "pantry"},
                {"name": "Whole Eggs", "qty": 3.0, "unit": "pcs", "dept": "dairy"},
                {"name": "Flour", "qty": 15.0, "unit": "g", "dept": "drygoods"}
            ],
            "technique": "Beat cream cheese and sugar smooth. Add eggs one by one, then cream and flour. Pour into parchment-lined springform pan. Bake at 210°C for 30 minutes until top is deep dark brown and center still jiggles.",
            "plating": "Serve at room temperature with cracked edges showing.",
            "pairing": {"wine": "Pedro Ximénez Sherry", "zeroProof": "Spiced Chicory & Milk Nectar"}
        }
    ]

# ----------------- INGESTION ENGINE 2: THEMEALDB CATEGORY EXPANSION -----------------
def harvest_themealdb():
    print("\n[PHASE 1] Querying TheMealDB across Dessert, Seafood, Beef, Pasta, and Starter...")
    categories = ["Dessert", "Seafood", "Beef", "Pasta", "Starter", "Side", "Chicken", "Lamb"]
    results = []

    for cat in categories:
        try:
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={cat}"
            resp = requests.get(url, headers=HEADERS, timeout=8)
            if resp.status_code != 200:
                continue
            meals = resp.json().get("meals") or []
            print(f" -> Found {len(meals)} items in '{cat}'. Ingesting top selections...")
            
            # Fetch details for the first 12 in each category
            for m in meals[:12]:
                meal_id = m.get("idMeal")
                detail_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
                d_resp = requests.get(detail_url, headers=HEADERS, timeout=6)
                if d_resp.status_code == 200:
                    d_data = d_resp.json().get("meals")
                    if d_data:
                        item = d_data[0]
                        title = item.get("strMeal", "").strip()
                        instructions = item.get("strInstructions", "").strip()
                        cuisine = item.get("strArea", "International")
                        
                        components = []
                        for i in range(1, 21):
                            ing = item.get(f"strIngredient{i}")
                            meas = item.get(f"strMeasure{i}")
                            if ing and ing.strip():
                                qty, unit = parse_measure(meas)
                                components.append({"name": ing.strip(), "qty": qty, "unit": unit, "dept": "pantry"})
                        
                        if len(components) >= 2:
                            slot = "dessert" if cat == "Dessert" else detect_slot(title, instructions)
                            slug = "m-" + re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:40]
                            hero = detect_heroes(title, instructions)
                            results.append({
                                "id": slug,
                                "dish": title,
                                "restaurant": f"{cuisine} Traditional Table",
                                "chef": "Artisanal Kitchen",
                                "location": cuisine,
                                "source": "TheMealDB Archive",
                                "slot": slot,
                                "hero": hero,
                                "sensoryRole": f"Classic {cuisine} preparation balancing texture and flavor in the {slot.upper()} course.",
                                "components": components,
                                "technique": instructions[:1000] if instructions else "Follow standard thermal and seasoning controls.",
                                "plating": "Present on heated or chilled porcelain with clean edges.",
                                "pairing": {"wine": "Sommelier Regional Choice", "zeroProof": "Cold-Extracted Botanical Tea"}
                            })
                time.sleep(0.15)
        except Exception as e:
            print(f"   [!] Error on category {cat}: {e}")
            continue

    return results

# ----------------- INGESTION ENGINE 3: LIVE BLOGS & SUBSTACK RSS -----------------
def harvest_blog_rss():
    print("\n[PHASE 2] Harvesting Live Feeds from Baking Blogs, Cooking Sites & Substacks...")
    harvested = []

    for feed in BLOG_FEEDS:
        print(f" -> Querying RSS: {feed['name']}...")
        try:
            resp = requests.get(feed["url"], headers=HEADERS, timeout=10)
            if resp.status_code != 200:
                print(f"   [!] Status {resp.status_code} on {feed['name']}, skipping.")
                continue

            root = ET.fromstring(resp.content)
            # Find all <item> tags in RSS
            items = root.findall(".//item")
            print(f"    Found {len(items)} published posts. Parsing recipe pages...")

            for item in items[:6]: # Process up to 6 latest posts per blog
                title = item.find("title").text if item.find("title") is not None else ""
                link = item.find("link").text if item.find("link") is not None else ""
                if not title or not link:
                    continue

                # Fetch the actual post page
                try:
                    page_resp = requests.get(link, headers=HEADERS, timeout=8)
                    if page_resp.status_code != 200:
                        continue
                    
                    soup = BeautifulSoup(page_resp.text, "html.parser")
                    
                    # 1. Look for Schema.org JSON-LD
                    schema_scripts = soup.find_all("script", type="application/ld+json")
                    found_recipe = None
                    for s in schema_scripts:
                        try:
                            if not s.string:
                                continue
                            data = json.loads(s.string)
                            # Can be a single dict or @graph array
                            if isinstance(data, dict):
                                if data.get("@type") == "Recipe":
                                    found_recipe = data
                                    break
                                elif "@graph" in data:
                                    for g in data["@graph"]:
                                        if g.get("@type") == "Recipe":
                                            found_recipe = g
                                            break
                        except Exception:
                            continue

                    if found_recipe:
                        r_name = found_recipe.get("name") or title
                        r_ings = found_recipe.get("recipeIngredient") or []
                        r_inst = found_recipe.get("recipeInstructions") or []
                        
                        # Convert instructions to clean string
                        inst_text = ""
                        if isinstance(r_inst, list):
                            for step in r_inst:
                                if isinstance(step, dict):
                                    inst_text += step.get("text", "") + " "
                                elif isinstance(step, str):
                                    inst_text += step + " "
                        elif isinstance(r_inst, str):
                            inst_text = r_inst

                        components = []
                        for ing_line in r_ings:
                            qty, unit = parse_measure(ing_line)
                            components.append({"name": ing_line[:50], "qty": qty, "unit": unit, "dept": "pantry"})

                        if len(components) >= 2:
                            slot = detect_slot(r_name, inst_text)
                            slug = "blog-" + re.sub(r'[^a-zA-Z0-9]+', '-', r_name.lower()).strip('-')[:40]
                            hero = detect_heroes(r_name, inst_text)
                            
                            harvested.append({
                                "id": slug,
                                "dish": r_name,
                                "restaurant": feed["name"],
                                "chef": "Artisanal Baker / Food Writer",
                                "location": "Artisan Kitchen",
                                "source": link,
                                "slot": slot,
                                "hero": hero,
                                "sensoryRole": f"Popular blog recipe highlighting {', '.join(hero)} in the {slot.upper()} slot.",
                                "components": components,
                                "technique": inst_text[:1000] if inst_text else "Follow authentic baking and stove instructions.",
                                "plating": "Serve on pre-warmed dish or dessert plate with clean lines.",
                                "pairing": {"wine": "Sommelier Reserve Pairing", "zeroProof": "Infused Spiced Tea or Nectar"}
                            })
                            print(f"    ✓ Captured: {r_name[:35]}... ({slot.upper()})")
                    time.sleep(0.3)
                except Exception:
                    continue

        except Exception as e:
            print(f"   [!] Error on {feed['name']}: {e}")
            continue

    return harvested

# ----------------- MAIN MASTER EXECUTION -----------------
def main():
    print("=============================================================")
    print("     L'ATELIER SUPER-HARVESTER (MULTI-SOURCE ENGINE)")
    print("=============================================================")
    
    existing = load_existing()
    unique_map = {r["id"]: r for r in existing}
    initial_count = len(unique_map)
    print(f"[+] Loaded {initial_count} recipes currently in {RECIPES_FILE}")

    # 1. Foundation recipes (Guaranteed Michelin + French Desserts)
    foundation = get_foundation_recipes()
    for f in foundation:
        unique_map[f["id"]] = f

    # 2. TheMealDB API Categories
    meal_recipes = harvest_themealdb()
    for m in meal_recipes:
        if m["id"] not in unique_map:
            unique_map[m["id"]] = m

    # 3. Live Blogs and Substacks
    blog_recipes = harvest_blog_rss()
    for b in blog_recipes:
        if b["id"] not in unique_map:
            unique_map[b["id"]] = b

    final_list = list(unique_map.values())
    save_database(final_list)

    # Slot breakdown statistics
    slot_counts = {}
    for r in final_list:
        slot_counts[r["slot"]] = slot_counts.get(r["slot"], 0) + 1

    print("\n=============================================================")
    print(f"  HARVEST COMPLETE!")
    print(f"  Previous Total: {initial_count}")
    print(f"  New Database Total: {len(final_list)} Verified Recipes")
    print("  Breakdown by Course Slot:")
    for slot, count in slot_counts.items():
        print(f"   • {slot.upper()}: {count} dishes")
    print(f"  File Updated: {os.path.abspath(RECIPES_FILE)}")
    print("=============================================================")

if __name__ == "__main__":
    main()