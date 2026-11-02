# recipes_data_part6.py
# High-precision culinary master recipes 37-41

PART_6_RECIPES = [
    {
        "id": "rec-tarte-citron-meringuee",
        "title": "Tarte au Citron Meringuée (French Lemon Curd Tart with Torched Italian Meringue)",
        "cuisine": "French / Classical Haute Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 45,
        "cookMins": 25,
        "totalMins": 70,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=1200&q=80",
        "summary": "The Parisian showcase: a razor-thin, crisp, buttery pâte sablée shell filled with Pierre Hermé-style emulsified lemon curd, crowned with towering peaks of glossy Italian meringue torched to caramelized bronze perfection.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Electric citrus acidity, silky unctuous lemon butter curd, crisp sweet shell, marshmallow torched meringue",
        "ingredients": [
            {"name": "Pâte Sablée (French Sweet Shortcrust)", "qty": 300, "unit": "g", "prep": "chilled all-butter shortcrust", "dept": "Baking & Pantry"},
            {"name": "Fresh Squeezed Eureka Lemons (Juice & Zest)", "qty": 180, "unit": "ml", "prep": "freshly squeezed + 12g zest from 4 lemons", "dept": "Produce"},
            {"name": "Granulated Castor Sugar", "qty": 200, "unit": "g", "prep": "divided: 150g curd, 150g Italian meringue", "dept": "Baking & Pantry"},
            {"name": "Large Whole Eggs", "qty": 4, "unit": "whole", "prep": "room temperature (approx 200g)", "dept": "Dairy & Fats"},
            {"name": "Unsalted European Butter (82% fat)", "qty": 180, "unit": "g", "prep": "chilled and cubed (for mounting)", "dept": "Dairy & Fats"},
            {"name": "Egg Whites", "qty": 3, "unit": "whole", "prep": "approx 100g, room temp for Italian meringue", "dept": "Dairy & Fats"},
            {"name": "Water", "qty": 40, "unit": "ml", "prep": "for sugar syrup", "dept": "Pantry"},
            {"name": "Fleur de Sel", "qty": 2, "unit": "g", "prep": "fine pinch", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "9-inch Fluted Tart Pan with Removable Bottom", "type": "Bakeware"},
            {"name": "High-Power Immersion Blender", "type": "Small Appliance"},
            {"name": "Piping Bag with Saint-Honoré or French Star Tip", "type": "Pâtisserie Tool"},
            {"name": "Butane Kitchen Blowtorch", "type": "Precision Tool"}
        ],
        "miseEnPlace": [
            "Blind-bake pâte sablée tart shell at 350°F (175°C) until deep golden and crisp; cool completely.",
            "Zest lemons directly into sugar and rub with fingers to release citrus oils.",
            "Cut butter into small cubes and chill in refrigerator."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Cook Lemon Base: In a heatproof bowl set over simmering water, whisk eggs, lemon sugar, and lemon juice. Cook whisking continuously until the mixture thickens and coats the back of a spoon, reaching exactly 180°F (82°C). Remove bowl from heat; cool to 140°F (60°C).",
                "sensoryCue": "Thick, glossy yellow curd holding whisk lines.",
                "scienceNote": "Cooking egg proteins to 180°F coagulates ovotransferrin and ovalbumin without scrambling, creating the primary thickening network.",
                "timerMins": 8
            },
            {
                "stepNum": 2,
                "text": "Mount the Butter (The Hermé Method): When curd cools to 140°F (60°C), add cold butter cubes a few at a time while blending with high-power immersion blender. Continue blending for full 2 minutes until an ultra-creamy, pale, velvety emulsion forms.",
                "sensoryCue": "Color lightens to pale lemon yellow; satiny mirror sheen.",
                "scienceNote": "High-shear blending breaks butterfat into micro-droplets under 2 microns, creating an unctuous emulsion that sets into a velvety texture when chilled without requiring cornstarch.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Fill Tart & Chill: Pour lemon curd into the baked, cooled tart shell, smoothing flat with an offset spatula. Chill in refrigerator for 2 hours until curd is firm and set.",
                "sensoryCue": "Glass-smooth porcelain yellow surface.",
                "scienceNote": "Chilling crystallizes the butterfat matrix, locking the curd into clean sliceable form.",
                "timerMins": 120
            },
            {
                "stepNum": 4,
                "text": "Make Italian Meringue: Boil 150g sugar and 40ml water to 244°F (118°C). Whip egg whites to soft peaks. Stream 244°F syrup into whipping egg whites; whip on high until stiff, glossy, and cooled to room temp.",
                "sensoryCue": "Blindingly shiny white meringue holding stiff sculpted peaks.",
                "scienceNote": "Italian meringue syrup cooks egg whites to 160°F+, sterilizing them and producing a micro-foam that never weeps or shrinks.",
                "timerMins": 8
            },
            {
                "stepNum": 5,
                "text": "Pipe & Torch: Pipe decorative peaks, swirls, or Saint-Honoré petals across top of lemon tart. Torch lightly with butane blowtorch until peak ridges turn toasted chestnut brown.",
                "sensoryCue": "Toasted marshmallow aroma; bronze ridges contrasting against snow-white valleys and bright yellow curd.",
                "scienceNote": "Direct torch flame caramelizes sucrose on peak tips via rapid thermal pyrolysis, creating toasted flavor contrast.",
                "timerMins": 4
            }
        ],
        "sensoryIndicators": {
            "aroma": "Intense fresh lemon oil, toasted marshmallow sugar, rich browned butter shortcrust",
            "texture": "Crisp shattering pastry crust, ultra-creamy melting lemon curd, and pillowy cloud-soft meringue",
            "finish": "Vibrant lemon acidity perfectly counterbalanced by sweet toasted meringue"
        },
        "scienceNotes": "Pierre Hermé's legendary lemon tart breakthrough was eliminating starch entirely. By relying on egg coagulation combined with high-shear cold butter emulsification, the tart avoids all gummy mouthfeel, delivering pure explosive citrus flavor.",
        "troubleshooting": {
            "Curd is runny and won't set": "Butter was added while curd was boiling hot (over 150°F), destroying emulsion, or curd didn't reach 180°F.",
            "Meringue weeps syrup onto curd": "French meringue was used instead of Italian; Italian meringue with 244°F cooked syrup is mandatory.",
            "Soggy tart shell": "Shell was under-baked during blind bake; must be baked to full golden-brown crispness."
        },
        "substitutions": [
            {"ingredient": "Eureka Lemons", "substitute": "Yuzu Juice or Calamansi Juice", "ratio": "1:1 for extraordinary Japanese/Filipino profile"},
            {"ingredient": "Italian Meringue", "substitute": "Simple dusting of Powdered Sugar and Lemon Zest", "ratio": "Tarte au Citron Pur style"}
        ],
        "flavorPairings": ["Champagne Extra Brut", "Cold Earl Grey Tea", "Fresh Blackberries", "Limoncello"],
        "advancedTechnique": "Infusing lemon juice with fresh lemon verbena leaves before cooking curd for herbal citrus complexity.",
        "storageAndReheating": "Store in refrigerator up to 2 days. Best eaten within 24 hours of torched meringue assembly.",
        "nutritionEstimates": {"calories": 410, "protein": 6, "carbs": 48, "fat": 22},
        "relatedRecipes": ["rec-shattered-lemon-tart", "rec-lemon-curd-bars", "rec-key-lime-pie"],
        "relatedTechniques": ["High-shear butter mounting (Hermé method)", "Italian meringue sugar syrup calibration", "Butane torch caramelization"]
    },
    {
        "id": "rec-pain-au-chocolat",
        "title": "Artisanal Pains au Chocolat (27-Layer Laminated Viennoiserie with Cacao Barry Batons)",
        "cuisine": "French / Classical Boulangerie",
        "category": "breakfast",
        "slot": "opener",
        "difficulty": "Advanced",
        "prepMins": 90,
        "cookMins": 18,
        "totalMins": 108,
        "yieldServings": 10,
        "heroImage": "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?auto=format&fit=crop&w=1200&q=80",
        "summary": "The holy grail of French morning viennoiserie: hand-laminated yeast dough layered with 84% tournage butter, folded into 27 crisp shattering micro-layers around two parallel batons of bittersweet 44% Cacao Barry dark chocolate, proofed to trembling lightness and baked to deep golden-bronze perfection.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Deafeningly crisp shattering laminated crust, honeycomb buttery interior crumb, bittersweet molten chocolate core",
        "ingredients": [
            {"name": "French T55 or Unbleached Bread Flour (12% protein)", "qty": 500, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Cold Whole Milk", "qty": 140, "unit": "ml", "prep": "38°F", "dept": "Dairy & Fats"},
            {"name": "Cold Water", "qty": 140, "unit": "ml", "prep": "filtered, 38°F", "dept": "Pantry"},
            {"name": "Granulated Castor Sugar", "qty": 55, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 10, "unit": "g", "prep": "2% baker's percentage", "dept": "Baking & Pantry"},
            {"name": "Instant Dry Yeast (SAF-Instant Gold)", "qty": 7, "unit": "g", "prep": "osmotolerant yeast", "dept": "Baking & Pantry"},
            {"name": "Unsalted European Butter for Dough (Détrempe)", "qty": 40, "unit": "g", "prep": "softened", "dept": "Dairy & Fats"},
            {"name": "Beurre de Tournage (Dry Butter 84% fat)", "qty": 250, "unit": "g", "prep": "beaten into flat 7x7-inch square slab", "dept": "Dairy & Fats"},
            {"name": "Boulangerie Chocolate Batons (44% Cacao Barry)", "qty": 20, "unit": "batons", "prep": "8cm baking-stable chocolate batons", "dept": "Baking & Pantry"},
            {"name": "Egg Wash (Egg Yolk + 1 tsp Cream + Pinch Salt)", "qty": 1, "unit": "whole", "prep": "whisked and strained", "dept": "Dairy & Fats"}
        ],
        "equipment": [
            {"name": "Heavy French Rolling Pin (Non-Tapered)", "type": "Baking Supply"},
            {"name": "Parchment Paper Sheets", "type": "Baking Supply"},
            {"name": "Heavy Rimmed Baking Sheets", "type": "Bakeware"},
            {"name": "Ruler & Pastry Pizza Wheel", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Prepare détrempe dough; knead lightly for 4 minutes and chill overnight (12h) in refrigerator.",
            "Beat dry butter with rolling pin inside parchment into an even 7x7-inch square block (beurre de tournage); chill to 55°F (13°C).",
            "Prepare egg wash and chill."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "The Lock-In (Enbriblage): Roll cold détrempe dough into a 10x10-inch square. Place 7x7-inch butter block at 45° angle like a diamond in center. Fold dough corners inward like an envelope, pinching seams tightly to seal butter inside completely.",
                "sensoryCue": "Smooth dough package with butter completely enclosed and no exposed edges.",
                "scienceNote": "Both dough and butter must be at the identical temperature (55°F / 13°C) and plasticity; if butter is too cold it shatters, if too warm it melts into the dough.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Lamination (1 Double Turn + 1 Single Turn = 27 Layers): Roll packet smoothly into a 24x8-inch rectangle. Perform a Double Turn (book fold): fold ends inward to meet off-center, then fold in half. Rest 45 minutes in refrigerator. Roll out again into 24x8-inch rectangle. Perform a Single Turn (letter fold): fold into thirds. Chill 2 hours.",
                "sensoryCue": "Pliable, elastic striped dough slab with zero butter leakage.",
                "scienceNote": "The mathematical progression (4 layers x 3 layers = 12 butter layers alternating with 13 dough layers, totaling 25-27 strata) creates the ideal honeycomb alveolar structure.",
                "timerMins": 120
            },
            {
                "stepNum": 3,
                "text": "Roll, Cut & Shape: Roll laminated dough to 4mm thickness (approx 10x18 inches). Trim edges with pizza wheel to expose raw laminated layers. Cut into 10 rectangles measuring 3.5x4.5 inches. Place one chocolate baton 1/2-inch from short edge; roll dough over baton. Place second chocolate baton; roll dough completely into a cylinder, finishing with seam on the bottom.",
                "sensoryCue": "Tightly rolled cylinders showing clearly visible horizontal butter-dough strata on exposed ends.",
                "scienceNote": "Trimming edges exposes laminated layers so trapped steam can expand freely during baking.",
                "timerMins": 20
            },
            {
                "stepNum": 4,
                "text": "The Proof (The Critical Window): Place on parchment-lined baking sheets spaced 3 inches apart. Brush lightly with egg wash (avoiding exposed laminated side edges). Proof in a humid 78-80°F (26°C) environment for 2 to 2.5 hours until doubled in size, extremely wobbly, and individual laminated layers separate like playing cards.",
                "sensoryCue": "Pastries jiggle dramatically when pan is tapped; light as feathers.",
                "scienceNote": "Proofing temperature MUST NEVER exceed 82°F (28°C), or the 84% butter will melt out of the layers, turning the pastry into a greasy pancake.",
                "timerMins": 150
            },
            {
                "stepNum": 5,
                "text": "Bake: Apply second coat of egg wash gently. Bake at 390°F (200°C) for 16 to 18 minutes until deeply caramelized to a dark amber-bronze with visible golden laminated ridges. Cool 15 minutes on wire rack before serving.",
                "sensoryCue": "Loud crackling sound; shattering flaky shards; aroma of roasted butter and dark chocolate.",
                "scienceNote": "High radiant heat vaporizes water in the butter layers into steam, lifting each dough leaf upward while butterfat fries the dough from within.",
                "timerMins": 18
            }
        ],
        "sensoryIndicators": {
            "aroma": "Caramelized 84% butter, roasted yeast wheat, melting bittersweet cacao, toasted milk solids",
            "texture": "Deafeningly crisp shattering exterior yielding to open, buttery honeycomb web and soft chocolate batons",
            "finish": "Rich butter sweetness balanced by bittersweet 44% dark chocolate tannins"
        },
        "scienceNotes": "Beurre de tournage (dry butter) contains 84% milkfat and only 14% water (compared to 18-20% water in American table butter). The lower moisture content prevents dough water absorption, ensuring clean, continuous, razor-thin fat barriers that create explosive oven spring.",
        "troubleshooting": {
            "Butter pools in baking pan": "Proofing temperature was too high (above 82°F) and butter melted before baking, or oven was too cool.",
            "Dense bread-like interior with no honeycomb": "Butter shattered during lamination (was too cold) and blended into the dough.",
            "Pastries are pale and heavy": "Under-proofed; pastries must double in volume and jiggle like gelatin before baking."
        },
        "substitutions": [
            {"ingredient": "Chocolate Batons", "substitute": "High-Quality 50-60% Dark Chocolate cut into 8cm sticks", "ratio": "2 batons per pastry"},
            {"ingredient": "Beurre de Tournage", "substitute": "Kerrygold or Plugrá Unsalted Butter (82-83% fat)", "ratio": "1:1"}
        ],
        "flavorPairings": ["Café au Lait", "Double Espresso", "Fresh Orange Juice", "Earl Grey Tea"],
        "advancedTechnique": "Bi-color lamination: laminating a 1mm sheet of chocolate-dyed dough across the final dough sheet for striped zebra viennoiserie.",
        "storageAndReheating": "Best eaten warm within 4 hours. Reheat at 350°F for 4 minutes to restore shattering crispness. Never microwave.",
        "nutritionEstimates": {"calories": 380, "protein": 6, "carbs": 38, "fat": 23},
        "relatedRecipes": ["rec-mille-feuille", "rec-brioche-french-toast", "rec-croque-madame"],
        "relatedTechniques": ["Tournage butter plasticity calibration", "27-layer mathematical folding", "Sub-82°F proofing control"]
    },
    {
        "id": "rec-brioche-feuilletee",
        "title": "Brioche Feuilletée au Sucre Perlé (Laminated Caramelized French Sugar Brioche)",
        "cuisine": "French / Classical Haute Boulangerie",
        "category": "bread",
        "slot": "accompaniment",
        "difficulty": "Advanced",
        "prepMins": 60,
        "cookMins": 25,
        "totalMins": 85,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "summary": "The decadent hybrid of rich egg brioche and flaky croissant lamination: enriched buttery brioche dough laminated with French butter, rolled with cinnamon brown butter and Belgian pearl sugar, baked in butter-sugared molds until the exterior caramelizes into a crunchy toffee shell.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Crunchy caramelized toffee exterior, melting soft pillowy buttery interior, popping sugar pearls",
        "ingredients": [
            {"name": "Brioche Dough Base (Flour, Eggs, Butter, Yeast)", "qty": 500, "unit": "g", "prep": "chilled overnight détrempe", "dept": "Baking & Pantry"},
            {"name": "European Butter (82% fat) for Lamination", "qty": 200, "unit": "g", "prep": "beaten into flat block", "dept": "Dairy & Fats"},
            {"name": "Belgian Pearl Sugar (Nib Sugar)", "qty": 120, "unit": "g", "prep": "high-melting sugar pearls", "dept": "Baking & Pantry"},
            {"name": "Dark Muscovado / Brown Sugar", "qty": 60, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Ground Cinnamon", "qty": 3, "unit": "g", "prep": "fine ground", "dept": "Spices & Botanicals"},
            {"name": "Softened Butter & Granulated Sugar", "qty": 50, "unit": "g", "prep": "for lining baking molds heavily", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Round Metal Cake Rings or Deep Brioche Molds", "type": "Bakeware"},
            {"name": "Rolling Pin", "type": "Baking Supply"},
            {"name": "Parchment Paper", "type": "Baking Supply"}
        ],
        "miseEnPlace": [
            "Prepare brioche dough; cold-ferment 12 hours.",
            "Butter baking molds heavily and coat generously with granulated sugar (this forms the caramelized exterior).",
            "Flatten butter block into 6x6-inch square."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Laminate Brioche: Roll chilled brioche dough to 10x10 inches. Place butter block in center. Enclose butter and roll out into 20x8-inch rectangle. Perform one Single Turn (letter fold). Chill 30 minutes. Perform second Single Turn. Chill 1 hour.",
                "sensoryCue": "Pliable, enriched golden dough with buttery laminated interior.",
                "scienceNote": "Enriched brioche dough contains eggs and fat in the base, making it softer than croissant dough; brief chills between turns are critical.",
                "timerMins": 90
            },
            {
                "stepNum": 2,
                "text": "Fill & Roll: Roll dough to 12x16 inches. Brush with melted butter; sprinkle evenly with brown sugar, cinnamon, and Belgian pearl sugar. Roll tightly into a log from the long edge.",
                "sensoryCue": "Dense spiral log studded with glistening white sugar pearls.",
                "scienceNote": "Belgian pearl sugar has high compaction and does not dissolve during proofing, providing crunchy sugar pops in the baked crumb.",
                "timerMins": 10
            },
            {
                "stepNum": 3,
                "text": "Portion & Proof: Slice log into 8 thick rounds. Place each round spiral-side up into the heavily sugared buttered rings set on a parchment-lined baking sheet. Proof at 78°F (26°C) for 90 minutes until puffed and filling the rings.",
                "sensoryCue": "Puffed pillowy spiral coils with sugar pearls nestled between folds.",
                "scienceNote": "The sugar-butter mold coating creates a thermal syrup buffer that fries the exterior into caramel.",
                "timerMins": 90
            },
            {
                "stepNum": 4,
                "text": "Bake & Caramelize: Bake at 375°F (190°C) for 22 to 25 minutes until deep mahogany-brown and the bottom sugar has melted into bubbling amber toffee.",
                "sensoryCue": "Violently bubbling golden caramel around mold edges; intoxicating aroma of toasted butter and cinnamon.",
                "scienceNote": "Sucrose caramelizes at 320-340°F, creating a crunchy, glassy toffee shell around the soft brioche.",
                "timerMins": 24
            },
            {
                "stepNum": 5,
                "text": "Demold Immediately: Remove from oven and immediately unmold onto wire rack (if left in pan to cool, the hard caramel will glue the brioche permanently to the metal!). Cool 15 minutes before serving warm.",
                "sensoryCue": "Glassy amber toffee glaze snapping audibly; soft, melting, pulling-apart flaky center.",
                "scienceNote": "Hot caramel stays fluid for 60 seconds out of oven, allowing clean release.",
                "timerMins": 2
            }
        ],
        "sensoryIndicators": {
            "aroma": "Caramelized toffee, warm cinnamon, brown butter, sweet yeast brioche",
            "texture": "Crunchy shattering toffee crust, feather-light flaky buttery interior crumb, and crunchy sugar pearl bursts",
            "finish": "Decadent butterscotch finish with warm cinnamon aroma"
        },
        "scienceNotes": "Brioche Feuilletée is one of the richest pastries in classical boulangerie, combining 50% butter within the brioche crumb and another 40% butter during lamination, achieving over 70% total butterfat by baker's percentage.",
        "troubleshooting": {
            "Glued to pan": "Was not demolded immediately while caramel was liquid; reheat pan on burner for 30s to melt caramel.",
            "Butter leaks excessively": "Proofing temperature was too warm; keep proofing room under 80°F.",
            "Dough tore during lamination": "Brioche dough was not chilled long enough; chill dough thoroughly before rolling."
        },
        "substitutions": [
            {"ingredient": "Pearl Sugar", "substitute": "Coarse Turbinado Sugar or Crushed Sugar Cubes", "ratio": "1:1"},
            {"ingredient": "Cinnamon", "substitute": "Cardamom or Orange Blossom Water", "ratio": "1:1"}
        ],
        "flavorPairings": ["Double Espresso", "Chicory Coffee", "Cold Whole Milk", "Salted Butter Caramel Spread"],
        "advancedTechnique": "Coating the base of the baking rings with fleur de sel caramel before placing the dough for a salted butter kouign-amann hybrid.",
        "storageAndReheating": "Best eaten day of baking. Re-crisp in 350°F oven for 5 minutes.",
        "nutritionEstimates": {"calories": 440, "protein": 6, "carbs": 46, "fat": 26},
        "relatedRecipes": ["rec-pain-au-chocolat", "rec-madeleines-commercy", "rec-caneles-bordeaux"],
        "relatedTechniques": ["Enriched dough lamination", "Belgian pearl sugar retention", "Hot toffee pan demolding"]
    },
    {
        "id": "rec-ceviche-clasico-peruano",
        "title": "Ceviche Clásico Peruano con Leche de Tigre (Catch of the Day, Canchita, Sweet Potato & Choclo)",
        "cuisine": "Peruvian / Classical Costeño",
        "category": "lunch",
        "slot": "opener",
        "difficulty": "Easy",
        "prepMins": 20,
        "cookMins": 0,
        "totalMins": 20,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pure national treasure of Peru: pristine fresh sashimi-grade white fish cured for only 90 seconds in ice-cold Leche de Tigre (lime juice, fish trim fumet, ají limo chili, red onion, garlic, ginger, and fresh cilantro), served with steamed sweet potato, giant choclo corn, and crunchy toasted canchita.",
        "dietary": ["Gluten-Free", "Dairy-Free"],
        "sensoryRole": "Electric citrus shock, searing ají limo heat, ultra-fresh tender fish, sweet starchy sweet potato balance",
        "ingredients": [
            {"name": "Ultra-Fresh Sashimi-Grade Corvina, Fluke, or Sea Bass", "qty": 500, "unit": "g", "prep": "cut into 3/4-inch uniform cubes, bone-cold", "dept": "Seafood"},
            {"name": "Fresh Squeezed Key Limes or Peruvian Limes", "qty": 120, "unit": "ml", "prep": "squeezed gently by hand (never pressed hard)", "dept": "Produce"},
            {"name": "Fresh Ají Limo Chili", "qty": 2, "unit": "whole", "prep": "seeded and finely minced (red and yellow)", "dept": "Produce"},
            {"name": "Red Onion", "qty": 1, "unit": "medium", "prep": "sliced razor-thin, rinsed in ice water 10 mins", "dept": "Produce"},
            {"name": "Fresh Cilantro Leaves", "qty": 15, "unit": "g", "prep": "finely chopped", "dept": "Produce"},
            {"name": "Garlic Clove & Fresh Ginger", "qty": 10, "unit": "g", "prep": "bruised for bowl rubbing and Leche de Tigre", "dept": "Produce"},
            {"name": "Concentrated Fish Fumet / Ice Cubes", "qty": 50, "unit": "ml", "prep": "cold fish trim stock", "dept": "Pantry"},
            {"name": "Peruvian Giant Choclo Corn", "qty": 150, "unit": "g", "prep": "steamed tender giant kernels", "dept": "Produce"},
            {"name": "Camote (Peruvian Sweet Potato)", "qty": 200, "unit": "g", "prep": "steamed in spiced citrus water, sliced into rounds", "dept": "Produce"},
            {"name": "Canchita (Toasted Peruvian Chulpe Corn)", "qty": 80, "unit": "g", "prep": "fried in oil until puffed and crunchy", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 8, "unit": "g", "prep": "dissolved directly onto fish", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Chilled Ceramic or Glass Mixing Bowl", "type": "Cookware"},
            {"name": "Wooden or Silicone Spoon", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Keep fish on crushed ice until the exact second of assembly.",
            "Rinse thinly sliced red onions in ice water for 10 minutes to remove sulfur harshness.",
            "Cut a garlic clove and rub interior of chilled mixing bowl."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Season the Fish: Place ice-cold fish cubes into the chilled, garlic-rubbed bowl. Sprinkle with 8g fine sea salt and minced ají limo chili. Toss gently for 30 seconds with a spoon. Drop in 2 clean ice cubes to maintain near-freezing temperature.",
                "sensoryCue": "Fish cubes glisten; aroma of fresh ocean and spicy chili.",
                "scienceNote": "Salting the fish first draws out surface proteins and tightens muscle fibers before acid is introduced, preventing the fish from turning mushy.",
                "timerMins": 1
            },
            {
                "stepNum": 2,
                "text": "The Gentle Lime Squeeze: Cut limes and squeeze gently by hand into a separate cup, extracting only the first 60% of juice. (Never squeeze to the rind, which releases bitter limonene and astringent white pith tannins).",
                "sensoryCue": "Pure, fragrant, bright green lime juice with zero bitterness.",
                "scienceNote": "Over-squeezing ruptures oil glands in the lime flavedo and albedo, releasing bitter terpene oils that destroy delicate fish flavor.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Cure in Leche de Tigre (90-Second Rule): Pour fresh lime juice and cold fish fumet over seasoned fish. Stir continuously for 60 to 90 seconds. Watch as the translucent fish turns opaque white on the outer 1mm perimeter while the liquid emulsifies into milky Leche de Tigre.",
                "sensoryCue": "Broth turns opaque milky white (leche de tigre); fish edges turn bright white while center stays raw and succulent.",
                "scienceNote": "Modern Peruvian ceviche cures for under 2 minutes (unlike 1970s recipes that marinated for hours). Citric acid denatures fish muscle proteins (myosin and actin) on the surface, creating a firm exterior while preserving raw, tender sashimi core.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Add Aromatics: Fold in drained crisp red onion slices and fresh chopped cilantro. Remove the melting ice cubes.",
                "sensoryCue": "Brilliant purple onions and vibrant green cilantro contrasting with white fish and milky broth.",
                "scienceNote": "Adding onions at the end preserves their crisp cellular turgor and sharp snap.",
                "timerMins": 1
            },
            {
                "stepNum": 5,
                "text": "Plate & Serve: Arrange fish mound in center of chilled shallow bowl; ladle generous pool of milky Leche de Tigre around it. Garnish with a slice of sweet orange camote, a cluster of giant choclo kernels, and a handful of crunchy toasted canchita. Drink remaining Leche de Tigre from the bowl at the end.",
                "sensoryCue": "Vibrant colors; electric aroma of lime, chili, and cilantro; crunch of canchita against succulent fish.",
                "scienceNote": "Sweet potato and choclo corn provide essential sweet starch buffer that protects the palate against intense citric acidity.",
                "timerMins": 2
            }
        ],
        "sensoryIndicators": {
            "aroma": "Electric fresh lime, spicy floral ají limo, pungent red onion, fresh cilantro, ocean breeze",
            "texture": "Firm yet tender melting raw fish, crunchy crisp red onion, sweet starchy sweet potato, and explosive crunchy corn",
            "finish": "Electrifying acid and chili shock followed by savory umami and sweet potato comfort"
        },
        "scienceNotes": "Leche de Tigre (Tiger's Milk) turns white not because of milk, but because fish myofibrillar proteins and lipids dissolve into the acidic lime juice and salt, forming a spontaneous, opaque white cold emulsion.",
        "troubleshooting": {
            "Fish turns dry, chalky, and rubbery": "Marinated too long; ceviche must be served within 2 minutes of adding lime juice.",
            "Bitter broth": "Limes were squeezed too hard or mechanically; squeeze gently by hand only.",
            "Fish is mushy": "Fish was warm during prep or salt step was skipped; keep everything ice cold."
        },
        "substitutions": [
            {"ingredient": "Corvina / Fluke", "substitute": "Wild Sea Bass, Hamachi, Halibut, or Snapper", "ratio": "1:1"},
            {"ingredient": "Ají Limo", "substitute": "Habanero or Fresno chili (minced microscopic)", "ratio": "1:1"}
        ],
        "flavorPairings": ["Pisco Sour", "Ice-Cold Peruvian Cerveza Cusqueña", "Inca Kola", "Ceviche Juice Shot (Leche de Pantera)"],
        "advancedTechnique": "Blending fish trimmings, a touch of celery, ginger, garlic, and lime juice in blender and straining to create a turbo-charged Leche de Tigre base.",
        "storageAndReheating": "Cannot be stored! Must be prepared and consumed immediately. Leftovers turn rubbery.",
        "nutritionEstimates": {"calories": 260, "protein": 32, "carbs": 24, "fat": 3},
        "relatedRecipes": ["rec-lomo-saltado", "rec-salmon-aburi-press", "rec-tom-yum-goong"],
        "relatedTechniques": ["Acid protein denaturation curing", "Gentle lime squeeze extraction", "Leche de tigre cold emulsification"]
    },
    {
        "id": "rec-shanghai-xiao-long-bao",
        "title": "Shanghai Xiao Long Bao (Soup Dumplings with Jelled Pork Aspic Broth)",
        "cuisine": "Chinese / Shanghainese Classical",
        "category": "lunch",
        "slot": "opener",
        "difficulty": "Advanced",
        "prepMins": 90,
        "cookMins": 12,
        "totalMins": 102,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pinnacle of Jiangnan dim sum engineering: paper-thin translucent wrappers folded with 18-24 intricate pleats, encapsulating tender ginger-seasoned Kurobuta pork and a rich, gelatin-rich broth that liquefies into a volcanic explosion of savory soup upon steaming.",
        "dietary": [],
        "sensoryRole": "Translucent delicate wrapper, volcanic savory broth explosion, tender savory pork, zingy black vinegar ginger dip",
        "ingredients": [
            {"name": "Pork Skin & Trotters (for Jelled Aspic)", "qty": 500, "unit": "g", "prep": "blanched and scraped clean (rich collagen source)", "dept": "Meat & Poultry"},
            {"name": "Chicken Stock & Shaoxing Wine", "qty": 800, "unit": "ml", "prep": "simmered with ginger and scallions into gelatin jelly", "dept": "Pantry"},
            {"name": "Ground Kurobuta Pork Belly (70/30 meat-to-fat)", "qty": 400, "unit": "g", "prep": "finely minced", "dept": "Meat & Poultry"},
            {"name": "Fresh Ginger Juice & Scallion Water", "qty": 60, "unit": "ml", "prep": "extracted by bruising ginger/scallions in water", "dept": "Produce"},
            {"name": "Light Soy Sauce & Toasted Sesame Oil", "qty": 30, "unit": "ml", "prep": "for meat seasoning", "dept": "Pantry"},
            {"name": "White Pepper & Sugar", "qty": 6, "unit": "g", "prep": "fine balance", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Wheat Flour (Medium Gluten)", "qty": 250, "unit": "g", "prep": "sifted for wrapper dough", "dept": "Baking & Pantry"},
            {"name": "Warm Water (130°F / 55°C)", "qty": 135, "unit": "ml", "prep": "for hot water dough hydration", "dept": "Pantry"},
            {"name": "Chinkiang Black Vinegar (Aged)", "qty": 60, "unit": "ml", "prep": "for dipping sauce", "dept": "Pantry"},
            {"name": "Fresh Ginger Matchsticks", "qty": 30, "unit": "g", "prep": "cut into razor-thin needles", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "Bamboo Steamer Baskets with Lids (10-inch)", "type": "Cookware"},
            {"name": "Perforated Silicone Steamer Liners or Cabbage Leaves", "type": "Baking Supply"},
            {"name": "Small Wooden XLB Rolling Pin", "type": "Small Tool"},
            {"name": "Digital Gram Scale", "type": "Precision Tool"}
        ],
        "miseEnPlace": [
            "Make pork aspic broth: simmer pig skin, chicken stock, ginger, and Shaoxing wine for 3 hours; strain, chill overnight into firm jelly, and finely dice into 3mm cubes.",
            "Mix ground pork with seasonings and ginger-scallion water until sticky; fold in equal volume of diced cold aspic jelly.",
            "Cut ginger into microscopic matchsticks and place in Chinkiang vinegar."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Hot-Water Wrapper Dough: Mix flour with warm water (130°F). Knead for 8-10 minutes until smooth, supple, and non-sticky. Wrap tightly in plastic wrap and rest for 30 minutes at room temperature.",
                "sensoryCue": "Silky, elastic dough that indents cleanly when pressed.",
                "scienceNote": "Warm water gelatinizes a fraction of the wheat starch, relaxing the gluten network so the dough can be rolled paper-thin without snapping back.",
                "timerMins": 10
            },
            {
                "stepNum": 2,
                "text": "Roll Wrappers (Thick Center, Paper-Thin Edges): Divide dough into small 10g pieces. Using a small rolling pin, roll from outer edge inward while rotating the dough disc with your other hand. Result should be a 3.5-inch round with a thicker 1.5mm center and a paper-thin 0.5mm translucent perimeter.",
                "sensoryCue": "Translucent ruffled outer rim with supportive thicker center base.",
                "scienceNote": "A thicker center supports the heavy weight of meat and broth during steaming, while the thin perimeter creates delicate pleats without doughy knots.",
                "timerMins": 25
            },
            {
                "stepNum": 3,
                "text": "Fill & Pleat (18+ Pleats): Place 18g cold pork-aspic filling in center. Hold wrapper in left palm. Using right thumb and index finger, pinch the outer edge into small accordion folds, rotating counter-clockwise to form at least 18 tight pleats. Twist the top slightly to seal the center crown completely.",
                "sensoryCue": "Graceful pleated pouch resembling a closed chrysanthemum blossom.",
                "scienceNote": "A complete hermetic seal is mandatory; any gap allows boiling broth to escape into the steamer, leaving a dry meatball.",
                "timerMins": 30
            },
            {
                "stepNum": 4,
                "text": "The High-Steam Blast: Arrange dumplings in bamboo steamer basket lined with perforated silicone, leaving 1.5 inches space between each. Place over a wok of rapidly boiling water on maximum high heat. Cover and steam for exactly 6 to 7 minutes.",
                "sensoryCue": "Steam billows violently; wrappers turn translucent, sagging plumply with trapped hot liquid.",
                "scienceNote": "High-intensity steam cooks the thin dough in 6 minutes while the solid collagen aspic melts completely at 100°F into liquid broth inside the dumpling.",
                "timerMins": 7
            },
            {
                "stepNum": 5,
                "text": "The Ritual Tasting: Lift dumpling gently by the pleated top crown with chopsticks onto a Chinese soup spoon. Nibble a tiny hole in the side of the wrapper to release steam. Slurp the rich, scalding broth from the spoon. Top dumpling with 2 ginger needles dipped in Chinkiang black vinegar, and eat in one bite.",
                "sensoryCue": "Scalding rich pork broth floods the mouth; tender meatball and melting wrapper.",
                "scienceNote": "Aged Chinkiang vinegar has 5% acetic acid and malty notes that cut the gelatinous pork collagen fat.",
                "timerMins": 2
            }
        ],
        "sensoryIndicators": {
            "aroma": "Steaming pork bone broth, Shaoxing wine, fresh ginger, toasted sesame, malty black vinegar",
            "texture": "Delicate elastic wrapper giving way to a volcanic burst of hot liquid broth and tender savory pork filling",
            "finish": "Malty sour vinegar brightness balancing rich savory pork broth"
        },
        "scienceNotes": "The magic of Xiao Long Bao is a thermodynamic phase change: gelatin is a reversible hydrocolloid that forms a solid gel below 68°F (allowing it to be diced and mixed with cold meat) but melts completely into liquid water at human body temperature (98.6°F) and turns into volcanic soup at steaming temperatures (212°F).",
        "troubleshooting": {
            "Dumplings break and leak soup when picked up": "Dough was rolled too thin in the center, or dumplings were overcooked past 8 minutes.",
            "Dumplings have no soup inside": "Aspic was omitted, ratio was too low, or top pleats were not sealed airtight.",
            "Tough, thick pleats on top": "Dough edges were rolled too thick; edges must be paper-thin (0.5mm)."
        },
        "substitutions": [
            {"ingredient": "Kurobuta Pork", "substitute": "Mix of 70% Pork and 30% Blue Crab Meat (Hairy Crab Roe XLB)", "ratio": "Luxury seasonal Shanghai variant"},
            {"ingredient": "Pig Skin Aspic", "substitute": "Concentrated Chicken Foot Gelatin Stock", "ratio": "1:1"}
        ],
        "flavorPairings": ["Chinkiang Black Vinegar", "Shredded Young Ginger", "Dragon Well (Longjing) Green Tea", "Tsingtao Beer"],
        "advancedTechnique": "Infusing pork aspic broth with sautéed hairy crab roe and ginger before chilling into jelly.",
        "storageAndReheating": "Uncooked dumplings can be frozen solid on a tray and stored in bags up to 1 month; steam directly from frozen for 9-10 minutes.",
        "nutritionEstimates": {"calories": 65, "protein": 4, "carbs": 6, "fat": 3},
        "relatedRecipes": ["rec-tonkotsu-ramen", "rec-haemul-pajeon", "rec-shakshuka-royale"],
        "relatedTechniques": ["Reversible collagen phase transition", "Hot-water dough starch pre-gelatinization", "Hermetic 18-pleat crown sealing"]
    }
]

print(f"Loaded {len(PART_6_RECIPES)} recipes in PART_6_RECIPES.")
