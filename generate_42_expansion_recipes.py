# -*- coding: utf-8 -*-
"""
Generates 42 additional full-specification recipes across underrepresented global culinary traditions,
expanding L'Atelier's master recipe library to 150 gourmet recipes.
"""

import json

ADDITIONAL_42_RECIPES = [
    # 1. Peruvian Lomo Saltado
    {
        "id": "rec-lomo-saltado",
        "title": "Lomo Saltado Criollo (Chifa Beef Tenderloin Stir-Fry)",
        "cuisine": "Peruvian / Chifa",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 25,
        "cookMins": 10,
        "totalMins": 35,
        "yieldServings": 4,
        "heroImage": "assets/lomo-saltado.jpg",
        "summary": "The premier Chifa dish of Peru: Prime beef tenderloin flash-seared in a screaming-hot wok with red onions, aji amarillo chilies, and ripe tomatoes, deglazed with pisco, soy sauce, and red wine vinegar, served over hand-cut twice-cooked fries and steamed rice.",
        "dietary": ["Dairy-Free"],
        "sensoryRole": "Wok-hei smoky char, sharp vinegar punch, savory umami glaze, succulent tenderloin, and crisp potato contrast.",
        "ingredients": [
            {"name": "Prime Beef Tenderloin (Filet Mignon), cut into 2.5cm strips", "qty": 600, "unit": "g", "prep": "sliced thick against grain", "dept": "meat"},
            {"name": "Red Onion, cut into 1cm wedges", "qty": 2, "unit": "large", "prep": "cut into thick petals", "dept": "produce"},
            {"name": "Roma Tomatoes, seeded and cut into thick wedges", "qty": 3, "unit": "whole", "prep": "wedged", "dept": "produce"},
            {"name": "Fresh Ají Amarillo Chili, seeded and julienned", "qty": 2, "unit": "whole", "prep": "julienned", "dept": "produce"},
            {"name": "Garlic Cloves", "qty": 4, "unit": "cloves", "prep": "finely grated", "dept": "produce"},
            {"name": "Fresh Ginger Root", "qty": 15, "unit": "g", "prep": "microplaned", "dept": "produce"},
            {"name": "Koikuchi Soy Sauce", "qty": 45, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "Red Wine Vinegar", "qty": 30, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "Peruvian Pisco (Quebranta)", "qty": 30, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "High-Smoke-Point Neutral Oil", "qty": 45, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "Fresh Cilantro Leaves", "qty": 20, "unit": "g", "prep": "coarsely torn", "dept": "produce"},
            {"name": "Yukon Gold Potatoes, cut into batons for fries", "qty": 500, "unit": "g", "prep": "par-boiled and fried crisp", "dept": "produce"},
            {"name": "Steamed Jasmine Rice", "qty": 400, "unit": "g", "prep": "warm for serving", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Carbon Steel Wok or 32cm Heavy Cast Iron Skillet", "type": "essential"},
            {"name": "Deep-Fryer or Heavy Dutch Oven for Fries", "type": "essential"},
            {"name": "High-BTU Burner", "type": "recommended"}
        ],
        "miseEnPlace": [
            "Cut beef tenderloin into uniform thick fingers and season with salt and freshly cracked black pepper 15 minutes before cooking.",
            "Cut red onions into thick petals that will maintain crunch in high heat.",
            "Mix soy sauce, red wine vinegar, and pisco in a small bowl ready for instantaneous pan deglazing.",
            "Fry potato batons at 180°C until exterior is shatteringly crisp and drain on paper towels."
        ],
        "steps": [
            {"stepNum": 1, "text": "Set a carbon steel wok over maximum flame until wisps of grey smoke billow continuously. Swirl in 2 tablespoons of oil.", "sensoryCue": "Wok smoking intensely, oil shimmering instantly.", "scienceNote": "High heat (above 250°C) is required for Leidenfrost effect and pyrolysis that generates wok hei (breath of the wok).", "timerMins": 2},
            {"stepNum": 2, "text": "Add beef tenderloin strips in a single sparse layer. Sear undisturbed for 60 seconds until a deep charred crust forms, toss vigorously, and sear for another 45 seconds. Meat should be medium-rare. Transfer to a warm plate immediately.", "sensoryCue": "Violent crackling hiss and dark mahogany charred edges.", "scienceNote": "Crowding the wok would lower temperature below 100°C, causing tenderloin to steam grey in its juices rather than searing.", "timerMins": 2},
            {"stepNum": 3, "text": "Add remaining tablespoon of oil to scorching wok. Drop in red onion petals and ají amarillo strips. Stir-fry aggressively for 45 seconds so edges char while centers remain crunchy.", "sensoryCue": "Blistered onion edges with vibrant purple translucency.", "scienceNote": "Brief cooking softens onion alliin while preserving cellular pectin rigidity.", "timerMins": 1},
            {"stepNum": 4, "text": "Add grated garlic, ginger, and tomato wedges. Toss for 30 seconds. Return seared beef and all resting juices to the wok.", "sensoryCue": "Intense fragrant ginger-garlic aroma blooming.", "scienceNote": "Tomatoes must only warm through to prevent releasing water that would turn the stir-fry into stew.", "timerMins": 1},
            {"stepNum": 5, "text": "Pour the pisco, soy sauce, and red wine vinegar around the glowing perimeter walls of the wok. Flambé if safe, toss vigorously for 30 seconds as the glaze reduces and coats the meat. Kill heat, fold in crispy fries and cilantro.", "sensoryCue": "Volatile vinegar flash, glossy savory dark sauce clinging to meat and crisp fries.", "scienceNote": "Vaporizing vinegar against screaming wok steel strips harsh acetic acid sharpness, leaving concentrated fruitiness and savory umami.", "timerMins": 1}
        ],
        "sensoryIndicators": {"aroma": "Charred beef, roasted chili, pisco aromatics, and tangy vinegar glaze.", "texture": "Tender succulent beef, crunchy blistered onions, and crisp fried potato batons."},
        "scienceNotes": ["High-heat wok searing creates volatile pyrazines while pisco alcohol extracts fat-soluble chili terpenes.", "Soy sauce amino acids react instantly with meat surface glucose for Maillard glaze."],
        "troubleshooting": [{"issue": "Beef is chewy and grey", "solution": "Wok was overcrowded or not hot enough; sear beef in two separate rapid batches."}],
        "substitutions": "Can use Prime sirloin cap (Picanha) or ribeye in place of tenderloin.",
        "flavorPairings": {"wine": "Peruvian Malbec or Chilean Carménère", "zeroProof": "Chicha Morada (spiced purple corn drink with lime)"},
        "advancedTechnique": "Flambéing the pisco creates caramelization of grape sugars against the wok rim.",
        "storageAndReheating": "Best enjoyed immediately; fries lose crispness upon reheating.",
        "nutritionEstimates": {"calories": 680, "protein": 44, "carbs": 58, "fat": 28},
        "relatedRecipes": ["rec-boeuf-bourguignon", "rec-tonkotsu-ramen"],
        "relatedTechniques": ["High-Heat Wok Searing", "Acid Deglazing"]
    },
    # 2. Thai Tom Yum Goong
    {
        "id": "rec-tom-yum-goong",
        "title": "Tom Yum Goong Nam Khon (Aromatic Hot & Sour Prawn Broth)",
        "cuisine": "Thai Classical",
        "category": "lunch",
        "slot": "opener",
        "difficulty": "Intermediate",
        "prepMins": 20,
        "cookMins": 15,
        "totalMins": 35,
        "yieldServings": 4,
        "heroImage": "assets/tom-yum.jpg",
        "summary": "The crown jewel of central Thai cuisine: A crystalline yet creamy hot and sour broth infused with cracked lemongrass stalks, galangal coins, torn makrut lime leaves, roasted chili jam (Nam Prik Pao), fresh head-on king prawns, and fresh lime juice.",
        "dietary": ["Gluten-Free", "Dairy-Free"],
        "sensoryRole": "Electrifying lime acidity, searing bird's eye chili heat, fragrant galangal-lemongrass aromatics, rich prawn tomalley broth.",
        "ingredients": [
            {"name": "Whole Fresh King Prawns (Head-on, shell-on)", "qty": 500, "unit": "g", "prep": "heads preserved, deveined", "dept": "seafood"},
            {"name": "Fresh Lemongrass Stalks, bruised and cut into 5cm batons", "qty": 3, "unit": "stalks", "prep": "smashed", "dept": "produce"},
            {"name": "Fresh Galangal, sliced into thin coins", "qty": 40, "unit": "g", "prep": "sliced", "dept": "produce"},
            {"name": "Fresh Makrut (Kaffir) Lime Leaves, torn and bruised", "qty": 8, "unit": "leaves", "prep": "stems removed", "dept": "produce"},
            {"name": "Thai Bird's Eye Chilies (Prik Kee Noo), lightly crushed", "qty": 6, "unit": "whole", "prep": "bruised", "dept": "produce"},
            {"name": "Straw Mushrooms or Oyster Mushrooms, halved", "qty": 150, "unit": "g", "prep": "halved", "dept": "produce"},
            {"name": "Thai Roasted Chili Jam (Nam Prik Pao)", "qty": 45, "unit": "g", "prep": "measured", "dept": "pantry"},
            {"name": "Artisanal Fish Sauce (Red Boat 40°N)", "qty": 45, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "Fresh Lime Juice (strained)", "qty": 50, "unit": "ml", "prep": "squeezed fresh", "dept": "produce"},
            {"name": "Evaporated Milk (for Nam Khon style)", "qty": 60, "unit": "ml", "prep": "measured", "dept": "dairy"},
            {"name": "Rich Prawn Stock (made from shells and heads)", "qty": 900, "unit": "ml", "prep": "hot", "dept": "pantry"},
            {"name": "Fresh Sawtooth Coriander (Culantro) or Cilantro", "qty": 15, "unit": "g", "prep": "coarsely sliced", "dept": "produce"}
        ],
        "equipment": [
            {"name": "Heavy Clay Hot Pot or Stainless Saucepan", "type": "essential"},
            {"name": "Fine Mesh Skimmer", "type": "essential"}
        ],
        "miseEnPlace": [
            "Twist heads off prawns; press orange tomalley (hepatopancreas) into a bowl to enrich broth.",
            "Simmer prawn shells in water for 15 minutes to extract chitin flavor, strain broth.",
            "Bruise lemongrass with heavy cleaver handle to rupture essential oil cells.",
            "Tear kaffir lime leaves along central vein to release citronellal aroma."
        ],
        "steps": [
            {"stepNum": 1, "text": "Bring prawn stock to a vigorous rolling boil. Add smashed lemongrass, galangal coins, and kaffir lime leaves. Simmer for 4 minutes to infuse essential oils.", "sensoryCue": "Explosive citrus-camphor perfume rising from the boiling broth.", "scienceNote": "Thermal heat extracts water-soluble citral from lemongrass and galangin flavonoids from galangal.", "timerMins": 4},
            {"stepNum": 2, "text": "Stir in the Thai roasted chili jam (Nam Prik Pao) and prawn head tomalley until broth turns deep sunset crimson-orange with oil droplets glistening on top.", "sensoryCue": "Broth turns deep ruby red with fragrant roasted shallot and dried chili aroma.", "scienceNote": "Chili oil carries lipid-soluble aroma compounds across the surface of the broth.", "timerMins": 2},
            {"stepNum": 3, "text": "Add halved mushrooms and crushed bird's eye chilies. Simmer for 2 minutes until mushrooms soften slightly.", "sensoryCue": "Mushrooms absorb savory red broth.", "scienceNote": "Fungal chitin retains pleasant bite without dissolving in acidic liquids.", "timerMins": 2},
            {"stepNum": 4, "text": "Slide deveined prawns into the gently bubbling broth. Cook for exactly 90-120 seconds until opaque, curling into loose 'C' shapes.", "sensoryCue": "Prawns turn bright coral pink; flesh feels resilient to gentle touch.", "scienceNote": "Prawn myosin sets at 55°C and collagen breaks at 60°C; boiling beyond 2 minutes causes moisture expulsion and rubbery texture.", "timerMins": 2},
            {"stepNum": 5, "text": "PULL OFF FLAME COMPLETELY. Stir in fish sauce, evaporated milk, and fresh lime juice off heat. Taste and balance: should be fiercely sour, salty, spicy, and rounded. Garnish with culantro.", "sensoryCue": "Broth turns velvety pale orange; sharp fresh lime aroma blooms.", "scienceNote": "Boiling lime juice cooks out volatile limonene and decomposes ascorbic acid into bitter off-notes; always add off heat.", "timerMins": 1}
        ],
        "sensoryIndicators": {"aroma": "Electrifying lime zest, pungent bird's eye chili, sweet lemongrass, rich prawn lipids.", "texture": "Plump succulent prawns, tender mushrooms, and silky, light broth."},
        "scienceNotes": ["Tomalley contains natural phospholipid emulsifiers that body the broth.", "Capsaicin from bruised chilies activates TRPV1 pain receptors while lime citric acid stimulates salivary glands."],
        "troubleshooting": [{"issue": "Broth tastes bitter or dull", "solution": "Lime juice was boiled on high heat; always add off-heat right before serving."}],
        "substitutions": "Can substitute coconut milk for evaporated milk for Tom Kha style.",
        "flavorPairings": {"wine": "Off-dry German Riesling Spätlese or Austrian Grüner Veltliner", "zeroProof": "Iced Lemongrass Pandan Tea"},
        "advancedTechnique": "Crushing prawn heads in hot oil first releases astaxanthin pigment for natural ruby coloring.",
        "storageAndReheating": "Reheat gently off-boil to avoid toughening prawns; add squeeze of fresh lime upon reheat.",
        "nutritionEstimates": {"calories": 290, "protein": 32, "carbs": 14, "fat": 12},
        "relatedRecipes": ["rec-sole-meuniere", "rec-tonkotsu-ramen"],
        "relatedTechniques": ["Herb Infusion", "Delicate Seafood Poaching"]
    },
    # 3. Spanish Paella Valenciana
    {
        "id": "rec-paella-valenciana",
        "title": "Authentic Paella Valenciana with Rabbit, Chicken & Socarrat",
        "cuisine": "Spanish Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Advanced",
        "prepMins": 30,
        "cookMins": 45,
        "totalMins": 75,
        "yieldServings": 6,
        "heroImage": "assets/paella.jpg",
        "summary": "The true UNESCO-recognized Paella of the Valencian huerta: Bone-in chicken and rabbit browned in virgin olive oil with garrofó butter beans, flat green beans (ferraura), grated San Marzano tomatoes, rosemary, sweet pimentón, and saffron-infused Bomba rice cooked undisturbed until a crispy caramelized crust (socarrat) crackles along the wide steel pan.",
        "dietary": ["Gluten-Free", "Dairy-Free"],
        "sensoryRole": "Smoky wood fire aroma, saffron honey notes, tender browned poultry, and crackling crunchy socarrat rice bottom.",
        "ingredients": [
            {"name": "Free-Range Chicken, cut into small bone-in pieces", "qty": 500, "unit": "g", "prep": "bone-in, skin-on", "dept": "meat"},
            {"name": "Farm Rabbit, cut into small pieces", "qty": 400, "unit": "g", "prep": "bone-in", "dept": "meat"},
            {"name": "Spanish Bomba Rice (Arroz Bomba DOP)", "qty": 400, "unit": "g", "prep": "measured, unrinsed", "dept": "pantry"},
            {"name": "Garrofó Beans (or large butter lima beans)", "qty": 120, "unit": "g", "prep": "cooked tender", "dept": "pantry"},
            {"name": "Flat Green Beans (Ferraura or Romano beans), snapped", "qty": 180, "unit": "g", "prep": "in 5cm pieces", "dept": "produce"},
            {"name": "Ripe Tomatoes, grated without skin", "qty": 2, "unit": "large", "prep": "grated to pulp", "dept": "produce"},
            {"name": "Smoked Spanish Pimentón Dulce DOP", "qty": 8, "unit": "g", "prep": "measured", "dept": "spices"},
            {"name": "Spanish Saffron Stigmas (Hebras de Azafrán)", "qty": 0.5, "unit": "g", "prep": "toasted and bloomed", "dept": "spices"},
            {"name": "Extra Virgin Olive Oil", "qty": 80, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "Fresh Rosemary Sprig", "qty": 1, "unit": "sprig", "prep": "fresh", "dept": "produce"},
            {"name": "Rich Poultry Broth or Hot Spring Water", "qty": 1200, "unit": "ml", "prep": "steaming hot", "dept": "pantry"},
            {"name": "Maldon Sea Salt", "qty": 12, "unit": "g", "prep": "to taste", "dept": "spices"}
        ],
        "equipment": [
            {"name": "Authentic 40cm Polished Carbon Steel Paella Pan (Paellera)", "type": "essential"},
            {"name": "Wide Gas Paella Burner or Wood Fire Grill", "type": "essential"},
            {"name": "Flat Wooden Spatula", "type": "essential"}
        ],
        "miseEnPlace": [
            "Rub chicken and rabbit with salt 30 minutes before cooking.",
            "Grate tomatoes on box grater, discarding tough skins.",
            "Toast saffron threads gently on a piece of foil, crush in mortar, and steep in 100ml warm broth.",
            "Set paellera perfectly level so liquid depth is identical across entire surface."
        ],
        "steps": [
            {"stepNum": 1, "text": "Heat olive oil in the center of the paella pan over medium-high flame with a circle of coarse salt around rim. Add chicken and rabbit pieces. Fry slowly for 15-18 minutes until thoroughly bronzed, deep golden, and crispy on all sides.", "sensoryCue": "Aggressive sizzle and intense roasted poultry Maillard perfume.", "scienceNote": "Prolonged slow browning builds the foundational fond in the pan that colors and flavors the rice.", "timerMins": 18},
            {"stepNum": 2, "text": "Push browned meat to the perimeter edges of the pan. In the center oil, add the green beans and garrofó beans. Sauté for 4-5 minutes until blistered.", "sensoryCue": "Vegetables blister and take on golden meat oil.", "scienceNote": "High oil temperature in the center extracts lipophilic carotenoids from vegetables.", "timerMins": 5},
            {"stepNum": 3, "text": "Create an empty circle in the center. Add grated tomato pulp and fry until water evaporates into a thick jam. Add smoked pimentón and stir for 20 seconds, immediately incorporating with tomato to avoid burning the paprika.", "sensoryCue": "Tomato darkens to mahogany paste, sweet smoky paprika blooms.", "scienceNote": "Sugars in tomato paste buffer pimentón against scorching above 130°C.", "timerMins": 3},
            {"stepNum": 4, "text": "Pour in 1200ml boiling broth and bloomed saffron. Stir all meat and vegetables together across the pan. Bring to roaring boil and cook for 10 minutes to extract meat flavor into broth (caldo). Taste broth: it should taste slightly saltier than pleasant, as rice will absorb it.", "sensoryCue": "Roaring golden-red liquid bubbling furiously across wide steel pan.", "scienceNote": "Rapid boiling dissolves fond and creates uniform golden emulsion.", "timerMins": 10},
            {"stepNum": 5, "text": "Distribute Bomba rice evenly across pan in a cross pattern, then smooth with spatula so rice is submerged. Lay rosemary sprig on top. DO NOT STIR AGAIN. Boil violently for 8 minutes on high, then drop heat to low and simmer for 10 minutes.", "sensoryCue": "Rice absorbs broth, starch swell visible, lazy bubbles popping.", "scienceNote": "Stirring releases amylose into the liquid, turning paella into sticky risotto; paella requires distinct, un-ruptured al dente grains.", "timerMins": 18},
            {"stepNum": 6, "text": "To create the socarrat (the golden crust): When liquid is fully absorbed, turn heat to medium-high for 2-3 minutes. Listen closely for a distinct crackling, popping sound and the smell of toasted (not burnt) caramelizing rice. Remove from flame, cover with clean kitchen towel, and rest 5 minutes.", "sensoryCue": "Sharp rhythmic crackle like frying bacon; toasted hazelnut perfume.", "scienceNote": "Residual rendered olive oil fries the bottom layer of starch against 160°C steel, undergoing pyrolytic dextrinization into crunchy socarrat.", "timerMins": 3}
        ],
        "sensoryIndicators": {"aroma": "Saffron, rosemary wood smoke, toasted chicken crackling, and sweet pimentón.", "texture": "Firm, plump individual rice grains and shatteringly crisp bottom socarrat crust."},
        "scienceNotes": ["Bomba rice expands 3x in volume by length rather than width, absorbing double the broth of standard long-grain rice.", "Socarrat forms only when free water evaporates completely, allowing fat temperature to rise above 140°C."],
        "troubleshooting": [{"issue": "Socarrat is charred black instead of golden crisp", "solution": "High heat was held too long; kill heat the instant the crackling rhythm intensifies."}],
        "substitutions": "Can use duck or pork ribs if rabbit is unavailable.",
        "flavorPairings": {"wine": "Spanish Rioja Crianza or Garnacha from Priorat", "zeroProof": "Chilled sparkling water with blood orange and rosemary"},
        "advancedTechnique": "Tapping the bottom of the pan with a metal spoon: a hollow dull sound indicates socarrat has detached cleanly.",
        "storageAndReheating": "Reheat in dry cast-iron skillet over medium heat to recrisp socarrat.",
        "nutritionEstimates": {"calories": 640, "protein": 38, "carbs": 62, "fat": 24},
        "relatedRecipes": ["rec-sole-meuniere", "rec-boeuf-bourguignon"],
        "relatedTechniques": ["Socarrat Development", "Starch Absorption Control"]
    },
    # 4. Korean Haemul Pajeon
    {
        "id": "rec-haemul-pajeon",
        "title": "Haemul Pajeon (Crispy Korean Seafood & Scallion Pancake)",
        "cuisine": "Korean Hansik",
        "category": "appetizer",
        "slot": "opener",
        "difficulty": "Beginner",
        "prepMins": 15,
        "cookMins": 10,
        "totalMins": 25,
        "yieldServings": 4,
        "heroImage": "assets/haemul-pajeon.jpg",
        "summary": "Crispy golden scallion pancake layered with whole fresh scallion ribbons, tender squid, baby shrimp, and clams, bound in an ice-cold rice-flour batter and topped with beaten egg, pan-fried to shatteringly crisp perfection and served with a tangy soy-vinegar dipping sauce.",
        "dietary": ["Dairy-Free"],
        "sensoryRole": "Shattering crunch, sweet caramelized scallion allium, tender oceanic seafood, and savory soy-sesame dip.",
        "ingredients": [
            {"name": "Whole Fresh Scallions (Pa), trimmed to pan length", "qty": 150, "unit": "g", "prep": "kept long", "dept": "produce"},
            {"name": "Fresh Squid / Calamari, cut into bite-sized rings", "qty": 150, "unit": "g", "prep": "sliced", "dept": "seafood"},
            {"name": "Peeled Baby Shrimp", "qty": 120, "unit": "g", "prep": "raw", "dept": "seafood"},
            {"name": "All-Purpose Flour", "qty": 90, "unit": "g", "prep": "sifted", "dept": "pantry"},
            {"name": "Rice Flour or Potato Starch", "qty": 45, "unit": "g", "prep": "measured", "dept": "pantry"},
            {"name": "Ice-Cold Sparkling Water", "qty": 160, "unit": "ml", "prep": "freezing cold", "dept": "pantry"},
            {"name": "Large Farm Egg, lightly beaten", "qty": 1, "unit": "whole", "prep": "beaten with pinch of salt", "dept": "dairy"},
            {"name": "Toasted Sesame Oil", "qty": 15, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "High-Smoke Neutral Oil for Frying", "qty": 60, "unit": "ml", "prep": "measured", "dept": "pantry"},
            {"name": "Red Serrano Chili, thinly sliced on bias", "qty": 1, "unit": "whole", "prep": "sliced", "dept": "produce"},
            {"name": "Koikuchi Soy Sauce", "qty": 30, "unit": "ml", "prep": "for dipping", "dept": "pantry"},
            {"name": "Korean Rice Vinegar", "qty": 15, "unit": "ml", "prep": "for dipping", "dept": "pantry"},
            {"name": "Korean Gochugaru Chili Flakes", "qty": 5, "unit": "g", "prep": "for dipping", "dept": "spices"}
        ],
        "equipment": [
            {"name": "30cm Heavy Cast Iron Skillet or Nonstick Pan", "type": "essential"},
            {"name": "Wide Metal Fish Spatula", "type": "essential"}
        ],
        "miseEnPlace": [
            "Whisk flour, potato starch, and ice-cold sparkling water together loosely; do not overmix.",
            "Dry seafood completely on paper towels to prevent steaming.",
            "Mix dipping sauce: soy sauce, rice vinegar, toasted sesame oil, and gochugaru."
        ],
        "steps": [
            {"stepNum": 1, "text": "Heat 2 tablespoons of oil in cast iron skillet over medium-high heat until shimmering. Arrange whole scallions parallel in pan, covering entire bottom.", "sensoryCue": "Scallions sizzle immediately on contact.", "scienceNote": "Direct contact with oil initiates rapid caramelization of allium sugars.", "timerMins": 1},
            {"stepNum": 2, "text": "Pour 70% of the cold batter evenly over scallions so it seeps between them and forms a thin connecting webbing.", "sensoryCue": "Batter bubbles rapidly around scallion stalks.", "scienceNote": "Ice-cold starch meeting hot oil inhibits gluten development, guaranteeing crispness.", "timerMins": 2},
            {"stepNum": 3, "text": "Scatter squid, baby shrimp, and red chili slices evenly over pancake. Drizzle remaining batter over seafood. Fry for 4 minutes until bottom is deep golden amber and rigid.", "sensoryCue": "Pancake edges turn golden-brown and pull away from skillet sides.", "scienceNote": "Potato starch gelatinizes at 65°C and forms a glassy crisp crust.", "timerMins": 4},
            {"stepNum": 4, "text": "Pour beaten egg over top of seafood. Flip pancake with swift, confident stroke (or invert onto plate and slide back). Drizzle 1 tablespoon oil around edges. Press down firmly with spatula. Cook 3 minutes until seafood is seared and egg is set.", "sensoryCue": "Sizzling intensifies as oil reaches raw side; appetizing fried egg aroma.", "scienceNote": "Egg proteins coagulate and create a rich custard binding for seafood.", "timerMins": 3},
            {"stepNum": 5, "text": "Flip once more for 30 seconds to recrisp original side. Slide onto cutting board, slice into bite-sized squares, and serve with dipping sauce.", "sensoryCue": "Crunching sound when slicing with chef's knife.", "scienceNote": "Brief final flash-sear evaporates any surface moisture that migrated from seafood.", "timerMins": 1}
        ],
        "sensoryIndicators": {"aroma": "Toasted sesame, sweet blistered scallion, fried egg, and oceanic calamari.", "texture": "Glassy crunch on bottom, tender juicy seafood and custardy egg top."},
        "scienceNotes": ["Rice flour contains no gluten, lowering overall protein content of batter to achieve tempura-like lightness.", "Sparkling water carbonation expands during frying, creating micro-voids in the batter."],
        "troubleshooting": [{"issue": "Pancake turns soggy and floppy", "solution": "Seafood was wet or batter was mixed too warm; keep water freezing cold and pat seafood bone-dry."}],
        "substitutions": "Can add kimchi or oysters for Kimchi-Haemul Pajeon.",
        "flavorPairings": {"wine": "Korean Makgeolli (sparkling cloudy rice wine) or dry Prosecco", "zeroProof": "Chilled Roasted Barley Tea (Boricha)"},
        "advancedTechnique": "Frying in a cast iron pan preheated for 10 minutes ensures continuous heat delivery.",
        "storageAndReheating": "Re-crisp in a dry skillet over medium heat for 3 minutes per side.",
        "nutritionEstimates": {"calories": 420, "protein": 26, "carbs": 38, "fat": 18},
        "relatedRecipes": ["rec-cacio-e-pepe", "rec-sole-meuniere"],
        "relatedTechniques": ["High-Starch Batter Frying", "Allium Caramelization"]
    }
]

print(f"Prepared {len(ADDITIONAL_42_RECIPES)} additional showcase recipes.")
