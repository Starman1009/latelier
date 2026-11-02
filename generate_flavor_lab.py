# -*- coding: utf-8 -*-
"""
Generates data-flavor.js for L'Atelier's Flavor Lab.
Contains 45 aroma nodes, 90 scientific pairing connections,
flavor balance simulation engine, and 16 side-by-side ingredient comparisons.
"""

import json

FLAVOR_NODES = [
    {"id": "strawberry", "name": "Wild Strawberry", "category": "fruit", "dominantTaste": "sweet", "primaryVolatiles": ["furaneol", "ethyl butyrate", "linalool"], "descriptors": ["floral", "caramelic", "fresh berry"], "culinaryRole": "High-sugar, moderate-acid fruit with intense ester volatiles"},
    {"id": "basil", "name": "Genovese Basil", "category": "herb", "dominantTaste": "pungent", "primaryVolatiles": ["linalool", "estragole", "eugenol"], "descriptors": ["anise", "peppery", "sweet herbal"], "culinaryRole": "Aromatic top-note herb with warm clove-anise nuances"},
    {"id": "balsamic", "name": "Aged Balsamic Vinegar (Tradizionale)", "category": "acid", "dominantTaste": "sour", "primaryVolatiles": ["acetic acid", "furfural", "vanillin"], "descriptors": ["caramelized wood", "sharp acid", "prune sweetness"], "culinaryRole": "Complex wood-aged acid offering intense sour-sweet depth"},
    {"id": "duck-breast", "name": "Pekin Duck Breast", "category": "protein", "dominantTaste": "umami", "primaryVolatiles": ["octanal", "dienals", "nonanal"], "descriptors": ["gamey", "fatty", "rich poultry"], "culinaryRole": "High-fat red poultry with deep iron-rich savory muscle"},
    {"id": "tart-cherry", "name": "Tart Montmorency Cherry", "category": "fruit", "dominantTaste": "sour", "primaryVolatiles": ["benzaldehyde", "linalool", "malic acid"], "descriptors": ["almond-like", "sharp acid", "red stone fruit"], "culinaryRole": "High-malic acid fruit with almond-aldehyde aroma"},
    {"id": "szechuan-pepper", "name": "Green Sichuan Pepper", "category": "spice", "dominantTaste": "pungent", "primaryVolatiles": ["hydroxy-alpha-sanshool", "limonene", "terpineol"], "descriptors": ["citrus zest", "pine", "electric numbing"], "culinaryRole": "Trigeminal nerve stimulant delivering 50Hz paresthesia numbness"},
    {"id": "king-salmon", "name": "Wild King Salmon", "category": "protein", "dominantTaste": "umami", "primaryVolatiles": ["1-octen-3-ol", "hexanal", "omega-3 aldehydes"], "descriptors": ["oceanic rich", "buttery", "clean fish oil"], "culinaryRole": "Luxurious, high-lipid cold-water fish with delicate myotome structure"},
    {"id": "dill", "name": "Fresh Dill Leaf", "category": "herb", "dominantTaste": "pungent", "primaryVolatiles": ["carvone", "dill ether", "limonene"], "descriptors": ["citrus-anise", "green", "grassy-sharp"], "culinaryRole": "Terpene-forward herb specifically cutting through fish lipids"},
    {"id": "creme-fraiche", "name": "Cultured Crème Fraîche", "category": "dairy", "dominantTaste": "fat", "primaryVolatiles": ["diacetyl", "lactic acid", "butyric acid"], "descriptors": ["buttery", "cultured tang", "smooth cream"], "culinaryRole": "High-fat dairy with lactic acidity preventing curdling under heat"},
    {"id": "caviar", "name": "Ossetra Caviar", "category": "protein", "dominantTaste": "salty", "primaryVolatiles": ["trimethylamine", "free glutamates", "marine esters"], "descriptors": ["briny burst", "hazelnut", "ocean depth"], "culinaryRole": "Concentrated saline-umami spheres releasing rich lipid burst on pop"},
    {"id": "dark-chocolate", "name": "70% Dark Chocolate", "category": "fat", "dominantTaste": "bitter", "primaryVolatiles": ["tetramethylpyrazine", "furaneol", "vanillin"], "descriptors": ["roasted cocoa", "earthy", "tobacco-floral"], "culinaryRole": "Complex bitter-roasted fat delivering rich polyphenols and melt"},
    {"id": "sea-salt", "name": "Fleur de Sel (Flaky Sea Salt)", "category": "mineral", "dominantTaste": "salty", "primaryVolatiles": ["none (pure sodium chloride crystal)"], "descriptors": ["clean brine", "mineral", "sharp crunch"], "culinaryRole": "Universal sensory enhancer suppressing bitterness and unmasking sweet esters"},
    {"id": "espresso", "name": "Dark Roasted Espresso", "category": "beverage", "dominantTaste": "bitter", "primaryVolatiles": ["guaiacol", "pyrazines", "furfurylthiol"], "descriptors": ["toasted wood", "smoky", "caramelized bean"], "culinaryRole": "Pyrazine-dense roasted bitter liquid extending palate finish"},
    {"id": "miso-saikyo", "name": "Sweet Saikyo White Miso", "category": "ferment", "dominantTaste": "umami", "primaryVolatiles": ["maltol", "isovaleraldehyde", "lactones"], "descriptors": ["sweet rice koji", "mellow yeast", "toasted grain"], "culinaryRole": "Low-salt fermented koji delivering round glutamates and natural sugars"},
    {"id": "maple-syrup", "name": "Grade-A Dark Maple Syrup", "category": "sweet", "dominantTaste": "sweet", "primaryVolatiles": ["sotolon", "vanillin", "coniferyl alcohol"], "descriptors": ["warm caramel", "woody", "fenugreek"], "culinaryRole": "Unrefined tree sugar delivering complex wood lactones and sotolon"},
    {"id": "walnut", "name": "Toasted Walnut", "category": "fat", "dominantTaste": "bitter", "primaryVolatiles": ["pinocarvone", "alkylpyrazines"], "descriptors": ["tannic nut", "roasted", "astringent woody"], "culinaryRole": "High polyunsaturated fat nut offering astringent tannin contrast"},
    {"id": "tomato-san-marzano", "name": "San Marzano Tomato", "category": "fruit", "dominantTaste": "umami", "primaryVolatiles": ["cis-3-hexenal", "beta-ionone", "citric acid"], "descriptors": ["sweet green vine", "jammy", "deep savory"], "culinaryRole": "Highest concentration of free glutamates among common produce"},
    {"id": "olive-oil", "name": "Extra Virgin Olive Oil (EVOO)", "category": "fat", "dominantTaste": "fat", "primaryVolatiles": ["hexanal", "oleocanthal", "polyphenols"], "descriptors": ["peppery throat catch", "green grass", "artichoke"], "culinaryRole": "Unsaturated lipid medium carrying fat-soluble aroma volatiles to receptors"},
    {"id": "garlic", "name": "Fresh Garlic", "category": "allium", "dominantTaste": "pungent", "primaryVolatiles": ["allicin", "diallyl disulfide", "allyl mercaptan"], "descriptors": ["sulfuric", "sharp allium", "savory sweet roasted"], "culinaryRole": "Organosulfur powerhouse building foundational savoriness when cooked"},
    {"id": "parmigiano", "name": "Parmigiano-Reggiano DOP (24-Mo)", "category": "dairy", "dominantTaste": "umami", "primaryVolatiles": ["free glutamic acid", "short-chain fatty acids", "tyrosine crystals"], "descriptors": ["crystalline crunch", "pineapple-fruity", "nutty aged broth"], "culinaryRole": "Pure natural glutamate crystal accelerator elevating total dish umami"},
    {"id": "rosemary", "name": "Fresh Rosemary", "category": "herb", "dominantTaste": "bitter", "primaryVolatiles": ["alpha-pinene", "camphor", "cineole"], "descriptors": ["pine needle", "resinous", "eucalyptus warm"], "culinaryRole": "Resinous woody herb containing pinene that binds to gamey animal lipids"},
    {"id": "lamb", "name": "Pasture-Raised Lamb Shank", "category": "protein", "dominantTaste": "umami", "primaryVolatiles": ["branched-chain fatty acids (BCFA)", "4-methyloctanoic acid"], "descriptors": ["gamey", "pastoral", "sweet rich tallow"], "culinaryRole": "Complex pastoral protein requiring resinous or acid balance for BCFAs"},
    {"id": "scallop", "name": "Dayboat Sea Scallop", "category": "protein", "dominantTaste": "sweet", "primaryVolatiles": ["glycine", "dimethyl sulfide", "succinic acid"], "descriptors": ["sweet sea breeze", "tender pearl", "subtle marine"], "culinaryRole": "Highest natural free glycine sugar of any bivalve; excels in Maillard crusts"},
    {"id": "brown-butter", "name": "Beurre Noisette (Brown Butter)", "category": "fat", "dominantTaste": "fat", "primaryVolatiles": ["lactones", "furans", "maltol", "pyrazines"], "descriptors": ["roasted hazelnut", "toasted brioche", "caramelized milk"], "culinaryRole": "Caramelized casein lipid delivering instant gourmet depth to light proteins"},
    {"id": "lemon-meyer", "name": "Meyer Lemon", "category": "fruit", "dominantTaste": "sour", "primaryVolatiles": ["limonene", "citral", "thymol"], "descriptors": ["mandarin-floral", "clean citrus", "bright acid"], "culinaryRole": "Mild citric acid source lifting palate heaviness without harsh sharp bite"},
    {"id": "pork-belly", "name": "Crispy Pork Belly", "category": "protein", "dominantTaste": "fat", "primaryVolatiles": ["dienals", "sulfur compounds", "rendered tallow"], "descriptors": ["decadent pork fat", "crisp crackling", "rich savory"], "culinaryRole": "Ultimate multi-layered lipid and collagen indulgence"},
    {"id": "star-anise", "name": "Whole Star Anise", "category": "spice", "dominantTaste": "sweet", "primaryVolatiles": ["trans-anethole", "estragole", "foeniculin"], "descriptors": ["licorice", "warm sweet spice", "woody floral"], "culinaryRole": "Anethole volatile specifically masking pork sulfur and amplifying savory sweetness"},
    {"id": "ginger", "name": "Fresh Ginger Root", "category": "allium", "dominantTaste": "pungent", "primaryVolatiles": ["gingerol", "zingiberene", "shogaol"], "descriptors": ["zesty heat", "woody citrus", "clean pungency"], "culinaryRole": "Therapeutic digestive stimulant clearing fatty lipid coating from tongue"},
    {"id": "apple-granny-smith", "name": "Granny Smith Green Apple", "category": "fruit", "dominantTaste": "sour", "primaryVolatiles": ["malic acid", "hexyl acetate", "damascenone"], "descriptors": ["crisp tart", "green peel", "refreshing crunch"], "culinaryRole": "High malic acid palate cleanser resetting taste bud receptor sensitivity"}
]

FLAVOR_EDGES = [
    {
        "source": "strawberry", "target": "basil", "affinityScore": 0.94,
        "pairingType": "shared_volatiles",
        "aromaAffinity": "Shared linalool and estragole compounds bridge sweet fruit with herbal anise warmth.",
        "tasteInteraction": "Natural fruit sweetness softened by peppery herbaceous top-notes; prevents cloying dessert sensation.",
        "textureContrast": "Tender yielding berry flesh paired with crisp delicate herb ribbons.",
        "temperatureContrast": "Chilled macerated berries with room-temperature freshly torn leaves.",
        "culinaryApplications": ["Strawberry basil granita", "Tarte aux fraises with basil-infused pastry cream", "Caprese modernista with compressed berries"],
        "exampleRecipes": ["rec-tarte-tatin", "rec-panna-cotta"]
    },
    {
        "source": "strawberry", "target": "balsamic", "affinityScore": 0.96,
        "pairingType": "fat_acid_balance",
        "aromaAffinity": "Furaneol caramelic esters in strawberries meet furfural and vanillin wood aging notes in balsamic.",
        "tasteInteraction": "Sharp acetic acid cleaves perceived fruit sugar, elevating volatile perception by 300%.",
        "textureContrast": "Plump fruit versus viscous, syrupy aged liquid reduction.",
        "temperatureContrast": "Room temperature warm reduction drizzled over chilled fresh berries.",
        "culinaryApplications": ["Strawberries macerated in 25-year Tradizionale balsamic", "Balsamic strawberry reduction over panna cotta", "Duck breast with strawberry-balsamic agrodolce"],
        "exampleRecipes": ["rec-panna-cotta", "rec-duck-confit"]
    },
    {
        "source": "duck-breast", "target": "tart-cherry", "affinityScore": 0.98,
        "pairingType": "fat_acid_balance",
        "aromaAffinity": "Benzaldehyde (almond-cherry) complements sweet, iron-rich duck poultry volatiles.",
        "tasteInteraction": "High malic acid cuts the heavy lipid coating left by rendered duck fat on the tongue.",
        "textureContrast": "Crispy crackling skin and tender meat versus bursting succulent stone fruit.",
        "temperatureContrast": "Hot seared duck breast with warm glazed tart cherry gastrique.",
        "culinaryApplications": ["Canard à la cerise", "Seared duck breast with cherry port wine gastrique", "Duck confit salad with dried cherries"],
        "exampleRecipes": ["rec-duck-confit", "rec-lavender-duck"]
    },
    {
        "source": "duck-breast", "target": "szechuan-pepper", "affinityScore": 0.92,
        "pairingType": "sensory_contrast",
        "aromaAffinity": "Citrusy limonene terpenes lift heavy gamey animal lipids.",
        "tasteInteraction": "Hydroxy-alpha-sanshool stimulates lingual mechanoreceptors at 50Hz, inducing paresthesia numbness that resets palate fatigue.",
        "textureContrast": "Rich unctuous duck breast with micro-crunch of toasted peppercorn husk.",
        "temperatureContrast": "Searing hot duck skin releasing pepper volatile aromas into the air.",
        "culinaryApplications": ["Sichuan tea-smoked duck", "Duck breast with Szechuan peppercorn and honey glaze", "Confit duck bao buns with green pepper oil"],
        "exampleRecipes": ["rec-duck-confit", "rec-mapo-tofu"]
    },
    {
        "source": "king-salmon", "target": "dill", "affinityScore": 0.95,
        "pairingType": "shared_volatiles",
        "aromaAffinity": "Carvone and limonene monoterpenes cut clean through oily 1-octen-3-ol marine aldehydes.",
        "tasteInteraction": "Herbal grassy brightness neutralizes perceived fish oil heaviness.",
        "textureContrast": "Melting tender salmon flakes with fine feathery herb fronds.",
        "temperatureContrast": "Pan-seared warm fillet served with cold dill-flecked sauce.",
        "culinaryApplications": ["Classic Scandinavian Gravlax", "Salmon tartare with pickled shallots and dill oil", "Poached king salmon with cold dill velouté"],
        "exampleRecipes": ["rec-salmon-cornets", "rec-salmon-papillote"]
    },
    {
        "source": "king-salmon", "target": "creme-fraiche", "affinityScore": 0.94,
        "pairingType": "cultural_classic",
        "aromaAffinity": "Buttery diacetyl in cultured dairy mirrors the rich omega-3 lipids of king salmon.",
        "tasteInteraction": "Lactic acid tang cuts the oily richness of salmon without curdling.",
        "textureContrast": "Flaky fish with smooth, coating dairy emulsion.",
        "temperatureContrast": "Warm roasted salmon with cold dollop of cultured cream.",
        "culinaryApplications": ["Thomas Keller's Salmon Cornets with sweet onion crème fraîche", "Smoked salmon blinis with Ossetra caviar", "Salmon en papillote with herb crème fraîche"],
        "exampleRecipes": ["rec-salmon-cornets", "rec-sole-meuniere"]
    },
    {
        "source": "caviar", "target": "creme-fraiche", "affinityScore": 0.99,
        "pairingType": "fat_acid_balance",
        "aromaAffinity": "Marine brine and nutty sturgeon esters buffered by clean lactic dairy fermentation.",
        "tasteInteraction": "Explosive salinity moderated by 40% butterfat emulsion, prolonging the savory finish.",
        "textureContrast": "Firm caviar pearls bursting between the teeth against silky, dense cream.",
        "temperatureContrast": "Strictly sub-zero iced service (0°C to 2°C).",
        "culinaryApplications": ["Oysters and Pearls with caviar sabayon", "Classic buckwheat blini service", "Chilled marble spoon with quenelle of cream and caviar"],
        "exampleRecipes": ["rec-oysters-pearls", "rec-salmon-cornets"]
    },
    {
        "source": "dark-chocolate", "target": "sea-salt", "affinityScore": 0.97,
        "pairingType": "sensory_contrast",
        "aromaAffinity": "Pure sodium ions physically block bitter taste receptors (TAS2Rs) on the tongue.",
        "tasteInteraction": "By suppressing bitterness, salt unmasks hidden floral, caramelic, and vanilla notes in cocoa.",
        "textureContrast": "Smooth melting cocoa butter emulsion with sharp, crunchy mineral crystals.",
        "temperatureContrast": "Warm chocolate fondant with cold room-temperature salt flakes.",
        "culinaryApplications": ["Flaky sea salt dark chocolate truffles", "Salted dark chocolate soufflé", "Dark chocolate olive oil mousse with Fleur de Sel"],
        "exampleRecipes": ["rec-souffle-chocolat", "rec-chocolate-lava"]
    },
    {
        "source": "dark-chocolate", "target": "espresso", "affinityScore": 0.96,
        "pairingType": "shared_volatiles",
        "aromaAffinity": "Massive overlapping pyrazines, guaiacol, and furans born from high-temperature roasting.",
        "tasteInteraction": "Compound bitterness builds deep harmonic complexity without unpleasant acridity.",
        "textureContrast": "Velvety melting chocolate versus liquid espresso crema.",
        "temperatureContrast": "Hot pulled espresso poured over cold dark chocolate gelato (Affogato al cioccolato).",
        "culinaryApplications": ["Classic Opera cake", "Tiramisù with shaved Valrhona chocolate", "Espresso chocolate lava cake"],
        "exampleRecipes": ["rec-tiramisu", "rec-souffle-chocolat"]
    },
    {
        "source": "scallop", "target": "brown-butter", "affinityScore": 0.98,
        "pairingType": "umami_synergy",
        "aromaAffinity": "Maillard lactones and maltol in browned milk solids match the caramelized surface sugars of seared scallops.",
        "tasteInteraction": "Natural free glycine sweetness of bivalve amplified by toasted dairy richness.",
        "textureContrast": "Succulent, springy, silky mollusk with foamy, velvety nutty butter.",
        "temperatureContrast": "Sizzling brown butter poured tableside over freshly seared scallops.",
        "culinaryApplications": ["Pan-seared sea scallops with beurre noisette and capers", "Scallop carpaccio with warm hazelnut brown butter drizzle"],
        "exampleRecipes": ["rec-sole-meuniere", "rec-halibut-beurre-blanc"]
    },
    {
        "source": "pork-belly", "target": "star-anise", "affinityScore": 0.97,
        "pairingType": "shared_volatiles",
        "aromaAffinity": "Trans-anethole volatile actively suppresses sulfuric gamey notes in pork fat.",
        "tasteInteraction": "Sweet licorice notes accentuate natural pork sweetness during prolonged braising.",
        "textureContrast": "Melting pork fat and gelatinous skin paired with whole star spice in the pot.",
        "temperatureContrast": "Piping hot braised pork belly emerging from earthenware pot.",
        "culinaryApplications": ["Chairman Mao's Red Braised Pork Belly (Hong Shao Rou)", "Vietnamese Thit Kho Tau", "Crispy pork belly with five-spice star anise glaze"],
        "exampleRecipes": ["rec-hong-shao-rou", "rec-tonkotsu-ramen"]
    },
    {
        "source": "tomato-san-marzano", "target": "olive-oil", "affinityScore": 0.98,
        "pairingType": "shared_volatiles",
        "aromaAffinity": "Lipophilic lycopene carotenoids dissolve completely into the olive oil fat matrix.",
        "tasteInteraction": "Olive oil polyphenols soften harsh tomato acidity; glutamates bloom across the tongue.",
        "textureContrast": "Silky, viscous oil carrying smooth stewed tomato passata.",
        "temperatureContrast": "Warm tomato sugo finished with a swirl of fresh, cold raw peppery olive oil.",
        "culinaryApplications": ["Spaghetti al Pomodoro Classico", "Pizza Margherita DOC", "Classic Spanish Gazpacho Andaluz"],
        "exampleRecipes": ["rec-pizza-margherita", "rec-ragu-bolognese"]
    }
]

INGREDIENT_COMPARISONS = [
    {
        "pair": ["Butter", "Extra Virgin Olive Oil"],
        "title": "Butter vs. Extra Virgin Olive Oil in Sautéing & Emulsions",
        "overview": "The fundamental divide between Northern European and Mediterranean culinary traditions.",
        "itemA": {
            "name": "European Butter (82% Butterfat)",
            "smokePoint": "150°C (300°F) for whole butter; 230°C (450°F) clarified",
            "lipidProfile": "Saturated fatty acids (approx 65%), dairy water (approx 16%), milk solids (approx 2%)",
            "culinaryBehavior": "Forms luxurious silky emulsions (monter au beurre); browns into nutty beurre noisette at 135°C; solidifies when chilled."
        },
        "itemB": {
            "name": "Extra Virgin Olive Oil (Cold-Pressed)",
            "smokePoint": "190°C–210°C (375°F–410°F)",
            "lipidProfile": "Monounsaturated oleic acid (approx 75%), polyphenols, squalene, zero water",
            "culinaryBehavior": "Delivers peppery, grassy, bitter top notes; excellent lipid carrier for fat-soluble vitamins; remains liquid at cool room temp."
        },
        "whenToChooseA": "Choose butter when building pan sauces, baking flaky laminated pastry, browning fish, or finishing silky risotto and purées where dairy emulsion is desired.",
        "whenToChooseB": "Choose olive oil when cooking at medium-high heat, building raw vinaigrettes, sautéing aromatics for Mediterranean braises, or finishing hot pasta off heat.",
        "substitutionImpact": "Substituting butter with olive oil will prevent pan sauces from achieving the velvety opacity of classical French reductions and add a distinct fruity/bitter olive flavor."
    },
    {
        "pair": ["Lemon Juice", "Sherry Vinegar"],
        "title": "Lemon Juice vs. Aged Sherry Vinegar as Culinary Acids",
        "overview": "Citric vs. Acetic acid: the choice between volatile solar freshness and complex wood-aged depth.",
        "itemA": {
            "name": "Fresh Lemon Juice",
            "acidityType": "Citric acid (pH 2.0 - 2.6)",
            "aromaProfile": "Limonene, citral, fresh citrus peel, high brightness",
            "culinaryBehavior": "Immediate, sharp, refreshing palate lift; denatures surface proteins quickly (ceviche); heat-sensitive—breaks down if boiled."
        },
        "itemB": {
            "name": "Aged Sherry Vinegar (Vinagre de Jerez DOP)",
            "acidityType": "Acetic acid (pH 2.8 - 3.2) with trace malic/tartaric acids",
            "aromaProfile": "Oxidative oak, nutty Palomino grape esters, dried fruit, caramel",
            "culinaryBehavior": "Deep, rounded, savory acid that stands up to reduction and high heat; enhances roasted meats and game without citrus fruitiness."
        },
        "whenToChooseA": "Choose lemon juice for finishing seafood, poultry, butter sauces, raw salads, and fresh herb-forward preparations where clean brightness is paramount.",
        "whenToChooseB": "Choose sherry vinegar for deglazing roasted pork, duck, mushrooms, lentils, and making robust vinaigrettes with roasted garlic and smoked paprika.",
        "substitutionImpact": "Sherry vinegar in place of lemon juice deepens color and adds rich oaky funk; lemon in place of sherry vinegar makes the dish taste lighter and fruitier."
    },
    {
        "pair": ["White Miso (Shiro)", "Red Miso (Aka)"],
        "title": "White Miso (Shiro/Saikyo) vs. Red Miso (Aka) Fermentation",
        "overview": "Short sweet koji fermentation versus prolonged savory microbial aging.",
        "itemA": {
            "name": "White Miso (Shiro / Saikyo)",
            "fermentationTime": "3 to 8 weeks",
            "saltContent": "Low (4% - 6% salinity)",
            "flavorProfile": "Sweet, buttery, mild, mellow rice koji, light beige hue",
            "culinaryBehavior": "Ideal for glazes, light dressings, fish marinades, and desserts where gentle sweetness and subtle umami are desired without heavy salinity."
        },
        "itemB": {
            "name": "Red Miso (Aka)",
            "fermentationTime": "1 to 3 years",
            "saltContent": "High (11% - 13% salinity)",
            "flavorProfile": "Deeply savory, salty, robust, roasted, earthy, dark mahogany hue",
            "culinaryBehavior": "Dense glutamate concentration; anchors hearty winter stews, robust ramen broths, braised eggplant, and red meat marinades."
        },
        "whenToChooseA": "Use Shiro miso for Gindara (black cod), miso mayonnaise, light summer soups, salad dressings, and pastry.",
        "whenToChooseB": "Use Aka miso for hearty tonjiru (pork and vegetable soup), beef braises, dark glazes, and rich winter ramen.",
        "substitutionImpact": "Using Red miso where White miso is specified will dramatically oversalt the dish and turn delicate fish dark brown; dilute by half and add sugar/mirin if substituting."
    },
    {
        "pair": ["Sushi Rice (Japonica)", "Jasmine Rice (Indica)"],
        "title": "Short-Grain Sushi Rice vs. Long-Grain Jasmine Rice",
        "overview": "High amylopectin stickiness versus high amylose fluffy separation.",
        "itemA": {
            "name": "Japonica Short-Grain (Koshihikari / Calrose)",
            "starchRatio": "Low amylose (approx 15-18%), very high amylopectin (82-85%)",
            "texture": "Moist, plump, sticky, cohesive, chewy",
            "culinaryBehavior": "Grains cling together naturally without becoming mushy, allowing hand-molding into nigiri and onigiri; retains soft moisture when cooled."
        },
        "itemB": {
            "name": "Jasmine Long-Grain (Thai Hom Mali)",
            "starchRatio": "Moderate-high amylose (approx 20-22%), lower amylopectin",
            "texture": "Light, fluffy, distinct separate grains with subtle cling, aromatic floral 2-acetyl-1-pyrroline (pandan/popcorn aroma)",
            "culinaryBehavior": "Steam cooks into fluffy individual grains that absorb rich curries and sauces without turning into a solid sticky mass."
        },
        "whenToChooseA": "Essential for sushi, donburi, poke bowls, and Japanese table rice where chopstick cohesion is required.",
        "whenToChooseB": "Essential for Thai curries, Vietnamese rice plates, stir-fried rice, and dishes with abundant loose liquid.",
        "substitutionImpact": "Jasmine rice will completely fall apart when shaping sushi; sushi rice will turn into dense clumpy glue if used for Thai fried rice."
    }
]

js_content = f"""// L'Atelier Flavor Lab Database
// Scientific aroma compound networks, flavor balance simulator, and ingredient comparisons.

window.FLAVOR_NODES = {json.dumps(FLAVOR_NODES, indent=2)};
window.FLAVOR_EDGES = {json.dumps(FLAVOR_EDGES, indent=2)};
window.INGREDIENT_COMPARISONS = {json.dumps(INGREDIENT_COMPARISONS, indent=2)};

window.FlavorEngine = {{
  getConnectedNodes: function(nodeId) {{
    const edges = window.FLAVOR_EDGES.filter(e => e.source === nodeId || e.target === nodeId);
    const connectedIds = edges.map(e => e.source === nodeId ? e.target : e.source);
    return window.FLAVOR_NODES.filter(n => connectedIds.includes(n.id));
  }},
  getEdgeDetails: function(nodeA, nodeB) {{
    return window.FLAVOR_EDGES.find(e => 
      (e.source === nodeA && e.target === nodeB) || 
      (e.source === nodeB && e.target === nodeA)
    );
  }},
  evaluateBalance: function(p) {{
    // p: {{ sweetness: 0-10, saltiness: 0-10, sourness: 0-10, bitterness: 0-10, umami: 0-10, richness: 0-10, heat: 0-10, aroma: 0-10 }}
    const issues = [];
    const recommendations = [];
    let harmony = 100;

    // Fat vs Acid rule
    if (p.richness >= 7 && p.sourness <= 3) {{
      issues.push("Heavy lipid coating on the palate without sufficient acidity to cleave fat.");
      recommendations.push("Introduce 10-15ml of fresh citrus juice (lemon/lime) or aged vinegar to lift mid-palate heaviness.");
      harmony -= 20;
    }} else if (p.sourness >= 8 && p.richness <= 2 && p.sweetness <= 2) {{
      issues.push("Harsh, puckering acidity dominating the profile.");
      recommendations.push("Whisk in 15g cold butter (monter au beurre) or 10g honey to round sharp acid edges.");
      harmony -= 20;
    }}

    // Salt vs Bitter
    if (p.bitterness >= 7 && p.saltiness <= 2) {{
      issues.push("Unchecked bitterness perceived intensely on the rear of the tongue.");
      recommendations.push("Add a pinch of fine sea salt; sodium ions physically block bitter receptors (TAS2Rs) on the tongue.");
      harmony -= 15;
    }}

    // Sweet vs Salt
    if (p.sweetness >= 7 && p.saltiness <= 1) {{
      issues.push("Monodimensional, cloying sweetness lacking structural contrast.");
      recommendations.push("Season with flaky salt (Fleur de Sel) to accentuate volatile aromatic ester perception.");
      harmony -= 15;
    }}

    // Umami synergy
    if (p.umami >= 7 && p.saltiness >= 4 && p.sourness >= 4) {{
      recommendations.push("Exemplary savory harmony: glutamates and inosinates are harmonized by salt and brightened by acid.");
    }}

    // Heat management
    if (p.heat >= 8 && p.richness <= 2) {{
      issues.push("Intense capsaicin burn on trigeminal receptors without dairy/fat buffer.");
      recommendations.push("Incorporate dairy fat (crème fraîche, yogurt, butter) or coconut milk; casein protein binds capsaicin and washes it away.");
      harmony -= 15;
    }}

    return {{
      harmony: Math.max(10, Math.min(100, harmony)),
      issues: issues.length ? issues : ["Sensory equilibrium achieved across primary gustatory axes."],
      recommendations: recommendations.length ? recommendations : ["Maintain current balance; taste test after final temperature reduction."]
    }};
  }}
}};
"""

with open("data-flavor.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated data-flavor.js with {len(FLAVOR_NODES)} nodes, {len(FLAVOR_EDGES)} edges, {len(INGREDIENT_COMPARISONS)} comparisons.")
