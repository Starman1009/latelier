# -*- coding: utf-8 -*-
"""
Generate comprehensive culinary master recipes adhering to the 28-field schema
and merge into data-recipes.js.
Focus on aggressive dessert expansion, breakfast/brunch, appetizers, and global classics.
"""
import json, re

NEW_RECIPES = [
    # DESSERTS
    {
        "id": "rec-creme-caramel",
        "title": "Classical Crème Caramel (Flan Parisien au Caramel)",
        "cuisine": "French",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "intermediate",
        "prepMins": 30,
        "cookMins": 45,
        "totalMins": 75,
        "yieldServings": 6,
        "heroImage": "assets/images/creme-caramel.jpg",
        "summary": "The pinnacle of French bistro pastry: a silky, glass-smooth whole milk and egg yolk custard inverted onto a plate with a pool of amber-bitter dry caramel sauce.",
        "dietary": ["vegetarian", "gluten_free"],
        "sensoryRole": "Silky, voluptuous custard yielding to a dark, bittersweet liquid amber caramel with floral Madagascar vanilla notes.",
        "ingredients": [
            {"name": "Granulated White Sugar", "qty": 150, "unit": "g", "prep": "for dry caramel", "dept": "pantry"},
            {"name": "Whole Milk (3.5% fat)", "qty": 500, "unit": "ml", "prep": "room temp", "dept": "dairy"},
            {"name": "Heavy Cream (36% fat)", "qty": 100, "unit": "ml", "prep": "for richness", "dept": "dairy"},
            {"name": "Madagascar Vanilla Bean", "qty": 1, "unit": "ea", "prep": "split and scraped", "dept": "pantry"},
            {"name": "Whole Farm Eggs", "qty": 3, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Egg Yolks", "qty": 3, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Granulated Sugar (Custard)", "qty": 85, "unit": "g", "prep": "for custard base", "dept": "pantry"},
            {"name": "Fine Sea Salt", "qty": 1, "unit": "g", "prep": "pinch", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Copper or heavy stainless saucepan", "type": "cookware"},
            {"name": "6 individual 150ml ceramic ramekins", "type": "bakeware"},
            {"name": "Roasting pan for bain-marie", "type": "cookware"},
            {"name": "Fine mesh conical chinois", "type": "tool"}
        ],
        "miseEnPlace": [
            "Set 6 ceramic ramekins in a deep roasting pan lined with a tea towel.",
            "Split vanilla bean lengthwise and scrape seeds into milk and cream in a saucepan.",
            "Preheat oven to 300°F (150°C) with low fan or static heat."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make the dry caramel: In a heavy stainless saucepan over medium heat, add sugar gradually. Allow to melt without stirring until it turns a deep mahogany amber (360°F/182°C). Immediately pour evenly into the base of the 6 ramekins, swirling to coat the bottom.",
                "sensoryCue": "Sugar transforms from clear syrup into foaming copper amber with an intoxicating bittersweet toasted aroma.",
                "scienceNote": "Thermal decomposition of sucrose begins at 320°F (160°C). Heating to mahogany stage produces caramelans and diacetyl, balancing sweet and bitter.",
                "timerMins": 8
            },
            {
                "stepNum": 2,
                "text": "Scald milk and cream: Bring milk, cream, vanilla pod, and scraped seeds to a gentle simmer (180°F/82°C). Remove from heat and infuse for 10 minutes.",
                "sensoryCue": "Tiny bubbles form at the saucepan perimeter; heady perfume of vanilla fills the air.",
                "scienceNote": "Scalding alters whey protein structures, allowing them to participate in the egg gel network for a denser, silkier texture.",
                "timerMins": 10
            },
            {
                "stepNum": 3,
                "text": "Whisk eggs and sugar: In a bowl, gently whisk whole eggs, yolks, sugar, and salt until combined without whipping air into the mixture.",
                "sensoryCue": "Yolks loosen and dissolve the sugar granules into a smooth pale ribbon.",
                "scienceNote": "Excessive whisking traps micro-bubbles that expand during baking, creating unsightly honeycomb craters inside the custard.",
                "timerMins": 3
            },
            {
                "stepNum": 4,
                "text": "Temper and strain: Slowly ladle warm milk into egg mixture while whisking constantly. Pass through a fine mesh chinois into a pitcher to remove chalazae and foam.",
                "sensoryCue": "The custard liquid pours completely smooth like heavy silk with no egg shreds.",
                "scienceNote": "Straining removes denatured egg cords and chalazae, ensuring an isotropic protein suspension.",
                "timerMins": 4
            },
            {
                "stepNum": 5,
                "text": "Bake in bain-marie: Pour custard into caramel-lined ramekins. Pour boiling water into roasting pan until it reaches halfway up ramekin sides. Bake at 300°F (150°C) for 40-45 minutes.",
                "sensoryCue": "The custards are set around the perimeter with a gentle gelatinous wobble in the center when tapped.",
                "scienceNote": "The water bath buffers heat, keeping the ramekin walls below 212°F (100°C) so egg vitellin coagulates smoothly without boiling.",
                "timerMins": 45
            },
            {
                "stepNum": 6,
                "text": "Chill and invert: Cool to room temperature, then refrigerate for at least 6 hours (preferably overnight). Run a thin paring knife around the edge, place plate over ramekin, and invert firmly.",
                "sensoryCue": "A satisfying vacuum pop as the flan slides onto the plate, draped in a cascade of glossy amber caramel.",
                "scienceNote": "Overnight resting allows moisture from the custard to migrate into the hard caramel layer, dissolving it into a liquid sauce.",
                "timerMins": 360
            }
        ],
        "sensoryIndicators": {
            "visual": "Mirror-smooth ivory custard cylinder cloaked in translucent copper-red caramel sauce",
            "tactile": "Melts instantly on the tongue without graininess or rubbery resistance",
            "aroma": "Burnished caramelized sugar, rich cream, and fragrant woody Bourbon vanilla",
            "internalTemp": "Center of custard registers 175°F-180°F (79°C-82°C) at pull"
        },
        "scienceNotes": "Egg protein coagulation is governed by salt, sugar, and lipid concentration. Added yolks increase the ratio of lecithin and vitellin relative to ovalbumin, lowering the water content and producing a velvety gel instead of a rubbery curd.",
        "troubleshooting": [
            {"issue": "Custard has small holes/craters (honeycombing)", "solution": "Oven temperature was too high or bain-marie water boiled. Keep oven at 300°F and line pan with towel."},
            {"issue": "Caramel is stuck to bottom of ramekin", "solution": "Custard needs more chilling time (minimum 6h) for moisture to dissolve the caramel. Dip ramekin base in hot water for 30s before inverting."}
        ],
        "substitutions": [
            {"original": "Madagascar Vanilla Bean", "sub": "Pure vanilla bean paste (1.5 tsp)", "impact": "Provides identical aroma and flecks without pod steeping."}
        ],
        "flavorPairings": {
            "wine": "Château d'Yquem Sauternes or Pedro Ximénez Sherry",
            "zeroProof": "Chilled Rooibos tea cold-brewed with orange peel and cinnamon quill"
        },
        "advancedTechnique": "Infuse the scalded milk with 2g of bruised kaffir lime leaves or tonka bean for a modern citrus-almond dimension.",
        "storageAndReheating": "Store covered in refrigerator for up to 4 days in ramekins. Invert onto plates right before serving.",
        "nutritionEstimates": {"calories": 285, "protein": 7, "carbs": 38, "fat": 12},
        "relatedRecipes": ["rec-creme-brulee", "rec-panna-cotta", "rec-paris-brest"],
        "relatedTechniques": ["Bain-marie baking", "Dry sugar caramelization", "Custard tempering"]
    },
    {
        "id": "rec-mousse-chocolat",
        "title": "Mousse au Chocolat Classique (Dark Chocolate Mousse with Fleur de Sel)",
        "cuisine": "French",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "intermediate",
        "prepMins": 25,
        "cookMins": 5,
        "totalMins": 30,
        "yieldServings": 6,
        "heroImage": "assets/images/mousse-chocolat.jpg",
        "summary": "The definitive French bistro dessert: bittersweet 70% chocolate emulsified with egg yolks, folded into an airy web of stiff meringue, and chilled to a cloud-like mousse.",
        "dietary": ["vegetarian", "gluten_free"],
        "sensoryRole": "Airy, billowy chocolate foam that collapses into intense, velvety cacao butter richness with intermittent bursts of crunchy mineral sea salt.",
        "ingredients": [
            {"name": "Valrhona Guanaja 70% Dark Chocolate", "qty": 200, "unit": "g", "prep": "finely chopped", "dept": "pantry"},
            {"name": "High-Fat Cultured Butter", "qty": 30, "unit": "g", "prep": "cubed", "dept": "dairy"},
            {"name": "Egg Yolks", "qty": 4, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Egg Whites", "qty": 5, "unit": "ea", "prep": "room temp, no yolk traces", "dept": "dairy"},
            {"name": "Superfine Castor Sugar", "qty": 35, "unit": "g", "prep": "for stabilizing whites", "dept": "pantry"},
            {"name": "Maldon Sea Salt Flakes", "qty": 2, "unit": "g", "prep": "for garnish", "dept": "pantry"},
            {"name": "Espresso Powder", "qty": 1, "unit": "g", "prep": "pinch to amplify cacao", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Double boiler or heatproof glass bowl", "type": "cookware"},
            {"name": "Stand mixer or balloon whisk", "type": "appliance"},
            {"name": "Flexible silicone spatula", "type": "tool"},
            {"name": "6 coupe glasses or ceramic ramekins", "type": "tableware"}
        ],
        "miseEnPlace": [
            "Finely chop chocolate with a serrated knife so it melts uniformly.",
            "Separate eggs cleanly; ensure bowl for whites is immaculately grease-free.",
            "Bring 1 inch of water to a bare simmer in double boiler."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Melt chocolate and butter: Set chopped chocolate and butter in heatproof bowl over barely simmering water. Stir occasionally until completely melted and glossy (115°F/46°C). Remove from heat and let cool 4 minutes.",
                "sensoryCue": "Chocolate relaxes into a viscous, fragrant mirror of dark silk.",
                "scienceNote": "Direct intense heat scorches cacao solids. Butterfat and lecithin in the chocolate maintain a smooth suspension.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Stir in yolks: Whisk egg yolks and espresso powder into the warm chocolate one by one until thoroughly emulsified. The mixture will thicken slightly.",
                "sensoryCue": "The mixture turns into a rich, fudge-like glossy paste.",
                "scienceNote": "Yolk lecithin binds chocolate fat droplets, creating an oil-in-water base emulsion.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Whip egg whites to glossy meringue: In a pristine bowl, whip egg whites on medium speed until foamy. Gradually rain in superfine sugar, then increase speed to medium-high until firm, glossy peaks form with a slight curl at the tip.",
                "sensoryCue": "Whites swell into voluminous, snow-white glossy crests that hold their shape inverted.",
                "scienceNote": "Sugar increases viscosity of the water phase between air bubbles, preventing foam drainage (syneresis).",
                "timerMins": 4
            },
            {
                "stepNum": 4,
                "text": "Fold together gently: Take 1/3 of the meringue and vigorously fold it into the chocolate base to lighten its density. Then gently fold in the remaining 2/3 with wide circular sweeps of a silicone spatula, rotating the bowl.",
                "sensoryCue": "Streaks of dark brown and white swirl together into an even, fluffy, cloud-like mousse.",
                "scienceNote": "The sacrifice of the first third matches specific gravities, preventing the heavier chocolate from collapsing the delicate protein bubbles.",
                "timerMins": 3
            },
            {
                "stepNum": 5,
                "text": "Portion and chill: Divide mousse among 6 serving glasses. Chill for at least 4 hours to set the cacao butter crystals. Garnish with flaky sea salt before serving.",
                "sensoryCue": "The surface sets to a delicate matte sheen with microscopic air bubbles intact.",
                "scienceNote": "Beta-form cocoa butter crystals solidify at 64°F-68°F, locking the whipped foam structure without need for gelatin.",
                "timerMins": 240
            }
        ],
        "sensoryIndicators": {
            "visual": "Deep chocolate-brown matte foam showing fine micro-aeration on the spoon",
            "tactile": "Feather-light on the tongue, melting smoothly without graininess",
            "aroma": "Intense roasted cacao, vanilla, and dark fruit esters",
            "internalTemp": "Cold at 38°F-42°F (3°C-5°C)"
        },
        "scienceNotes": "Egg white proteins (conalbumin, ovalbumin) unfold during mechanical whipping to form an amphiphilic matrix around air pockets. As the melted chocolate cools, its polymorph V cocoa butter crystals solidify, providing rigid structure to the foam without gelatin.",
        "troubleshooting": [
            {"issue": "Chocolate seized into a stiff grain", "solution": "A drop of water contaminated the melting chocolate. Whisk in 1 tsp boiling water or warm cream to restore emulsion."},
            {"issue": "Mousse is dense and heavy", "solution": "Whites were over-whipped into dry clumps or folded too aggressively, knocking out trapped air."}
        ],
        "substitutions": [
            {"original": "70% Dark Chocolate", "sub": "60% Bittersweet Chocolate", "impact": "Sweeter finish; reduce added sugar by 10g."}
        ],
        "flavorPairings": {
            "wine": "Banyuls Grand Cru or 20-Year Tawny Port",
            "zeroProof": "Chilled single-origin Colombian cold brew with cardamom tonic"
        },
        "advancedTechnique": "Infuse the melted butter with smoked Maldon salt or chipotle powder for subtle smoky undertones that complement dark cacao.",
        "storageAndReheating": "Keep refrigerated covered for up to 3 days. Never freeze.",
        "nutritionEstimates": {"calories": 290, "protein": 6, "carbs": 24, "fat": 20},
        "relatedRecipes": ["rec-chocolate-lava", "rec-souffle-chocolat", "rec-tiramisu"],
        "relatedTechniques": ["Chocolate melting curve", "French meringue aeration", "Specific gravity folding"]
    },
    {
        "id": "rec-bourbon-pecan-pie",
        "title": "Bourbon Pecan Pie with Brown Butter & Flaky Shortcrust",
        "cuisine": "American",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "intermediate",
        "prepMins": 40,
        "cookMins": 55,
        "totalMins": 95,
        "yieldServings": 8,
        "heroImage": "assets/images/bourbon-pecan-pie.jpg",
        "summary": "The quintessential Southern dessert elevated with nutty beurre noisette, toasted Texas pecan halves, dark brown sugar, and barrel-aged Kentucky bourbon in an all-butter blind-baked crust.",
        "dietary": ["vegetarian"],
        "sensoryRole": "Deep buttery caramel and smoky whiskey notes balancing the earthy crunch of toasted pecans and shattering, flaky pastry.",
        "ingredients": [
            {"name": "All-Butter Pie Dough (Blind-baked 9\" shell)", "qty": 1, "unit": "shell", "prep": "chilled", "dept": "bakery"},
            {"name": "Pecan Halves", "qty": 250, "unit": "g", "prep": "toasted at 325°F", "dept": "produce"},
            {"name": "Unsalted Butter (Browned)", "qty": 85, "unit": "g", "prep": "beurre noisette", "dept": "dairy"},
            {"name": "Dark Brown Sugar", "qty": 150, "unit": "g", "prep": "packed", "dept": "pantry"},
            {"name": "Pure Cane Maple Syrup", "qty": 120, "unit": "ml", "prep": "Grade A", "dept": "pantry"},
            {"name": "Kentucky Bourbon Whiskey", "qty": 45, "unit": "ml", "prep": "barrel-aged", "dept": "beverages"},
            {"name": "Whole Eggs", "qty": 3, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Fine Sea Salt", "qty": 3, "unit": "g", "prep": "fine grain", "dept": "pantry"},
            {"name": "Vanilla Bean Paste", "qty": 5, "unit": "ml", "prep": "extract", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "9-inch fluted ceramic or metal pie pan", "type": "bakeware"},
            {"name": "Small heavy saucepan for browning butter", "type": "cookware"},
            {"name": "Whisk and stainless mixing bowl", "type": "tool"}
        ],
        "miseEnPlace": [
            "Blind bake 9-inch pie crust with pie weights at 375°F for 20 minutes; remove weights and bake 8 minutes more until golden; cool.",
            "Toast pecan halves on sheet tray at 325°F for 8 minutes until aromatic; cool.",
            "Brown butter in saucepan until foaming subsides and hazelnut-brown milk solids appear."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make brown butter: Melt butter over medium heat. Swirl as it foams, then turns clear golden, and finally develops nutty brown flecks at the bottom (beurre noisette). Immediately pour into bowl to stop cooking.",
                "sensoryCue": "Intense hazelnut and toasted biscuit aroma with a frothy amber foam.",
                "scienceNote": "Maillard reaction between milk lactose and whey proteins creates nutty alkylpyrazines at 285°F (140°C).",
                "timerMins": 6
            },
            {
                "stepNum": 2,
                "text": "Whisk custard base: In a bowl, whisk brown sugar, maple syrup, warm brown butter, eggs, bourbon, salt, and vanilla until smooth and dissolved.",
                "sensoryCue": "Glossy mahogany caramel custard that ribbons from the whisk.",
                "scienceNote": "Maple syrup invert sugars prevent crystallization of the sucrose during baking.",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Assemble pie: Scatter 2/3 of toasted pecans across the bottom of the par-baked pie shell. Pour custard over the nuts. Arrange remaining pecan halves neatly in concentric circles on top.",
                "sensoryCue": "Pecan halves float gently atop the glossy amber custard.",
                "scienceNote": "Pecans are less dense than the high-sugar custard; they float to create a naturally crisp top layer.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "Bake to gentle set: Bake at 350°F (175°C) on the lowest oven rack for 45-50 minutes until the edges are puffed and center has a slight gelatinous tremor.",
                "sensoryCue": "The filling puffs like a soufflé at edges with tiny caramelized bubbles; center wobbles gently.",
                "scienceNote": "Egg proteins set at 165°F-170°F (74°C-77°C); cooling allows the starch and sugar matrix to firm up.",
                "timerMins": 48
            },
            {
                "stepNum": 5,
                "text": "Cool completely: Cool on a wire rack for at least 4 hours before slicing. Serve with stabilized Chantilly cream.",
                "sensoryCue": "Crust stays razor crisp; interior slices cleanly like rich fudge.",
                "scienceNote": "Allowing pie to cool to room temperature finishes starch retrogradation and butterfat solidification.",
                "timerMins": 240
            }
        ],
        "sensoryIndicators": {
            "visual": "Glistening concentric circles of dark toasted pecans over a rich amber custard in a flaky golden crust",
            "tactile": "Shattering crisp crust, crunchy nutty top, and toothsome gooey custard interior",
            "aroma": "Toasted pecans, brown butter, vanilla, and oaky bourbon vapors",
            "internalTemp": "Center registers 170°F (77°C) when pulled from oven"
        },
        "scienceNotes": "Replacing corn syrup with maple syrup and browned butter eliminates cloying sweetness while increasing complex aromatic pyrazines and vanillin. Baking on the lowest rack conducts heat into the bottom crust to prevent a soggy bottom.",
        "troubleshooting": [
            {"issue": "Crust bottom is pale and soggy", "solution": "Blind-bake the crust thoroughly before adding filling, and bake on a preheated pizza stone or bottom oven rack."},
            {"issue": "Filling is watery/soupy after cutting", "solution": "Pie was cut warm before the egg-starch gel set. Must cool completely for 4 hours."}
        ],
        "substitutions": [
            {"original": "Kentucky Bourbon", "sub": "Dark Rum or Cognac", "impact": "Subtle fruit/molasses note instead of oak-smoke whiskey profile."},
            {"original": "Maple Syrup", "sub": "Dark corn syrup or sorghum syrup", "impact": "Traditional Southern flavor with slightly more viscous body."}
        ],
        "flavorPairings": {
            "wine": "Tawny Port or Madeira (Bual)",
            "zeroProof": "Smoked black tea (Lapsang Souchong) sweetened with raw demerara syrup"
        },
        "advancedTechnique": "Brush the par-baked crust with beaten egg white and bake for 2 minutes to create an impermeable protein shield against soggy bottoms.",
        "storageAndReheating": "Store loosely covered at room temperature for 2 days or refrigerated for 4 days.",
        "nutritionEstimates": {"calories": 520, "protein": 6, "carbs": 58, "fat": 32},
        "relatedRecipes": ["rec-creme-brulee", "rec-sourdough-country-loaf"],
        "relatedTechniques": ["Blind baking pie crust", "Beurre noisette", "Custard stabilization"]
    },
    {
        "id": "rec-coconut-cream-pie",
        "title": "Coconut Cream Pie with Graham Cracker Crust & Toasted Flakes",
        "cuisine": "American",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "intermediate",
        "prepMins": 45,
        "cookMins": 20,
        "totalMins": 65,
        "yieldServings": 8,
        "heroImage": "assets/images/coconut-cream-pie.jpg",
        "summary": "A restaurant pastry benchmark: a buttery crisp graham cracker shell loaded with scratch coconut pastry cream (crème pâtissière), topped with mountain peaks of stabilized Chantilly and toasted coconut shreds.",
        "dietary": ["vegetarian"],
        "sensoryRole": "Creamy tropical coconut sweetness enveloped in airy whipped cream, contrasted by buttery cinnamon graham cracker crunch.",
        "ingredients": [
            {"name": "Graham Cracker Crumbs", "qty": 200, "unit": "g", "prep": "finely ground", "dept": "pantry"},
            {"name": "Melted Butter", "qty": 75, "unit": "g", "prep": "for crust", "dept": "dairy"},
            {"name": "Granulated Sugar", "qty": 130, "unit": "g", "prep": "split for crust & custard", "dept": "pantry"},
            {"name": "Whole Milk", "qty": 500, "unit": "ml", "prep": "for custard", "dept": "dairy"},
            {"name": "Coconut Cream (Unsweetened)", "qty": 200, "unit": "ml", "prep": "canned full fat", "dept": "pantry"},
            {"name": "Egg Yolks", "qty": 4, "unit": "ea", "prep": "for custard", "dept": "dairy"},
            {"name": "Cornstarch", "qty": 40, "unit": "g", "prep": "thickener", "dept": "pantry"},
            {"name": "Unsweetened Shredded Coconut", "qty": 120, "unit": "g", "prep": "toasted golden", "dept": "pantry"},
            {"name": "Cold Butter (diced)", "qty": 45, "unit": "g", "prep": "to mount custard", "dept": "dairy"},
            {"name": "Heavy Whipping Cream (36% fat)", "qty": 300, "unit": "ml", "prep": "chilled for Chantilly", "dept": "dairy"},
            {"name": "Powdered Sugar", "qty": 35, "unit": "g", "prep": "for Chantilly", "dept": "pantry"},
            {"name": "Vanilla Bean Paste", "qty": 5, "unit": "ml", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "9-inch pie dish", "type": "bakeware"},
            {"name": "Heavy bottom saucepan", "type": "cookware"},
            {"name": "Stand mixer with whisk attachment", "type": "appliance"}
        ],
        "miseEnPlace": [
            "Bake graham crust: mix crumbs, melted butter, 30g sugar; press into pie pan; bake at 350°F for 10 minutes; cool.",
            "Toast coconut shreds on sheet tray at 325°F for 6 minutes until golden brown; reserve 1/3 for top garnish.",
            "Separate egg yolks into clean stainless bowl."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat milk and coconut cream: In a heavy saucepan, bring whole milk and coconut cream to a gentle simmer (180°F/82°C).",
                "sensoryCue": "Fragrant tropical aroma fills kitchen as steam rises.",
                "scienceNote": "Coconut milk fatty acids (lauric acid) blend with dairy lipids, creating a rich multi-chain lipid profile.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Whisk eggs and cornstarch: Whisk egg yolks, 100g sugar, and cornstarch in bowl until pale and thick.",
                "sensoryCue": "Cornstarch dissolves into an airy, pale yellow slurry.",
                "scienceNote": "Coating starch granules in egg yolk and sugar prevents lumping when scalded with hot liquid.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Cook pastry cream: Temper egg mixture with 1 cup hot milk. Pour back into saucepan. Whisk vigorously over medium-low heat until it thickens and boils for 1 full minute (190°F/88°C).",
                "sensoryCue": "Custard turns from pourable liquid into thick, glossy pudding with volcanic bubbles.",
                "scienceNote": "Boiling for 1 minute is mandatory to deactivate alpha-amylase in egg yolks which would otherwise break down starch bonds.",
                "timerMins": 6
            },
            {
                "stepNum": 4,
                "text": "Mount butter & coconut: Remove from heat. Whisk in cold butter cubes, vanilla, and 80g toasted coconut. Pour into cooled graham crust. Press plastic wrap directly onto custard surface. Chill 4 hours until firmly set.",
                "sensoryCue": "Surface is protected from rubbery skin formation.",
                "scienceNote": "Cold butter fat crystals disperse into the hot custard, melting into an ultra-creamy emulsion.",
                "timerMins": 240
            },
            {
                "stepNum": 5,
                "text": "Top with Chantilly: Whip heavy cream, powdered sugar, and vanilla to medium-firm peaks. Pile high over chilled custard and scatter remaining toasted coconut on top.",
                "sensoryCue": "Billowy white peaks decorated with crunchy golden toasted coconut strands.",
                "scienceNote": "Powdered sugar contains cornstarch which stabilizes the whipped cream against weeping for 48 hours.",
                "timerMins": 10
            }
        ],
        "sensoryIndicators": {
            "visual": "Crisp golden graham crust with a thick layer of ivory coconut custard beneath a snowy mountain of Chantilly and toasted flakes",
            "tactile": "Spoon slices through airy whipped cream into luscious thick custard and crunchy cracker base",
            "aroma": "Toasted coconut, rich dairy cream, and vanilla bean perfume",
            "internalTemp": "Custard cooked to 190°F (88°C) to gelatinize starch"
        },
        "scienceNotes": "Starch gelatinization occurs when amylose and amylopectin absorb water and swell at 170°F-185°F. Egg yolk amylase enzyme digests starch molecules; boiling the custard for 60 seconds denatures the enzyme completely.",
        "troubleshooting": [
            {"issue": "Pastry cream turned runny after 24 hours", "solution": "Custard did not boil for the full 60 seconds; active amylase broke down the cornstarch gel."},
            {"issue": "Graham crust crumbled when slicing", "solution": "Press crumbs very firmly with the flat base of a measuring cup and bake 10m to caramelize butter sugars."}
        ],
        "substitutions": [
            {"original": "Graham Cracker Crumbs", "sub": "Speculoos / Biscoff Cookie Crumbs", "impact": "Adds spiced ginger-cinnamon warmth to the crust."}
        ],
        "flavorPairings": {
            "wine": "Late Harvest Riesling or Demi-Sec Champagne",
            "zeroProof": "Chilled pineapple-lemongrass iced tea with lime wheel"
        },
        "advancedTechnique": "Infuse the milk overnight with 3 cracked kaffir lime leaves before cooking the custard for a bright Southeast Asian contrast.",
        "storageAndReheating": "Store in refrigerator covered for up to 3 days. Do not freeze.",
        "nutritionEstimates": {"calories": 440, "protein": 6, "carbs": 44, "fat": 28},
        "relatedRecipes": ["rec-creme-brulee", "rec-panna-cotta", "rec-bourbon-pecan-pie"],
        "relatedTechniques": ["Crème pâtissière cooking", "Starch gelatinization", "Stabilized Chantilly piping"]
    },
    {
        "id": "rec-key-lime-pie",
        "title": "Authentic Florida Key Lime Pie with Torched Meringue",
        "cuisine": "American",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "beginner",
        "prepMins": 25,
        "cookMins": 15,
        "totalMins": 40,
        "yieldServings": 8,
        "heroImage": "assets/images/key-lime-pie.jpg",
        "summary": "True Floridian Key Lime Pie featuring the chemical reaction between acidic key lime juice, sweetened condensed milk, and egg yolks in a crisp buttery graham crust.",
        "dietary": ["vegetarian"],
        "sensoryRole": "Electric, puckering citrus acidity mellowed by lush sweetened condensed milk and toasted vanilla meringue.",
        "ingredients": [
            {"name": "Graham Cracker Crust (Pre-baked 9\")", "qty": 1, "unit": "shell", "prep": "cooled", "dept": "bakery"},
            {"name": "Sweetened Condensed Milk", "qty": 2, "unit": "cans (14 oz each)", "dept": "pantry"},
            {"name": "Fresh Key Lime Juice", "qty": 180, "unit": "ml", "prep": "or bottled Nellie & Joe's", "dept": "produce"},
            {"name": "Egg Yolks", "qty": 4, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Key Lime Zest", "qty": 10, "unit": "g", "prep": "finely microplaned", "dept": "produce"},
            {"name": "Heavy Cream or Meringue", "qty": 200, "unit": "ml", "prep": "for topping", "dept": "dairy"},
            {"name": "Fine Sea Salt", "qty": 1, "unit": "g", "prep": "pinch", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "9-inch pie dish", "type": "bakeware"},
            {"name": "Microplane zester", "type": "tool"},
            {"name": "Whisk and mixing bowl", "type": "tool"}
        ],
        "miseEnPlace": [
            "Zest key limes before juicing to capture fragrant citrus oils.",
            "Juice key limes through a fine strainer to remove seeds.",
            "Preheat oven to 350°F (175°C)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Whisk yolks and zest: In a large bowl, whisk egg yolks and microplaned lime zest on high speed for 2 minutes until pale and voluminous.",
                "sensoryCue": "Yolks lighten to pale yellow; floral lime oils burst with aromatics.",
                "scienceNote": "Microplaning ruptures flavedo oil glands, releasing limonene and citral directly into yolk lipids.",
                "timerMins": 2
            },
            {
                "stepNum": 2,
                "text": "Stir in condensed milk and lime juice: Whisk in sweetened condensed milk. Slowly pour in key lime juice and salt. Stir gently until completely combined.",
                "sensoryCue": "Mixture thickens almost immediately upon contact with the lime juice.",
                "scienceNote": "Acid-induced casein denaturation: The citric acid drops pH to ~4.5, causing milk casein proteins to aggregate and set the custard without high heat.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Bake gently: Pour filling into pre-baked graham cracker crust. Bake at 350°F (175°C) for 15 minutes to pasteurize egg yolks and set custard.",
                "sensoryCue": "Filling has set around edges with a slight wobble in center; no browning on surface.",
                "scienceNote": "Gentle heat completes egg vitellin coagulation without boiling or curdling the acid emulsion.",
                "timerMins": 15
            },
            {
                "stepNum": 4,
                "text": "Chill thoroughly: Cool to room temperature, then chill in refrigerator for minimum 4 hours. Top with whipped cream or torched meringue before serving.",
                "sensoryCue": "Custard turns firm, cool, and cleanly sliceable.",
                "scienceNote": "Chilling allows milk lipids and acid-protein complexes to solidify into a clean-cutting gel.",
                "timerMins": 240
            }
        ],
        "sensoryIndicators": {
            "visual": "Pale yellow-green custard slice with visible lime zest flecks in a golden graham shell",
            "tactile": "Creamy, mouth-coating curd with bright zesty snap",
            "aroma": "Pungent Key lime zest, sweet milk, and warm graham cracker",
            "internalTemp": "Baked to 155°F (68°C) in center"
        },
        "scienceNotes": "Key lime juice has a lower pH (2.1) and higher citric acid concentration than standard Persian limes. This high acidity curdles and denatures milk casein into a tender gel network, historically allowing Florida Keys residents to set the pie without ovens.",
        "troubleshooting": [
            {"issue": "Filling is watery", "solution": "Do not skip baking for 15m; egg yolks need heat to fully link with the acid-curdled casein."},
            {"issue": "Bitter metallic flavor", "solution": "Zested too deeply into the white bitter pith. Only grate the outermost green skin."}
        ],
        "substitutions": [
            {"original": "Key Lime Juice", "sub": "Equal parts Persian lime juice and fresh lemon juice", "impact": "Replicates Key lime tartness and floral acidity."}
        ],
        "flavorPairings": {
            "wine": "Sparkling Prosecco or Moscato d'Asti",
            "zeroProof": "Iced coconut water with fresh mint and crushed lime"
        },
        "advancedTechnique": "Top with Swiss meringue and scorch with a culinary blowtorch to create toasted marshmallow notes.",
        "storageAndReheating": "Refrigerate covered for up to 5 days. Excellent served semi-frozen in hot weather.",
        "nutritionEstimates": {"calories": 380, "protein": 7, "carbs": 52, "fat": 16},
        "relatedRecipes": ["rec-shattered-lemon-tart", "rec-coconut-cream-pie"],
        "relatedTechniques": ["Acid-induced protein denaturation", "Graham cracker crust blind baking", "Torching meringue"]
    },
    {
        "id": "rec-eclairs-chocolat",
        "title": "Éclairs au Chocolat (Crisp Choux Pastry & Chocolate Crème Pâtissière)",
        "cuisine": "French",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "advanced",
        "prepMins": 50,
        "cookMins": 35,
        "totalMins": 85,
        "yieldServings": 10,
        "heroImage": "assets/images/eclairs-chocolat.jpg",
        "summary": "The masterwork of French pastry: crisp, hollow choux shells piped to perfection, filled with rich dark chocolate pastry cream, and dipped in mirror-shine chocolate fondant glaze.",
        "dietary": ["vegetarian"],
        "sensoryRole": "Crisp, airy choux shell giving way to a cool, velvety dark chocolate custard explosion, capped with a glossy chocolate glaze.",
        "ingredients": [
            {"name": "Whole Milk", "qty": 125, "unit": "ml", "prep": "for choux", "dept": "dairy"},
            {"name": "Water", "qty": 125, "unit": "ml", "prep": "for choux", "dept": "pantry"},
            {"name": "Unsalted Butter", "qty": 100, "unit": "g", "prep": "cubed", "dept": "dairy"},
            {"name": "Granulated Sugar", "qty": 10, "unit": "g", "prep": "for choux", "dept": "pantry"},
            {"name": "Fine Salt", "qty": 3, "unit": "g", "prep": "for choux", "dept": "pantry"},
            {"name": "All-Purpose Flour (T55)", "qty": 150, "unit": "g", "prep": "sifted", "dept": "pantry"},
            {"name": "Whole Eggs", "qty": 4, "unit": "ea", "prep": "beaten, room temp", "dept": "dairy"},
            {"name": "Chocolate Pastry Cream (Crème Pâtissière)", "qty": 500, "unit": "g", "prep": "chilled in piping bag", "dept": "dairy"},
            {"name": "Dark Chocolate Mirror Glaze", "qty": 150, "unit": "g", "prep": "warmed to 95°F", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy saucepan for panade", "type": "cookware"},
            {"name": "Piping bag with French star tip (PF16)", "type": "tool"},
            {"name": "Perforated silicone baking mat (Air Mat)", "type": "bakeware"},
            {"name": "Stand mixer with paddle attachment", "type": "appliance"}
        ],
        "miseEnPlace": [
            "Sift flour onto parchment paper.",
            "Beat eggs together in a measuring pitcher.",
            "Fit piping bag with French star tip PF16.",
            "Preheat oven to 375°F (190°C) static heat."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Cook the panade: Bring milk, water, butter, sugar, and salt to a rolling boil in saucepan. Dump in all flour at once. Stir vigorously with wooden spoon over medium heat for 2 minutes until dough pulls cleanly away from pan walls and leaves a thin white starch film on the bottom.",
                "sensoryCue": "Dough comes together into a smooth, glossy ball; sizzling sound indicates water evaporation.",
                "scienceNote": "Pre-gelatinizing flour starch at 175°F allows it to absorb the egg moisture while creating an elastic gluten matrix.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Cool and beat in eggs: Transfer panade to stand mixer. Beat on low speed for 2 minutes to cool to 120°F. Gradually stream in beaten eggs in 4 additions until dough forms a smooth, glossy ribbon that drops from paddle in a sharp 'V' shape.",
                "sensoryCue": "Dough is shiny and cohesive, falling in a slow triangular curtain from the paddle.",
                "scienceNote": "Adding eggs below 130°F prevents cooking the egg proteins while emulsifying the butterfat.",
                "timerMins": 6
            },
            {
                "stepNum": 3,
                "text": "Pipe éclair shells: Pipe 12cm (5 inch) straight logs onto perforated baking mat using the star tip. Dust lightly with powdered sugar or cocoa butter spray to promote even rising.",
                "sensoryCue": "Uniform ribbed cylinders with crisp defined ridges.",
                "scienceNote": "The French star tip creates micro-grooves that expand uniformly, preventing éclairs from cracking or bursting irregularly.",
                "timerMins": 8
            },
            {
                "stepNum": 4,
                "text": "Bake without opening oven: Bake at 375°F (190°C) for 25 minutes until deeply puffed and golden brown. Reduce oven to 325°F (160°C) and bake 10 minutes more to dry interiors. Never open oven door during the first 25 minutes.",
                "sensoryCue": "Shells are rigid, light as feathers, and deep amber brown.",
                "scienceNote": "Trapped water flash-vaporizes into steam, inflating the hollow interior while egg proteins and starch coagulate to set the shell.",
                "timerMins": 35
            },
            {
                "stepNum": 5,
                "text": "Fill and glaze: Pierce 3 small holes in the bottom of each cooled shell. Pipe chocolate pastry cream into both ends until heavy. Dip the smooth top of each éclair into warm chocolate glaze; scrape excess with finger for a crisp edge.",
                "sensoryCue": "Éclair feels heavy and filled in hand; glossy mirror glaze reflects light like glass.",
                "scienceNote": "Glazing at 90°F-95°F ensures the chocolate fondant sets with high gloss without melting the interior cream.",
                "timerMins": 20
            }
        ],
        "sensoryIndicators": {
            "visual": "Straight, proud, glossy dark chocolate-topped cylinders with zero cracking",
            "tactile": "Crisp snap of pastry giving way to rich, luscious, cool cream",
            "aroma": "Browned butter pastry and bittersweet roasted cacao",
            "internalTemp": "Bake until hollow sound when tapped on bottom"
        },
        "scienceNotes": "Choux pastry relies entirely on steam for leavening (physical expansion of water turning to gas at 212°F expands volume by 1,600 times). Egg white albumen proteins provide the structural network that traps this steam.",
        "troubleshooting": [
            {"issue": "Éclairs collapsed after coming out of oven", "solution": "Oven door was opened prematurely, or shells were underbaked and retained too much internal moisture. Bake until deeply golden."},
            {"issue": "Shells cracked and warped irregularly", "solution": "Dough was piped with a plain round tip instead of a French star tip, or oven heat had excessive fan velocity."}
        ],
        "substitutions": [
            {"original": "French T55 Flour", "sub": "Unbleached All-Purpose Flour (11% protein)", "impact": "Standard all-purpose functions excellently; avoid cake flour."}
        ],
        "flavorPairings": {
            "wine": "Brut Champagne or Espresso",
            "zeroProof": "Cascara coffee cherry tea with sparkling mineral water"
        },
        "advancedTechnique": "Top choux logs with a 1mm strip of chocolate craquelin before baking for a crunchy, crackled exterior shell.",
        "storageAndReheating": "Best enjoyed within 6 hours of filling. Empty baked shells can be stored airtight for 3 days and recrisped at 350°F for 4 minutes.",
        "nutritionEstimates": {"calories": 310, "protein": 6, "carbs": 32, "fat": 18},
        "relatedRecipes": ["rec-paris-brest", "rec-creme-brulee", "rec-mousse-chocolat"],
        "relatedTechniques": ["Choux panade gelatinization", "Steam leavening", "Pastry cream injection"]
    },
    {
        "id": "rec-madeleines-commercy",
        "title": "Madeleines de Commercy (Brown Butter, Wild Honey & Lemon Thyme)",
        "cuisine": "French",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "beginner",
        "prepMins": 20,
        "cookMins": 12,
        "totalMins": 32,
        "yieldServings": 12,
        "heroImage": "assets/images/madeleines-commercy.jpg",
        "summary": "The timeless French teacake of Commercy: golden scallop-shelled cakes with an iconic pronounced 'bump' (la bosse), enriched with nutty beurre noisette, lemon zest, and wildflower honey.",
        "dietary": ["vegetarian"],
        "sensoryRole": "Crisp buttery edges, moist tender crumb, and floral lemon-honey warmth with toasted hazelnut aromas.",
        "ingredients": [
            {"name": "All-Purpose Flour", "qty": 100, "unit": "g", "prep": "sifted", "dept": "pantry"},
            {"name": "Baking Powder", "qty": 4, "unit": "g", "prep": "leavener", "dept": "pantry"},
            {"name": "Whole Eggs", "qty": 2, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Granulated Sugar", "qty": 80, "unit": "g", "dept": "pantry"},
            {"name": "Wildflower Honey", "qty": 20, "unit": "g", "dept": "pantry"},
            {"name": "Unsalted Butter (Browned)", "qty": 100, "unit": "g", "prep": "beurre noisette", "dept": "dairy"},
            {"name": "Lemon Zest", "qty": 1, "unit": "ea", "prep": "microplaned", "dept": "produce"},
            {"name": "Fresh Lemon Thyme", "qty": 1, "unit": "t", "prep": "finely chopped", "dept": "produce"},
            {"name": "Fine Sea Salt", "qty": 1, "unit": "g", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Traditional metal scalloped madeleine pan", "type": "bakeware"},
            {"name": "Pastry brush", "type": "tool"},
            {"name": "Piping bag", "type": "tool"}
        ],
        "miseEnPlace": [
            "Brown butter to beurre noisette; cool to lukewarm (100°F).",
            "Butter and flour madeleine pan thoroughly; chill pan in freezer for 20 minutes.",
            "Sift flour, baking powder, and salt together."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Whip eggs, sugar, and honey: In a bowl, whip eggs, sugar, honey, lemon zest, and lemon thyme on medium-high speed for 4 minutes until pale, thickened, and tripled in volume.",
                "sensoryCue": "Batter forms thick ribbons that slowly sink back into the bowl.",
                "scienceNote": "Honey contains fructose which acts as a humectant, keeping the baked madeleines moist.",
                "timerMins": 4
            },
            {
                "stepNum": 2,
                "text": "Fold dry ingredients & brown butter: Sift dry ingredients over the whipped eggs in two additions, gently folding with a spatula. Pour in the warm brown butter around the perimeter and fold until glossy and incorporated.",
                "sensoryCue": "Batter turns silky, shiny, and fragrant with nutty brown butter.",
                "scienceNote": "Folding butter around the edges prevents it from sinking to the bottom and deflating the egg foam.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Chill batter (Thermal Shock): Transfer batter to piping bag and refrigerate for at least 2 hours (or overnight).",
                "sensoryCue": "Batter firms up into a dense, cold paste.",
                "scienceNote": "Thermal shock: The extreme temperature difference between ice-cold batter and a 400°F oven creates rapid steam expansion that forces the center upward into the iconic 'bump'.",
                "timerMins": 120
            },
            {
                "stepNum": 4,
                "text": "Pipe and bake: Pipe batter into chilled madeleine molds (filling 3/4 full). Bake at 400°F (200°C) for 4 minutes until edges brown, then reduce oven to 350°F (175°C) and bake 6-7 minutes more.",
                "sensoryCue": "The center erupts into a dramatic rounded bump while the scallop ridges turn golden crisp.",
                "scienceNote": "The chilled outer shell sets against the hot metal pan while the center remains liquid longer, erupting upward through the path of least resistance.",
                "timerMins": 11
            },
            {
                "stepNum": 5,
                "text": "Unmold and serve warm: Immediately rap pan on counter to release madeleines. Cool scallop-side up on wire rack. Best eaten warm within 30 minutes of baking.",
                "sensoryCue": "Crisp scalloped crust with a feather-light interior that melts like warm sponge.",
                "scienceNote": "Butterfat at the surface stays crunchy immediately after baking before moisture equilibrates.",
                "timerMins": 2
            }
        ],
        "sensoryIndicators": {
            "visual": "Golden brown scalloped shell with crisp ridges and a proud, high rounded hump on the back",
            "tactile": "Crunchy exterior giving way to a warm, airy, tender crumb",
            "aroma": "Nutty brown butter, floral honey, and bright lemon thyme",
            "internalTemp": "Springs back immediately when center hump is lightly pressed"
        },
        "scienceNotes": "The famous madeleine hump is achieved through thermal shock and pan geometry. Freezing the pan and chilling the batter causes outer margins to set fast, forcing moisture vapor into the core where it pushes the uncoagulated batter skyward.",
        "troubleshooting": [
            {"issue": "No bump formed (flat madeleine)", "solution": "Batter was not chilled, or oven was not hot enough. Rest batter in fridge for minimum 2h before baking."},
            {"issue": "Madeleines stuck to the pan", "solution": "Ensure pan is brushed with melted butter, dusted with flour, and frozen before piping."}
        ],
        "substitutions": [
            {"original": "Lemon Thyme", "sub": "Pure vanilla bean or orange blossom water", "impact": "Classical floral profile instead of herbal citrus."}
        ],
        "flavorPairings": {
            "wine": "Earl Grey Tea or Sauternes",
            "zeroProof": "Freshly brewed Jasmine green tea with wildflower honey"
        },
        "advancedTechnique": "Dip the scalloped tips into tempered 70% dark chocolate or brush with a lemon glaze right out of the oven.",
        "storageAndReheating": "Best eaten fresh out of the oven. Can be stored airtight for 2 days; refresh in 350°F oven for 2 minutes.",
        "nutritionEstimates": {"calories": 145, "protein": 2, "carbs": 15, "fat": 9},
        "relatedRecipes": ["rec-caneles-bordeaux", "rec-paris-brest"],
        "relatedTechniques": ["Thermal shock baking", "Beurre noisette", "Egg foam folding"]
    },
    {
        "id": "rec-passionfruit-pavlova",
        "title": "Passionfruit & Berry Pavlova (Crisp Meringue Shell with Marshmallow Core)",
        "cuisine": "Australian / New Zealand",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "intermediate",
        "prepMins": 30,
        "cookMins": 90,
        "totalMins": 120,
        "yieldServings": 8,
        "heroImage": "assets/images/passionfruit-pavlova.jpg",
        "summary": "The show-stopping Antipodean celebration dessert: a delicate, crunchy snow-white meringue shell concealing a soft, pillowy marshmallow interior, crowned with tart passionfruit pulp and fresh berries.",
        "dietary": ["vegetarian", "gluten_free", "dairy_free"],
        "sensoryRole": "Crackling crisp meringue giving way to soft pillowy marshmallow, cut through by electric tart passionfruit seeds and lush berries.",
        "ingredients": [
            {"name": "Egg Whites", "qty": 4, "unit": "ea", "prep": "room temp, exactly 120g", "dept": "dairy"},
            {"name": "Superfine Castor Sugar", "qty": 220, "unit": "g", "prep": "fine sugar", "dept": "pantry"},
            {"name": "Cornstarch", "qty": 10, "unit": "g", "prep": "for marshmallow interior", "dept": "pantry"},
            {"name": "White Wine Vinegar", "qty": 5, "unit": "ml", "prep": "acid stabilizer", "dept": "pantry"},
            {"name": "Pure Vanilla Extract", "qty": 5, "unit": "ml", "dept": "pantry"},
            {"name": "Fresh Passionfruit", "qty": 4, "unit": "ea", "prep": "pulp and seeds scooped", "dept": "produce"},
            {"name": "Fresh Raspberries & Blackberries", "qty": 150, "unit": "g", "prep": "washed and dried", "dept": "produce"},
            {"name": "Fresh Mint Leaves", "qty": 8, "unit": "ea", "prep": "garnish", "dept": "produce"}
        ],
        "equipment": [
            {"name": "Stand mixer with balloon whisk", "type": "appliance"},
            {"name": "Baking sheet with silicone mat or parchment", "type": "bakeware"},
            {"name": "Offset spatula", "type": "tool"}
        ],
        "miseEnPlace": [
            "Wipe mixer bowl and whisk with paper towel dipped in vinegar to remove all trace lipids.",
            "Draw an 8-inch circle on parchment paper as a sizing guide.",
            "Preheat oven to 300°F (150°C)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Whip egg whites: Whip egg whites on medium speed until soft peaks form. Gradually rain in superfine sugar 1 tablespoon at a time over 6 minutes while continuing to whip on high speed.",
                "sensoryCue": "Meringue becomes blindingly white, dense, glossy, and silky smooth with no gritty sugar granules remaining.",
                "scienceNote": "Slow sugar addition ensures each grain dissolves into the water phase, creating a stable, high-viscosity protein film.",
                "timerMins": 8
            },
            {
                "stepNum": 2,
                "text": "Fold cornstarch and acid: Gently fold in sifted cornstarch, white wine vinegar, and vanilla extract using a silicone spatula.",
                "sensoryCue": "Meringue retains full volume and glossy sheen.",
                "scienceNote": "Acid lowers pH to tighten ovalbumin bonds, while cornstarch absorbs moisture to prevent sugar weeping and creates the pillowy marshmallow core.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Shape the meringue mound: Spoon meringue onto prepared parchment within the 8-inch circle. Use an offset spatula to smooth the sides upward and create a gentle crater/nest in the center.",
                "sensoryCue": "Graceful architectural swirls with a hollow center ready for fruit filling.",
                "scienceNote": "Upward fluting encourages structural stability and prevents the meringue from spreading flat.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "Low-temperature baking: Place into oven and immediately reduce temperature to 250°F (120°C). Bake for 75-80 minutes without opening the oven door.",
                "sensoryCue": "The shell is pale ivory and dry to the touch; no browning.",
                "scienceNote": "Baking at 250°F dehydrates the outer protein skin into a crisp shell while gently setting the interior starch-egg gel.",
                "timerMins": 80
            },
            {
                "stepNum": 5,
                "text": "Slow cooling (Anti-collapse): Turn off the oven and prop the door slightly open with a wooden spoon. Allow pavlova to cool inside the oven for at least 2 hours.",
                "sensoryCue": "Cooling gradually prevents thermal contraction shock and excessive cracking.",
                "scienceNote": "Rapid temperature drops cause interior air pockets to contract faster than the rigid shell can adapt, causing total collapse.",
                "timerMins": 120
            },
            {
                "stepNum": 6,
                "text": "Garnish and serve: Spoon lightly sweetened whipped cream into the center crater. Drizzle fresh passionfruit pulp and scatter raspberries, blackberries, and baby mint leaves.",
                "sensoryCue": "Dramatic contrast of snowy white meringue, golden passionfruit seeds, and crimson berries.",
                "scienceNote": "Serve immediately after topping; meringue absorbs moisture from whipped cream over time.",
                "timerMins": 5
            }
        ],
        "sensoryIndicators": {
            "visual": "A snow-white ruffled cloud topped with vibrant yellow-gold passionfruit seeds and ruby berries",
            "tactile": "Eggshell-thin crisp shatter yielding to warm marshmallow softness",
            "aroma": "Sweet vanilla sugar, tropical passionfruit acidity, and fresh berries",
            "internalTemp": "Completely cooled and dried exterior"
        },
        "scienceNotes": "The unique dual texture of a pavlova (crisp shell + marshmallow core) is made possible by the cornstarch and acid. Cornstarch swells and traps liquid water inside the egg matrix, preventing full dehydration in the center.",
        "troubleshooting": [
            {"issue": "Syrupy liquid weeping from bottom (syneresis)", "solution": "Sugar was not fully dissolved during whipping, or oven was too hot. Whip until sugar is completely smooth between fingertips."},
            {"issue": "Meringue turned brown/tan", "solution": "Oven temperature was too high. Bake at exactly 250°F and use an oven thermometer."}
        ],
        "substitutions": [
            {"original": "Fresh Passionfruit", "sub": "Lemon curd or passionfruit purée", "impact": "Equally bright and tart contrast against sweet meringue."}
        ],
        "flavorPairings": {
            "wine": "Sparkling Moscato d'Asti or Rosé Champagne",
            "zeroProof": "Sparkling hibiscus spritzer with crushed mint"
        },
        "advancedTechnique": "Fold 1 tsp of freeze-dried raspberry powder into half the meringue to create a stunning pink marble effect.",
        "storageAndReheating": "Unfilled pavlova shell can be stored in a dry airtight container for 2 days. Once assembled, serve within 2 hours.",
        "nutritionEstimates": {"calories": 260, "protein": 4, "carbs": 48, "fat": 8},
        "relatedRecipes": ["rec-shattered-lemon-tart", "rec-panna-cotta"],
        "relatedTechniques": ["French meringue aeration", "Starch-stabilized foam", "Slow thermal cooling"]
    },

    # BREAKFAST & BRUNCH
    {
        "id": "rec-french-rolled-omelette",
        "title": "Classical French Rolled Omelette (Omelette aux Fines Herbes)",
        "cuisine": "French",
        "category": "breakfast",
        "slot": "breakfast",
        "difficulty": "advanced",
        "prepMins": 10,
        "cookMins": 3,
        "totalMins": 13,
        "yieldServings": 1,
        "heroImage": "assets/images/french-rolled-omelette.jpg",
        "summary": "The ultimate test of a chef's hand: a flawless, pale golden almond-shaped omelette with zero browning, a creamy molten 'baveuse' center, and a mirror glaze of cold cultured butter.",
        "dietary": ["vegetarian", "gluten_free"],
        "sensoryRole": "Tender, velvety egg curds rolling like soft silk on the tongue, lifted by aromatic fines herbes and rich cultured butter.",
        "ingredients": [
            {"name": "Farm Fresh Large Eggs", "qty": 3, "unit": "ea", "prep": "room temp", "dept": "dairy"},
            {"name": "Cultured French Butter", "qty": 25, "unit": "g", "prep": "split into pan butter and cold butter", "dept": "dairy"},
            {"name": "Fresh Chives", "qty": 1, "unit": "T", "prep": "sliced 1/16\" thin", "dept": "produce"},
            {"name": "Fresh Chervil & Tarragon", "qty": 1, "unit": "t", "prep": "finely minced", "dept": "produce"},
            {"name": "Fine Sea Salt", "qty": 1.5, "unit": "g", "dept": "pantry"},
            {"name": "White Pepper", "qty": 0.5, "unit": "g", "prep": "freshly ground", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "8-inch nonstick or seasoned carbon steel skillet", "type": "cookware"},
            {"name": "High-heat silicone spatula or wooden chopsticks", "type": "tool"},
            {"name": "Fork and ceramic mixing bowl", "type": "tool"}
        ],
        "miseEnPlace": [
            "Beat eggs with salt, white pepper, and minced fines herbes using a fork until completely homogenous without whipping foam.",
            "Cut 10g cold butter into a small piece for surface glazing.",
            "Warm the serving plate so the omelette does not chill upon landing."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Melt butter to bubbling: Place skillet over medium-high heat. Add 15g butter. Swirl as it melts and foams, but do not let it brown.",
                "sensoryCue": "Butter foams violently with a sweet dairy aroma; no nutty browning.",
                "scienceNote": "Water in butter boils off, creating a steam vapor layer that prevents egg proteins from adhering to the pan surface.",
                "timerMins": 1
            },
            {
                "stepNum": 2,
                "text": "Pour eggs and shake pan vigorously: Pour beaten eggs into hot skillet. Instantly begin shaking the pan back and forth with your non-dominant hand while vigorously scrambling the eggs in rapid circles with a fork or spatula.",
                "sensoryCue": "Tiny, creamy micro-curds form across the entire surface within 30 seconds.",
                "scienceNote": "Rapid agitation breaks apart growing protein networks into microscopic curds instead of large, firm rubbery sheets.",
                "timerMins": 1
            },
            {
                "stepNum": 3,
                "text": "Smooth and bank the curds: When eggs are 80% cooked but still loose and creamy on top (baveuse), remove pan from heat. Use spatula to smooth the surface flat, then tilt pan forward at a 45° angle to gather the eggs against the far lip.",
                "sensoryCue": "Eggs form an even, glossy sheet banked along the curved edge of the skillet.",
                "scienceNote": "Residual thermal mass of the pan finishes cooking the exterior while leaving the interior core molten.",
                "timerMins": 1
            },
            {
                "stepNum": 4,
                "text": "Roll the omelette: Tap the heel of the pan handle with your fist to bounce the far edge of the omelette over itself. Fold the nearest edge over with your spatula to enclose the roll into a neat torpedo (cigar) shape.",
                "sensoryCue": "The eggs curl neatly into a seamless, smooth golden almond cylinder.",
                "scienceNote": "Surface egg proteins adhere under light pressure, sealing the molten core.",
                "timerMins": 1
            },
            {
                "stepNum": 5,
                "text": "Invert and butter glaze: Grasp the pan handle underhand. Invert the omelette seam-side down onto the warm plate. Immediately rub the remaining cold butter over the top to create a glistening mirror glaze.",
                "sensoryCue": "A gleaming, unblemished pale yellow torpedo with zero brown spots.",
                "scienceNote": "Cold butter melts on contact, creating an emulsion that prevents surface drying and oxidation.",
                "timerMins": 1
            }
        ],
        "sensoryIndicators": {
            "visual": "A seamless pale yellow oval with no brown speckles, glistening with a butter glaze and flecks of emerald chives",
            "tactile": "Soft and yielding to the fork, spilling a rich, jammy baveuse custard when slit open",
            "aroma": "Cultured butter, sweet fresh eggs, and peppery aniseed fines herbes",
            "internalTemp": "Interior core at 145°F-150°F (63°C-65°C)"
        },
        "scienceNotes": "Salting eggs 10 minutes prior to cooking allows sodium ions to dissolve into the yolk and white, neutralizing repulsive charges on ovalbumin proteins so they aggregate into softer, moister curds that weep less water.",
        "troubleshooting": [
            {"issue": "Omelette has brown spots or crust", "solution": "Heat was too high or butter browned before eggs went in. Cook over medium heat with constant motion."},
            {"issue": "Omelette tore while rolling", "solution": "Eggs were undercooked or stuck to pan. Ensure pan is seasoned or nonstick, and don't rush the initial curd formation."}
        ],
        "substitutions": [
            {"original": "Fines Herbes", "sub": "Pure Chives and Parsley", "impact": "Clean herbal flavor if chervil or French tarragon is unavailable."}
        ],
        "flavorPairings": {
            "wine": "Dry Champagne or Sancerre",
            "zeroProof": "Chilled sparkling mineral water with fresh cucumber and lemon peel"
        },
        "advancedTechnique": "Tuck a cylinder of softened goat cheese or Boursin into the center right before rolling for an ultra-luxurious molten core.",
        "storageAndReheating": "Must be eaten within 2 minutes of leaving the pan. Cannot be reheated.",
        "nutritionEstimates": {"calories": 310, "protein": 19, "carbs": 2, "fat": 25},
        "relatedRecipes": ["rec-eggs-benedict", "rec-shakshuka"],
        "relatedTechniques": ["Micro-curd scrambling", "Omelette rolling & banking", "Butter glazing"]
    },
    {
        "id": "rec-chilaquiles-rojos",
        "title": "Chilaquiles Rojos con Chorizo & Huevos Estrellados",
        "cuisine": "Mexican",
        "category": "breakfast",
        "slot": "breakfast",
        "difficulty": "beginner",
        "prepMins": 20,
        "cookMins": 15,
        "totalMins": 35,
        "yieldServings": 4,
        "heroImage": "assets/images/chilaquiles-rojos.jpg",
        "summary": "The ultimate Mexican breakfast: house-fried crispy corn tortilla triangles simmered in roasted salsa roja until semi-tender, topped with crispy spiced chorizo, sunny farm eggs, Mexican crema, and crumbled cotija.",
        "dietary": ["gluten_free"],
        "sensoryRole": "Crisp-chewy toasted corn tortillas soaked in smoky, charred tomato-chili salsa, contrasted by rich runny egg yolks and salty cotija.",
        "ingredients": [
            {"name": "Corn Tortillas (6-inch yellow)", "qty": 12, "unit": "ea", "prep": "quartered and separated", "dept": "bakery"},
            {"name": "House Charred Salsa Roja", "qty": 400, "unit": "ml", "prep": "roasted tomatoes, jalapeños, garlic", "dept": "pantry"},
            {"name": "Mexican Pork Chorizo", "qty": 200, "unit": "g", "prep": "crumbled & seared crisp", "dept": "meat"},
            {"name": "Farm Eggs", "qty": 4, "unit": "ea", "prep": "sunny side up", "dept": "dairy"},
            {"name": "Queso Cotija or Queso Fresco", "qty": 80, "unit": "g", "prep": "crumbled", "dept": "dairy"},
            {"name": "Crema Mexicana (or sour cream)", "qty": 60, "unit": "ml", "prep": "drizzled", "dept": "dairy"},
            {"name": "Fresh Cilantro Leaves", "qty": 15, "unit": "g", "prep": "rough chopped", "dept": "produce"},
            {"name": "Pickled Red Onions", "qty": 40, "unit": "g", "prep": "sliced", "dept": "pantry"},
            {"name": "Hass Avocado", "qty": 1, "unit": "ea", "prep": "sliced", "dept": "produce"}
        ],
        "equipment": [
            {"name": "Wide cast-iron skillet or rondeau", "type": "cookware"},
            {"name": "Deep frying pan or Dutch oven", "type": "cookware"},
            {"name": "Spider skimmer", "type": "tool"}
        ],
        "miseEnPlace": [
            "Cut corn tortillas into quarters and separate layers so they don't stick together.",
            "Brown chorizo in skillet over medium heat until crispy; drain on paper towels.",
            "Warm salsa roja in a wide sauté pan."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Fry tortilla chips (Totopos): Heat 2 inches of oil to 350°F (175°C). Fry tortilla quarters in batches for 90 seconds until golden and crisp. Drain on paper towels and toss immediately with fine sea salt.",
                "sensoryCue": "Tortillas bubble vigorously and turn pale gold with a hollow, brittle crunch.",
                "scienceNote": "Rapid moisture expulsion gelatinizes corn starch, locking a crisp porous cellular structure.",
                "timerMins": 6
            },
            {
                "stepNum": 2,
                "text": "Simmer in salsa: Bring warm salsa roja to a simmer in the wide skillet. Add crisp totopos and toss for exactly 45-60 seconds so each chip is coated in hot salsa while retaining inner crunch.",
                "sensoryCue": "Salsa sizzles and clings to every chip; edges soften slightly while centers stay firm.",
                "scienceNote": "Tossing briefly coats the chips without saturating the corn starch matrix, maintaining the prized textural contrast between crunchy and tender.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Fry eggs: In a separate pan, fry eggs in olive oil or butter over medium-high heat until whites are crispy and lacy around the edges with golden runny yolks.",
                "sensoryCue": "Egg whites bubble into crisp frills while yolks stay molten.",
                "scienceNote": "High heat caramelizes egg white proteins while leaving yolk lipids raw and fluid.",
                "timerMins": 3
            },
            {
                "stepNum": 4,
                "text": "Plate and garnish: Divide sauced tortilla chips onto warm plates. Top with crisp chorizo, a fried egg, generous crumbles of cotija, zigzag drizzles of crema, sliced avocado, pickled red onions, and cilantro.",
                "sensoryCue": "A colorful mountain of red, white, green, and golden yellow with steaming aromas.",
                "scienceNote": "Acid from pickled onions and lactic acid from cotija balance the richness of fried corn chips and chorizo.",
                "timerMins": 4
            }
        ],
        "sensoryIndicators": {
            "visual": "Vibrant heap of brick-red sauced tortilla triangles crowned with a glistening sunny egg, white crema ribbons, and green cilantro",
            "tactile": "Satisfying contrast between crisp chip corners and tender sauce-soaked centers",
            "aroma": "Charred roasted tomatoes, smoky chipotle, toasted corn masa, and savory spiced pork",
            "internalTemp": "Served piping hot immediately after tossing"
        },
        "scienceNotes": "Nixtamalization of corn (soaking kernels in alkaline calcium hydroxide) frees bound niacin, cross-links hemicellulose, and produces distinctive calcium pectate bonds that give corn tortillas their aroma and crisp frying capability.",
        "troubleshooting": [
            {"issue": "Chips turned into soggy mush", "solution": "Chips simmered in sauce too long. Toss in hot salsa for no more than 45 seconds before plating immediately."},
            {"issue": "Chips are leathery", "solution": "Oil temperature was below 350°F during frying. Maintain 350°F so oil does not soak in."}
        ],
        "substitutions": [
            {"original": "Salsa Roja", "sub": "Salsa Verde (tomatillo and serrano)", "impact": "Yields classic Chilaquiles Verdes with tangy, bright acidity."}
        ],
        "flavorPairings": {
            "wine": "Mexican Michelada or Crisp Corona with Lime",
            "zeroProof": "Fresh Agua de Horchata with toasted canela"
        },
        "advancedTechnique": "Sear the tortillas directly on a dry comal or griddle before frying to develop deep charred roasted corn notes.",
        "storageAndReheating": "Must be assembled fresh. Store salsa, chips, and chorizo separately for up to 3 days.",
        "nutritionEstimates": {"calories": 580, "protein": 24, "carbs": 48, "fat": 34},
        "relatedRecipes": ["rec-shakshuka", "rec-eggs-benedict"],
        "relatedTechniques": ["Tortilla chip frying", "Nixtamalized starch hydration", "Salsa balancing"]
    },

    # APPETIZERS & GLOBAL SPECIALTIES
    {
        "id": "rec-salmon-aburi-press",
        "title": "Salmon Aburi Pressed Sushi (Oshizushi with Miso Mayo & Torched Jalapeño)",
        "cuisine": "Japanese",
        "category": "appetizer",
        "slot": "appetizer",
        "difficulty": "intermediate",
        "prepMins": 30,
        "cookMins": 5,
        "totalMins": 35,
        "yieldServings": 4,
        "heroImage": "assets/images/salmon-aburi-press.jpg",
        "summary": "Vancouver's iconic pressed sushi: seasoned sushi rice molded in a wooden oshibako box, draped with sashimi-grade Atlantic salmon, glazed with dashi-miso mayo, and seared table-side with a blowtorch over binchotan.",
        "dietary": ["gluten_free", "dairy_free"],
        "sensoryRole": "Warm, smoky torched salmon fat melting over cool, seasoned vinegar rice with sweet umami miso glaze and spicy jalapeño kick.",
        "ingredients": [
            {"name": "Sushi Rice (Cooked & seasoned with sushi vinegar)", "qty": 300, "unit": "g", "prep": "body temperature (98°F)", "dept": "pantry"},
            {"name": "Sashimi-Grade Atlantic Salmon Filet", "qty": 150, "unit": "g", "prep": "sliced 1/8\" on bias", "dept": "seafood"},
            {"name": "Dashi-Miso Mayonnaise", "qty": 30, "unit": "g", "prep": "mayo, white miso, dashi powder", "dept": "pantry"},
            {"name": "Fresh Jalapeño Pepper", "qty": 1, "unit": "ea", "prep": "sliced into razor-thin rounds", "dept": "produce"},
            {"name": "Sweet Soy Glaze (Nikiri / Unagi Sauce)", "qty": 20, "unit": "ml", "prep": "for finishing", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Wooden oshibako (pressed sushi mold) or cling film lined rectangular loaf pan", "type": "tool"},
            {"name": "High-powered culinary butane blowtorch", "type": "tool"},
            {"name": "Sharp yanagiba or chef knife", "type": "tool"}
        ],
        "miseEnPlace": [
            "Cook short-grain sushi rice and season with seasoned rice vinegar; hold at body temperature.",
            "Slice salmon across the grain into thin 1/8-inch slices.",
            "Thinly slice jalapeño into translucent rounds on a mandoline."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Layer rice in mold: Line oshibako with plastic wrap. Press 150g of warm seasoned sushi rice evenly into the base using moist hands, leveling the surface.",
                "sensoryCue": "Rice grains are distinct, glossy, and evenly distributed without being mashed into paste.",
                "scienceNote": "Sushi vinegar seasoning (pH ~4.0) lowers starch Retrogradation while seasoning every starch granule.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Layer salmon and press: Overlap thin salmon slices across the rice in an even sheet. Place wooden lid on top and press firmly with both hands for 10 seconds to compress the layers.",
                "sensoryCue": "Salmon adheres cleanly to the rice block.",
                "scienceNote": "Gentle mechanical compression binds amylose starch molecules to the salmon surface without crushing rice grains.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Slice into bite-sized rectangles: Remove press lid and lift the block out. Using a damp, razor-sharp knife, slice through the salmon and rice block into 6 equal rectangular pieces (approx. 1.25\" x 2\"). Wipe blade with damp cloth between cuts.",
                "sensoryCue": "Clean, sharp edges with clear division between white rice and coral salmon.",
                "scienceNote": "Wiping knife with water lubricates the blade, preventing sticky surface amylose from tearing the salmon.",
                "timerMins": 4
            },
            {
                "stepNum": 4,
                "text": "Dollop mayo and jalapeño: Dab a small pea-sized dollop of dashi-miso mayo onto each salmon slice. Crown with a razor-thin jalapeño round.",
                "sensoryCue": "Evenly decorated pieces arranged on a fireproof stoneware platter.",
                "scienceNote": "Mayonnaise lipids blister and caramelize rapidly under high flame, adding smoky charred complexity.",
                "timerMins": 2
            },
            {
                "stepNum": 5,
                "text": "Aburi flame torching: Ignite culinary blowtorch to a sharp blue flame. Sweep flame 3 inches above the sushi pieces for 6-8 seconds until salmon edges curl, fat sizzles, and mayonnaise caramelizes with golden spots.",
                "sensoryCue": "Sizzling fat pops; aroma of wood smoke and charred salmon fills the air.",
                "scienceNote": "Flame sear triggers instant Maillard browning and renders surface polyunsaturated omega-3 fatty acids without warming the cold rice underneath.",
                "timerMins": 1
            }
        ],
        "sensoryIndicators": {
            "visual": "Caramelized charred salmon with sizzling mayo bubbles and charred green jalapeño ring on a neat rice rectangle",
            "tactile": "Warm, buttery melt-in-the-mouth salmon contrasting with cool, chewy, vinegar-seasoned rice",
            "aroma": "Charred ocean fat, umami dashi smoke, and sharp jalapeño capsicum",
            "internalTemp": "Salmon surface warm (130°F); interior core remains rare and cool"
        },
        "scienceNotes": "Aburi (meaning 'flame-seared') relies on the rapid temperature gradient of an open torch flame (>2,000°F). It renders low-melting-point fish fats on the exterior 1mm, creating smoky volatile pyrazines while the insulating sushi rice keeps the fish interior buttery and raw.",
        "troubleshooting": [
            {"issue": "Rice fell apart during cutting", "solution": "Rice was too cold when pressed or not compressed firmly enough. Use body-temperature rice and press with steady pressure."},
            {"issue": "Fish cooked all the way through", "solution": "Torch was held too close or too long. Sweep the flame quickly across the surface in continuous fluid passes."}
        ],
        "substitutions": [
            {"original": "Atlantic Salmon", "sub": "Hamachi (Yellowtail) or Saku Ahi Tuna", "impact": "High-fat fish like Hamachi torched aburi-style is extraordinary."}
        ],
        "flavorPairings": {
            "wine": "Dry Junmai Ginjo Sake or Chablis",
            "zeroProof": "Iced Yuzu Sencha with cucumber ribbon"
        },
        "advancedTechnique": "Place a thin piece of binchotan (white Japanese charcoal) on a metal rack above the sushi while torching to impart authentic charcoal aroma.",
        "storageAndReheating": "Must be consumed immediately after torching. Never refrigerate torched sushi.",
        "nutritionEstimates": {"calories": 340, "protein": 18, "carbs": 42, "fat": 11},
        "relatedRecipes": ["rec-citrus-ahi-tuna", "rec-spicy-tuna-crispy-rice"],
        "relatedTechniques": ["Oshizushi pressing", "Aburi torching", "Sushi rice acidification"]
    },
    {
        "id": "rec-potato-pave",
        "title": "Classical Potato Pavé (Crisp Layered Duck-Fat Potato Cake with Thyme)",
        "cuisine": "French",
        "category": "dinner",
        "slot": "side",
        "difficulty": "advanced",
        "prepMins": 45,
        "cookMins": 90,
        "totalMins": 135,
        "yieldServings": 6,
        "heroImage": "assets/images/potato-pave.jpg",
        "summary": "Thomas Keller's legendary French Laundry classic: hundreds of paper-thin mandoline-sliced Yukon gold potatoes layered with clarified butter and fresh thyme, slow-baked, compressed under weights for 24 hours, cut into neat geometric cobblestones, and pan-seared to a glass-shattering crispness.",
        "dietary": ["gluten_free"],
        "sensoryRole": "Mirror-smooth golden crackling exterior giving way to fifty gossamer layers of melting, buttery, herbaceous potato.",
        "ingredients": [
            {"name": "Yukon Gold Potatoes", "qty": 1500, "unit": "g", "prep": "peeled, squared", "dept": "produce"},
            {"name": "Clarified Butter or Duck Fat", "qty": 150, "unit": "g", "prep": "melted", "dept": "dairy"},
            {"name": "Fresh Thyme Leaves", "qty": 2, "unit": "t", "prep": "finely chopped", "dept": "produce"},
            {"name": "Fine Sea Salt", "qty": 12, "unit": "g", "dept": "pantry"},
            {"name": "Freshly Ground White Pepper", "qty": 2, "unit": "g", "dept": "pantry"},
            {"name": "High-Smoke Neutral Oil", "qty": 60, "unit": "ml", "prep": "for searing", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Japanese Benriner mandoline slicer", "type": "tool"},
            {"name": "Standard 8.5 x 4.5 inch metal loaf pan", "type": "bakeware"},
            {"name": "Cardboard press cut to size and heavy canned goods/weights", "type": "tool"},
            {"name": "Cast-iron skillet", "type": "cookware"}
        ],
        "miseEnPlace": [
            "Line loaf pan with parchment paper, leaving generous overhang on all 4 sides.",
            "Peel potatoes and square off sides to fit the width of the loaf pan.",
            "Preheat oven to 350°F (175°C)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Mandoline slice: Using a mandoline set to 1mm (1/16\"), slice potatoes lengthwise into razor-thin translucent planks. Do not soak in water—the starch is essential to glue the layers together.",
                "sensoryCue": "Translucent potato ribbons showing light through their surfaces.",
                "scienceNote": "Unwashed potatoes retain surface amylose and amylopectin granules which act as an edible cement between layers upon baking.",
                "timerMins": 15
            },
            {
                "stepNum": 2,
                "text": "Toss with fat and seasoning: Toss potato slices with melted clarified butter (or duck fat), chopped thyme, sea salt, and white pepper until every slice is coated in a thin sheen.",
                "sensoryCue": "Glossy potato sheets coated evenly with herb flecks.",
                "scienceNote": "Clarified butter removes milk solids and water, allowing potato starch to absorb pure butter lipids.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Layer into loaf pan: Layer potato slices into the prepared loaf pan one by one, overlapping each layer slightly and pressing down firmly with your fingers every 5 layers to eliminate trapped air pockets. Build until pan is filled.",
                "sensoryCue": "A dense, tightly packed brick of hundreds of potato layers.",
                "scienceNote": "Eliminating air voids ensures direct conduction between potato surfaces for seamless starch fusion.",
                "timerMins": 25
            },
            {
                "stepNum": 4,
                "text": "Bake until tender: Fold parchment overhang over top. Cover tightly with aluminum foil. Bake at 350°F (175°C) for 1 hour 30 minutes until a cake tester or paring knife glides through the center with zero resistance.",
                "sensoryCue": "Kitchen fills with the rich perfume of roasted potato and thyme.",
                "scienceNote": "Prolonged baking gelatinizes potato starch while softening insoluble pectin cell wall glue into soluble pectic acid.",
                "timerMins": 90
            },
            {
                "stepNum": 5,
                "text": "Weight and compress for 24 hours: Remove foil. Place a piece of cardboard wrapped in foil directly over the hot potatoes. Top with 5-8 lb of heavy weights (canned food or brick). Cool to room temperature, then refrigerate under weight for 24 hours.",
                "sensoryCue": "Potatoes compress into a solid, impenetrable chilled brick.",
                "scienceNote": "Starch retrogradation: As the gelatinized starch cools under mechanical pressure, amylose molecules recrystallize into an unbreakable laminated brick.",
                "timerMins": 1440
            },
            {
                "stepNum": 6,
                "text": "Trim, portion, and sear: Unmold the solid brick onto a cutting board. Trim edges cleanly with a sharp chef knife, then slice into 1.5\" x 1.5\" cubes (pavés). Heat oil in cast-iron skillet over medium-high heat. Sear pavés on top and bottom faces for 3-4 minutes per side until deeply golden and shatteringly crisp.",
                "sensoryCue": "Deep golden glass-like crust sizzles furiously; edges crisp like potato chips.",
                "scienceNote": "Direct contact heat on the flat retrograded surface produces an intense Maillard reaction, contrasting with the tender steaming interior.",
                "timerMins": 12
            }
        ],
        "sensoryIndicators": {
            "visual": "Geometric golden-brown cube displaying fifty micro-layers of potato on its cut flanks",
            "tactile": "Glass-like crackle on first bite, giving way to creamy potato velvet",
            "aroma": "Clarified butter, roasted potato chips, and savory fresh thyme",
            "internalTemp": "Steaming hot at 165°F (74°C) inside after pan searing"
        },
        "scienceNotes": "Potato pavé (French for 'cobblestone') demonstrates retrograded starch lamination. Cold compression forces gelatinized starch chains to interlock, allowing a delicate vegetable preparation to be sliced cleanly with sharp right angles and seared without disintegrating.",
        "troubleshooting": [
            {"issue": "Layers separated during searing", "solution": "Potatoes were washed in water (removing starch), or weights were insufficient during cooling. Do not wash potato slices, and weight with 5+ lbs."},
            {"issue": "Core is tough/hard", "solution": "Underbaked in initial oven phase. Ensure paring knife enters without any resistance before weighting."}
        ],
        "substitutions": [
            {"original": "Duck Fat", "sub": "Ghee (Clarified Butter)", "impact": "Equally high smoke point and luxurious rich dairy profile."}
        ],
        "flavorPairings": {
            "wine": "Cabernet Sauvignon or Northern Rhône Syrah",
            "zeroProof": "Chilled sparkling apple cider with a sprig of fresh rosemary"
        },
        "advancedTechnique": "Brush the seared faces with white truffle oil and sprinkle with Maldon smoked sea salt flakes right before plating.",
        "storageAndReheating": "Unseared cubes can be stored in refrigerator for up to 5 days. Sear directly from cold for optimal texture.",
        "nutritionEstimates": {"calories": 320, "protein": 4, "carbs": 38, "fat": 18},
        "relatedRecipes": ["rec-pan-seared-ribeye", "rec-peppercorn-sauce"],
        "relatedTechniques": ["Mandoline precision slicing", "Starch retrogradation lamination", "Cast-iron pan searing"]
    }
]

def merge_recipes():
    with open('data-recipes.js', 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'window\.MASTER_RECIPES\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not m:
        print("Error: Could not find window.MASTER_RECIPES in data-recipes.js")
        return

    existing = json.loads(m.group(1))
    existing_ids = {r['id'] for r in existing}
    added = 0

    for r in NEW_RECIPES:
        if r['id'] not in existing_ids:
            existing.append(r)
            existing_ids.add(r['id'])
            added += 1

    updated_js = re.sub(
        r'window\.MASTER_RECIPES\s*=\s*\[.*?\];',
        'window.MASTER_RECIPES = ' + json.dumps(existing, indent=2, ensure_ascii=False) + ';',
        content,
        flags=re.DOTALL
    )

    with open('data-recipes.js', 'w', encoding='utf-8') as f:
        f.write(updated_js)

    print(f"Merged {added} new showcase recipes into data-recipes.js. Total recipes: {len(existing)}")

if __name__ == '__main__':
    merge_recipes()
