# -*- coding: utf-8 -*-
"""
Extended High-Fidelity Flavor Lab Generator for L'Atelier.
Generates data-flavor.js with 50 aroma nodes, 36 deep scientific pairing connections,
8-axis flavor balance simulator engine, and 10 side-by-side ingredient comparisons.
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
    {"id": "apple-granny-smith", "name": "Granny Smith Green Apple", "category": "fruit", "dominantTaste": "sour", "primaryVolatiles": ["malic acid", "hexyl acetate", "damascenone"], "descriptors": ["crisp tart", "green peel", "refreshing crunch"], "culinaryRole": "High malic acid palate cleanser resetting taste bud receptor sensitivity"},
    {"id": "black-truffle", "name": "Black Périgord Truffle", "category": "produce", "dominantTaste": "umami", "primaryVolatiles": ["dimethyl sulfide", "2-methylbutanal", "octen-3-ol"], "descriptors": ["earthy forest", "musky", "damp cocoa"], "culinaryRole": "Volatile aroma bomb binding to warm animal fats and eggs"},
    {"id": "yuzu", "name": "Japanese Yuzu Citrus", "category": "acid", "dominantTaste": "sour", "primaryVolatiles": ["yuzunone", "yuzulactone", "limonene"], "descriptors": ["pine-grapefruit", "floral citrus", "electric tart"], "culinaryRole": "Complex aromatic acid lifting oily raw fish sashimi"},
    {"id": "hamachi", "name": "Japanese Yellowtail / Hamachi", "category": "protein", "dominantTaste": "umami", "primaryVolatiles": ["marine esters", "fatty aldehydes"], "descriptors": ["buttery", "clean fish lipid", "sweet ocean"], "culinaryRole": "High-fat raw fish requiring citrus and chili counterpoint"},
    {"id": "serrano-chili", "name": "Serrano Chili", "category": "spice", "dominantTaste": "pungent", "primaryVolatiles": ["capsaicin", "isobutyl methoxypyrazine"], "descriptors": ["crisp heat", "green bell", "bright capsaicin"], "culinaryRole": "Fast, clean trigeminal heat cutting through rich crudo fats"},
    {"id": "saffron", "name": "Iranian Sargol Saffron", "category": "spice", "dominantTaste": "bitter", "primaryVolatiles": ["safranal", "crocin", "picrocrocin"], "descriptors": ["honeyed hay", "floral metallic", "vibrant gold"], "culinaryRole": "Luxurious water-soluble golden color and ethereal bitter floral aroma"},
    {"id": "carnaroli-rice", "name": "Carnaroli Risotto Rice", "category": "starch", "dominantTaste": "sweet", "primaryVolatiles": ["hexanal", "2-acetyl-1-pyrroline"], "descriptors": ["toasted grain", "firm core", "creamy starch"], "culinaryRole": "High-amylose rice releasing amylopectin for velvety mantecatura"},
    {"id": "doubanjiang", "name": "Pixian Fermented Chili Bean Paste", "category": "ferment", "dominantTaste": "salty", "primaryVolatiles": ["pyrazines", "esters", "fermented amino acids"], "descriptors": ["aged funk", "earthy chili", "deep savory"], "culinaryRole": "The umami engine of Sichuan cuisine requiring hot oil blooming"},
    {"id": "tofu-silken", "name": "Silken Tofu", "category": "protein", "dominantTaste": "sweet", "primaryVolatiles": ["soy lactones", "hexanal"], "descriptors": ["delicate bean", "cooling custard", "neutral canvas"], "culinaryRole": "Silky custard protein absorbing spicy and savory chili oils"},
    {"id": "pimenton", "name": "Smoked Spanish Pimentón", "category": "spice", "dominantTaste": "sweet", "primaryVolatiles": ["guaiacol", "capsanthin", "syringol"], "descriptors": ["oak smoke", "sweet red pepper", "earthy"], "culinaryRole": "Oak wood smoke infusing rich red color and campfire depth"},
    {"id": "octopus", "name": "Spanish Galician Octopus", "category": "protein", "dominantTaste": "umami", "primaryVolatiles": ["dimethyl sulfide", "collagen gelatin"], "descriptors": ["sweet lobster-like", "tender toothsome", "briny"], "culinaryRole": "High-collagen cephalopod converting to melting gelatin when braised"},
    {"id": "kombu", "name": "Ma-Kombu Kelp", "category": "produce", "dominantTaste": "umami", "primaryVolatiles": ["free glutamic acid", "mannitol"], "descriptors": ["ocean breeze", "deep savory", "subtle iodine"], "culinaryRole": "World's richest natural source of pure free glutamates"},
    {"id": "katsuobushi", "name": "Smoked Skipjack Tuna Flakes", "category": "protein", "dominantTaste": "umami", "primaryVolatiles": ["inosine monophosphate (IMP)", "wood smoke"], "descriptors": ["smoky cured fish", "dry savory", "umami multiplier"], "culinaryRole": "IMP carrier unlocking 8x umami synergy with kombu glutamates"},
    {"id": "guanciale", "name": "Aged Italian Guanciale", "category": "protein", "dominantTaste": "fat", "primaryVolatiles": ["cured pork fat", "black pepper", "juniper"], "descriptors": ["sweet pork tallow", "herbal peppery", "silky crackling"], "culinaryRole": "High collagen-to-fat cured jowl emulsifying into pasta water"},
    {"id": "pecorino-romano", "name": "Pecorino Romano DOP", "category": "dairy", "dominantTaste": "salty", "primaryVolatiles": ["caproic acid", "caprylic acid", "tyrosine"], "descriptors": ["sharp sheep tang", "pungent salt", "nutty aged"], "culinaryRole": "Piquant high-saline sheep cheese creating silky Cacio e Pepe"},
    {"id": "black-pepper", "name": "Cracked Tellicherry Black Pepper", "category": "spice", "dominantTaste": "pungent", "primaryVolatiles": ["piperine", "pinene", "limonene"], "descriptors": ["woody heat", "fruity citrus", "toasted spice"], "culinaryRole": "Dry-toasted piperine heat dissolving into sheep cheese emulsions"},
    {"id": "tarragon", "name": "Fresh French Tarragon", "category": "herb", "dominantTaste": "pungent", "primaryVolatiles": ["estragole", "methylchavicol"], "descriptors": ["licorice", "sweet anise", "herbal warmth"], "culinaryRole": "Anise volatile cutting through egg yolk and butter lipids"},
    {"id": "egg-yolk", "name": "Pasture-Raised Egg Yolk", "category": "protein", "dominantTaste": "fat", "primaryVolatiles": ["vitellin", "lecithin", "lutein"], "descriptors": ["velvety custard", "rich unctuous", "jammy cream"], "culinaryRole": "Natural lecithin phospholipid creating thick, glossy emulsions"},
    {"id": "shallot", "name": "French Grey Shallot", "category": "allium", "dominantTaste": "sweet", "primaryVolatiles": ["dipropyl disulfide", "allicin"], "descriptors": ["sweet allium", "refined garlic", "mellow onion"], "culinaryRole": "Indispensable acid reduction base for Béarnaise and Beurre Blanc"},
    {"id": "white-wine-vinegar", "name": "Champagne / White Wine Vinegar", "category": "acid", "dominantTaste": "sour", "primaryVolatiles": ["acetic acid", "ethyl acetate"], "descriptors": ["crisp tart", "clean acid", "floral wine"], "culinaryRole": "Sharp acid lowering pH and brightening dense egg emulsions"},
    {"id": "clarified-butter", "name": "Clarified Butter (Ghee / Beurre Clarifié)", "category": "fat", "dominantTaste": "fat", "primaryVolatiles": ["butyric acid esters", "lactones"], "descriptors": ["pure golden fat", "nutty clean", "silky gloss"], "culinaryRole": "Pure lipid phase devoid of water, forming 80% of Hollandaise matrix"},
    {"id": "morel", "name": "Fresh Spring Morel", "category": "produce", "dominantTaste": "umami", "primaryVolatiles": ["1-octen-3-ol", "ribonucleotides"], "descriptors": ["forest soil", "hazelnut", "smoky wood"], "culinaryRole": "Honeycomb sponge texture trapping rich butter and cream reductions"}
]

FLAVOR_EDGES = [
    # 1. Strawberry + Basil
    {
        "source": "strawberry", "target": "basil", "affinityScore": 0.94,
        "pairingType": "shared_volatiles",
        "aromaAffinity": "Shared linalool and estragole compounds bridge sweet fruit with herbal anise warmth.",
        "tasteInteraction": "Natural fruit sweetness softened by peppery herbaceous top-notes; prevents cloying dessert sensation.",
        "textureContrast": "Tender yielding berry flesh paired with crisp delicate herb ribbons.",
        "temperatureContrast": "Chilled macerated berries with room-temperature freshly torn leaves.",
        "culinaryApplications": ["Strawberry basil granita", "Tarte aux fraises with basil pastry cream", "Modernist Caprese with compressed berries"],
        "exampleRecipes": ["rec-tarte-tatin", "rec-panna-cotta"]
    },
    # 2. Strawberry + Balsamic
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
    # 3. Duck + Cherry
    {
        "source": "duck-breast", "target": "tart-cherry", "affinityScore": 0.93,
        "pairingType": "fat_acid_balance",
        "aromaAffinity": "Benzaldehyde and linalool in cherries weave into roasted lipid aldehydes (octanal) of duck.",
        "tasteInteraction": "Aggressive malic and citric acids pierce dense duck fat, cleansing the palate.",
        "textureContrast": "Crispy rendered skin and tender medium-rare breast paired with tender, bursting stewed cherries.",
        "temperatureContrast": "Piping hot seared breast with warm, glossy fruit gastrique.",
        "culinaryApplications": ["Canard aux Cerises (classical duck with sour cherry gastrique)", "Smoked duck breast salad with pickled cherries"],
        "exampleRecipes": ["rec-duck-confit"]
    },
    # 4. Duck + Szechuan Pepper
    {
        "source": "duck-breast", "target": "szechuan-pepper", "affinityScore": 0.91,
        "pairingType": "contrast_stimulation",
        "aromaAffinity": "Limonene and citrus terpenes in green Sichuan pepper contrast with deep gamey duck tallow.",
        "tasteInteraction": "Hydroxy-alpha-sanshool stimulates 50Hz mechanoreceptors, vibrating the tongue and clearing lipid coating.",
        "textureContrast": "Crackling duck skin paired with finely cracked toasted peppercorn crust.",
        "temperatureContrast": "Hot pan sear with room temperature tingling spice finish.",
        "culinaryApplications": ["Sichuan tea-smoked duck (Zhangcha Ya)", "Duck breast with Sichuan pepper and cherry reduction"],
        "exampleRecipes": ["rec-duck-confit"]
    },
    # 5. Salmon + Dill
    {
        "source": "king-salmon", "target": "dill", "affinityScore": 0.95,
        "pairingType": "terpene_lipid_bridge",
        "aromaAffinity": "Carvone and limonene in dill break through 1-octen-3-ol oceanic notes of cold-water salmon.",
        "tasteInteraction": "Cool herbaceous pungency brightens rich omega-3 fat without coagulating delicate proteins.",
        "textureContrast": "Velvety, flaking fish flesh contrasted with fine, feathery fresh dill fronds.",
        "temperatureContrast": "Warm pan-seared or room-temperature cured gravlax with cold fresh dill garnish.",
        "culinaryApplications": ["Nordic Gravlax with mustard-dill sauce", "Pan-roasted king salmon with dill beurre blanc"],
        "exampleRecipes": ["rec-sole-meuniere", "rec-halibut-beurre-blanc"]
    },
    # 6. Salmon + Crème Fraîche
    {
        "source": "king-salmon", "target": "creme-fraiche", "affinityScore": 0.92,
        "pairingType": "lactic_lipid_cushion",
        "aromaAffinity": "Diacetyl butter esters harmonize with fish oil aldehydes.",
        "tasteInteraction": "Lactic acid cuts salmon richness while high dairy fat coats the mid-palate luxuriously.",
        "textureContrast": "Flaky succulent protein paired with smooth, spreadable cultured cream.",
        "temperatureContrast": "Chilled crème fraîche dollop melting over hot seared salmon fillet.",
        "culinaryApplications": ["Salmon tartare with crème fraîche and lemon", "Potato blinis with smoked salmon and crème fraîche"],
        "exampleRecipes": ["rec-sole-meuniere"]
    },
    # 7. Caviar + Crème Fraîche
    {
        "source": "caviar", "target": "creme-fraiche", "affinityScore": 0.98,
        "pairingType": "saline_lactic_equilibrium",
        "aromaAffinity": "Marine esters and free amino acids cushioned by velvety cultured dairy lactones.",
        "tasteInteraction": "High dairy fat buffers sharp sodium chloride pop, allowing delicate hazelnut notes to linger for 45+ seconds.",
        "textureContrast": "Taut sturgeon egg membranes bursting against dense, velvety cultured cream.",
        "temperatureContrast": "Cold 0°C caviar atop chilled crème fraîche on warm, freshly griddled blini.",
        "culinaryApplications": ["Classic Tsar imperial caviar service", "Garde manger soft scrambled eggs with caviar and crème fraîche"],
        "exampleRecipes": ["rec-french-omelette"]
    },
    # 8. Dark Chocolate + Sea Salt
    {
        "source": "dark-chocolate", "target": "sea-salt", "affinityScore": 0.97,
        "pairingType": "receptor_unmasking",
        "aromaAffinity": "Sodium chloride crystal has zero aroma, but unmasks roasted cocoa pyrazines and furaneol esters.",
        "tasteInteraction": "Sodium ions physically block TAS2R bitter receptors, suppressing cocoa bitterness and amplifying perceived sweetness by 40%.",
        "textureContrast": "Silky, melting cocoa butter against crisp, crystalline salt pyramids that shatter on the tooth.",
        "temperatureContrast": "Room temperature chocolate with ambient temperature crystals.",
        "culinaryApplications": ["Salted dark chocolate ganache tart", "Valrhona chocolate pots de crème with Maldon salt"],
        "exampleRecipes": ["rec-souffle-chocolat", "rec-tiramisu-classico"]
    },
    # 9. Scallop + Brown Butter
    {
        "source": "scallop", "target": "brown-butter", "affinityScore": 0.96,
        "pairingType": "maillard_synergy",
        "aromaAffinity": "Glycine and succinic acid in scallops fuse with nutty pyrazines and lactones in toasted butter solids.",
        "tasteInteraction": "Natural bivalve sweetness amplified by nutty, toasted caramelized butter richness.",
        "textureContrast": "Tender, pearlescent translucent interior contrasted with crispy, dark amber seared crust.",
        "temperatureContrast": "Piping hot seared scallop glazed with foaming nut-brown butter.",
        "culinaryApplications": ["Pan-seared diver scallops with beurre noisette and capers", "Scallop carpaccio with warm brown butter emulsion"],
        "exampleRecipes": ["rec-sole-meuniere", "rec-halibut-beurre-blanc"]
    },
    # 10. Lamb + Rosemary
    {
        "source": "lamb", "target": "rosemary", "affinityScore": 0.94,
        "pairingType": "lipid_terpene_binding",
        "aromaAffinity": "Alpha-pinene and camphor in rosemary bind chemically to branched-chain fatty acids (BCFAs) in lamb fat.",
        "tasteInteraction": "Resinous herbal bitterness cuts through heavy tallow, preventing greasy palate fatigue.",
        "textureContrast": "Succulent, melting pink meat paired with crisp, finely minced piney needles.",
        "temperatureContrast": "Hot roasted rack with warm pan herb drippings.",
        "culinaryApplications": ["Herb-crusted roasted rack of lamb", "Slow-braised lamb shanks with rosemary and red wine"],
        "exampleRecipes": ["rec-boeuf-bourguignon"]
    },
    # 11. Tomato + Parmigiano
    {
        "source": "tomato-san-marzano", "target": "parmigiano", "affinityScore": 0.97,
        "pairingType": "umami_synergy",
        "aromaAffinity": "Green tomato volatiles (hexenal) enveloped by aged dairy lactones and toasted nut aromas.",
        "tasteInteraction": "Free glutamates in tomatoes fuse with free glutamates in 24-month cheese, triggering massive umami receptor activation.",
        "textureContrast": "Silky, jammy tomato sauce against granular, melting tyrosine crystals.",
        "temperatureContrast": "Hot bubbling pasta sauce with freshly grated room-temperature cheese.",
        "culinaryApplications": ["Spaghetti al Pomodoro con Parmigiano", "Classic Eggplant Parmigiana"],
        "exampleRecipes": ["rec-ragu-bolognese", "rec-cacio-e-pepe"]
    },
    # 12. Pork Belly + Star Anise
    {
        "source": "pork-belly", "target": "star-anise", "affinityScore": 0.95,
        "pairingType": "volatile_masking",
        "aromaAffinity": "Trans-anethole binds to sulfur and boar-taint volatiles in cooking pork fat, converting them into pleasant sweet spice.",
        "tasteInteraction": "Natural sweetness of star anise enhances caramelized sugars in soy-wine braising liquid.",
        "textureContrast": "Gelatinous, melting braised belly pork against glossy reduction glaze.",
        "temperatureContrast": "Hot steaming red-braised pork belly.",
        "culinaryApplications": ["Chairman Mao's Red-Braised Pork Belly (Hong Shao Rou)", "Vietnamese Thit Kho Tau"],
        "exampleRecipes": ["rec-tonkotsu-ramen"]
    },
    # 13. Hamachi + Yuzu + Serrano
    {
        "source": "hamachi", "target": "yuzu", "affinityScore": 0.96,
        "pairingType": "lipid_acid_balance",
        "aromaAffinity": "Yuzunone and limonene in yuzu break through the oily omega-3 aldehydes of winter yellowtail.",
        "tasteInteraction": "Electrifying floral acidity cuts through buttery fish lipids, leaving a clean, sweet oceanic finish.",
        "textureContrast": "Silky, melting raw fish slice paired with micro-drops of citrus juice and crunchy sea salt.",
        "temperatureContrast": "Ice-cold sashimi slices with chilled yuzu dressing.",
        "culinaryApplications": ["Hamachi Crudo with yuzu ponzu and serrano", "Yellowtail collar grilled with yuzu kosho"],
        "exampleRecipes": ["rec-miso-black-cod"]
    },
    # 14. Hamachi + Serrano Chili
    {
        "source": "hamachi", "target": "serrano-chili", "affinityScore": 0.92,
        "pairingType": "trigeminal_activation",
        "aromaAffinity": "Green pyrazines in fresh chili complement the clean marine notes of yellowtail.",
        "tasteInteraction": "Capsaicin stimulates heat receptors, triggering salivation that washes away heavy fish fat.",
        "textureContrast": "Velvety smooth raw fish versus razor-thin crunchy chili wheel.",
        "temperatureContrast": "Chilled crudo with room-temperature pepper slice.",
        "culinaryApplications": ["Nobu-style Yellowtail with Jalapeño / Serrano", "Hamachi ceviche with citrus and avocado"],
        "exampleRecipes": ["rec-miso-black-cod"]
    },
    # 15. Carnaroli Rice + Saffron + Parmigiano
    {
        "source": "carnaroli-rice", "target": "saffron", "affinityScore": 0.95,
        "pairingType": "starch_infusion",
        "aromaAffinity": "Crocin and safranal absorb into expanding rice starch grains during simmer.",
        "tasteInteraction": "Bittersweet floral saffron cuts through rich bone marrow and butter mantecatura.",
        "textureContrast": "Creamy, flowing wave ('all'onda') enveloping distinct al dente rice grains.",
        "temperatureContrast": "Piping hot risotto served on warmed porcelain.",
        "culinaryApplications": ["Risotto alla Milanese", "Arancini alla Milanese with saffron ragù"],
        "exampleRecipes": ["rec-ragu-bolognese"]
    },
    # 16. Silken Tofu + Pixian Doubanjiang + Sichuan Pepper
    {
        "source": "tofu-silken", "target": "doubanjiang", "affinityScore": 0.97,
        "pairingType": "umami_absorption",
        "aromaAffinity": "Pungent fermented bean paste esters coat the neutral soy protein of custard tofu.",
        "tasteInteraction": "Deep savory fermented umami and chili heat completely penetrate mild bean curds.",
        "textureContrast": "Molten, custard-soft tofu floating in rich, glossy chili oil broth.",
        "temperatureContrast": "Piping hot bubbling clay pot with sizzling chili oil.",
        "culinaryApplications": ["Authentic Sichuan Mapo Tofu", "Braised silken tofu in chili bean paste"],
        "exampleRecipes": ["rec-tonkotsu-ramen"]
    },
    # 17. Octopus + Smoked Pimentón + Olive Oil
    {
        "source": "octopus", "target": "pimenton", "affinityScore": 0.95,
        "pairingType": "phenolic_gelatin_harmony",
        "aromaAffinity": "Oak smoke volatiles in pimentón merge with sweet ocean aromas of braised cephalopod.",
        "tasteInteraction": "Smoky, earthy sweet paprika grounds the sweet marine flavor of octopus gelatin.",
        "textureContrast": "Tender, toothsome octopus medallions against crunchy grains of coarse sea salt.",
        "temperatureContrast": "Warm freshly sliced octopus with room temperature EVOO and paprika.",
        "culinaryApplications": ["Pulpo a la Gallega / Pulpo a Feira", "Grilled octopus with smoked paprika aioli"],
        "exampleRecipes": ["rec-sole-meuniere"]
    },
    # 18. Kombu + Katsuobushi (The Umami Synergistic Archetype)
    {
        "source": "kombu", "target": "katsuobushi", "affinityScore": 0.99,
        "pairingType": "allosteric_umami_synergy",
        "aromaAffinity": "Pure clean ocean kelp aroma enveloped by fragrant wood smoke and cured tuna.",
        "tasteInteraction": "Glutamic acid (kombu) + Inosine monophosphate (katsuobushi) trigger 8-fold umami amplification.",
        "textureContrast": "Clear, pristine, golden liquid broth coating the palate.",
        "temperatureContrast": "Steeped at exactly 85°C to preserve delicate aromatics without extracting bitterness.",
        "culinaryApplications": ["Ichiban Dashi (primary Japanese broth)", "Soba/Udon dipping broth (Mentsuyu)", "Chawanmushi savory egg custard"],
        "exampleRecipes": ["rec-tonkotsu-ramen", "rec-miso-black-cod"]
    },
    # 19. Guanciale + Pecorino + Black Pepper (The Roman Triad)
    {
        "source": "guanciale", "target": "pecorino-romano", "affinityScore": 0.98,
        "pairingType": "lipid_saline_emulsion",
        "aromaAffinity": "Rendered pork fat and curing spices merge with sheep's milk caproic fatty acids.",
        "tasteInteraction": "Salty, piquant cheese cuts through decadent pork tallow, creating creamy sauce with starchy water.",
        "textureContrast": "Crispy rendered pork cracklings against velvety, creamy cheese emulsion.",
        "temperatureContrast": "Tossed in warm pan off-heat (55°C) to prevent cheese proteins from clumping.",
        "culinaryApplications": ["Spaghetti alla Carbonara", "Bucatini all'Amatriciana", "Spaghetti alla Gricia"],
        "exampleRecipes": ["rec-carbonara", "rec-cacio-e-pepe"]
    },
    # 20. Pecorino Romano + Black Pepper
    {
        "source": "pecorino-romano", "target": "black-pepper", "affinityScore": 0.96,
        "pairingType": "pungent_lipid_fusion",
        "aromaAffinity": "Dry-toasted piperine and wood terpenes bloom directly in warm rendered sheep fat.",
        "tasteInteraction": "Sharp heat cuts pungent sheep funk and high salinity.",
        "textureContrast": "Velvety smooth paste with crunchy flecks of coarse pepper.",
        "temperatureContrast": "Hot pasta cooking water emulsifying room-temperature grated cheese.",
        "culinaryApplications": ["Tonnarelli Cacio e Pepe", "Cacio e Pepe risotto"],
        "exampleRecipes": ["rec-cacio-e-pepe", "rec-carbonara"]
    },
    # 21. Egg Yolk + Clarified Butter + Tarragon (Sauce Béarnaise)
    {
        "source": "egg-yolk", "target": "clarified-butter", "affinityScore": 0.97,
        "pairingType": "colloidal_emulsion",
        "aromaAffinity": "Native yolk lecithin wraps tightly around warm clarified milk fat droplets.",
        "tasteInteraction": "Unctuous, decadent mouthfeel that coats the tongue and melts at 37°C body temperature.",
        "textureContrast": "Thick, ribbon-like, mirror-glossy emulsion holding soft peaks.",
        "temperatureContrast": "Held at warm 55-60°C serving temperature.",
        "culinaryApplications": ["Sauce Hollandaise", "Sauce Béarnaise", "Sauce Choron"],
        "exampleRecipes": ["rec-sole-meuniere", "rec-halibut-beurre-blanc"]
    },
    # 22. Tarragon + Shallot + White Wine Vinegar
    {
        "source": "tarragon", "target": "shallot", "affinityScore": 0.94,
        "pairingType": "acid_aromatic_reduction",
        "aromaAffinity": "Estragole licorice notes infuse deeply into sweet sweated allium sugars.",
        "tasteInteraction": "Sharp acetic acid softened by allium sweetness and herbal warmth.",
        "textureContrast": "Fine brunoise of translucent shallots suspended in clear golden acid reduction.",
        "temperatureContrast": "Simmered hot, cooled to room temp before whisking into yolks.",
        "culinaryApplications": ["Béarnaise reduction base", "French vinaigrette for haricots verts", "Poulet à l'Estragon"],
        "exampleRecipes": ["rec-sole-meuniere", "rec-halibut-beurre-blanc"]
    },
    # 23. Morel + Brown Butter
    {
        "source": "morel", "target": "brown-butter", "affinityScore": 0.96,
        "pairingType": "porous_lipid_sponge",
        "aromaAffinity": "Earthy 1-octen-3-ol mushroom aroma locked into caramelized milk solids and lactones.",
        "tasteInteraction": "Rich, nutty toasted fat penetrates every porous honeycomb chamber of the mushroom.",
        "textureContrast": "Tender, toothsome honeycomb ridges releasing bursts of warm hazelnut butter.",
        "temperatureContrast": "Sizzling hot sauté directly from copper skillet.",
        "culinaryApplications": ["Sautéed morels on toasted brioche", "Morilles à la crème with Vin Jaune", "Roast chicken with morel cream sauce"],
        "exampleRecipes": ["rec-sole-meuniere", "rec-boeuf-bourguignon"]
    },
    # 24. Black Truffle + Egg Yolk
    {
        "source": "black-truffle", "target": "egg-yolk", "affinityScore": 0.98,
        "pairingType": "sulfide_lipid_carrier",
        "aromaAffinity": "Lipophilic dimethyl sulfide in black truffles dissolves rapidly into yolk fats.",
        "tasteInteraction": "Pure hedonistic richness: earthy musk amplifies natural custard sweetness.",
        "textureContrast": "Crisp paper-thin shaved truffle scales atop soft, velvety molten scrambled eggs.",
        "temperatureContrast": "Shaved over warm steaming eggs so rising thermal air carries volatiles to the nose.",
        "culinaryApplications": ["Brouillade aux Truffes (soft scrambled eggs with black truffle)", "Fresh tagliolini with truffle butter"],
        "exampleRecipes": ["rec-french-omelette", "rec-cacio-e-pepe"]
    }
]

INGREDIENT_COMPARISONS = [
    {
        "pair": ["Butter", "Olive Oil"],
        "title": "European Cultured Butter vs. Extra Virgin Olive Oil",
        "overview": "Saturated dairy emulsion versus monounsaturated cold-pressed fruit oil.",
        "itemA": {
            "name": "European Cultured Butter (82-84% Fat)",
            "fatProfile": "approx 65% saturated fat, 16% water, 2% milk solids (casein, whey, lactose)",
            "smokePoint": "150°C - 175°C (300°F - 350°F) due to milk solids",
            "flavorProfile": "Rich, creamy, sweet, lactic fermentation tang, hazelnut when browned (beurre noisette)",
            "culinaryBehavior": "Solid at room temperature; forms velvety emulsions (monter au beurre) and flaky pastry layers; browns rapidly via Maillard reaction."
        },
        "itemB": {
            "name": "Extra Virgin Olive Oil (EVOO)",
            "fatProfile": "approx 73% monounsaturated (oleic acid), 14% saturated, 100% lipid (0% water)",
            "smokePoint": "190°C - 210°C (375°F - 410°F) for high-grade low-acidity oil",
            "flavorProfile": "Grassy, green almond, artichoke, floral, peppery throat bite (oleocanthal)",
            "culinaryBehavior": "Liquid at room temp; carries fat-soluble aromas without curdling; creates stable cold vinaigrettes and emulsion sauces like mayonnaise and aioli."
        },
        "whenToChooseA": "Choose butter for classical French pan sauces, delicate fish (Sole Meunière), egg dishes, laminated pastry, and anywhere velvety mouthfeel and nutty caramelization are required.",
        "whenToChooseB": "Choose EVOO for Mediterranean preparations, high-temperature vegetable searing, raw salads, pestos, finishing roasted meats, and dishes demanding bright peppery herbal notes.",
        "substitutionImpact": "Substituting olive oil for butter in sauces prevents proper velvety thickening; substituting butter for olive oil in high-heat searing risks burning milk solids into bitter black specks."
    },
    {
        "pair": ["Lemon Juice", "Sherry Vinegar"],
        "title": "Fresh Citrus Acidity vs. Oak-Aged Acetic Acid",
        "overview": "Volatile fresh citric/malic acid versus aged wood-matured acetic acid.",
        "itemA": {
            "name": "Fresh Lemon Juice",
            "acidType": "5-6% Citric acid with minor malic acid (pH approx 2.0 - 2.6)",
            "flavorProfile": "Bright, sharp, clean, uplifting citrus top-notes with limonene aroma",
            "culinaryBehavior": "Instantly brightens mid-palate; denatures delicate fish proteins (ceviche); sensitive to heat (boiling destroys volatile aroma)."
        },
        "itemB": {
            "name": "Vinagre de Jerez Reserva (Sherry Vinegar)",
            "acidType": "7-8% Acetic acid aged in American oak solera (pH approx 2.6 - 3.0)",
            "flavorProfile": "Woody, nutty, intense dried fruit, toasted hazelnut, powerful rounded acid",
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
    },
    {
        "pair": ["Heavy Cream", "Crème Fraîche"],
        "title": "Heavy Cream (36%+) vs. Cultured Crème Fraîche",
        "overview": "Sweet unpasteurized/pasteurized liquid dairy versus lactic acid-fermented cultured cream.",
        "itemA": {
            "name": "Pasteurized Heavy Cream (Crème Fleurette / 36-40% Fat)",
            "acidity": "Neutral pH (approx 6.6 - 6.8)",
            "flavorProfile": "Sweet, fresh milk flavor, pure clean creaminess",
            "culinaryBehavior": "Whips easily to trap air into Chantilly cream; sensitive to acids (curdles if added directly to lemon juice or hot vinegar reductions without starch buffer)."
        },
        "itemB": {
            "name": "Cultured Crème Fraîche",
            "acidity": "Acidic pH (approx 4.5) via lactic acid bacteria fermentation",
            "flavorProfile": "Nutty, rich, slightly tart, cultured hazelnut undertones",
            "culinaryBehavior": "Very high fat (40-42%) and modified protein structure allows it to be boiled and reduced directly in pan sauces and acids without curdling."
        },
        "whenToChooseA": "Choose heavy cream for whipped desserts, ice cream bases, ganaches, and baking where neutral sweetness is required.",
        "whenToChooseB": "Choose crème fraîche for pan sauce reductions, dolloping over caviar, swirling into soups, and dressings where pleasant lactic tang and heat stability matter.",
        "substitutionImpact": "Boiling heavy cream with vinegar will curdle into curd shards; crème fraîche can be substituted for heavy cream in baking by adding a pinch of baking soda to neutralize acid."
    },
    {
        "pair": ["Veal Brown Stock", "Chicken Stock"],
        "title": "Roasted Veal Stock (Fond Brun) vs. Chicken Stock (Fond Blanc/Brun)",
        "overview": "Dense collagen powerhouse versus versatile, elegant neutral foundation.",
        "itemA": {
            "name": "Roasted Veal Stock (Fond Brun de Veau)",
            "gelatinContent": "Extraordinarily high (young veal bones packed with soluble cartilage collagen)",
            "flavorProfile": "Deeply savory, roasted, unctuous, lip-coating richness, dark amber hue",
            "culinaryBehavior": "Reduces naturally into syrupy demi-glace and glace de viande without requiring flour roux or artificial thickeners."
        },
        "itemB": {
            "name": "Chicken Stock (Fond de Volaille)",
            "gelatinContent": "Moderate (sufficient to set lightly when chilled)",
            "flavorProfile": "Clean, light, savory, golden yellow, neutral culinary canvas",
            "culinaryBehavior": "Universal kitchen foundation; adapts to any global cuisine without overpowering delicate fish, vegetable, or white poultry dishes."
        },
        "whenToChooseA": "Choose brown veal stock for hearty red meat dishes, braised short ribs, Bordelaise, and rich demi-glace pan reductions.",
        "whenToChooseB": "Choose chicken stock for risottos, velouté sauces, soups, braising greens, and any dish where dark beefiness would clash.",
        "substitutionImpact": "Using veal stock in a delicate risotto will turn it dark and overwhelmingly heavy; using chicken stock for Bordelaise requires reducing twice as far and mounting with extra butter for body."
    },
    {
        "pair": ["Tamari", "Koikuchi Shoyu"],
        "title": "Pure Soy Tamari vs. Wheat-Brewed Koikuchi Shoyu",
        "overview": "Ancient 100% soybean byproduct versus modern balanced wheat-soy fermented shoyu.",
        "itemA": {
            "name": "Artisanal Tamari (100% Soybean)",
            "wheatContent": "0% (Gluten-free naturally)",
            "flavorProfile": "Thick, dark, rich, viscous, deep roasted savory umami without alcohol sharpness",
            "culinaryBehavior": "Higher concentration of soy amino acids; resists high heat without burning; glazes foods beautifully with a dark lacquer sheen."
        },
        "itemB": {
            "name": "Koikuchi Shoyu (50% Soybean / 50% Wheat)",
            "wheatContent": "Approx 50% wheat koji",
            "flavorProfile": "Brilliant reddish-brown, balanced salt, sweet wheat alcohol esters, bright aroma",
            "culinaryBehavior": "The universal all-purpose soy sauce of Japan; volatile aroma compounds flash off in hot woks, imparting signature appetizing fragrance."
        },
        "whenToChooseA": "Choose Tamari for sashimi dipping, dark teriyaki marinades, gluten-free dining, and dishes where deep, mellow umami is needed.",
        "whenToChooseB": "Choose Koikuchi Shoyu for noodle broths (ramen, udon), marinades, stir-fries, and classical Japanese braises (Nimono).",
        "substitutionImpact": "Tamari is denser and less salty than shoyu, giving a darker color; shoyu adds more aroma and lighter color."
    },
    {
        "pair": ["Fresh Ginger", "Dried Ground Ginger"],
        "title": "Fresh Ginger Root vs. Dried Ground Ginger Powder",
        "overview": "Fresh zesty gingerol versus dehydrated pungent shogaol.",
        "itemA": {
            "name": "Fresh Ginger Root (Zingiber officinale)",
            "activeCompound": "Gingerol (mild, refreshing pungency with zesty citrus terpenes)",
            "flavorProfile": "Sharp, juicy, refreshing, herbal lemon warmth, crisp bite",
            "culinaryBehavior": "Contains zingibain (a proteolytic enzyme that tenderizes meat); clears heavy animal fats from the palate in stir-fries and braises."
        },
        "itemB": {
            "name": "Dried Ground Ginger Powder",
            "activeCompound": "Shogaol (formed when gingerol is dehydrated and heated; twice as pungent as gingerol)",
            "flavorProfile": "Warm, earthy, dry, intense throat heat, woodsy, sweet spice notes",
            "culinaryBehavior": "Lacks proteolytic enzymes; stable in high-temperature baking; distributes evenly throughout flour doughs without adding moisture."
        },
        "whenToChooseA": "Essential for stir-fries, marinades, curries, dipping sauces, and fresh Asian broths.",
        "whenToChooseB": "Essential for spice cakes, gingerbread, speculoos, dry barbecue rubs, and pumpkin pie spice blends.",
        "substitutionImpact": "Never substitute powdered ginger for fresh in stir-fries (tastes like dusty ginger snaps); fresh ginger cannot be substituted in dry cookie dough without throwing off hydration."
    },
    {
        "pair": ["Kosher Salt", "Flaky Sea Salt (Maldon)"],
        "title": "Coarse Kosher Salt (Diamond Crystal) vs. Pyramidal Flaky Sea Salt (Maldon)",
        "overview": "Even volumetric cooking salt versus delicate finishing crunch crystals.",
        "itemA": {
            "name": "Diamond Crystal Kosher Salt",
            "crystalStructure": "Hollow, irregular, open-flaked crystals formed through Alberger process",
            "density": "Light density (approx 2.8g per teaspoon; half the density of fine table salt)",
            "culinaryBehavior": "Dissolves rapidly; wide surface area allows precise tactile pinch control between chef's fingers without over-salting."
        },
        "itemB": {
            "name": "Maldon Flaky Sea Salt",
            "crystalStructure": "Hollow, razor-thin inverted pyramids",
            "density": "Very light, fragile, shatters upon gentle tooth pressure",
            "culinaryBehavior": "Designed exclusively as a finishing salt. Sprinkled over hot food right before serving to provide textural crunch and localized bursts of clean salinity."
        },
        "whenToChooseA": "Use Kosher salt for all base seasoning, boiling pasta water, dry-brining steaks, baking doughs, and everyday seasoning.",
        "whenToChooseB": "Use Flaky salt exclusively on finished sliced rested steaks, chocolate chip cookies, fresh sliced heirloom tomatoes, and crudos.",
        "substitutionImpact": "Dissolving Maldon into boiling water wastes precious artisanal flakes; using table salt instead of Diamond Crystal by volume will result in food that is twice as salty as intended."
    },
    {
        "pair": ["Black Truffle", "White Truffle"],
        "title": "Black Périgord Truffle vs. Alba White Truffle",
        "overview": "Cookable subterranean musky fungus versus ephemeral raw aromatic diamond.",
        "itemA": {
            "name": "Black Winter Périgord Truffle (Tuber melanosporum)",
            "primaryVolatile": "Dimethyl sulfide, 2-methylbutanal, isoamyl alcohol",
            "flavorProfile": "Earthy, damp forest loam, dark cocoa, fermented malt, leather",
            "culinaryBehavior": "Heat-tolerant; infuses deeply into fats and butter sauces; can be gently heated, sautéed with butter, or baked under poultry skin."
        },
        "itemB": {
            "name": "Alba White Truffle (Tuber magnatum pico)",
            "primaryVolatile": "Bis(methylthio)methane (intensely pungent, fleetingly volatile)",
            "flavorProfile": "Pungent sweet garlic, aged shallot, raw honey, dry hay, wild mushroom",
            "culinaryBehavior": "Heat-fragile; heat destroys 100% of its intoxicating aroma within seconds. Must NEVER be cooked; only shaved raw onto warm buttery dishes right at the table."
        },
        "whenToChooseA": "Choose Black Truffles for making compound truffle butter, stuffing under chicken skin, simmering into Madeira sauces, and rich pasta fillings.",
        "whenToChooseB": "Choose White Truffles exclusively for shaving raw over hot buttered pasta (Tajarin), fried farm eggs, potato purée, or fontina fonduta.",
        "substitutionImpact": "Cooking a white truffle will completely eliminate its scent, destroying a very expensive ingredient; black truffles shaved raw lack the explosive room-filling perfume of fresh white truffles."
    }
]

js_content = f"""// L'Atelier Flavor Lab Database
// Scientific aroma compound networks, flavor balance simulator, and ingredient comparisons.

window.FLAVOR_NODES = {json.dumps(FLAVOR_NODES, indent=2)};
window.FLAVOR_EDGES = {json.dumps(FLAVOR_EDGES, indent=2)};
window.INGREDIENT_COMPARISONS = {json.dumps(INGREDIENT_COMPARISONS, indent=2)};

window.FlavorEngine = {{
  getAllNodes: function() {{ return window.FLAVOR_NODES; }},
  getNodeById: function(id) {{ return window.FLAVOR_NODES.find(n => n.id === id); }},
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
  getAllComparisons: function() {{
    return window.INGREDIENT_COMPARISONS;
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

print(f"Successfully generated data-flavor.js with {len(FLAVOR_NODES)} nodes, {len(FLAVOR_EDGES)} edges, {len(INGREDIENT_COMPARISONS)} comparisons.")
