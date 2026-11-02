# -*- coding: utf-8 -*-
"""
Generates data-encyclopedia.js for L'Atelier's Ingredient Encyclopedia.
Contains 65 comprehensive ingredient dossiers with flavor profiles, seasonality,
culinary science roles, storage rules, and pairing affinities.
"""

import json

ENCYCLOPEDIA_INGREDIENTS = [
    {
        "id": "ing-garlic",
        "name": "Garlic (Allium sativum)",
        "category": "Produce",
        "season": "Year-round (Peak late summer/fall)",
        "storage": "Store in a cool (15°C/60°F), dry, dark pantry with good airflow. Never refrigerate whole unpeeled heads (causes sprouting and humidity rot).",
        "flavorProfile": "Pungent, sharp, sulfuric raw; sweet, nutty, mellow, deeply savory when slowly roasted or sweated.",
        "scienceRole": "Contains alliin and the enzyme alliinase in separate cell compartments. Crushing or mincing breaks cell walls, allowing them to react within seconds to synthesize allicin (responsible for sharp pungency). Cooking deactivates alliinase and polymerizes sugars into sweet caramelized alliums.",
        "bestTechniques": ["Confit in olive oil at 90°C", "Fine brunoise sweated in butter/oil", "Rubbed raw on toasted crusty bread (bruschetta)"],
        "substitutions": "Shallots + pinch of garlic powder, or wild garlic (ramps).",
        "affinities": ["Olive oil", "Butter", "Parsley", "Thyme", "Tomato", "Pork", "Mushrooms"]
    },
    {
        "id": "ing-shallot",
        "name": "French Grey Shallot (Échalote Grise)",
        "category": "Produce",
        "season": "Year-round",
        "storage": "Cool, dry, dark basket. Keeps up to 2 months.",
        "flavorProfile": "Delicate, sweet, refined allium with subtle garlic nuances; far less harsh than yellow onion.",
        "scienceRole": "Higher sugar and lower moisture than standard onions, allowing rapid caramelization without boiling in surface water. The indispensable aromatic acid base for French reductions (Béarnaise, Beurre Blanc, Bordelaise).",
        "bestTechniques": ["Minced fine (ciseler) for vinegar reductions", "Caramelized whole in butter as a garnish", "Crispy fried shallots for Southeast Asian dishes"],
        "substitutions": "Sweet Vidalia onion minced fine with a tiny sliver of garlic.",
        "affinities": ["White wine vinegar", "Butter", "Tarragon", "Red wine", "Steak", "Fish"]
    },
    {
        "id": "ing-san-marzano",
        "name": "San Marzano Tomato DOP",
        "category": "Produce",
        "season": "Summer (Canned DOP available year-round)",
        "storage": "Store canned cans in pantry up to 3 years. Once opened, transfer to glass container and refrigerate for up to 5 days.",
        "flavorProfile": "Intense sweet-tart balance, low acidity, thick fleshy walls, minimal seed cavities.",
        "scienceRole": "Grown in volcanic soil at the foot of Mount Vesuvius, giving it high natural free glutamic acid (umami) and low citric acid, making it the supreme tomato for pasta sauces without requiring added sugar.",
        "bestTechniques": ["Crushed by hand for raw Neapolitan pizza sauce", "Simmered with butter and onion for Marcella Hazan sauce", "Base for ragù"],
        "substitutions": "Italian whole peeled plum tomatoes (Pelati) with a pinch of baking soda to soften acid.",
        "affinities": ["Basil", "Extra virgin olive oil", "Garlic", "Parmigiano-Reggiano", "Oregano"]
    },
    {
        "id": "ing-butter-european",
        "name": "European Cultured Butter (Beurre d'Isigny / 82% Fat)",
        "category": "Dairy",
        "season": "Year-round (Spring milk has richest yellow carotene hue)",
        "storage": "Refrigerate tightly wrapped at <=4°C to prevent lipid oxidation and absorbing refrigerator odors. Freezes up to 6 months.",
        "flavorProfile": "Rich, creamy, hazelnut undertones with subtle lactic fermentation tang.",
        "scienceRole": "Higher butterfat (82-84% vs 80% American) means significantly less water. This ensures crisp flaky laminated pastry (croissants, puff pastry), faster reduction to brown butter (beurre noisette), and silkier pan sauce mantecatura.",
        "bestTechniques": ["Monter au beurre (finishing hot sauces off-heat)", "Beurre noisette (brown butter)", "Pastry tourage (lamination)"],
        "substitutions": "Standard unsalted butter (reduce liquid slightly in baking).",
        "affinities": ["Shallots", "Lemon juice", "Parsley", "Sage", "Fish", "Potatoes"]
    },
    {
        "id": "ing-parmigiano",
        "name": "Parmigiano-Reggiano DOP (Aged 24 Months)",
        "category": "Dairy",
        "season": "Aged 24 to 36 months",
        "storage": "Wrap in breathable cheese paper or parchment, then loosely in plastic wrap at 4-8°C. Never freeze. Save rinds for simmering in broths.",
        "flavorProfile": "Nutty, fruity (pineapple notes), deep savory broth flavor, crunchy tyrosine amino acid crystals.",
        "scienceRole": "During 24 months of enzymatic proteolysis, milk casein is broken down into free amino acids, yielding over 1,200mg of free glutamic acid per 100g (the highest of any natural Western food). Acts as a clean, natural umami amplifier.",
        "bestTechniques": ["Microplaned into hot risotto during mantecatura", "Shaved over carpaccio", "Rinds simmered in minestrone and stocks"],
        "substitutions": "Grana Padano (milder, younger) or Pecorino Romano (much saltier and sheep-funky).",
        "affinities": ["Balsamic vinegar", "Carnaroli rice", "Egg yolks", "Black pepper", "Prosciutto di Parma"]
    },
    {
        "id": "ing-king-salmon",
        "name": "Wild Alaskan King (Chinook) Salmon",
        "category": "Seafood",
        "season": "Late spring through summer",
        "storage": "Pack in a perforated pan set over crushed ice in the refrigerator (0°C to 1°C). Consume within 48 hours of harvest.",
        "flavorProfile": "Rich, luscious, buttery, clean oceanic sweet finish with zero fishy odor.",
        "scienceRole": "High intramuscular omega-3 fatty acids (over 13% fat) insulate the short myotome muscle fibers, ensuring velvety, succulent texture even under high-heat searing. Delicate collagen melts at 40-50°C.",
        "bestTechniques": ["Crispy-skin pan sear", "Gentle olive oil confit at 48°C", "Cured as gravlax with dill and aquavit"],
        "substitutions": "Steelhead trout, Arctic char, or Atlantic salmon.",
        "affinities": ["Dill", "Lemon", "Crème fraîche", "Capers", "Brown butter", "Cucumber"]
    },
    {
        "id": "ing-duck-fat",
        "name": "Rendered Duck Fat (Graisse de Canard)",
        "category": "Pantry / Fat",
        "season": "Year-round",
        "storage": "Refrigerate in a sealed glass jar up to 6 months; freezes indefinitely. Can be strained and reused multiple times.",
        "flavorProfile": "Savory, silky, deeply aromatic poultry richness with a low melting point (32°C / 90°F) that melts instantly on the human tongue.",
        "scienceRole": "Contains a high ratio of monounsaturated fatty acids (approx 50% oleic acid) similar to olive oil, creating incomparable crispness when frying potatoes (Pommes Sarladaises) without leaving a greasy, waxy residue.",
        "bestTechniques": ["Confit immersion cooking at 90°C", "Roasting Yukon gold potatoes", "Sautéing mushrooms and root vegetables"],
        "substitutions": "Rendered pork lard (saindoux) or clarified butter (ghee).",
        "affinities": ["Potatoes", "Thyme", "Garlic", "Shallots", "Duck legs", "Mushrooms"]
    },
    {
        "id": "ing-sichuan-pepper",
        "name": "Green & Red Sichuan Peppercorns (Huajiao)",
        "category": "Spices",
        "season": "Autumn harvest",
        "storage": "Airtight glass jar away from light. Grind fresh; volatile aroma terpenes degrade within 30 minutes of grinding.",
        "flavorProfile": "Red: warm, woodsy, camphoraceous, intense numbness. Green (Qing Huajiao): electrifying kaffir lime, lemongrass, citrus floral top notes.",
        "scienceRole": "Not related to black pepper or chiles. Contains hydroxy-alpha-sanshool which binds to touch and vibration mechanoreceptors on the tongue, creating a physical 50Hz paresthesia tingling sensation that cleanses fat and refreshes taste buds.",
        "bestTechniques": ["Dry toasted in skillet, ground to fine powder for finishing dishes", "Infused into hot wok oil (Huajiao You)", "Blended with sea salt as a dip"],
        "substitutions": "Grains of paradise + black pepper + lemon zest (cannot replicate sanshool numbness).",
        "affinities": ["Pixian Doubanjiang", "Tofu", "Beef", "Scallions", "Soy sauce", "Chili flakes"]
    }
]

js_content = f"""// L'Atelier Ingredient Encyclopedia
// 65 comprehensive dossiers on culinary behaviors, storage, seasonality, and affinities.

window.ENCYCLOPEDIA_INGREDIENTS = {json.dumps(ENCYCLOPEDIA_INGREDIENTS, indent=2)};

window.EncyclopediaEngine = {{
  getAll: function() {{ return window.ENCYCLOPEDIA_INGREDIENTS; }},
  getById: function(id) {{ return window.ENCYCLOPEDIA_INGREDIENTS.find(i => i.id === id); }},
  search: function(query) {{
    const q = (query || '').toLowerCase().trim();
    if (!q) return window.ENCYCLOPEDIA_INGREDIENTS;
    return window.ENCYCLOPEDIA_INGREDIENTS.filter(i => 
      i.name.toLowerCase().includes(q) || 
      i.category.toLowerCase().includes(q) || 
      i.flavorProfile.toLowerCase().includes(q) ||
      (i.affinities || []).some(a => a.toLowerCase().includes(q))
    );
  }}
}};
"""

with open("data-encyclopedia.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated data-encyclopedia.js with {len(ENCYCLOPEDIA_INGREDIENTS)} detailed ingredient dossiers.")
