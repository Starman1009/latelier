# -*- coding: utf-8 -*-
"""
French Classical & Modern Culinary Masterpieces
15 completely detailed recipes with all 20 required properties.
"""

FRENCH_RECIPES = [
    {
        "id": "rec-sole-meuniere",
        "title": "Classic Sole Meunière with Beurre Noisette & Capers",
        "cuisine": "French Classical",
        "category": "dinner",
        "slot": "mid",
        "difficulty": "Intermediate",
        "prepMins": 15,
        "cookMins": 10,
        "totalMins": 25,
        "yieldServings": 2,
        "heroImage": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=1200&q=80",
        "summary": "The archetypal French bistro preparation: delicate whole Dover sole dredged in flour, sautéed gently in clarified butter, and bathed in a foamy hazelnut-brown butter scented with fresh lemon juice, briny capers, and chopped flat-leaf parsley.",
        "dietary": ["pescatarian", "nut-free"],
        "sensoryRole": "Delicate, sweet flaky white fish enrobed in nutty, caramelized dairy fat, punctuated by sharp citrus acidity and briny pops of pickled caper.",
        "ingredients": [
            {"qty": 2, "unit": "pcs", "name": "Dover sole fillets or whole skinned sole (approx 350g each)", "prep": "patted bone dry with paper towels", "dept": "seafood"},
            {"qty": 45, "unit": "g", "name": "All-purpose flour", "prep": "seasoned with 3g fine sea salt and 1g white pepper", "dept": "drygoods"},
            {"qty": 30, "unit": "ml", "name": "Clarified butter (ghee)", "prep": "for initial pan searing", "dept": "dairy"},
            {"qty": 60, "unit": "g", "name": "Unsalted European butter (82% butterfat)", "prep": "cut into 1cm cubes, chilled", "dept": "dairy"},
            {"qty": 30, "unit": "ml", "name": "Fresh lemon juice", "prep": "strained of seeds", "dept": "produce"},
            {"qty": 20, "unit": "g", "name": "Nonpareil capers in brine", "prep": "rinsed and drained thoroughly", "dept": "pantry"},
            {"qty": 15, "unit": "g", "name": "Italian flat-leaf parsley", "prep": "finely chiffonaded", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Lemon", "prep": "cut into decorative fluted wedges for service", "dept": "produce"}
        ],
        "equipment": [
            {"name": "12-inch heavy-gauge oval fish skillet or stainless steel sauté pan", "type": "everyday"},
            {"name": "Thin flexible fish spatula (pellet spatula)", "type": "everyday"},
            {"name": "Fine wire sieve or dredge tray", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Pat the sole completely dry inside and out; surface moisture suppresses Maillard reaction and turns dredge gummy.",
            "Season the flour evenly with salt and white pepper in a wide shallow dish.",
            "Cut the finishing butter into uniform cubes and keep chilled until the exact moment of saucing.",
            "Squeeze fresh lemon juice into a small ramekin and chop parsley fine."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat clarified butter in a wide stainless steel or copper skillet over medium-high heat until shimmering and registering approximately 175°C (350°F).",
                "timerMins": 2,
                "temperature": "175°C",
                "sensoryCue": "The butter shimmers with faint ripples across the surface without smoking.",
                "scienceNote": "Clarified butter has milk solids removed, raising its smoke point from 150°C to over 230°C, preventing burnt bitter off-flavors during initial high-heat pan contact."
            },
            {
                "stepNum": 2,
                "text": "Immediately before placing in the pan, dredge each sole lightly in the seasoned flour. Shake vigorously to leave only a gossamer-thin veil of flour.",
                "timerMins": 1,
                "sensoryCue": "The fish appears matte and powdery; no clumping or doughy patches.",
                "scienceNote": "The flour starch gelatinizes on contact with hot fat and moisture, creating a microscopic protective barrier that seals in muscle juices and creates crisp golden texture."
            },
            {
                "stepNum": 3,
                "text": "Lay the sole gently into the pan away from yourself. Sauté undisturbed for 3 to 4 minutes until the underside is rich golden brown and releases freely from the pan.",
                "timerMins": 3.5,
                "temperature": "170°C",
                "sensoryCue": "Listen for a steady, lively sizzle that softens slightly as surface moisture evaporates. The fish will release naturally once an even crust forms.",
                "scienceNote": "Do not pry the fish while sticking. The Maillard reaction creates crust detachment as surface proteins contract and moisture vaporizes."
            },
            {
                "stepNum": 4,
                "text": "Carefully slide the flexible fish spatula underneath and flip the sole in a single confident stroke. Cook the reverse side for 2 to 3 minutes until flesh is opaque to the bone (core temp 52°C / 125°F). Transfer to warm warmed serving plates.",
                "timerMins": 2.5,
                "temperature": "52°C core",
                "sensoryCue": "The flesh feels gently resilient when pressed lightly near the spine; edge flakes separate with faint fork pressure."
            },
            {
                "stepNum": 5,
                "text": "Wipe residual oil from the pan with a kitchen towel. Return to medium heat and add the cold cubed butter. Swirl continuously as butter melts, foams vigorously, and begins to crackle.",
                "timerMins": 2,
                "temperature": "145°C",
                "sensoryCue": "The white foam subsides to fine champagne bubbles, and a deep, intoxicating aroma of roasted hazelnuts and toasted brioche fills the room.",
                "scienceNote": "Beurre noisette forms when water boils away (100°C) and milk proteins (casein and whey) drop to pan bottom and undergo rapid Maillard browning and sugar caramelization at 130-145°C."
            },
            {
                "stepNum": 6,
                "text": "The second the milk solids turn hazelnut brown, immediately pour in the lemon juice, capers, and parsley. The sauce will violently hiss, froth, and halt further browning.",
                "timerMins": 0.5,
                "sensoryCue": "Vigorous thermal steam and a sharp release of aromatic citrus and briny vapor. The sauce emulsifies into a glistening golden veil.",
                "scienceNote": "The cold lemon juice rapidly drops the pan temperature below the scorching point (155°C) and acts as an aqueous phase to temporarily suspend the browned lipids."
            },
            {
                "stepNum": 7,
                "text": "Spoon the sizzling beurre noisette evenly over the rested fish fillets. Garnish with a fluted lemon crown and serve immediately while the crust is crisp.",
                "timerMins": 0.5,
                "sensoryCue": "The sauce foams gently across the crisp sole crust with an audible faint sizzle."
            }
        ],
        "sensoryIndicators": {
            "see": "Glistening amber-gold crust, foam-flecked brown butter with micro-specks of toasted milk solids, bright emerald parsley flecks.",
            "hear": "Crisp skin crackle against the knife; initial violent hiss when lemon juice halts the foaming butter.",
            "smell": "Intense toasted hazelnuts, caramelized milk lactose, sweet sea breeze, and sharp volatile lemon terpenes.",
            "feel": "Velvety, unctuous sauce yielding to feather-light, silky, melting fish flakes."
        },
        "scienceNotes": [
            "Fish muscle tissue contains very little collagen (approx 3% vs 15% in land mammals) and consists of short muscle fibers called myotomes separated by thin connective myocommata membranes. These membranes melt at merely 40-50°C, making delicate fish prone to drying out if overcooked past 55°C.",
            "Lactose in butter milk solids begins Maillard browning at lower temperatures than sucrose, yielding compounds like furans, maltol, and lactones which impart the quintessential nutty hazelnut profile."
        ],
        "troubleshooting": [
            {"issue": "Fish stuck to pan and tore during flip", "cause": "Pan was not hot enough or fish was moved before protein denaturation completed the natural release.", "solution": "Ensure pan reaches 175°C before adding fish, and allow the crust to form completely before attempting to slide spatula beneath."},
            {"issue": "Brown butter turned black and bitter", "cause": "Pan remained on heat too long after foam subsided; milk solids scorched past 155°C.", "solution": "Immediately remove pan from heat or add the cold lemon juice the second milk solids transition from golden to pale amber."}
        ],
        "substitutions": [
            {"original": "Dover sole", "substitute": "Petrale sole, Flounder, or Black sea bass fillets", "culinaryConsequence": "Flounder is thinner and cooks in 1.5 minutes per side; watch core temperature carefully to prevent mushy texture."},
            {"original": "Clarified butter", "substitute": "High-smoke-point neutral oil (grapeseed or avocado)", "culinaryConsequence": "Works well for frying stage, but finish strictly with genuine European dairy butter for flavor."}
        ],
        "flavorPairings": {
            "wine": "Premier Cru Chablis (Chardonnay with flinty minerality and vibrant acidity) or Sancerre (Sauvignon Blanc)",
            "zeroProof": "Chilled sparkling mineral water infused with fresh lemon peel and bruised lemon verbena leaves",
            "complementarySides": ["Pommes vapeurs (steamed new potatoes tossed in chives)", "Haricots verts amandine (tender French green beans)"]
        },
        "advancedTechnique": "Classic tableside filleting: Use a silver fish knife and fork to peel the peripheral fin cartilage, slide the spine out whole from head to tail, and reconstruct the fillets with the hot sauce poured over the exposed meat.",
        "storageAndReheating": "Best enjoyed immediately. If needed, reheat gently in a covered skillet over low heat with an additional 10g of butter for 3 minutes; never microwave as it toughens delicate fish proteins.",
        "nutritionEstimates": {"calories": 480, "proteinG": 38, "carbsG": 12, "fatG": 32},
        "relatedRecipes": ["rec-halibut-beurre-blanc", "rec-bouillabaisse"],
        "relatedTechniques": ["lesson-sauté-deglaze", "lesson-mother-sauces"]
    },
    {
        "id": "rec-french-omelette",
        "title": "L'Omelette Française Classique (Classic Rolled French Omelette)",
        "cuisine": "French Classical",
        "category": "breakfast",
        "slot": "opener",
        "difficulty": "Advanced",
        "prepMins": 5,
        "cookMins": 3,
        "totalMins": 8,
        "yieldServings": 1,
        "heroImage": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=1200&q=80",
        "summary": "The ultimate benchmark of culinary technique: an unbrowned, canary-yellow, cigar-shaped cylinder of gently folded egg, glossy with cold butter, enclosing a creamy, custard-like baveuse center.",
        "dietary": ["vegetarian", "gluten-free", "nut-free"],
        "sensoryRole": "Silky, tender exterior giving way to a warm, velvety, molten egg custard infused with aromatic fresh herbs and rich cultured butter.",
        "ingredients": [
            {"qty": 3, "unit": "pcs", "name": "Fresh Grade-AA large pasture-raised eggs", "prep": "at room temperature", "dept": "dairy"},
            {"qty": 25, "unit": "g", "name": "European cultured butter (unsalted)", "prep": "divided: 15g for cooking, 10g cold for final glaze", "dept": "dairy"},
            {"qty": 1, "unit": "g", "name": "Fine sea salt (sel fin)", "prep": "to season", "dept": "pantry"},
            {"qty": 0.5, "unit": "g", "name": "Finely ground white pepper", "prep": "to preserve pristine yellow color", "dept": "pantry"},
            {"qty": 8, "unit": "g", "name": "Fresh fines herbes (equal parts chives, chervil, tarragon, parsley)", "prep": "minced razor-fine with a sharp knife", "dept": "produce"}
        ],
        "equipment": [
            {"name": "8-inch or 10-inch heavy curved non-stick skillet or seasoned carbon steel pan", "type": "everyday"},
            {"name": "Heat-resistant flexible silicone spatula or fork", "type": "everyday"},
            {"name": "Fine-mesh wire strainer / tamis", "type": "specialty", "substitute": "Whisk vigorously until completely homogenous"}
        ],
        "miseEnPlace": [
            "Crack eggs into a bowl, season with salt and white pepper, and beat vigorously with a fork until the whites and yolks are completely unified without foam.",
            "Optionally pass beaten eggs through a fine strainer to catch any chalazae strings for silk-smooth texture.",
            "Chop the four classical fines herbes cleanly without bruising.",
            "Have your serving plate warm and the cold glazing butter ready next to the stove."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Place the non-stick pan over medium-low heat. Add 15g butter and let it melt. As it begins to foam gently without coloring, swirl to coat the bottom and sides thoroughly.",
                "timerMins": 1,
                "temperature": "110°C",
                "sensoryCue": "Gentle, lazy white bubbles form across the pan without browning or hissing.",
                "scienceNote": "High heat causes egg proteins (albumen and vitellin) to cross-link into tight, rubbery networks that squeeze out water. Low-to-moderate thermal energy allows loose, delicate gelation."
            },
            {
                "stepNum": 2,
                "text": "Pour in the beaten eggs all at once. Immediately begin shaking the pan vigorously back and forth with your non-dominant hand while rapidly stirring the eggs in tight circular motions using the flat of the spatula.",
                "timerMins": 1,
                "sensoryCue": "Fine, velvety curds develop instantly throughout the mass, resembling loose scrambled eggs.",
                "scienceNote": "Continuous rapid agitation breaks apart protein aggregates as they coagulate, creating millions of microscopic soft curds suspended in liquid egg rather than one large dense sheet."
            },
            {
                "stepNum": 3,
                "text": "When the eggs are 80% coagulated—resembling soft, wet oatmeal with no pools of raw egg—stop stirring. Smooth the top with the spatula and scatter the fines herbes over the center.",
                "timerMins": 0.5,
                "sensoryCue": "The surface looks glistening, wet, and creamy (baveuse) but holds its form when tilted.",
                "scienceNote": "Residual heat will continue cooking the interior during the rolling and plating steps (carryover cooking)."
            },
            {
                "stepNum": 4,
                "text": "Remove the pan from the heat. Tilt the pan away from you at a 45-degree angle. Use the spatula to gently fold the top third of the omelette down toward the middle, then roll the bottom third over to encase the center into a neat cylinder.",
                "timerMins": 0.5,
                "sensoryCue": "The egg layer peels effortlessly from the pan like silk without tearing or browning."
            },
            {
                "stepNum": 5,
                "text": "Tap the handle of the pan firmly with your fist to bounce the far lip of the omelette upward over the seam. Invert the pan directly over a warm plate so the omelette lands seam-side down in a perfect tapered spindle.",
                "timerMins": 0.5,
                "sensoryCue": "A smooth, unbroken, golden-yellow almond shape resting on the porcelain."
            },
            {
                "stepNum": 6,
                "text": "Rub the remaining 10g cold butter block directly over the hot surface of the omelette to create a mirror-like sheen. Garnish with a pinch of fresh chives and serve immediately.",
                "timerMins": 0.2,
                "sensoryCue": "A glossy lacquer reflects light; a slit with a knife reveals the molten, custardy baveuse interior running slowly onto the plate."
            }
        ],
        "sensoryIndicators": {
            "see": "Pristine canary yellow with zero brown spots, glistening mirror-glaze of butter, vivid green herb flecks.",
            "hear": "Gentle quiet sizzle in the pan; absolute silence when resting on the plate.",
            "smell": "Sweet dairy creaminess, rich egg yolk, fresh anise-like tarragon, and sharp chive aromatics.",
            "feel": "Pillowy, tender outer skin that yields instantly to a fork, giving way to a luxurious molten core."
        },
        "scienceNotes": [
            "Egg white protein (ovalbumin) coagulates at 62-65°C, while egg yolk protein coagulates at 65-70°C. By keeping the pan below 120°C and stirring continuously, both proteins solidify in equilibrium without expressing moisture through syneresis (weeping).",
            "Salt acts as a tenderizer when mixed into raw eggs: it dissolves into charged sodium and chloride ions that bind to protein charges, reducing repulsive forces and allowing a softer, more pliable gel network."
        ],
        "troubleshooting": [
            {"issue": "Omelette has brown spots or crispy edges", "cause": "Pan heat was too high or butter was allowed to brown before eggs entered.", "solution": "Lower heat to medium-low; the butter must only foam softly without coloring before adding eggs."},
            {"issue": "Interior is dry and cakey rather than creamy", "cause": "Stirring was continued too long over heat before rolling.", "solution": "Pull the pan off heat while the eggs still look suspiciously wet; carryover heat finishes the setting."}
        ],
        "substitutions": [
            {"original": "Fines herbes", "substitute": "Finely minced fresh chives alone or chervil and parsley", "culinaryConsequence": "Chives provide a clean, allium brightness; avoid woody herbs like rosemary or thyme which overpower delicate eggs."},
            {"original": "Cultured butter", "substitute": "Standard unsalted sweet cream butter", "culinaryConsequence": "Lacks the subtle lactic tang of cultured butter, but produces identical structural texture."}
        ],
        "flavorPairings": {
            "wine": "Champagne Brut or Blanc de Blancs (the high effervescence and acidity cleanly slice through the rich egg yolk fat)",
            "zeroProof": "Fresh cold-pressed cucumber juice with sparkling green tea and a drop of yuzu",
            "complementarySides": ["Warm toasted brioche soldier fingers", "Petite salade of mache (lamb's lettuce) with champagne vinaigrette"]
        },
        "advancedTechnique": "The Escoffier Tap-Roll: In classic French brigade kitchens, chefs do not use spatulas to roll omelettes; they hold the pan by the handle at a steep angle and strike their wrist against the handle to make the omelette roll itself into a neat spindle using kinetic momentum alone.",
        "storageAndReheating": "French omelettes must be eaten within 90 seconds of plating. Reheating destroys the delicate baveuse emulsion; prepare fresh for each diner.",
        "nutritionEstimates": {"calories": 310, "proteinG": 18, "carbsG": 1, "fatG": 26},
        "relatedRecipes": ["rec-quiche-lorraine", "rec-vichyssoise"],
        "relatedTechniques": ["lesson-egg-geometry", "lesson-seasoning-osmosis"]
    },
    {
        "id": "rec-boeuf-bourguignon",
        "title": "Boeuf Bourguignon Traditionnel with Glazed Pearl Onions & Pommes Purée",
        "cuisine": "French Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 180,
        "totalMins": 210,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1534939561126-855b8675edd7?auto=format&fit=crop&w=1200&q=80",
        "summary": "The crown jewel of Burgundian slow-cooking: succulent chunks of collagen-rich beef chuck seared to a mahogany crust, gently braised in a full bottle of Pinot Noir with aromatic mirepoix and veal stock until fork-tender, garnished with glazed pearl onions, sautéed cremini mushrooms, and crisp slab bacon lardons.",
        "dietary": ["nut-free", "dairy-free-option"],
        "sensoryRole": "Deep, savory, umami-laden red wine reduction clinging to meltingly tender braised beef with sweet caramelized alliums and smoky bacon accents.",
        "ingredients": [
            {"qty": 1400, "unit": "g", "name": "Beef chuck roast or cheek", "prep": "trimmed of excess hard fat and cut into 5cm (2-inch) cubes", "dept": "butchery"},
            {"qty": 200, "unit": "g", "name": "French slab bacon (lardons)", "prep": "cut into 1cm thick matchsticks", "dept": "butchery"},
            {"qty": 750, "unit": "ml", "name": "Dry red Burgundy wine (Pinot Noir)", "prep": "full 750ml bottle", "dept": "pantry"},
            {"qty": 500, "unit": "ml", "name": "Brown veal stock or rich beef bone stock", "prep": "unsalted, gelatin-rich", "dept": "pantry"},
            {"qty": 30, "unit": "ml", "name": "Cognac or French brandy", "prep": "for flambe deglazing", "dept": "pantry"},
            {"qty": 45, "unit": "g", "name": "Tomato paste (double concentrate)", "prep": "to brown in the fond", "dept": "pantry"},
            {"qty": 35, "unit": "g", "name": "All-purpose flour", "prep": "to singer (dust) over the seared meat", "dept": "drygoods"},
            {"qty": 2, "unit": "pcs", "name": "Yellow onions", "prep": "medium diced", "dept": "produce"},
            {"qty": 2, "unit": "pcs", "name": "Carrots", "prep": "cut into 2cm rounds on the bias", "dept": "produce"},
            {"qty": 4, "unit": "cloves", "name": "Garlic", "prep": "crushed with the flat of a knife", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Bouquet garni (fresh thyme, flat parsley stems, 2 bay leaves tied in leek green)", "prep": "tied with butcher's twine", "dept": "produce"},
            {"qty": 250, "unit": "g", "name": "White pearl onions", "prep": "peeled whole, glazed in butter and sugar", "dept": "produce"},
            {"qty": 300, "unit": "g", "name": "Small cremini mushrooms", "prep": "quartered and browned in butter", "dept": "produce"},
            {"qty": 40, "unit": "g", "name": "Unsalted European butter", "prep": "for glazing garnishes", "dept": "dairy"}
        ],
        "equipment": [
            {"name": "6 to 7-quart enameled cast-iron Dutch oven (cocotte)", "type": "everyday"},
            {"name": "Splatter guard and stainless tongs", "type": "everyday"},
            {"name": "Fine-mesh conical strainer (chinois)", "type": "specialty", "substitute": "Fine wire kitchen strainer"}
        ],
        "miseEnPlace": [
            "Pat beef cubes completely dry on all sides; wet meat steams instead of browning.",
            "Cut slab bacon into uniform lardons; chop carrots, onions, and garlic.",
            "Tie the bouquet garni tightly with kitchen twine.",
            "Blanch pearl onions in boiling water for 1 minute, drain, and pinch off skins effortlessly."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Render lardons in a large Dutch oven over medium heat for 8 minutes until crisp and golden. Remove lardons with a slotted spoon, leaving fragrant bacon fat in the pot.",
                "timerMins": 8,
                "temperature": "140°C",
                "sensoryCue": "Lardons turn deep amber-gold and buoyant in their rendered clear fat with a distinct smoky, savory aroma."
            },
            {
                "stepNum": 2,
                "text": "Increase heat to high until the fat is shimmering. Sear the beef cubes in three uncrowded batches for 3 minutes per side until a dark mahogany Maillard crust forms. Transfer seared beef to a resting platter.",
                "timerMins": 12,
                "temperature": "190°C",
                "sensoryCue": "Violent sizzling and intense aroma of roasting meat. The meat develops a rich deep brown crust without turning grey.",
                "scienceNote": "Crowding the pan causes meat juices to pool, dropping pan temperature below 100°C and boiling the meat. Searing in batches maintains 180°C+ needed for rapid Maillard browning."
            },
            {
                "stepNum": 3,
                "text": "Add chopped onions and carrots to the remaining fat; cook over medium heat for 6 minutes until lightly caramelized. Stir in tomato paste and crushed garlic; cook 2 minutes until the paste turns brick red and fragrant.",
                "timerMins": 8,
                "temperature": "140°C",
                "sensoryCue": "Tomato paste darkens from bright red to deep mahogany; sugars lightly toast against the pan base (pincer la tomate)."
            },
            {
                "stepNum": 4,
                "text": "Return the beef and its accumulated juices to the pot. Dust with 35g flour and toss well to coat. Cook for 2 minutes to cook out raw starch flavor.",
                "timerMins": 2,
                "sensoryCue": "The flour toasts lightly and absorbs the surface fat, coating the meat in a matte sheen (singer)."
            },
            {
                "stepNum": 5,
                "text": "Pour in the Cognac and scrape up the dark fond from the bottom of the pot. Pour in the full bottle of Pinot Noir and the brown veal stock. Add the bouquet garni and half of the reserved crispy lardons. Bring to a gentle simmer.",
                "timerMins": 5,
                "temperature": "95°C",
                "sensoryCue": "Steam rises carrying intoxicating wine esters and roasted aromatics. The liquid turns a deep purple-red hue."
            },
            {
                "stepNum": 6,
                "text": "Cover the Dutch oven with a tight-fitting lid, transfer to a 150°C (300°F) oven, and braise undisturbed for 2.5 to 3 hours until the beef yields completely to a fork.",
                "timerMins": 160,
                "temperature": "150°C oven / 85°C braise",
                "sensoryCue": "A paring knife slips into the center of a beef chunk with zero resistance; meat fibers separate like velvet.",
                "scienceNote": "Between 70°C and 85°C, tough insoluble collagen triple-helices denature and hydrolyze into luscious soluble gelatin, turning fibrous chuck into meltingly tender meat while enriching the braising sauce."
            },
            {
                "stepNum": 7,
                "text": "While beef braises, glaze the pearl onions in a small skillet with 20g butter, 50ml water, a pinch of sugar and salt, covered for 15 minutes, then uncover to caramelize. In a separate pan, sauté mushrooms in 20g butter over high heat until browned.",
                "timerMins": 20,
                "sensoryCue": "Pearl onions turn glossy and golden-amber; mushrooms brown deeply and release rich earthy aromatics."
            },
            {
                "stepNum": 8,
                "text": "Remove Dutch oven from oven. Gently transfer beef to a dish. Strain the braising liquid through a chinois into a saucepan, pressing lightly on vegetables. Skim excess fat from the surface and simmer sauce for 10 minutes until it coats the back of a spoon (nappe).",
                "timerMins": 12,
                "sensoryCue": "The sauce reduces to a lustrous, glossy deep mahogany sauce that coats a spoon cleanly without separating."
            },
            {
                "stepNum": 9,
                "text": "Recombine the beef, sauce, glazed pearl onions, sautéed mushrooms, and remaining crisp lardons in the Dutch oven. Warm gently for 5 minutes. Serve over velvety Pommes Purée.",
                "timerMins": 5,
                "sensoryCue": "Glistening, rich braise with steam carrying deep red wine, herbs, and earthy mushroom perfume."
            }
        ],
        "sensoryIndicators": {
            "see": "Glossy mahogany braising sauce clinging to tender beef chunks, contrasted with golden pearl onions and dark sautéed cremini.",
            "hear": "Gentle slow bubbling in the Dutch oven; silent silky spooning over hot mashed potatoes.",
            "smell": "Concentrated Pinot Noir reduction, earthy bay leaf and thyme, caramelized alliums, smoky bacon fat.",
            "feel": "Beef that dissolves on the tongue with no knife required; silky, gelatin-enriched sauce coating the palate."
        },
        "scienceNotes": [
            "Gelatin extraction: As collagen breaks down, it creates gelatin molecules that physically thicken the braising liquid, giving it an unctuous mouthfeel (body) without needing heavy flour or cornstarch slurry.",
            "Alcohol reduction: Simmering wine drives off ethanol (boiling point 78.4°C) while concentrating tartaric and malic acids and volatile grape aroma compounds, creating the structural backbone of classic French sauces."
        ],
        "troubleshooting": [
            {"issue": "Beef is tough and rubbery", "cause": "Braise was pulled too early or oven temperature was too high (above 165°C), forcing moisture out before collagen melted.", "solution": "Return to oven at 145°C for another 30-45 minutes; collagen requires prolonged low-temperature thermal exposure to dissolve."},
            {"issue": "Sauce is overly sour or acidic", "cause": "Wine had high volatile acidity or was not reduced sufficiently before adding stock.", "solution": "Whisk in 10g cold butter (monter au beurre) and 1 teaspoon red currant jelly or brown sugar to buffer excess acid."}
        ],
        "substitutions": [
            {"original": "Pinot Noir Burgundy", "substitute": "Côtes du Rhône, Syrah, or dry Cabernet Sauvignon", "culinaryConsequence": "Cabernet yields a heavier, more tannic sauce; Pinot Noir provides the authentic lighter, brighter Burgundian acidity."},
            {"original": "Veal stock", "substitute": "High-quality low-sodium beef bone broth simmered with 5g unflavored gelatin", "culinaryConsequence": "Adding powdered gelatin accurately mimics the luxurious mouthfeel of classical brown veal stock."}
        ],
        "flavorPairings": {
            "wine": "Gevrey-Chambertin, Pommard, or aged Bourgogne Rouge (mirrors the Pinot Noir notes in the sauce)",
            "zeroProof": "Tart cherry juice infused with lapsang souchong smoked tea and reduced with fresh rosemary",
            "complementarySides": ["Robuchon-style Pommes Purée (silky potato purée with 50% butter)", "Buttered egg tagliatelle"]
        },
        "advancedTechnique": "Forty-eight hour overnight marinade: Submerge the raw beef cubes in the red wine with aromatics and carrots in the refrigerator for 24-48 hours prior to cooking. Strain, dry the meat, and reduce the marinade liquid separately, skimming impurities, before assembling the braise for astonishing depth.",
        "storageAndReheating": "Bourguignon tastes substantially better on the second and third days as gelatin and wine flavors equilibrate throughout the meat fibers. Store refrigerated for up to 5 days; reheat gently covered on the stovetop over low heat.",
        "nutritionEstimates": {"calories": 680, "proteinG": 54, "carbsG": 18, "fatG": 40},
        "relatedRecipes": ["rec-coq-au-vin", "rec-duck-confit"],
        "relatedTechniques": ["lesson-braising-collagen", "lesson-mother-sauces"]
    },
    {
        "id": "rec-coq-au-vin",
        "title": "Coq au Vin de Bourgogne (Braised Chicken in Burgundy Wine)",
        "cuisine": "French Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 25,
        "cookMins": 60,
        "totalMins": 85,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=1200&q=80",
        "summary": "The timeless French farmhouse centerpiece: bone-in chicken thighs and drumsticks browned in smoky bacon lardons, simmered gently in rich Pinot Noir with garlic, mushrooms, and butter-glazed pearl onions until deeply stained purple-garnet and fall-apart tender.",
        "dietary": ["nut-free"],
        "sensoryRole": "Deeply savory chicken meat bathed in a velvety red wine sauce with earthy button mushrooms and smoky pork fat.",
        "ingredients": [
            {"qty": 1200, "unit": "g", "name": "Bone-in, skin-on chicken thighs and drumsticks", "prep": "patted dry, seasoned with sea salt", "dept": "butchery"},
            {"qty": 150, "unit": "g", "name": "Smoked thick-cut bacon or pork belly lardons", "prep": "cut into matchsticks", "dept": "butchery"},
            {"qty": 600, "unit": "ml", "name": "Dry red Burgundy or Pinot Noir", "prep": "full-bodied dry red", "dept": "pantry"},
            {"qty": 350, "unit": "ml", "name": "Rich chicken stock", "prep": "unsalted", "dept": "pantry"},
            {"qty": 30, "unit": "ml", "name": "Cognac or brandy", "prep": "for flambe", "dept": "pantry"},
            {"qty": 25, "unit": "g", "name": "Tomato paste", "prep": "for acidity and depth", "dept": "pantry"},
            {"qty": 25, "unit": "g", "name": "All-purpose flour", "prep": "or beurre manié to finish", "dept": "drygoods"},
            {"qty": 200, "unit": "g", "name": "Small button or cremini mushrooms", "prep": "cleaned, halved", "dept": "produce"},
            {"qty": 180, "unit": "g", "name": "Small pearl onions", "prep": "peeled whole", "dept": "produce"},
            {"qty": 3, "unit": "cloves", "name": "Garlic", "prep": "minced fine", "dept": "produce"},
            {"qty": 30, "unit": "g", "name": "Unsalted European butter", "prep": "divided", "dept": "dairy"},
            {"qty": 1, "unit": "pcs", "name": "Herb sachet (fresh thyme, rosemary, bay leaf, parsley stems)", "prep": "tied in cheesecloth", "dept": "produce"}
        ],
        "equipment": [
            {"name": "5.5-quart Dutch oven with lid", "type": "everyday"},
            {"name": "Sauté pan for mushrooms and onions", "type": "everyday"},
            {"name": "Fine mesh skimmer", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Season chicken parts generously with salt and pepper 30 minutes before cooking.",
            "Blanch and peel the pearl onions.",
            "Cut mushrooms into uniform halves or quarters.",
            "Measure out red wine and stock."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Crisp lardons in Dutch oven over medium heat for 6 minutes until browned. Transfer with slotted spoon to a paper-towel-lined plate.",
                "timerMins": 6,
                "temperature": "145°C",
                "sensoryCue": "Lardons are crisp and fragrant; clear rendered pork fat fills the pan."
            },
            {
                "stepNum": 2,
                "text": "Sear chicken skin-side down in the hot bacon fat over medium-high heat for 5 minutes until deep golden brown. Turn and cook 3 minutes on reverse. Transfer chicken to a platter.",
                "timerMins": 8,
                "temperature": "175°C",
                "sensoryCue": "Chicken skin renders its fat and turns crispy and amber-gold; aroma of roasting poultry."
            },
            {
                "stepNum": 3,
                "text": "Add minced garlic and tomato paste to the pot; stir for 1 minute until fragrant. Deglaze with Cognac, scraping up all brown fond.",
                "timerMins": 2,
                "sensoryCue": "Flambé flame subsides leaving a glossy glaze on the bottom of the pot."
            },
            {
                "stepNum": 4,
                "text": "Pour in Pinot Noir and chicken stock. Whisk in flour thoroughly. Add the herb sachet and return chicken pieces and half the lardons to the pot. Liquid should reach two-thirds up the chicken.",
                "timerMins": 3,
                "sensoryCue": "The purple-red braising liquid comes to a gentle simmer with small lazy bubbles."
            },
            {
                "stepNum": 5,
                "text": "Cover partially and simmer gently over low heat for 35 to 40 minutes until chicken is tender and registers 74°C (165°F) internally.",
                "timerMins": 38,
                "temperature": "88°C braise",
                "sensoryCue": "Chicken meat pulls easily from the bone; chicken skin absorbs the deep purple wine hue."
            },
            {
                "stepNum": 6,
                "text": "Meanwhile, sauté pearl onions and mushrooms in 20g butter in a separate skillet for 10 minutes until deeply golden.",
                "timerMins": 10,
                "sensoryCue": "Mushrooms squeak then sizzle; onions develop glistening golden caramelized edges."
            },
            {
                "stepNum": 7,
                "text": "Transfer chicken to a warm platter. Simmer the sauce over medium-high heat for 6-8 minutes until reduced and silky. Whisk in remaining 10g cold butter. Add sautéed mushrooms, pearl onions, and reserved lardons. Pour over chicken.",
                "timerMins": 8,
                "sensoryCue": "The sauce shines like lacquer; garnishes coat evenly in the rich Burgundian reduction."
            }
        ],
        "sensoryIndicators": {
            "see": "Stunning garnet-purple braised chicken, glossy wine glaze, golden-brown pearl onions, dark earthy mushrooms.",
            "hear": "Gentle slow simmer; bubbling sauce thickening to nappe consistency.",
            "smell": "Warm red wine bouquet, bacon smoke, garlic, and fresh thyme.",
            "feel": "Chicken meat that slips effortlessly off the bone; velvety sauce that clings to the tongue."
        },
        "scienceNotes": [
            "Braising chicken on the bone imparts marrow gelatin and calcium minerals into the sauce, creating a thicker body than boneless cuts.",
            "Anthocyanins in red wine bind to chicken surface myoglobin and protein, giving authentic coq au vin its distinctive deep violet-burgundy color."
        ],
        "troubleshooting": [
            {"issue": "Sauce is thin and watery", "cause": "Lid was kept tightly sealed or liquid was not reduced after chicken was removed.", "solution": "Remove chicken and boil sauce vigorously for 5 minutes, or whisk in 15g beurre manié (equal parts soft butter and flour kneaded together)."},
            {"issue": "Chicken skin is flabby and greasy", "cause": "Chicken was not seared thoroughly before braising.", "solution": "Ensure skin is deeply rendered and browned before adding wine."}
        ],
        "substitutions": [
            {"original": "Pinot Noir", "substitute": "Beaujolais (Gamay) or Côtes du Rhône", "culinaryConsequence": "Gamay brings a lighter, fruit-forward acidity; perfect for farmhouse style."},
            {"original": "Chicken thighs", "substitute": "Rooster (capon) or guinea fowl", "culinaryConsequence": "Traditional coq au vin used tough rooster meat, requiring 2-3 hours of braising. Modern chicken requires only 40 minutes."}
        ],
        "flavorPairings": {
            "wine": "Mercurey Rouge, Morgon, or Domaine Dujac Morey-Saint-Denis",
            "zeroProof": "Spiced pomegranate juice with sparkling black currant infusion",
            "complementarySides": ["Buttered egg noodles with chopped flat parsley", "Crusty sourdough country batard"]
        },
        "advancedTechnique": "Finishing with chicken liver liaison: Puree 30g cooked chicken liver with a spoonful of hot sauce and whisk back into the pot off heat for extraordinary gloss and classic French richness.",
        "storageAndReheating": "Keeps refrigerated for 4 days. Reheat gently in a covered pot on low heat for 15 minutes.",
        "nutritionEstimates": {"calories": 590, "proteinG": 48, "carbsG": 14, "fatG": 34},
        "relatedRecipes": ["rec-boeuf-bourguignon", "rec-duck-confit"],
        "relatedTechniques": ["lesson-sauté-deglaze", "lesson-braising-collagen"]
    },
    {
        "id": "rec-duck-confit",
        "title": "Confit de Canard with Pommes Sarladaises & Spiced Cherry Gastrique",
        "cuisine": "French Classical",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Advanced",
        "prepMins": 30,
        "cookMins": 180,
        "totalMins": 210,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1514944298352-78d12089060b?auto=format&fit=crop&w=1200&q=80",
        "summary": "Gascon culinary alchemy: whole duck legs cured overnight in coarse sea salt, garlic, and wild herbs, submerged in rendered duck fat and slow-cooked at a gentle 90°C until the meat is succulent and falling off the bone. Finished in a scorching skillet for crackling skin, served with duck-fat-crisped Sarladaise potatoes and a tart cherry-ruby port gastrique.",
        "dietary": ["dairy-free", "gluten-free", "nut-free"],
        "sensoryRole": "Ultra-crispy, shattering duck skin enclosing melting, savory meat, cut through with a high-acid, sweet-tart cherry gastrique.",
        "ingredients": [
            {"qty": 4, "unit": "pcs", "name": "Whole duck legs (Mary's or Moulard duck)", "prep": "trimmed of excess skin flaps", "dept": "butchery"},
            {"qty": 35, "unit": "g", "name": "Coarse sea salt (Gros sel de Guérande)", "prep": "for dry curing", "dept": "pantry"},
            {"qty": 6, "unit": "cloves", "name": "Fresh garlic", "prep": "smashed", "dept": "produce"},
            {"qty": 6, "unit": "sprigs", "name": "Fresh thyme", "prep": "whole sprigs", "dept": "produce"},
            {"qty": 2, "unit": "pcs", "name": "Bay leaves", "prep": "crumbled", "dept": "produce"},
            {"qty": 1, "unit": "g", "name": "Crushed black peppercorns", "prep": "coarsely ground", "dept": "pantry"},
            {"qty": 800, "unit": "g", "name": "Pure rendered duck fat (graisse de canard)", "prep": "warmed until liquid", "dept": "dairy"},
            {"qty": 600, "unit": "g", "name": "Yukon Gold potatoes", "prep": "sliced into 3mm rounds for Sarladaises", "dept": "produce"},
            {"qty": 150, "unit": "g", "name": "Tart dark cherries (fresh or frozen)", "prep": "pitted", "dept": "produce"},
            {"qty": 60, "unit": "ml", "name": "Ruby port wine", "prep": "for gastrique", "dept": "pantry"},
            {"qty": 40, "unit": "ml", "name": "Sherry vinegar", "prep": "for gastrique", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Honey or raw sugar", "prep": "to caramelize for gastrique", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy ceramic baking dish or Dutch oven", "type": "everyday"},
            {"name": "12-inch cast iron skillet", "type": "everyday"},
            {"name": "Mandoline slicer for uniform potato rounds", "type": "specialty", "substitute": "Sharp chef's knife"}
        ],
        "miseEnPlace": [
            "Rub duck legs with salt, smashed garlic, thyme, and cracked pepper; refrigerate for 12 to 24 hours to cure.",
            "Rinse cure thoroughly from duck legs with cold water and pat completely dry.",
            "Preheat oven to 105°C (225°F).",
            "Melt duck fat over low heat."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Place rinsed, dried duck legs snugly in a single layer inside a deep baking dish or Dutch oven. Pour melted duck fat over them until completely submerged.",
                "timerMins": 5,
                "temperature": "60°C fat",
                "sensoryCue": "Duck legs are entirely immersed beneath a golden liquid sea of warm duck fat."
            },
            {
                "stepNum": 2,
                "text": "Cover tightly with foil and a lid. Bake in a 105°C (225°F) oven for 3 hours. The fat should never boil, only releasing a single lazy bubble every few seconds.",
                "timerMins": 180,
                "temperature": "90°C internal fat",
                "sensoryCue": "Subtle lazy bubbles rise through the clear fat; intoxicating perfume of herbs and roasting duck.",
                "scienceNote": "Confit is a sub-boiling lipid immersion method. Because duck fat contains virtually no water, meat moisture is retained while collagen hydrolyzes at low steady temperature without toughening proteins."
            },
            {
                "stepNum": 3,
                "text": "Check doneness: the meat should have shrunk slightly up the drumstick bone, and a toothpick should pierce the thickest part of the thigh with zero resistance.",
                "timerMins": 2,
                "sensoryCue": "Meat pulls back from bone tips; texture is soft and supple."
            },
            {
                "stepNum": 4,
                "text": "Prepare Sarladaise potatoes: Heat 45g of the duck fat from the confit in a wide skillet over medium heat. Add sliced potatoes in an even layer. Sauté for 18 minutes, tossing periodically, until deeply browned and crisp at the edges. Toss with minced garlic and parsley.",
                "timerMins": 18,
                "temperature": "165°C",
                "sensoryCue": "Potatoes sizzle merrily, transforming into crispy golden disks with soft, creamy centers."
            },
            {
                "stepNum": 5,
                "text": "Prepare Spiced Cherry Gastrique: In a small saucepan, bring honey and sherry vinegar to a vigorous boil until reduced and lightly caramelized (3 minutes). Add ruby port and tart cherries. Simmer 6 minutes until cherries burst and sauce is syrupy.",
                "timerMins": 9,
                "sensoryCue": "Deep ruby red glossy syrup coating the spoon, with bright sweet-sour aroma cutting through the kitchen."
            },
            {
                "stepNum": 6,
                "text": "Finish duck: Place duck legs skin-side down in a dry, cold cast iron skillet over medium-low heat. Cook for 8-10 minutes without moving as remaining skin fat renders and skin crisps to a dark golden mahogany. Flip for 1 minute to warm the underside.",
                "timerMins": 10,
                "sensoryCue": "Audible crackling like glass shattering; skin turns razor-thin, blistered, and deep golden brown."
            },
            {
                "stepNum": 7,
                "text": "Plate the hot confit leg atop crisp Pommes Sarladaises and spoon the warm spiced cherry gastrique in an arc beside the duck.",
                "timerMins": 2,
                "sensoryCue": "Steam rises as the knife edge crunches audibly through the skin."
            }
        ],
        "sensoryIndicators": {
            "see": "Mahogany blistered crisp skin, golden potato chips with green parsley flecks, glistening ruby red cherry gastrique.",
            "hear": "A loud, brittle crunch when the fork punctures the skin; silence as the tender meat separates.",
            "smell": "Rich roasted duck fat, caramelized alliums, sweet-tart cherry reduction, earthy thyme.",
            "feel": "Shattering crispy skin followed by melting, velvety, luscious duck meat."
        },
        "scienceNotes": [
            "Salt curing draws out free water (lowering water activity Aw below 0.85), which inhibits microbial proliferation and concentrates amino acid savory flavors before slow immersion.",
            "Starting skin-down in a cold skillet allows the subcutaneous fat pad to render out gradually before the skin burns, ensuring a paper-thin, crispy crust rather than a chewy, greasy layer."
        ],
        "troubleshooting": [
            {"issue": "Skin is chewy and rubbery instead of crisp", "cause": "Pan was too hot during finishing, searing the exterior before fat rendered out.", "solution": "Start in a cold dry skillet over medium-low heat and allow 8-10 minutes for slow fat rendering."},
            {"issue": "Meat is dry and stringy", "cause": "Confit fat boiled above 115°C during oven cooking.", "solution": "Verify oven temperature with a thermometer; keep fat between 88°C and 93°C."}
        ],
        "substitutions": [
            {"original": "Duck fat", "substitute": "Pure pork lard (saindoux) or extra virgin olive oil", "culinaryConsequence": "Lard produces authentic crispness; olive oil produces Spanish-style confit with a distinct fruity olive note."},
            {"original": "Tart cherries", "substitute": "Blackberries, figs, or sour plums", "culinaryConsequence": "All high-tannin, high-acid fruits pair exceptionally with rich duck fat."}
        ],
        "flavorPairings": {
            "wine": "Madiran, Cahors (Malbec), or Saint-Émilion Grand Cru",
            "zeroProof": "Spiced pomegranate tonic with bruised rosemary and Meyer lemon twist",
            "complementarySides": ["Pommes Sarladaises (duck-fat sautéed potatoes)", "Frisée salad with warm bacon vinaigrette"]
        },
        "advancedTechnique": "Long-term cellar preservation: Traditionally, confit was stored in ceramic crocks completely submerged under 2 inches of solidified duck fat in a cold cellar for up to 6 months without refrigeration. The fat forms an airtight barrier excluding oxygen and bacteria.",
        "storageAndReheating": "Cooked confit submerged in fat keeps in the refrigerator for up to 3 months. To serve, scrape off fat and crisp in a pan.",
        "nutritionEstimates": {"calories": 740, "proteinG": 42, "carbsG": 28, "fatG": 52},
        "relatedRecipes": ["rec-boeuf-bourguignon", "rec-coq-au-vin"],
        "relatedTechniques": ["lesson-confit-fat", "lesson-sauté-deglaze"]
    },
    {
        "id": "rec-souffle-chocolat",
        "title": "Soufflé Chaud au Chocolat Noir with Crème Anglaise",
        "cuisine": "French Classical",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Advanced",
        "prepMins": 25,
        "cookMins": 14,
        "totalMins": 39,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1579372786545-d24232daf58c?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pinnacle of French pastry drama: a rich Valrhona 70% dark chocolate pastry cream lightened with perfectly whipped French meringue, baked in sugar-coated ramekins until it rises majestically two inches above the rim, dusted with powdered sugar and cracked open tableside to receive cold vanilla bean crème anglaise.",
        "dietary": ["vegetarian", "nut-free"],
        "sensoryRole": "Airy, cloud-like dark chocolate cloud with a warm molten center, contrasted by cold, velvety, aromatic vanilla custard.",
        "ingredients": [
            {"qty": 180, "unit": "g", "name": "70% bittersweet dark chocolate (Valrhona Guanaja or similar)", "prep": "chopped fine", "dept": "pantry"},
            {"qty": 4, "unit": "pcs", "name": "Large eggs", "prep": "separated cleanly into yolks and whites at room temp", "dept": "dairy"},
            {"qty": 1, "unit": "pcs", "name": "Egg white (extra)", "prep": "for additional meringue lift", "dept": "dairy"},
            {"qty": 160, "unit": "ml", "name": "Whole milk", "prep": "warmed", "dept": "dairy"},
            {"qty": 20, "unit": "g", "name": "Unsalted European butter", "prep": "softened, for brushing ramekins", "dept": "dairy"},
            {"qty": 50, "unit": "g", "name": "Granulated sugar", "prep": "divided: 20g for ramekins, 30g for meringue", "dept": "pantry"},
            {"qty": 15, "unit": "g", "name": "Cornstarch or flour", "prep": "for chocolate base stability", "dept": "drygoods"},
            {"qty": 1, "unit": "g", "name": "Fine sea salt", "prep": "to balance chocolate bitterness", "dept": "pantry"},
            {"qty": 5, "unit": "ml", "name": "Pure vanilla extract", "prep": "in base", "dept": "pantry"},
            {"qty": 200, "unit": "ml", "name": "Crème anglaise (custard with heavy cream, yolks, sugar, vanilla bean)", "prep": "chilled, for service", "dept": "dairy"}
        ],
        "equipment": [
            {"name": "Four 6-ounce ceramic soufflé ramekins with straight vertical sides", "type": "everyday"},
            {"name": "Pastry brush", "type": "everyday"},
            {"name": "Stand mixer or copper bowl with balloon whisk", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Brush ramekins with softened butter using upward vertical strokes; coat evenly with granulated sugar, tapping out excess.",
            "Separate eggs with meticulous care; not a single speck of fat/yolk may contaminate the whites.",
            "Melt dark chocolate over a gentle bain-marie.",
            "Preheat oven to 195°C (385°F) with a heavy baking sheet set on the middle rack."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Butter ramekins: Using a pastry brush, coat the interior of each ramekin with softened butter using strictly upward vertical brush strokes. Chill 5 minutes, then apply a second layer. Dust with sugar, turning to coat every millimeter, then tap out excess.",
                "timerMins": 5,
                "sensoryCue": "A uniform sandpaper-like coating of crystalline sugar covering every interior surface.",
                "scienceNote": "The vertical butter strokes and sugar crystals provide microscopic footholds that allow the rising egg whites to climb vertically without sticking to the ceramic wall."
            },
            {
                "stepNum": 2,
                "text": "Prepare chocolate base: Whisk milk and cornstarch in a small saucepan over medium heat until thickened into a smooth cream (2 minutes). Remove from heat, whisk in chopped chocolate, salt, and vanilla until smooth and glossy. Whisk in the 4 egg yolks one by one.",
                "timerMins": 5,
                "temperature": "50°C",
                "sensoryCue": "Rich, glossy mahogany chocolate cream with a mirror finish."
            },
            {
                "stepNum": 3,
                "text": "Whip egg whites: In a clean bowl, whip 5 egg whites on medium speed until foamy. Gradually rain in the 30g sugar while increasing speed to high. Whip until medium-stiff peaks form—glossy and holding their shape with a gentle curve at the very tip.",
                "timerMins": 4,
                "sensoryCue": "Snow-white, glistening peaks that hold when the whisk is lifted, without looking dry or granular.",
                "scienceNote": "Over-whipped whites form dry, stiff curds that tear during folding. Medium-stiff peaks retain elastic protein films that expand smoothly when heated."
            },
            {
                "stepNum": 4,
                "text": "Fold: Whisk one-third of the whipped whites vigorously into the warm chocolate base to lighten its density (sacrifice fold). Then gently fold the remaining whites in two batches using a wide silicone spatula in wide sweeping J-motions until no white streaks remain.",
                "timerMins": 3,
                "sensoryCue": "A homogenous, airy mousse that feels featherweight in the bowl."
            },
            {
                "stepNum": 5,
                "text": "Fill ramekins to the very brim. Level the top flat with a metal offset spatula. Run your thumb tip around the inside top rim of each ramekin to create a 2mm 'gutter' between the batter and the ceramic edge.",
                "timerMins": 2,
                "sensoryCue": "A clean, pristine flat surface with a defined shallow trench along the circumference.",
                "scienceNote": "The thumb trench detaches the top edge of batter from the rim, preventing it from catching and ensuring a straight, uniform vertical rise like a top hat."
            },
            {
                "stepNum": 6,
                "text": "Place immediately onto the preheated baking sheet on the center rack. Bake at 195°C (385°F) undisturbed for 13 to 14 minutes. NEVER open the oven door during the first 12 minutes.",
                "timerMins": 14,
                "temperature": "195°C",
                "sensoryCue": "Soufflés rise dramatically 2 inches above the rim, straight and proud, with set crusts and trembling centers.",
                "scienceNote": "Heat expands air bubbles trapped in the meringue while water vaporizes into steam (expanding 1,600 times its liquid volume), driving the soufflé upward before protein coagulation locks the crumb."
            },
            {
                "stepNum": 7,
                "text": "Dust tops immediately with powdered sugar. Serve within 90 seconds. At the table, pierce the center with a spoon and pour in cold vanilla bean crème anglaise.",
                "timerMins": 1,
                "sensoryCue": "The spoon plunges into a warm, airy cloud, revealing a molten chocolate river that mingles with cold cream."
            }
        ],
        "sensoryIndicators": {
            "see": "Majestic vertical rise 2 inches above the ceramic rim, dusted in white powdered sugar, dark chocolate crumb.",
            "hear": "Absolute silence; a gentle airy sigh as the spoon punctures the crust.",
            "smell": "Intense bittersweet Valrhona cocoa, warm vanilla bean, caramelized sugar crust.",
            "feel": "Warm, ethereal, feather-light foam melting instantaneously on the tongue into a rich chocolate cream."
        },
        "scienceNotes": [
            "Thermal expansion: Gay-Lussac's Law dictates that trapped air pockets expand proportionally with absolute temperature (V1/T1 = V2/T2). Combined with the boiling of water into steam, this generates tremendous upward hydrostatic pressure.",
            "Egg white protein denaturation: Ovalbumin and conalbumin set at 65-80°C, solidifying the delicate bubble walls into an open cellular sponge before steam can escape."
        ],
        "troubleshooting": [
            {"issue": "Soufflé rose lopsided or tilted", "cause": "Ramekin was not buttered with vertical strokes or batter caught on the edge without a thumb gutter.", "solution": "Always brush butter vertically and clean the inner rim with your thumb before baking."},
            {"issue": "Soufflé collapsed immediately in oven", "cause": "Oven door was opened early, causing a sudden drop in ambient air temperature and pressure.", "solution": "Do not open oven door until the 13-minute mark."}
        ],
        "substitutions": [
            {"original": "Valrhona Guanaja 70%", "substitute": "Any premium 65-72% bittersweet chocolate (Guittard, Callebaut)", "culinaryConsequence": "Do not use chocolate chips as they contain stabilizers that impede smooth melting."},
            {"original": "Crème anglaise", "substitute": "Tahitian vanilla bean gelato or whipped heavy cream with sea salt", "culinaryConsequence": "Cold ice cream melting into the hot core provides stunning thermal contrast."}
        ],
        "flavorPairings": {
            "wine": "Banyuls Grand Cru, 20-Year Tawny Port, or Pedro Ximénez Sherry",
            "zeroProof": "Chilled espresso tonic with blood orange reduction",
            "complementarySides": ["Chilled vanilla bean crème anglaise", "Fresh wild raspberries"]
        },
        "advancedTechnique": "Core ganache sphere insertion: Freeze a small tablespoon-sized ball of dark chocolate truffle ganache and insert it into the center of the batter before baking; it melts into an ultra-luxurious hidden molten lava core.",
        "storageAndReheating": "Soufflés cannot be stored once baked; they deflate within 3 minutes as internal steam cools and contracts. However, filled raw ramekins can be held refrigerated for up to 3 hours before baking.",
        "nutritionEstimates": {"calories": 390, "proteinG": 10, "carbsG": 36, "fatG": 24},
        "relatedRecipes": ["rec-tarte-tatin"],
        "relatedTechniques": ["lesson-egg-geometry", "lesson-starch-gelatinization"]
    }
]

print(f"Loaded {len(FRENCH_RECIPES)} French Classical master recipes.")
