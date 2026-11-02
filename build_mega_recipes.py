# build_mega_recipes.py
# Expands L'Atelier with 31 master recipes across Desserts, Global Savory, Breakfast/Brunch, and Breads.
# All recipes strictly conform to the 28-field schema.

import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

MEGA_RECIPES = [
    {
        "id": "rec-basque-cheesecake",
        "title": "Basque Burnt Cheesecake (Tarta de Queso de San Sebastián)",
        "cuisine": "Spanish / Basque",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 20,
        "cookMins": 50,
        "totalMins": 70,
        "yieldServings": 10,
        "heroImage": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=1200&q=80",
        "summary": "The iconic crustless cheesecake of La Viña in San Sebastián. Baked at intense 425°F heat to develop an intensely caramelized, mahogany-blackened exterior while preserving a luxuriantly runny, custardy molten center.",
        "dietary": ["Vegetarian", "Gluten-Friendly Option"],
        "sensoryRole": "Rich, caramelized, dairy-forward decadence with bitter-sweet Maillard crust and silky cream center",
        "ingredients": [
            {"name": "Philadelphia Cream Cheese", "qty": 900, "unit": "g", "prep": "softened at room temperature", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 350, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Large Eggs", "qty": 6, "unit": "whole", "prep": "room temperature (approx 300g)", "dept": "Dairy & Fats"},
            {"name": "Heavy Cream (36-40% Milkfat)", "qty": 450, "unit": "ml", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Unbleached Pastry Flour", "qty": 20, "unit": "g", "prep": "sifted (or cornstarch for gluten-free)", "dept": "Baking & Pantry"},
            {"name": "Madagascar Vanilla Bean Paste", "qty": 10, "unit": "ml", "prep": "pure extract or paste", "dept": "Spices & Botanicals"},
            {"name": "Flaky Sea Salt (Fleur de Sel)", "qty": 4, "unit": "g", "prep": "fine pinch", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "10-inch Springform Pan (or 9-inch Deep Cake Pan)", "type": "Bakeware"},
            {"name": "Parchment Paper (2 large sheets crumpled)", "type": "Baking Supply"},
            {"name": "Stand Mixer with Paddle Attachment (or large bowl & whisk)", "type": "Small Appliance"},
            {"name": "Digital Probe Thermometer", "type": "Precision Tool"}
        ],
        "miseEnPlace": [
            "Ensure cream cheese, eggs, and heavy cream are at 68-72°F (room temp) for at least 2 hours before blending to prevent curdling or lumps.",
            "Preheat oven to 425°F (220°C) with rack in center position.",
            "Grease the 10-inch springform pan lightly with butter. Press two overlapping sheets of crumpled parchment paper into the pan, allowing 2 inches of paper to overhang the rim."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "In the bowl of a stand mixer fitted with the paddle attachment, beat the softened cream cheese and sugar on medium-low speed for 3 to 4 minutes until completely smooth, satiny, and free of lumps. Scrape down bowl sides and paddle thoroughly.",
                "sensoryCue": "Cream cheese looks glossy, ivory, and fully homogenized without trapping excess aerated bubbles.",
                "scienceNote": "We use the paddle instead of a whisk to minimize air incorporation; excess air pockets cause soufflé-like rising followed by violent collapse and cracked surfaces.",
                "timerMins": 4
            },
            {
                "stepNum": 2,
                "text": "Add eggs one at a time on low speed, beating until each egg is fully emulsified before adding the next. Stop and scrape down bottom of bowl.",
                "sensoryCue": "Batter turns pale primrose yellow and ribbons off the paddle.",
                "scienceNote": "Egg yolk lecithin naturally encapsulates the dispersed fat globules from the cream cheese, building a stable colloidal suspension.",
                "timerMins": 3
            },
            {
                "stepNum": 3,
                "text": "Add heavy cream, vanilla paste, and fine sea salt. Mix on low speed for 30 seconds. Sift in the 20g pastry flour and mix just until barely incorporated (15-20 seconds). Tap bowl firmly on counter 3 times to dislodge micro-bubbles.",
                "sensoryCue": "Fluid, velvety batter resembles pancake batter consistency.",
                "scienceNote": "The minimal flour (under 2%) provides just enough amylose/amylopectin starch network to bind free whey water without masking the dairy silkiness.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Pour the batter into the prepared parchment-lined pan. Bake at 425°F (220°C) for 50 to 55 minutes, until the top is deeply caramelized to a dark chestnut-black tone, the edges are puffed and set, but the center 3 inches still jiggles dramatically like loose custard when gently nudged.",
                "sensoryCue": "Dark burnished mahogany crown with aroma of toasted milk solids and caramel; center wobbles like panna cotta.",
                "scienceNote": "High radiant heat triggers rapid non-enzymatic browning (Maillard reaction between milk proteins and lactose/sucrose) on the surface while thermal conduction to the dense interior remains slow, stopping core coagulated temperature at 150-155°F.",
                "timerMins": 52
            },
            {
                "stepNum": 5,
                "text": "Transfer pan to a wire cooling rack and let cool at room temperature undisturbed for 4 hours. As it cools, the puffed exterior gently settles. For a molten center, serve at room temperature. For a firmer custard, chill 4 hours then bring back to room temp 45 minutes prior to slicing.",
                "sensoryCue": "Creased rustic parchment folds release cleanly; knife glides through molten core.",
                "scienceNote": "As cooling progresses, egg proteins stabilize into a delicate gel matrix without expelling water (syneresis).",
                "timerMins": 240
            }
        ],
        "sensoryIndicators": {
            "aroma": "Burnished caramel, toasted milk powder, warm vanilla bean, slight lactic tang",
            "texture": "Caramelized tender top skin transitioning into silky, ultra-creamy, molten core",
            "finish": "Balanced richness cut by gentle acidity and mineral sea salt flakes"
        },
        "scienceNotes": "Unlike New York style cheesecakes which rely on low-and-slow 225°F water baths to avoid any browning, Basque cheesecake intentionally leverages extreme heat gradient. The 425°F convection current browns the surface through lactose caramelization and Maillard interactions before the center eggs can fully denature past 160°F, creating a gradient from set cake to molten cream.",
        "troubleshooting": {
            "Too dry or cakey": "Overbaked. Remove from oven when center 3-4 inches still wobbles violently; it will carry-over cook as it rests.",
            "Batter has white lumps": "Cream cheese was too cold when beaten. Cream cheese must be at least 70°F before starting.",
            "Burnt taste without sweetness": "Oven temperature was calibrated too high or sugar crystallized; use castor sugar for even dispersion."
        },
        "substitutions": [
            {"ingredient": "Pastry Flour", "substitute": "Cornstarch or Sweet Rice Flour", "ratio": "1:1 for 100% gluten-free"},
            {"ingredient": "Heavy Cream", "substitute": "Double Cream (48%) mixed with whole milk", "ratio": "350ml double cream + 100ml milk"}
        ],
        "flavorPairings": ["Pedro Ximénez Sherry", "Espresso Macchiato", "Tart Blackberry Compote", "Roasted Figs"],
        "advancedTechnique": "Flambéed Cognac or Pedro Ximénez reduction brushed onto the warm crust right out of the oven for aromatic depth.",
        "storageAndReheating": "Store tightly wrapped in parchment in refrigerator up to 5 days. Do not freeze (breaks custard emulsion). Always bring to room temp 1 hour before serving.",
        "nutritionEstimates": {"calories": 480, "protein": 8, "carbs": 32, "fat": 36},
        "relatedRecipes": ["rec-creme-brulee", "rec-panna-cotta", "rec-tarte-tatin"],
        "relatedTechniques": ["Maillard caramelization gradient", "Egg protein emulsification", "Crustless high-heat baking"]
    },
    {
        "id": "rec-ny-cheesecake",
        "title": "Classical New York Cheesecake with Graham Crust & Sour Cream Crown",
        "cuisine": "American / Classical",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 75,
        "totalMins": 105,
        "yieldServings": 12,
        "heroImage": "https://images.unsplash.com/photo-1508737027454-e6454ef45afd?auto=format&fit=crop&w=1200&q=80",
        "summary": "The definitive skyscraper New York cheesecake: dense, satiny, ultra-smooth cream cheese custard on a spiced par-baked Graham cracker crust, crowned with a tangy sour cream glaze baked in a gentle water bath.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Ultra-dense, velvety, tang-balanced classic dessert with crunchy buttery spiced base",
        "ingredients": [
            {"name": "Graham Cracker Crumbs", "qty": 200, "unit": "g", "prep": "finely pulverized", "dept": "Baking & Pantry"},
            {"name": "Unsalted Butter", "qty": 85, "unit": "g", "prep": "melted", "dept": "Dairy & Fats"},
            {"name": "Brown Sugar", "qty": 30, "unit": "g", "prep": "packed", "dept": "Baking & Pantry"},
            {"name": "Full-Fat Cream Cheese (Block)", "qty": 1000, "unit": "g", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Granulated White Sugar", "qty": 260, "unit": "g", "prep": "superfine", "dept": "Baking & Pantry"},
            {"name": "Sour Cream", "qty": 240, "unit": "g", "prep": "divided: 160g in batter, 80g for crown", "dept": "Dairy & Fats"},
            {"name": "Large Eggs", "qty": 4, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Egg Yolks", "qty": 2, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Cornstarch", "qty": 25, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Fresh Lemon Juice & Zest", "qty": 20, "unit": "ml", "prep": "freshly microplaned", "dept": "Produce"},
            {"name": "Vanilla Bean Extract", "qty": 15, "unit": "ml", "prep": "pure bourbon vanilla", "dept": "Spices & Botanicals"}
        ],
        "equipment": [
            {"name": "9-inch or 10-inch Leakproof Springform Pan", "type": "Bakeware"},
            {"name": "Heavy-Duty Wide Aluminum Foil", "type": "Baking Supply"},
            {"name": "Roasting Pan (for Bain-Marie water bath)", "type": "Bakeware"},
            {"name": "Food Processor or Stand Mixer", "type": "Small Appliance"}
        ],
        "miseEnPlace": [
            "Bring cream cheese, sour cream, and eggs to exactly 70°F room temperature.",
            "Preheat oven to 350°F (175°C) for crust par-bake; prepare kettle with 2 liters of boiling water for water bath.",
            "Wrap the outside bottom and sides of the springform pan with 3 layers of heavy-duty aluminum foil to create a 100% watertight seal."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Combine Graham crumbs, melted butter, and brown sugar. Press firmly into bottom and 1 inch up the sides of the springform pan using flat bottom of a glass. Par-bake at 350°F (175°C) for 10 minutes. Cool completely. Lower oven to 300°F (150°C).",
                "sensoryCue": "Crust is fragrant, nutty, toasted golden brown, and set.",
                "scienceNote": "Par-baking gelatinizes starches in the crust and melts the butter-sugar binder, creating a hydrophobic moisture barrier against the wet cheesecake batter.",
                "timerMins": 10
            },
            {
                "stepNum": 2,
                "text": "Beat cream cheese and granulated sugar on low speed for 3 minutes until perfectly creamy and free of granules. Blend in cornstarch, vanilla, lemon zest, and lemon juice. Add sour cream (160g) and mix on low.",
                "sensoryCue": "Silky, ivory emulsion with micro-flecks of lemon zest.",
                "scienceNote": "Cornstarch buffers egg protein coagulation, raising the curdling threshold temperature and preventing syneresis (weeping).",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Add whole eggs and extra yolks one at a time, mixing on slowest speed just until incorporated. Do not whip. Pour batter over cooled crust.",
                "sensoryCue": "Heavy, luxurious batter levels smoothly into pan.",
                "scienceNote": "Extra yolks increase phospholipid lecithin and fat content, yielding dense New York mouthfeel rather than fluffy sponge.",
                "timerMins": 3
            },
            {
                "stepNum": 4,
                "text": "Place foil-wrapped springform into the large roasting pan. Pour boiling water into roasting pan until it reaches halfway up sides of springform. Bake at 300°F (150°C) for 65-75 minutes until edges are set but center 2 inches has a gentle slow tremor.",
                "sensoryCue": "Pale ivory surface with no cracking, gentle wobble in center.",
                "scienceNote": "Bain-marie water bath caps ambient pan temperature at 212°F (100°C), eliminating edge scorching and preventing temperature-shock fissure cracks.",
                "timerMins": 70
            },
            {
                "stepNum": 5,
                "text": "Whisk remaining 80g sour cream with 15g sugar and 1 tsp lemon juice. Spread gently over warm top. Turn oven off, crack door open 2 inches with a wooden spoon, and leave cheesecake inside to cool slowly for 1 hour. Chill in refrigerator at least 8 hours before unmolding.",
                "sensoryCue": "Glossy porcelain-smooth sour cream crown; clean slice with hot knife.",
                "scienceNote": "Slow cooling prevents thermal contraction cracking. Extended chill allows milkfat crystallization network to lock into firm New York texture.",
                "timerMins": 60
            }
        ],
        "sensoryIndicators": {
            "aroma": "Tangy cream cheese, toasted honey graham, bright lemon blossom, bourbon vanilla",
            "texture": "Dense, fudgy, melt-in-mouth richness with crunchy buttery crust",
            "finish": "Refreshing lactic acidity from sour cream crown that cuts the decadence"
        },
        "scienceNotes": "New York style cheesecake demands density (high fat, low air). Incorporating air via high-speed whipping produces an airy soufflé that collapses into deep central craters upon cooling. Low-speed paddle work plus cornstarch protein buffering ensures pristine, level, uncracked perfection.",
        "troubleshooting": {
            "Cracks across surface": "Oven cooled too rapidly or cake was overbaked past 160°F core temp. Always cool in cracked oven.",
            "Soggy bottom crust": "Water leaked through foil. Use silicone springform protector sleeve or double-ply extra-wide foil.",
            "Grainy curdled texture": "Ingredients were too cold or oven temperature was above 325°F."
        },
        "substitutions": [
            {"ingredient": "Graham Crackers", "substitute": "Speculoos Biscoff or Digestive Biscuits", "ratio": "1:1 by weight"},
            {"ingredient": "Sour Cream", "substitute": "Crème Fraîche or Greek Full-Fat Yogurt", "ratio": "1:1"}
        ],
        "flavorPairings": ["Fresh Raspberry Coulis", "Espresso", "Macerated Strawberries", "Meyer Lemon Marmalade"],
        "advancedTechnique": "Silicone pan wrap technique to eliminate water bath leakage risk 100%.",
        "storageAndReheating": "Keep refrigerated up to 7 days covered. Can freeze well for up to 2 months; thaw overnight in fridge.",
        "nutritionEstimates": {"calories": 520, "protein": 9, "carbs": 42, "fat": 38},
        "relatedRecipes": ["rec-basque-cheesecake", "rec-bourbon-pecan-pie", "rec-shattered-lemon-tart"],
        "relatedTechniques": ["Bain-marie thermal buffering", "Cornstarch protein stabilization", "Par-baked crust sealing"]
    },
    {
        "id": "rec-valrhona-brownies",
        "title": "Valrhona Dark Chocolate Fudge Brownies with Flaky Sea Salt",
        "cuisine": "French / American Modern",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 15,
        "cookMins": 28,
        "totalMins": 43,
        "yieldServings": 16,
        "heroImage": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ultimate restaurant-grade brownie: intense 70% Valrhona Guanaja chocolate, browned butter, shiny paper-thin crackly meringue top, and an intensely fudgy, truffle-dense core finished with Maldon sea salt.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Bittersweet chocolate intensity, nutty browned butter, crackly top and fudgy truffle center",
        "ingredients": [
            {"name": "Valrhona Guanaja 70% Dark Chocolate", "qty": 250, "unit": "g", "prep": "chopped into small chunks", "dept": "Baking & Pantry"},
            {"name": "Unsalted European Butter (82% fat)", "qty": 180, "unit": "g", "prep": "cubed for browning", "dept": "Dairy & Fats"},
            {"name": "Dutch Process Cocoa Powder (Valrhona)", "qty": 35, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Large Eggs", "qty": 3, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Egg Yolk", "qty": 1, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Granulated White Sugar", "qty": 180, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Dark Muscovado / Brown Sugar", "qty": 100, "unit": "g", "prep": "packed", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Flour", "qty": 90, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Espresso Powder", "qty": 3, "unit": "g", "prep": "instant fine", "dept": "Baking & Pantry"},
            {"name": "Pure Vanilla Bean Extract", "qty": 8, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Flaky Sea Salt (Maldon)", "qty": 4, "unit": "g", "prep": "for finishing", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "8x8-inch Square Metal Baking Pan", "type": "Bakeware"},
            {"name": "Parchment Paper Sling", "type": "Baking Supply"},
            {"name": "Saucepan for Beurre Noisette", "type": "Cookware"},
            {"name": "Electric Hand Mixer or Whisk", "type": "Small Appliance"}
        ],
        "miseEnPlace": [
            "Line an 8x8 metal pan with criss-cross parchment paper leaving 2-inch overhang handles; butter lightly.",
            "Preheat oven to 350°F (175°C).",
            "Chop chocolate into uniform small pieces so it melts instantly in hot butter."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "In a saucepan over medium heat, melt the cubed butter. Swirl as it foams, bubbles, and subsides until hazelnut-colored milk solids brown at the bottom (beurre noisette, 4-5 mins). Remove from heat, immediately add chopped Valrhona chocolate, cocoa powder, and espresso powder. Whisk until silky and melted.",
                "sensoryCue": "Nutty toasty aroma with deep dark glossy melted chocolate sheen.",
                "scienceNote": "Blooming cocoa powder in hot 250°F browned butter dissolves fat-soluble flavor pyrazines and releases latent cacao volatile aromatics.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "In a separate bowl, whip eggs, extra yolk, white sugar, and brown sugar with an electric mixer on medium-high speed for full 5 minutes until pale, tripled in volume, and forms a thick ribbon trail.",
                "sensoryCue": "Pale coffee-crema color, aerated foam that holds ribbon for 3 seconds.",
                "scienceNote": "Dissolving and aerating sucrose with egg albumin creates a micro-meringue foam. As the brownie bakes, this foam floats to the surface and dries out, forming the signature glossy paper-thin crinkly skin.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Gently stream the warm melted chocolate-butter mixture down side of egg bowl while folding with a silicone spatula until homogeneous.",
                "sensoryCue": "Glossy, thick mahogany ribbon batter.",
                "scienceNote": "Folding preserves the aerated egg emulsion without deflating delicate air cells.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Sift in the flour and fine salt. Fold just until no dry flour streaks remain (approx 20 folds). Spread evenly into prepared pan. Tap pan twice on counter.",
                "sensoryCue": "Fudge-thick batter levels out smoothly in pan corners.",
                "scienceNote": "Minimal flour and minimal folding prevents gluten development, ensuring dense truffle fudginess rather than cakey crumb.",
                "timerMins": 2
            },
            {
                "stepNum": 5,
                "text": "Bake at 350°F (175°C) for 26 to 28 minutes, until edges are set and a toothpick inserted in the center comes out with moist, fudgy crumbs (not wet batter). Immediately sprinkle Maldon sea salt flakes across top. Cool completely in pan, then chill 2 hours before slicing into sharp squares.",
                "sensoryCue": "Crinkled tissue-paper top, glossy flakes of sea salt, deep fudgy interior.",
                "scienceNote": "Chilling crystallizes the cocoa butter and milkfat matrix, allowing laser-sharp knife cuts without tearing.",
                "timerMins": 28
            }
        ],
        "sensoryIndicators": {
            "aroma": "Intense dark cocoa, brown butter hazelnut, roasted espresso, vanilla bean",
            "texture": "Crisp paper-thin shattering crust yielding into dense, chewy, molten truffle center",
            "finish": "Lingering bittersweet cacao balanced by bright saline crunch of Maldon salt"
        },
        "scienceNotes": "The secret to the coveted crackly brownie top is two-fold: high ratio of dissolved sugar in aerated egg proteins (forming a microscopic surface meringue) and baking in an aluminum/metal pan rather than glass (glass is an insulator that slows bottom heat conduction, causing soggy overbaked edges).",
        "troubleshooting": {
            "No shiny crackly skin": "Eggs and sugar were not whipped long enough; sugar was undissolved.",
            "Cakey dry texture": "Too much flour or overbaked. Toothpick should never come out completely clean for fudge brownies.",
            "Greasy separation": "Melted butter was too hot when added to eggs, breaking the emulsion."
        },
        "substitutions": [
            {"ingredient": "Valrhona Guanaja 70%", "substitute": "Guittard 72% or Callebaut 70-30-38", "ratio": "1:1"},
            {"ingredient": "Muscovado Sugar", "substitute": "Dark Brown Sugar", "ratio": "1:1"}
        ],
        "flavorPairings": ["Bourbon Vanilla Bean Gelato", "Fresh Raspberries", "Single Malt Scotch", "Café au Lait"],
        "advancedTechnique": "Infusing browned butter with roasted crushed cocoa nibs and filtering through cheesecloth before combining with chocolate.",
        "storageAndReheating": "Store in airtight container at room temperature for up to 5 days, or refrigerate for dense cold truffle texture.",
        "nutritionEstimates": {"calories": 340, "protein": 5, "carbs": 36, "fat": 21},
        "relatedRecipes": ["rec-chocolate-lava", "rec-mousse-chocolat", "rec-souffle-chocolat"],
        "relatedTechniques": ["Beurre noisette browning", "Egg-sugar ribbon aeration", "Cocoa fat blooming"]
    },
    {
        "id": "rec-chocolate-chunk-cookies",
        "title": "Brown Butter 70% Chocolate Chunk Sea Salt Cookies",
        "cuisine": "American / Modern Bakery",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 20,
        "cookMins": 12,
        "totalMins": 32,
        "yieldServings": 14,
        "heroImage": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?auto=format&fit=crop&w=1200&q=80",
        "summary": "The definitive bakery-style chocolate chip cookie: nutty browned butter, 48-hour cold aged dough, hand-chopped 70% dark chocolate pools, crisp rippled edges, and a gooey chewy center topped with fleur de sel.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Deep butterscotch and toffee notes, pools of molten dark chocolate, chewy interior and crispy edge",
        "ingredients": [
            {"name": "Unsalted Butter", "qty": 225, "unit": "g", "prep": "browned down to approx 180g net fat", "dept": "Dairy & Fats"},
            {"name": "Dark Brown Sugar", "qty": 180, "unit": "g", "prep": "firmly packed", "dept": "Baking & Pantry"},
            {"name": "Granulated Castor Sugar", "qty": 90, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Large Egg", "qty": 1, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Large Egg Yolk", "qty": 1, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Pure Vanilla Bean Paste", "qty": 10, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Unbleached Bread Flour (12.7% protein)", "qty": 260, "unit": "g", "prep": "sifted (bread flour ensures chew)", "dept": "Baking & Pantry"},
            {"name": "Baking Soda (Sodium Bicarbonate)", "qty": 4, "unit": "g", "prep": "fine powder", "dept": "Baking & Pantry"},
            {"name": "Baking Powder", "qty": 2, "unit": "g", "prep": "double acting", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 5, "unit": "g", "prep": "dissolved in dough", "dept": "Baking & Pantry"},
            {"name": "Valrhona 70% Dark Chocolate Feves / Bar", "qty": 220, "unit": "g", "prep": "coarsely hand-chopped into shards and blocks", "dept": "Baking & Pantry"},
            {"name": "Flaky Sea Salt (Maldon)", "qty": 4, "unit": "g", "prep": "finishing pinch", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Heavy Gauge Rimmed Half-Sheet Baking Pans", "type": "Bakeware"},
            {"name": "Silpat Baking Mats or Parchment Paper", "type": "Baking Supply"},
            {"name": "Large Cookie Scoop (approx 65g / 2.5 oz)", "type": "Small Tool"},
            {"name": "Round Biscuit Cutter (for pan-banging swirl)", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Brown butter in a light-colored saucepan until golden amber with nutty toasted specks. Pour into bowl and cool to room temp paste (approx 30 mins).",
            "Chop chocolate by hand rather than using chocolate chips (chips contain stabilizers that prevent pool formation).",
            "Weigh dry ingredients and whisk together thoroughly."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Whisk the cooled browned butter with dark brown sugar and castor sugar for 2 minutes until glossy and smooth like wet sand. Whisk in whole egg, extra yolk, and vanilla paste until emulsified and slightly lightened in color.",
                "sensoryCue": "Rich butterscotch aroma, smooth emulsified batter without oily separation.",
                "scienceNote": "High proportion of brown sugar contributes hygroscopic molasses fructose, ensuring chewy moisture retention and accelerated caramelization.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Fold in the flour, baking soda, baking powder, and fine salt with a wooden spoon or spatula just until halfway combined. Add chopped chocolate chunks and fold until no dry flour pockets remain. Do not overmix.",
                "sensoryCue": "Dense, studded dough with prominent chocolate chunks distributed throughout.",
                "scienceNote": "Using higher-protein bread flour promotes gluten network elasticity, yielding a substantive chew that balances molten chocolate chunks.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Scoop into 14 large balls (approx 65g each). Place onto a tray, wrap airtight in plastic film, and chill in refrigerator for 24 to 48 hours (minimum 12 hours).",
                "sensoryCue": "Dough turns firm, deep golden caramel color as flour hydrates.",
                "scienceNote": "48-hour cold aging allows endogenous enzymes to hydrolyze starches into simple sugars, amplifying toffee/butterscotch complexity while drying surface moisture for crisp outer edges.",
                "timerMins": 1440
            },
            {
                "stepNum": 4,
                "text": "Preheat oven to 350°F (175°C). Space 6 dough balls per half-sheet lined with parchment. Bake for 10-12 minutes until edges are golden bronze and set, but centers are still pale and soft.",
                "sensoryCue": "Rippled golden edges, molten chocolate pools, aroma filling the kitchen.",
                "scienceNote": "Baking soda alkaline pH promotes rapid surface browning and horizontal spread.",
                "timerMins": 11
            },
            {
                "stepNum": 5,
                "text": "Immediately upon removing pan from oven, swirl a large round cookie cutter or bowl over each hot cookie in a circular motion to shape into perfect concentric circles with rippled edges. Sprinkle each with flaky sea salt. Cool on pan 10 minutes, then transfer to rack.",
                "sensoryCue": "Picture-perfect circular cookies with glistening salt crystals and chocolate pools.",
                "scienceNote": "Hot molten cookies remain malleable for 30 seconds out of oven; the cutter technique pushes edge ripples into high-density crispy ruffles.",
                "timerMins": 10
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toffee, caramelized brown butter, rich roasted cacao, toasted grains",
            "texture": "Crisp golden edge ripples giving way to dense, soft, chewy dough and molten chocolate rivers",
            "finish": "Sweet butterscotch rounded by mineral salinity from Maldon flakes"
        },
        "scienceNotes": "Cold aging dough is the single biggest difference between amateur and professional cookies. During 24-48 hours chilling, flour proteins and starches fully absorb available egg and butter water. This reduces spreading in the oven, retains moisture in the center, and allows flavor precursors to develop.",
        "troubleshooting": {
            "Cookies spread into thin puddle": "Brown butter was melted/hot when mixed, or dough was baked without chilling.",
            "Puffy and dry": "Too much flour used (measure by grams) or all-purpose flour substituted with too much baking powder.",
            "No chocolate pools": "Commercial chocolate chips used instead of hand-chopped bar chocolate."
        },
        "substitutions": [
            {"ingredient": "Bread Flour", "substitute": "All-Purpose Flour", "ratio": "1:1 (cookie will be slightly more tender and less chewy)"},
            {"ingredient": "70% Dark Chocolate", "substitute": "Mix of 70% Dark and 40% Milk Chocolate", "ratio": "1:1 for sweeter profile"}
        ],
        "flavorPairings": ["Cold Whole Milk", "Espresso Cortado", "Bourbon", "Earl Grey Tea"],
        "advancedTechnique": "Pan-banging technique (dropping sheet pan firmly onto oven rack at minute 8 and 10) to create concentric accordion ripple waves.",
        "storageAndReheating": "Dough balls freeze beautifully for up to 3 months; bake directly from frozen at 350°F for 13-14 minutes.",
        "nutritionEstimates": {"calories": 370, "protein": 5, "carbs": 44, "fat": 20},
        "relatedRecipes": ["rec-valrhona-brownies", "rec-madeleines-commercy", "rec-caneles-bordeaux"],
        "relatedTechniques": ["Cold dough enzymatic aging", "Beurre noisette butterscotch development", "Pan-banging ripple acoustics"]
    },
    {
        "id": "rec-mille-feuille",
        "title": "Classical Mille-Feuille (Caramelized Puff Pastry & Vanilla Diplomat Cream)",
        "cuisine": "French / Classical Haute Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Advanced",
        "prepMins": 60,
        "cookMins": 35,
        "totalMins": 95,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pinnacle of French pastry architecture: three crisp, razor-thin layers of caramelized inverted puff pastry (pâte feuilletée inversée) sandwiching silky Madagascar vanilla diplomat cream, finished with traditional feathered fondant glaze.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Ultra-crisp shattering caramelized lamination alternating with cloud-like velvety vanilla cream",
        "ingredients": [
            {"name": "All-Butter Puff Pastry (Pâte Feuilletée)", "qty": 500, "unit": "g", "prep": "chilled block (or scratch 6-turn inverted)", "dept": "Baking & Pantry"},
            {"name": "Icing / Powdered Sugar", "qty": 80, "unit": "g", "prep": "sifted for pastry caramelization", "dept": "Baking & Pantry"},
            {"name": "Whole Milk (3.5% fat)", "qty": 500, "unit": "ml", "prep": "farm fresh", "dept": "Dairy & Fats"},
            {"name": "Madagascar Bourbon Vanilla Bean", "qty": 1, "unit": "whole", "prep": "split and seeds scraped", "dept": "Spices & Botanicals"},
            {"name": "Egg Yolks", "qty": 6, "unit": "whole", "prep": "approx 110g", "dept": "Dairy & Fats"},
            {"name": "Granulated Sugar", "qty": 100, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Cornstarch (Maizena)", "qty": 45, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Unsalted European Butter", "qty": 50, "unit": "g", "prep": "cold, cubed", "dept": "Dairy & Fats"},
            {"name": "Gelatin Sheets (Silver 160 Bloom)", "qty": 4, "unit": "g", "prep": "bloomed in cold ice water", "dept": "Baking & Pantry"},
            {"name": "Heavy Whipping Cream (36% fat)", "qty": 200, "unit": "ml", "prep": "chilled at 38°F", "dept": "Dairy & Fats"},
            {"name": "White Fondant Glaze & Dark Chocolate", "qty": 150, "unit": "g", "prep": "for feathered top", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Heavy Rimmed Baking Sheets (2 matched sheets)", "type": "Bakeware"},
            {"name": "Parchment Paper & Silpat", "type": "Baking Supply"},
            {"name": "Serrated Bread Knife (offset)", "type": "Cutlery"},
            {"name": "Piping Bag with 12mm Round Tip", "type": "Pâtisserie Tool"}
        ],
        "miseEnPlace": [
            "Roll puff pastry between parchment to 3mm uniform thickness (approx 12x16 inches). Chill 1 hour.",
            "Bloom gelatin sheet in ice water for 10 minutes.",
            "Preheat oven to 375°F (190°C)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Dock the rolled puff pastry thoroughly with a fork. Place on parchment-lined sheet pan. Cover with second sheet of parchment and top with a second heavy baking sheet (weighting prevents uncontrolled puffing). Bake at 375°F (190°C) for 25 minutes until deep golden.",
                "sensoryCue": "Pastry is compressed, golden-brown, and wafer-crisp.",
                "scienceNote": "Weighting the pastry restricts vertical expansion, forcing steam to laminate the 729 microscopic butter-dough leaves into razor-thin, shatteringly crisp layers.",
                "timerMins": 25
            },
            {
                "stepNum": 2,
                "text": "Remove top pan and top parchment. Dust pastry generously with sifted powdered sugar. Return uncovered to 425°F (220°C) oven for 4-5 minutes until sugar melts into a gleaming, glassy, amber caramel sheen. Remove and cool completely on wire rack.",
                "sensoryCue": "Gleaming mirror-like caramel glaze that protects pastry from absorbing moisture.",
                "scienceNote": "The caramelized sugar layer acts as an impermeable hydrophobic seal, preventing cream moisture from softening the crisp pastry leaves.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Make Crème Pâtissière: Scald milk with vanilla bean and seeds. Whisk yolks, sugar, and cornstarch. Temper hot milk into yolks, return to pan, and boil 2 minutes vigorously while whisking until thickened. Off heat, whisk in bloomed gelatin and cold butter. Cool to 68°F (20°C).",
                "sensoryCue": "Thick, glossy, fragrant pastry cream with dense flecks of vanilla seeds.",
                "scienceNote": "Gelatin and cornstarch dual gelling network provides structural rigidity needed to support piped pastry tiers.",
                "timerMins": 10
            },
            {
                "stepNum": 4,
                "text": "Whip heavy cream to medium peaks. Gently fold into the cooled pastry cream in two batches to create Crème Diplomate. Transfer to piping bag with round tip; chill 30 minutes to set slightly.",
                "sensoryCue": "Lighter than pastry cream, velvety, aerated yet piped peaks hold shape.",
                "scienceNote": "Folding whipped cream creates an aerated mousse emulsion with delicate dairy mouthfeel.",
                "timerMins": 5
            },
            {
                "stepNum": 5,
                "text": "Trim cooled caramelized pastry into 3 identical 4x12-inch rectangles using a gentle sawing motion with an offset serrated knife. Pipe uniform spheres of diplomat cream across bottom layer. Place middle pastry layer, pipe second layer of cream. Crown with top glazed pastry (glazed with white fondant and feathered chocolate). Chill 1 hour before portioning into individual 4x2-inch slices.",
                "sensoryCue": "Pristine architectural lines, visible caramel gleam, crisp crack as serrated knife enters.",
                "scienceNote": "Chilling allows diplomat cream fats to solidify, preventing cream from extruding out the sides when sliced.",
                "timerMins": 60
            }
        ],
        "sensoryIndicators": {
            "aroma": "Caramelized sugar, toasted puff pastry butter, floral Madagascar vanilla, scalding milk",
            "texture": "Dramatic shattering crispness of pastry followed instantly by melting, cloud-like cream",
            "finish": "Clean vanilla bean finish without excessive cloying sweetness"
        },
        "scienceNotes": "The traditional challenge with mille-feuille is sogginess and squishing during slicing. Double-pan weighted baking forces moisture out and aligns gluten sheets; high-heat sugar caramelization creates a hydrophobic varnish that repels water from the crème diplomate for up to 8 hours.",
        "troubleshooting": {
            "Pastry puffs unevenly into pillow": "Top baking sheet was not heavy enough; add an extra sheet or cast iron pan on top.",
            "Cream squishes out sides when sliced": "Diplomat cream was not chilled enough, or chef pressed down instead of using a sawing serrated knife.",
            "Pastry gets soft within 1 hour": "Pastry was under-caramelized; sugar glaze must melt into a glassy continuous seal."
        },
        "substitutions": [
            {"ingredient": "Crème Diplomate", "substitute": "Crème Mousseline (whipped butter-pastry cream)", "ratio": "1:1 for firmer hold"},
            {"ingredient": "Fondant Glaze", "substitute": "Simple dusting of Powdered Sugar and Cocoa powder", "ratio": "Rustic alternative"}
        ],
        "flavorPairings": ["Champagne Brut", "Café Crème", "Fresh Raspberries", "Earl Grey Tea"],
        "advancedTechnique": "Assembling the mille-feuille on its side (vertical lamination) so that when sliced, the knife cuts between pastry layers rather than crushing them.",
        "storageAndReheating": "Best enjoyed within 6 hours of assembly for peak crispness. Keep refrigerated. Do not freeze.",
        "nutritionEstimates": {"calories": 440, "protein": 6, "carbs": 48, "fat": 25},
        "relatedRecipes": ["rec-eclairs-chocolat", "rec-paris-brest", "rec-creme-brulee"],
        "relatedTechniques": ["Weighted puff pastry compression", "Sugar caramel hydrophobic sealing", "Crème diplomate folding"]
    }
]

print(f"Loaded {len(MEGA_RECIPES)} initial recipes in MEGA_RECIPES.")
