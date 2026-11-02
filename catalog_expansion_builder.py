# -*- coding: utf-8 -*-
"""
Expansion Catalog for L'Atelier Culinary Platform
Defines 82 additional comprehensive recipes to bring the total master catalog to 109 recipes.
"""

import json

EXPANSION_RECIPES = [
    # 1. Classical Tarte Tatin
    {
        "id": "rec-tarte-tatin", "title": "Classical Tarte Tatin with Crème Fraîche",
        "cuisine": "French Classical", "category": "dessert", "slot": "dessert", "difficulty": "Intermediate",
        "prepMins": 30, "cookMins": 45, "totalMins": 75, "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1519915028121-7d3463d20b13?auto=format&fit=crop&w=1200&q=80",
        "summary": "The accidental 1880s masterpiece of the Tatin sisters in Lamotte-Beuvron: crisp, tart Reinette apples caramelized slowly in butter and sugar until mahogany and translucent, draped with all-butter puff pastry, baked crisp, and inverted warm onto porcelain.",
        "dietary": ["vegetarian", "nut-free"],
        "sensoryRole": "Deep, buttery, bittersweet caramel enrobing melting, pectin-rich apples, contrasted by crisp, flaky puff pastry and tart crème fraîche.",
        "ingredients": [
            {"qty": 2000, "unit": "g", "name": "Firm tart apples (Honeycrisp, Pink Lady, or Reinette)", "prep": "peeled, cored, quartered, rested overnight to dry", "dept": "produce"},
            {"qty": 150, "unit": "g", "name": "Unsalted European butter", "prep": "room temperature", "dept": "dairy"},
            {"qty": 180, "unit": "g", "name": "Granulated sugar", "prep": "for caramel", "dept": "pantry"},
            {"qty": 1, "unit": "sheet", "name": "All-butter puff pastry (pâte feuilletée)", "prep": "rolled to 3mm thickness, cut to 26cm disc", "dept": "dairy"},
            {"qty": 200, "unit": "g", "name": "French Crème Fraîche", "prep": "chilled, for service", "dept": "dairy"},
            {"qty": 2, "unit": "g", "name": "Fleur de Sel", "prep": "to balance caramel", "dept": "pantry"}
        ],
        "equipment": [{"name": "9.5-inch heavy copper or cast iron Tatin skillet", "type": "everyday"}, {"name": "Round heatproof serving platter with lip", "type": "everyday"}],
        "miseEnPlace": ["Peel and quarter apples; rest uncovered in fridge for 12 hours so surface moisture evaporates.", "Smear soft butter thickly across the bottom of the skillet; pack with sugar.", "Pack apple quarters vertically in tight concentric circles."],
        "steps": [
            {"stepNum": 1, "text": "Pack apple quarters into the buttered and sugared skillet on their sides in tight concentric rings. They will shrink by 30% during cooking, so wedge them as tightly as possible.", "timerMins": 10, "sensoryCue": "Apples fit tightly with no gaps between quarters."},
            {"stepNum": 2, "text": "Place skillet over medium heat. As butter and sugar melt, they begin to boil and bubble vigorously around the apples. Cook for 25 to 30 minutes, basting apple tops occasionally with the foaming caramel.", "timerMins": 30, "temperature": "140°C", "sensoryCue": "Liquid transforms from clear sweet foam into a thick, bubbly, dark amber-mahogany caramel; aroma of roasted apples and toffee.", "scienceNote": "Thermal caramelization breaks sucrose into maltol and furans, while apple pectin hydrolyzes into soft gelatinous fruit flesh."},
            {"stepNum": 3, "text": "Remove skillet from heat. Let cool 10 minutes so bubbling stops. Lay the cold puff pastry disc directly over the hot caramelized apples, tucking the edges down inside the rim of the pan (tucking the blanket).", "timerMins": 2, "sensoryCue": "Pastry settles snugly over the apples."},
            {"stepNum": 4, "text": "Bake in a preheated 190°C (375°F) oven for 30 minutes until the puff pastry is deep golden brown and completely crisp throughout.", "timerMins": 30, "temperature": "190°C", "sensoryCue": "Puff pastry rises in crisp, laminated golden layers; caramel bubbles up along the pan edges."},
            {"stepNum": 5, "text": "THE INVERSION: Let rest for 15 minutes. Place a round serving platter over the skillet. Wearing heavy oven mitts, grip skillet and platter tightly together, and invert in one swift, confident, decisive motion. Tap pan bottom; lift skillet away.", "timerMins": 2, "sensoryCue": "A gleaming, glistening mosaic of translucent, dark amber caramelized apples glistening atop a crisp pastry pedestal."}
        ],
        "sensoryIndicators": {"see": "Lustrous, glass-like amber caramelized apples in concentric spirals atop golden pastry, white dollop of crème fraîche.", "hear": "Shattering flake of puff pastry under the cake server.", "smell": "Rich toffee caramel, baked cinnamon-like apples, browned dairy butter.", "feel": "Melting, jammy, unctuous apples yielding to crisp, flaky, shattering pastry."},
        "scienceNotes": ["Drying peeled apples uncovered overnight evaporates free water, preventing the caramel from becoming diluted and watery during stove cooking.", "Resting 15 minutes before inversion allows caramel to thicken slightly so it stays draped across the apples rather than pouring off as liquid syrup."],
        "troubleshooting": [{"issue": "Apples stuck to the pan bottom when inverted", "cause": "Pan cooled too long and caramel solidified like concrete.", "solution": "Set the skillet over a low flame for 60 seconds to remelt butterfat and caramel before inverting."}],
        "substitutions": [{"original": "Puff pastry", "substitute": "Pâte Brisée (all-butter shortcrust pastry)", "culinaryConsequence": "Shortcrust provides a denser, sandier biscuit crunch than airy laminated puff pastry."}],
        "flavorPairings": {"wine": "Sauternes, Coteaux du Layon, or Calvados apple brandy", "zeroProof": "Chilled sparkling apple cider with a dash of vanilla", "complementarySides": ["Cold French Crème Fraîche", "Tahitian vanilla bean ice cream"]},
        "advancedTechnique": "Pre-caramelization dry method: Cook sugar to a dry amber caramel first in the skillet, whisk in butter, then arrange apples and bake for cleaner jewel-like clarity.",
        "storageAndReheating": "Best served warm 30 minutes after inversion. Leftovers can be reheated in a 160°C oven for 10 minutes to recrisp pastry.",
        "nutritionEstimates": {"calories": 420, "proteinG": 4, "carbsG": 52, "fatG": 24},
        "relatedRecipes": ["rec-shattered-lemon-tart", "rec-souffle-chocolat"],
        "relatedTechniques": ["lesson-heat-control", "lesson-pastry-lamination"]
    },

    # 2. Ratatouille Niçoise (Confit Byaldi)
    {
        "id": "rec-ratatouille-byaldi", "title": "Ratatouille Niçoise Traditionnelle (Confit Byaldi Presentation)",
        "cuisine": "French Provençal", "category": "dinner", "slot": "mid", "difficulty": "Intermediate",
        "prepMins": 35, "cookMins": 90, "totalMins": 125, "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=1200&q=80",
        "summary": "The elevated Provençal celebration of summer garden abundance made famous by Chef Thomas Keller: a foundation of roasted bell pepper, tomato, and onion Piperade, topped with razor-thin shingled spirals of zucchini, yellow summer squash, Japanese eggplant, and Roma tomatoes, slow-baked under parchment until tender and glossy with herb-infused olive oil.",
        "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free", "nut-free"],
        "sensoryRole": "Sweet, silky, tender summer vegetables concentrated into deep savory harmony with aromatic thyme and peppery olive oil.",
        "ingredients": [
            {"qty": 2, "unit": "pcs", "name": "Medium zucchini (courgette)", "prep": "sliced into 1.5mm rounds on a mandoline", "dept": "produce"},
            {"qty": 2, "unit": "pcs", "name": "Yellow squash", "prep": "sliced into 1.5mm rounds on a mandoline", "dept": "produce"},
            {"qty": 4, "unit": "pcs", "name": "Japanese or Chinese slender eggplants", "prep": "sliced into 1.5mm rounds", "dept": "produce"},
            {"qty": 6, "unit": "pcs", "name": "Firm Roma tomatoes", "prep": "sliced into 1.5mm rounds", "dept": "produce"},
            {"qty": 2, "unit": "pcs", "name": "Red bell peppers", "prep": "roasted, peeled, seeded, chopped for Piperade", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Yellow onion", "prep": "finely diced for Piperade", "dept": "produce"},
            {"qty": 4, "unit": "cloves", "name": "Garlic", "prep": "minced fine", "dept": "produce"},
            {"qty": 60, "unit": "ml", "name": "Extra virgin olive oil", "prep": "first cold-pressed", "dept": "pantry"},
            {"qty": 4, "unit": "sprigs", "name": "Fresh thyme", "prep": "leaves stripped", "dept": "produce"},
            {"qty": 10, "unit": "ml", "name": "Aged balsamic vinegar", "prep": "for finishing vinaigrette", "dept": "pantry"}
        ],
        "equipment": [{"name": "Japanese mandoline slicer", "type": "specialty"}, {"name": "Oval or round enameled gratin baking dish", "type": "everyday"}, {"name": "Parchment paper cartouche", "type": "everyday"}],
        "miseEnPlace": ["Roast, peel, and mince red bell peppers.", "Sauté onion, garlic, minced peppers, and tomato paste into a smooth Piperade; spread across bottom of gratin dish.", "Slice zucchini, squash, eggplant, and tomatoes into identical 1.5mm disks."],
        "steps": [
            {"stepNum": 1, "text": "Prepare Piperade: Heat 30ml olive oil in skillet. Sweat diced onion and garlic for 6 minutes until soft. Stir in minced roasted bell peppers, 2 crushed tomatoes, and thyme. Cook 10 minutes until thick. Spread evenly across the bottom of the gratin dish.", "timerMins": 16, "sensoryCue": "Sweet, aromatic red vegetable foundation lining the dish."},
            {"stepNum": 2, "text": "Shingle vegetables: Arrange alternating slices of zucchini, eggplant, yellow squash, and tomato in tight, overlapping concentric spirals over the piperade until the dish is completely filled.", "timerMins": 15, "sensoryCue": "A breathtaking, mesmerizing spiral mosaic of alternating green, purple, yellow, and red vegetable disks."},
            {"stepNum": 3, "text": "Drizzle with remaining olive oil mixed with minced thyme, garlic, salt, and black pepper. Cut a piece of parchment paper to fit inside the rim (cartouche) and lay directly on top of vegetables.", "timerMins": 2, "sensoryCue": "Parchment traps moisture, allowing slow convective steaming without browning.", "scienceNote": "The cartouche traps steam right at the vegetable surface, allowing high-water vegetables (90% water) to soften gently in their own juices without dehydrating or scorching."},
            {"stepNum": 4, "text": "Bake in a 140°C (285°F) oven for 75 minutes until vegetables are completely tender. Remove parchment and bake uncovered for 15 minutes to concentrate juices.", "timerMins": 90, "temperature": "140°C", "sensoryCue": "Vegetables slump slightly, glistening with concentrated sweet juices and fragrant herb oil."},
            {"stepNum": 5, "text": "Serve warm or at room temperature, drizzled with a vinaigrette of extra virgin olive oil, balsamic vinegar, and fresh chervil.", "timerMins": 2, "sensoryCue": "Vibrant colors deepen into rich jewel tones."}
        ],
        "sensoryIndicators": {"see": "Hypnotic concentric jewel-toned spiral of purple, green, yellow, and red vegetable tiles, glossy with olive oil.", "hear": "Silent tender slicing.", "smell": "Sweet roasted bell pepper, thyme, caramelized allium, fresh fruity olive oil.", "feel": "Silky, melting vegetable slices offering delicate individual textures."},
        "scienceNotes": ["Eggplants contain bitter anthocyanins and solanine; slicing thin and slow-roasting with acidic tomatoes neutralizes bitterness and breaks down spongy air pockets into silky cream.", "Lycopene and beta-carotene in tomatoes and peppers are lipophilic, dissolving into the warm olive oil to create an antioxidant-dense, savory sauce."],
        "troubleshooting": [{"issue": "Vegetables dried out and turned leathery", "cause": "Baking was done without a parchment cartouche or oven temperature was too high.", "solution": "Always cover directly with a fitted parchment cartouche to capture steam."}],
        "substitutions": [{"original": "Japanese eggplant", "substitute": "Standard Italian globe eggplant cut into quarters before slicing", "culinaryConsequence": "Japanese eggplant has thin tender skin and few seeds, making it ideal for uniform disks."}],
        "flavorPairings": {"wine": "Bandol Rosé, Côtes de Provence, or a light Chinon (Cabernet Franc)", "zeroProof": "Chilled sparkling water with bruised rosemary and cucumber slice", "complementarySides": ["Crusty country sourdough bread", "Herb-roasted lamb chops or roast chicken"]},
        "advancedTechnique": "Keller's accordion presentation: Use a metal offset spatula to lift a neat 10-slice accordion fan of vegetables onto the plate, curving it into a gentle S-shape, crowned with a tiny bouquet of baby micro-greens.",
        "storageAndReheating": "Ratatouille tastes even more profound the next day at room temperature as flavors marry. Refrigerate up to 5 days; serve cold or gently rewarmed.",
        "nutritionEstimates": {"calories": 210, "proteinG": 5, "carbsG": 22, "fatG": 14},
        "relatedRecipes": ["rec-sole-meuniere", "rec-boeuf-bourguignon"],
        "relatedTechniques": ["lesson-heat-control", "lesson-seasoning-osmosis"]
    }
]

print(f"Loaded {len(EXPANSION_RECIPES)} initial expansion recipes.")
