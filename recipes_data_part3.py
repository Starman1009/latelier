# recipes_data_part3.py
# High-precision culinary master recipes 11-20

PART_3_RECIPES = [
    {
        "id": "rec-lemon-curd-bars",
        "title": "French Meyer Lemon Curd Shortbread Bars (Tartelette Bars)",
        "cuisine": "French / Classical Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 20,
        "cookMins": 35,
        "totalMins": 55,
        "yieldServings": 16,
        "heroImage": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ultimate bakery bar: rich, buttery, melt-in-mouth sablé shortbread crust par-baked to golden perfection, topped with a thick, satiny, ultra-tart Meyer lemon curd baked gently until custardy and dusted with snowy confectioners' sugar.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Vibrant electrifying citrus acidity balanced by buttery crumbly shortbread base",
        "ingredients": [
            {"name": "Unsalted European Butter (82% fat)", "qty": 225, "unit": "g", "prep": "softened at room temp", "dept": "Dairy & Fats"},
            {"name": "Powdered / Icing Sugar", "qty": 80, "unit": "g", "prep": "sifted for crust", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Pastry Flour", "qty": 260, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 3, "unit": "g", "prep": "divided: 2g crust, 1g curd", "dept": "Baking & Pantry"},
            {"name": "Fresh Meyer Lemons (Juice & Zest)", "qty": 180, "unit": "ml", "prep": "freshly squeezed (approx 4-5 lemons) + 10g zest", "dept": "Produce"},
            {"name": "Granulated Castor Sugar", "qty": 300, "unit": "g", "prep": "fine crystals for curd", "dept": "Baking & Pantry"},
            {"name": "Large Eggs", "qty": 6, "unit": "whole", "prep": "room temperature (approx 300g)", "dept": "Dairy & Fats"},
            {"name": "All-Purpose Flour", "qty": 45, "unit": "g", "prep": "sifted (stabilizer for curd)", "dept": "Baking & Pantry"},
            {"name": "Powdered Sugar", "qty": 20, "unit": "g", "prep": "for finishing dust", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "9x13-inch Rectangular Metal Baking Pan", "type": "Bakeware"},
            {"name": "Parchment Paper with Overhang Slings", "type": "Baking Supply"},
            {"name": "Microplane Zester", "type": "Cutlery"},
            {"name": "Fine Mesh Sieve", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Line a 9x13 metal pan with parchment paper, leaving 2-inch overhangs on all sides; butter lightly.",
            "Preheat oven to 350°F (175°C).",
            "Zest Meyer lemons before squeezing juice; strain juice to remove seeds and pulp."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Sablé Shortbread Crust: In a bowl, cream softened butter and sifted powdered sugar for 2 minutes until pale and creamy. Add flour and sea salt; mix on low speed just until dough comes together into moist clumps. Press evenly into bottom of prepared pan using flat bottom of measuring cup.",
                "sensoryCue": "Even, flat, buttery dough base filling pan corners.",
                "scienceNote": "Powdered sugar contains finely pulverized starch and dissolves immediately, creating a delicate melt-in-mouth crumb (sablé) rather than a tough cracker.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Par-bake crust at 350°F (175°C) for 20 minutes until edges are light golden brown and surface is dry to the touch.",
                "sensoryCue": "Buttery, toasted biscuit aroma and light golden edges.",
                "scienceNote": "Par-baking sets crust starch network so hot lemon curd batter cannot penetrate and create a soggy base.",
                "timerMins": 20
            },
            {
                "stepNum": 3,
                "text": "Make Meyer Lemon Curd: Rub fresh lemon zest into granulated sugar with fingertips for 1 minute to express citrus essential oils. Whisk in whole eggs until smooth. Whisk in sifted 45g flour and 1g salt until no lumps remain. Slowly whisk in fresh lemon juice.",
                "sensoryCue": "Intense fragrant citrus oil aroma; smooth golden liquid.",
                "scienceNote": "Abrading lemon zest with sucrose crystals bursts microscopic oil sacs, extracting terpene aromatics (limonene and citral) directly into the sugar matrix.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "Pour curd mixture directly onto the warm par-baked crust. Lower oven temperature to 325°F (165°C). Bake for 20 to 22 minutes until curd is set around edges and center has just a slight jiggle (probe reads 170°F / 77°C).",
                "sensoryCue": "Matte yellow surface with slight gentle wobble in center.",
                "scienceNote": "Baking at lower 325°F prevents egg proteins from scrambling or forming air blisters, producing a glass-smooth custard.",
                "timerMins": 22
            },
            {
                "stepNum": 5,
                "text": "Cool completely in pan on wire rack for 1 hour, then refrigerate for at least 2 hours until firm. Use parchment sling to lift slab out onto cutting board. Dust heavily with sifted powdered sugar. Slice with a hot clean chef's knife into 16 bars.",
                "sensoryCue": "Crisp straight cuts; glistening bright yellow curd against snow-white powdered sugar.",
                "scienceNote": "Chilling solidifies butterfat in the crust and gelatinizes egg proteins in the curd for clean, non-smearing edges.",
                "timerMins": 120
            }
        ],
        "sensoryIndicators": {
            "aroma": "Fresh zesty lemon oil, rich caramelized butter shortbread, powdered sugar",
            "texture": "Crisp, crumbly buttery base meeting silky, luscious, melt-in-mouth citrus curd",
            "finish": "Electrifying lemon tartness that refreshes the palate, rounded by sweet butter"
        },
        "scienceNotes": "Meyer lemons have higher sugar content and lower acidity (pH ~2.5-3.0) than standard Eureka lemons, with floral, herbal notes reminiscent of mandarin orange and thyme. The flour in the curd gelatinizes at 165°F, preventing egg syneresis even with high lemon acid concentrations.",
        "troubleshooting": {
            "Curd separates or forms air bubbles": "Oven was too hot; curd boiled and scrambled. Bake strictly at 325°F.",
            "Soggy crust bottom": "Crust was under-baked during par-bake, or curd was poured onto cold crust.",
            "Powdered sugar melts into puddles": "Sugar was dusted while bars were still warm; dust only immediately before serving."
        },
        "substitutions": [
            {"ingredient": "Meyer Lemons", "substitute": "Standard Eureka Lemons mixed with 20% Fresh Orange Juice", "ratio": "1:1 total liquid"},
            {"ingredient": "Meyer Lemon Juice", "substitute": "Fresh Key Lime Juice or Passionfruit Pulp", "ratio": "1:1 for tropical twist"}
        ],
        "flavorPairings": ["Earl Grey Tea", "Iced Espresso", "Fresh Raspberries", "Elderflower Spritz"],
        "advancedTechnique": "Infusing lemon juice with fresh lemon verbena leaves before whisking into curd.",
        "storageAndReheating": "Store bars in airtight container in refrigerator up to 5 days. Re-dust with powdered sugar just before serving.",
        "nutritionEstimates": {"calories": 280, "protein": 4, "carbs": 38, "fat": 13},
        "relatedRecipes": ["rec-shattered-lemon-tart", "rec-key-lime-pie", "rec-madeleines-commercy"],
        "relatedTechniques": ["Zest sucrose abrasion", "Par-baked sablé sealing", "Low-temperature curd coagulation"]
    },
    {
        "id": "rec-bread-pudding-bourbon",
        "title": "New Orleans Brioche Bread Pudding with Bourbon Crème Anglaise",
        "cuisine": "American / Creole Classical",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 25,
        "cookMins": 45,
        "totalMins": 70,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=1200&q=80",
        "summary": "The crown jewel of French Quarter comfort: cubes of rich, buttery day-old brioche soaked in vanilla-cinnamon-nutmeg custard with plumped bourbon raisins, baked until puffed and golden with crisp caramelized edges, drowned in warm Kentucky bourbon hard sauce.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Warm, custardy interior, crisp caramelized top crust, heady oaky bourbon and brown sugar richness",
        "ingredients": [
            {"name": "Day-Old Artisanal Brioche Loaf", "qty": 450, "unit": "g", "prep": "cut into 1-inch cubes", "dept": "Bakery"},
            {"name": "Heavy Cream (36% fat)", "qty": 350, "unit": "ml", "prep": "fresh", "dept": "Dairy & Fats"},
            {"name": "Whole Milk", "qty": 250, "unit": "ml", "prep": "farm fresh", "dept": "Dairy & Fats"},
            {"name": "Large Eggs", "qty": 4, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Egg Yolks", "qty": 2, "unit": "whole", "prep": "room temp", "dept": "Dairy & Fats"},
            {"name": "Dark Brown Sugar", "qty": 150, "unit": "g", "prep": "packed", "dept": "Baking & Pantry"},
            {"name": "Granulated White Sugar", "qty": 50, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Kentucky Straight Bourbon Whiskey", "qty": 80, "unit": "ml", "prep": "divided: 30ml soaking, 50ml sauce", "dept": "Pantry"},
            {"name": "Golden Thompson Raisins", "qty": 90, "unit": "g", "prep": "plumped in warm bourbon", "dept": "Baking & Pantry"},
            {"name": "Ground Cinnamon & Fresh Grated Nutmeg", "qty": 6, "unit": "g", "prep": "freshly grated", "dept": "Spices & Botanicals"},
            {"name": "Pure Vanilla Bean Paste", "qty": 10, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Unsalted European Butter", "qty": 85, "unit": "g", "prep": "for bourbon sauce", "dept": "Dairy & Fats"},
            {"name": "Powdered Sugar", "qty": 100, "unit": "g", "prep": "for sauce emulsion", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "9x9-inch Ceramic or Cast Iron Baking Dish", "type": "Bakeware"},
            {"name": "Large Mixing Bowl", "type": "Cookware"},
            {"name": "Small Saucepan for Bourbon Sauce", "type": "Cookware"}
        ],
        "miseEnPlace": [
            "Cut brioche into 1-inch cubes; spread on baking sheet and toast at 300°F for 10 minutes to dry out (dry bread absorbs maximum custard).",
            "Macerate raisins in 30ml warm bourbon for 20 minutes.",
            "Butter baking dish generously with softened butter."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Whisk whole eggs, extra yolks, dark brown sugar, granulated sugar, vanilla paste, cinnamon, grated nutmeg, and fine salt in a large bowl until sugar dissolves. Whisk in heavy cream and whole milk until smooth and uniform.",
                "sensoryCue": "Fragrant spice-flecked custard batter with caramel tones.",
                "scienceNote": "High proportion of egg yolks and cream fat (approx 20% milkfat) prevents the bread pudding from turning spongy or rubbery.",
                "timerMins": 4
            },
            {
                "stepNum": 2,
                "text": "Add dried brioche cubes and plumped bourbon raisins (with soaking liquid) to the bowl. Gently press bread down into custard so every cube is submerged. Let stand undisturbed for 20 minutes at room temperature.",
                "sensoryCue": "Bread cubes drink up liquid, swelling into soft pillowy sponges.",
                "scienceNote": "Capillary action draws custard into the open crumb pores of dried bread; resting ensures center of bread cubes are fully saturated, avoiding dry pockets.",
                "timerMins": 20
            },
            {
                "stepNum": 3,
                "text": "Transfer soaked bread and all remaining custard into the buttered baking dish, gently arranging top cubes with peaks and edges sticking up (these will crisp into crunchy golden croutons). Dot top with 20g butter and sprinkle with coarse sugar.",
                "sensoryCue": "Irregular textured surface with glistening sugar crystals.",
                "scienceNote": "Exposed peaks undergo rapid surface dehydration and caramelization, creating contrast against the moist pudding beneath.",
                "timerMins": 3
            },
            {
                "stepNum": 4,
                "text": "Bake at 350°F (175°C) for 42 to 45 minutes until puffed like a soufflé, deeply bronzed, and a knife inserted in center emerges hot and clean (custard temp 175°F / 80°C).",
                "sensoryCue": "Towering puffed pudding with crackly caramelized peaks and rich bourbon spice aroma.",
                "scienceNote": "Egg proteins coagulate between 160-175°F, locking the custard and swollen brioche into a cohesive, trembling pudding.",
                "timerMins": 45
            },
            {
                "stepNum": 5,
                "text": "Make Warm Bourbon Hard Sauce: Melt 85g butter in saucepan over low heat. Whisk in powdered sugar and pinch of salt. Whisk in 50ml bourbon and 30ml heavy cream. Simmer gently 2 minutes until glossy and emulsified. Pour warm sauce over warm sliced pudding at service.",
                "sensoryCue": "Silky, golden amber sauce cascading over puffed brioche.",
                "scienceNote": "Alcohol volatile esters vaporize upon meeting hot pudding, delivering an intoxicating aromatic burst at the table.",
                "timerMins": 5
            }
        ],
        "sensoryIndicators": {
            "aroma": "Kentucky oak bourbon, brown sugar molasses, toasted brioche butter, grated nutmeg",
            "texture": "Crisp crunchy toasted peaks yielding to ultra-moist, creamy, melt-in-mouth custard",
            "finish": "Warming bourbon alcohol notes balanced by sweet dairy cream and raisins"
        },
        "scienceNotes": "Bread pudding relies on stale or toasted bread because fresh bread collapses into gluey paste when wet. Starch retrogradation in dried bread maintains cellular structure, allowing the egg custard to fill microscopic air voids without destroying the crumb architecture.",
        "troubleshooting": {
            "Soggy mushy center": "Too much custard for bread volume, or pudding was under-baked. Probe center to 175°F.",
            "Dry and chalky": "Bread was soaked insufficiently or over-baked past 185°F, causing egg curdling.",
            "Sauce breaks oily": "Sauce boiled too vigorously; keep heat low and whisk constantly."
        },
        "substitutions": [
            {"ingredient": "Brioche", "substitute": "Challah, Croissants, or Panettone", "ratio": "1:1 by weight"},
            {"ingredient": "Kentucky Bourbon", "substitute": "Dark Spiced Rum or Cognac", "ratio": "1:1"}
        ],
        "flavorPairings": ["Dark Chicory Coffee", "Vanilla Bean Gelato", "Pecan Pralines", "Rye Whiskey"],
        "advancedTechnique": "Flambéing the bourbon in a copper saucepan before whisking into the butter sauce for toasted caramelized notes.",
        "storageAndReheating": "Refrigerate up to 4 days covered. Reheat individual portions in 350°F oven for 8 minutes to restore crisp peaks.",
        "nutritionEstimates": {"calories": 460, "protein": 8, "carbs": 52, "fat": 24},
        "relatedRecipes": ["rec-bourbon-pecan-pie", "rec-brioche-french-toast", "rec-creme-caramel"],
        "relatedTechniques": ["Starch retrogradation absorption", "Custard coagulation monitoring", "Spirits volatile emulsification"]
    },
    {
        "id": "rec-peach-blackberry-cobbler",
        "title": "Cast-Iron Bourbon Peach & Blackberry Cobbler with Buttermilk Biscuits",
        "cuisine": "American / Southern Classical",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 25,
        "cookMins": 40,
        "totalMins": 65,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1568571780765-9276ac8b75a2?auto=format&fit=crop&w=1200&q=80",
        "summary": "Rustic summer perfection in a seasoned cast-iron skillet. Ripe peaches and wild plump blackberries tossed in brown sugar, bourbon, and lemon, topped with fluffy, golden-crusted cream buttermilk drop biscuits and raw turbinado sugar.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Bubbling sweet-tart fruit juices, fragrant bourbon and peach perfume, flaky tender buttermilk biscuits",
        "ingredients": [
            {"name": "Ripe Yellow Peaches", "qty": 900, "unit": "g", "prep": "sliced 1/2-inch thick (approx 6 peaches)", "dept": "Produce"},
            {"name": "Fresh Wild Blackberries", "qty": 250, "unit": "g", "prep": "rinsed and dried", "dept": "Produce"},
            {"name": "Dark Brown Sugar", "qty": 100, "unit": "g", "prep": "packed", "dept": "Baking & Pantry"},
            {"name": "Granulated Castor Sugar", "qty": 50, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Cornstarch (Maizena)", "qty": 25, "unit": "g", "prep": "for fruit thickening", "dept": "Baking & Pantry"},
            {"name": "Fresh Lemon Juice & Zest", "qty": 20, "unit": "ml", "prep": "for brightness", "dept": "Produce"},
            {"name": "Bourbon Whiskey", "qty": 30, "unit": "ml", "prep": "straight bourbon", "dept": "Pantry"},
            {"name": "Ground Cinnamon & Ginger", "qty": 4, "unit": "g", "prep": "ground fine", "dept": "Spices & Botanicals"},
            {"name": "All-Purpose Pastry Flour", "qty": 220, "unit": "g", "prep": "sifted for biscuits", "dept": "Baking & Pantry"},
            {"name": "Baking Powder", "qty": 10, "unit": "g", "prep": "aluminum-free", "dept": "Baking & Pantry"},
            {"name": "Cold Unsalted Butter", "qty": 100, "unit": "g", "prep": "cubed small and chilled", "dept": "Dairy & Fats"},
            {"name": "Cold Cultured Buttermilk", "qty": 180, "unit": "ml", "prep": "full-fat", "dept": "Dairy & Fats"},
            {"name": "Turbinado / Demerara Raw Sugar", "qty": 25, "unit": "g", "prep": "for crunchy biscuit topping", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "10 or 12-inch Seasoned Cast-Iron Skillet", "type": "Cookware"},
            {"name": "Pastry Cutter or Food Processor", "type": "Small Tool"},
            {"name": "Large Cookie Scoop (for drop biscuits)", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Preheat oven to 375°F (190°C).",
            "Slice peaches and toss with lemon juice, zest, brown sugar, castor sugar, cornstarch, bourbon, and spices in cast-iron skillet.",
            "Cut butter into flour and baking powder until pea-sized crumbs form; hold in freezer for 10 minutes."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Place cast-iron skillet with fruit mixture on stovetop over medium heat for 4 minutes, stirring gently until fruit juices begin to release and brown sugar melts into an aromatic syrup. Remove from heat; fold in fresh blackberries.",
                "sensoryCue": "Glossy crimson-amber fruit juices beginning to simmer; sweet bourbon peach aroma.",
                "scienceNote": "Pre-warming the fruit in the skillet jumpstarts starch gelatinization so fruit juices thicken simultaneously with biscuit baking, avoiding soggy biscuit bottoms.",
                "timerMins": 4
            },
            {
                "stepNum": 2,
                "text": "Make Buttermilk Biscuit Dough: Add cold cultured buttermilk to the chilled butter-flour mixture. Stir with a fork just until a shaggy, wet dough forms (do not knead or overwork).",
                "sensoryCue": "Tender, moist dough studded with visible butter shards.",
                "scienceNote": "Minimal mixing limits gluten formation, while butter pieces melt in the oven leaving steam pockets that puff the biscuits into flaky layers.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Drop 8 large mounds of biscuit dough over the hot fruit using a scoop, leaving small cobblestone gaps for fruit juices to bubble up. Brush biscuit tops lightly with buttermilk and sprinkle heavily with raw turbinado sugar.",
                "sensoryCue": "Chunky rustic dough mounds crowned with amber sugar crystals.",
                "scienceNote": "Turbinado sugar has high melting point (365°F), preserving crunchy glass-like texture on top of tender biscuits.",
                "timerMins": 3
            },
            {
                "stepNum": 4,
                "text": "Bake in cast-iron skillet at 375°F (190°C) for 38 to 42 minutes until biscuits are deep golden-bronze and fruit filling is bubbling aggressively throughout center (not just around edges).",
                "sensoryCue": "Violently bubbling magenta fruit syrup; rich aroma of toasted butter and peaches.",
                "scienceNote": "Cornstarch requires bubbling at 205°F to achieve complete gelatinization; if taken out before bubbling in the center, juices will remain runny upon cooling.",
                "timerMins": 40
            },
            {
                "stepNum": 5,
                "text": "Let rest for 15 minutes before serving so thickened fruit juices stabilize into luscious jammy consistency. Serve warm directly from skillet with generous scoops of vanilla bean ice cream.",
                "sensoryCue": "Melting ice cream rivers swirling into hot purple blackberry juices.",
                "scienceNote": "Resting allows retrograded starch to increase sauce viscosity while retaining warmth in heat-retaining cast iron.",
                "timerMins": 15
            }
        ],
        "sensoryIndicators": {
            "aroma": "Warm spiced peaches, tart bubbling blackberries, toasted buttermilk biscuit, bourbon",
            "texture": "Crunchy turbinado sugar crunch on fluffy tender biscuit; jammy warm fruit",
            "finish": "Bright fruit acidity cutting rich biscuit butter, lingering floral stone fruit finish"
        },
        "scienceNotes": "Seasoned cast-iron provides radiant thermal mass from below, cooking the underside of the drop biscuits through direct conduction so they never end up gummy or underdone.",
        "troubleshooting": {
            "Biscuits are gummy on bottom": "Fruit wasn't pre-warmed on stovetop, or cobbler was pulled before center bubbled.",
            "Filling is watery and runny": "Cornstarch was under-measured or filling didn't reach full 205°F boil.",
            "Biscuits browned too fast before cooking through": "Tent skillet loosely with aluminum foil for the final 15 minutes."
        },
        "substitutions": [
            {"ingredient": "Yellow Peaches", "substitute": "Nectarines, Plums, or Dark Sweet Cherries", "ratio": "1:1 by weight"},
            {"ingredient": "Cultured Buttermilk", "substitute": "Heavy Cream with 1 tsp lemon juice", "ratio": "1:1"}
        ],
        "flavorPairings": ["Bourbon Vanilla Gelato", "Fresh Mint Leaves", "Sweet Iced Tea", "Riesling Spätlese"],
        "advancedTechnique": "Infusing peach slices with bruised fresh lemon thyme sprigs before baking.",
        "storageAndReheating": "Cover loosely and keep at room temp 2 days or refrigerate 4 days. Re-warm in 350°F oven for 10 minutes.",
        "nutritionEstimates": {"calories": 380, "protein": 5, "carbs": 58, "fat": 15},
        "relatedRecipes": ["rec-apple-cardamom-crumble", "rec-bourbon-pecan-pie", "rec-tarte-tatin"],
        "relatedTechniques": ["Cast-iron thermal conduction", "Drop biscuit steam aeration", "Starch gelatinization boiling point"]
    },
    {
        "id": "rec-apple-cardamom-crumble",
        "title": "Honeycrisp Apple & Blackberry Crumble with Rolled Oats & Clotted Cream",
        "cuisine": "British / Classical Modern",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 20,
        "cookMins": 35,
        "totalMins": 55,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1568571780765-9276ac8b75a2?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ultimate autumn comfort dessert: crisp, tart Honeycrisp apples and wild blackberries spiced with green cardamom and cinnamon, buried beneath a thick blanket of buttery rolled oat, brown sugar, and toasted pecan crumble, served with thick clotted cream.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Warm spiced baked apples, tart blackberry bursts, deeply crunchy oat streusel, silky clotted cream",
        "ingredients": [
            {"name": "Honeycrisp or Bramley Apples", "qty": 800, "unit": "g", "prep": "peeled, cored, and sliced into 1/2-inch wedges", "dept": "Produce"},
            {"name": "Wild Blackberries", "qty": 150, "unit": "g", "prep": "fresh or frozen", "dept": "Produce"},
            {"name": "Dark Brown Sugar", "qty": 120, "unit": "g", "prep": "divided: 40g fruit, 80g crumble", "dept": "Baking & Pantry"},
            {"name": "Fresh Lemon Juice", "qty": 15, "unit": "ml", "prep": "freshly squeezed", "dept": "Produce"},
            {"name": "Ground Green Cardamom & Cinnamon", "qty": 5, "unit": "g", "prep": "freshly ground", "dept": "Spices & Botanicals"},
            {"name": "All-Purpose Flour", "qty": 120, "unit": "g", "prep": "sifted for crumble", "dept": "Baking & Pantry"},
            {"name": "Old Fashioned Rolled Oats", "qty": 80, "unit": "g", "prep": "whole grain", "dept": "Baking & Pantry"},
            {"name": "Pecan Pieces", "qty": 60, "unit": "g", "prep": "toasted and chopped", "dept": "Baking & Pantry"},
            {"name": "Cold European Butter (82% fat)", "qty": 115, "unit": "g", "prep": "cubed small and chilled", "dept": "Dairy & Fats"},
            {"name": "Flaky Sea Salt", "qty": 3, "unit": "g", "prep": "in crumble topping", "dept": "Baking & Pantry"},
            {"name": "Cornstarch", "qty": 15, "unit": "g", "prep": "for fruit thickening", "dept": "Baking & Pantry"},
            {"name": "English Clotted Cream", "qty": 150, "unit": "g", "prep": "thick dollops for serving", "dept": "Dairy & Fats"}
        ],
        "equipment": [
            {"name": "9-inch Ceramic or Stoneware Pie Dish", "type": "Bakeware"},
            {"name": "Large Mixing Bowl", "type": "Cookware"},
            {"name": "Pastry Blender or Fingers", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Preheat oven to 375°F (190°C).",
            "Toss sliced apples with lemon juice, 40g brown sugar, cornstarch, cinnamon, and half the ground cardamom.",
            "Butter the ceramic pie dish."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Transfer spiced apple slices into the buttered dish and scatter blackberries evenly throughout the apples.",
                "sensoryCue": "Vibrant purple blackberries nestled between pale gold apple slices.",
                "scienceNote": "Apple pectin and lemon citric acid interact with cornstarch to create a clear, glossy glaze as juices express during baking.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Make Cardamom Oat Streusel: In a bowl, combine flour, rolled oats, pecans, 80g dark brown sugar, remaining cardamom, and flaky sea salt. Rub the cold cubed butter into dry ingredients with fingertips until clumpy streusel clusters form ranging from pea to walnut size.",
                "sensoryCue": "Uneven clusters that hold shape when squeezed in fist.",
                "scienceNote": "Keeping butter cold ensures defined crunchy clusters form; melted butter would create a greasy paste that bakes flat.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Scatter the crumble clusters evenly over the fruit in a thick, generous layer, making sure fruit is completely covered to trap steam inside.",
                "sensoryCue": "Thick, textured blanket of oats, pecans, and brown sugar clusters.",
                "scienceNote": "The crumble topping acts as a thermal blanket, trapping steam underneath to tenderize the apples while radiant top heat toasts the oats.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Bake at 375°F (190°C) for 32 to 35 minutes until crumble is deep golden-brown and fragrant, and fruit juices bubble up around perimeter.",
                "sensoryCue": "Nutty toasted aroma of roasted pecans and oats; thick amber syrup bubbling.",
                "scienceNote": "Oat starches toast and brown sugars caramelize at 320°F, generating nutty pyrazines.",
                "timerMins": 35
            },
            {
                "stepNum": 5,
                "text": "Cool 10 minutes. Spoon into bowls while piping hot and top each serving with a large quenelle of cold, dense English clotted cream.",
                "sensoryCue": "Rich clotted cream slowly melting into the warm spiced fruit and crunchy oats.",
                "scienceNote": "The 55% fat content in clotted cream provides an insulating dairy barrier that balances the tart fruit acids on the palate.",
                "timerMins": 10
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted rolled oats, warm green cardamom, caramelized apples, roasted pecans",
            "texture": "Tremendous contrast: shatteringly crunchy oat crumble against tender, juicy apples and melting clotted cream",
            "finish": "Exotic floral cardamom notes lingering behind rich dairy fat"
        },
        "scienceNotes": "Cardamom contains high concentrations of 1,8-cineole and terpinyl acetate, aromatic compounds that synergize chemically with the malic acid in tart apples, transforming a pedestrian apple bake into an extraordinary sensory experience.",
        "troubleshooting": {
            "Crumble turns soggy": "Oats were pulverized into powder, or butter was warm when rubbed in.",
            "Apples are still crunchy": "Apples were sliced too thick or were a dry baking variety; use Honeycrisp, Braeburn, or Bramley.",
            "Topping burns before apples cook": "Tent top loosely with foil for the first 20 minutes of baking."
        },
        "substitutions": [
            {"ingredient": "Honeycrisp Apples", "substitute": "Bramley, Honeygold, or Granny Smith", "ratio": "1:1"},
            {"ingredient": "English Clotted Cream", "substitute": "Crème Fraîche or Vanilla Bean Ice Cream", "ratio": "1:1"}
        ],
        "flavorPairings": ["English Breakfast Tea", "Calvados", "Cheddar Cheese Slice", "Hard Apple Cider"],
        "advancedTechnique": "Pre-caramelizing apple slices in browned butter on high heat for 3 minutes before topping with crumble.",
        "storageAndReheating": "Store at room temp up to 2 days covered with foil. Re-crisp in 350°F oven for 8 minutes to restore crunchy oat texture.",
        "nutritionEstimates": {"calories": 360, "protein": 5, "carbs": 48, "fat": 17},
        "relatedRecipes": ["rec-peach-blackberry-cobbler", "rec-tarte-tatin", "rec-bourbon-pecan-pie"],
        "relatedTechniques": ["Cold butter streusel cluster rub", "Terpene spice synergy", "Steam entrapment fruit baking"]
    },
    {
        "id": "rec-fior-di-latte-gelato",
        "title": "Gelato Fior di Latte (Pure Emulsified Sweet Cream Churn)",
        "cuisine": "Italian / Classical Gelateria",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 20,
        "cookMins": 10,
        "totalMins": 30,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ultimate test of an authentic Italian gelatiere: Fior di Latte (flower of milk). No eggs, no vanilla, no distractions—pure, unadorned grass-fed milk and heavy cream churned to low-overrun silky dense perfection with natural locust bean gum.",
        "dietary": ["Vegetarian", "Gluten-Free"],
        "sensoryRole": "Purity of fresh sweet pasture milk, silky smooth tongue-coating density, clean refreshing melt",
        "ingredients": [
            {"name": "Whole Farm Fresh Milk (Grass-Fed)", "qty": 650, "unit": "ml", "prep": "unhomogenized preferred", "dept": "Dairy & Fats"},
            {"name": "Heavy Cream (36-40% fat)", "qty": 200, "unit": "ml", "prep": "fresh sweet cream", "dept": "Dairy & Fats"},
            {"name": "Nonfat Dry Milk Powder", "qty": 35, "unit": "g", "prep": "adds milk solids-not-fat (MSNF)", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 140, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Dextrose / Atomized Glucose", "qty": 30, "unit": "g", "prep": "lowers freezing point", "dept": "Baking & Pantry"},
            {"name": "Locust Bean Gum (Carob Bean Gum)", "qty": 2, "unit": "g", "prep": "natural ice crystal inhibitor", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 1, "unit": "g", "prep": "micro pinch", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Compressor Gelato / Ice Cream Maker", "type": "Small Appliance"},
            {"name": "Digital Gram Scale (0.1g precision)", "type": "Precision Tool"},
            {"name": "Immersion Blender", "type": "Small Appliance"},
            {"name": "Instant Read Thermometer", "type": "Precision Tool"}
        ],
        "miseEnPlace": [
            "Blend dry ingredients: dry milk powder, castor sugar, dextrose, locust bean gum, and salt together in a small bowl to disperse gum evenly.",
            "Chill compressor gelato machine bowl.",
            "Prepare an ice bath to rapid-cool pasteurized base."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "In a heavy saucepan, combine whole milk and heavy cream. Warm over medium heat to 105°F (40°C). Whisk in the blended dry ingredients in a steady rain so locust bean gum doesn't clump.",
                "sensoryCue": "Smooth milky liquid with no sediment.",
                "scienceNote": "Dispersing locust bean gum with dry sugar prevents 'fish eyes' (undissolved hydrocolloid gel lumps).",
                "timerMins": 4
            },
            {
                "stepNum": 2,
                "text": "Heat mixture while stirring constantly to 185°F (85°C). Hold at 185°F for 2 full minutes to pasteurize and fully hydrate the locust bean gum. Remove from heat.",
                "sensoryCue": "Subtle thickening; base coats back of spoon with satiny milk sheen.",
                "scienceNote": "Locust bean gum requires 185°F to fully solubilize its galactomannan polymer chains, which bind free water molecules and inhibit ice crystal growth during freezing.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Emulsify with an immersion blender on high speed for 60 seconds to homogenize fat globules. Transfer base to bowl set inside ice water bath; stir until chilled below 50°F (10°C).",
                "sensoryCue": "Froth-free, glistening, snowy white emulsion.",
                "scienceNote": "High shear immersion blending reduces milkfat globule size, improving tongue-coating lubricity and mouthfeel.",
                "timerMins": 10
            },
            {
                "stepNum": 4,
                "text": "Cover and age base in refrigerator at 38°F (4°C) for 6 to 12 hours (overnight maturation).",
                "sensoryCue": "Viscous, thick, ivory liquid cream.",
                "scienceNote": "Maturation allows milk proteins to fully hydrate and milkfats to partially crystallize, which stabilizes the air cell walls during churning.",
                "timerMins": 480
            },
            {
                "stepNum": 5,
                "text": "Churn in gelato machine for 20 to 25 minutes until thick, dense, and ribboning off the paddle at 21-23°F (-5°C). Transfer into a chilled metal pan and harden in freezer for 2 hours before serving at true gelato temperature (12-14°F / -10°C).",
                "sensoryCue": "Ultra-creamy, shiny, dense gelato waves with minimal air overrun.",
                "scienceNote": "Italian gelato features low overrun (20-30% air vs 80-100% in industrial ice cream) and is served warmer (14°F vs 0°F) so taste buds aren't numbed by cold.",
                "timerMins": 25
            }
        ],
        "sensoryIndicators": {
            "aroma": "Fresh pasture milk, sweet cream, subtle lactic sweetness",
            "texture": "Dense, ultra-silky, velvety melt without a single grain of ice; luxurious mouth-coating",
            "finish": "Clean, refreshing dairy finish with zero cloying heaviness"
        },
        "scienceNotes": "Fior di Latte is the ultimate formulation science dish. Dextrose has 1.9x the freezing point depression of sucrose with only 70% of the sweetness, allowing the gelato to stay scoopable and soft at 14°F without tasting excessively sweet.",
        "troubleshooting": {
            "Icy crunchy texture": "Base was not aged long enough, or churn speed was too slow; freeze churn bowl colder.",
            "Greasy buttery film on roof of mouth": "Fat content was too high (above 12%) or base was over-churned, causing butter churning.",
            "Gelato is too hard to scoop": "Freezer is at 0°F (standard ice cream temp); temper gelato in fridge for 15 mins before scooping."
        },
        "substitutions": [
            {"ingredient": "Locust Bean Gum", "substitute": "Guar Gum or Xanthan Gum", "ratio": "Use 1.5g (note: guar gum hydrates cold)"},
            {"ingredient": "Dextrose", "substitute": "Corn Syrup or additional sugar", "ratio": "1:1 (gelato will be slightly firmer)"}
        ],
        "flavorPairings": ["Fresh Espresso (Affogato)", "Aged Balsamico Tradizionale", "Extra Virgin Olive Oil & Sea Salt", "Wild Strawberries"],
        "advancedTechnique": "Affogato al Caffè: dropping a dense quenelle of Fior di Latte into a preheated porcelain cup and pulling a hot double espresso shot directly over it.",
        "storageAndReheating": "Store in airtight container with parchment pressed to surface in freezer up to 2 weeks. Best eaten within 3 days.",
        "nutritionEstimates": {"calories": 210, "protein": 5, "carbs": 24, "fat": 11},
        "relatedRecipes": ["rec-pistachio-gelato", "rec-blood-orange-sorbet", "rec-panna-cotta"],
        "relatedTechniques": ["Freezing point depression balancing", "Hydrocolloid hot activation", "Low-overrun churn rheology"]
    },
    {
        "id": "rec-pistachio-gelato",
        "title": "Bronte Pistachio Gelato (100% Roasted Sicilian Pistachio Paste)",
        "cuisine": "Italian / Sicilian Classical",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 25,
        "cookMins": 10,
        "totalMins": 35,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=1200&q=80",
        "summary": "The undisputed king of Italian gelaterias: authentic Sicilian Pistacchio di Bronte gelato. Made with 100% pure roasted emerald-green pistachio paste (no almond extracts, no green food dyes), balanced with Sicilian sea salt and churned to dense, luxurious perfection.",
        "dietary": ["Vegetarian", "Gluten-Free"],
        "sensoryRole": "Intensely nutty, roasted, savory-sweet emerald perfection with silky dense churn texture",
        "ingredients": [
            {"name": "Whole Farm Milk (3.5% fat)", "qty": 600, "unit": "ml", "prep": "cold", "dept": "Dairy & Fats"},
            {"name": "Heavy Cream (36% fat)", "qty": 120, "unit": "ml", "prep": "fresh", "dept": "Dairy & Fats"},
            {"name": "Pure Sicilian Bronte Pistachio Paste (100%)", "qty": 140, "unit": "g", "prep": "unsweetened, roasted (Pasta di Pistacchio)", "dept": "Baking & Pantry"},
            {"name": "Nonfat Dry Milk Powder", "qty": 35, "unit": "g", "prep": "for milk solids", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 135, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Dextrose Powder", "qty": 30, "unit": "g", "prep": "for scoopability", "dept": "Baking & Pantry"},
            {"name": "Locust Bean Gum", "qty": 2.5, "unit": "g", "prep": "stabilizer", "dept": "Baking & Pantry"},
            {"name": "Trapani Sea Salt (Fine)", "qty": 2.5, "unit": "g", "prep": "amplifies nut sweetness", "dept": "Baking & Pantry"},
            {"name": "Roasted Pistachios", "qty": 30, "unit": "g", "prep": "coarsely crushed for garnish", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Compressor Gelato Maker", "type": "Small Appliance"},
            {"name": "High-Power Immersion Blender", "type": "Small Appliance"},
            {"name": "Digital Scale (0.1g)", "type": "Precision Tool"}
        ],
        "miseEnPlace": [
            "Whisk dry sugar, dextrose, milk powder, locust bean gum, and sea salt together in a bowl.",
            "Ensure 100% pure pistachio paste is stirred well to homogenize natural oil separation.",
            "Prepare ice bath."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat milk and cream in saucepan to 105°F (40°C). Whisk in the blended dry ingredients in a steady stream. Heat to 185°F (85°C) while stirring continuously; hold at 185°F for 2 minutes to activate the locust bean gum.",
                "sensoryCue": "Smooth ivory base, lightly thickened.",
                "scienceNote": "Thermal activation of locust bean gum creates a 3D network that stabilizes both free water and free pistachio nut oils.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Remove base from heat. Add the 140g pure Sicilian pistachio paste. Emulsify with high-power immersion blender for 90 seconds until the paste is completely dispersed and the base turns a rich, olive-moss green.",
                "sensoryCue": "Fragrant roasted pistachio aroma; uniform sage-green silky emulsion.",
                "scienceNote": "Pistachios contain 45-50% monounsaturated fat; high-shear immersion blending shears the oil droplets down to 1-2 microns, integrating them into the milk protein matrix.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Cool base rapidly in ice water bath below 50°F (10°C). Transfer to refrigerator and mature for 8 to 12 hours.",
                "sensoryCue": "Thick, fragrant green custard base.",
                "scienceNote": "Cold maturation allows pistachio aromatics to permeate the dairy fat phase while triglycerides solidify.",
                "timerMins": 480
            },
            {
                "stepNum": 4,
                "text": "Re-blend base with immersion blender for 20 seconds. Pour into chilled gelato machine. Churn for 20-25 minutes until dense, thick, and pulling away in glossy waves from paddle at 22°F (-5°C).",
                "sensoryCue": "Voluptuous, dense green ribbon waves with velvet sheen.",
                "scienceNote": "Nut fats have lower melting points than butterfat, requiring precise churn temperature to prevent fat agglomeration.",
                "timerMins": 25
            },
            {
                "stepNum": 5,
                "text": "Layer gelato into chilled container, scattering crushed roasted pistachios between layers. Freeze 2 hours before serving at 14°F (-10°C).",
                "sensoryCue": "Smooth, elastic scoop with dark green pistachio flecks.",
                "scienceNote": "Serving at 14°F allows the high unsaturated fat content of pistachios to melt cleanly on tongue receptors.",
                "timerMins": 120
            }
        ],
        "sensoryIndicators": {
            "aroma": "Intensely roasted pistachio, warm toasted sesame nuances, sweet dairy, mineral salt",
            "texture": "Incredible density and elasticity; coats the tongue like liquid silk with crunch of chopped nuts",
            "finish": "Persistent savory-sweet nut complexity that lasts for minutes"
        },
        "scienceNotes": "Cheap pistachio ice creams use almond oil and artificial benzaldehyde flavoring (which tastes like marzipan) because authentic Bronte pistachios cost over $60/kg. Authentic pistachio has an earthy, savory, slightly mineral profile without cherry or almond overtones.",
        "troubleshooting": {
            "Gelato tastes like artificial almond": "Cheap commercial pistachio paste with almond extract was used; look for 100% Bronte D.O.P. paste.",
            "Oily separation": "Immersion blending step was skipped; nut oils must be mechanically sheared into emulsion.",
            "Too soft or soupy": "Pistachio nut oils lower freezing point; reduce cream slightly if necessary."
        },
        "substitutions": [
            {"ingredient": "Pistachio Paste", "substitute": "Piedmont Hazelnut Paste (Nocciola del Piemonte I.G.P.)", "ratio": "1:1 for world-class Hazelnut Gelato"},
            {"ingredient": "Dextrose", "substitute": "Invert Sugar Syrup", "ratio": "1:1"}
        ],
        "flavorPairings": ["Espresso Ristretto", "Dark Chocolate Sorbet", "Brioche col Tuppo", "Sicilian Cannoli"],
        "advancedTechnique": "Brioche con Gelato: slicing a warm Sicilian sweet brioche in half and filling with two massive scoops of pistachio gelato.",
        "storageAndReheating": "Keep in freezer up to 10 days covered with parchment. Temper in refrigerator for 10 minutes before scooping.",
        "nutritionEstimates": {"calories": 260, "protein": 6, "carbs": 26, "fat": 15},
        "relatedRecipes": ["rec-fior-di-latte-gelato", "rec-baklava-pistachio", "rec-paris-brest"],
        "relatedTechniques": ["Nut oil high-shear emulsification", "Galactomannan heat hydration", "Gelato overrun calibration"]
    },
    {
        "id": "rec-blood-orange-sorbet",
        "title": "Blood Orange & Campari Sorbet (Refractometer Brix-Balanced)",
        "cuisine": "Italian / Modernist Sorbetteria",
        "category": "dessert",
        "slot": "predessert",
        "difficulty": "Easy",
        "prepMins": 15,
        "cookMins": 5,
        "totalMins": 20,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=1200&q=80",
        "summary": "A breathtaking ruby-crimson palate cleanser and modernist sorbet. Fresh Sicilian Moro blood orange juice calibrated to exactly 28° Brix with simple syrup and dextrose, infused with Campari bitter aperitivo and stabilized with cold-hydrating xanthan gum.",
        "dietary": ["Vegan", "Gluten-Free"],
        "sensoryRole": "Electric citrus acidity, bitter botanical complexity, melting jewel-like ruby silkiness",
        "ingredients": [
            {"name": "Fresh Squeezed Blood Orange Juice (Moro or Tarocco)", "qty": 600, "unit": "ml", "prep": "strained of seeds and heavy pulp", "dept": "Produce"},
            {"name": "Mineral Water", "qty": 150, "unit": "ml", "prep": "filtered", "dept": "Pantry"},
            {"name": "Granulated Castor Sugar", "qty": 130, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Dextrose Powder", "qty": 35, "unit": "g", "prep": "lowers freezing point without excess sweetness", "dept": "Baking & Pantry"},
            {"name": "Campari Bitter Liqueur", "qty": 25, "unit": "ml", "prep": "adds botanical bitterness & antifreeze effect", "dept": "Pantry"},
            {"name": "Fresh Lemon Juice", "qty": 20, "unit": "ml", "prep": "sharpens pH balance", "dept": "Produce"},
            {"name": "Xanthan Gum (or Locust Bean)", "qty": 0.8, "unit": "g", "prep": "molecular stabilizer for creaminess", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Digital Optical Brix Refractometer (optional but recommended)", "type": "Precision Tool"},
            {"name": "Compressor Gelato / Ice Cream Maker", "type": "Small Appliance"},
            {"name": "Immersion Blender", "type": "Small Appliance"}
        ],
        "miseEnPlace": [
            "Squeeze fresh blood oranges and pass juice through fine sieve; measure 600ml.",
            "Whisk dry sugar, dextrose, and xanthan gum together in a cup.",
            "Chill blood orange juice in refrigerator to 38°F."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Base Syrup: Combine 150ml water and the dry sugar/dextrose/xanthan blend in small saucepan. Bring just to a simmer for 60 seconds while whisking until completely clear and dissolved. Remove from heat and cool in ice bath.",
                "sensoryCue": "Clear, slightly viscous sugar syrup.",
                "scienceNote": "Xanthan gum hydrates instantly in warm water, creating a pseudoplastic shear-thinning fluid that prevents large ice crystals from aggregating.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Combine chilled syrup, fresh blood orange juice, lemon juice, and Campari in a pitcher. Blend with immersion blender on high for 30 seconds. Check sugar concentration with refractometer: target is exactly 28-30° Brix (or float a raw clean egg in shell; egg should float leaving a quarter-sized patch exposed above liquid).",
                "sensoryCue": "Vibrant fluorescent crimson-ruby liquid with citrus botanical aroma.",
                "scienceNote": "Sorbet texture is governed entirely by sugar concentration (Brix). At 28° Brix, exactly 72% of water freezes into microscopic ice crystals while 28% remains as liquid sugar syrup, creating spoonable silk without dairy.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Chill base in refrigerator for 2 hours until thoroughly cold (under 40°F / 4°C).",
                "sensoryCue": "Viscous ruby nectar.",
                "scienceNote": "Pouring warm base into a churner causes slow freezing and coarse, crunchy ice needles.",
                "timerMins": 120
            },
            {
                "stepNum": 4,
                "text": "Pour into gelato machine and churn for 18-20 minutes until firm, satiny, and pulling away from paddle in dense ribbon folds.",
                "sensoryCue": "Gleaming ruby-red ribboning sorbet with frosty sheen.",
                "scienceNote": "Campari contains 24% ABV alcohol; alcohol significantly depresses the freezing point of water, boosting sorbet softness.",
                "timerMins": 20
            },
            {
                "stepNum": 5,
                "text": "Transfer into a chilled shallow pan and freeze for 1 hour. Scoop into chilled glasses; garnish with candied blood orange wheel or fresh mint sprig.",
                "sensoryCue": "Spoon glides through like butter; jewel-toned ruby sphere.",
                "scienceNote": "Melts rapidly on tongue, releasing intense fruit terpenes and volatile aromatic esters.",
                "timerMins": 60
            }
        ],
        "sensoryIndicators": {
            "aroma": "Floral blood orange zest, bitter gentian root, ruby grapefruit, campari herbal aromatics",
            "texture": "Ultra-smooth, velvety, grain-free melt withzero iciness",
            "finish": "Electrifying tart-bitter-sweet finish that completely resets and cleanses the palate"
        },
        "scienceNotes": "Sorbets contain zero milkfat, meaning ice crystal inhibition depends 100% on sugar physics and small concentrations of hydrocolloids. Dextrose provides freezing point depression without excess cloying sweetness, while Campari adds both flavor complexity and ethanol antifreeze properties.",
        "troubleshooting": {
            "Sorbet is a hard rock ice block": "Not enough sugar (Brix was under 24°); add 2-3 tbsp simple syrup.",
            "Sorbet won't freeze / remains slush": "Too much sugar or too much alcohol (Brix over 32° or over 35ml Campari); dilute with more juice.",
            "Icy, coarse texture": "Base was churned warm or lacked stabilizer; use exact 0.8g xanthan gum."
        },
        "substitutions": [
            {"ingredient": "Blood Orange Juice", "substitute": "Ruby Red Grapefruit Juice, Pomegranate Juice, or Passionfruit", "ratio": "1:1"},
            {"ingredient": "Campari", "substitute": "Aperol (sweeter) or Gin", "ratio": "1:1"}
        ],
        "flavorPairings": ["Prosecco Pour", "Fresh Basil Leaves", "Dark Chocolate Tuile", "Fennel Pollen"],
        "advancedTechnique": "Sgropino Moderno: whisking two scoops of blood orange sorbet with 60ml chilled Prosecco and 15ml vodka into an airy effervescent cocktail coupe.",
        "storageAndReheating": "Store airtight in freezer up to 2 weeks. Best texture within first 3 days.",
        "nutritionEstimates": {"calories": 140, "protein": 1, "carbs": 33, "fat": 0},
        "relatedRecipes": ["rec-fior-di-latte-gelato", "rec-shattered-lemon-tart", "rec-mango-spheres"],
        "relatedTechniques": ["Refractometer Brix balancing", "Ethanol freezing point depression", "Hydrocolloid ice crystal inhibition"]
    },
    {
        "id": "rec-quiche-lorraine",
        "title": "Quiche Lorraine Traditionnelle (Smoked Bacon Lardons & Gruyère Custard)",
        "cuisine": "French / Classical Bistro",
        "category": "lunch",
        "slot": "opener",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 45,
        "totalMins": 75,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=1200&q=80",
        "summary": "The authentic French country classic from northeastern France: crisp, buttery, flaky pâte brisée blind-baked to golden perfection, filled with crispy smoked bacon lardons, aged Swiss Gruyère, and an ultra-silky, wobbling egg-and-crème-fraîche custard kissed with fresh nutmeg.",
        "dietary": [],
        "sensoryRole": "Rich, silky custardy center, smoky pork savoriness, nutty alpine cheese, crisp shattering crust",
        "ingredients": [
            {"name": "Pâte Brisée (Flaky French Shortcrust)", "qty": 300, "unit": "g", "prep": "chilled dough (butter, flour, salt, ice water)", "dept": "Baking & Pantry"},
            {"name": "Thick-Cut Smoked Bacon / Pancetta", "qty": 200, "unit": "g", "prep": "sliced into 1/4-inch lardons", "dept": "Meat & Poultry"},
            {"name": "Aged Gruyère A.O.P. or Comté Cheese", "qty": 150, "unit": "g", "prep": "freshly shredded", "dept": "Dairy & Fats"},
            {"name": "Large Whole Eggs", "qty": 3, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Egg Yolks", "qty": 2, "unit": "whole", "prep": "adds velvety richness", "dept": "Dairy & Fats"},
            {"name": "Crème Fraîche or Heavy Cream (36%)", "qty": 250, "unit": "ml", "prep": "rich cultured cream", "dept": "Dairy & Fats"},
            {"name": "Whole Milk", "qty": 150, "unit": "ml", "prep": "farm fresh", "dept": "Dairy & Fats"},
            {"name": "Fresh Grated Whole Nutmeg", "qty": 2, "unit": "g", "prep": "microplaned", "dept": "Spices & Botanicals"},
            {"name": "Fresh Cracked White Pepper", "qty": 2, "unit": "g", "prep": "fine grind", "dept": "Spices & Botanicals"},
            {"name": "Fine Sea Salt", "qty": 2, "unit": "g", "prep": "careful with bacon saltiness", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "9-inch Fluted Tart Pan with Removable Bottom (Deep 1.5-inch)", "type": "Bakeware"},
            {"name": "Pie Weights or Dry Beans", "type": "Baking Supply"},
            {"name": "Cast-Iron Skillet for Lardons", "type": "Cookware"},
            {"name": "Whisk & Mixing Bowl", "type": "Cookware"}
        ],
        "miseEnPlace": [
            "Roll chilled pâte brisée to 3mm thickness, fit into 9-inch tart pan, trim overhang, and freeze for 20 minutes.",
            "Preheat oven to 375°F (190°C).",
            "Cut bacon into lardons; grate Gruyère cheese."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Blind-Bake Crust: Line frozen tart shell with parchment paper and fill to the brim with pie weights or dried beans. Bake at 375°F (190°C) for 20 minutes. Remove parchment and weights; prick base lightly with fork. Return to oven for 8-10 minutes until base is pale golden and completely dry. Cool 10 minutes. Lower oven to 325°F (165°C).",
                "sensoryCue": "Pastry is crisp, golden, dry, and smelling of toasted butter.",
                "scienceNote": "Blind-baking gelatinizes starches and browns the crust, forming an impermeable moisture barrier that prevents the wet liquid custard from creating a soggy 'flabby' bottom.",
                "timerMins": 30
            },
            {
                "stepNum": 2,
                "text": "Crisp Lardons: Cook bacon lardons in skillet over medium-low heat for 8 minutes until golden brown and crisp but still tender in center (not hard crumbles). Drain on paper towels; reserve rendered fat for other kitchen uses.",
                "sensoryCue": "Crisp mahogany exterior with aromatic smoked hardwood aroma.",
                "scienceNote": "Rendering excess fat prevents oil slicks from pooling on top of the custard during baking.",
                "timerMins": 8
            },
            {
                "stepNum": 3,
                "text": "Make Custard Emulsion: In a bowl, whisk whole eggs, extra yolks, crème fraîche, whole milk, grated nutmeg, white pepper, and salt until smooth and uniform (do not whip aggressively to avoid foam).",
                "sensoryCue": "Pale primrose yellow custard with micro-flecks of nutmeg.",
                "scienceNote": "Using extra yolks and crème fraîche elevates fat content to approx 18%, lowering the water activity and ensuring an unctuous custard that wobbles without weeping.",
                "timerMins": 4
            },
            {
                "stepNum": 4,
                "text": "Assemble & Bake: Scatter crisp lardons and shredded Gruyère evenly across bottom of par-baked tart shell. Place tart pan on a baking sheet on center oven rack. Pour custard batter slowly over lardons up to 1/8-inch below tart rim. Bake at 325°F (165°C) for 32 to 38 minutes until puffed, golden, but center still has a gentle slow tremble.",
                "sensoryCue": "Golden-bronzed top with light cheese browning; center jiggles gently.",
                "scienceNote": "Baking at gentle 325°F maintains egg coagulation temperature below 180°F, preventing protein syneresis and rubbery curdling.",
                "timerMins": 35
            },
            {
                "stepNum": 5,
                "text": "Rest & Slice: Rest quiche on wire rack for 20 minutes before removing tart outer ring. Slice warm into wedges with a sharp chef's knife.",
                "sensoryCue": "Pristine clean triangular slices; silky custard showing suspended bacon and melted cheese pockets.",
                "scienceNote": "Resting allows the thermal energy to equalize and the dairy protein network to set firmly for clean cutting.",
                "timerMins": 20
            }
        ],
        "sensoryIndicators": {
            "aroma": "Smoky hickory bacon, melted alpine Gruyère, warm nutmeg, buttery pastry crust",
            "texture": "Crisp shattering pastry crust meeting ultra-creamy, melt-in-mouth custard and chewy savory lardons",
            "finish": "Savory umami and nutty cheese lingering with subtle nutmeg warmth"
        },
        "scienceNotes": "The traditional ratio for luxury quiche custard is 1 large egg (or 2 yolks) per 100ml of dairy liquid (milk + crème fraîche). Crème fraîche contains lactic acid cultures that impart subtle tang and soften the egg protein gel network.",
        "troubleshooting": {
            "Soggy bottom crust": "Crust was not blind-baked sufficiently before adding custard.",
            "Custard wept water or turned rubbery": "Oven was too hot (above 350°F), causing egg proteins to contract violently and expel water.",
            "Lardons sank to bottom in single clump": "Distribute lardons and cheese evenly across pan before pouring custard."
        },
        "substitutions": [
            {"ingredient": "Smoked Bacon", "substitute": "Caramelized Leeks and Wild Mushrooms", "ratio": "For a Vegetarian Quiche aux Poireaux"},
            {"ingredient": "Gruyère", "substitute": "Comté, Emmental, or Beaufort", "ratio": "1:1"}
        ],
        "flavorPairings": ["Crisp Butter Lettuce Salad with Dijon Vinaigrette", "Sancerre or Chablis", "Dry Hard Cider"],
        "advancedTechnique": "Brushing inside of hot par-baked tart shell with raw beaten egg white and baking for 2 minutes to create a glass-like albumen waterproof glaze.",
        "storageAndReheating": "Refrigerate up to 4 days covered. Reheat whole or slices in 325°F oven for 12 minutes to restore crust crispness.",
        "nutritionEstimates": {"calories": 480, "protein": 16, "carbs": 24, "fat": 36},
        "relatedRecipes": ["rec-french-rolled-omelette", "rec-croque-madame", "rec-eggs-benedict"],
        "relatedTechniques": ["Blind baking moisture barrier", "Custard protein coagulation window", "Albumen waterproofing glaze"]
    }
]

print(f"Loaded {len(PART_3_RECIPES)} recipes in PART_3_RECIPES.")
