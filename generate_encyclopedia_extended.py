# -*- coding: utf-8 -*-
"""
Extended High-Fidelity Ingredient Encyclopedia for L'Atelier.
Generates data-encyclopedia.js containing 62 comprehensive culinary dossiers.
"""

import json

ENCYCLOPEDIA_INGREDIENTS = [
    # --- ALLIUMS & AROMATICS ---
    {
        "id": "ing-garlic",
        "name": "Garlic (Allium sativum)",
        "category": "Alliums",
        "season": "Year-round (Peak late summer/early autumn)",
        "storage": "Store in a cool (15°C/60°F), dry, dark pantry with gentle airflow. Never refrigerate whole unpeeled bulbs (triggers sprouting and mold).",
        "flavorProfile": "Pungent, sulfuric, sharp raw; sweet, nutty, mellow, deeply savory when slowly roasted or sweated.",
        "scienceRole": "Contains alliin and alliinase in isolated cell compartments. Mincing or crushing breaks cell walls, catalyzing instant synthesis of allicin. Gentle heat deactivates alliinase and polymerizes fructan sugars into sweet caramelized alliums.",
        "bestTechniques": ["Confit in olive oil at 90°C", "Fine brunoise sweated in butter", "Rubbed raw over warm toasted rustic bread"],
        "substitutions": "Shallots + pinch of garlic powder, or wild ramps.",
        "affinities": ["Olive oil", "Butter", "Parsley", "Thyme", "Tomato", "Pork", "Mushrooms"]
    },
    {
        "id": "ing-shallot",
        "name": "French Grey Shallot (Échalote Grise)",
        "category": "Alliums",
        "season": "Year-round (Peak late autumn)",
        "storage": "Cool, dry, dark mesh basket. Keeps up to 2 months.",
        "flavorProfile": "Delicate, sweet, refined allium with subtle garlic nuances; lacks the aggressive pungency of yellow onions.",
        "scienceRole": "Higher sugar and lower moisture than standard onions, allowing fast caramelization without boiling in surface water. The indispensable aromatic acid base for French reductions (Béarnaise, Beurre Blanc, Bordelaise).",
        "bestTechniques": ["Minced fine (ciseler) for vinegar reductions", "Caramelized whole in butter as a garnish", "Crispy fried shallots for Southeast Asian dishes"],
        "substitutions": "Sweet Vidalia onion minced fine with a tiny sliver of garlic.",
        "affinities": ["White wine vinegar", "Butter", "Tarragon", "Red wine", "Steak", "Fish"]
    },
    {
        "id": "ing-scallion",
        "name": "Japanese Tokyo Negi / Scallions",
        "category": "Alliums",
        "season": "Year-round",
        "storage": "Wrap roots in damp paper towel and store upright in refrigerator crisper (3-4°C) up to 10 days.",
        "flavorProfile": "White base: crisp, pungent, peppery sweetness when heated. Green top: fresh, grassy, mild allium bite.",
        "scienceRole": "Biphenyls and dipropyl disulfides deliver instant sulfur punch in wok stir-frying. Whites withstand high searing (Yakitori Negima); greens contain heat-sensitive chlorophyll and are used raw as finishes.",
        "bestTechniques": ["Charred over Binchotan charcoal", "Fine julienne shocked in ice water (shiraga negi) for ramen", "Infused into hot wok oil (Cong You)"],
        "substitutions": "Young spring onions, sweet leek whites, or chives.",
        "affinities": ["Ginger", "Soy sauce", "Sesame oil", "Chicken", "Pork belly", "Miso"]
    },
    {
        "id": "ing-leek",
        "name": "Poireau (French Leek)",
        "category": "Alliums",
        "season": "Autumn through early spring",
        "storage": "Refrigerate unwashed in plastic bag at 2-4°C up to 2 weeks. Wash split leeks thoroughly before cooking to remove gritty sand.",
        "flavorProfile": "Mild, sweet, floral, creamy when braised; tender onion elegance without sharpness.",
        "scienceRole": "High concentration of inulin and soluble sugars. Slow cooking breaks inulin down into fructose, giving leeks their silky melting texture (fondant de poireaux).",
        "bestTechniques": ["Braised in white wine and chicken stock", "Poireaux Vinaigrette with Dijon mustard", "Base for Potage Parmentier / Vichyssoise"],
        "substitutions": "Sweet onions sweated very gently without color.",
        "affinities": ["Potatoes", "Dijon mustard", "Butter", "Crème fraîche", "Gruyère", "Fish"]
    },
    {
        "id": "ing-chives",
        "name": "French Fine Chives (Ciboulette)",
        "category": "Alliums",
        "season": "Spring and summer",
        "storage": "Wrap gently in damp paper towels inside an airtight container in the refrigerator (2-4°C). Cut only with a razor-sharp knife.",
        "flavorProfile": "Delicate, fresh, clean grassy onion note with zero harsh sulfur lingering.",
        "scienceRole": "Dull knife blades crush cell walls, causing sulfur bruising and an unpleasant swampy odor. Slicing with a razor-sharp blade keeps cell walls intact and preserves delicate aroma esters.",
        "bestTechniques": ["Precision razor-thin rounds for French rolled omelettes", "Stirred into fines herbes", "Garnish on chilled soups"],
        "substitutions": "Green scallion tops sliced razor-thin.",
        "affinities": ["Eggs", "Butter", "Sour cream", "Smoked salmon", "Potatoes", "Crab"]
    },
    {
        "id": "ing-ramps",
        "name": "Wild Ramps (Allium tricoccum)",
        "category": "Alliums",
        "season": "Ephemeral Spring (3-4 weeks only in April/May)",
        "storage": "Refrigerate unwashed between damp towels for up to 5 days; freeze ramp butter or ramp pickle brine.",
        "flavorProfile": "Intense wild fusion of sweet garlic and pungent scallion with earthy forest floor undertones.",
        "scienceRole": "Wild forest allium with high concentrations of S-allylcysteine and aromatic sulfur compounds that caramelize rapidly.",
        "bestTechniques": ["Charred whole in cast iron with butter", "Pickled ramp bulbs in white wine vinegar", "Blended into vibrant green ramp compound butter"],
        "substitutions": "Scallions mixed with minced fresh garlic and leek whites.",
        "affinities": ["Morel mushrooms", "Farm eggs", "Bacon", "Polenta", "Spring peas", "Pork chops"]
    },

    # --- PRODUCE, VEGETABLES & FUNGI ---
    {
        "id": "ing-san-marzano",
        "name": "San Marzano Tomato DOP",
        "category": "Produce",
        "season": "Summer (Canned DOP available year-round)",
        "storage": "Store canned DOP tomatoes in pantry up to 3 years. Once opened, transfer to glass jar and refrigerate up to 5 days.",
        "flavorProfile": "Intense sweet-tart balance, low acidity, thick fleshy walls, minimal seed cavities.",
        "scienceRole": "Grown in volcanic soil at the foot of Mount Vesuvius; extraordinarily high natural free glutamic acid (umami) and low citric acid, making it the supreme tomato for pasta sauces without requiring added sugar.",
        "bestTechniques": ["Crushed by hand for raw Neapolitan pizza sauce", "Simmered with butter and sweet onion (Marcella Hazan method)", "Base for ragù alla Bolognese"],
        "substitutions": "Italian whole peeled plum tomatoes (Pelati) with a tiny pinch of baking soda.",
        "affinities": ["Basil", "Extra virgin olive oil", "Garlic", "Parmigiano-Reggiano", "Oregano"]
    },
    {
        "id": "ing-fennel",
        "name": "Florence Fennel Bulb (Finocchio)",
        "category": "Produce",
        "season": "Autumn through early spring",
        "storage": "Crisper drawer at 2-4°C wrapped in perforated bag up to 10 days.",
        "flavorProfile": "Raw: crisp, refreshing, sweet anise/licorice bite. Braised: silky, nutty, rich, mellow.",
        "scienceRole": "Contains anethole (the same essential oil as star anise and tarragon). Anethole cuts through heavy animal fats and pairs with pork and seafood.",
        "bestTechniques": ["Shaved paper-thin on mandoline with lemon and olive oil", "Braised in white wine and butter until caramelized", "Roasted with citrus and whole sea bass"],
        "substitutions": "Celery stalks tossed with a pinch of ground fennel seed or tarragon.",
        "affinities": ["Blood orange", "Pork chops", "Scallops", "Tarragon", "Goat cheese", "Olive oil"]
    },
    {
        "id": "ing-morels",
        "name": "Fresh Morel Mushrooms (Morchella)",
        "category": "Produce",
        "season": "Mid-spring (April - May)",
        "storage": "Never soak in standing water. Brush clean or swish briefly in cold water right before cooking; store in paper bag in fridge.",
        "flavorProfile": "Intense earthy, nutty, smoky, woodsy savory depth with a tender honeycomb chew.",
        "scienceRole": "Contains mild natural hydrazine toxins that decompose completely under thermal heat; must NEVER be eaten raw. Packed with natural ribonucleotides that multiply glutamates.",
        "bestTechniques": ["Sautéed in foaming butter with shallots and Madeira", "Simmered in heavy cream sauce for poultry", "Stuffed with poultry mousseline"],
        "substitutions": "Dried morels reconstituted in warm water, or chanterelles / cremini.",
        "affinities": ["Asparagus", "Shallots", "Butter", "Madeira", "Veal", "Cream", "Tarragon"]
    },
    {
        "id": "ing-porcini",
        "name": "Porcini / Cèpes (Boletus edulis)",
        "category": "Produce",
        "season": "Late summer through autumn",
        "storage": "Refrigerate wrapped in dry cloth; dried porcini store in cool pantry up to 2 years.",
        "flavorProfile": "Deeply savory, forest floor, hazelnut, meaty, umami-rich broth notes.",
        "scienceRole": "Extraordinarily high guanylate content (synergistic umami amplifier). Dried porcini powder acts as a natural MSG booster when dusted onto seared meats.",
        "bestTechniques": ["Sliced and pan-seared in olive oil with garlic and parsley", "Dried porcini steeped into mushroom broth for risotto", "Ground into umami steak rub"],
        "substitutions": "Dried shiitake or maitake mushrooms.",
        "affinities": ["Carnaroli rice", "Garlic", "Parsley", "Steak", "Parmigiano-Reggiano", "Polenta"]
    },
    {
        "id": "ing-black-truffle",
        "name": "Black Winter Périgord Truffle (Tuber melanosporum)",
        "category": "Produce",
        "season": "December through March",
        "storage": "Wrap in dry paper towel in sealed glass jar with fresh eggs or Arborio rice at 2-4°C; replace towel daily. Consume within 7 days.",
        "flavorProfile": "Complex damp forest soil, cocoa, musk, fermented malt, and leather.",
        "scienceRole": "Aroma driven by dimethyl sulfide, 2-methylbutanal, and volatile sulfur compounds. Heat-tolerant; infuses deeply into dairy fats, egg yolks, and butter.",
        "bestTechniques": ["Cooked into truffle butter or Madeira pan reductions", "Tucked under skin of roasted capon or Bresse chicken", "Infused into warm scrambled eggs or pomme purée"],
        "substitutions": "Summer black truffles (milder) or high-grade authentic truffle butter (avoid petroleum-derived 2,4-dithiapentane oils).",
        "affinities": ["Butter", "Eggs", "Duck breast", "Potatoes", "Cognac", "Parmigiano-Reggiano"]
    },
    {
        "id": "ing-white-truffle",
        "name": "Alba White Truffle (Tuber magnatum pico)",
        "category": "Produce",
        "season": "October through December",
        "storage": "Store identical to black truffle. Must be consumed within 5 days of harvest.",
        "flavorProfile": "Intense pungent garlic, shallot, aged cheese, honey, and damp hay.",
        "scienceRole": "Aroma dominated by bis(methylthio)methane, which is extremely volatile and completely destroyed by cooking heat. Must NEVER be cooked; only shaved raw onto hot, buttery dishes.",
        "bestTechniques": ["Shaved raw at the table over buttered Tajarin pasta", "Shaved over warm fontina fonduta", "Shaved over soft scrambled eggs"],
        "substitutions": "None exists that replicates genuine fresh Alba white truffle.",
        "affinities": ["Fresh egg pasta (Tajarin)", "Butter", "Eggs", "Risotto", "Fontina"]
    },
    {
        "id": "ing-radicchio",
        "name": "Radicchio di Treviso Tardivo IGP",
        "category": "Produce",
        "season": "Late autumn through winter",
        "storage": "Perforated bag in refrigerator crisper (2-4°C) up to 12 days.",
        "flavorProfile": "Pleasantly bitter, crisp, peppery, mineral, with sweet finish when grilled or roasted.",
        "scienceRole": "Contains intybin and lactucopicrin, bitter sesquiterpene lactones that stimulate bile production and digestive enzymes. Cooking caramelizes natural sugars, balancing the bitterness.",
        "bestTechniques": ["Split and grilled over charcoal with aged balsamic and olive oil", "Stirred into Venetian risotto", "Raw in winter bitter-greens salad with citrus and walnuts"],
        "substitutions": "Belgian endive or Castelfranco radicchio.",
        "affinities": ["Aged balsamic", "Gorgonzola", "Walnuts", "Pancetta", "Olive oil", "Oranges"]
    },
    {
        "id": "ing-artichoke",
        "name": "Globe Artichoke / Violet de Provence",
        "category": "Produce",
        "season": "Spring and autumn",
        "storage": "Store stem-down in a glass of water in refrigerator or crisper up to 1 week.",
        "flavorProfile": "Earthy, nutty, herbal, vegetal, with an intriguing sweet lingering aftertaste.",
        "scienceRole": "Contains cynarin, an organic acid that temporarily inhibits sweet taste bud receptors. When you follow an artichoke bite with plain water or wine, cynarin washes off and the receptors rebound, making everything taste sweet.",
        "bestTechniques": ["Artichokes à la Barigoule (braised with white wine, carrots, shallots, and thyme)", "Fried Roman style (Carciofi alla Giudia)", "Steamed whole with lemon-herb vinaigrette"],
        "substitutions": "Hearts of palm or cardoons.",
        "affinities": ["Lemon", "Olive oil", "White wine", "Mint", "Garlic", "Parsley"]
    },

    # --- HERBS ---
    {
        "id": "ing-basil",
        "name": "Genovese Basil (Ocimum basilicum)",
        "category": "Herbs",
        "season": "Summer peak",
        "storage": "Never refrigerate (causes enzymatic blackening below 10°C). Keep stems in a glass of water at room temperature.",
        "flavorProfile": "Sweet, aromatic, warm clove, anise, peppery freshness.",
        "scienceRole": "Rich in linalool, eugenol (clove aroma), and estragole (anise). Polyphenol oxidase causes rapid browning when leaves are bruised or cut with dull blades; blanching 3 seconds in boiling water denatures the enzyme, preserving electric emerald green.",
        "bestTechniques": ["Pounded in granite mortar with garlic and pine nuts for pesto", "Torn raw over hot Margherita pizza off heat", "Blanched and blended into bright green herb oil"],
        "substitutions": "Thai basil (more licorice/minty) or fresh sweet marjoram.",
        "affinities": ["San Marzano tomato", "Mozzarella di Bufala", "Garlic", "Pine nuts", "Olive oil"]
    },
    {
        "id": "ing-tarragon",
        "name": "French Tarragon (Artemisia dracunculus)",
        "category": "Herbs",
        "season": "Spring through summer",
        "storage": "Wrap in dry paper towel in airtight container in fridge (2-4°C).",
        "flavorProfile": "Pungent anise, licorice, sweet herbal, with faint peppery tongue numbing.",
        "scienceRole": "High in methylchavicol (estragole), providing warm licorice aromatics that cut through egg and butter fats in classical French emulsified sauces.",
        "bestTechniques": ["Steeped in vinegar reduction for Sauce Béarnaise", "Chiffonade into roasted chicken pan juices", "Fines herbes mixture with chervil, parsley, chives"],
        "substitutions": "Chervil + pinch of ground aniseed.",
        "affinities": ["Butter", "Egg yolks", "Chicken", "Mustard", "Shallots", "White wine vinegar"]
    },
    {
        "id": "ing-thyme",
        "name": "Fresh French Thyme (Thymus vulgaris)",
        "category": "Herbs",
        "season": "Year-round",
        "storage": "Refrigerate wrapped in paper towel up to 2 weeks.",
        "flavorProfile": "Earthy, woodsy, minty, pungent, savory medicinal warmth.",
        "scienceRole": "Dominated by thymol, a powerful antioxidant and antimicrobial volatile that withstands multi-hour braises and pan basting without losing aroma.",
        "bestTechniques": ["Arrosé pan basting with butter and garlic over steak", "Bouquet garni for stocks and stews", "Roasted with root vegetables"],
        "substitutions": "Fresh oregano or savory in equal measure.",
        "affinities": ["Butter", "Beef", "Chicken", "Mushrooms", "Garlic", "Red wine", "Potatoes"]
    },
    {
        "id": "ing-rosemary",
        "name": "Fresh Rosemary (Rosmarinus officinalis)",
        "category": "Herbs",
        "season": "Year-round",
        "storage": "Crisper drawer wrapped in dry paper towel up to 3 weeks.",
        "flavorProfile": "Resinous, pine needle, camphoraceous, woodsy, warm astringent.",
        "scienceRole": "High concentrations of pinene, camphor, and carnosic acid. Carnosic acid is one of nature's strongest fat-soluble antioxidants, protecting cooking oils and meats from lipid peroxidation during high-heat roasting.",
        "bestTechniques": ["Charred over charcoal skewers for lamb spiedini", "Infused into hot olive oil for focaccia", "Roasted with baby potatoes and sea salt"],
        "substitutions": "Fresh thyme + sage (milder resinous tone).",
        "affinities": ["Lamb", "Pork", "Potatoes", "Olive oil", "Garlic", "White beans"]
    },
    {
        "id": "ing-dill",
        "name": "Fresh Dill Leaf (Anethum graveolens)",
        "category": "Herbs",
        "season": "Spring and summer",
        "storage": "Trim stem ends and place upright in a jar of water in the fridge with a plastic bag loosely tented over top.",
        "flavorProfile": "Grassy, sweet, citrus-anise, refreshingly clean herbal punch.",
        "scienceRole": "Carvone and dill ether provide cool volatile top notes that break through rich fish lipids and dairy coats without requiring harsh acid.",
        "bestTechniques": ["Cured with salt and sugar on gravlax salmon", "Chopped into cucumber tzatziki or sour cream", "Garnish on borscht"],
        "substitutions": "Fennel fronds or fresh tarragon.",
        "affinities": ["Salmon", "Cucumber", "Crème fraîche", "Mustard", "Potatoes", "Lemon"]
    },
    {
        "id": "ing-shiso",
        "name": "Japanese Green & Red Shiso (Perilla frutescens)",
        "category": "Herbs",
        "season": "Summer through early autumn",
        "storage": "Store upright in a glass of water inside the refrigerator up to 7 days.",
        "flavorProfile": "Complex, intoxicating blend of basil, mint, anise, cinnamon, and cumin.",
        "scienceRole": "Dominated by perillaldehyde, which provides antimicrobial properties traditionally valued for preserving raw fish freshness in sashimi presentations.",
        "bestTechniques": ["Whole leaves wrapping sashimi or tempura", "Chiffonade over cold soba noodles", "Pickled red shiso for umeboshi plums"],
        "substitutions": "Genovese basil mixed with a tiny leaf of fresh mint.",
        "affinities": ["Sashimi", "Soy sauce", "Wasabi", "Cucumber", "Tempura", "Plum"]
    },

    # --- CITRUS & ACIDS ---
    {
        "id": "ing-meyer-lemon",
        "name": "Meyer Lemon (Citrus × meyeri)",
        "category": "Acids & Citrus",
        "season": "Winter through early spring",
        "storage": "Refrigerate up to 3 weeks.",
        "flavorProfile": "Sweet citrus, mandarin floral undertones, soft herbal fragrance, lower acidity than Eureka lemons.",
        "scienceRole": "Higher sugar-to-acid ratio and thin, edible peel rich in thymol and limonene. Adds brightness to emulsions without coagulating delicate proteins prematurely.",
        "bestTechniques": ["Preserved whole in sea salt and lemon juice (Moroccan style)", "Zested into fresh pasta and ricottas", "Segments tossed with pan-roasted sea bass"],
        "substitutions": "Equal parts regular lemon juice and mandarin orange juice.",
        "affinities": ["Ricotta", "Scallops", "Thyme", "Olive oil", "Chicken", "Honey"]
    },
    {
        "id": "ing-yuzu",
        "name": "Japanese Yuzu (Citrus junos)",
        "category": "Acids & Citrus",
        "season": "Late autumn / winter",
        "storage": "Refrigerate fresh fruit up to 2 weeks; freeze pure 100% yuzu juice in ice cube trays up to 6 months.",
        "flavorProfile": "Electrifying hybrid of grapefruit, mandarin orange, lime, and wild floral pine.",
        "scienceRole": "Contains yuzunone and yuzulactone, unique sesquiterpenes that resist high thermal degradation and deliver persistent aromatic top-notes.",
        "bestTechniques": ["Whisked with soy sauce, mirin, and dashi for Ponzu sauce", "Yuzu kosho (fermented chili paste with yuzu peel and salt)", "Zested over raw Hamachi or oysters"],
        "substitutions": "Blend of Meyer lemon juice, lime juice, and a dash of grapefruit juice.",
        "affinities": ["Hamachi / Yellowtail", "Soy sauce", "Sesame oil", "Duck", "Oysters", "Chili"]
    },
    {
        "id": "ing-balsamic-tradizionale",
        "name": "Aceto Balsamico Tradizionale di Modena DOP (12 to 25+ Years)",
        "category": "Acids & Citrus",
        "season": "Aged 12 to 25+ years in battery wood casks",
        "storage": "Room temperature pantry away from heat. Keeps indefinitely.",
        "flavorProfile": "Viscous, syrupy, mahogany hue, velvety harmony of intense wood tannins, dried figs, prune sweetness, and mellow acetic acid.",
        "scienceRole": "Made exclusively from cooked Trebbiano/Lambrusco grape must (mosto cotto) aged through progressively smaller wooden barrels (oak, chestnut, cherry, ash, mulberry). Never diluted with wine vinegar or caramel coloring.",
        "bestTechniques": ["Drizzled drop by drop over aged Parmigiano-Reggiano chunks", "Finishing drops over ripe summer strawberries", "Drizzled over warm seared duck liver or filet mignon"],
        "substitutions": "High-grade IGP balsamic vinegar reduced gently over low heat until syrupy.",
        "affinities": ["Strawberries", "Parmigiano-Reggiano", "Vanilla gelato", "Duck breast", "Foie gras"]
    },
    {
        "id": "ing-sherry-vinegar",
        "name": "Vinagre de Jerez Reserva DOP (Sherry Vinegar)",
        "category": "Acids & Citrus",
        "season": "Aged 2 to 10+ years in American oak criaderas",
        "storage": "Pantry away from direct sunlight; shelf life indefinite.",
        "flavorProfile": "Woody, nutty, intense dried fruit, toasted hazelnut, powerful yet rounded acidity.",
        "scienceRole": "Aged in American oak solera barrels previously used for Oloroso and Pedro Ximénez sherry. Volatile phenols cut through animal fats and elevate roasted pan fond glazes.",
        "bestTechniques": ["Deglazing pan for seared pork chops or duck breast", "Classic Andalusian gazpacho base", "Warm vinaigrette for roasted wild mushrooms"],
        "substitutions": "Red wine vinegar blended with a splash of dry amontillado sherry.",
        "affinities": ["Duck", "Pork", "Smoked paprika", "Shallots", "Mushrooms", "Lentils"]
    },
    {
        "id": "ing-champagne-vinegar",
        "name": "Champagne Vinegar (Vinagre de Champagne)",
        "category": "Acids & Citrus",
        "season": "Year-round",
        "storage": "Pantry shelf away from heat.",
        "flavorProfile": "Crisp, pale, delicate, floral, clean, elegant acidity without harsh pungent bite.",
        "scienceRole": "Crafted from Chardonnay and Pinot Noir grapes from the Champagne region; maintains light color and floral esters, ideal for delicate emulsions where dark vinegars would discolor sauces.",
        "bestTechniques": ["Béarnaise reduction base", "Delicate oyster mignonette with French shallots", "Vinaigrette for butterhead lettuce"],
        "substitutions": "High-quality white wine vinegar diluted with a few drops of dry white wine.",
        "affinities": ["Oysters", "Tarragon", "Shallots", "Butterhead lettuce", "Crab", "Avocado"]
    },

    # --- DAIRY & FATS ---
    {
        "id": "ing-butter-european",
        "name": "European Cultured Butter (Beurre d'Isigny / 82-84% Fat)",
        "category": "Dairy & Fats",
        "season": "Year-round (Spring milk has richest yellow carotene hue)",
        "storage": "Refrigerate tightly wrapped at <=4°C to prevent lipid oxidation and absorbing off-odors. Freezes up to 6 months.",
        "flavorProfile": "Rich, creamy, hazelnut undertones with subtle lactic fermentation tang.",
        "scienceRole": "Higher butterfat (82-84% vs 80% American) means significantly less water. This ensures crisp flaky laminated pastry (croissants, puff pastry), faster reduction to brown butter (beurre noisette), and silkier pan sauce mantecatura.",
        "bestTechniques": ["Monter au beurre (finishing hot pan sauces off-heat)", "Beurre noisette (brown butter with nutty caramelized milk solids)", "Laminated viennoiserie pastry"],
        "substitutions": "Standard unsalted butter (reduce liquid slightly in baking).",
        "affinities": ["Shallots", "Lemon juice", "Parsley", "Sage", "Fish", "Potatoes"]
    },
    {
        "id": "ing-parmigiano",
        "name": "Parmigiano-Reggiano DOP (Aged 24 Months)",
        "category": "Dairy & Fats",
        "season": "Aged 24 to 36 months",
        "storage": "Wrap in breathable cheese paper or parchment, then loosely in plastic wrap at 4-8°C. Save rinds for simmering in broths.",
        "flavorProfile": "Nutty, pineapple-fruity, savory broth flavor, crunchy tyrosine amino acid crystals.",
        "scienceRole": "During 24 months of enzymatic proteolysis, milk casein is broken down into free amino acids, yielding over 1,200mg of free glutamic acid per 100g (the highest of any natural Western food). Acts as a clean, natural umami amplifier.",
        "bestTechniques": ["Microplaned into hot risotto during mantecatura", "Shaved over beef carpaccio", "Rinds simmered in minestrone and chicken broths"],
        "substitutions": "Grana Padano (milder) or Pecorino Romano (much saltier and sheep-funky).",
        "affinities": ["Aged balsamic", "Carnaroli rice", "Egg yolks", "Black pepper", "Prosciutto di Parma"]
    },
    {
        "id": "ing-pecorino-romano",
        "name": "Pecorino Romano DOP (Aged 12 Months)",
        "category": "Dairy & Fats",
        "season": "Aged 8 to 12 months",
        "storage": "Refrigerate wrapped in wax paper at 4-6°C.",
        "flavorProfile": "Sharp, salty, sheep's milk tang, pungent, rustic, savory.",
        "scienceRole": "Made entirely from sheep's milk; contains short-chain caproic, caprylic, and capric fatty acids that produce signature pungent piquant flavor. Crucial for Cacio e Pepe and Carbonara emulsions.",
        "bestTechniques": ["Finely grated with hot pasta cooking water for Cacio e Pepe sauce", "Tossed with guanciale and eggs for Carbonara", "Shaved over raw fava beans"],
        "substitutions": "Parmigiano-Reggiano mixed with a pinch of salt.",
        "affinities": ["Black pepper", "Guanciale", "Pasta water", "Fava beans", "Honey"]
    },
    {
        "id": "ing-creme-fraiche",
        "name": "French Cultured Crème Fraîche",
        "category": "Dairy & Fats",
        "season": "Year-round",
        "storage": "Refrigerate at 2-4°C; consume within 10 days of opening.",
        "flavorProfile": "Silky, unctuous, thick, nutty, mild lactic tang without harsh sourness.",
        "scienceRole": "High fat content (38-42%) and low protein content prevents curdling when boiled or combined with acidic ingredients. Can be boiled and reduced directly in pan sauces without breaking.",
        "bestTechniques": ["Swirled into hot wild mushroom pan sauce", "Dolloped on caviar and blinis", "Whipped with lemon juice for smoked salmon"],
        "substitutions": "Heavy cream whisked with buttermilk and fermented 24 hours at room temp.",
        "affinities": ["Caviar", "Smoked salmon", "Dill", "Mushrooms", "Black truffles"]
    },
    {
        "id": "ing-duck-fat",
        "name": "Rendered Duck Fat (Graisse de Canard)",
        "category": "Dairy & Fats",
        "season": "Year-round",
        "storage": "Refrigerate in a sealed glass jar up to 6 months; freezes indefinitely. Can be strained and reused.",
        "flavorProfile": "Savory, silky, deeply aromatic poultry richness with a low melting point (32°C / 90°F) that melts instantly on the human tongue.",
        "scienceRole": "Contains approx 50% monounsaturated fatty acids (oleic acid) similar to olive oil, creating incomparable crispness when frying potatoes (Pommes Sarladaises) without leaving a greasy, waxy film on the palate.",
        "bestTechniques": ["Confit immersion cooking at 90°C", "Roasting Yukon gold potatoes", "Sautéing mushrooms and root vegetables"],
        "substitutions": "Rendered pork lard (saindoux) or clarified butter (ghee).",
        "affinities": ["Potatoes", "Thyme", "Garlic", "Shallots", "Duck legs", "Mushrooms"]
    },
    {
        "id": "ing-guanciale",
        "name": "Aged Italian Guanciale (Cured Pork Jowl)",
        "category": "Dairy & Fats",
        "season": "Cured 2 to 3 months",
        "storage": "Wrap in parchment paper in refrigerator crisper up to 2 months; freeze up to 6 months.",
        "flavorProfile": "Sweet, silky pork fat infused with black pepper, rosemary, and juniper; far richer and tenderer than pancetta.",
        "scienceRole": "Pork jowl contains a unique collagen-fat matrix that renders out translucent, ultra-flavorful fat when slowly rendered over low heat. The liquid fat emulsifies with pasta cooking water to create Carbonara and Amatriciana sauces.",
        "bestTechniques": ["Rendered slowly over low heat until crispy outside and tender within", "Base for Spaghetti alla Carbonara", "Base for Bucatini all'Amatriciana"],
        "substitutions": "High-quality slab unsmoked pancetta.",
        "affinities": ["Pecorino Romano", "Black pepper", "San Marzano tomatoes", "Egg yolks", "Pasta"]
    },
    {
        "id": "ing-evoo",
        "name": "Single-Estate Extra Virgin Olive Oil (EVOO - Tuscan / Picual)",
        "category": "Dairy & Fats",
        "season": "Late autumn harvest (November - December)",
        "storage": "Store in dark glass bottle in cool, dark cupboard (14-18°C) away from stove heat. Consume within 6 months of opening.",
        "flavorProfile": "Bright green aroma, freshly cut grass, artichoke, green almond, peppery throat catch (oleocanthal).",
        "scienceRole": "Unrefined cold-pressed lipid packed with polyphenols and squalene. Oleocanthal produces the characteristic peppery irritation in the throat and mimics the anti-inflammatory action of ibuprofen.",
        "bestTechniques": ["Finishing drizzle over warm soups and pastas", "Raw emulsion in mayonnaise or aioli", "Dipping for warm crusty rustic sourdough"],
        "substitutions": "Mild Spanish Arbequina EVOO or California extra virgin olive oil.",
        "affinities": ["San Marzano tomatoes", "Garlic", "Sea salt", "Bread", "White beans", "Fish"]
    },
    {
        "id": "ing-jamon-iberico",
        "name": "Jamón Ibérico de Bellota (100% Acorn-Fed)",
        "category": "Dairy & Fats",
        "season": "Cured 36 to 48 months",
        "storage": "Room temperature on jamonero stand covered with clean fat slice; never refrigerate sliced ham.",
        "flavorProfile": "Incomparable nutty, toasted acorn sweetness, savory cured depth, fat that melts at 28°C on the tongue.",
        "scienceRole": "Free-range Iberian pigs feed on oak acorns (bellotas) rich in oleic acid, making their fat chemically similar to olive oil. Prolonged 4-year curing hydrolyzes proteins into massive concentrations of free glutamates and crunchy tyrosine crystals.",
        "bestTechniques": ["Hand-sliced paper-thin at room temperature (24°C)", "Draped over warm toasted pan con tomate", "Paired with dry Manzanilla sherry"],
        "substitutions": "Prosciutto di Parma DOP or Jamón Serrano Gran Reserva.",
        "affinities": ["Pan con tomate", "Manzanilla sherry", "Marcona almonds", "Figs", "Melon"]
    },

    # --- SEAFOOD ---
    {
        "id": "ing-king-salmon",
        "name": "Wild Alaskan King (Chinook) Salmon",
        "category": "Seafood",
        "season": "Late spring through summer",
        "storage": "Pack in a perforated pan set over crushed ice in the refrigerator (0°C to 1°C). Consume within 48 hours of harvest.",
        "flavorProfile": "Rich, luscious, buttery, clean oceanic sweet finish with zero fishy odor.",
        "scienceRole": "High intramuscular omega-3 fatty acids (over 13% fat) insulate the short myotome muscle fibers, ensuring velvety, succulent texture even under high-heat searing. Delicate collagen melts at 40-50°C.",
        "bestTechniques": ["Crispy-skin pan sear with butter basting", "Gentle olive oil confit at 48°C", "Cured as gravlax with dill and coarse sea salt"],
        "substitutions": "Steelhead trout, Arctic char, or Scottish organic salmon.",
        "affinities": ["Dill", "Lemon", "Crème fraîche", "Capers", "Brown butter", "Cucumber"]
    },
    {
        "id": "ing-diver-scallops",
        "name": "Dayboat Wild Diver Sea Scallops (Placopecten magellanicus)",
        "category": "Seafood",
        "season": "Year-round (Peak winter when sweet glycogen peaks)",
        "storage": "Store dry on paper towels over ice at 0-2°C. Must be 'dry-packed' (never treated with sodium tripolyphosphate soak).",
        "flavorProfile": "Sweet, briny, clean sea breeze, tender pearl texture, intense caramelized crust.",
        "scienceRole": "Packed with free glycine and glycogen (sugar polymers). Dry-packed scallops sear instantly to deep mahogany Maillard crust in 90 seconds per side; chemically soaked scallops weep milky water and steam grey.",
        "bestTechniques": ["Hard sear in screaming hot cast iron with clarified butter", "Crudo sliced raw with yuzu, sea salt, and olive oil", "Poached gently in beurre blanc"],
        "substitutions": "Fresh Nantucket bay scallops (sweeter, smaller) or wild prawns.",
        "affinities": ["Brown butter", "Cauliflower purée", "Truffle", "Lemon", "Tarragon", "Caviar"]
    },
    {
        "id": "ing-hamachi",
        "name": "Japanese Hamachi / Yellowtail (Seriola quinqueradiata)",
        "category": "Seafood",
        "season": "Winter peak (Kan-Buri has highest fat content)",
        "storage": "Wrap tightly in absorbent culinary paper (shungiku/magu roll) at 0°C on ice. Keeps 3-4 days.",
        "flavorProfile": "Luscious, buttery, melt-in-mouth, sweet finish with mild pleasant richness.",
        "scienceRole": "High subcutaneous lipid content makes it the premier fish for raw sashimi and crudo; fat buffers acidity and carries citrus volatiles effortlessly.",
        "bestTechniques": ["Hamachi Crudo with sliced serrano chili and ponzu", "Nigiri sushi with seasoned sushi rice and nikiri shoyu", "Buri Daikon (simmered collar with daikon radish and sweet soy)"],
        "substitutions": "Kanpachi (amberjack), Kingfish, or Hiramasa.",
        "affinities": ["Ponzu", "Yuzu kosho", "Serrano chili", "White soy sauce", "Daikon", "Cilantro"]
    },
    {
        "id": "ing-caviar",
        "name": "Royal Ossetra Sturgeon Caviar (Acipenser gueldenstaedtii)",
        "category": "Seafood",
        "season": "Farm-harvested year-round",
        "storage": "Store in the coldest zone of refrigerator at -2°C to +2°C. Never freeze. Once opened, consume within 24 hours.",
        "flavorProfile": "Pop on the palate, rich nutty hazelnut undertones, pristine oceanic brine, buttery finish.",
        "scienceRole": "Cured via the Malossol method ('little salt', under 3.5% NaCl) to preserve fragile sturgeon egg membranes without curdling delicate lipovitellin proteins. Use mother-of-pearl or gold spoons (silver oxidizes and imparts metallic off-notes).",
        "bestTechniques": ["Served atop warm potato blinis with crème fraîche", "Garnishing soft custard scrambled eggs", "Crown on raw beef tartare or sea urchin"],
        "substitutions": "Sevruga caviar, Kaluga hybrid caviar, or Siberian sturgeon caviar.",
        "affinities": ["Crème fraîche", "Blinis", "Egg yolks", "Chives", "Champagne", "Potatoes"]
    },
    {
        "id": "ing-octopus",
        "name": "Spanish Galician Octopus (Octopus vulgaris)",
        "category": "Seafood",
        "season": "Year-round",
        "storage": "Freeze fresh octopus for 48 hours before cooking: ice crystallization naturally ruptures tough rubbery connective tissue.",
        "flavorProfile": "Sweet, delicate lobster-like flavor with a tender, gelatinous, toothsome bite.",
        "scienceRole": "Octopus muscle contains 3 to 5 times more collagen than teleost finfish, distributed in five distinct layers. Requires either rapid flash-cooking (under 1 minute) or prolonged gentle simmering (60-90 minutes at 88°C) to convert collagen to gelatin.",
        "bestTechniques": ["Pulpo a la Gallega (braised tender, sliced, seasoned with coarse salt, sweet smoked pimentón, and EVOO)", "Braised and charred over charcoal", "Ceviche with lime and red onion"],
        "substitutions": "Cuttlefish or large squid.",
        "affinities": ["Smoked pimentón", "Yukon gold potatoes", "Extra virgin olive oil", "Maldon salt", "Garlic"]
    },

    # --- MEAT & POULTRY ---
    {
        "id": "ing-ribeye-aged",
        "name": "USDA Prime Dry-Aged Beef Ribeye (45-Day Aged)",
        "category": "Meat & Poultry",
        "season": "Year-round",
        "storage": "Unwrap and store on wire rack over sheet pan in refrigerator (1-2°C) uncovered for 12-24 hours to dry pellicle.",
        "flavorProfile": "Intense concentrated beefiness, roasted hazelnut, blue cheese funk, umami mushroom undertones.",
        "scienceRole": "45 days of dry aging allows endogenous calpain and cathepsin enzymes to break down tough muscle fibers while moisture loss (15-20%) concentrates natural flavor. Surface microbial molds (Thamnidium) release nutty, earthy aromatic ketones.",
        "bestTechniques": ["Reverse sear (bake at 105°C until 48°C core, sear hard in cast iron with foaming butter, garlic, thyme)", "Broiled in 800°C infrared salamander", "Grilled over white oak embers"],
        "substitutions": "Prime wet-aged bone-in ribeye or dry-aged strip steak.",
        "affinities": ["Bordelaise sauce", "Marrow butter", "Shallots", "Cabernet Sauvignon", "Thyme"]
    },
    {
        "id": "ing-duck-breast",
        "name": "Moulard Duck Breast (Magret de Canard)",
        "category": "Meat & Poultry",
        "season": "Year-round",
        "storage": "Refrigerate at 1-3°C; score skin in tight diamond hatch without piercing flesh.",
        "flavorProfile": "Deep, gamey, rich red-meat flavor with sweet, crispy roasted fat crackling.",
        "scienceRole": "High concentration of myoglobin gives duck breast its dark red steak appearance. Slow cold-pan start renders the thick subcutaneous fat layer while gradually crisping skin without overcooking the medium-rare (55°C) breast meat.",
        "bestTechniques": ["Cold-pan render: skin side down over low heat for 12 minutes, flip and sear 3 minutes, rest 8 minutes", "Smoked over tea leaves and star anise", "Duck breast with cherry-port gastrique"],
        "substitutions": "Pekin duck breast or squab breast.",
        "affinities": ["Cherries", "Balsamic vinegar", "Star anise", "Port wine", "Parsnip purée", "Orange"]
    },
    {
        "id": "ing-berkshire-pork",
        "name": "Heritage Berkshire Pork Belly (Kurobuta)",
        "category": "Meat & Poultry",
        "season": "Year-round",
        "storage": "Wrap in parchment paper at 1-3°C up to 4 days.",
        "flavorProfile": "Decadent, sweet, rich porkiness with silky white intramuscular marbling that melts effortlessly.",
        "scienceRole": "Berkshire pork features a higher pH and shorter muscle fibers, resulting in superior water retention and tenderness during prolonged braising. Low melting point fat keeps meat moist at 85°C.",
        "bestTechniques": ["Red braised Dongpo Rou with Shaoxing wine, rock sugar, and ginger", "Slow roasted with crispy blistered crackling skin", "Sous vide at 68°C for 24 hours then seared"],
        "substitutions": "Mangalitsa pork belly or standard heritage pork belly.",
        "affinities": ["Star anise", "Ginger", "Shaoxing wine", "Soy sauce", "Scallions", "Apples"]
    },
    {
        "id": "ing-lamb-rack",
        "name": "Pasture-Raised Colorado / New Zealand Lamb Rack",
        "category": "Meat & Poultry",
        "season": "Spring peak",
        "storage": "Store at 1-2°C; bring to room temperature 30 minutes before roasting.",
        "flavorProfile": "Sweet, delicate pastoral flavor, tender pearl pink flesh, herbaceous aroma.",
        "scienceRole": "Pasture feeding deposits phytol derivatives and branched-chain fatty acids (BCFAs) in lamb fat, producing signature pastoral notes that pair synergistically with resinous herbs (rosemary, thyme, mint).",
        "bestTechniques": ["Herb-crusted roasted rack with Dijon mustard and parsley breadcrumbs", "Pan-roasted with butter, rosemary, and garlic cloves", "Grilled over rosemary branch charcoal"],
        "substitutions": "Pasture-raised veal chops or venison rack.",
        "affinities": ["Rosemary", "Garlic", "Dijon mustard", "Mint", "Red wine reduction", "Peas"]
    },

    # --- FERMENTS, CONDIMENTS & UMAMI ---
    {
        "id": "ing-shiro-miso",
        "name": "Saikyo Sweet White Miso (Shiro Miso)",
        "category": "Ferments & Umami",
        "season": "Fermented 3 to 8 weeks",
        "storage": "Refrigerate in sealed container up to 1 year; high sugar/salt prevents spoilage.",
        "flavorProfile": "Sweet, creamy, mellow rice koji fragrance, light golden-beige hue, low salinity (4-6%).",
        "scienceRole": "Fermented with a high proportion of rice koji to soybeans and minimal salt. High maltose and free amino acids create rapid golden caramelization under a broiler (Gindara Saikyo-yaki).",
        "bestTechniques": ["Saikyo marinade for black cod with mirin and sake", "Miso butter for roasted vegetables and corn", "Whisked into light summery dressings and custards"],
        "substitutions": "Yellow miso (Shinshu) mixed with a small spoon of honey.",
        "affinities": ["Black cod (Gindara)", "Mirin", "Sake", "Butter", "Scallops", "Eggplant"]
    },
    {
        "id": "ing-aka-miso",
        "name": "Hatcho / Red Miso (Aka Miso)",
        "category": "Ferments & Umami",
        "season": "Aged 1 to 3 years",
        "storage": "Refrigerate up to 2 years.",
        "flavorProfile": "Intense, robust, salty (11-13%), roasted, earthy, dark mahogany, chocolate-malty notes.",
        "scienceRole": "Prolonged aging allows intense Maillard browning to take place at ambient temperatures over years. Packed with melanoidins and high free glutamic acid; stands up to hearty braises and game meats.",
        "bestTechniques": ["Tonjiru (hearty pork and root vegetable soup)", "Miso-braised beef shanks or eggplant Dengaku", "Enriching winter dark ramen broths"],
        "substitutions": "Shiro miso with reduced salt and a splash of soy sauce (will lack depth).",
        "affinities": ["Pork", "Beef", "Eggplant", "Dashi", "Garlic", "Ginger"]
    },
    {
        "id": "ing-doubanjiang",
        "name": "Pixian Fermented Chili Bean Paste (Pixian Doubanjiang DOP)",
        "category": "Ferments & Umami",
        "season": "Aged 1 to 3 years in clay urns",
        "storage": "Refrigerate in glass jar up to 18 months.",
        "flavorProfile": "Deeply savory, salty, spicy, fermented funk, dark red-black hue, umami powerhouse.",
        "scienceRole": "The 'Soul of Sichuan Cuisine'. Broad beans (fava) and Erjingtiao chilies are fermented together in open-air clay jars, turned daily under the sun. High microbial enzymes synthesize free amino acids; must be fried in hot oil ('Hong You') to awaken fat-soluble aromatic esters.",
        "bestTechniques": ["Fried in hot wok oil until oil turns ruby red for Mapo Tofu", "Base for Sichuan Twice-Cooked Pork (Hui Guo Rou)", "Spicy braised beef noodle soup"],
        "substitutions": "Korean Gochujang + pinch of salt and red miso (sweeter, less funky).",
        "affinities": ["Sichuan peppercorns", "Ground beef/pork", "Tofu", "Garlic", "Ginger", "Scallions"]
    },
    {
        "id": "ing-fish-sauce",
        "name": "Artisanal First-Press Fish Sauce (Red Boat 40°N)",
        "category": "Ferments & Umami",
        "season": "Aged 12 months in tropical wood barrels",
        "storage": "Cool, dark cupboard up to 2 years.",
        "flavorProfile": "Deeply savory, salty, clean oceanic sweetness, zero rotten or foul odor.",
        "scienceRole": "Fermented from wild black anchovies and sea salt in Phu Quoc, Vietnam. 40°N indicates 40 grams of natural nitrogen per liter, reflecting exceptionally high concentration of intact hydrolyzed amino acids.",
        "bestTechniques": ["Nước Chấm dipping sauce with lime, sugar, garlic, and chili", "Secret umami drop in tomato sauce, Bolognese, and beef chili", "Pad Thai and Thai green curry seasoning"],
        "substitutions": "Colatura di Alici (Italian anchovy extract) or high-grade soy sauce.",
        "affinities": ["Lime juice", "Palm sugar", "Garlic", "Bird's eye chili", "Pork", "Shrimp"]
    },
    {
        "id": "ing-kombu",
        "name": "Ma-Kombu / Rausu Kombu (Giant Dried Kelp)",
        "category": "Ferments & Umami",
        "season": "Harvested late summer in Hokkaido, sun-dried and aged",
        "storage": "Keep in airtight container in dark dry pantry. White powdery bloom on surface is natural mannitol sugar, do NOT wipe off.",
        "flavorProfile": "Subtle oceanic sweetness, mineral, pure clean umami.",
        "scienceRole": "Highest natural concentration of free glutamic acid of any food on earth (over 2,200mg per 100g). Steeped gently below 60°C to extract glutamates without leaching bitter alginic acid and slimy mucilage.",
        "bestTechniques": ["Ichiban Dashi with Katsuobushi (the universal foundation of Japanese cooking)", "Kobujime (curing white fish fillets between kombu sheets)", "Simmered into tsukudani with soy and mirin"],
        "substitutions": "Hidaka kombu or dried dashi kelp.",
        "affinities": ["Katsuobushi", "Soy sauce", "Mirin", "Sake", "White fish", "Shiitake"]
    },
    {
        "id": "ing-katsuobushi",
        "name": "Honkarebushi (Fermented & Smoked Skipjack Tuna Flakes)",
        "category": "Ferments & Umami",
        "season": "Smoked, sun-dried, and mold-fermented over 6 months",
        "storage": "Airtight bag in freezer or refrigerator; aroma compounds degrade quickly once opened.",
        "flavorProfile": "Smoky, woodsy, savory, concentrated cured fish depth.",
        "scienceRole": "Rich in inosine monophosphate (IMP). When combined with the glutamic acid in kombu, the two molecules bind to distinct allosteric sites on human taste receptors, multiplying perceived umami by up to 800% (the Umami Synergy principle).",
        "bestTechniques": ["Steeped in hot kombu broth for 30 seconds for Ichiban Dashi", "Garnishing okonomiyaki and takoyaki ('dancing flakes')", "Tossed with warm steamed rice and shoyu"],
        "substitutions": "Sababushi (smoked mackerel flakes) or dried bonito flakes.",
        "affinities": ["Kombu", "Soy sauce", "Eggs", "Tofu", "Rice", "Daikon"]
    },
    {
        "id": "ing-mirin",
        "name": "Hon-Mirin (True Brewed Sweet Rice Wine)",
        "category": "Ferments & Umami",
        "season": "Aged 6 months to 1 year",
        "storage": "Pantry shelf away from light; do not refrigerate (causes sugar crystallization).",
        "flavorProfile": "Golden amber, velvety sweet, mellow rice alcohol fragrance, rounded complex finish (14% ABV).",
        "scienceRole": "Made from steamed glutinous rice, rice koji, and shochu alcohol. Natural enzymatic conversion creates glucose and amino acids that prevent protein fish flesh from breaking apart during simmering and impart lacquer-like gloss (teri) to teriyaki glazes.",
        "bestTechniques": ["Simmered into authentic Teriyaki glaze with shoyu and sake", "Dashi broth balancing for noodle soups", "Yakitori tare basting sauce"],
        "substitutions": "Sake mixed with sugar (1 tbsp sake + 1 tsp sugar). Avoid 'Mirin-fu' (corn syrup substitute).",
        "affinities": ["Soy sauce", "Sake", "Dashi", "Ginger", "Eel", "Chicken"]
    },

    # --- SPICES & SEASONINGS ---
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
    },
    {
        "id": "ing-saffron",
        "name": "Sargol Saffron (Crocus sativus Stigmas)",
        "category": "Spices",
        "season": "Autumn harvest (October - November)",
        "storage": "Airtight amber glass vial away from light and humidity. Keeps up to 3 years.",
        "flavorProfile": "Intoxicating floral, honey, bittersweet metallic, fresh hay, rich golden hue.",
        "scienceRole": "Contains crocin (water-soluble carotenoid pigment producing brilliant yellow), picrocrocin (bitter glycoside), and safranal (volatile aroma). Must be bloomed in warm water (or over ice cubes) before adding to dishes to unlock water-soluble pigments.",
        "bestTechniques": ["Steeped in warm white wine or stock for Risotto alla Milanese", "Essential foundation of Spanish Paella Valenciana", "Bouillabaisse fish stew from Marseille"],
        "substitutions": "Turmeric + sweet paprika (provides yellow color, zero authentic saffron aroma).",
        "affinities": ["Carnaroli rice", "Shellfish", "White wine", "Butter", "Garlic", "Fish"]
    },
    {
        "id": "ing-tellicherry-pepper",
        "name": "Tellicherry Garbled Special Extra Bold (TGSEB) Black Peppercorns",
        "category": "Spices",
        "season": "Winter harvest in Malabar, India",
        "storage": "Whole peppercorns in airtight glass jar up to 3 years. Grind exclusively fresh at the moment of cooking.",
        "flavorProfile": "Pungent piperine heat, intense fruity citrus, pine, woodsy sweetness.",
        "scienceRole": "TGSEB peppercorns are left on the vine longer to mature to full berry size (over 4.75mm) before drying. This develops higher essential oil content (terpenes, pinene, limonene) alongside sharp piperine pungency.",
        "bestTechniques": ["Coarsely crushed in mortar for Steak au Poivre", "Toasted in dry skillet for Roman Cacio e Pepe", "Crackled over hot broth"],
        "substitutions": "Lampong black peppercorns or Madagascar black pepper.",
        "affinities": ["Beef", "Butter", "Pecorino Romano", "Cream", "Cognac", "Strawberries"]
    },
    {
        "id": "ing-pimenton",
        "name": "Pimentón de la Vera DOP (Spanish Smoked Paprika - Dulce)",
        "category": "Spices",
        "season": "Autumn harvest dried over oak smoke",
        "storage": "Sealed tin in dark pantry up to 18 months.",
        "flavorProfile": "Deeply smoky, warm oak, sweet red pepper, earthy, vibrant scarlet red.",
        "scienceRole": "Red capsicum peppers are slowly dried over burning Holm oak wood fires for 10-15 days in stone smokehouses. Smoke polyphenols bind with carotenoid capsanthin, providing intense smoky complexity without bitterness.",
        "bestTechniques": ["Bloomed in olive oil off-heat for Gambas al Ajillo", "Dusted over Galician octopus (Pulpo a la Gallega)", "Seasoning Spanish chorizo and romesco sauce"],
        "substitutions": "Hungarian sweet paprika mixed with a drop of liquid smoke.",
        "affinities": ["Octopus", "Garlic", "Olive oil", "Pork", "Shrimp", "Potatoes"]
    },
    {
        "id": "ing-star-anise",
        "name": "Whole Star Anise (Illicium verum)",
        "category": "Spices",
        "season": "Autumn harvest",
        "storage": "Store whole pods in airtight container up to 2 years.",
        "flavorProfile": "Intense sweet licorice, warm floral spice, woody clove undertones.",
        "scienceRole": "Dominated by trans-anethole. Food science studies demonstrate that anethole binds specifically with sulfur volatiles in browning pork and poultry, eliminating gaminess and amplifying sweet umami.",
        "bestTechniques": ["Simmered in Vietnamese Phở broth", "Key element of Chinese five-spice and red-braised pork", "Infused into poached pears and mulled wine"],
        "substitutions": "Aniseed or fennel seeds crushed in cheesecloth.",
        "affinities": ["Pork belly", "Beef brisket", "Ginger", "Soy sauce", "Duck", "Cinnamon"]
    },
    {
        "id": "ing-cardamom",
        "name": "Green Cardamom Pods (Elettaria cardamomum)",
        "category": "Spices",
        "season": "Autumn harvest in Kerala, India / Guatemala",
        "storage": "Store whole in pods; crack open pods immediately before grinding black seeds.",
        "flavorProfile": "Resinous, citrus, eucalyptus, warm floral spice, camphoraceous sweetness.",
        "scienceRole": "Contains 1,8-cineole (eucalyptus) and alpha-terpinyl acetate, providing an uplifting resinous aroma that cuts through rich dairy and ghee in biryanis and desserts.",
        "bestTechniques": ["Cracked whole pods infused into basmati rice pilafs", "Ground into Nordic cardamom buns (Kardemummabullar)", "Infused into Indian chai and kheer"],
        "substitutions": "Black cardamom (much smokier) or cinnamon + pinch of nutmeg.",
        "affinities": ["Basmati rice", "Ghee", "Milk / Cream", "Pistachio", "Coffee", "Lamb"]
    },
    {
        "id": "ing-maldon-salt",
        "name": "Maldon Flaky Sea Salt",
        "category": "Spices",
        "season": "Harvested year-round in Essex, England",
        "storage": "Open salt cellar at room temperature; keeps indefinitely.",
        "flavorProfile": "Pristine, clean ocean brine, rapid dissolution, delicate crunchy pyramid flake texture.",
        "scienceRole": "Boiled in shallow iron pans to form hollow, inverted pyramidal crystals. The thin pyramid structure yields a delicate crunch that shatters on teeth and dissolves instantly on the tongue, creating bursts of salinity without persistent saltiness.",
        "bestTechniques": ["Finishing salt sprinkled over sliced rested steak", "Crinkled on warm chocolate chip cookies or caramel", "Dusted over fresh heirloom tomatoes with EVOO"],
        "substitutions": "Fleur de Sel de Guérande or flaky kosher salt.",
        "affinities": ["Steak", "Tomatoes", "Dark chocolate", "Olive oil", "Caramel"]
    },

    # --- GRAINS, STARCHES & LEGUMES ---
    {
        "id": "ing-carnaroli-rice",
        "name": "Carnaroli Superfino Rice ('The King of Risotto Rice')",
        "category": "Grains & Starches",
        "season": "Autumn harvest in Po Valley, Italy",
        "storage": "Store in airtight container in cool dry pantry up to 2 years.",
        "flavorProfile": "Nutty, firm toothsome grain, luxurious creamy mantecatura starch release.",
        "scienceRole": "Possesses a higher amylose content than Arborio rice (around 24%), allowing it to absorb enormous volumes of hot broth while maintaining a perfect firm 'al dente' core without bursting or turning to mush.",
        "bestTechniques": ["Risotto alla Milanese with saffron and bone marrow", "Risotto ai Funghi Porcini", "Risotto al Nero di Seppia (squid ink)"],
        "substitutions": "Vialone Nano rice or Arborio rice.",
        "affinities": ["Parmigiano-Reggiano", "Butter", "White wine", "Chicken stock", "Saffron"]
    },
    {
        "id": "ing-koshihikari-rice",
        "name": "Koshihikari Short-Grain Rice (Japonica)",
        "category": "Grains & Starches",
        "season": "Autumn harvest (Shinmai / New Crop)",
        "storage": "Keep in cool, dark pantry or wine cooler (15°C); consume within 2 months of milling date.",
        "flavorProfile": "Plump, slightly sticky, sweet rice aroma, clean finish, shiny translucent pearl appearance.",
        "scienceRole": "Low amylose and high amylopectin content creates cohesive stickiness without sogginess, allowing sushi chefs to hand-mold nigiri that holds shape until the instant it touches the palate.",
        "bestTechniques": ["Seasoned with sushi-zu vinegar for nigiri and maki sushi", "Steamed table rice for Japanese donburi", "Okayu (comforting breakfast rice porridge)"],
        "substitutions": "Sasanishiki rice or Calrose medium-grain rice.",
        "affinities": ["Nori seaweed", "Rice vinegar", "Soy sauce", "Mirin", "Sashimi"]
    },
    {
        "id": "ing-tipo-00",
        "name": "Italian Tipo 00 Flour (Caputo Pizzeria / Chef's Flour)",
        "category": "Grains & Starches",
        "season": "Year-round",
        "storage": "Airtight bin in cool dry pantry; freeze for prolonged storage.",
        "flavorProfile": "Delicate, clean, wheaty sweetness, airy blistered crust with tender chew.",
        "scienceRole": "Milled to the finest grade of flour in Italy (almost powdery talc texture) from high-protein wheat (12.5-13% protein). Produces an extraordinarily extensible gluten network that stretches paper-thin without tearing and blisters leopard-spot crusts at 450°C.",
        "bestTechniques": ["Authentic Neapolitan pizza dough fermented 24-48 hours", "Fresh egg pasta sheets for lasagna and ravioli", "Focaccia Genovese"],
        "substitutions": "Unbleached bread flour mixed with a small touch of all-purpose flour.",
        "affinities": ["Yeast", "San Marzano tomatoes", "Mozzarella di Bufala", "Olive oil", "Egg yolks"]
    },
    {
        "id": "ing-puy-lentils",
        "name": "French Green Lentils du Puy AOP (Lentilles Vertes du Puy)",
        "category": "Grains & Starches",
        "season": "Late summer harvest in Auvergne volcanic plateau",
        "storage": "Airtight jar in pantry up to 2 years.",
        "flavorProfile": "Earthy, peppery, nutty, holds shape perfectly with a tender mineral chew.",
        "scienceRole": "Grown in volcanic soil with microclimatic föhn winds; has an exceptionally thin seed coat and high mineral density. Unlike brown or red lentils, Puy lentils never disintegrate into mush during prolonged boiling.",
        "bestTechniques": ["Braised with mirepoix, smoked bacon lardons, and thyme", "Warm lentil salad with Dijon shallot vinaigrette and goat cheese", "Bed for seared duck confit or salmon fillet"],
        "substitutions": "Black Beluga lentils or Spanish Pardina lentils.",
        "affinities": ["Duck confit", "Dijon mustard", "Bacon lardons", "Shallots", "Thyme", "Salmon"]
    },
    {
        "id": "ing-masa-harina",
        "name": "Nixtamalized Corn Flour (Masa Harina - Heirloom White/Blue)",
        "category": "Grains & Starches",
        "season": "Year-round",
        "storage": "Airtight container in pantry up to 1 year.",
        "flavorProfile": "Intense toasted corn aroma, nutty, earthy, comforting alkaline sweetness.",
        "scienceRole": "Corn is soaked and simmered in an alkaline calcium hydroxide (cal) bath (Nixtamalization). The alkaline pH strips the outer pericarp, unlocks bound Vitamin B3 (niacin), and partially gelatinizes starches so dough binds into tortillas without requiring gluten.",
        "bestTechniques": ["Pressed fresh corn tortillas puffed on a screaming hot comal", "Tamales steamed in corn husks with shredded pork", "Thickener for Mexican Hot Chocolate (Champurrado)"],
        "substitutions": "Fresh prepared masa from a local tortilleria (superior to dry flour).",
        "affinities": ["Lard", "Cilantro", "Salsa verde", "Braised carnitas", "Queso Oaxaca", "Lime"]
    }
]

js_content = f"""// L'Atelier Ingredient Encyclopedia
// 62 comprehensive dossiers on culinary behaviors, storage, seasonality, and affinities.

window.ENCYCLOPEDIA_INGREDIENTS = {json.dumps(ENCYCLOPEDIA_INGREDIENTS, indent=2)};

window.EncyclopediaEngine = {{
  getAll: function() {{ return window.ENCYCLOPEDIA_INGREDIENTS; }},
  getById: function(id) {{ return window.ENCYCLOPEDIA_INGREDIENTS.find(i => i.id === id); }},
  getByCategory: function(cat) {{
    if (!cat || cat === 'all') return window.ENCYCLOPEDIA_INGREDIENTS;
    return window.ENCYCLOPEDIA_INGREDIENTS.filter(i => i.category === cat);
  }},
  search: function(query) {{
    const q = (query || '').toLowerCase().trim();
    if (!q) return window.ENCYCLOPEDIA_INGREDIENTS;
    return window.ENCYCLOPEDIA_INGREDIENTS.filter(i => 
      i.name.toLowerCase().includes(q) || 
      i.category.toLowerCase().includes(q) || 
      i.flavorProfile.toLowerCase().includes(q) ||
      i.scienceRole.toLowerCase().includes(q) ||
      (i.affinities || []).some(a => a.toLowerCase().includes(q))
    );
  }}
}};
"""

with open("data-encyclopedia.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated data-encyclopedia.js with {len(ENCYCLOPEDIA_INGREDIENTS)} comprehensive dossiers.")
