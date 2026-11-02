# -*- coding: utf-8 -*-
"""
Definitions for the remaining master culinary recipes.
"""

from compile_master_library import build_recipe

RAW_RECIPES_DATA = [
    # Japanese Edomae Sushi
    {
        "id": "rec-edomae-sushi", "title": "Edomae Nigiri Sushi with Seasoned Akazu Rice",
        "cuisine": "Japanese Washoku", "category": "dinner", "slot": "opener", "difficulty": "Professional Technique",
        "prepMins": 45, "cookMins": 30, "totalMins": 75, "yieldServings": 2,
        "heroImage": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pinnacle of Tokyo craftsmanship: warm Koshihikari sushi rice seasoned with aged red sake lees vinegar (akazu), hand-molded into airy pillow nigiri, crowned with aged bluefin tuna, sea urchin, and kobujime cured sea bass, brushed with nikiri shoyu glaze.",
        "dietary": ["pescatarian", "dairy-free", "nut-free"],
        "sensoryRole": "Warm, acidic-savory umami shari rice melting instantaneously on the tongue with cool, unctuous cured fish.",
        "ingredients": [
            {"qty": 300, "unit": "g", "name": "Koshihikari short-grain sushi rice", "prep": "washed until water runs clear", "dept": "drygoods"},
            {"qty": 50, "unit": "ml", "name": "Akazu (aged red sake lees vinegar)", "prep": "aged 3+ years", "dept": "pantry"},
            {"qty": 15, "unit": "g", "name": "Okinawa sea salt", "prep": "fine mineral salt", "dept": "pantry"},
            {"qty": 10, "unit": "g", "name": "Raw cane sugar", "prep": "minimal sweetness", "dept": "pantry"},
            {"qty": 150, "unit": "g", "name": "Sashimi-grade Bluefin Tuna (Chutoro / medium-fatty)", "prep": "aged 4 days, sliced across the grain", "dept": "seafood"},
            {"qty": 150, "unit": "g", "name": "Wild Madai (Japanese Red Sea Bream)", "prep": "cured between kombu sheets 6 hours (Kobujime)", "dept": "seafood"},
            {"qty": 50, "unit": "g", "name": "Hokkaido Sea Urchin (Uni)", "prep": "chilled A-grade tongues", "dept": "seafood"},
            {"qty": 20, "unit": "g", "name": "Fresh Hon-Wasabi root", "prep": "grated on sharkskin oroshi", "dept": "produce"},
            {"qty": 45, "unit": "ml", "name": "Nikiri shoyu (soy sauce, mirin, sake, dashi reduction)", "prep": "for brushing fish", "dept": "pantry"}
        ],
        "equipment": [{"name": "Hangiri (sawara cypress rice tub)", "type": "specialty"}, {"name": "Shamoji (flat wooden rice paddle)", "type": "everyday"}, {"name": "Yanagiba sushi knife (single-bevel)", "type": "specialty"}],
        "miseEnPlace": ["Cook rice with kombu; transfer immediately to hangiri, season with warm akazu vinegar, and slice with shamoji while fanning to glossy sheen.", "Slice fish across the grain at a 45-degree angle in a single fluid draw.", "Grate fresh wasabi in circular motions on sharkskin."],
        "steps": [
            {"stepNum": 1, "text": "Cook rice in an earthenware donabe with a square of kombu. Transfer piping hot into the wet cypress hangiri tub.", "timerMins": 30, "sensoryCue": "Fragrant steam of sweet toasted rice."},
            {"stepNum": 2, "text": "Drizzle warm akazu vinegar mixture evenly over the rice. Cut and fold with shamoji using rapid slicing motions while fanning vigorously with a flat fan (uchiwa) to cool rice quickly to body temperature (36°C) while setting a glass-like sheen.", "timerMins": 5, "temperature": "36°C body temp", "sensoryCue": "Rice turns warm mahogany-amber and glossy without a single crushed grain."},
            {"stepNum": 3, "text": "Nigiri molding: Moisten hands with tezu (vinegar water). Scoop 18g warm rice. Shape into an airy, boat-shaped cylinder with gentle fingertip pressure, leaving tiny air pockets in the core (airy honeycomb).", "timerMins": 1, "sensoryCue": "Rice holds its shape firmly in the hand, but collapses effortlessly when placed in the mouth."},
            {"stepNum": 4, "text": "Dab a micro-speck of freshly grated wasabi onto the fish slice. Press fish against the rice pillow with index and thumb, roll 90 degrees, and set shape in two confident strokes (hon-tegaeshi).", "timerMins": 1, "sensoryCue": "Fish drapes organically over the rice, following its curve."},
            {"stepNum": 5, "text": "Brush fish surface with a light stroke of warm nikiri glaze. Serve immediately directly onto the chef's wooden counter; eat with fingers within 10 seconds.", "timerMins": 0.5, "sensoryCue": "Mirror-like sheen of nikiri; fish gently warms from the body-temperature rice."}
        ],
        "sensoryIndicators": {"see": "Glossy mahogany akazu rice, iridescent fish flesh with clean translucent grain, dark amber nikiri brush.", "hear": "Complete silence; faint crunch when picking up with fingers.", "smell": "Fermented sake lees acidity, ocean freshness, floral spicy wasabi, savory soy.", "feel": "Rice grain cloud collapsing effortlessly on the tongue, followed by melting, buttery seafood richness."},
        "scienceNotes": ["Akazu is brewed from aged sake lees (kasu) stored for 3-5 years; amino acids break down into rich glutamates, giving the vinegar its deep red color and complex umami without needing heavy added sugar.", "Fanning hot sushi rice rapidly lowers surface temperature, locking in surface starch retrogradation so each grain remains distinct and glossy."],
        "troubleshooting": [{"issue": "Rice became dense and gummy like dough", "cause": "Rice was stirred in circles rather than sliced with cutting motions, rupturing starch granules.", "solution": "Use slicing horizontal motions with the paddle and never mash rice against the tub."}],
        "substitutions": [{"original": "Akazu vinegar", "substitute": "Standard Komezu (rice vinegar) + 5ml dark soy sauce and 5ml mirin", "culinaryConsequence": "Replicates the darker hue and umami profile of traditional red vinegar."}],
        "flavorPairings": {"wine": "Junmai Daiginjo Sake (dry, clean), Grand Cru Chablis, or Champagne", "zeroProof": "Warm Gyokuro green tea or chilled Genmaicha with roasted brown rice", "complementarySides": ["Gari (sweet pickled young ginger slices)", "Aka dashi (red miso soup with clams)"]},
        "advancedTechnique": "The Ten-Second Rule: Traditional Edomae nigiri is served at precisely 36°C (human body temperature). After 30 seconds on the counter, the rice cools, the fish fat oxidizes, and the temperature contrast is lost; always eat nigiri within 10 seconds of placement.",
        "storageAndReheating": "Nigiri must be eaten within 15 minutes of assembly. Never refrigerate finished nigiri as cold temperatures crystallize rice starch into hard, chalky grains.",
        "nutritionEstimates": {"calories": 440, "proteinG": 32, "carbsG": 58, "fatG": 8},
        "relatedRecipes": ["rec-miso-black-cod", "rec-salmon-sashimi"],
        "relatedTechniques": ["lesson-seasoning-osmosis", "lesson-knife-skills"]
    },

    # French Bouillabaisse
    build_recipe(
        "rec-bouillabaisse", "Traditional Bouillabaisse Marseillaise with Spicy Rouille & Baguette",
        "French Provençal", "dinner", "climax", "Advanced", 40, 35, 6,
        "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=1200&q=80",
        "The immortal pride of Marseille: an aggressive rolling boil of rockfish, red mullet, sea bass, and wild langoustines in a golden saffron-infused court-bouillon with fennel, leeks, tomatoes, and orange zest. Served traditionally in two stages: first the fragrant boiling broth with garlic-rubbed croutons and fiery cayenne-garlic Rouille emulsion, followed by the carved fish on a platter.",
        ["pescatarian", "dairy-free", "nut-free"],
        "Complex, briny, saffron-golden broth with sweet licorice fennel and citrus notes, enriched by pungent garlic-chili rouille.",
        [
            {"qty": 1800, "unit": "g", "name": "Mixed Mediterranean fish (Red mullet, monkfish, sea bass, cod, gurnard)", "prep": "cleaned, cut into thick steaks", "dept": "seafood"},
            {"qty": 6, "unit": "pcs", "name": "Wild Mediterranean langoustines or head-on prawns", "prep": "whole", "dept": "seafood"},
            {"qty": 1000, "unit": "g", "name": "Small rockfish and fish heads/carcasses", "prep": "for foundational stock", "dept": "seafood"},
            {"qty": 2, "unit": "pcs", "name": "Fennel bulbs", "prep": "thinly sliced, fronds reserved", "dept": "produce"},
            {"qty": 2, "unit": "pcs", "name": "Leeks (white and pale green parts)", "prep": "washed, sliced", "dept": "produce"},
            {"qty": 4, "unit": "pcs", "name": "Ripe plum tomatoes", "prep": "coarsely chopped", "dept": "produce"},
            {"qty": 1, "unit": "g", "name": "Pure saffron threads", "prep": "steeped in 50ml warm water", "dept": "pantry"},
            {"qty": 1, "unit": "strip", "name": "Dried orange peel", "prep": "essential Provençal aromatic", "dept": "produce"},
            {"qty": 45, "unit": "ml", "name": "Pastis or Pernod (anise liqueur)", "prep": "for deglazing", "dept": "beverage"},
            {"qty": 80, "unit": "ml", "name": "Extra virgin olive oil", "prep": "for broth and rouille", "dept": "pantry"},
            {"qty": 2, "unit": "pcs", "name": "Egg yolks", "prep": "for Rouille emulsion", "dept": "dairy"},
            {"qty": 4, "unit": "cloves", "name": "Garlic", "prep": "pounded in mortar with salt and cayenne", "dept": "produce"},
            {"qty": 1, "unit": "loaf", "name": "French crusty baguette", "prep": "sliced into croutons, toasted crisp", "dept": "drygoods"}
        ],
        [{"name": "Wide, heavy 12-quart stockpot", "type": "everyday"}, {"name": "Granite mortar and pestle for Rouille", "type": "everyday"}, {"name": "Food mill (moulin à légumes)", "type": "specialty"}],
        ["Make rockfish broth: simmer fish carcasses with fennel, leek, tomato, and pastis for 30 minutes; pass through food mill.", "Pound garlic, cayenne, saffron, egg yolk, and olive oil in mortar into thick Rouille mayonnaise.", "Rub toasted baguette slices with raw garlic cloves.", "Steep saffron threads in warm water."],
        [
            {"stepNum": 1, "text": "Heat 40ml olive oil in a wide stockpot. Sauté sliced leeks, fennel, and tomatoes over medium heat for 8 minutes until softened.", "timerMins": 8, "sensoryCue": "Vegetables soften and release sweet allium and licorice perfume."},
            {"stepNum": 2, "text": "Deglaze with Pastis. Pour in 2.5 liters of the strained rockfish broth, orange peel, and steeped saffron infusion. Bring to a violent rolling boil.", "timerMins": 5, "temperature": "100°C rolling boil", "sensoryCue": "Vibrant golden-orange broth bubbles vigorously.", "scienceNote": "The name bouillabaisse comes from 'quand ça bouille, tu baisses' (when it boils, lower it). An initial violent rolling boil emulsifies olive oil into the gelatinous fish stock, giving the soup its golden opacity."},
            {"stepNum": 3, "text": "Add firm fish first (monkfish, gurnard) and cook at rolling boil for 6 minutes. Then add delicate fish (red mullet, sea bass) and langoustines; boil for 5 more minutes until fish is cooked through.", "timerMins": 11, "sensoryCue": "Langoustines turn bright coral-pink; fish steaks turn opaque and tender."},
            {"stepNum": 4, "text": "Lift fish and langoustines carefully with a slotted skimmer onto a large warmed serving platter. Keep warm with a ladle of broth.", "timerMins": 2, "sensoryCue": "Bountiful seafood mountain steaming with saffron and sea aromas."},
            {"stepNum": 5, "text": "Serve Stage 1: Ladle hot golden broth into deep bowls. Guests spread spicy garlic Rouille onto toasted croutons, float them in the boiling broth, and eat the soup.", "timerMins": 2, "sensoryCue": "Golden croutons soak in red rouille and saffron broth."},
            {"stepNum": 6, "text": "Serve Stage 2: Present the platter of fish, carve tableside, and serve alongside additional hot broth.", "timerMins": 2, "sensoryCue": "Flaky sweet fish bathed in fragrant saffron broth."}
        ],
        {"see": "Radiant saffron-orange boiling broth, ruby rouille on toasted croutons, coral langoustines and snowy white fish steaks.", "hear": "Violent bubbling in the cauldron; crunch of rouille crouton under spoon.", "smell": "Intoxicating Mediterranean sea breeze, sweet anise pastis, bitter orange peel, saffron, roasted garlic.", "feel": "Spicy, velvety rouille melting into piping hot, savory broth, followed by succulent tender seafood flakes."},
        ["Fish gelatin from rockfish heads acts as an emulsifier that suspends droplets of extra virgin olive oil under violent boiling kinetic energy, creating the characteristic opaque golden broth.", "Capsaicin and allicin in Rouille trigger trigeminal stimulation that contrasts the delicate sweetness of fresh Mediterranean fish."],
        [{"issue": "Fish broke into shredded mush in the pot", "cause": "Fish was stirred violently or delicate fish was added at the same time as firm fish.", "solution": "Always stagger cooking: firm fish (monkfish) first, delicate fish (red mullet) in the final 4-5 minutes."}],
        [{"original": "Mediterranean rockfish", "substitute": "Cod, Halibut, Red Snapper, and head-on wild shrimp", "culinaryConsequence": "Snapper and shrimp heads provide phenomenal gelatin and sweet oceanic flavor."}],
        {"wine": "Cassis Blanc (Provençal white with salinity and herbal garrigue notes) or Bandol Rosé", "zeroProof": "Chilled sparkling mineral water with fresh fennel fronds and orange twist", "complementarySides": ["Garlic-rubbed baguette croutons", "Homemade spicy Rouille"]},
        "Broth keeps refrigerated for 2 days. Seafood must be consumed fresh.",
        {"calories": 590, "proteinG": 62, "carbsG": 28, "fatG": 24},
        advanced_technique="Two-stage authentic service: In Marseille, Bouillabaisse is never served as a single combined soup bowl; the broth and croutons are savored first as an independent course to awaken the palate before the fish is consumed.",
        related_recipes=["rec-sole-meuniere", "rec-halibut-beurre-blanc"],
        related_techniques=["lesson-heat-control", "lesson-emulsions-mastery"]
    ),

    # French Onion Soup
    build_recipe(
        "rec-french-onion-soup", "Soupe à l'Oignon Gratinée (Classical French Onion Soup with Gruyère)",
        "French Classical", "lunch", "opener", "Intermediate", 20, 65, 4,
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1200&q=80",
        "The timeless Parisian bistro comfort: three pounds of yellow onions slowly caramelized for 45 minutes until melting, dark mahogany, and sweet, deglazed with dry white wine and Cognac, simmered in rich beef bone stock with thyme, ladled into ovenproof crocks over toasted baguette rounds, blanketed in cave-aged Gruyère and broiled until blistered, bubbling, and deeply browned.",
        ["nut-free"],
        "Deep, savory-sweet caramelized allium broth contrasting sharp, nutty melted Gruyère cheese crust and wine-soaked bread.",
        [
            {"qty": 1400, "unit": "g", "name": "Yellow onions (approx 5 large)", "prep": "sliced into uniform 3mm half-moons from pole to pole", "dept": "produce"},
            {"qty": 45, "unit": "g", "name": "Unsalted European butter", "prep": "for slow sweating and browning", "dept": "dairy"},
            {"qty": 15, "unit": "ml", "name": "Extra virgin olive oil", "prep": "prevents butter from scorching", "dept": "pantry"},
            {"qty": 120, "unit": "ml", "name": "Dry white wine (Sauvignon Blanc or Chardonnay)", "prep": "for deglazing", "dept": "pantry"},
            {"qty": 30, "unit": "ml", "name": "French Cognac or brandy", "prep": "for depth and aroma", "dept": "pantry"},
            {"qty": 1500, "unit": "ml", "name": "Rich brown beef stock or veal stock", "prep": "gelatinous, unsalted", "dept": "pantry"},
            {"qty": 20, "unit": "g", "name": "All-purpose flour", "prep": "to lightly singer the caramelized onions", "dept": "drygoods"},
            {"qty": 4, "unit": "sprigs", "name": "Fresh thyme", "prep": "tied with 1 bay leaf into a bouquet", "dept": "produce"},
            {"qty": 8, "unit": "slices", "name": "French baguette", "prep": "sliced 2cm thick, toasted completely dry in oven", "dept": "drygoods"},
            {"qty": 250, "unit": "g", "name": "Cave-aged Swiss Gruyère or Comté AOP", "prep": "shredded coarse", "dept": "dairy"},
            {"qty": 1, "unit": "clove", "name": "Garlic", "prep": "halved, to rub toasted croutons", "dept": "produce"}
        ],
        [{"name": "Heavy 6-quart enameled cast iron Dutch oven", "type": "everyday"}, {"name": "Four ovenproof ceramic soup crocks (lion's head bowls)", "type": "everyday"}, {"name": "High-heat oven broiler", "type": "everyday"}],
        ["Slice onions pole to pole for uniform melting without stringiness.", "Bake baguette slices at 150°C for 15 minutes until bone-dry and crisp like rusks (prevents crouton from turning to mush in soup).", "Shred Gruyère cheese coarse.", "Heat beef stock to gentle simmer on back burner."],
        [
            {"stepNum": 1, "text": "Melt butter and olive oil in Dutch oven over medium heat. Add all sliced onions and 1 teaspoon sea salt. Toss to coat evenly. Cover with lid and sweat for 10 minutes until onions collapse and release their water.", "timerMins": 10, "temperature": "120°C", "sensoryCue": "Onions turn translucent and watery, reducing in volume by half."},
            {"stepNum": 2, "text": "Uncover. Cook over medium-low heat for 35 to 45 minutes, stirring every few minutes. As fond browns on the bottom of the pot, scrape it up with a wooden spoon so it incorporates into the onions. Onions will progress from blonde to golden, then to deep amber, and finally to dark mahogany-brown.", "timerMins": 40, "temperature": "135°C", "sensoryCue": "Onions collapse into a rich, sweet, jammy dark mahogany paste; kitchen smells intoxicatingly of caramelized sugar.", "scienceNote": "Thermal caramelization breaks down sucrose into maltol and furans, while Maillard reactions between onion amino acids and reducing sugars create hundreds of savory melanoidin pigments."},
            {"stepNum": 3, "text": "Dust caramelized onions with 20g flour; stir constantly for 2 minutes to cook out raw starch flavor.", "timerMins": 2, "sensoryCue": "Flour absorbs onion fat and turns toasty."},
            {"stepNum": 4, "text": "Deglaze with Cognac and dry white wine, scraping up every speck of brown fond. Cook for 3 minutes until liquid is reduced by three-quarters.", "timerMins": 3, "sensoryCue": "Vigorous hissing steam of boiling alcohol, leaving a glossy wine-onion glaze."},
            {"stepNum": 5, "text": "Pour in hot beef stock and add thyme/bay bouquet. Bring to a gentle simmer, partially cover, and simmer over low heat for 25 minutes. Season with salt and freshly cracked black pepper. Discard herb bouquet.", "timerMins": 25, "temperature": "88°C", "sensoryCue": "Broth turns deep lustrous mahogany brown with sweet, rich savory perfume."},
            {"stepNum": 6, "text": "Assembly & Gratinée: Place 4 ovenproof crocks on a heavy baking sheet. Ladle piping hot soup into each crock, filling 80% full. Float 2 garlic-rubbed dry croutons on top of each bowl.", "timerMins": 2, "sensoryCue": "Croutons float securely on top of the broth."},
            {"stepNum": 7, "text": "Mound shredded Gruyère generously over the bread, allowing cheese to drape over the lip of the bowl. Transfer under a preheated HIGH broiler for 4 to 5 minutes until cheese is molten, bubbling vigorously, and blistered with deep golden-brown spots.", "timerMins": 5, "temperature": "Broiler High (260°C)", "sensoryCue": "Cheese bubbles and browns with an audible sizzle; edges form a crisp frico crust on ceramic."},
            {"stepNum": 8, "text": "Carefully remove crocks with oven mitts; rest 3 minutes before serving. Caution guests of molten temperature.", "timerMins": 3, "sensoryCue": "Spoon breaks through crisp browned cheese crust, releasing a plume of fragrant onion steam."}
        ],
        {"see": "Blistered golden-brown bubbling cheese crust draping over crock edges, dark mahogany onion broth beneath.", "hear": "Audible bubbling sizzle of molten cheese straight from the broiler.", "smell": "Nutty roasted Gruyère cheese, sweet caramelized alliums, wine reduction, fresh thyme.", "feel": "Stretchy, elastic cheese pull, followed by savory broth-soaked bread and melting sweet onions."},
        ["Browning onions slowly for 45 minutes converts harsh pungent allicin and lachrymatory compounds into sweet disulfides and caramelized oligosaccharides.", "Baking bread into dry rusks before placing in soup creates a structural cellular network that holds broth without dissolving into mush."],
        [{"issue": "Onions scorched and taste bitter and burnt", "cause": "Heat was too high or pot was left unattended without scraping fond.", "solution": "Cook over medium-low heat; add a tablespoon of water if fond darkens too rapidly to lift it without scorching."}],
        [{"original": "Swiss Gruyère", "substitute": "French Comté AOP, Emmental, or Fontina Valdostana", "culinaryConsequence": "Comté provides a sweeter, fruitier profile; Fontina melts into an ultra-stretchy blanket."}],
        {"wine": "Dry white Côtes du Rhône, Cru Beaujolais (Morgon), or a rich Saint-Émilion", "zeroProof": "Chilled sparkling apple cider with a dash of Angostura bitters and lemon peel", "complementarySides": ["Salade verte with Dijon vinaigrette"]},
        "The soup base keeps refrigerated for 5 days and freezes for 3 months. Always gratinée with fresh cheese right before serving.",
        {"calories": 520, "proteinG": 26, "carbsG": 44, "fatG": 28},
        advanced_technique="The Double-Cheese Layer: Line the bottom of the empty crock with a slice of bread and a pinch of cheese before ladling soup, then add the top crouton and cheese layer for an decadent multi-tiered gratinée.",
        related_recipes=["rec-quiche-lorraine", "rec-vichyssoise"],
        related_techniques=["lesson-heat-control", "lesson-mother-sauces"]
    )
]

print(f"Catalog data definitions ready: {len(RAW_RECIPES_DATA)} additional recipes loaded.")
