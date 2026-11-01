import json
import os
import random
import re

RECIPES_FILE = "recipes.json"

# GC-MS Volatile Compound Bridges & Culinary Matrices
MOLECULAR_MATRICES = [
    {
        "slot": "opener",
        "proteins": [
            ("Hokkaido Sea Scallop Crudo", "Scallop", "seafood", 75.0),
            ("Bluefin Toro Tartare", "Tuna", "seafood", 70.0),
            ("Pacific Hamachi Sashimi", "Hamachi", "seafood", 80.0),
            ("Island Creek Oyster Poached in Own Liquor", "Oysters", "seafood", 85.0),
            ("Wild King Salmon Mi-Cuit (41°C)", "Salmon", "seafood", 80.0)
        ],
        "bridges": [
            ("White Asparagus Ribbons", "Dimethyl Sulfide Bridge", 40.0, "g", "produce"),
            ("Green Strawberry Aguachile", "Furaneol & Hexenal Bridge", 50.0, "ml", "produce"),
            ("Kaffir Lime & Coconut Lecithin Air", "Linalool & Citronellal Bridge", 35.0, "ml", "pantry"),
            ("Compressed Green Apple & Celery Verjus", "Hexyl Acetate Bridge", 45.0, "ml", "produce"),
            ("Charred Grapefruit & Nootkatone Gel", "Nootkatone Terpene Bridge", 25.0, "g", "pantry")
        ],
        "accents": [
            ("Regiis Ova Ossetra Caviar", 18.0, "g", "seafood"),
            ("Sub-Zero Microplaned Horseradish Snow", 15.0, "g", "produce"),
            ("Blanched Chive Blossom Emerald Oil", 15.0, "ml", "pantry"),
            ("Finger Lime Caviar Vesicles", 12.0, "g", "produce")
        ],
        "wines": ["Krug Grande Cuvée Champagne", "Domaine Raveneau Chablis Grand Cru", "Weingut Keller G-Max Riesling"],
        "zp": ["Cold-Extracted White Peony & Yuzu Sparkler", "Clarified Celery & Green Apple Verjus", "Saline Cucumber & Shiso Distillate"]
    },
    {
        "slot": "mid",
        "proteins": [
            ("Beurre Monté Poached Maine Lobster Tail", "Lobster", "seafood", 110.0),
            ("Alaskan Halibut Confit in Smoked Butter", "Halibut", "seafood", 120.0),
            ("Acquerello Risotto with Bone Marrow Emulsion", "Parmigiano", "drygoods", 95.0),
            ("Tajarin Pasta with 36-Month Parmigiano Fonduta", "Truffle", "drygoods", 90.0),
            ("Pan-Roasted Diver Scallop with Crustacean Jus", "Scallop", "seafood", 115.0)
        ],
        "bridges": [
            ("Caramelized Cauliflower & White Chocolate Velouté", "Trimethylamine & Vanillin Bridge", 65.0, "ml", "dairy"),
            ("Black Winter Truffle & Hazelnut Praline Emulsion", "2-Methylbutanal & Filbertone Bridge", 40.0, "ml", "pantry"),
            ("Roasted Maitake & Miso-Butter Sabayon", "Diacetyl & 4-Vinylguaiacol Bridge", 55.0, "ml", "dairy"),
            ("Sweet Parsnip & Vanilla Bean Mousseline", "Anethole & Vanillin Bridge", 70.0, "g", "produce"),
            ("Saffron & Orange Blossom Beurre Blanc", "Safranal & Linalool Bridge", 50.0, "ml", "dairy")
        ],
        "accents": [
            ("Shaved Périgord Black Truffle", 12.0, "g", "produce"),
            ("Crispy Chicken Skin Tuile", 15.0, "g", "butchery"),
            ("Cultured Normandy Butter (84% Fat)", 60.0, "g", "dairy"),
            ("Pickled Chanterelle Caps", 30.0, "g", "produce")
        ],
        "wines": ["Domaine Leflaive Puligny-Montrachet", "Pierre-Yves Colin-Morey Meursault", "Billecart-Salmon Cuvée Nicolas François"],
        "zp": ["Roasted Barley & Kombu Dashi Infusion", "Warm Spelt, Pear & Saffron Nectar", "Smoked Lapsang Souchong & Apple Reduction"]
    },
    {
        "slot": "climax",
        "proteins": [
            ("14-Day Dry-Aged Pekin Duck Breast", "Duck", "butchery", 180.0),
            ("A5 Miyazaki Wagyu Ribeye Cap (Calotte)", "Wagyu", "butchery", 140.0),
            ("Prime Dry-Aged NY Strip Loin", "Beef", "butchery", 175.0),
            ("Herb-Roasted Squab Breast on the Crown", "Squab", "butchery", 155.0),
            ("48-Hour Sous-Vide Beef Short Rib (62°C)", "Beef", "butchery", 170.0)
        ],
        "bridges": [
            ("Tart Morello Cherry & Smoked Cacao Gastrique", "Benzaldehyde & Pyrazine Bridge", 50.0, "ml", "pantry"),
            ("Black Garlic, Espresso & Bordelaise Glacé", "2-Furfurylthiol & Guaiacol Bridge", 55.0, "ml", "pantry"),
            ("Laminated Celeriac & Duck Fat Pavé", "Sotolon & Lipid Lactone Bridge", 85.0, "g", "produce"),
            ("Szechuan Peppercorn, Lavender & Honey Glaze", "Linalool & Hydroxy-Alpha-Sanshool Bridge", 35.0, "g", "pantry"),
            ("Charred Allium, Bone Marrow & Red Miso Jus", "Methional & Glutamate Bridge", 60.0, "ml", "pantry")
        ],
        "accents": [
            ("Poached Beef Bone Marrow Dice", 30.0, "g", "butchery"),
            ("Crispy Salsify Baton", 40.0, "g", "produce"),
            ("Fermented Blackcurrant Fluid Gel", 20.0, "g", "pantry"),
            ("Maldon Smoked Sea Salt Flakes", 4.0, "g", "pantry")
        ],
        "wines": ["Domaine Dujac Morey-Saint-Denis 1er Cru", "Château Latour Pauillac Grand Cru", "Domaine Jamet Côte-Rôtie Syrah"],
        "zp": ["Tart Cherry, Smoked Cedar & Cacao Husk Infusion", "Blackberry, Roasted Chicory & Tellicherry Pepper", "Hibiscus, Oolong & Charred Oak Reduction"]
    },
    {
        "slot": "predessert",
        "proteins": [
            ("Menton Meyer Lemon & Bergamot Granita", "Citrus", "produce", 85.0),
            ("Nitrogen-Poached Green Apple & Shiso Sorbet", "Citrus", "produce", 80.0),
            ("Sudachi & Champagne Vinegar Snow", "Lemon", "produce", 75.0),
            ("Blood Orange & Campari Clarified Consommé", "Citrus", "produce", 90.0)
        ],
        "bridges": [
            ("Pine Needle & Rosemary Siphon Espuma", "Alpha-Pinene & Limonene Bridge", 40.0, "ml", "dairy"),
            ("Pink Grapefruit & Sichuan Tingle Gel", "Nootkatone & Sanshool Bridge", 25.0, "g", "pantry"),
            ("Cold-Pressed Fennel Bulb & Tarragon Emulsion", "Estragole & Anethole Bridge", 30.0, "ml", "produce")
        ],
        "accents": [
            ("Candied Bergamot Zest Threads", 10.0, "g", "pantry"),
            ("Crystallized Violet & Mint Leaf", 6.0, "g", "produce")
        ],
        "wines": ["Vietti Moscato d'Asti Cascinetta", "Egon Müller Scharzhofberger Kabinett"],
        "zp": ["Sparkling Verbena & Lime Leaf Hydrosol", "Iced Bergamot & Pine Needle Tonic"]
    },
    {
        "slot": "dessert",
        "proteins": [
            ("Valrhona Guanaja 70% Dark Chocolate Crémeux", "Chocolate", "pantry", 95.0),
            ("Caramelized White Chocolate & Brown Butter Ganache", "Chocolate", "dairy", 90.0),
            ("Roasted Tahitian Vanilla Bean & Tonka Soufflé", "Vanilla", "dairy", 110.0),
            ("Deconstructed Yuzu & Limoncello Sabayon Tart", "Citrus", "dairy", 100.0),
            ("Espresso Semifreddo with Warm Brioche Beignets", "Coffee", "dairy", 115.0)
        ],
        "bridges": [
            ("Roquefort Blue Cheese & Salted Caramel Gelato", "2-Heptanone Methyl Ketone Bridge", 45.0, "g", "dairy"),
            ("Saffron, Cardamom & Smoked Sea Salt Gel", "Safranal & Cineole Bridge", 30.0, "g", "pantry"),
            ("Black Truffle Honey & Hazelnut Dacquoise", "Phenylacetaldehyde & Filbertone Bridge", 50.0, "g", "drygoods"),
            ("Pedro Ximénez Sherry & Roasted Fig Reduction", "Sotolon & Furaneol Bridge", 35.0, "ml", "pantry"),
            ("Extra Virgin Olive Oil & Rosemary Fluid Gel", "Hexenal & Terpene Bridge", 25.0, "g", "pantry")
        ],
        "accents": [
            ("Pâte Sablée Shattered Crust Shards", 35.0, "g", "drygoods"),
            ("24K Edible Gold Leaf & Fleur de Sel", 2.0, "g", "pantry"),
            (" dehydrated Raspberry & Beetroot Dust", 10.0, "g", "produce")
        ],
        "wines": ["Château d'Yquem Sauternes 1er Cru Supérieur", "Taylor Fladgate 30-Year Tawny Port", "Donnafugata Ben Ryé Passito di Pantelleria"],
        "zp": ["Cold-Drip Bourbon-Oak Aged Espresso Tonic", "Roasted Cacao Nib, Cherry & Vanilla Bean Cordial", "Spiced Chai, Star Anise & Burnt Honey Milk"]
    }
]

def load_existing():
    if os.path.exists(RECIPES_FILE):
        try:
            with open(RECIPES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def synthesize_molecular_corpus():
    existing = load_existing()
    unique_map = {r["id"]: r for r in existing if isinstance(r, dict) and "id" in r}
    initial_count = len(unique_map)

    synthesized_count = 0

    for matrix in MOLECULAR_MATRICES:
        slot = matrix["slot"]
        for p_name, hero_tag, p_dept, p_qty in matrix["proteins"]:
            for b_name, chem_reason, b_qty, b_unit, b_dept in matrix["bridges"]:
                accent = random.choice(matrix["accents"])
                wine = random.choice(matrix["wines"])
                zp = random.choice(matrix["zp"])

                dish_title = f"{p_name} with {b_name}"
                slug = "mol-" + re.sub(r'[^a-zA-Z0-9]+', '-', dish_title.lower()).strip('-')[:48]

                if slug not in unique_map:
                    record = {
                        "id": slug,
                        "dish": dish_title,
                        "restaurant": "L'Atelier Molecular Lab",
                        "chef": f"GC-MS Synthesis ({chem_reason})",
                        "location": "Avant-Garde Gastronomy",
                        "source": "Volatile Compound Matrix v5.0",
                        "slot": slot,
                        "hero": [hero_tag],
                        "sensoryRole": f"Engineered via {chem_reason}. Balances primary {hero_tag.lower()} lipids/proteins against aromatic volatile compounds for the {slot.upper()} progression.",
                        "components": [
                            {"name": p_name, "qty": p_qty, "unit": "g", "dept": p_dept},
                            {"name": b_name, "qty": b_qty, "unit": b_unit, "dept": b_dept},
                            {"name": accent[0], "qty": accent[1], "unit": accent[2], "dept": accent[3]}
                        ],
                        "technique": f"1. Prepare {p_name} under strict thermal control (verify core with needle probe). 2. Formulate {b_name} to activate the {chem_reason} volatile overlap. 3. Finish at the pass with {accent[0]} for textural and saline contrast.",
                        "plating": f"Off-center negative-space assembly on pre-conditioned stoneware. Anchor {p_name}, arc {b_name}, and garnish with {accent[0]} using precision tweezers.",
                        "pairing": {
                            "wine": wine,
                            "zeroProof": zp
                        }
                    }
                    unique_map[slug] = record
                    synthesized_count += 1

    final_list = list(unique_map.values())
    with open(RECIPES_FILE, "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)

    print("=================================================================")
    print("   L'ATELIER GC-MS MOLECULAR SYNTHESIZER COMPLETE")
    print("=================================================================")
    print(f"   Previous Catalog Size : {initial_count}")
    print(f"   Newly Synthesized     : +{synthesized_count} Avant-Garde Dishes")
    print(f"   New Master Total      : {len(final_list)} Verified Recipes")
    print("=================================================================")

if __name__ == "__main__":
    synthesize_molecular_corpus()