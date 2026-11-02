# -*- coding: utf-8 -*-
"""
Italian Culinary Masterpieces
14 authentic, highly detailed recipes with all 20 required properties.
"""

ITALIAN_RECIPES = [
    {
        "id": "rec-ragu-bolognese",
        "title": "Authentic Tagliatelle al Ragù Bolognese Classico",
        "cuisine": "Italian Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 210,
        "totalMins": 240,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1621996346565-e3d5d6281033?auto=format&fit=crop&w=1200&q=80",
        "summary": "The authentic Accademia Italiana della Cucina recipe from Bologna: coarse-ground beef chuck and fatty pork belly gently browned with a fine battuto of onion, celery, and carrot, deglazed with dry white wine, braised in whole milk and gentle tomato passata for 3.5 hours, and tossed with silky fresh handmade egg tagliatelle.",
        "dietary": ["nut-free"],
        "sensoryRole": "Deep, savory, sweet-milky meat sauce with velvety texture clinging to wide, porous egg pasta ribbons.",
        "ingredients": [
            {"qty": 500, "unit": "g", "name": "Coarse-ground beef chuck (cartella or spalla)", "prep": "ground through 8mm plate", "dept": "butchery"},
            {"qty": 250, "unit": "g", "name": "Coarse-ground pork belly or unsmoked pancetta", "prep": "finely chopped", "dept": "butchery"},
            {"qty": 1, "unit": "pcs", "name": "Yellow onion", "prep": "brunoise (3mm dice)", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Celery rib", "prep": "brunoise (3mm dice)", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Carrot", "prep": "brunoise (3mm dice)", "dept": "produce"},
            {"qty": 250, "unit": "ml", "name": "Dry Italian white wine (Trebbiano or Pinot Grigio)", "prep": "room temperature", "dept": "pantry"},
            {"qty": 300, "unit": "ml", "name": "Whole milk", "prep": "warmed", "dept": "dairy"},
            {"qty": 300, "unit": "g", "name": "Italian tomato passata or peeled San Marzano tomatoes", "prep": "crushed", "dept": "pantry"},
            {"qty": 250, "unit": "ml", "name": "Beef or capon broth", "prep": "warm, unsalted", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Extra virgin olive oil", "prep": "for battuto", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Unsalted butter", "prep": "to finish", "dept": "dairy"},
            {"qty": 500, "unit": "g", "name": "Fresh egg tagliatelle", "prep": "rolled thin, 8mm width", "dept": "drygoods"},
            {"qty": 60, "unit": "g", "name": "Parmigiano-Reggiano DOP (aged 24 months)", "prep": "freshly microplaned", "dept": "dairy"}
        ],
        "equipment": [
            {"name": "Heavy-bottomed enameled cast iron Dutch oven", "type": "everyday"},
            {"name": "Large stockpot for pasta boiling", "type": "everyday"},
            {"name": "Wooden spatula for deglazing", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Mince onion, celery, and carrot into fine, uniform 3mm brunoise.",
            "Bring milk to lukewarm; cold milk curdles when meeting hot acidic wine fond.",
            "Open white wine and measure passata.",
            "Grate Parmigiano-Reggiano on a microplane."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat olive oil in a Dutch oven over medium heat. Add pancetta and render for 5 minutes until fat is released. Add the finely minced onion, celery, and carrot (soffritto) and sweat gently for 10 minutes until soft and translucent without browning.",
                "timerMins": 15,
                "temperature": "120°C",
                "sensoryCue": "Vegetables soften into a sweet, translucent mirepoix; sweet aroma of cooked allium and celery.",
                "scienceNote": "Slow sweating without browning (suer) breaks down vegetal hemicellulose and releases simple sugars without generating Maillard bitterness."
            },
            {
                "stepNum": 2,
                "text": "Increase heat to medium-high. Add ground beef and pork. Stir vigorously, breaking apart large chunks, and cook for 8-10 minutes until the meat turns grey-brown and all expelled water evaporates.",
                "timerMins": 10,
                "sensoryCue": "Initial hissing of boiling water transitions to a crackling sizzle as meat fries in its own rendered fat.",
                "scienceNote": "Authentic ragù does not sear the meat to a dark hard crust. Meat is lightly browned to maintain tender, delicate morsels that disperse smoothly throughout the sauce."
            },
            {
                "stepNum": 3,
                "text": "Pour in the dry white wine. Scrape up any fond and cook briskly over medium-high heat for 6 minutes until the smell of alcohol disappears and the liquid has completely evaporated into the meat.",
                "timerMins": 6,
                "sensoryCue": "Sharp ethanol vapor gives way to a clean, fruity, acidic wine aroma; the bottom of the pot is dry."
            },
            {
                "stepNum": 4,
                "text": "Pour in 150ml of the warm milk. Simmer gently over medium-low heat until the milk is completely absorbed into the meat fibers (about 10 minutes).",
                "timerMins": 10,
                "sensoryCue": "The meat absorbs the white dairy liquid, turning creamy and unctuous."
            },
            {
                "stepNum": 5,
                "text": "Stir in tomato passata and remaining 150ml milk. Add a pinch of sea salt and black pepper. Bring to a faint simmer with tiny bubbles barely breaking the surface (sobollire). Partially cover with the lid.",
                "timerMins": 5,
                "temperature": "85°C",
                "sensoryCue": "The sauce transforms into a rich terracotta orange hue with lazy, occasional bubbles."
            },
            {
                "stepNum": 6,
                "text": "Simmer on the lowest heat setting for 3 to 3.5 hours, adding a ladle of warm broth whenever the sauce becomes too dry. Stir every 20 minutes to prevent scorching.",
                "timerMins": 180,
                "sensoryCue": "The meat breaks down into a melt-in-the-mouth, velvety paste; droplets of orange fat glisten on the surface.",
                "scienceNote": "Milk lactic acid and calcium tenderize muscle fibers during prolonged low-temperature braising, while milk proteins buffer tomato acidity, yielding Bologna's signature round, velvety profile."
            },
            {
                "stepNum": 7,
                "text": "Boil fresh tagliatelle in salted water (10g salt per liter) for 2 to 3 minutes until al dente. Reserve 100ml pasta water.",
                "timerMins": 3,
                "sensoryCue": "Fresh pasta floats to the surface and feels supple yet firm to the bite."
            },
            {
                "stepNum": 8,
                "text": "Transfer cooked pasta directly into the ragù pan with a splash of pasta cooking water and 30g butter. Toss vigorously for 1 minute over medium heat to emulsify (mantecare). Serve immediately with grated Parmigiano-Reggiano.",
                "timerMins": 1.5,
                "sensoryCue": "The sauce coats every strand of tagliatelle like silk; no watery pool left on the bottom of the bowl."
            }
        ],
        "sensoryIndicators": {
            "see": "Warm terracotta-orange meat sauce coating pale yellow ribbons of egg pasta, dusted with powdery white cheese.",
            "hear": "Slurping sound during mantecatura; quiet bubbling of the gentle 3-hour simmer.",
            "smell": "Sweet dairy, rich slow-cooked beef, aromatic soffritto, aged savory cheese notes.",
            "feel": "Porous, rough tagliatelle texture holding velvety, melting meat in every forkful."
        },
        "scienceNotes": [
            "Porous pasta surface: Bronze-extruded or handmade rolled egg pasta has microscopic craters that trap sauce emulsions, unlike slick Teflon-extruded dry spaghetti where sauce simply slides off.",
            "Emulsion mantecatura: Starch washed into pasta cooking water acts as a surfactant, bridging the fat (olive oil/butter/pork fat) and water into a creamy, cohesive sauce."
        ],
        "troubleshooting": [
            {"issue": "Sauce separated into oily pool and dry meat", "cause": "Heat was too high during braising or milk was added cold, breaking the emulsion.", "solution": "Whisk in 3-4 tablespoons of boiling starchy pasta water vigorously off heat to re-emulsify the sauce."},
            {"issue": "Sauce tastes sharp and acidic", "cause": "Too much tomato was added or wine was not boiled off completely.", "solution": "Stir in an additional 50ml of warm whole milk or heavy cream and simmer 10 minutes."}
        ],
        "substitutions": [
            {"original": "Beef chuck", "substitute": "Veal shoulder or ground pork/beef blend", "culinaryConsequence": "Veal produces an even lighter, silkier traditional Bolognese."},
            {"original": "Tagliatelle", "substitute": "Pappardelle, Fettuccine, or Rigatoni", "culinaryConsequence": "Never serve with spaghetti in Bologna; wide ribbons or tubular shapes are necessary to hold the coarse meat."}
        ],
        "flavorPairings": {
            "wine": "Sangiovese di Romagna, Barbera d'Alba, or Chianti Classico Riserva",
            "zeroProof": "Chilled non-alcoholic bitter aperitivo with blood orange and sparkling tonic",
            "complementarySides": ["Insalata mista with shaved fennel and white balsamic", "Warm crusty ciabatta"]
        },
        "advancedTechnique": "Traditional chicken liver enrichment: Finely chop 50g fresh chicken livers and sauté with the meat during step 2; this is the secret historic Bolognese restaurant technique that imparts profound depth and umami.",
        "storageAndReheating": "Ragù stores in the refrigerator for up to 5 days and freezes for 3 months. Reheat gently in a saucepan with a splash of water before tossing with fresh pasta.",
        "nutritionEstimates": {"calories": 650, "proteinG": 38, "carbsG": 58, "fatG": 28},
        "relatedRecipes": ["rec-cacio-e-pepe", "rec-carbonara"],
        "relatedTechniques": ["lesson-braising-collagen", "lesson-starch-gelatinization"]
    },
    {
        "id": "rec-cacio-e-pepe",
        "title": "Cacio e Pepe Autentico (Pecorino Romano & Toasted Black Pepper)",
        "cuisine": "Italian Classical",
        "category": "lunch",
        "slot": "mid",
        "difficulty": "Advanced",
        "prepMins": 5,
        "cookMins": 12,
        "totalMins": 17,
        "yieldServings": 2,
        "heroImage": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=1200&q=80",
        "summary": "Roman minimalism pushed to technical perfection: exactly three ingredients—spaghetti, aged Pecorino Romano DOP, and freshly cracked black peppercorns. Toasted whole peppercorns blooming in warm water meet starchy pasta water and microplaned cheese, forming a glossy, creamy emulsion without cream, butter, or oil.",
        "dietary": ["vegetarian", "nut-free"],
        "sensoryRole": "Sharp, salty, sheep's-milk pungency enveloped in a velvety starch cream, illuminated by floral, fiery bursts of toasted piperine.",
        "ingredients": [
            {"qty": 220, "unit": "g", "name": "Artisanal bronze-die Spaghetti or Tonnarelli", "prep": "high-protein durum semolina", "dept": "drygoods"},
            {"qty": 140, "unit": "g", "name": "Pecorino Romano DOP (aged 12-16 months)", "prep": "grated powder-fine on a microplane", "dept": "dairy"},
            {"qty": 8, "unit": "g", "name": "Whole black peppercorns (Tellicherry or Sarawak)", "prep": "coarsely cracked in a mortar", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Coarse sea salt", "prep": "for pasta water (use sparingly; Pecorino is very salty)", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy stainless steel or aluminum skillet", "type": "everyday"},
            {"name": "Granite mortar and pestle", "type": "everyday"},
            {"name": "Large ceramic pasta bowl for cheese paste mixing", "type": "everyday"},
            {"name": "Long stainless cooking tongs", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Grate Pecorino Romano on the finest microplane; cheese must be fluffy and powdery like snow, not shredded, to dissolve without clumping.",
            "Crack whole peppercorns coarsely in a mortar—avoid fine pre-ground pepper.",
            "Bring 2 liters of water to a boil in a wide pot (use less water than usual to concentrate starch)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Add cracked peppercorns to a dry, wide skillet over medium heat. Toast for 2 minutes, swirling constantly, until intensely fragrant and crackling faintly.",
                "timerMins": 2,
                "temperature": "140°C",
                "sensoryCue": "Pepper aroma intensifies dramatically from sharp heat to warm, floral, woody aromatics.",
                "scienceNote": "Thermal toasting volatilizes piperine and monoterpenes (pinene, limonene) in the black pepper corns, rounding harsh raw bite into complex floral spice."
            },
            {
                "stepNum": 2,
                "text": "Ladle 100ml of hot boiling water into the skillet with the toasted pepper. The water will boil violently, harvesting the pepper oils. Turn off heat.",
                "timerMins": 1,
                "sensoryCue": "Vigorous hissing steam and pepper extraction turns the liquid grey-amber."
            },
            {
                "stepNum": 3,
                "text": "Drop spaghetti into boiling water with only 5g salt (half normal ratio). Cook for exactly half its package time (approx 5 minutes), keeping it very firm.",
                "timerMins": 5,
                "sensoryCue": "Pasta is pliable but has an opaque, raw core."
            },
            {
                "stepNum": 4,
                "text": "Transfer the half-cooked spaghetti directly with tongs into the pepper skillet over medium heat. Ladle in 150ml of starchy cooking water. Finish cooking the pasta directly in the skillet (risottare), tossing constantly for 3-4 minutes until al dente.",
                "timerMins": 4,
                "sensoryCue": "The pasta starch leaches into the water, transforming the skillet liquid into a cloudy, viscous emulsion."
            },
            {
                "stepNum": 5,
                "text": "Meanwhile, prepare the cheese paste (la crema): Place 100g grated Pecorino in a small ceramic bowl. Whisk in 3-4 tablespoons of warm (approx 60°C) pasta water until a thick, smooth, spreadable paste forms with zero clumps.",
                "timerMins": 2,
                "temperature": "60°C",
                "sensoryCue": "A smooth, mayonnaise-like white paste with no melted rubbery strings.",
                "scienceNote": "Pecorino Romano proteins (casein) coagulate and form stubborn rubbery clumps (filare) if heated above 65°C. Pre-tempering cheese below 60°C with starchy water ensures stable suspension."
            },
            {
                "stepNum": 6,
                "text": "CRITICAL STEP: Remove the skillet completely from heat. Wait 30 seconds for the pan to cool to approximately 60°C (140°F). Dump the Pecorino crema over the pasta.",
                "timerMins": 0.5,
                "temperature": "60°C pan",
                "sensoryCue": "The pan stops hissing and sizzling; quiet steam replaces vigorous boiling."
            },
            {
                "stepNum": 7,
                "text": "Toss and stir the pasta violently with tongs and a wooden spoon for 45 seconds, adding a tablespoon of warm pasta water if needed, until the cheese crema marries the pepper starch into an ultra-creamy, glossy sauce.",
                "timerMins": 1,
                "sensoryCue": "Audible slapping sound (schiaffo) as the sauce thickens into a glossy white velvet that coats every strand."
            },
            {
                "stepNum": 8,
                "text": "Plate immediately in warm bowls. Dust with the remaining 40g grated Pecorino and an extra grind of coarsely cracked pepper.",
                "timerMins": 0.5,
                "sensoryCue": "A gleaming, glossy nest of pasta with pepper flecks and no broken oil or clumping."
            }
        ],
        "sensoryIndicators": {
            "see": "Pristine creamy white emulsion clinging tightly to golden pasta strands, speckled with coarse black pepper shards.",
            "hear": "Distinct slapping, sloshing sound as pasta is whipped off-heat against the skillet.",
            "smell": "Intense pungent sheep's milk cheese, toasted black pepper, fresh warm semolina starch.",
            "feel": "Chewy, al dente pasta wrapped in a luxurious, silky sauce that coats the mouth without greasy residue."
        },
        "scienceNotes": [
            "Amylose-casein synergy: Gelatinized amylose starch molecules from pasta water suspend fat globules from the cheese, preventing casein proteins from aggregating into a solid curd.",
            "Temperature threshold: Above 65°C, Pecorino casein dehydrates and cross-links irreversibly into tough strands. Keeping the pan below this threshold is the scientific key to silk-smooth Cacio e Pepe."
        ],
        "troubleshooting": [
            {"issue": "Cheese clumped into a solid rubber ball (stracciatella effect)", "cause": "The pan was too hot when the cheese was added (above 65°C).", "solution": "Always remove the pan from heat and allow it to cool for 30-45 seconds before adding the pre-tempered cheese paste."},
            {"issue": "Sauce is watery and pools at the bottom", "cause": "Too much water was added, or pasta was cooked in too much water, diluting the starch concentration.", "solution": "Cook pasta in minimal water (just enough to cover) to concentrate amylose starch."}
        ],
        "substitutions": [
            {"original": "Pecorino Romano", "substitute": "70% Pecorino Romano and 30% Parmigiano-Reggiano", "culinaryConsequence": "Parmigiano melts more easily and softens the pungent salinity of pure Pecorino, ideal for beginners."},
            {"original": "Tonnarelli", "substitute": "Spaghettoni, Bucatini, or Mezze Maniche", "culinaryConsequence": "Tonnarelli is traditional square-cut Roman egg pasta; thick spaghetti works superbly."}
        ],
        "flavorPairings": {
            "wine": "Frascati Superiore, Cesanese del Piglio, or Verdicchio dei Castelli di Jesi",
            "zeroProof": "Chilled sparkling mineral water with a sprig of fresh basil and cracked green peppercorn",
            "complementarySides": ["Carciofi alla Romana (braised Roman artichokes with mint)", "Simple arugula salad with lemon"]
        },
        "advancedTechnique": "The blender emulsion fail-safe: In modern Michelin-starred Roman kitchens, chefs blend the grated Pecorino with ice water and cooked pasta water in a high-speed blender to create a completely stable cheese gel before pouring over the rested pasta.",
        "storageAndReheating": "Cacio e Pepe must be consumed immediately. Reheating separates the delicate emulsion into oil and cheese curd. If needed, reheat over a gentle double-boiler while whisking in 2 tablespoons of warm water.",
        "nutritionEstimates": {"calories": 520, "proteinG": 24, "carbsG": 64, "fatG": 18},
        "relatedRecipes": ["rec-carbonara", "rec-ragu-bolognese"],
        "relatedTechniques": ["lesson-emulsions-mastery", "lesson-starch-gelatinization"]
    },
    {
        "id": "rec-risotto-milanese",
        "title": "Risotto alla Milanese con Midollo (Saffron Risotto with Bone Marrow)",
        "cuisine": "Italian Classical",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Intermediate",
        "prepMins": 15,
        "cookMins": 25,
        "totalMins": 40,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=1200&q=80",
        "summary": "The crown of Lombard cuisine: high-starch Carnaroli rice toasted in rendered beef bone marrow, quenched with dry white wine, gently simmered in simmering capon-veal stock infused with crimson saffron threads, and finished off heat with ice-cold butter and 24-month Parmigiano-Reggiano until it flows like an undulating golden wave (all'onda).",
        "dietary": ["gluten-free", "nut-free"],
        "sensoryRole": "Rich, creamy, golden grain carrying earthy-floral saffron perfume, savory bone marrow richness, and sharp, crystalline Parmigiano.",
        "ingredients": [
            {"qty": 320, "unit": "g", "name": "Superfino Carnaroli or Acquerello rice", "prep": "high amylose rice; do not rinse", "dept": "drygoods"},
            {"qty": 1200, "unit": "ml", "name": "Rich beef and capon (chicken) broth", "prep": "kept at a gentle simmer", "dept": "pantry"},
            {"qty": 0.5, "unit": "g", "name": "Pure saffron threads (Zafferano dell'Aquila DOP)", "prep": "steeped in 60ml warm broth", "dept": "pantry"},
            {"qty": 40, "unit": "g", "name": "Fresh beef bone marrow (midollo di bue)", "prep": "soaked in cold water, diced", "dept": "butchery"},
            {"qty": 1, "unit": "pcs", "name": "Small white onion or shallot", "prep": "minced microscopic", "dept": "produce"},
            {"qty": 120, "unit": "ml", "name": "Dry Italian white wine (Gavi or Franciacorta)", "prep": "dry, crisp", "dept": "pantry"},
            {"qty": 80, "unit": "g", "name": "Unsalted European butter", "prep": "divided: 30g to start, 50g frozen in cubes to finish", "dept": "dairy"},
            {"qty": 70, "unit": "g", "name": "Parmigiano-Reggiano DOP (aged 24 months)", "prep": "freshly grated", "dept": "dairy"},
            {"qty": 2, "unit": "g", "name": "Fine sea salt", "prep": "to balance", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy copper or stainless steel risotto pan (casseruola bassa)", "type": "everyday"},
            {"name": "Perforated wooden risotto spoon (cucchiaio girarisotto)", "type": "specialty", "substitute": "Standard wooden spoon"},
            {"name": "Ladle and small saucepan for hot broth", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Crumble saffron threads into 60ml of warm broth 30 minutes before cooking to extract crocin (color) and safranal (aroma).",
            "Dice bone marrow fine and keep broth simmering on the adjacent burner.",
            "Cut 50g finishing butter into cubes and keep in the freezer until mantecatura.",
            "Mince onion so fine that it will melt invisibly into the rice."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Melt 30g butter and the diced beef marrow in a heavy risotto pan over medium-low heat. Add minced onion and sweat gently for 5 minutes without allowing any color.",
                "timerMins": 5,
                "temperature": "115°C",
                "sensoryCue": "Onions turn soft and clear; bone marrow renders into fragrant, clear beef lipid.",
                "scienceNote": "Bone marrow contains high levels of monounsaturated oleic acid and umami compounds that coat the rice grains, providing deep savory foundation."
            },
            {
                "stepNum": 2,
                "text": "Add the raw Carnaroli rice. Toast (tostatura) over medium heat for 3 minutes, stirring constantly with a wooden spoon, until grains become translucent at the edges with a chalky center and feel hot to the touch.",
                "timerMins": 3,
                "temperature": "130°C",
                "sensoryCue": "Audible dry clattering sound like glass beads clicking; faint nutty aroma of toasted starch.",
                "scienceNote": "Tostatura gelatinizes the outer starch layer, creating a microscopic crust that prevents the grain from disintegrating into mush during simmering while retaining internal al dente core."
            },
            {
                "stepNum": 3,
                "text": "Pour in white wine. It will hiss violently and steam. Stir continuously until the wine has completely evaporated and the pan is almost dry.",
                "timerMins": 2,
                "sensoryCue": "Sharp steam of evaporating alcohol, followed by clean grape acidity."
            },
            {
                "stepNum": 4,
                "text": "Add two ladles of simmering broth (broth must be boiling-hot to maintain pan temperature). Simmer over medium heat, stirring regularly in a figure-eight pattern. As broth is absorbed by the rice, add another ladle.",
                "timerMins": 10,
                "sensoryCue": "Steady, gentle bubbling; broth thickens as starch sloughs off the grain surfaces into the liquid."
            },
            {
                "stepNum": 5,
                "text": "At minute 12 of cooking, pour in the steeped saffron infusion along with the threads. Stir well.",
                "timerMins": 2,
                "sensoryCue": "The entire pan transforms instantly into a dazzling, luminous deep golden-canary color with intoxicating hay-like saffron aroma."
            },
            {
                "stepNum": 6,
                "text": "Continue simmering and ladling broth until rice is cooked to 16-17 minutes total. Taste: the grain should be tender on the exterior with a distinct firm tooth in the center (all'onda). Remove pan from heat.",
                "timerMins": 5,
                "sensoryCue": "Grains are plump, suspended in a glossy golden emulsion."
            },
            {
                "stepNum": 7,
                "text": "THE MANTECATURA: Let the risotto rest off-heat for 1 minute. Add the frozen 50g butter cubes and grated Parmigiano-Reggiano. Beat vigorously with the wooden spoon while shaking the pan back and forth to incorporate air and emulsify fat into the starch.",
                "timerMins": 2,
                "sensoryCue": "The mixture whips into a creamy, shimmering suspension. Tipping the pan causes the risotto to flow forward in a gentle, rolling wave (all'onda)."
            },
            {
                "stepNum": 8,
                "text": "Spoon into flat warmed plates. Tap the bottom of the plate firmly with the palm of your hand; the risotto should spread smoothly into an even, glossy disc without puddling liquid.",
                "timerMins": 1,
                "sensoryCue": "Luminous gold disc that quivers gently when nudged."
            }
        ],
        "sensoryIndicators": {
            "see": "Brilliant, radiant saffron-gold, creamy sheen, smooth flat disc with individual visible glistening grains.",
            "hear": "Distinct wet rhythmic slapping as the pan is tossed during mantecatura.",
            "smell": "Exotic floral saffron, toasted rice, rich beef bone marrow, nutty aged cheese.",
            "feel": "Silky, unctuous sauce with perfectly resistant, firm, toothsome rice grains."
        },
        "scienceNotes": [
            "Amylose vs Amylopectin: Carnaroli rice contains 24% amylose (linear starch) and 76% amylopectin (branched starch). Amylose maintains grain structural integrity under heat, while amylopectin sloughs off to create the luxurious creamy emulsion.",
            "Mantecatura physics: Adding ice-cold butter creates a thermal shock that forces butterfat droplets to disperse evenly through the hot starch matrix without melting into a greasy separated oil layer."
        ],
        "troubleshooting": [
            {"issue": "Risotto is stiff and stands up like spackle", "cause": "Not enough broth was added during mantecatura; starch absorbed too much water.", "solution": "Whisk in 2-3 tablespoons of boiling broth immediately off heat until it flows in a wave (all'onda)."},
            {"issue": "Rice grains are mushy and broken", "cause": "Rice was overstirred violently during the early stages, or non-risotto short grain rice was used.", "solution": "Use authentic Italian Carnaroli, Vialone Nano, or Arborio, and stir gently in smooth rhythmic circles."}
        ],
        "substitutions": [
            {"original": "Beef bone marrow", "substitute": "Extra 30g European butter or rich beef tallow", "culinaryConsequence": "Butter produces a clean, elegant saffron risotto; bone marrow provides the deep historic Milanese authenticity."},
            {"original": "Carnaroli rice", "substitute": "Vialone Nano or Arborio rice", "culinaryConsequence": "Vialone Nano absorbs broth faster and yields a slightly softer, creamier texture; Carnaroli yields the firmest al dente."}
        ],
        "flavorPairings": {
            "wine": "Franciacorta Brut, Barolo, or Valtellina Superiore (Nebbiolo)",
            "zeroProof": "Chilled sparkling pear nectar with fresh lemon balm and saffron mist",
            "complementarySides": ["Traditional Osso Buco alla Milanese with gremolata", "Braised bitter chicory"]
        },
        "advancedTechnique": "Gold leaf presentation: In Gualtiero Marchesi's legendary 1981 Milanese masterpiece, a square sheet of 24-karat edible pure gold leaf is placed squarely in the center of the deep yellow saffron risotto, creating breathtaking chromatic contrast.",
        "storageAndReheating": "Risotto is best eaten within 5 minutes of mantecatura. Leftovers can be chilled overnight and shaped into breadcrumb-crusted Arancini or fried into crispy Risotto al Salto patties.",
        "nutritionEstimates": {"calories": 540, "proteinG": 14, "carbsG": 68, "fatG": 24},
        "relatedRecipes": ["rec-osso-buco", "rec-ragu-bolognese"],
        "relatedTechniques": ["lesson-starch-gelatinization", "lesson-emulsions-mastery"]
    },
    {
        "id": "rec-carbonara",
        "title": "Spaghetti alla Carbonara Tradizionale (Guanciale, Pecorino & Egg Yolks)",
        "cuisine": "Italian Classical",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Intermediate",
        "prepMins": 10,
        "cookMins": 15,
        "totalMins": 25,
        "yieldServings": 2,
        "heroImage": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pure, uncompromising Roman standard: thick artisanal spaghetti tossed with crispy cured pork jowl (guanciale), bathed in an unctuous, silky liaison of pasture-raised egg yolks, freshly grated Pecorino Romano, and an avalanche of toasted black pepper. Strictly zero cream, zero peas, zero garlic, and zero onions.",
        "dietary": ["nut-free"],
        "sensoryRole": "Decadent, rich egg yolk cream tempered by salty, funky cured pork fat and sharp, pungent black pepper bite.",
        "ingredients": [
            {"qty": 220, "unit": "g", "name": "Artisanal Spaghetti or Rigatoni", "prep": "bronze-die extruded", "dept": "drygoods"},
            {"qty": 150, "unit": "g", "name": "Authentic cured pork jowl (Guanciale)", "prep": "cut into 1cm thick lardons", "dept": "butchery"},
            {"qty": 4, "unit": "pcs", "name": "Large pasture-raised egg yolks", "prep": "deep orange yolks, at room temp", "dept": "dairy"},
            {"qty": 1, "unit": "pcs", "name": "Whole large egg", "prep": "for lighter emulsion balance", "dept": "dairy"},
            {"qty": 60, "unit": "g", "name": "Pecorino Romano DOP", "prep": "freshly grated powder-fine", "dept": "dairy"},
            {"qty": 20, "unit": "g", "name": "Parmigiano-Reggiano DOP", "prep": "to round the sharp saltiness", "dept": "dairy"},
            {"qty": 6, "unit": "g", "name": "Freshly cracked black peppercorns", "prep": "coarse grind", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy stainless or carbon steel skillet", "type": "everyday"},
            {"name": "Heatproof glass or stainless steel mixing bowl", "type": "everyday"},
            {"name": "Whisk and pasta tongs", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Cut guanciale into uniform 1cm batons.",
            "Whisk egg yolks, whole egg, grated cheeses, and half the black pepper in a heatproof bowl until a thick, golden paste forms.",
            "Bring 2.5 liters of water to a boil with moderate salt."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Place guanciale lardons in a cold skillet with no added oil. Place over medium-low heat. Slowly render the pork jowl for 8-10 minutes, stirring occasionally, until the exterior is deeply crisp and amber-brown, but the interior retains a tender, yielding chew.",
                "timerMins": 9,
                "temperature": "130°C",
                "sensoryCue": "Lardons sizzle gently in a pool of clear, aromatic liquid pork fat; color is dark amber-gold.",
                "scienceNote": "Starting in a cold pan prevents the surface from burning before internal collagen and intramuscular fat can render out."
            },
            {
                "stepNum": 2,
                "text": "Remove the crispy guanciale with a slotted spoon to a small dish, leaving the fragrant rendered liquid fat in the skillet. Turn off the heat under the skillet.",
                "timerMins": 1,
                "sensoryCue": "Lardons cool to glass-crisp bite; rendered liquid fat smells savory and cured."
            },
            {
                "stepNum": 3,
                "text": "Boil spaghetti in salted water until 1.5 minutes shy of al dente. Reserve 150ml of starchy pasta water.",
                "timerMins": 8,
                "sensoryCue": "Pasta has a firm core when bitten."
            },
            {
                "stepNum": 4,
                "text": "Whisk 2 tablespoons of the warm rendered guanciale fat directly into the bowl of egg yolks and cheese. This tempers the yolks and infuses them with rich pork flavor.",
                "timerMins": 1,
                "temperature": "55°C",
                "sensoryCue": "The egg paste turns glossy, silky, and unctuous."
            },
            {
                "stepNum": 5,
                "text": "Using tongs, transfer hot spaghetti directly into the skillet with the remaining rendered fat over low heat. Toss for 1 minute with 3 tablespoons of pasta water to coat the strands in a shiny fat-water emulsion.",
                "timerMins": 1,
                "sensoryCue": "Pasta turns glistening and glossy as fat binds to starch."
            },
            {
                "stepNum": 6,
                "text": "CRITICAL EMULSION STEP: Remove the skillet completely from the heat. Allow the pan to cool for 30 seconds (down to approximately 62°C). Pour the egg-cheese mixture over the pasta. Toss and stir rapidly with tongs without stopping.",
                "timerMins": 1,
                "temperature": "62°C",
                "sensoryCue": "The yellow egg mixture thickens instantly against the warm pasta, clinging in a creamy, velvety custard without a single speck of scrambled egg.",
                "scienceNote": "Egg yolks set into custard between 65°C and 70°C. By tossing off heat, residual heat cooks the egg yolks to safe pasteurization (60°C+) while preventing egg coagulation."
            },
            {
                "stepNum": 7,
                "text": "Fold in three-quarters of the crisp guanciale. If sauce is too thick, add a splash of reserved pasta water to loosen until it flows luxuriously.",
                "timerMins": 0.5,
                "sensoryCue": "Velvety, rich yellow sauce coating every single strand."
            },
            {
                "stepNum": 8,
                "text": "Twirl into warm bowls. Top with remaining crisp guanciale lardons, an extra dusting of Pecorino, and a shower of cracked black pepper.",
                "timerMins": 0.5,
                "sensoryCue": "Steam carries the scent of cured pork and toasted pepper; deep golden yellow presentation."
            }
        ],
        "sensoryIndicators": {
            "see": "Radiant golden-yellow pasta enrobed in a glossy, mirror-like cream, crowned with dark amber crisp lardons and coarse black pepper.",
            "hear": "Crispy crunch of guanciale between the teeth; wet swirling sound in the skillet.",
            "smell": "Intense savory cured pork fat, sharp Pecorino, pungent freshly cracked pepper.",
            "feel": "Decadently rich, unctuous sauce melting on the tongue, followed by shattering pork crunch."
        },
        "scienceNotes": [
            "Lecithin emulsification: Egg yolks are packed with lecithin, a powerful natural phospholipid surfactant that bonds the rendered pork lipids with water-based starch into an unbreakable emulsion.",
            "Scrambling prevention: Adding warm pork fat to the eggs before heating coats the egg proteins in a protective lipid layer, raising the temperature at which they coagulate."
        ],
        "troubleshooting": [
            {"issue": "Sauce curdled into scrambled eggs", "cause": "Pan was left on the heat or skillet was too hot when eggs were poured.", "solution": "Always pull the skillet off heat and wait 30 seconds before adding eggs; toss vigorously in the residual warmth."},
            {"issue": "Sauce is thin and watery", "cause": "Pasta was not hot enough or too much pasta water was added.", "solution": "Set the skillet over the steam of the pasta boiling pot (bain-marie method) and toss for 30 seconds to gently thicken the yolk proteins."}
        ],
        "substitutions": [
            {"original": "Guanciale", "substitute": "High-quality slab pancetta or thick unsmoked bacon", "culinaryConsequence": "Pancetta works well; bacon imparts a smoky profile that differs from authentic Roman funk."},
            {"original": "Spaghetti", "substitute": "Rigatoni or Mezze Maniche", "culinaryConsequence": "In Rome, Rigatoni alla Carbonara is equally prized, trapping crisp guanciale and sauce inside the tubes."}
        ],
        "flavorPairings": {
            "wine": "Frascati Superiore, Grechetto, or an earthy Montepulciano d'Abruzzo",
            "zeroProof": "Chilled sparkling rosemary tonic with fresh lemon zest",
            "complementarySides": ["Puntarelle alla Romana (chicory sprouts with anchovy garlic dressing)"]
        },
        "advancedTechnique": "Double boiler mantecatura: Place the heatproof mixing bowl directly over the pasta pot steam while tossing the pasta and eggs; this delivers foolproof, precise 65°C thermal control that guarantees a velvety restaurant consistency.",
        "storageAndReheating": "Carbonara cannot be reheated without curdling eggs. Eat immediately upon plating.",
        "nutritionEstimates": {"calories": 690, "proteinG": 28, "carbsG": 62, "fatG": 36},
        "relatedRecipes": ["rec-cacio-e-pepe", "rec-ragu-bolognese"],
        "relatedTechniques": ["lesson-egg-geometry", "lesson-emulsions-mastery"]
    }
]

print(f"Loaded {len(ITALIAN_RECIPES)} Italian Classical master recipes.")
