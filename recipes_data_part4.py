# recipes_data_part4.py
# High-precision culinary master recipes 21-31

PART_4_RECIPES = [
    {
        "id": "rec-croque-madame",
        "title": "Croque Madame Parisienne (Brioche, Jambon de Paris, Sauce Mornay & Fried Egg)",
        "cuisine": "French / Classical Bistro",
        "category": "breakfast",
        "slot": "opener",
        "difficulty": "Easy",
        "prepMins": 15,
        "cookMins": 15,
        "totalMins": 30,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=1200&q=80",
        "summary": "The quintessential Parisian cafe luxury: thick slices of golden toasted brioche stuffed with French cooked ham (jambon blanc) and aged Gruyère, smothered in bubbling, broiled Sauce Mornay and crowned with a sunny-side-up farm egg with a molten yolk.",
        "dietary": [],
        "sensoryRole": "Decadent toasted brioche crunch, bubbling cheesy Mornay blanket, molten runny yolk cascading over salty ham",
        "ingredients": [
            {"name": "Artisanal Brioche or Pain de Mie", "qty": 8, "unit": "slices", "prep": "cut 3/4-inch thick", "dept": "Bakery"},
            {"name": "Jambon de Paris (French Cooked Ham)", "qty": 250, "unit": "g", "prep": "thinly sliced", "dept": "Meat & Poultry"},
            {"name": "Aged Gruyère A.O.P. or Comté Cheese", "qty": 200, "unit": "g", "prep": "grated", "dept": "Dairy & Fats"},
            {"name": "Dijon Mustard (Edmond Fallot)", "qty": 30, "unit": "g", "prep": "smooth spicy", "dept": "Baking & Pantry"},
            {"name": "Unsalted European Butter", "qty": 60, "unit": "g", "prep": "divided: 40g Mornay, 20g frying", "dept": "Dairy & Fats"},
            {"name": "All-Purpose Flour", "qty": 40, "unit": "g", "prep": "for blond roux", "dept": "Baking & Pantry"},
            {"name": "Whole Milk", "qty": 400, "unit": "ml", "prep": "warmed", "dept": "Dairy & Fats"},
            {"name": "Fresh Grated Whole Nutmeg", "qty": 2, "unit": "g", "prep": "fine pinch", "dept": "Spices & Botanicals"},
            {"name": "Large Farm Fresh Eggs", "qty": 4, "unit": "whole", "prep": "sunny side up frying", "dept": "Dairy & Fats"},
            {"name": "Fresh Chives", "qty": 10, "unit": "g", "prep": "finely minced", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "Heavy Cast-Iron Skillet", "type": "Cookware"},
            {"name": "Small Saucepan for Mornay", "type": "Cookware"},
            {"name": "Baking Sheet with Parchment", "type": "Bakeware"}
        ],
        "miseEnPlace": [
            "Grate Gruyère cheese; slice ham and bread.",
            "Warm milk in small saucepan.",
            "Preheat oven broiler to High."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Sauce Mornay: In a small saucepan over medium heat, melt 40g butter. Add flour and cook whisking for 2 minutes to form a blond roux (do not brown). Slowly whisk in warm milk in 3 additions until smooth. Simmer 3 minutes until thick and bubbling. Remove from heat; whisk in 80g grated Gruyère, grated nutmeg, salt, and black pepper until silky smooth.",
                "sensoryCue": "Rich, velvety ivory cheese sauce that heavily coats a spoon.",
                "scienceNote": "Starch granules swell and gelatinize at 180°F, while melted Gruyère fat is suspended by casein proteins into a stable emulsion.",
                "timerMins": 6
            },
            {
                "stepNum": 2,
                "text": "Toast Bread: Brush both sides of brioche slices lightly with melted butter. Toast in a hot cast-iron skillet over medium heat for 2 minutes per side until golden brown and crisp.",
                "sensoryCue": "Golden-amber buttery toast with toasty brioche perfume.",
                "scienceNote": "Pre-toasting creates a rigid starch exterior that prevents the wet cheese sauce from turning the sandwich soggy.",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Assemble Sandwiches: Lay 4 toasted slices on a parchment-lined baking sheet. Spread each with 1 tsp Dijon mustard. Layer generously with sliced jambon de Paris and 20g grated Gruyère. Top with remaining bread slices.",
                "sensoryCue": "Plump sandwiches stacked with savory ham and cheese.",
                "scienceNote": "Dijon mustard contains vinegar and sinigrin glucosinolate, providing an acidic counterpoint to rich dairy fats.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Broil Mornay: Spoon generous ladle of warm Sauce Mornay over top of each sandwich, spreading to edges. Sprinkle remaining grated Gruyère over the sauce. Place under broiler for 3 to 4 minutes until cheese is vigorously bubbling with blistered deep brown spots.",
                "sensoryCue": "Bubbling golden-brown volcanic crust with toasted cheese aroma.",
                "scienceNote": "Direct intense radiant broiler heat caramelizes milk sugars and proteins via rapid Maillard reactions.",
                "timerMins": 4
            },
            {
                "stepNum": 5,
                "text": "Fry Eggs & Crown: In the skillet, melt 20g butter over medium-low heat. Crack 4 eggs gently; fry until whites are set and edges are crisp, with yolks remaining liquid and warm. Crown each broiled sandwich with a fried egg; garnish with minced chives and cracked black pepper.",
                "sensoryCue": "Glossy golden yolk perched atop blistered cheese; yolk breaks and rivers down sandwich.",
                "scienceNote": "Egg yolk at 145°F acts as a rich self-saucing sauce, combining with Mornay to create luxury mouthfeel.",
                "timerMins": 3
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted brioche, melted nutty Gruyère, smoked cured ham, brown butter, fried egg",
            "texture": "Crisp buttery toast crunch giving way to tender ham, molten creamy Mornay, and liquid yolk burst",
            "finish": "Spicy Dijon mustard punch balancing rich, bubbling cheese"
        },
        "scienceNotes": "A Croque Monsieur becomes a Croque Madame with the addition of the fried egg (named for resembling an Edwardian lady's wide-brimmed hat). The combination of Sauce Mornay (béchamel + cheese) on top provides a protective moisture seal during high-heat broiling.",
        "troubleshooting": {
            "Soggy sandwich": "Bread was not pre-toasted in skillet before assembly.",
            "Sauce splits oily under broiler": "Roux was under-cooked or sauce was boiled too hard before spreading.",
            "Hard rubbery egg yolk": "Egg was cooked on high heat or covered with lid; fry on gentle heat uncovered."
        },
        "substitutions": [
            {"ingredient": "Jambon de Paris", "substitute": "Prosciutto Cotto, Rosemary Ham, or Smoked Turkey", "ratio": "1:1"},
            {"ingredient": "Brioche", "substitute": "Country Sourdough or Pullman White", "ratio": "1:1"}
        ],
        "flavorPairings": ["Café au Lait", "Mâche Salad with Champagne Vinaigrette", "Bloody Mary", "Pilsner Beer"],
        "advancedTechnique": "Infusing milk for Mornay with a bay leaf, shallot, and black peppercorn sachet before making béchamel.",
        "storageAndReheating": "Best enjoyed immediately. Un-broiled sandwiches can be assembled and refrigerated for up to 24 hours.",
        "nutritionEstimates": {"calories": 620, "protein": 32, "carbs": 38, "fat": 38},
        "relatedRecipes": ["rec-quiche-lorraine", "rec-french-rolled-omelette", "rec-eggs-benedict"],
        "relatedTechniques": ["Sauce Mornay starch emulsion", "Blond roux formulation", "Sunny-side egg baste"]
    },
    {
        "id": "rec-tonkotsu-ramen",
        "title": "Hakata Tonkotsu Ramen (12-Hour Emulsified Pork Broth, Chashu & Ajitsuke Tamago)",
        "cuisine": "Japanese / Hakata Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Advanced",
        "prepMins": 60,
        "cookMins": 720,
        "totalMins": 780,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1200&q=80",
        "summary": "The legendary pride of Fukuoka: opaque, milky-white, intensely unctuous pork marrow broth achieved through violent 12-hour rolling boil emulsification. Served with springy low-hydration noodles, rolled chashu pork belly, 6-minute jammy shoyu egg, and aromatic mayu black garlic oil.",
        "dietary": [],
        "sensoryRole": "Ultra-rich collagenous broth, savory umami depth, tender melting pork belly, springy alkaline noodles",
        "ingredients": [
            {"name": "Pork Femur Bones (Marrow Bones)", "qty": 1800, "unit": "g", "prep": "cut across to expose marrow", "dept": "Meat & Poultry"},
            {"name": "Pork Trotters (Split Pig's Feet)", "qty": 900, "unit": "g", "prep": "split lengthwise (provides collagen)", "dept": "Meat & Poultry"},
            {"name": "Pork Back Fat (Fatback)", "qty": 300, "unit": "g", "prep": "diced small for emulsion", "dept": "Meat & Poultry"},
            {"name": "Aromatics (Yellow Onion, Garlic Head, Ginger)", "qty": 300, "unit": "g", "prep": "halved and charred", "dept": "Produce"},
            {"name": "Shoyu Tare (Soy Sauce Seasoning Base)", "qty": 180, "unit": "ml", "prep": "concentrated shoyu, mirin, sake, kombu, katsuobushi", "dept": "Pantry"},
            {"name": "Fresh Hakata-Style Ramen Noodles", "qty": 600, "unit": "g", "prep": "thin, straight, low-hydration (26-28%)", "dept": "Bakery"},
            {"name": "Rolled Pork Belly Chashu", "qty": 500, "unit": "g", "prep": "braised in soy-mirin and torched", "dept": "Meat & Poultry"},
            {"name": "Ajitsuke Tamago (Marinated Ramen Eggs)", "qty": 6, "unit": "whole", "prep": "6-min 15-sec soft boiled and soy-marinated", "dept": "Dairy & Fats"},
            {"name": "Wood Ear Mushrooms (Kikurage)", "qty": 40, "unit": "g", "prep": "rehydrated and shredded", "dept": "Produce"},
            {"name": "Finely Sliced Scallions (Negi)", "qty": 60, "unit": "g", "prep": "green tops fine sliced", "dept": "Produce"},
            {"name": "Mayu (Black Garlic Oil)", "qty": 30, "unit": "ml", "prep": "burnt garlic sesame oil finishing drizzle", "dept": "Pantry"}
        ],
        "equipment": [
            {"name": "Large Stockpot (12 to 16 quart)", "type": "Cookware"},
            {"name": "Spider Strainer & Fine Chinois", "type": "Small Tool"},
            {"name": "High-Heat Butane Kitchen Torch", "type": "Precision Tool"},
            {"name": "Noodle Strainer Basket", "type": "Cookware"}
        ],
        "miseEnPlace": [
            "Soak pork femur bones and trotters in cold water overnight (12h) to leach out hemoglobin and myoglobin (essential for white broth).",
            "Prepare Shoyu Tare and Ajitsuke Tamago 24 hours ahead.",
            "Braid and braise Chashu pork belly; chill to slice cleanly."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "The Blanch: Place soaked bones and trotters in stockpot, cover with fresh cold water. Bring to a rapid rolling boil for 15 minutes. Drain completely, discarding the dark bloody scum water. Scrub every bone under cold running water with a stiff brush to remove coagulated marrow and black marrow veins.",
                "sensoryCue": "Bones become pristine white/cream with zero dark blood clots.",
                "scienceNote": "Blanching removes denatured blood proteins and impurities that would turn the broth muddy gray and impart off-flavors.",
                "timerMins": 25
            },
            {
                "stepNum": 2,
                "text": "The 12-Hour Rolling Boil: Return scrubbed bones and diced fatback to cleaned pot. Cover with 6 liters fresh water. Bring to a violent, galloping rolling boil. Keep at maximum boil for 10-12 hours, topping off with boiling water to keep bones submerged. Stir every 45 minutes to scrape bottom.",
                "sensoryCue": "Broth transforms from translucent to milky, opaque white ivory; gelatin coats lips.",
                "scienceNote": "Unlike French stock (which is kept at a gentle 185°F simmer to preserve clarity), Tonkotsu demands violent kinetic rolling boiling. Turbulent boiling mechanically shears melted backfat into droplets under 5 microns, emulsifying them with hydrolyzed gelatin collagen into a permanent opaque oil-in-water suspension.",
                "timerMins": 660
            },
            {
                "stepNum": 3,
                "text": "Add charred aromatics (onion, garlic, ginger) for the final 60 minutes of boiling. Strain broth through fine chinois into clean pot; press solids to extract all liquid. Keep hot at 195°F (90°C).",
                "sensoryCue": "Silky, viscous, creamy white broth with deep pork and roasted allium aroma.",
                "scienceNote": "Adding aromatics only in the final hour preserves fresh volatile terpenes and sulfur compounds without boiling them into bitter stewed flavors.",
                "timerMins": 60
            },
            {
                "stepNum": 4,
                "text": "Noodle Cook (Katamé / Firm): Drop fresh Hakata ramen noodles into a massive pot of aggressively boiling water for exactly 45 to 55 seconds (firm texture). Drain vigorously with 5 sharp downward snaps to expel water.",
                "sensoryCue": "Firm, springy noodles with toothsome bite (al dente).",
                "scienceNote": "Snapping the basket removes water droplets that would otherwise dilute the rich broth in the bowl.",
                "timerMins": 1
            },
            {
                "stepNum": 5,
                "text": "Assembly: Add 35ml hot Shoyu Tare and 1 tsp melted pork lard into pre-warmed ramen bowl. Ladle in 350ml scalding Tonkotsu broth; whisk with tare until frothy. Fold cooked noodles into broth with chopsticks. Top with torched chashu slices, halved ajitsuke tamago, shredded kikurage, negi scallions, and a drizzle of mayu black garlic oil.",
                "sensoryCue": "Frothy milky broth contrasting with black garlic swirl and charred pork belly.",
                "scienceNote": "Warming the bowl is vital; Tonkotsu fat starts solidifying below 140°F, creating a greasy film if served in cold ceramics.",
                "timerMins": 3
            }
        ],
        "sensoryIndicators": {
            "aroma": "Deep pork bone umami, roasted garlic oil (mayu), charred chashu, sweet ginger and scallion",
            "texture": "Unctuously thick, creamy, tongue-coating broth with firm chewy noodles and melting pork belly",
            "finish": "Intense savory umami depth, lips coated with silky collagen sheen"
        },
        "scienceNotes": "Tonkotsu broth is a colloidal emulsion of collagen, gelatin, and micro-dispersed pork fat. Split trotters supply rich proline and glycine amino acids, which convert to gelatin at 160°F+ and act as natural emulsifiers, stabilizing the suspended fat globules so they never separate.",
        "troubleshooting": {
            "Broth is clear and brown, not milky": "Heat was too low; Tonkotsu requires a violent rolling boil to force emulsification.",
            "Broth is muddy gray with foul smell": "Bones were not blanched and scrubbed thoroughly in step 1.",
            "Noodles turn soggy in bowl": "Noodles were overcooked or low-heat boil was used; boil strictly 45-55s."
        },
        "substitutions": [
            {"ingredient": "Pork Trotters", "substitute": "Pork Neck Bones or Chicken Feet (Momiji)", "ratio": "1:1 for extra collagen"},
            {"ingredient": "Mayu Black Garlic Oil", "substitute": "Toasted Sesame Chili Oil (Rayu)", "ratio": "1:1"}
        ],
        "flavorPairings": ["Cold Asahi Super Dry Draft Beer", "Crispy Gyoza", "Spicy Takana Mustard Greens"],
        "advancedTechnique": "Using an immersion blender directly in the hot strained broth for 2 minutes to create a barista-style micro-foam cappuccino froth (Tonkotsu Awa style).",
        "storageAndReheating": "Broth solidifies into a rock-hard jelly when cold. Store refrigerated up to 5 days or freeze 3 months. Reheat to full boil.",
        "nutritionEstimates": {"calories": 780, "protein": 42, "carbs": 62, "fat": 42},
        "relatedRecipes": ["rec-birria-de-res", "rec-shakshuka-royale", "rec-peppercorn-sauce"],
        "relatedTechniques": ["Violent boil kinetic emulsification", "Collagen gelatin hydrolysis", "Low-hydration noodle snapping"]
    },
    {
        "id": "rec-lomo-saltado",
        "title": "Peruvian Lomo Saltado (Wok-Seared Tenderloin with Ají Amarillo & Crispy Frites)",
        "cuisine": "Peruvian / Chifa Fusion",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 25,
        "cookMins": 8,
        "totalMins": 33,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        "summary": "The quintessential icon of Peruvian Chifa (Chinese-Peruvian) cuisine: prime beef tenderloin strips flash-seared in a smoking-hot carbon steel wok with red onions, ripe tomatoes, spicy ají amarillo paste, soy sauce, and pisco, tossed with double-fried crispy frites and served over garlic jasmine rice.",
        "dietary": ["Gluten-Friendly Option"],
        "sensoryRole": "Intense wok hei smokiness, tender juicy beef, sweet crunchy red onion, spicy fruity chili, vinegary savory glaze",
        "ingredients": [
            {"name": "Prime Beef Tenderloin (Filet Mignon)", "qty": 550, "unit": "g", "prep": "sliced into 1/2-inch thick strips across the grain", "dept": "Meat & Poultry"},
            {"name": "Red Onion", "qty": 2, "unit": "medium", "prep": "cut into 1/2-inch thick wedges", "dept": "Produce"},
            {"name": "Plum / Roma Tomatoes", "qty": 3, "unit": "whole", "prep": "seeded and cut into 1/2-inch wedges", "dept": "Produce"},
            {"name": "Ají Amarillo Paste (Peruvian Yellow Pepper)", "qty": 30, "unit": "g", "prep": "pureed paste", "dept": "Pantry"},
            {"name": "Garlic Cloves", "qty": 4, "unit": "whole", "prep": "minced fine", "dept": "Produce"},
            {"name": "Fresh Ginger", "qty": 10, "unit": "g", "prep": "microplaned", "dept": "Produce"},
            {"name": "Dark Soy Sauce & Light Soy Sauce", "qty": 40, "unit": "ml", "prep": "blended 50/50", "dept": "Pantry"},
            {"name": "Red Wine Vinegar", "qty": 30, "unit": "ml", "prep": "adds vital acid punch", "dept": "Pantry"},
            {"name": "Peruvian Pisco (or Dry White Wine)", "qty": 25, "unit": "ml", "prep": "for wok flambé", "dept": "Pantry"},
            {"name": "Russet Potatoes (Double-Fried Frites)", "qty": 400, "unit": "g", "prep": "baton cut, double-fried until shatteringly crisp", "dept": "Produce"},
            {"name": "Fresh Cilantro Leaves", "qty": 20, "unit": "g", "prep": "coarsely chopped", "dept": "Produce"},
            {"name": "Steamed Garlic Jasmine Rice", "qty": 400, "unit": "g", "prep": "warm for serving", "dept": "Grains & Starches"}
        ],
        "equipment": [
            {"name": "14-inch Carbon Steel Wok (Well Seasoned)", "type": "Cookware"},
            {"name": "High-Output Burner", "type": "Small Appliance"},
            {"name": "Wok Chuan (Spatula)", "type": "Small Tool"},
            {"name": "Deep Fryer or Heavy Dutch Oven for Frites", "type": "Cookware"}
        ],
        "miseEnPlace": [
            "Prepare all ingredients before turning on stove; cooking takes under 5 minutes.",
            "Double-fry potatoes to crispy golden frites; keep hot and salted.",
            "Toss beef strips with 1 tsp soy sauce, 1 tsp oil, and pinch of salt 15 mins prior."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat carbon steel wok over maximum flame until it smokes furiously (500°F / 260°C). Swirl in 2 tbsp high-smoke point oil. Add half the beef strips in a single layer. Sear undisturbed for 60 seconds without moving to achieve deep char. Toss and cook 30 seconds more. Transfer beef to a plate (still rare). Repeat with second batch.",
                "sensoryCue": "Sizzling roar; smoke and charred meat aroma; deep caramelized crust on beef.",
                "scienceNote": "Batching beef prevents temperature drop. High wok heat triggers intense Maillard reaction while leaving meat center tender and pink.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Add 1 tbsp oil to smoking wok. Add red onion wedges and ají amarillo paste. Stir-fry aggressively for 60 seconds until onions pick up smoky char spots but remain crisp and crunchy.",
                "sensoryCue": "Pungent sweet allium smoke with fruity chili aroma.",
                "scienceNote": "High-heat flash cooking caramelizes onion exterior while maintaining internal crunch (retaining cellular turgor).",
                "timerMins": 1
            },
            {
                "stepNum": 3,
                "text": "Add minced garlic, ginger, and tomato wedges. Stir-fry for 45 seconds until tomatoes are hot but not breaking down into mush.",
                "sensoryCue": "Aromatic ginger-garlic burst; tomatoes blister lightly.",
                "scienceNote": "Seeding tomatoes removes excess free water, preventing wok temperature collapse.",
                "timerMins": 1
            },
            {
                "stepNum": 4,
                "text": "Return seared beef and any resting juices to wok. Pour in Pisco and tilt wok slightly toward flame to flambé (igniting alcohol vapors with a dramatic whoosh). Immediately pour soy sauce blend and red wine vinegar around perimeter of wok.",
                "sensoryCue": "Dramatic flame leap; fragrant alcohol burn; sizzling vapor cloud with savory-sour aroma.",
                "scienceNote": "Wok hei is achieved through aerosolized oil droplet combustion in the open flame. Pouring sauces around the screaming hot rim caramelizes amino acids and sugars instantaneously.",
                "timerMins": 1
            },
            {
                "stepNum": 5,
                "text": "Toss in crispy double-fried frites and fresh cilantro. Give 2 swift tosses to coat frites in savory pan juices without softening them. Immediately slide onto a serving platter next to steamed garlic rice.",
                "sensoryCue": "Frites glistening with dark soy-vinegar glaze while retaining audible crunch.",
                "scienceNote": "Tossing frites right at the end allows them to absorb savory umami pan sauce while starch shell remains crisp for the first 3 minutes.",
                "timerMins": 1
            }
        ],
        "sensoryIndicators": {
            "aroma": "Intense smoky wok hei, charred beef, tangy vinegar sizzle, fruity ají amarillo chili, fresh cilantro",
            "texture": "Melt-in-mouth tender beef filet against crunchy sweet onions and crispy frites soaking in sauce",
            "finish": "Bright acidic snap of red wine vinegar balancing deep umami and fruity chili heat"
        },
        "scienceNotes": "Lomo Saltado is the ultimate demonstration of high-temperature wok thermodynamics and culinary migration. Chinese immigrants who arrived in Lima in the 1850s combined Cantonese wok stir-fry technique with native Peruvian ingredients (ají amarillo, native Andean potatoes, and tomatoes).",
        "troubleshooting": {
            "Beef boils and turns gray": "Too much meat added at once, or wok was not hot enough. Sear in 2 distinct small batches.",
            "Soggy frites": "Frites were tossed too early or sat in pan sauce too long. Toss in the final 10 seconds only.",
            "Tomatoes turn to mush": "Tomatoes were cooked too long or seeds weren't removed; cook tomatoes for under 1 minute."
        },
        "substitutions": [
            {"ingredient": "Beef Tenderloin", "substitute": "Ribeye (Ojo de Bife) or Skirt Steak (Entraña)", "ratio": "1:1"},
            {"ingredient": "Ají Amarillo Paste", "substitute": "Fresno Chili paste or Habanero mixed with orange bell pepper", "ratio": "1:1"}
        ],
        "flavorPairings": ["Pisco Sour Cocktail", "Inca Kola", "Cusqueña Cerveza", "Garlic Jasmine Rice"],
        "advancedTechnique": "Flambéing with Peruvian Pisco Quebranta directly from a copper ladle to impart distinct grape spirit aromatics.",
        "storageAndReheating": "Best eaten immediately. Leftovers do not store well because frites absorb liquid and soften.",
        "nutritionEstimates": {"calories": 590, "protein": 38, "carbs": 48, "fat": 26},
        "relatedRecipes": ["rec-french-rolled-omelette", "rec-chilaquiles-rojos", "rec-birria-de-res"],
        "relatedTechniques": ["Wok hei thermal aerodynamics", "High-heat batch searing", "Alcohol vapor combustion flambé"]
    },
    {
        "id": "rec-paella-valenciana",
        "title": "Paella Valenciana Tradicional (Bomba Rice, Saffron & Socarrat Crust)",
        "cuisine": "Spanish / Valencian Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 40,
        "totalMins": 70,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?auto=format&fit=crop&w=1200&q=80",
        "summary": "The sacred rice monument of the Valencian huerta. Made in a wide polished steel paella pan: golden Bomba rice infused with La Mancha saffron, rich rich sofrito, tender chicken, rabbit, flat green beans (bajoqueta), butter beans (garrofó), and fresh rosemary, finished with an authentic caramelized crunchy bottom crust (socarrat).",
        "dietary": ["Gluten-Free"],
        "sensoryRole": "Aromatic saffron and wood-smoke perfume, tender chicken and rabbit, al dente Bomba rice, crackling crunchy socarrat",
        "ingredients": [
            {"name": "Spanish Bomba Rice (D.O. Arroz de Valencia)", "qty": 400, "unit": "g", "prep": "never wash or rinse", "dept": "Grains & Starches"},
            {"name": "Bone-In Chicken & Rabbit Pieces", "qty": 800, "unit": "g", "prep": "cut into small 1.5-inch pieces", "dept": "Meat & Poultry"},
            {"name": "Flat Green Beans (Bajoqueta or Romano)", "qty": 200, "unit": "g", "prep": "trimmed and snapped into 2-inch lengths", "dept": "Produce"},
            {"name": "Large White Lima Beans (Garrofó)", "qty": 150, "unit": "g", "prep": "pre-cooked or rehydrated", "dept": "Pantry"},
            {"name": "Grated Fresh Tomatoes", "qty": 200, "unit": "g", "prep": "grated pulp without skin", "dept": "Produce"},
            {"name": "Spanish Saffron Threads (Azafrán de La Mancha)", "qty": 0.5, "unit": "g", "prep": "lightly toasted and crushed", "dept": "Spices & Botanicals"},
            {"name": "Sweet Spanish Smoked Paprika (Pimentón de la Vera)", "qty": 8, "unit": "g", "prep": "dulce", "dept": "Spices & Botanicals"},
            {"name": "Fresh Rosemary Sprig", "qty": 2, "unit": "sprigs", "prep": "fresh branch", "dept": "Produce"},
            {"name": "Extra Virgin Olive Oil", "qty": 80, "unit": "ml", "prep": "Spanish Arbequina", "dept": "Dairy & Fats"},
            {"name": "Rich Poultry & Vegetable Broth", "qty": 1200, "unit": "ml", "prep": "simmering hot (3:1 ratio to rice)", "dept": "Pantry"},
            {"name": "Fresh Lemon Wedges", "qty": 2, "unit": "whole", "prep": "for table squeeze", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "16-inch (40cm) Carbon Steel Paella Pan", "type": "Cookware"},
            {"name": "Wide Outdoor Gas Paella Burner (or large stovetop burner)", "type": "Cookware"},
            {"name": "Flat Wooden Paella Paddle", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Toast saffron threads gently in dry pan for 20 seconds; grind with pinch of salt.",
            "Cut poultry and rabbit into small uniform pieces; salt heavily 30 mins prior.",
            "Grate tomatoes on box grater, discarding skin."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Brown Meats: Heat olive oil in center of paella pan over medium-high heat. Season chicken and rabbit heavily with sea salt. Sear meats slowly for 12-14 minutes, turning frequently until deeply browned and caramelized on all sides. Push browned meats outward to perimeter of pan where heat is lower.",
                "sensoryCue": "Intense sizzling; mahogany browned crust on poultry.",
                "scienceNote": "Developing heavy fond on the pan surface is crucial; these caramelized meat juices dissolve into the broth and flavor the rice grains.",
                "timerMins": 14
            },
            {
                "stepNum": 2,
                "text": "Sofrito: Add flat green beans (bajoqueta) and garrofó to center of pan; sauté 4 minutes. Clear a small space in center, add grated tomato pulp and smoked paprika. Stir-fry sofrito for 3 minutes until tomato water evaporates and turns into a thick, dark jam.",
                "sensoryCue": "Sweet, smoky aroma of toasted pimentón and caramelized tomato.",
                "scienceNote": "Cooking tomato until oil separates (sofrito technique) concentrates umami glutamates and eliminates raw watery acidity.",
                "timerMins": 7
            },
            {
                "stepNum": 3,
                "text": "Add Broth & Saffron: Mix meats, vegetables, and sofrito together across the pan. Pour in 1200ml simmering broth and ground saffron. Bring to a rolling boil over high heat. Taste broth: it should taste pleasantly over-salted (the rice will absorb half the salt). Simmer 5 minutes.",
                "sensoryCue": "Vibrant golden-orange bubbling broth with saffron perfume.",
                "scienceNote": "Crocin pigment in saffron dissolves in hot water, imparting signature yellow-gold radiance and floral-honey aromatics.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "Add Rice & Distribute: Sprinkle Bomba rice across pan in a diagonal cross (el caballón), then distribute evenly across pan with wooden paddle. (NEVER STIR AGAIN after this point!). Add rosemary sprig. Boil vigorously on high heat for 8 minutes until rice grains absorb half the liquid and swell to surface. Lower heat to gentle simmer for 10 minutes until all liquid is absorbed.",
                "sensoryCue": "Rice grains emerge in uniform mosaic layer; rosemary releases piney aroma.",
                "scienceNote": "Stirring rice breaks grains and releases amylose starch, creating creamy risotto. Paella demands dry, separate, individual grains, achieved by leaving the rice completely undisturbed.",
                "timerMins": 18
            },
            {
                "stepNum": 5,
                "text": "The Socarrat: Remove rosemary sprig. Increase heat to medium-high for final 2-3 minutes. Listen closely: the gentle bubbling sound transforms into a distinct crackling, popping sound (chur-chur). Smell the pan: a faint aroma of toasted, nutty rice appears (stop immediately if it smells acrid/burnt!). Turn off heat, cover pan with clean linen towel, and rest 5 minutes before serving.",
                "sensoryCue": "Distinct rhythm of crackling rice; crisp caramelized bottom crust releases with a spoon.",
                "scienceNote": "Socarrat forms when bottom starches and oils fry directly against the steel at 330°F, creating a caramelized, crunchy golden crust without burning.",
                "timerMins": 8
            }
        ],
        "sensoryIndicators": {
            "aroma": "La Mancha saffron, wood smoke, wild rosemary, toasted caramelized rice (socarrat), savory poultry",
            "texture": "Plump, distinct, al dente rice grains contrasting with the shatteringly crisp, chewy crunch of the socarrat bottom",
            "finish": "Lingering saffron honey warmth and deep savory poultry fond"
        },
        "scienceNotes": "Bomba rice (Oryza sativa japonica) is capable of absorbing 3 times its volume in liquid (compared to 2x for standard long grain) without bursting its outer cell walls, keeping grains distinct, dry, and infused with concentrated stock.",
        "troubleshooting": {
            "Rice is mushy / sticky": "Rice was stirred during cooking, or too much liquid was used; never stir once distributed.",
            "Burnt socarrat with acrid taste": "Heat was left on too long during crackling phase; remove as soon as toasting aroma appears.",
            "Rice is hard and chalky": "Broth evaporated too fast on high heat; cover with foil or damp towel to trap steam.",
            "Seafood in authentic Valenciana?": "Traditional Paella Valenciana strictly uses land ingredients (chicken, rabbit, beans); seafood paella is Paella de Marisco."
        },
        "substitutions": [
            {"ingredient": "Bomba Rice", "substitute": "Calasparra, Senia, or Italian Carnaroli", "ratio": "1:1"},
            {"ingredient": "Rabbit", "substitute": "Chicken Thighs or Duck", "ratio": "1:1"}
        ],
        "flavorPairings": ["Spanish Garnacha / Tempranillo", "Cava Brut Nature", "Allioli (Garlic Emulsion)", "Lemon Wedges"],
        "advancedTechnique": "Cooking over orange wood embers (leña de naranjo) to infuse authentic citrus wood smoke into the rice.",
        "storageAndReheating": "Best enjoyed straight from pan at table. Leftovers reheat in dry nonstick skillet to re-crisp bottom socarrat.",
        "nutritionEstimates": {"calories": 540, "protein": 34, "carbs": 64, "fat": 16},
        "relatedRecipes": ["rec-risotto-porcini", "rec-shakshuka-royale", "rec-chilaquiles-rojos"],
        "relatedTechniques": ["Socarrat acoustic monitoring", "Undisturbed grain expansion", "Sofrito concentration"]
    },
    {
        "id": "rec-tom-yum-goong",
        "title": "Thai Tom Yum Goong (Hot & Sour River Prawn Broth with Galangal & Kaffir)",
        "cuisine": "Thai / Classical Royal Central",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Intermediate",
        "prepMins": 20,
        "cookMins": 15,
        "totalMins": 35,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1548943487-a2e4e43b4853?auto=format&fit=crop&w=1200&q=80",
        "summary": "The electric benchmark of Thai culinary balance: scalding river prawn broth infused with head fat (toman), bruised lemongrass stalks, fresh galangal roots, torn kaffir lime leaves, fiery bird's eye chilies, roasted chili jam (nam prik pao), fresh lime juice, and oyster mushrooms.",
        "dietary": ["Gluten-Free Option", "Dairy-Free"],
        "sensoryRole": "Electrifying harmony: searing lime acidity, fiery chili heat, savory fish sauce umami, herbal citrus aromatics",
        "ingredients": [
            {"name": "Whole Fresh Head-On Jumbo Prawns (River Prawns)", "qty": 500, "unit": "g", "prep": "heads attached, deveined, shells slit", "dept": "Seafood"},
            {"name": "Fresh Lemongrass Stalks", "qty": 3, "unit": "stalks", "prep": "bottom 5 inches, heavily bruised and sliced 2-inch bias", "dept": "Produce"},
            {"name": "Fresh Galangal Root", "qty": 40, "unit": "g", "prep": "sliced into 1/8-inch coins (do not substitute ginger)", "dept": "Produce"},
            {"name": "Fresh Kaffir Lime Leaves (Makrut)", "qty": 8, "unit": "leaves", "prep": "stems removed, hand torn to express oils", "dept": "Produce"},
            {"name": "Thai Bird's Eye Chilies (Prik Kee Noo)", "qty": 6, "unit": "whole", "prep": "crushed with side of cleaver", "dept": "Produce"},
            {"name": "Nam Prik Pao (Thai Roasted Chili Jam)", "qty": 35, "unit": "g", "prep": "adds sweet-smoky chili depth", "dept": "Pantry"},
            {"name": "Premium Thai Fish Sauce (Megachef or Red Boat)", "qty": 45, "unit": "ml", "prep": "fermented anchovy umami", "dept": "Pantry"},
            {"name": "Fresh Squeezed Lime Juice", "qty": 60, "unit": "ml", "prep": "freshly squeezed (never bottled)", "dept": "Produce"},
            {"name": "Straw Mushrooms or Oyster Mushrooms", "qty": 150, "unit": "g", "prep": "quartered", "dept": "Produce"},
            {"name": "Evaporated Milk (for Tom Yum Nam Khon style)", "qty": 60, "unit": "ml", "prep": "optional: creates creamy broth", "dept": "Dairy & Fats"},
            {"name": "Fresh Sawtooth Herb (Culantro) & Cilantro", "qty": 20, "unit": "g", "prep": "coarsely torn for finishing", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "Clay Hot Pot (Mor Din) or Stainless Steel Pot", "type": "Cookware"},
            {"name": "Heavy Granite Mortar & Pestle", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Separate prawn heads from bodies; retain heads (prawn fat in heads makes the broth).",
            "Bruise lemongrass with cleaver; slice galangal; tear kaffir leaves.",
            "Crush bird's eye chilies gently to crack open without shredding."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Prawn Stock: Heat 1 tbsp oil in pot over medium-high heat. Add prawn heads and shells. Sauté for 4 minutes while crushing heads with a wooden spoon to express orange prawn tomalley (head fat). Pour in 900ml water. Simmer 8 minutes; strain through fine sieve into clean pot.",
                "sensoryCue": "Vibrant orange-tinted broth with sweet ocean prawn essence.",
                "scienceNote": "Prawn tomalley contains lipid-rich hepatopancreas fat containing astaxanthin pigments and free amino acids that provide immediate umami body.",
                "timerMins": 12
            },
            {
                "stepNum": 2,
                "text": "Infuse Aromatics: Bring strained broth to a boil. Add bruised lemongrass, galangal coins, and kaffir lime leaves. Simmer gently for 4 minutes to infuse essential oils.",
                "sensoryCue": "Explosive citrus, piney, and herbal perfume fills the kitchen.",
                "scienceNote": "Tearing kaffir leaves and bruising lemongrass ruptures plant oil cells, liberating citronellal and citral monoterpenes into hot water.",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Add Mushrooms & Seasoning: Stir in Nam Prik Pao (chili jam), fish sauce, and mushrooms. Simmer 2 minutes. (If making creamy Tom Yum Nam Khon, stir in 60ml evaporated milk now).",
                "sensoryCue": "Broth turns glossy orange-red with floating chili oil pearls.",
                "scienceNote": "Nam Prik Pao supplies fried shallots, garlic, and dried shrimp, rounding out the sharp citrus with sweet roasted savory tones.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Cook Prawns: Add whole prawn bodies and crushed bird's eye chilies. Simmer gently for 2 to 3 minutes just until prawns curl into a C-shape and turn opaque pink.",
                "sensoryCue": "Tender, juicy prawns with zero overcooking.",
                "scienceNote": "Shrimp muscle proteins denature and shrink rapidly above 145°F; cooking past 3 minutes causes muscle fiber contraction and rubbery texture.",
                "timerMins": 3
            },
            {
                "stepNum": 5,
                "text": "Finish with Lime Off Heat: Turn off heat completely. Stir in fresh lime juice and torn sawtooth herb. Taste broth: adjust balance (should be aggressively sour first, followed by salty, spicy, and subtle sweet). Ladle immediately into bowls.",
                "sensoryCue": "Fragrant fresh citrus steam; glistening orange broth with herbs.",
                "scienceNote": "Boiling lime juice degrades delicate ascorbic acid and turns volatile citric terpene molecules unpleasantly bitter; lime juice must ALWAYS be added off the heat.",
                "timerMins": 1
            }
        ],
        "sensoryIndicators": {
            "aroma": "Fragrant kaffir lime oil, piney galangal, roasted chili jam, fresh lime zest, ocean prawns",
            "texture": "Clear or lightly creamy searing broth with tender succulent prawns and spongy mushrooms",
            "finish": "Electrifying lime acidity followed by creeping chili heat and lingering fish sauce savoriness"
        },
        "scienceNotes": "Tom Yum is a masterclass in the five Thai flavor pillars. The dynamic equilibrium between citric acid (lime), sodium/glutamate (fish sauce), capsaicin (chilies), and sucrose (chili jam) triggers multi-modal sensory excitation.",
        "troubleshooting": {
            "Broth tastes flat and bitter": "Lime juice was boiled on high heat; always add lime juice after turning off flame.",
            "Weak, watery soup": "Prawn heads weren't sautéed and crushed; prawn head fat is the foundational flavor.",
            "Ginger taste instead of Thai": "Ginger was substituted for galangal; galangal has a distinct camphor/pine profile unlike ginger."
        },
        "substitutions": [
            {"ingredient": "River Prawns", "substitute": "Black Tiger Prawns or Sea Bass / Red Snapper fillets", "ratio": "1:1"},
            {"ingredient": "Sawtooth Herb", "substitute": "Fresh Cilantro & Thai Basil", "ratio": "1:1"}
        ],
        "flavorPairings": ["Steamed Jasmine Rice", "Thai Crab Fried Rice", "Singha Beer", "Thai Iced Tea"],
        "advancedTechnique": "Crushing prawn heads in mortar with 1 tbsp neutral oil before sautéing to extract 100% of the lipid-soluble carotenoid color.",
        "storageAndReheating": "Best eaten fresh within 2 hours. Reheat gently; do not boil after lime is added.",
        "nutritionEstimates": {"calories": 220, "protein": 28, "carbs": 12, "fat": 7},
        "relatedRecipes": ["rec-shakshuka-royale", "rec-tonkotsu-ramen", "rec-salmon-aburi-press"],
        "relatedTechniques": ["Off-heat citric acid preservation", "Crustacean hepatopancreas extraction", "Monoterpene bruise extraction"]
    },
    {
        "id": "rec-haemul-pajeon",
        "title": "Crispy Korean Haemul Pajeon (Scallion & Seafood Pancake with Choganjang)",
        "cuisine": "Korean / Classical Street & Pub",
        "category": "lunch",
        "slot": "opener",
        "difficulty": "Easy",
        "prepMins": 20,
        "cookMins": 12,
        "totalMins": 32,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ultimate rainy-day Korean feast: whole tender scallions laid parallel in a screaming-hot cast iron skillet, bound with an icy starch batter, studded with fresh squid, prawns, and oysters, crowned with a beaten egg and fried in generous oil until shatteringly crisp.",
        "dietary": [],
        "sensoryRole": "Shatteringly crispy golden edges, sweet tender charred scallions, succulent seafood, tangy spicy soy dip",
        "ingredients": [
            {"name": "Whole Fresh Scallions (Pa)", "qty": 14, "unit": "stalks", "prep": "trimmed to pan length, lightly crushed", "dept": "Produce"},
            {"name": "Fresh Squid (Calamari)", "qty": 150, "unit": "g", "prep": "cleaned and sliced into thin strips", "dept": "Seafood"},
            {"name": "Small Prawns / Shrimp", "qty": 120, "unit": "g", "prep": "peeled, deveined, halved lengthwise", "dept": "Seafood"},
            {"name": "All-Purpose Flour", "qty": 100, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Sweet Rice Flour or Cornstarch", "qty": 40, "unit": "g", "prep": "provides shattering crunch", "dept": "Baking & Pantry"},
            {"name": "Potato Starch", "qty": 20, "unit": "g", "prep": "for crisp perimeter", "dept": "Baking & Pantry"},
            {"name": "Ice-Cold Water (with Ice Cubes)", "qty": 180, "unit": "ml", "prep": "freezing cold", "dept": "Pantry"},
            {"name": "Large Egg", "qty": 1, "unit": "whole", "prep": "lightly beaten for topping", "dept": "Dairy & Fats"},
            {"name": "Red & Green Chili Peppers", "qty": 2, "unit": "whole", "prep": "sliced thinly on bias for garnish", "dept": "Produce"},
            {"name": "Korean Toasted Sesame Oil", "qty": 15, "unit": "ml", "prep": "pure cold pressed", "dept": "Pantry"},
            {"name": "High-Smoke Neutral Oil", "qty": 80, "unit": "ml", "prep": "for shallow frying", "dept": "Baking & Pantry"},
            {"name": "Choganjang Dipping Sauce", "qty": 60, "unit": "ml", "prep": "soy sauce, rice vinegar, gochugaru, sesame seeds, sugar", "dept": "Pantry"}
        ],
        "equipment": [
            {"name": "12-inch Heavy Cast-Iron Skillet", "type": "Cookware"},
            {"name": "Wide Metal Fish Spatula", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Wash and dry scallions thoroughly (excess surface water prevents crisping).",
            "Whisk flour, rice flour, potato starch, garlic powder, and salt together.",
            "Slice seafood and pat bone-dry with paper towels.",
            "Mix Choganjang sauce ingredients in small ramekin."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Ice Batter: Whisk dry flours with 180ml ice-cold water just until barely combined into a thin crepe-like batter (small lumps are fine; do not overmix). Keep batter cold.",
                "sensoryCue": "Thin, fluid batter; cold to touch.",
                "scienceNote": "Using ice water inhibits gluten development, while blending wheat flour with potato and rice starch creates a delicate, shatteringly crisp matrix rather than chewy bread.",
                "timerMins": 3
            },
            {
                "stepNum": 2,
                "text": "Sear Scallions: Heat 3 tbsp neutral oil in 12-inch cast iron skillet over medium-high heat until shimmering. Lay scallions across the pan in a tight parallel row. Sizzle for 60 seconds until scallions start to soften and char lightly.",
                "sensoryCue": "Aggressive sizzling sound; fragrant charred allium aroma.",
                "scienceNote": "Pre-searing scallions collapses their cellular moisture and caramelizes natural allium sugars before batter is poured.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Pour Batter & Add Seafood: Pour 3/4 of the cold batter evenly over the scallions, ensuring batter seeps between every stalk. Scatter sliced squid and prawns evenly over top. Drizzle remaining batter over seafood. Scatter sliced chilies.",
                "sensoryCue": "Batter sizzles and bubbles furiously in the hot oil.",
                "scienceNote": "Thermal shock between ice batter and 375°F oil causes rapid steam expansion, blowing microscopic crisp bubbles throughout the batter.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Egg Crown & The Flip: Pour beaten egg across top of pancake. Cook undisturbed over medium heat for 4-5 minutes until bottom is deeply golden-brown and crisp. Swirl 1 tbsp oil around pan edges. In one confident motion, flip the pancake over with wide spatula. Press down firmly with spatula.",
                "sensoryCue": "Deep golden-bronze crackling bottom; egg coats and seals seafood in place.",
                "scienceNote": "Egg forms a protein seal that binds the seafood securely to the pancake during the flip.",
                "timerMins": 5
            },
            {
                "stepNum": 5,
                "text": "Crisp Second Side: Drizzle 1 tbsp oil and 1 tsp sesame oil around perimeter. Fry for 3-4 minutes, pressing with spatula, until seafood is cooked through and pancake is intensely crispy on both sides. Slide onto cutting board, cut into bite-sized squares, and serve piping hot with Choganjang dip.",
                "sensoryCue": "Audible crackle when sliced with knife; steaming juicy seafood interior.",
                "scienceNote": "Sesame oil added at the very end provides toasted aroma without scorching.",
                "timerMins": 4
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted sesame oil, sweet charred scallions, sizzling sea squid, fried starch crunch",
            "texture": "Ultra-crispy glass-like exterior yielding to sweet tender scallions and succulent chewy seafood",
            "finish": "Tangy vinegar-soy kick that cuts the fried oil richness"
        },
        "scienceNotes": "The secret to restaurant-grade Korean pajeon crispness is the triple-starch blend: all-purpose flour for structure, rice flour for lightness, and potato starch for low gelatinization temperature glass-like brittleness, combined with ice-cold temperature shock.",
        "troubleshooting": {
            "Pancake is soggy or gummy": "Water was warm, batter was overmixed (excess gluten), or not enough oil was used in the pan.",
            "Pancake breaks apart during flip": "Flipped too early before the bottom had crisped into a cohesive crust.",
            "Seafood falls off pancake": "Top drizzle of batter and beaten egg was skipped; egg is the structural glue."
        },
        "substitutions": [
            {"ingredient": "Squid & Prawns", "substitute": "Kimchi and Pork Belly (for Kimchijeon)", "ratio": "1:1"},
            {"ingredient": "Potato Starch", "substitute": "Cornstarch or Tapioca Starch", "ratio": "1:1"}
        ],
        "flavorPairings": ["Korean Makgeolli (Sparkling Rice Wine)", "Cold Soju", "Banchan (Pickled Radish)", "Choganjang Dip"],
        "advancedTechnique": "Twirling the pancake in the pan during the final minute to allow centrifugal force to distribute hot oil to every corner of the perimeter.",
        "storageAndReheating": "Best eaten immediately. Leftovers re-crisp in a hot dry cast-iron skillet for 3 minutes per side.",
        "nutritionEstimates": {"calories": 380, "protein": 18, "carbs": 36, "fat": 19},
        "relatedRecipes": ["rec-french-rolled-omelette", "rec-shakshuka-royale", "rec-tonkotsu-ramen"],
        "relatedTechniques": ["Triple starch ratio balancing", "Ice-oil temperature shock", "Egg albumin seafood binding"]
    },
    {
        "id": "rec-birria-de-res",
        "title": "Birria de Res con Consomé (Slow-Braised Guajillo Beef Shank & Quesabirria)",
        "cuisine": "Mexican / Jalisco Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 40,
        "cookMins": 210,
        "totalMins": 250,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=1200&q=80",
        "summary": "The soul of Jalisco: bone-in beef shank and chuck roast slow-braised in a rich, velvety adobo of toasted Guajillo, Ancho, and Pasilla chilies, charred aromatics, Mexican cinnamon, cloves, and Mexican oregano. Served as shred-tender beef with steaming bowls of cilantro-flecked rich consomé and griddled quesabirria tacos.",
        "dietary": ["Gluten-Free"],
        "sensoryRole": "Deep earthy chili warmth, melt-in-mouth beef collagen, rich glistening chili fat, crispy griddled corn tortilla",
        "ingredients": [
            {"name": "Bone-In Beef Shank (with Marrow)", "qty": 1000, "unit": "g", "prep": "thick cut (supplies rich collagen & broth body)", "dept": "Meat & Poultry"},
            {"name": "Beef Chuck Roast", "qty": 1000, "unit": "g", "prep": "cut into 3-inch cubes", "dept": "Meat & Poultry"},
            {"name": "Dried Guajillo Chilies", "qty": 8, "unit": "pods", "prep": "stemmed and seeded", "dept": "Spices & Botanicals"},
            {"name": "Dried Ancho Chilies", "qty": 4, "unit": "pods", "prep": "stemmed and seeded", "dept": "Spices & Botanicals"},
            {"name": "Dried Pasilla / Cascabel Chilies", "qty": 2, "unit": "pods", "prep": "stemmed and seeded", "dept": "Spices & Botanicals"},
            {"name": "Fire-Roasted Roma Tomatoes", "qty": 4, "unit": "whole", "prep": "charred in skillet", "dept": "Produce"},
            {"name": "White Onion & Garlic Head", "qty": 1, "unit": "whole", "prep": "onion quartered, garlic unpeeled and charred", "dept": "Produce"},
            {"name": "Apple Cider Vinegar", "qty": 60, "unit": "ml", "prep": "for adobo acid balance", "dept": "Pantry"},
            {"name": "Mexican Cinnamon (Canela)", "qty": 1, "unit": "stick", "prep": "true Ceylon cinnamon", "dept": "Spices & Botanicals"},
            {"name": "Mexican Oregano, Cumin, Cloves, Allspice", "qty": 12, "unit": "g", "prep": "toasted and ground", "dept": "Spices & Botanicals"},
            {"name": "Corn Tortillas & Oaxaca Cheese", "qty": 16, "unit": "tortillas", "prep": "for quesabirria assembly", "dept": "Baking & Pantry"},
            {"name": "Finely Minced White Onion & Fresh Cilantro", "qty": 80, "unit": "g", "prep": "for consomé garnish", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "Large Enameled Cast-Iron Dutch Oven (7-8 quart)", "type": "Cookware"},
            {"name": "High-Speed Blender", "type": "Small Appliance"},
            {"name": "Fine Mesh Chinois Strainer", "type": "Small Tool"},
            {"name": "Flat Comal / Cast Iron Griddle", "type": "Cookware"}
        ],
        "miseEnPlace": [
            "Toast dried chilies in dry skillet for 30 seconds until fragrant (do not burn); soak in 500ml boiling water for 15 minutes.",
            "Char onion, garlic, and tomatoes on comal until blackened in spots.",
            "Season beef shank and chuck generously with coarse salt."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Sear Beef: In large Dutch oven, heat 2 tbsp oil over high heat. Sear beef shank and chuck cubes in batches for 8-10 minutes until deeply browned with dark crust. Remove beef to a platter.",
                "sensoryCue": "Deep sizzling fond coating Dutch oven bottom; roasted beef aroma.",
                "scienceNote": "Intense Maillard browning produces flavor compounds that dissolve into the adobo during the slow braise.",
                "timerMins": 12
            },
            {
                "stepNum": 2,
                "text": "Blend Adobo: In high-speed blender, combine soaked rehydrated chilies (with their soaking water), charred tomatoes, peeled charred garlic, charred onion, apple cider vinegar, canela stick, Mexican oregano, cumin, cloves, allspice, and 1 tbsp salt. Blend on high for 2 full minutes until velvety smooth. Strain adobo through fine mesh directly into Dutch oven.",
                "sensoryCue": "Vibrant brick-red, fragrant, silky chili puree.",
                "scienceNote": "Straining removes fibrous chili skins, ensuring the consomé is velvety smooth rather than grainy.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "The Slow Braise: Return seared beef, marrow bones, and bay leaves to the Dutch oven. Add 1.5 liters beef stock or water (liquid should just cover meat). Bring to a simmer, cover tightly with foil and lid. Transfer to 300°F (150°C) oven for 3.5 hours until beef is fall-apart tender.",
                "sensoryCue": "Beef shreds effortlessly with a fork; rich red chili fat pools at surface.",
                "scienceNote": "Slow 300°F convection allows tough collagen in beef shank to slowly hydrolyze into gelatin without drying out muscle fibers.",
                "timerMins": 210
            },
            {
                "stepNum": 4,
                "text": "Skim Fat & Shred: Transfer tender beef to cutting board; shred with two forks, discarding bones and gristle. Skim the gleaming orange-red chili beef fat (grasa) from top of broth into a small bowl (this fat is used to fry the tortillas!). Keep broth hot on stove.",
                "sensoryCue": "Shredded beef glistening with spices; rich red dipping broth.",
                "scienceNote": "Chili pigments (capsanthin and capsorubin) are fat-soluble, migrating into the beef fat during cooking, creating the intensely red frying fat.",
                "timerMins": 15
            },
            {
                "stepNum": 5,
                "text": "Make Quesabirria Tacos: Dip corn tortillas into the reserved red birria fat. Place on hot griddle over medium heat. Top with shredded Oaxaca cheese and shredded beef. Fold in half into a taco. Griddle 2 minutes per side until tortilla is crackling-crisp and cheese is melted and bubbling. Serve immediately with a bowl of hot consomé garnished with minced onion, cilantro, and lime.",
                "sensoryCue": "Crisp red-lacquered tortilla shell; stretchy melted cheese; dipping taco into steaming consomé.",
                "scienceNote": "Dipping the taco into the hot consomé creates instant contrast: crisp tortilla softening in rich gelatinous broth.",
                "timerMins": 8
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted guajillo earthiness, Mexican oregano, canela clove warmth, rich beef marrow broth, crispy corn",
            "texture": "Shattering griddled taco shell, stretchy molten cheese, succulent melting beef, velvety rich consomé",
            "finish": "Warming chili hum balanced by bright lime acidity and fresh cilantro"
        },
        "scienceNotes": "Birria consomé achieves its luxurious viscosity through gelatin extracted from beef shank bones and marrow. Apple cider vinegar balances the rich gelatin and melted tallow, cutting the fat on the palate.",
        "troubleshooting": {
            "Consomé tastes bitter": "Chilies were scorched/burned during dry toasting; toast for only 20-30 seconds until pliable.",
            "Beef is tough and chewy": "Braise was not cooked long enough; connective tissue requires full 3-3.5 hours at 300°F.",
            "Tortillas tear when dipped": "Use quality corn tortillas, or double-stack two tortillas per quesabirria."
        },
        "substitutions": [
            {"ingredient": "Beef Shank & Chuck", "substitute": "Bone-In Goat Shoulder (Chivo) or Lamb Shank", "ratio": "Traditional Jalisco style"},
            {"ingredient": "Oaxaca Cheese", "substitute": "Queso Asadero, Mozzarella, or Monterey Jack", "ratio": "1:1"}
        ],
        "flavorPairings": ["Ice-Cold Mexican Cerveza (Negra Modelo)", "Agua de Horchata", "Pickled Red Onions", "Lime Wedges"],
        "advancedTechnique": "Using a combination of bone marrow and roasted beef knuckles to enrich the consomé with maximum natural collagen body.",
        "storageAndReheating": "Birria improves dramatically after overnight chilling. Keeps refrigerated up to 5 days, or freeze 3 months.",
        "nutritionEstimates": {"calories": 640, "protein": 44, "carbs": 32, "fat": 38},
        "relatedRecipes": ["rec-chilaquiles-rojos", "rec-lomo-saltado", "rec-tonkotsu-ramen"],
        "relatedTechniques": ["Chili rehydration adobo blending", "Collagen braise hydrolysis", "Fat-soluble carotenoid skimming"]
    },
    {
        "id": "rec-dal-makhani",
        "title": "Dal Makhani Bukhara Style (Slow-Simmered Black Lentils with Cultured Butter)",
        "cuisine": "Indian / Mughlai & Punjabi Classical",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Easy",
        "prepMins": 30,
        "cookMins": 180,
        "totalMins": 210,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=1200&q=80",
        "summary": "The legendary crown of North Indian dal: whole black urad lentils (sabut urad) and red kidney beans (rajma) soaked overnight and slow-simmered for hours over gentle embers with fresh tomato puree, Kashmiri chili, ginger, cultured white butter (makhan), and heavy cream.",
        "dietary": ["Vegetarian", "Gluten-Free"],
        "sensoryRole": "Ultra-creamy, velvety, comforting warmth with earthy lentils, sweet tomato tang, and smoky butter richness",
        "ingredients": [
            {"name": "Whole Black Urad Dal (Black Gram)", "qty": 250, "unit": "g", "prep": "soaked in water for 12 hours", "dept": "Grains & Starches"},
            {"name": "Red Kidney Beans (Rajma)", "qty": 50, "unit": "g", "prep": "soaked with the dal", "dept": "Grains & Starches"},
            {"name": "Fresh Tomato Puree", "qty": 350, "unit": "g", "prep": "finely pureed ripe tomatoes", "dept": "Produce"},
            {"name": "Cultured White Butter (Makhan) or European Butter", "qty": 100, "unit": "g", "prep": "divided: 40g cook, 60g finish", "dept": "Dairy & Fats"},
            {"name": "Heavy Cream (36% fat)", "qty": 100, "unit": "ml", "prep": "fresh dairy", "dept": "Dairy & Fats"},
            {"name": "Ginger-Garlic Paste", "qty": 30, "unit": "g", "prep": "50/50 freshly ground", "dept": "Produce"},
            {"name": "Kashmiri Red Chili Powder", "qty": 15, "unit": "g", "prep": "vibrant red color without blistering heat", "dept": "Spices & Botanicals"},
            {"name": "Kasuri Methi (Dried Fenugreek Leaves)", "qty": 4, "unit": "g", "prep": "lightly toasted and crushed between palms", "dept": "Spices & Botanicals"},
            {"name": "Garam Masala", "qty": 4, "unit": "g", "prep": "freshly ground royal spice blend", "dept": "Spices & Botanicals"},
            {"name": "Fine Sea Salt", "qty": 8, "unit": "g", "prep": "to taste", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Heavy-Bottom Dutch Oven or Degchi", "type": "Cookware"},
            {"name": "Potato Masher or Wooden Mathani", "type": "Small Tool"},
            {"name": "Pressure Cooker or Instant Pot (Optional)", "type": "Small Appliance"}
        ],
        "miseEnPlace": [
            "Wash black urad dal and kidney beans in 4 changes of water until water runs clear; soak overnight with a pinch of baking soda.",
            "Puree fresh tomatoes until completely smooth.",
            "Toast kasuri methi in dry pan for 20 seconds; crush between palms."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "The Initial Simmer: Drain soaked dal and rajma. Place in heavy pot with 1.2 liters fresh water, 1 tsp salt, and 1 tsp Kashmiri chili powder. Bring to a boil, then cover and simmer gently for 90 minutes (or 35 minutes in pressure cooker) until lentils are completely tender and crush easily between thumb and finger.",
                "sensoryCue": "Lentils are soft and splitting; cooking water turns dark purple-brown.",
                "scienceNote": "Extended soaking and cooking gelatinizes the dense starch and softens the thick black seed coats of whole urad dal.",
                "timerMins": 90
            },
            {
                "stepNum": 2,
                "text": "Make Tomato-Tarka Base: In a separate pan, melt 40g butter over medium heat. Add ginger-garlic paste; sauté 2 minutes until raw aroma dissipates. Add pureed tomatoes and remaining Kashmiri chili. Cook stirring for 8-10 minutes until tomato water evaporates and butter begins to separate at edges.",
                "sensoryCue": "Deep glossy crimson tomato reduction with fragrant ginger-garlic perfume.",
                "scienceNote": "Cooking tomato puree until fat separates caramelizes tomato sugars and ensures no raw acidic tomato notes taint the dal.",
                "timerMins": 10
            },
            {
                "stepNum": 3,
                "text": "Combine & The Great Mash: Pour tomato-tarka base into the cooked lentils. Mash 30% of the lentils against the side of the pot using a potato masher or back of a ladle. Stir well. Add 200ml boiling water if mixture is too thick.",
                "sensoryCue": "Broth thickens instantly into a creamy, luxurious gravy.",
                "scienceNote": "Mashing releases starches and proteins from inside the lentil cotyledons, which act as a natural thickener and emulsifier for the butter.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "The Slow Bukhara Simmer: Simmer dal over lowest possible heat for 60 to 90 minutes, stirring every 10 minutes to prevent bottom sticking. The dal will transform from dark brown to a velvety, creamy mahogany.",
                "sensoryCue": "Gentle slow eruption of thick creamy bubbles; rich comforting aroma.",
                "scienceNote": "Extended slow simmering allows starch and fat to fully emulsify, creating the signature velvety texture that defines Dal Bukhara.",
                "timerMins": 75
            },
            {
                "stepNum": 5,
                "text": "The Finish: Stir in remaining 60g butter, heavy cream, garam masala, and crushed toasted kasuri methi. Simmer for 5 more minutes. Swirl additional cream and a slab of cultured butter on top for presentation. Serve with garlic butter naan or basmati rice.",
                "sensoryCue": "Glossy mahogany dal with white cream swirl; intoxicating aroma of fenugreek and cultured butter.",
                "scienceNote": "Kasuri methi contains sotolon, an aromatic compound with maple-caramel notes that synergizes with butterfat to create signature Mughlai depth.",
                "timerMins": 5
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted kasuri methi, rich cultured butter, sweet cooked ginger, warm garam masala, earthy black lentils",
            "texture": "Ultra-creamy, velvety, luxurious mouth-coating gravy studded with tender whole lentils",
            "finish": "Rich buttery sweetness balanced by gentle tomato tang and aromatic fenugreek"
        },
        "scienceNotes": "Authentic Dal Bukhara (made famous by ITC Maurya in New Delhi) is traditionally cooked for 18 hours over the dying embers of a tandoor. The continuous gentle heat breaks down the complex oligosaccharides in black lentils while emulsifying enormous amounts of cultured butter into the starch matrix.",
        "troubleshooting": {
            "Dal remains watery with lentils sinking": "Lentils weren't mashed; mashing 30% of lentils is mandatory to release starch thickener.",
            "Lentils remain hard and gritty": "Lentils weren't soaked long enough, or salt/acid was added too early in the cook.",
            "Tastes like raw tomato soup": "Tomato puree wasn't cooked down sufficiently in step 2 before combining with dal."
        },
        "substitutions": [
            {"ingredient": "Cultured White Butter", "substitute": "European Cultured Butter (82% fat) or Ghee", "ratio": "1:1"},
            {"ingredient": "Heavy Cream", "substitute": "Cashew Cream (for Vegan version)", "ratio": "1:1"}
        ],
        "flavorPairings": ["Garlic Butter Naan", "Tandoori Roti", "Jeera Rice", "Mango Lassi"],
        "advancedTechnique": "Dhungar smoking method: placing a glowing piece of charcoal in a small metal bowl atop the dal, pouring ghee over coal, and covering with lid for 3 minutes to infuse authentic tandoor smoke.",
        "storageAndReheating": "Dal Makhani tastes significantly better on day 2 and day 3 as starches and spices harmonize. Keeps refrigerated 5 days.",
        "nutritionEstimates": {"calories": 390, "protein": 14, "carbs": 38, "fat": 22},
        "relatedRecipes": ["rec-shakshuka-royale", "rec-cilbir-turkish-eggs", "rec-paella-valenciana"],
        "relatedTechniques": ["Starch cotyledon mashing", "Kasuri methi sotolon bloom", "Extended low-temperature emulsification"]
    },
    {
        "id": "rec-risotto-porcini",
        "title": "Risotto ai Funghi Porcini (Carnaroli Rice, Wild Porcini & Parmigiano Mantecatura)",
        "cuisine": "Italian / Piedmontese Classical",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Intermediate",
        "prepMins": 20,
        "cookMins": 25,
        "totalMins": 45,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=1200&q=80",
        "summary": "The masterclass of Northern Italian grain cookery: superfino Carnaroli rice toasted in butter, deglazed with crisp dry white wine, and slow-nourished with steaming porcini mushroom broth, finished off the heat with the vigorous emulsification (mantecatura) of frozen cultured butter and 24-month Parmigiano-Reggiano into a flowing wave (all'onda).",
        "dietary": ["Vegetarian", "Gluten-Free"],
        "sensoryRole": "Unctuous creamy wave, deep earthy forest umami, nutty cheese savoriness, al dente rice bite",
        "ingredients": [
            {"name": "Carnaroli Superfino Rice (or Vialone Nano)", "qty": 320, "unit": "g", "prep": "the 'king of risotto rices', never washed", "dept": "Grains & Starches"},
            {"name": "Dried Porcini Mushrooms (Boletus Edulis)", "qty": 35, "unit": "g", "prep": "rehydrated in 500ml boiling water, liquid reserved", "dept": "Pantry"},
            {"name": "Fresh Cremini or Wild Chanterelle Mushrooms", "qty": 200, "unit": "g", "prep": "sliced and sautéed golden", "dept": "Produce"},
            {"name": "Shallot", "qty": 2, "unit": "medium", "prep": "minced into microscopic brunoise", "dept": "Produce"},
            {"name": "Crisp Dry White Wine (Pinot Grigio or Gavi)", "qty": 120, "unit": "ml", "prep": "chilled", "dept": "Pantry"},
            {"name": "Rich Vegetable or Chicken Stock", "qty": 1000, "unit": "ml", "prep": "simmering hot (combined with strained porcini soaking broth)", "dept": "Pantry"},
            {"name": "Unsalted European Butter (82% fat)", "qty": 80, "unit": "g", "prep": "divided: 30g toasting, 50g frozen cubes for mantecatura", "dept": "Dairy & Fats"},
            {"name": "Parmigiano-Reggiano D.O.P. (24-Month)", "qty": 70, "unit": "g", "prep": "finely microplaned", "dept": "Dairy & Fats"},
            {"name": "Fresh Flat-Leaf Italian Parsley", "qty": 15, "unit": "g", "prep": "finely chopped", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "Wide Heavy Copper Sauté Pan or Saucier", "type": "Cookware"},
            {"name": "Wooden Risotto Spoon (with center hole)", "type": "Small Tool"},
            {"name": "Small Ladle", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Rehydrate dried porcini in boiling water for 20 minutes; strain soaking liquid through coffee filter to remove grit and add to stockpot.",
            "Keep mushroom stock at a bare simmer on adjacent burner.",
            "Freeze 50g diced butter cubes for mantecatura; grate Parmigiano finely."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Soffritto & Tostatura: Melt 30g butter in wide saucier over medium-low heat. Add shallot brunoise and pinch of salt; cook 3 minutes until translucent without browning. Add Carnaroli rice. Toast rice (tostatura) for 2 to 3 minutes, stirring constantly, until edges turn translucent and grains feel hot to the touch and emit a nutty toasted aroma.",
                "sensoryCue": "Grains click against pan like pebbles; warm nutty toasted perfume.",
                "scienceNote": "Tostatura par-cooks surface starches, hardening the outer grain perimeter to prevent it from turning to mush during simmering while preserving an al dente core.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Sfumatura (Deglaze): Pour in the 120ml dry white wine. It will hiss violently. Stir continuously for 90 seconds until alcohol aroma cooks off and wine is completely absorbed by the rice.",
                "sensoryCue": "Vigorous hissing steam cloud; sharp wine aroma gives way to rich fruit acidity.",
                "scienceNote": "Tartaric and malic acids from wine brighten the dish and lower pH, regulating starch breakdown.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Cottura (The Simmer): Add chopped rehydrated porcini. Begin adding simmering mushroom broth 1-2 ladles at a time, maintaining a constant lively simmer. Stir frequently with wooden spoon. Only add more broth when the previous addition has been almost completely absorbed. Continue for 15 to 17 minutes until rice is al dente (tender exterior with subtle firm white core when bitten).",
                "sensoryCue": "Creamy starch sauce begins to form around plump grains; rich earthy woodland aroma.",
                "scienceNote": "Frequent stirring creates mechanical friction between grains, sloughing off amylopectin starch into the broth to form a natural creamy emulsion.",
                "timerMins": 16
            },
            {
                "stepNum": 4,
                "text": "Riposo (The Rest): Remove saucier completely from heat. Fold in sautéed fresh mushrooms. Let rest undisturbed for 1 full minute off heat.",
                "sensoryCue": "Bubbling subsides; temperature drops slightly to 160-170°F.",
                "scienceNote": "Resting lowers temperature just enough so the cheese and butterfat will emulsify rather than melt into an oily grease slick.",
                "timerMins": 1
            },
            {
                "stepNum": 5,
                "text": "Mantecatura (The Emulsion): Add frozen butter cubes and microplaned Parmigiano-Reggiano. Using the wooden spoon and a rapid back-and-forth flick of the wrist, beat and agitate the risotto violently for 90 seconds (la mantecatura) until a gleaming, velvety, creamy sauce coats every grain. Add a splash of hot broth if needed to achieve 'all'onda' (flowing wave). Plate immediately onto flat warm plates; rap bottom of plate with palm so risotto settles into an even sheet.",
                "sensoryCue": "Gleaming glossy sheen; risotto waves gently when pan is shaken; aroma of aged cheese and porcini.",
                "scienceNote": "Beating frozen butter into warm starch forces dairy fat and water into a stable emulsion with cheese proteins, without breaking into oil.",
                "timerMins": 2
            }
        ],
        "sensoryIndicators": {
            "aroma": "Earthy wild porcini, 24-month Parmigiano-Reggiano, sweet toasted shallots, white wine acidity, rich butter",
            "texture": "Perfect al dente bite to each distinct grain suspended in an ultra-creamy, wave-like emulsion",
            "finish": "Persistent forest umami and savory Parmigiano depth"
        },
        "scienceNotes": "Carnaroli rice is considered superior to Arborio because it has higher amylose content (approx 24% vs 18%). Amylose maintains structural rigidity at the grain core, while outer amylopectin starches dissolve into the cooking broth to create the signature luxurious cream.",
        "troubleshooting": {
            "Risotto is stiff and stands in a mound": "Risotto is too dry; add 2 ladles hot broth during mantecatura to make it flow like a wave (all'onda).",
            "Oily melted butter separates": "Butter was added while pan was still on the flame; always perform mantecatura OFF the heat.",
            "Grains are mushy with broken centers": "Rice was overcooked past 18 minutes, or low-quality rice was used."
        },
        "substitutions": [
            {"ingredient": "Carnaroli Rice", "substitute": "Vialone Nano or Superfino Arborio", "ratio": "1:1"},
            {"ingredient": "Parmigiano-Reggiano", "substitute": "Grana Padano or Pecorino Romano", "ratio": "1:1"}
        ],
        "flavorPairings": ["Barolo or Nebbiolo", "Sautéed Duck Breast", "Shaved Black Truffle", "Roasted Hazelnuts"],
        "advancedTechnique": "Infusing finishing butter with freshly grated nutmeg and porcini powder for ultra-concentrated woodland depth.",
        "storageAndReheating": "Risotto cannot be properly reheated without losing al dente texture; use leftovers to make crispy Arancini (fried stuffed rice balls).",
        "nutritionEstimates": {"calories": 480, "protein": 12, "carbs": 58, "fat": 22},
        "relatedRecipes": ["rec-paella-valenciana", "rec-potato-pave", "rec-peppercorn-sauce"],
        "relatedTechniques": ["Mantecatura off-heat emulsion", "Tostatura starch hardening", "All'onda fluid wave rheology"]
    },
    {
        "id": "rec-pizza-margherita",
        "title": "Pizza Napoletana Verace Margherita (72-Hour Cold Ferment, San Marzano & Fior di Latte)",
        "cuisine": "Italian / Neapolitan Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Advanced",
        "prepMins": 40,
        "cookMins": 6,
        "totalMins": 46,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=1200&q=80",
        "summary": "The sacred benchmark of the Associazione Verace Pizza Napoletana (AVPN): 65% hydration dough cold-fermented for 72 hours for explosive leopard-spotted cornicione (crust puff), topped with crushed San Marzano D.O.P. tomatoes, fresh Fior di Latte mozzarella, fragrant basil, and extra virgin olive oil, baked at extreme heat.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Charred smoky leopard spotting, blistered airy crust, sweet volcanic tomato acidity, milky fresh mozzarella melt",
        "ingredients": [
            {"name": "Italian Tipo 00 Flour (Caputo Pizzeria or Cuoco)", "qty": 500, "unit": "g", "prep": "high-protein wheat flour (W280-320)", "dept": "Baking & Pantry"},
            {"name": "Cold Filtered Water", "qty": 325, "unit": "ml", "prep": "65% hydration", "dept": "Pantry"},
            {"name": "Fine Sea Salt", "qty": 14, "unit": "g", "prep": "2.8% baker's percentage", "dept": "Baking & Pantry"},
            {"name": "Instant Dry Yeast (or Fresh Yeast)", "qty": 1.2, "unit": "g", "prep": "minimal yeast for long ferment", "dept": "Baking & Pantry"},
            {"name": "San Marzano D.O.P. Whole Peeled Tomatoes", "qty": 400, "unit": "g", "prep": "hand-crushed with 4g salt (never cooked!)", "dept": "Pantry"},
            {"name": "Fresh Fior di Latte Mozzarella (Cow's Milk)", "qty": 250, "unit": "g", "prep": "torn and drained in sieve 2 hours", "dept": "Dairy & Fats"},
            {"name": "Fresh Genovese Basil Leaves", "qty": 16, "unit": "leaves", "prep": "fresh tender leaves", "dept": "Produce"},
            {"name": "Extra Virgin Olive Oil", "qty": 30, "unit": "ml", "prep": "for spiral drizzle", "dept": "Dairy & Fats"},
            {"name": "Semolina Flour (Semola Rimacinata)", "qty": 60, "unit": "g", "prep": "for dusting pizza peel", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Outdoor Pizza Oven (Ooni, Roccbox) or 550°F Oven with Baking Steel", "type": "Cookware"},
            {"name": "12-inch Perforated Aluminum Pizza Peel", "type": "Small Tool"},
            {"name": "Dough Proofing Containers", "type": "Baking Supply"}
        ],
        "miseEnPlace": [
            "Mix dough, perform 3 stretch-and-folds, divide into 4 balls (approx 210g each), and cold-ferment in refrigerator for 48 to 72 hours.",
            "Bring dough balls to room temperature (68-72°F) for 3 hours before stretching.",
            "Tear mozzarella into strips and drain in a colander for 2 hours to eliminate excess water that causes soupy pizza.",
            "Crush San Marzano tomatoes by hand with 4g sea salt; do not cook or puree."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Preheat Baking Environment: If using home oven, place heavy 3/8-inch baking steel on highest rack. Preheat at maximum 550°F (285°C) for 60 full minutes, then switch to high broiler for 10 minutes before launching (if using outdoor oven, heat stone to 850-900°F / 450-480°C).",
                "sensoryCue": "Radiant heat shimmering from steel/stone.",
                "scienceNote": "High conductive heat transfer is required to flash-boil trapped water into steam within 60 seconds, creating explosive crust volume.",
                "timerMins": 60
            },
            {
                "stepNum": 2,
                "text": "Open the Dough: Dust dough ball in semolina flour. Press fingertips from center outward, pushing trapped gas bubbles toward the outer 1-inch perimeter to form the cornicione rim (NEVER touch or flatten the outer rim!). Pick up dough and drape over knuckles, rotating in a circle to stretch to a 10-12 inch disc. Center should be paper-thin (almost translucent).",
                "sensoryCue": "Plump puffy outer rim; thin extensible center with visible fermentation micro-bubbles.",
                "scienceNote": "Rolling pins destroy the carbon dioxide alveoli created by 72-hour fermentation. Finger-stretching preserves bubble walls.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Sauce & Cheese: Lay stretched dough onto lightly dusted peel. Spoon 70g crushed San Marzano tomatoes onto center; spiral outward with back of spoon up to the rim. Distribute 60g drained mozzarella strips across tomato. Scatter 4 basil leaves. Drizzle a gentle swirl of extra virgin olive oil.",
                "sensoryCue": "Vibrant red tomato against white mozzarella and green basil.",
                "scienceNote": "San Marzano tomatoes grown in volcanic soil near Mount Vesuvius have high natural pectin, lower acidity, and dense flesh that thickens perfectly during flash-baking.",
                "timerMins": 1
            },
            {
                "stepNum": 4,
                "text": "The Bake: Jiggle peel to ensure dough slides freely. Launch pizza onto screaming-hot baking steel. If in 900°F oven, bake 60-90 seconds, rotating with turning peel every 20 seconds. (If in 550°F home oven on steel under broiler, bake 4 to 5 minutes until cornicione is puffed, blistered, and leopard-spotted with dark char spots).",
                "sensoryCue": "Crust puffs up dramatically like a balloon; cheese bubbles furiously; black leopard char spots appear.",
                "scienceNote": "Leopard spots (maculatura) occur where micro-blisters of dough touch extreme radiant heat, caramelizing instantly into paper-thin crisp charred crust.",
                "timerMins": 4
            },
            {
                "stepNum": 5,
                "text": "Slice & Serve: Slide pizza onto cutting board. Garnish with a few fresh raw basil leaves and a final tiny drizzle of extra virgin olive oil. Slice with pizza rocker wheel into 4 or 6 slices; serve piping hot.",
                "sensoryCue": "Crust crackles lightly when pressed; tender, cloud-like interior crumb; aroma of wood smoke and sweet tomatoes.",
                "scienceNote": "Authentic Neapolitan pizza is soft, pliable, and foldable ('a portafoglio') rather than rigid like New York or Chicago style.",
                "timerMins": 1
            }
        ],
        "sensoryIndicators": {
            "aroma": "Charred wood smoke, toasted fermented wheat, sweet volcanic San Marzano tomatoes, fresh basil, grassy olive oil",
            "texture": "Crisp paper-thin blistered skin yielding to cloud-soft, airy, tender chewy crumb; molten milky mozzarella",
            "finish": "Clean, bright tomato acidity balanced by sweet dairy and rich olive oil"
        },
        "scienceNotes": "Cold fermentation at 38°F (3°C) for 72 hours slows yeast metabolism while allowing protease and amylase enzymes to break complex starches into maltose and glucose. This creates unprecedented flavor complexity and dramatic leopard-spotted charring during the bake.",
        "troubleshooting": {
            "Pizza sticks to peel upon launch": "Dough was left on peel too long before launching, or too little dusting flour was used. Always shake peel before launching.",
            "Pale crust with no char spots": "Baking surface was not hot enough; preheat steel for full 60 minutes.",
            "Watery puddle on pizza center": "Mozzarella was not drained, or canned tomatoes were pureed in a blender (blenders release excess water)."
        },
        "substitutions": [
            {"ingredient": "Tipo 00 Flour", "substitute": "High-Protein Bread Flour (12.7%)", "ratio": "1:1"},
            {"ingredient": "Fior di Latte", "substitute": "Mozzarella di Bufala Campana D.O.P. (drain 4 hours)", "ratio": "1:1 for luxury buffalo mozzarella"}
        ],
        "flavorPairings": ["Italian Peroni Nastro Azzurro", "Campanian Greco di Tufo", "Aperol Spritz", "Gelato Fior di Latte"],
        "advancedTechnique": "Pre-fermenting with Biga or Poolish (100% hydration pre-ferment) to amplify lactic and acetic sourdough acidity.",
        "storageAndReheating": "Reheat leftover slices in dry cast-iron skillet over medium heat for 3 minutes, then cover with lid for 1 minute to melt cheese.",
        "nutritionEstimates": {"calories": 420, "protein": 18, "carbs": 58, "fat": 14},
        "relatedRecipes": ["rec-fior-di-latte-gelato", "rec-risotto-porcini", "rec-quiche-lorraine"],
        "relatedTechniques": ["Baking steel high thermal conduction", "72-hour enzymatic cold fermentation", "Cornicione gas bubble preservation"]
    },
    {
        "id": "rec-pain-de-campagne",
        "title": "Artisan Sourdough Pain de Campagne (80% Hydration French Country Boule)",
        "cuisine": "French / Classical Boulangerie",
        "category": "bread",
        "slot": "accompaniment",
        "difficulty": "Advanced",
        "prepMins": 60,
        "cookMins": 45,
        "totalMins": 105,
        "yieldServings": 10,
        "heroImage": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "summary": "The soul of the French countryside: a rustic high-hydration naturally leavened country sourdough boule. Crafted with wild levain, stoneground dark rye, whole wheat, and high-protein bread flour, cold-retarded for 18 hours and baked inside a blistering Dutch oven to achieve a singing, blistered, mahogany crust with an open, custard-like crumb.",
        "dietary": ["Vegan"],
        "sensoryRole": "Deep crackling mahogany crust, blistered ears, complex wild lactic acidity, open glossy custard crumb",
        "ingredients": [
            {"name": "Unbleached Bread Flour (12.7% protein)", "qty": 400, "unit": "g", "prep": "hard red spring wheat", "dept": "Baking & Pantry"},
            {"name": "Whole Wheat Flour", "qty": 70, "unit": "g", "prep": "stoneground", "dept": "Baking & Pantry"},
            {"name": "Stoneground Dark Rye Flour", "qty": 30, "unit": "g", "prep": "adds enzymatic activity & earthy notes", "dept": "Baking & Pantry"},
            {"name": "Filtered Water (90°F / 32°C)", "qty": 400, "unit": "ml", "prep": "divided: 375ml autolyse, 25ml with salt (80% hydration)", "dept": "Pantry"},
            {"name": "Active Ripe Sourdough Starter (Levain)", "qty": 100, "unit": "g", "prep": "fed 100% hydration, used at peak rise", "dept": "Baking & Pantry"},
            {"name": "Fine Sea Salt", "qty": 11, "unit": "g", "prep": "2.2% baker's percentage", "dept": "Baking & Pantry"},
            {"name": "Rice Flour (50/50 with All-Purpose)", "qty": 30, "unit": "g", "prep": "for dusting banneton proofing basket", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Heavy 5 to 6-Quart Cast-Iron Dutch Oven (or Combo Cooker)", "type": "Cookware"},
            {"name": "Round Cane Banneton (Proofing Basket, 9-inch)", "type": "Baking Supply"},
            {"name": "Baker's Lame (Curved Razor Blade)", "type": "Cutlery"},
            {"name": "Digital Scale & Bench Knife", "type": "Precision Tool"}
        ],
        "miseEnPlace": [
            "Feed wild sourdough starter 4-5 hours prior; ensure it passes float test in water.",
            "Dust round proofing banneton generously with rice flour-wheat blend.",
            "Preheat Dutch oven inside oven at 500°F (260°C) for 60 minutes."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Autolyse: In a large bowl, mix bread flour, whole wheat flour, and dark rye with 375ml warm water until no dry flour remains. Cover and rest for 60 minutes.",
                "sensoryCue": "Shaggy dough mass; relaxes into supple cohesive dough over 60 mins.",
                "scienceNote": "Autolyse allows water to hydrate flour proteins and activates endogenous protease enzymes that relax gluten bonds, making high-hydration dough pliable without mechanical kneading.",
                "timerMins": 60
            },
            {
                "stepNum": 2,
                "text": "Incorporate Levain & Salt: Spread 100g active levain across top of dough; dimple in with fingertips. Perform slap-and-fold for 3 minutes. Rest 20 minutes. Sprinkle 11g sea salt and remaining 25ml water over dough; pinch and fold until salt grains dissolve completely and dough turns glossy.",
                "sensoryCue": "Dough tightens and becomes smooth, silky, and elastic.",
                "scienceNote": "Salt draws out water, strengthens gluten bonds, and regulates wild yeast and lactic acid bacteria fermentation speed.",
                "timerMins": 5
            },
            {
                "stepNum": 3,
                "text": "Bulk Fermentation with Coil Folds: Place dough in transparent container. Keep at 78°F (26°C) for 4 to 5 hours. Perform 4 sets of stretch-and-folds / coil folds spaced 30 minutes apart during first 2 hours. Rest dough undisturbed for remaining time until it increases 40-50% in volume, exhibits aerated domed top, and bubbles are visible on surface.",
                "sensoryCue": "Dough wobbles like jello when container is shaken; airy, pillowy, dome-shaped top.",
                "scienceNote": "Gentle coil folds align gluten sheets around expanding carbon dioxide gas cells without degassing the delicate interior alveoli.",
                "timerMins": 270
            },
            {
                "stepNum": 4,
                "text": "Pre-Shape, Final Shape & Cold Retard: Turn dough onto lightly floured bench. Pre-shape into round ball with bench knife; rest 20 mins uncovered. Shape into a taut boule by folding edges into center and rolling gently against counter to create high surface tension. Transfer seam-side UP into rice-flour dusted banneton. Place in plastic bag; refrigerate at 38°F (3°C) for 14 to 18 hours.",
                "sensoryCue": "Taut, smooth outer dough skin with visible gas bubbles underneath.",
                "scienceNote": "Cold retardation halts yeast fermentation while allowing hetero-fermentative lactic acid bacteria (L. sanfranciscensis) to produce acetic acid, imparting classic sourdough tang.",
                "timerMins": 960
            },
            {
                "stepNum": 5,
                "text": "Score & Dutch Oven Bake: Turn cold dough directly from fridge onto parchment sheet. Score top with curved baker's lame at a 30° angle in a single fluid crescent stroke. Lower into preheated 500°F Dutch oven. Drop 2 ice cubes under parchment (steam generation), cover immediately with lid. Bake covered at 450°F (230°C) for 22 minutes. Remove lid; bake uncovered for 20-22 minutes until crust is deep mahogany chestnut with blistered bubbles. Cool on wire rack for minimum 2 hours before slicing.",
                "sensoryCue": "Dramatic 2-inch oven spring 'ear'; crust 'sings' (crackles) as it cools; open translucent custard crumb.",
                "scienceNote": "Trapped steam keeps the outer dough skin elastic during the first 15 minutes, allowing maximum vertical oven spring expansion before starches gelatinize into a glass-like blistered crust.",
                "timerMins": 45
            }
        ],
        "sensoryIndicators": {
            "aroma": "Toasted grain, hazelnut malt, dark roasted crust, tangy lactic wild sourdough aroma",
            "texture": "Deafeningly crunchy shattering blistered crust giving way to open, glossy, custardy, tender chewy crumb",
            "finish": "Complex wheaty sweetness followed by clean, refreshing wild lactic and acetic acidity"
        },
        "scienceNotes": "The 'ear' forms because the 30° angled razor cut creates a flap of skin. When extreme bottom heat hits the wet dough, steam rushes to the path of least resistance (the score line), peeling the flap back and upward into a razor-sharp blistered crest.",
        "troubleshooting": {
            "Bread is dense and gummy inside": "Loaf was sliced while still hot; starches require 2 hours of cooling to set. Or bulk fermentation was under-proofed.",
            "Dough spreads into a flat pancake": "Shaping lacked surface tension, gluten was over-fermented, or starter was too acidic.",
            "No blistered ear": "Dutch oven was not hot enough, steam escaped, or score was too vertical instead of angled 30°."
        },
        "substitutions": [
            {"ingredient": "Dark Rye Flour", "substitute": "Spelt Flour, Khorasan (Kamut), or Einkorn", "ratio": "1:1"},
            {"ingredient": "High-Protein Bread Flour", "substitute": "French T65 Flour", "ratio": "1:1 for authentic Parisian texture"}
        ],
        "flavorPairings": ["Salted Cultured French Butter", "Raw Milk Comté", "Charcuterie Board", "Boeuf Bourguignon"],
        "advancedTechnique": "Spritzing the cold dough surface with fine water mist immediately before scoring to maximize micro-blister formation on the crust.",
        "storageAndReheating": "Store cut-side down on cutting board for 3 days, or in paper bag. Re-crisp whole loaf in 375°F oven for 8 minutes.",
        "nutritionEstimates": {"calories": 210, "protein": 7, "carbs": 42, "fat": 1},
        "relatedRecipes": ["rec-croque-madame", "rec-french-rolled-omelette", "rec-quiche-lorraine"],
        "relatedTechniques": ["Autolyse enzymatic relaxation", "Cold overnight acid retard", "Dutch oven steam entrapment"]
    }
]

print(f"Loaded {len(PART_4_RECIPES)} recipes in PART_4_RECIPES.")
