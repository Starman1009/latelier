# recipes_data_part2.py
# High-precision culinary master recipes 6-15

PART_2_RECIPES = [
    {
        "id": "rec-opera-cake",
        "title": "Classical Gâteau Opéra (Joconde Sponge, Coffee Syrup & Bittersweet Ganache)",
        "cuisine": "French / Classical Haute Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Advanced",
        "prepMins": 90,
        "cookMins": 12,
        "totalMins": 102,
        "yieldServings": 12,
        "heroImage": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=80",
        "summary": "The Parisian classic created by Maison Dalloyau in 1955. Six distinct architectural tiers: almond biscuit Joconde soaked in concentrated espresso syrup, silky French coffee buttercream, dark chocolate ganache, and a flawless chocolate glaze (glaçage miroir) crowned with edible gold leaf.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Intense coffee roast, bittersweet chocolate, nutty almond sponge, silky layered elegance",
        "ingredients": [
            {"name": "Almond Flour (Superfine)", "qty": 150, "unit": "g", "prep": "sifted blanched almonds", "dept": "Baking & Pantry"},
            {"name": "Powdered / Icing Sugar", "qty": 150, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Whole Eggs", "qty": 4, "unit": "whole", "prep": "approx 200g, room temperature", "dept": "Dairy & Fats"},
            {"name": "Egg Whites", "qty": 4, "unit": "whole", "prep": "approx 140g, room temp", "dept": "Dairy & Fats"},
            {"name": "Granulated Sugar", "qty": 30, "unit": "g", "prep": "for meringue", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Cake Flour", "qty": 40, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Unsalted Butter", "qty": 30, "unit": "g", "prep": "melted and cooled", "dept": "Dairy & Fats"},
            {"name": "Fresh Brewed Espresso & Coffee Extract", "qty": 250, "unit": "ml", "prep": "reduced with 80g sugar syrup and 15ml dark rum", "dept": "Baking & Pantry"},
            {"name": "Valrhona Guanaja 70% Dark Chocolate", "qty": 200, "unit": "g", "prep": "for ganache and glaze", "dept": "Baking & Pantry"},
            {"name": "Heavy Cream (36% fat)", "qty": 180, "unit": "ml", "prep": "scalded", "dept": "Dairy & Fats"},
            {"name": "French Coffee Buttercream (Crème au Beurre)", "qty": 350, "unit": "g", "prep": "pâte à bombe base with Trablit coffee extract", "dept": "Dairy & Fats"},
            {"name": "Edible 24k Gold Leaf", "qty": 2, "unit": "sheets", "prep": "for delicate centerpiece garniture", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Half-Sheet Baking Pan (12x17 inch)", "type": "Bakeware"},
            {"name": "Silpat Baking Mat or Silicone Liner", "type": "Baking Supply"},
            {"name": "Adjustable Rectangular Cake Ring (8x8 or 8x10 inch)", "type": "Pâtisserie Tool"},
            {"name": "Long Offset Pastry Spatula", "type": "Pâtisserie Tool"}
        ],
        "miseEnPlace": [
            "Bake the Joconde sponge in half-sheet pan at 425°F (220°C) for 8 minutes; cool and cut into 3 identical 8x8-inch squares.",
            "Prepare coffee soaking syrup by simmering espresso, sugar syrup, and rum.",
            "Make dark chocolate ganache by pouring scalded cream over chopped 70% chocolate; cool to spreadable paste.",
            "Prepare coffee French buttercream using egg yolk pâte à bombe and European butter."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Bake Biscuit Joconde: Whip almond flour, powdered sugar, and whole eggs for 8 minutes until light and voluminous. Whip egg whites and sugar to glossy stiff peaks. Gently fold meringue, sifted flour, and melted butter into almond batter. Spread evenly across Silpat-lined half sheet and bake at 425°F (220°C) for 8 minutes. Cool and divide into three 8x8-inch squares.",
                "sensoryCue": "Golden, springy, pliable sponge that absorbs syrup without falling apart.",
                "scienceNote": "Almond flour provides fat that maintains moisture, while whipped whole eggs and meringue give structure to hold heavy syrup absorption.",
                "timerMins": 8
            },
            {
                "stepNum": 2,
                "text": "Bottom Seal: Melt 50g dark chocolate. Brush a razor-thin layer of chocolate across one side of the first Joconde layer. Chill 5 minutes until set. Flip chocolate-side down onto parchment (this forms an impermeable base that prevents the cake from sticking to the cake board when served).",
                "sensoryCue": "Thin matte chocolate barrier.",
                "scienceNote": "The tempered chocolate base prevents coffee syrup from leaking onto the presentation platter.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Soak bottom sponge thoroughly with espresso syrup. Spread half of the coffee buttercream in an immaculate 3mm layer using an offset spatula. Place second Joconde sponge on top; press gently. Soak with espresso syrup. Spread dark chocolate ganache in an even 3mm layer.",
                "sensoryCue": "Syrup glistens on sponge surface; layers are level and calibrated.",
                "scienceNote": "Uniform layer height is critical to Opéra architecture; uneven cream produces sloping top glaze.",
                "timerMins": 15
            },
            {
                "stepNum": 4,
                "text": "Place third Joconde sponge, soak generously with coffee syrup. Spread remaining coffee buttercream over top, smoothing with a warm bench scraper until glass-flat. Chill cake in freezer for 30 minutes until buttercream is firm as stone.",
                "sensoryCue": "Pristine level top surface with zero spatula marks.",
                "scienceNote": "Freezer chilling hardens the butter emulsion so hot glaze can flow across without melting the buttercream.",
                "timerMins": 30
            },
            {
                "stepNum": 5,
                "text": "Pour warm chocolate glaze (at exactly 90-95°F / 32-35°C) across the chilled cake in one fluid motion; smooth with one swipe of an offset spatula. Chill 1 hour. Trim all 4 perimeter edges by 1/4 inch with a hot chef's knife dipped in boiling water to reveal pristine multi-colored horizontal stripes. Garnish center with gold leaf.",
                "sensoryCue": "Mirror-reflective chocolate crown; sharp geometric horizontal strata of black, cream, and almond sponge.",
                "scienceNote": "Glaze temperature of 95°F allows smooth sheet flow without dissolving the underlying buttercream.",
                "timerMins": 60
            }
        ],
        "sensoryIndicators": {
            "aroma": "Dark roasted espresso, bittersweet cocoa, almond marzipan, dark rum",
            "texture": "Multi-tiered harmony: syrupy sponge melting with silky buttercream and snapping glaze",
            "finish": "Persistent roasted coffee and cocoa tannins balanced by smooth dairy richness"
        },
        "scienceNotes": "Opéra cake depends on precise thermodynamic assembly: each layer must be chilled to solidify fats before the next tier is added. The pâte à bombe coffee buttercream provides structural firmness when chilled due to saturated dairy triglycerides, yet melts at body temperature (98.6°F) on the palate.",
        "troubleshooting": {
            "Glaze melts buttercream and mixes": "Buttercream was not chilled enough or glaze was too hot (over 100°F).",
            "Edges rip or smear when trimming": "Knife was cold; dip knife in hot water and wipe dry between every single cut.",
            "Dry cake texture": "Joconde was under-soaked; sponge must absorb almost its entire weight in coffee syrup."
        },
        "substitutions": [
            {"ingredient": "Trablit Coffee Extract", "substitute": "Triple-strength reduced espresso", "ratio": "1:1"},
            {"ingredient": "Dark Rum", "substitute": "Cognac, Grand Marnier, or additional espresso", "ratio": "1:1"}
        ],
        "flavorPairings": ["Double Espresso", "Single Malt Islay Scotch", "Tawny Port", "Raspberry Coulis"],
        "advancedTechnique": "Calligraphic chocolate piping: piping the word 'Opéra' across the center mirror glaze with a paper cornet.",
        "storageAndReheating": "Store covered in refrigerator up to 5 days. Remove 20 minutes before serving so buttercream softens slightly.",
        "nutritionEstimates": {"calories": 490, "protein": 7, "carbs": 46, "fat": 31},
        "relatedRecipes": ["rec-mille-feuille", "rec-tiramisu", "rec-paris-brest"],
        "relatedTechniques": ["Pâte à bombe emulsion", "Biscuit Joconde lamination", "Mirror glaze temperature calibration"]
    },
    {
        "id": "rec-french-macarons",
        "title": "French Macarons au Chocolat Noir (Pied Formed Shells with 66% Ganache)",
        "cuisine": "French / Classical Haute Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Advanced",
        "prepMins": 45,
        "cookMins": 16,
        "totalMins": 61,
        "yieldServings": 24,
        "heroImage": "https://images.unsplash.com/photo-1569864358642-9d1684040f43?auto=format&fit=crop&w=1200&q=80",
        "summary": "The holy grail of French confectionery: smooth satin shells with iconic ruffled ruffled feet (le pied), crisp delicate shells giving way to chewy almond centers, sandwiched with bittersweet 66% Valrhona Caraïbe chocolate ganache.",
        "dietary": ["Vegetarian", "Gluten-Free"],
        "sensoryRole": "Delicate shattering crisp shell, chewy almond interior, intense bittersweet ganache core",
        "ingredients": [
            {"name": "Superfine Blanched Almond Flour", "qty": 150, "unit": "g", "prep": "ground extra fine and sifted", "dept": "Baking & Pantry"},
            {"name": "Pure Powdered Sugar (without cornstarch)", "qty": 150, "unit": "g", "prep": "sifted twice with almond flour (tant pour tant)", "dept": "Baking & Pantry"},
            {"name": "Aged Egg Whites", "qty": 110, "unit": "g", "prep": "separated 24h prior, room temp (divided: 55g + 55g)", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 150, "unit": "g", "prep": "for Italian sugar syrup", "dept": "Baking & Pantry"},
            {"name": "Mineral Spring Water", "qty": 38, "unit": "ml", "prep": "for syrup", "dept": "Pantry"},
            {"name": "Dutch Cocoa Powder (Extra Brute)", "qty": 15, "unit": "g", "prep": "sifted with tant pour tant", "dept": "Baking & Pantry"},
            {"name": "Valrhona Caraïbe 66% Dark Chocolate", "qty": 160, "unit": "g", "prep": "finely chopped", "dept": "Baking & Pantry"},
            {"name": "Heavy Cream (36% fat)", "qty": 140, "unit": "ml", "prep": "scalded", "dept": "Dairy & Fats"},
            {"name": "Unsalted European Butter", "qty": 25, "unit": "g", "prep": "softened at 68°F", "dept": "Dairy & Fats"}
        ],
        "equipment": [
            {"name": "Digital Candy Thermometer", "type": "Precision Tool"},
            {"name": "Piping Bag with #804 (10mm) Plain Round Tip", "type": "Pâtisserie Tool"},
            {"name": "Heavy Rimmed Baking Sheets (Doubled)", "type": "Bakeware"},
            {"name": "Teflon / Silpat Macaron Mats with Printed Guides", "type": "Baking Supply"}
        ],
        "miseEnPlace": [
            "Age egg whites for 24-48 hours in refrigerator to relax protein bonds; bring to 70°F room temp before whipping.",
            "Pulse almond flour, powdered sugar, and cocoa powder in food processor for 10 seconds; sift twice through medium mesh.",
            "Fit piping bag with 10mm round tip and prepare baking sheets with Silpat mats."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Tant Pour Tant Paste: Mix the first 55g of raw egg whites directly into the sifted almond flour, powdered sugar, and cocoa powder with a stiff spatula until a dense, uniform paste forms. Cover with plastic wrap.",
                "sensoryCue": "Thick marzipan-like chocolate paste.",
                "scienceNote": "Coating the dry almond particles in raw egg whites shields fat from destabilizing the Italian meringue whipped in the next step.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Italian Meringue: Heat castor sugar and water in a small pan to 244°F (118°C). When syrup hits 230°F, begin whipping the remaining 55g egg whites on medium speed to soft peaks. Once syrup reaches 244°F, stream it slowly down inside of the mixer bowl while beating on high speed until glossy, stiff, and cooled to 110°F (43°C).",
                "sensoryCue": "Blindingly shiny, dense meringue with stiff 'bird's beak' (bec d'oiseau) tip.",
                "scienceNote": "The 244°F sugar syrup cooks the ovalbumin proteins, producing a remarkably stable micro-bubble foam far less prone to overmixing than French meringue.",
                "timerMins": 10
            },
            {
                "stepNum": 3,
                "text": "Macaronage: Fold 1/3 of the Italian meringue into the almond paste to lighten it. Add remaining meringue and perform macaronage: scrape bottom, fold up and over, and flatten batter against sides of bowl with spatula. Continue until batter flows off spatula in an unbroken ribbon that slowly re-incorporates into itself over 20-25 seconds (lava stage).",
                "sensoryCue": "Glossy molten magma consistency; ribbons flatten smooth after 25 seconds.",
                "scienceNote": "Macaronage intentionally deflates a calculated percentage of air bubbles. Under-macaronage leaves peaked nipples; over-macaronage creates flat puddles without feet.",
                "timerMins": 6
            },
            {
                "stepNum": 4,
                "text": "Pipe 3.5cm (1.4-inch) circles onto Silpat mats holding piping bag perpendicular at 90°. Rap baking sheets firmly onto counter 4 times to release trapped air bubbles; pop any stubborn surface bubbles with a toothpick. Let rest uncovered at room temp for 25-35 minutes until a dull, dry, non-sticky skin forms on touch.",
                "sensoryCue": "A clean finger touched gently to shell surface picks up zero moisture.",
                "scienceNote": "The dry skin forces steam to escape horizontally around the bottom perimeter during baking, producing the signature ruffled 'pied' (feet).",
                "timerMins": 30
            },
            {
                "stepNum": 5,
                "text": "Bake on doubled sheet pans at 300°F (150°C) for 14-16 minutes. Cool completely on mats before peeling shells away. Pipe 66% dark chocolate ganache between matched shells. Transfer assembled macarons to an airtight container and mature in refrigerator for 24-48 hours before eating.",
                "sensoryCue": "Shells peel cleanly off mat; ruffled feet 3mm tall; interior completely full without hollow gaps.",
                "scienceNote": "24-48 hour maturation allows ganache moisture to migrate into the interior almond crumb, creating the iconic chewy center inside a brittle shell.",
                "timerMins": 1440
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted almond marzipan, bittersweet dark chocolate, caramelized sugar",
            "texture": "Crisp paper-delicate shell crack giving way instantly to dense, chewy, melt-in-mouth ganache core",
            "finish": "Persistent 66% cacao richness balanced by sweet almond finish"
        },
        "scienceNotes": "The Italian meringue method provides far greater batch-to-batch consistency than the French method because hot sugar syrup denatures and sets the egg white protein matrix before baking. The double baking pan protects delicate bottom bases from scorch.",
        "troubleshooting": {
            "No feet formed / cracked tops": "Batter did not rest long enough to form a dry skin, or oven temperature was too high.",
            "Hollow shells": "Meringue was overwhipped or oven had uneven airflow; ensure oven vents steam properly.",
            "Lopsided shells": "Piping bag was tilted at an angle instead of strict 90° vertical, or oven convection fan was too strong."
        },
        "substitutions": [
            {"ingredient": "Almond Flour", "substitute": "Pistachio Flour or Hazelnut Flour (extra fine)", "ratio": "1:1 by weight"},
            {"ingredient": "Dark Chocolate Ganache", "substitute": "Passionfruit White Chocolate Ganache or Salted Butter Caramel", "ratio": "1:1"}
        ],
        "flavorPairings": ["Darjeeling First Flush Tea", "Champagne Rosé", "Espresso", "Cognac"],
        "advancedTechnique": "Dusting raw piped shells with freeze-dried raspberry powder or gold luster dust through a stencil before baking.",
        "storageAndReheating": "Must mature 24h in fridge before eating! Keep refrigerated up to 7 days, or freeze airtight up to 3 months.",
        "nutritionEstimates": {"calories": 140, "protein": 3, "carbs": 18, "fat": 7},
        "relatedRecipes": ["rec-opera-cake", "rec-madeleines-commercy", "rec-paris-brest"],
        "relatedTechniques": ["Italian meringue sugar calibration", "Macaronage lava ribbon stage", "Maturation moisture osmosis"]
    },
    {
        "id": "rec-profiteroles",
        "title": "Profiteroles au Chocolat Noir & Glace Vanille (Warm Ganache Pour)",
        "cuisine": "French / Classical Bistro",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 25,
        "totalMins": 55,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "summary": "The Parisian brasserie icon: crisp, golden choux pastry puffs hollowed and filled à la minute with artisanal Madagascar vanilla bean ice cream, draped in warm, glossy bittersweet 70% dark chocolate sauce and toasted sliced almonds.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Contrast of crisp warm pastry, freezing vanilla cream, and cascading hot bittersweet chocolate sauce",
        "ingredients": [
            {"name": "Whole Milk", "qty": 60, "unit": "ml", "prep": "cold", "dept": "Dairy & Fats"},
            {"name": "Water", "qty": 60, "unit": "ml", "prep": "filtered", "dept": "Pantry"},
            {"name": "Unsalted European Butter", "qty": 55, "unit": "g", "prep": "cubed", "dept": "Dairy & Fats"},
            {"name": "Granulated Sugar", "qty": 5, "unit": "g", "prep": "for dough color", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 2, "unit": "g", "prep": "fine pinch", "dept": "Baking & Pantry"},
            {"name": "Bread Flour (High Protein)", "qty": 70, "unit": "g", "prep": "sifted (bread flour ensures hollow puff)", "dept": "Baking & Pantry"},
            {"name": "Large Eggs", "qty": 2, "unit": "whole", "prep": "beaten (approx 100-110g)", "dept": "Dairy & Fats"},
            {"name": "Artisanal Madagascar Vanilla Bean Ice Cream", "qty": 500, "unit": "g", "prep": "firm scoops", "dept": "Dairy & Fats"},
            {"name": "Valrhona Guanaja 70% Chocolate", "qty": 150, "unit": "g", "prep": "finely chopped", "dept": "Baking & Pantry"},
            {"name": "Heavy Cream (36% fat)", "qty": 150, "unit": "ml", "prep": "for warm sauce", "dept": "Dairy & Fats"},
            {"name": "Toasted Sliced Almonds", "qty": 30, "unit": "g", "prep": "golden roasted", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Piping Bag with 12mm Round Tip", "type": "Pâtisserie Tool"},
            {"name": "Heavy Baking Sheet with Silpat", "type": "Bakeware"},
            {"name": "Small Copper Saucepan for Ganache", "type": "Cookware"},
            {"name": "Serrated Paring Knife", "type": "Cutlery"}
        ],
        "miseEnPlace": [
            "Preheat oven to 400°F (200°C).",
            "Prepare choux panades by boiling milk, water, butter, sugar, and salt.",
            "Pre-scoop 18 small perfect spheres of vanilla ice cream onto a parchment tray and hold in deep freeze."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Choux Panade: Bring milk, water, butter, sugar, and salt to a rolling boil in a heavy saucepan. Dump in all flour at once. Stir vigorously with a wooden spoon over medium heat for 2 full minutes until the dough forms a smooth mass and leaves a thin starch film on bottom of pan.",
                "sensoryCue": "Dough pulls away cleanly from pan sides; thin white haze lines pan bottom.",
                "scienceNote": "Cooking the panade gelatinizes wheat starches (amylose and amylopectin) allowing them to absorb maximum water, which converts to steam in the oven to expand the hollow cavern.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Transfer hot panade to a stand mixer bowl (or cool 3 mins by hand). Beat on low 1 minute to release steam. Slowly add beaten eggs in 4 additions, beating until each is absorbed. Batter is ready when it falls off spatula in a glossy V-shaped hanging ribbon.",
                "sensoryCue": "Shiny, satiny dough that forms a smooth hanging triangle from spatula tip.",
                "scienceNote": "Adding eggs too quickly breaks the emulsion. Egg albumin sets the outer shell structure while yolk lecithin stabilizes trapped water.",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Pipe 18 uniform 3.5cm mounds onto Silpat-lined sheet. Dampen finger with water and flatten any pointed tips. Bake at 400°F (200°C) for 15 minutes without opening oven door; reduce to 350°F (175°C) and bake 10 more minutes until deeply golden and bone-dry. Poke small steam hole in base of each puff with a skewer and cool on wire rack.",
                "sensoryCue": "Lightweight, golden-amber hollow spheres with hollow resonance when tapped.",
                "scienceNote": "Never open the oven door during the first 15 minutes; sudden temperature drop condenses steam before egg proteins set, causing catastrophic puff collapse.",
                "timerMins": 25
            },
            {
                "stepNum": 4,
                "text": "Prepare Warm Chocolate Sauce: Scald heavy cream with a pinch of sea salt. Pour over chopped 70% chocolate in a bowl. Let sit 1 minute, then stir from center outward until velvety, glossy, and fluid. Keep warm at 115-120°F (46°C).",
                "sensoryCue": "Deep glossy dark chocolate sauce with zero air bubbles.",
                "scienceNote": "Maintaining sauce temperature at 115°F ensures smooth cascading viscosity without melting the ice cream immediately upon table delivery.",
                "timerMins": 5
            },
            {
                "stepNum": 5,
                "text": "Assembly (à la minute): Slice top third off each choux puff with a serrated knife. Place a frozen scoop of vanilla bean ice cream inside bottom cavity. Replace pastry cap. Arrange 3 filled profiteroles per chilled coupe or plate. Cascade hot chocolate sauce generously over tops at tableside; scatter toasted almonds.",
                "sensoryCue": "Dramatic tableside pour; steam from hot chocolate rising against frozen ice cream.",
                "scienceNote": "Dynamic contrast: sensory receptors detect concurrent hot chocolate (115°F), room-temp crisp choux (70°F), and freezing ice cream (10°F).",
                "timerMins": 3
            }
        ],
        "sensoryIndicators": {
            "aroma": "Warm dark cocoa, toasted butter pastry, chilled vanilla bean cream, roasted almonds",
            "texture": "Crisp dry pastry crunch, freezing silky ice cream melt, warm velvety ganache blanket",
            "finish": "Classic Parisian balance of bitter dark cacao and pure sweet cream"
        },
        "scienceNotes": "Profiteroles showcase temperature and moisture contrast. The hollow choux structure acts as an insulating chamber: its low thermal conductivity keeps the ice cream cold while supporting the warm chocolate drape.",
        "troubleshooting": {
            "Puffs collapse into flat disks": "Oven door was opened too early, or puffs were removed before moisture baked out of walls.",
            "Puffs are dense inside, not hollow": "Panade was not cooked long enough on stovetop, or too much egg was incorporated.",
            "Chocolate sauce splits or seizes": "Cream boiled too violently or water dripped into melting chocolate."
        },
        "substitutions": [
            {"ingredient": "Vanilla Ice Cream", "substitute": "Pistachio Gelato, Hazelnut Gelato, or Crème Diplomat", "ratio": "1:1"},
            {"ingredient": "70% Dark Chocolate", "substitute": "Gianduja Chocolate (hazelnut milk chocolate)", "ratio": "1:1 for sweeter profile"}
        ],
        "flavorPairings": ["Espresso", "Cognac VSOP", "Amaretto di Saronno", "Fresh Raspberries"],
        "advancedTechnique": "Craquelin topping: topping choux mounds with a thin disc of brown sugar-butter dough before baking for crunchy crackled surface.",
        "storageAndReheating": "Choux puffs can be baked ahead and stored airtight for 2 days; re-crisp at 350°F for 4 mins before filling. Must assemble immediately before serving.",
        "nutritionEstimates": {"calories": 420, "protein": 7, "carbs": 38, "fat": 26},
        "relatedRecipes": ["rec-eclairs-chocolat", "rec-paris-brest", "rec-chocolate-lava"],
        "relatedTechniques": ["Choux panade starch gelatinization", "Steam cavern expansion", "Dynamic temperature plating"]
    },
    {
        "id": "rec-financiers-amandes",
        "title": "Financiers aux Amandes et Beurre Noisette (Golden Almond Tea Cakes)",
        "cuisine": "French / Classical Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 15,
        "cookMins": 14,
        "totalMins": 29,
        "yieldServings": 12,
        "heroImage": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "summary": "The miniature gold bars of French baking. Created near the Paris Stock Exchange in the late 19th century: tender, moist almond flour tea cakes infused with deeply caramelized hazelnut-browned butter (beurre noisette) and egg whites.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Deeply aromatic nutty browned butter, moist chewy almond crumb, crisp caramelized perimeter",
        "ingredients": [
            {"name": "Unsalted European Butter", "qty": 130, "unit": "g", "prep": "browned down to approx 100g net hazelnut fat", "dept": "Dairy & Fats"},
            {"name": "Superfine Blanched Almond Flour", "qty": 60, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Icing / Powdered Sugar", "qty": 120, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Pastry Flour", "qty": 45, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Egg Whites", "qty": 3, "unit": "whole", "prep": "approx 100g, room temp, unbeaten", "dept": "Dairy & Fats"},
            {"name": "Pure Vanilla Bean Paste", "qty": 5, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Fine Sea Salt", "qty": 2, "unit": "g", "prep": "fine pinch", "dept": "Baking & Pantry"},
            {"name": "Flaked Almonds", "qty": 20, "unit": "g", "prep": "for top garniture", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Traditional Rectangular Financier Mold (or mini muffin tin)", "type": "Bakeware"},
            {"name": "Small Light-Bottom Saucepan", "type": "Cookware"},
            {"name": "Fine Mesh Sieve", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Brown butter until foaming subsides and milk solids turn deep chestnut brown with hazelnut aroma; strain through fine sieve and cool to lukewarm (110°F).",
            "Preheat oven to 390°F (200°C).",
            "Butter rectangular financier molds thoroughly with melted butter and dust with flour (or use nonstick silicone)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Beurre Noisette: Melt butter in small saucepan over medium heat. Whisk as it crackles and foams. Watch as foam subsides and toasted golden-brown specks collect at bottom of pan with intense roasted hazelnut aroma. Immediately pour into a clean bowl to stop cooking.",
                "sensoryCue": "Deep amber hue with nutty, toasty perfume.",
                "scienceNote": "Maillard reaction occurs between milk lactose sugars and milk proteins at 265-285°F, synthesizing aromatic lactones, pyrazines, and furans.",
                "timerMins": 6
            },
            {
                "stepNum": 2,
                "text": "In a medium bowl, whisk together sifted almond flour, powdered sugar, flour, and fine salt. Add unbeaten egg whites and vanilla paste. Whisk gently just until a smooth batter forms (do not whip or incorporate air).",
                "sensoryCue": "Smooth, pale ivory batter.",
                "scienceNote": "Financiers rely on dense moisture rather than leavening; keeping egg whites unwhipped prevents cake from doming and cracking.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Gradually pour the lukewarm browned butter into batter in a steady stream while whisking gently until completely emulsified and glossy.",
                "sensoryCue": "Liquid gold emulsion with golden specks.",
                "scienceNote": "Lukewarm butter (110°F) emulsifies seamlessly with egg whites without cooking them or separating.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Divide batter evenly among prepared financier molds filling 80% full. Scatter a few flaked almonds across tops. Rest batter in molds for 10 minutes at room temp.",
                "sensoryCue": "Level batter with glistening almond flakes.",
                "scienceNote": "Resting allows starch granules to hydrate, yielding tender crumb.",
                "timerMins": 10
            },
            {
                "stepNum": 5,
                "text": "Bake at 390°F (200°C) for 12 to 14 minutes until edges are crisp and golden-bronze and centers spring back when lightly touched with fingertip. Cool in molds 5 minutes, then turn out onto a wire rack to cool completely.",
                "sensoryCue": "Crisp golden rectangular bars with golden edges and tender springy center.",
                "scienceNote": "High heat creates crisp caramelized outer edges while high fat content retains moist interior.",
                "timerMins": 13
            }
        ],
        "sensoryIndicators": {
            "aroma": "Nutty browned butter, toasted sweet almond, floral vanilla, warm caramel",
            "texture": "Crisp, crackly outer edge yielding to moist, chewy, buttery almond crumb",
            "finish": "Rich buttery finish with clean roasted nut aftertaste"
        },
        "scienceNotes": "Unlike madeleines which whip whole eggs to generate a towering hump, financiers intentionally use unwhipped egg whites. The egg white proteins coagulate into a firm yet moist matrix that suspends the high concentration of browned butter fat.",
        "troubleshooting": {
            "Greasy or heavy cake": "Brown butter was too hot when added, or batter was under-mixed.",
            "Cakes stick to pan": "Molds were insufficiently buttered; use softened butter brushed in upward strokes and chilled.",
            "Financiers are pale and soft": "Oven temperature was too low; high heat (390°F) is required for caramelized crust."
        },
        "substitutions": [
            {"ingredient": "Almond Flour", "substitute": "Pistachio Flour or Hazelnut Flour", "ratio": "1:1 for stunning color/flavor"},
            {"ingredient": "Rectangular Molds", "substitute": "Standard Mini Muffin Pan", "ratio": "Bake 10-12 minutes"}
        ],
        "flavorPairings": ["Espresso", "Green Sencha Tea", "Fresh Blackberries", "Calvados"],
        "advancedTechnique": "Studding each unbaked financier with two fresh raspberries for tart acid bursts against the rich butter crumb.",
        "storageAndReheating": "Store airtight at room temperature for up to 4 days. Crisp in 350°F oven for 2 minutes before enjoying.",
        "nutritionEstimates": {"calories": 160, "protein": 3, "carbs": 14, "fat": 11},
        "relatedRecipes": ["rec-madeleines-commercy", "rec-caneles-bordeaux", "rec-french-macarons"],
        "relatedTechniques": ["Beurre noisette caramelization", "Unwhipped albumin emulsion", "High-heat perimeter crusting"]
    },
    {
        "id": "rec-grand-marnier-souffle",
        "title": "Soufflé Chaud au Grand Marnier (Warm Citrus Cloud with Powdered Sugar)",
        "cuisine": "French / Classical Haute Cuisine",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Advanced",
        "prepMins": 25,
        "cookMins": 14,
        "totalMins": 39,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ethereal pinnacle of Parisian restaurant dining. A towering hot dessert soufflé infused with orange zest and Grand Marnier liqueur, rising 2 inches straight above the ramekin rim with a golden top and molten citrus cream core.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Airy, cloud-like lightness with fragrant citrus orange liqueur, warm vanilla, and powdered sugar melt",
        "ingredients": [
            {"name": "Whole Milk", "qty": 180, "unit": "ml", "prep": "farm fresh", "dept": "Dairy & Fats"},
            {"name": "Grand Marnier Cordon Rouge Liqueur", "qty": 45, "unit": "ml", "prep": "cognac & bitter orange", "dept": "Pantry"},
            {"name": "Fresh Navel Orange Zest", "qty": 5, "unit": "g", "prep": "finely microplaned", "dept": "Produce"},
            {"name": "Egg Yolks", "qty": 3, "unit": "whole", "prep": "approx 55g", "dept": "Dairy & Fats"},
            {"name": "Egg Whites", "qty": 4, "unit": "whole", "prep": "approx 140g, room temperature", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 65, "unit": "g", "prep": "divided: 35g base, 30g meringue", "dept": "Baking & Pantry"},
            {"name": "Cornstarch (Maizena)", "qty": 20, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Flour", "qty": 10, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Softened Butter & Granulated Sugar", "qty": 30, "unit": "g", "prep": "for ramekin preparation", "dept": "Baking & Pantry"},
            {"name": "Powdered Sugar", "qty": 15, "unit": "g", "prep": "for tableside dusting", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Four 6-oz Straight-Sided Ceramic Soufflé Ramekins", "type": "Bakeware"},
            {"name": "Pastry Brush", "type": "Small Tool"},
            {"name": "Copper or Stainless Steel Whisking Bowl", "type": "Cookware"},
            {"name": "Baking Sheet", "type": "Bakeware"}
        ],
        "miseEnPlace": [
            "Preheat oven to 390°F (200°C) with baking sheet on center rack.",
            "Ramekin Prep: Brush softened butter in vertical upward strokes along interior walls. Chill 5 mins, apply second vertical butter layer, then coat with granulated sugar, tapping out excess.",
            "Separate eggs cleanly; egg whites must have zero traces of yolk or fat."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Orange Pastry Cream Base: Scald milk with orange zest. In a bowl, whisk yolks, 35g castor sugar, cornstarch, and flour until pale. Temper hot milk into yolks, return to pan, and whisk constantly over medium heat until it bubbles and thickens into a dense pastry cream (2 mins). Remove from heat, whisk in Grand Marnier liqueur. Transfer to bowl and cool to lukewarm (100°F).",
                "sensoryCue": "Thick, fragrant orange pastry cream with glossy sheen.",
                "scienceNote": "Cornstarch and flour starch granules gelatinize, creating a stabilized matrix that suspends liqueur and prevents water weeping.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Whip French Meringue: Whip room temperature egg whites on medium speed until foamy. Gradually rain in 30g castor sugar, increasing speed to medium-high. Whip until glossy medium-firm peaks form with gentle curled tip (do not whip to dry stiff peaks).",
                "sensoryCue": "Gleaming white cloud; tip droops slightly when whisk is inverted.",
                "scienceNote": "Medium-firm peaks retain elasticity; overwhipping stretches egg albumin protein bonds too thin, causing premature collapse and ragged expansion.",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Fold: Whisk 1/4 of the meringue aggressively into the lukewarm pastry cream base to lighten its density. Then gently fold in the remaining meringue in two additions with a flexible silicone spatula, cutting down the center, sweeping along bottom, and folding over.",
                "sensoryCue": "Fluffy, uniform, pale apricot-tinted aerated mousse.",
                "scienceNote": "Lightening the base first prevents the heavy pastry cream from deflating delicate air cells in the second fold.",
                "timerMins": 3
            },
            {
                "stepNum": 4,
                "text": "Fill & Crown: Divide batter among the 4 prepared ramekins, filling slightly above the rim. Level flat across the top with a straight metal spatula. Run thumb around inner top edge of each ramekin to create a 2mm moat/gap between batter and rim.",
                "sensoryCue": "Immaculate flat surface with clean recessed perimeter groove.",
                "scienceNote": "The thumb groove decouples the rising soufflé from the rim, preventing it from catching and tilting, ensuring a straight vertical rise.",
                "timerMins": 3
            },
            {
                "stepNum": 5,
                "text": "Place ramekins on the preheated baking sheet. Bake at 390°F (200°C) for 13 to 14 minutes without opening oven door. Soufflés will rise 1.5 to 2 inches straight above the rim with golden crowns. Immediately dust with powdered sugar and serve within 90 seconds.",
                "sensoryCue": "Towering vertical cylinder, trembling gently, fragrant citrus aroma.",
                "scienceNote": "Thermal expansion of trapped air bubbles combined with water turning to steam lifts the elastic coagulating egg protein walls.",
                "timerMins": 14
            }
        ],
        "sensoryIndicators": {
            "aroma": "Sweet orange blossom, Grand Marnier cognac, caramelized sugar, vanilla",
            "texture": "Ethereal, melting cloud texture with molten warm citrus cream center",
            "finish": "Warm cognac liqueur hum and bright citrus oil acidity"
        },
        "scienceNotes": "Charles's Law dictates that gas volume expands proportionally with temperature. Millions of micro-bubbles trapped in the meringue expand rapidly as they reach 160-180°F, while egg ovalbumin proteins denature and solidify around them, creating a self-supporting edible foam skyscraper.",
        "troubleshooting": {
            "Soufflé rises lopsided or tilts": "Ramekin was not buttered in vertical upward strokes, or thumb groove was skipped.",
            "Soufflé deflates instantly upon leaving oven": "Normal after 3-4 minutes, but if it collapses within 30 seconds it was underbaked in center.",
            "Dense rubbery texture": "Meringue was over-folded or over-whipped to dry stiff peaks."
        },
        "substitutions": [
            {"ingredient": "Grand Marnier", "substitute": "Cointreau, Triple Sec, or Dark Rum", "ratio": "1:1"},
            {"ingredient": "Orange Zest", "substitute": "Meyer Lemon Zest or Passionfruit Puree", "ratio": "1:1"}
        ],
        "flavorPairings": ["Crème Anglaise Pour", "Dark Espresso", "Champagne Demi-Sec", "Candied Orange Peel"],
        "advancedTechnique": "Cracking center tableside with two spoons and pouring warm vanilla bean crème anglaise directly into the molten core.",
        "storageAndReheating": "Must be baked and served immediately. Unbaked ramekins can be held in refrigerator for up to 30 minutes before baking.",
        "nutritionEstimates": {"calories": 230, "protein": 6, "carbs": 28, "fat": 8},
        "relatedRecipes": ["rec-souffle-chocolat", "rec-creme-brulee", "rec-creme-caramel"],
        "relatedTechniques": ["Vertical upward ramekin buttering", "French meringue elasticity control", "Thumb perimeter groove release"]
    }
]

print(f"Loaded {len(PART_2_RECIPES)} recipes in PART_2_RECIPES.")
