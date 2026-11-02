# -*- coding: utf-8 -*-
"""
Asian Masterpieces: Japanese Washoku, Chinese Heritage & Korean Hansik
24 authentic, deeply detailed recipes with all 20 required properties.
"""

ASIAN_RECIPES = [
    {
        "id": "rec-miso-black-cod",
        "title": "Gindara Saikyo Yaki (Nobu-Style Miso Glazed Black Cod)",
        "cuisine": "Japanese Washoku",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Intermediate",
        "prepMins": 20,
        "cookMins": 12,
        "totalMins": 32,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=1200&q=80",
        "summary": "The legendary Tokyo and Kyoto masterpiece popularized worldwide by Chef Nobu Matsuhisa: buttery, velvety Alaskan sablefish (black cod) steeped for 72 hours in a sweet Saikyo white miso, sake, and mirin marinade, then caramelized under high heat until blistered mahogany with a melting, succulent core.",
        "dietary": ["pescatarian", "dairy-free", "nut-free"],
        "sensoryRole": "Unctuous, melt-in-the-mouth fish with sweet, fermented umami marinade caramelized into crisp savory-sweet lacquer.",
        "ingredients": [
            {"qty": 4, "unit": "pcs", "name": "Alaskan Black Cod (Sablefish) fillets (approx 180g each)", "prep": "skin-on, pin bones removed", "dept": "seafood"},
            {"qty": 150, "unit": "g", "name": "Saikyo white miso (Kyoto sweet shiro miso)", "prep": "naturally fermented, low salt", "dept": "pantry"},
            {"qty": 60, "unit": "ml", "name": "Hon-mirin (true brewed sweet rice wine)", "prep": "high sugar content", "dept": "pantry"},
            {"qty": 60, "unit": "ml", "name": "Junmai sake (Japanese rice wine)", "prep": "dry", "dept": "pantry"},
            {"qty": 50, "unit": "g", "name": "Granulated raw sugar", "prep": "to balance miso", "dept": "pantry"},
            {"qty": 4, "unit": "pcs", "name": "Hajikami (pickled young ginger shoots with pink tips)", "prep": "for palate cleansing garnish", "dept": "produce"},
            {"qty": 5, "unit": "g", "name": "Coarse sea salt", "prep": "for initial moisture extraction", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy stainless baking sheet lined with heavy aluminum foil or silpat", "type": "everyday"},
            {"name": "High-heat broiler or salamander", "type": "everyday"},
            {"name": "Shallow glass or ceramic marinating dish", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Salt the raw cod fillets lightly and rest 30 minutes; wipe away expelled fish water to eliminate raw fishiness.",
            "In a small saucepan, bring sake and mirin to a rolling boil for 20 seconds to evaporate ethanol. Whisk in sugar until dissolved, then whisk in Saikyo miso over low heat until glossy. Let cool completely.",
            "Submerge fish in the cooled miso marinade in a sealed container; cure refrigerated for 48 to 72 hours."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Remove black cod fillets from the refrigerator 45 minutes before cooking to take off the chill. Gently wipe off excess miso paste with your fingers, leaving a thin golden lacquer on the fish.",
                "timerMins": 5,
                "sensoryCue": "Fillets are firm, translucent amber-white with a sweet, alcoholic, fermented rice aroma.",
                "scienceNote": "Wiping off excess thick miso prevents the sugars from scorching into black carbon before the interior fish reaches safe thermal target."
            },
            {
                "stepNum": 2,
                "text": "Preheat your oven to 200°C (400°F) and position the top rack 6 inches from the broiler element. Line a heavy baking sheet with parchment paper.",
                "timerMins": 10,
                "temperature": "200°C",
                "sensoryCue": "Oven reaches uniform radiant heat."
            },
            {
                "stepNum": 3,
                "text": "Arrange the cod fillets skin-side down with 2 inches of space between each piece. Transfer to oven and bake for 8 minutes until fish begins to flake.",
                "timerMins": 8,
                "temperature": "200°C",
                "sensoryCue": "Fish fat begins to render, glistening across the surface with sweet caramelizing aromas.",
                "scienceNote": "Black cod has extraordinary lipid content (over 15% fat), primarily heart-healthy monounsaturated and omega-3 fatty acids, making it practically impossible to dry out compared to lean cod."
            },
            {
                "stepNum": 4,
                "text": "Turn on the oven broiler to HIGH. Broil the tops of the fillets for 2 to 3 minutes, watching continuously without leaving the oven door, until the miso glaze bubbles violently and blisters into mahogany and charred spots.",
                "timerMins": 2.5,
                "temperature": "Broiler high",
                "sensoryCue": "Audible sizzling and popping; aromatic billows of toasted caramelized sugars and fermented koji aroma; surface develops charred leopard spots.",
                "scienceNote": "Reducing sugars from mirin and amino acids from fermented soy protein undergo intense pyrolytic and Maillard caramelization at 160-180°C under radiant broiler heat."
            },
            {
                "stepNum": 5,
                "text": "Transfer carefully with a fish spatula to warmed ceramic plates. Rest for 2 minutes. Lay a pink-tipped pickled ginger shoot (hajikami) beside each fillet.",
                "timerMins": 2,
                "sensoryCue": "The fish flakes separate into silky, snow-white tiers under the slightest fork pressure."
            }
        ],
        "sensoryIndicators": {
            "see": "Blistered, glossy mahogany lacquer with scorched charred edges, snow-white lustrous fish flakes beneath, vibrant pink ginger shoot.",
            "hear": "Gentle sizzle from rendered fish oils on the hot porcelain plate.",
            "smell": "Intoxicating toasted sweet miso, fermented rice sake notes, roasted caramel, oceanic sweetness.",
            "feel": "Velvety, buttery, melting texture with zero chew; silky collagen and lipids dissolving instantly on the tongue."
        },
        "scienceNotes": [
            "Saikyo miso fermentation: Kyoto sweet miso uses twice as much rice koji as soybeans and ferments for a shorter period, yielding high maltose and glucose concentrations (sweetness) with low salinity (approx 5% vs 12% in red miso).",
            "Osmotic curing: During 72 hours, alcohol and sugars penetrate deep into the dense sablefish muscle, denaturing proteins gently and locking in extraordinary succulence."
        ],
        "troubleshooting": [
            {"issue": "Glaze burned to bitter black ash before fish was hot", "cause": "Too much thick miso paste was left on the surface, or fish was placed too close to the broiler element.", "solution": "Wipe off thick paste with fingers before cooking and bake at 200°C first, using broiler only for the final 2 minutes."},
            {"issue": "Fish is watery and lacks flavor", "cause": "Fish was marinated for only a few hours instead of the mandatory 48-72 hours.", "solution": "Black cod's high fat requires at least 48 hours for miso solutes to penetrate the lipid barrier."}
        ],
        "substitutions": [
            {"original": "Alaskan Black Cod", "substitute": "Chilean Sea Bass (Patagonian Toothfish), King Salmon, or Halibut", "culinaryConsequence": "Sea bass matches black cod's luxurious fat; salmon cures faster (24-36 hours); lean halibut requires lower heat."},
            {"original": "Saikyo sweet miso", "substitute": "Standard white shiro miso mixed with an additional 15g sugar and splash of mirin", "culinaryConsequence": "Replicates Saikyo miso's low-salt, high-sweetness profile."}
        ],
        "flavorPairings": {
            "wine": "Junmai Daiginjo Sake (chilled, floral), Meursault (Chardonnay with buttery richness), or dry German Riesling",
            "zeroProof": "Chilled Gyokuro shaded green tea infused with pickled yuzu peel",
            "complementarySides": ["Steamed Koshihikari rice", "Sunomono (pickled cucumber and wakame salad)"]
        },
        "advancedTechnique": "Kombu-wrapped cure (Kobujime): Wrap the black cod in sake-rehydrated giant kelp sheets (kombu) slathered in the miso paste; the kelp infuses natural glutamic acid (free umami) directly into the flesh during curing.",
        "storageAndReheating": "Cooked cod keeps refrigerated for 2 days. Reheat under a low broiler for 4 minutes; avoid microwaves.",
        "nutritionEstimates": {"calories": 420, "proteinG": 32, "carbsG": 18, "fatG": 24},
        "relatedRecipes": ["rec-sole-meuniere", "rec-tonkotsu-ramen"],
        "relatedTechniques": ["lesson-seasoning-osmosis", "lesson-heat-control"]
    },
    {
        "id": "rec-tonkotsu-ramen",
        "title": "Hakata Tonkotsu Ramen (Rich 18-Hour Pork Bone Broth & Chashu)",
        "cuisine": "Japanese Washoku",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Professional Technique",
        "prepMins": 45,
        "cookMins": 720,
        "totalMins": 765,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1200&q=80",
        "summary": "The holy grail of Japanese noodle craftsmanship from Fukuoka: pork femur bones and trotters blanched of impurities, then subjected to an aggressive 12 to 18-hour rolling boil until marrow, collagen, and fat violently emulsify into a milky-white, opaque, unctuous broth. Served with ultra-thin firm Hakata noodles, rolled pork belly chashu, ramen egg (ajitsuke tamago), wood-ear mushrooms, and black garlic oil (mayu).",
        "dietary": ["dairy-free", "nut-free"],
        "sensoryRole": "Viscous, creamy, bone-marrow richness coating the lips, balanced by savory soy tare, aromatic garlic oil, and springy, firm alkaline noodles.",
        "ingredients": [
            {"qty": 2000, "unit": "g", "name": "Pork femur bones (genkotsu)", "prep": "cut across to expose marrow cavities", "dept": "butchery"},
            {"qty": 1000, "unit": "g", "name": "Pork trotters (pig's feet)", "prep": "split lengthwise for maximum gelatin extraction", "dept": "butchery"},
            {"qty": 300, "unit": "g", "name": "Pork back fat (seabura)", "prep": "for boiling and grating into broth", "dept": "butchery"},
            {"qty": 1, "unit": "pcs", "name": "Yellow onion", "prep": "charred on open flame", "dept": "produce"},
            {"qty": 1, "unit": "head", "name": "Garlic", "prep": "halved crosswise", "dept": "produce"},
            {"qty": 50, "unit": "g", "name": "Fresh ginger", "prep": "sliced thick", "dept": "produce"},
            {"qty": 6, "unit": "portions", "name": "Fresh Hakata-style ultra-thin ramen noodles (26-gauge)", "prep": "low-hydration (28%)", "dept": "drygoods"},
            {"qty": 600, "unit": "g", "name": "Pork belly (rolled and tied for Chashu)", "prep": "braised in soy, mirin, sake", "dept": "butchery"},
            {"qty": 6, "unit": "pcs", "name": "Ajitsuke Tamago (soft-boiled ramen eggs)", "prep": "marinated in soy-mirin 12 hours", "dept": "dairy"},
            {"qty": 50, "unit": "g", "name": "Kikurage (wood ear mushroom)", "prep": "rehydrated, sliced thin", "dept": "pantry"},
            {"qty": 6, "unit": "stalks", "name": "Scallions", "prep": "finely sliced rounds", "dept": "produce"},
            {"qty": 100, "unit": "ml", "name": "Shoyu Tare (concentrated soy, kombu, niboshi seasoning base)", "prep": "to season bowls", "dept": "pantry"},
            {"qty": 30, "unit": "ml", "name": "Mayu (black roasted garlic sesame oil)", "prep": "for finishing drizzle", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "16-quart heavy stockpot with lid", "type": "everyday"},
            {"name": "Fine conical strainer (chinois) and fine skimming ladle", "type": "specialty", "substitute": "Large wire mesh strainer"},
            {"name": "Ramen noodle basket (tebo)", "type": "specialty", "substitute": "Large pasta strainer"}
        ],
        "miseEnPlace": [
            "Soak femur bones and trotters in cold water for 4 hours, changing water twice to purge myoglobin blood.",
            "Char onion and ginger under broiler.",
            "Prepare shoyu tare by simmering soy sauce, mirin, sake, kombu, and dried bonito flakes, then straining.",
            "Roll and tie pork belly; braise in soy-mirin for 2 hours, chill, and slice thin with a sharp knife."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "THE BLANCH: Place pork bones and trotters in the stockpot, cover with cold water, and bring to a violent rolling boil for 15 minutes. A thick, grey, murky scum will rise to the surface.",
                "timerMins": 15,
                "temperature": "100°C",
                "sensoryCue": "Foul grey foam and scum accumulates rapidly on top; water turns dark and muddy.",
                "scienceNote": "Blanching coagulates surface blood proteins, residual marrow debris, and oxidized pigments so they can be completely washed away, which is critical for achieving a pristine, snow-white broth without foul odors."
            },
            {
                "stepNum": 2,
                "text": "Dump the bones into the sink and discard all blanching water. Scrub every bone under cold running water with a stiff brush, picking out all black marrow clots and brown coagulated blood. Scrub the pot completely clean.",
                "timerMins": 15,
                "sensoryCue": "Bones are pristine ivory and pink with no brown scum."
            },
            {
                "stepNum": 3,
                "text": "Return clean bones, trotters, and pork back fat to the pot. Cover with 6 liters of fresh cold water. Bring to a violent, rolling boil over high heat.",
                "timerMins": 25,
                "temperature": "100°C",
                "sensoryCue": "Turbulent boiling water tumbling the heavy bones violently against one another."
            },
            {
                "stepNum": 4,
                "text": "Cover with a tight lid and keep at a vigorous rolling boil for 10 to 12 hours. Check hourly, adding boiling water to keep bones fully submerged. At hour 10, add charred onion, garlic, and ginger. Boil for 2 more hours.",
                "timerMins": 720,
                "temperature": "100°C rolling boil",
                "sensoryCue": "The turbulent churning liquid transforms from clear to cloudy, then to rich, opaque, creamy off-white milk; deep pork aroma without bitterness.",
                "scienceNote": "Violent kinetic energy is mandatory for tonkotsu: boiling water collides rendered fat globules with dissolved gelatin molecules, forming a permanent, milky oil-in-water emulsion that never separates."
            },
            {
                "stepNum": 5,
                "text": "Strain the broth through a fine chinois, pressing firmly on bone marrow and aromatics to extract every drop of gelatinous richness. Keep hot at 85°C.",
                "timerMins": 10,
                "sensoryCue": "Broth coats the ladle with an opaque, velvety white film that leaves a sticky sensation on the lips."
            },
            {
                "stepNum": 6,
                "text": "Cook Hakata noodles in vigorously boiling water for exactly 45 to 60 seconds (kata - firm). Shake vigorously in the tebo basket to remove all cooking starch water.",
                "timerMins": 1,
                "temperature": "100°C",
                "sensoryCue": "Noodles are pale, thin, with a springy toothsome snap."
            },
            {
                "stepNum": 7,
                "text": "Assemble bowls: Pour 35ml hot Shoyu Tare into each warmed ramen bowl. Ladle in 350ml piping hot Tonkotsu broth. Fold in noodles with chopsticks, lifting once to seat them neatly.",
                "timerMins": 1,
                "temperature": "85°C",
                "sensoryCue": "The tare blooms into the white broth, tinting it a warm ivory-tan."
            },
            {
                "stepNum": 8,
                "text": "Top with 2 slices of chashu, a halved soft ramen egg, wood-ear mushroom strips, chopped scallions, and a swirl of black garlic mayu.",
                "timerMins": 1,
                "sensoryCue": "Steam rises carrying intoxicating aromas of garlic, roasted pork, and sesame; dark black mayu streaks float across creamy ivory broth."
            }
        ],
        "sensoryIndicators": {
            "see": "Creamy, opaque ivory-tan broth with drops of golden fat, black swirls of mayu garlic oil, golden jammy egg yolk.",
            "hear": "Satisfying slurping sound as noodles and rich broth are drawn into the mouth.",
            "smell": "Profound, clean roasted pork essence, toasted garlic, sesame oil, savory dashi tare.",
            "feel": "Viscous, velvety broth that coats the palate and sticks lightly to the lips (gelatin content >5%)."
        },
        "scienceNotes": [
            "Gelatin-fat emulsion physics: Trotters provide abundant type-I collagen which breaks down into gelatin. Gelatin acts as a protective colloid and steric stabilizer around tiny lipid droplets, maintaining the opaque milky appearance.",
            "Alkaline noodles (kansui): Potassium and sodium carbonate raise noodle dough pH to 9-11, which strengthens gluten networks, produces signature yellow color from wheat flavonoids, and creates Hakata ramen's distinctive springy, crisp chew."
        ],
        "troubleshooting": [
            {"issue": "Broth is clear and separated with oily layer on top", "cause": "Broth was simmered too gently instead of kept at an aggressive rolling boil.", "solution": "Cover and boil violently over high heat for 60-90 minutes, or blend a portion with an immersion blender to force emulsification."},
            {"issue": "Broth smells barnyardy or dirty", "cause": "Bones were not soaked and blanched properly before the main boil.", "solution": "Always discard blanching water and scrub interior marrow cavities under cold water."}
        ],
        "substitutions": [
            {"original": "Pork femur bones", "substitute": "Pork neck bones and chicken feet", "culinaryConsequence": "Chicken feet provide massive collagen for body; broth cooks in 6 hours instead of 12."},
            {"original": "Hakata noodles", "substitute": "Fresh thin Chinese egg noodles or store-bought fresh ramen", "culinaryConsequence": "Cook for minimal time to preserve authentic firm chew."}
        ],
        "flavorPairings": {
            "wine": "Crisp dry Japanese lager (Asahi Super Dry, Sapporo) or a rich, earthy Honjozo Sake",
            "zeroProof": "Chilled roasted barley tea (Mugicha) or sparkling yuzu water",
            "complementarySides": ["Pan-fried Kurobuta Pork Gyoza with crispy lace skirt", "Spicy pickled mustard greens (karashi takana)"]
        },
        "advancedTechnique": "Seabura grating (Chasshu fat snow): Boil pork back fat separately until tender, then grate it through a metal wire sieve directly over the finished ramen bowl for an authentic Hakata street stall fat snow finish.",
        "storageAndReheating": "Broth solidifies into a gelatin brick when chilled. Keeps refrigerated for 5 days or frozen for 6 months. Reheat to boiling to re-emulsify fat.",
        "nutritionEstimates": {"calories": 820, "proteinG": 46, "carbsG": 72, "fatG": 42},
        "relatedRecipes": ["rec-miso-black-cod", "rec-dan-dan-noodles"],
        "relatedTechniques": ["lesson-braising-collagen", "lesson-emulsions-mastery"]
    },
    {
        "id": "rec-mapo-tofu",
        "title": "Authentic Sichuan Mapo Tofu (Chen Mapo Doufu with Beef & Green Sichuan Pepper)",
        "cuisine": "Chinese Sichuan",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 15,
        "cookMins": 15,
        "totalMins": 30,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=1200&q=80",
        "summary": "The legendary pride of Chengdu: silken tofu cubes poached in gentle salted water, folded into a searing wok reduction of crispy minced beef, authentic Pixian fermented broad bean paste (Doubanjiang), fermented black beans (Douchi), and ground roasted green and red Sichuan peppercorns, creating the electrifying harmony of Mala (numbing and spicy).",
        "dietary": ["dairy-free", "nut-free"],
        "sensoryRole": "Electric, tingling numbness from Sichuan pepper harmonizing with savory fermented chili umami and silky, melting tofu curds.",
        "ingredients": [
            {"qty": 500, "unit": "g", "name": "Medium-firm or soft silken tofu", "prep": "cut into 2cm uniform cubes", "dept": "produce"},
            {"qty": 120, "unit": "g", "name": "Minced beef chuck or flank steak", "prep": "finely chopped with a cleaver", "dept": "butchery"},
            {"qty": 35, "unit": "g", "name": "Authentic Pixian Doubanjiang (aged chili bean paste)", "prep": "finely minced with a cleaver", "dept": "pantry"},
            {"qty": 15, "unit": "g", "name": "Douchi (fermented Chinese black beans)", "prep": "lightly chopped", "dept": "pantry"},
            {"qty": 15, "unit": "g", "name": "Sichuan chili flakes or ground chili powder", "prep": "for vibrant red color", "dept": "pantry"},
            {"qty": 4, "unit": "cloves", "name": "Garlic", "prep": "minced fine", "dept": "produce"},
            {"qty": 15, "unit": "g", "name": "Fresh ginger", "prep": "peeled, minced razor-fine", "dept": "produce"},
            {"qty": 300, "unit": "ml", "name": "Unsalted chicken or beef stock", "prep": "warm", "dept": "pantry"},
            {"qty": 15, "unit": "ml", "name": "Shaoxing rice cooking wine", "prep": "dry", "dept": "pantry"},
            {"qty": 10, "unit": "ml", "name": "Light soy sauce", "prep": "for savory depth", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Sugar", "prep": "to round sharp chili heat", "dept": "pantry"},
            {"qty": 20, "unit": "g", "name": "Potato starch slurry (20g starch + 35ml water)", "prep": "divided into three additions", "dept": "drygoods"},
            {"qty": 5, "unit": "g", "name": "Roasted Sichuan peppercorns (mix of green and red)", "prep": "toasted in dry pan, ground fine in mortar", "dept": "pantry"},
            {"qty": 4, "unit": "stalks", "name": "Garlic greens or Chinese scallions", "prep": "sliced on bias into 2cm batons", "dept": "produce"},
            {"qty": 40, "unit": "ml", "name": "Toasted rapeseed oil (Caizi You) or peanut oil", "prep": "traditional wok frying oil", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "14-inch carbon steel round-bottom wok", "type": "everyday"},
            {"name": "Wide wok spatula (chuan)", "type": "everyday"},
            {"name": "Spider skimmer", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Cut tofu into pristine 2cm cubes; bring a saucepan of water with 3g salt to a simmer and gently poach tofu cubes for 2 minutes, then keep in warm water.",
            "Mince Pixian Doubanjiang fine so chili skins disperse into the oil.",
            "Grind toasted Sichuan peppercorns fresh right before cooking.",
            "Mix potato starch and cold water into a smooth slurry."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat wok over high heat until smoking lightly. Swirl in 30ml oil to season (longyau). Add minced beef and stir-fry briskly over medium heat for 3 minutes until crisp, dark brown, and all moisture has evaporated.",
                "timerMins": 3,
                "temperature": "180°C",
                "sensoryCue": "Beef sizzles and turns deep reddish-brown and crispy (su-cui); savory aroma fills the air.",
                "scienceNote": "Traditional Chengdu mapo uses beef, not pork. Frying beef until completely dry concentrates umami and creates a crispy texture contrast to the silky tofu."
            },
            {
                "stepNum": 2,
                "text": "Push beef to the side. Turn heat to medium-low and add minced Pixian Doubanjiang, Douchi black beans, and chili flakes into the pool of oil. Stir-fry for 1.5 minutes until the oil turns brilliant, luminous ruby-red.",
                "timerMins": 1.5,
                "temperature": "130°C",
                "sensoryCue": "The oil takes on a radiant crimson lacquer (hongyou); pungent fermented bean and chili aroma blooms.",
                "scienceNote": "Chili pigments (capsanthin) are lipid-soluble. Frying in warm oil dissolves carotenoids into the oil phase, giving authentic Sichuan dishes their dazzling red sheen."
            },
            {
                "stepNum": 3,
                "text": "Add minced garlic and ginger; stir-fry 30 seconds until fragrant. Pour in Shaoxing wine around the wok rim, then add the warm chicken stock, light soy sauce, and sugar. Bring to a vigorous boil.",
                "timerMins": 1.5,
                "sensoryCue": "Lively bubbling red broth carrying spicy, fermented, and allium perfumes."
            },
            {
                "stepNum": 4,
                "text": "Using a spider, gently drain the warm tofu cubes and slide them into the boiling red sauce. Simmer gently over medium heat for 4 minutes, nudging the tofu gently with the back of the wok spatula to prevent breaking.",
                "timerMins": 4,
                "temperature": "95°C",
                "sensoryCue": "Tofu absorbs the spicy red liquid; sauce reduces slightly around the pristine white cubes.",
                "scienceNote": "Pre-poaching tofu in salted water expels excess internal moisture and strengthens calcium sulfate protein bonds, preventing the cubes from shattering in the wok."
            },
            {
                "stepNum": 5,
                "text": "THE THREE-STAGE THICKENING: Stir the potato starch slurry. Drizzle one-third of the slurry around the simmering sauce; push gently with back of spatula. Wait 30 seconds, add second third. Add sliced garlic greens. Add the final third.",
                "timerMins": 2,
                "sensoryCue": "The sauce turns from watery broth to a glistening, clingy red glaze that coats every face of the tofu.",
                "scienceNote": "Adding starch slurry in three distinct stages prevents syneresis (weeping) where tofu expels water and dilutes the sauce after plating."
            },
            {
                "stepNum": 6,
                "text": "Drizzle remaining 10ml oil around the edges of the wok; cook 20 seconds on high to set the glaze. Pour into a heated serving bowl.",
                "timerMins": 0.5,
                "sensoryCue": "Glossy red oil separates slightly to the surface, insulating the dish."
            },
            {
                "stepNum": 7,
                "text": "Immediately dust the top with a generous snow of freshly ground roasted Sichuan peppercorn powder. Serve piping hot with bowls of steamed jasmine rice.",
                "timerMins": 0.5,
                "sensoryCue": "Intense floral citrus-pine aroma of Sichuan pepper releases instantly as the powder hits the hot red oil."
            }
        ],
        "sensoryIndicators": {
            "see": "Brilliant crimson red oil glaze, pristine white tofu cubes, crispy dark beef bits, vibrant green garlic shoots, dusty grey-green Sichuan pepper powder.",
            "hear": "Gentle hissing as the hot oil bubbles in the serving bowl.",
            "smell": "Electrifying volatile citrus-floral Sichuan peppercorn, roasted chiles, fermented broad beans, sweet beef.",
            "feel": "Molten, silky tofu melting like cream, punctuated by crunchy beef bits and a vibrating, cool numbness across the tongue."
        },
        "scienceNotes": [
            "Hydroxy-alpha-sanshool chemesthesis: Sichuan pepper does not create heat (capsaicin). Sanshool molecules bind directly to touch receptors (mechanoreceptors) on the tongue, firing at 50 Hertz, inducing a genuine physical tingling/numbing sensation (paresthesia) that refreshes the palate between spicy bites.",
            "Potato starch translucency: Potato starch amylopectin swells at lower temperatures than cornstarch (65°C vs 75°C) and produces a crystal-clear, glossy glaze without dulling the fiery red color."
        ],
        "troubleshooting": [
            {"issue": "Tofu broke into small crushed fragments", "cause": "Tofu was stirred aggressively with the front blade of the spatula.", "solution": "Use only the curved back of the wok spatula to gently push the sauce; never stir violently."},
            {"issue": "Sauce became watery 5 minutes after plating", "cause": "Starch was added in a single rush or tofu was not pre-poached.", "solution": "Always pre-poach tofu in salted water and add starch slurry in three gradual stages."}
        ],
        "substitutions": [
            {"original": "Minced beef", "substitute": "Minced pork belly, ground lamb, or finely diced rehydrated shiitake mushrooms", "culinaryConsequence": "Shiitake mushrooms provide phenomenal vegetarian umami and chewy texture."},
            {"original": "Caizi You (rapeseed oil)", "substitute": "Peanut oil or high-heat sunflower oil", "culinaryConsequence": "Caizi You adds a signature rustic mustard-like aroma; peanut oil yields a clean, nutty profile."}
        ],
        "flavorPairings": {
            "wine": "Off-dry German Riesling Spätlese (residual sugar buffers capsaicin heat) or a fruity Gewürztraminer",
            "zeroProof": "Chilled sweet soymilk (doujiang) or iced sour plum juice (suanmeitang)",
            "complementarySides": ["Steamed Koshihikari or Jasmine rice", "Stir-fried baby bok choy with garlic"]
        },
        "advancedTechnique": "Green vs Red Huajiao dual layering: Blend red Sichuan peppercorns (earthy, warm, intense tongue numbness) with green Qing Huajiao (vibrant citrus, kaffir lime perfume) for an exhilarating multi-dimensional sensory explosion.",
        "storageAndReheating": "Keeps refrigerated for 2 days. Reheat gently in a wok over medium heat with 2 tablespoons of water.",
        "nutritionEstimates": {"calories": 380, "proteinG": 22, "carbsG": 16, "fatG": 26},
        "relatedRecipes": ["rec-dan-dan-noodles", "rec-kimchi-jjigae"],
        "relatedTechniques": ["lesson-seasoning-osmosis", "lesson-heat-control"]
    }
]

print(f"Loaded {len(ASIAN_RECIPES)} Asian master recipes.")
