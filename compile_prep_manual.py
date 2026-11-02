"""
Comprehensive compilation of 25+ professional restaurant prep specs, knife cuts,
sauces, pastry creams, lineset standards, and HACCP protocols from the 12 kitchen manuals.
"""
import json

prep_items = [
    # SAUCES & EMULSIONS
    {
        "id": "prep-hollandaise",
        "title": "Classical Emulsified Hollandaise (Vitamix & Handheld Methods)",
        "category": "Sauces & Emulsions",
        "station": "Panfry / Sauté Station",
        "shelfLife": "2 hours at 120°F (discard after 2 hours)",
        "prepFrequency": "Every 2 hours during service",
        "haccp": "Critical Control Point: Hold in dedicated thermos or gentle steam bath at exactly 120°F (49°C). Never exceed 2 hours hold time. Discard remaining product to prevent Bacillus cereus and Salmonella growth in the warm danger zone.",
        "yields": {
            "1 Quart": [
                {"name": "Egg Yolks", "qty": "9 oz", "notes": "Liquid yolks"},
                {"name": "White Wine Vinegar", "qty": "2 fl oz + 1 T"},
                {"name": "Fresh Squeezed Lemon Juice", "qty": "1 T"},
                {"name": "Dijon Mustard", "qty": "2 t", "notes": "Acts as emulsion stabilizer"},
                {"name": "Cayenne Pepper", "qty": "1/8 t"},
                {"name": "Melted Warm Butter", "qty": "1 lb 6 oz", "notes": "Warm throughout, not boiling"}
            ],
            "1 Gallon": [
                {"name": "Egg Yolks", "qty": "2 lb 4 oz"},
                {"name": "White Wine Vinegar", "qty": "10 fl oz"},
                {"name": "Fresh Squeezed Lemon Juice", "qty": "2 fl oz"},
                {"name": "Dijon Mustard", "qty": "1 fl oz + 2 t"},
                {"name": "Cayenne Pepper", "qty": "1/2 t"},
                {"name": "Melted Warm Butter", "qty": "5 lb 8 oz"}
            ]
        },
        "steps": [
            "Place egg yolks in a dry Vitamix blender. Gradually turn to high speed and blend until yolks turn pale yellow and reach ribbon stage (double fluid volume, approximately 2 minutes).",
            "While running on high speed, stream in vinegar, lemon juice, Dijon mustard, and cayenne until incorporated.",
            "Quickly stream in warm melted butter over 6 seconds until fully emulsified into a thick, glossy sabayon.",
            "Handheld Method: Whisk yolks and vinegar over a double boiler until pale and ribbon stage; remove from heat repeatedly to prevent curdling. Stream in warm clarified butter using immersion blender; finish with lemon, Dijon, and cayenne.",
            "Transfer immediately to a preheated thermos at 120°F. If sauce thickens during service, reconstitute with 1-2 tsp hot water."
        ],
        "scienceNote": "Dijon mustard contributes sinigrin and plant mucilage, which provide steric stabilization alongside lecithin in the egg yolks. Holding at 120°F keeps butterfat in liquid crystalline phase without coagulating yolk vitellin proteins (coagulation begins at 144°F/62°C)."
    },
    {
        "id": "prep-calabrian-chili-dressing",
        "title": "Calabrian Chili Caesar Dressing",
        "category": "Sauces & Emulsions",
        "station": "Pantry / Salad Station",
        "shelfLife": "5 days refrigerated",
        "prepFrequency": "2x / week",
        "haccp": "Keep refrigerated at <40°F. Wash produce before peeling.",
        "yields": {
            "1 Quart": [
                {"name": "Egg Yolks", "qty": "4 oz"},
                {"name": "Fresh Lemon Juice", "qty": "4 oz"},
                {"name": "White Wine Vinegar", "qty": "2 oz"},
                {"name": "Sour Cream", "qty": "1.25 oz"},
                {"name": "Parmesan (1/2\" diced, rind off)", "qty": "1.25 oz"},
                {"name": "Shallots (rough chopped)", "qty": "1.25 oz"},
                {"name": "Calabrian Chili Paste", "qty": "0.75 oz"},
                {"name": "Anchovies (drained)", "qty": "0.75 oz"},
                {"name": "Garlic Cloves", "qty": "0.75 oz"},
                {"name": "Worcestershire Sauce", "qty": "0.75 oz"},
                {"name": "Dijon Mustard", "qty": "0.75 oz"},
                {"name": "Fine Salt", "qty": "1 T + 1 t"},
                {"name": "Black Pepper", "qty": "1.5 t"},
                {"name": "Vegetable Oil", "qty": "14.5 oz"}
            ]
        },
        "steps": [
            "Combine all Part A aromatics, acids, dairy, and seasonings in a Vitamix blender.",
            "Blend on high speed until completely smooth with no visible shallot or parmesan chunks.",
            "With blender still running on high speed, slowly drizzle vegetable oil in a continuous pencil-thin stream until a rich, glossy mayonnaise-like emulsion forms.",
            "Transfer into stainless insert, label, date, and refrigerate."
        ],
        "scienceNote": "The combination of citric acid, acetic acid, Worcestershire anchovy paste, and aged Parmigiano-Reggiano glutamates creates intense umami synergy with capsaicinoids from fermented Calabrian chilies."
    },
    {
        "id": "prep-green-chermoula",
        "title": "Green Herb Chermoula",
        "category": "Sauces & Emulsions",
        "station": "Pantry / Garde Manger",
        "shelfLife": "2 days refrigerated",
        "prepFrequency": "4x / week",
        "haccp": "Cool on ice bath immediately after blending to prevent chlorophyll oxidation and browning.",
        "yields": {
            "1 Quart": [
                {"name": "Vegetable Oil", "qty": "1 lb 3 oz"},
                {"name": "Fresh Lemon Juice", "qty": "5.5 oz"},
                {"name": "Flat Leaf Parsley (stems removed)", "qty": "3.5 oz"},
                {"name": "Cilantro (rough chopped)", "qty": "3.5 oz"},
                {"name": "Grated Parmesan", "qty": "2 fl oz"},
                {"name": "Jalapeño (seeded, ribs removed)", "qty": "0.75 oz"},
                {"name": "Garlic Cloves", "qty": "0.75 oz"},
                {"name": "Harissa Powder", "qty": "1 fl oz"},
                {"name": "Fine Salt", "qty": "2 t"}
            ]
        },
        "steps": [
            "Prepare an ice bath with one stainless mixing bowl nestled inside another filled with ice water.",
            "Combine all ingredients in a Vitamix blender and blend on high speed until completely smooth (max 1 quart per blender batch).",
            "Immediately transfer into the chilled bowl on the ice bath. Stir continuously with a rubber spatula to pull thermal energy out of the sauce within 3 minutes.",
            "Seal with plastic wrap touching the surface, lid, label, and refrigerate."
        ],
        "scienceNote": "Blender friction rapidly heats herb chlorophyll. If temperature exceeds 122°F (50°C), chlorophyllase enzymes and magnesium displacement convert vibrant green chlorophyll a/b into dull olive-brown pheophytin. Rapid ice-bath shock stops this transformation dead."
    },
    {
        "id": "prep-peppercorn-sauce",
        "title": "Classical Sauce au Poivre (Green Peppercorn with Flambéed Brandy)",
        "category": "Sauces & Emulsions",
        "station": "Panfry / Sauté Station",
        "shelfLife": "5 days refrigerated (refrigerate 24 hours before first service)",
        "prepFrequency": "2x / week",
        "haccp": "Never boil after mounting with butter (monté au beurre) or the emulsion will break.",
        "yields": {
            "1 Quart": [
                {"name": "Shallot (1/8\" sliced rings)", "qty": "1 oz"},
                {"name": "Minced Garlic", "qty": "0.5 oz"},
                {"name": "Brandy / Cognac", "qty": "2 fl oz"},
                {"name": "Fresh Thyme Sprigs (with stems)", "qty": "0.1 oz"},
                {"name": "Green Peppercorns with Brine", "qty": "2 fl oz"},
                {"name": "Coarse Black Pepper", "qty": "1 T"},
                {"name": "Veal Demi-Glace", "qty": "1 L"},
                {"name": "Cornstarch + Cold Water Slurry", "qty": "1 T each"},
                {"name": "Heavy Whipping Cream", "qty": "2 fl oz"},
                {"name": "Cold Butter (1\" cubes)", "qty": "1 oz"}
            ]
        },
        "steps": [
            "Sweat shallots and minced garlic in minimal oil over open medium flame until translucent with zero browning.",
            "Remove from heat, add brandy, return to open flame and tilt pan to flambé. Burn off raw ethanol for 5-8 seconds to caramelize esters.",
            "Add thyme stems, green peppercorns with brine, and cracked black pepper; cook 2 minutes.",
            "Pour in demi-glace. Simmer and reduce from 1 L down to exactly 28 fl oz (verify with measuring pitcher).",
            "Fish out thyme stems. Whisk in cornstarch slurry and bring to a high simmer to activate starch granules. Do not boil.",
            "Turn heat to lowest setting. Slowly whisk in cream, then mount with cold butter cubes one at a time (monter au beurre) until glossy and velvety.",
            "Chill and age in cooler 24 hours to allow pepper piperine to marry with gelatin matrix."
        ],
        "scienceNote": "Flambéeing brandy reaches vapor temperatures over 300°F (150°C), triggering flash pyrolysis that degrades harsh fusel alcohols and produces fragrant ethyl esters. Finishing with cold butter below 140°F suspends butterfat droplets in the demi-glace gelatin matrix."
    },
    {
        "id": "prep-truffle-butter",
        "title": "House Black Truffle Butter & Finishing Glaze",
        "category": "Compound Butters & Fats",
        "station": "Butchery / Prep Station",
        "shelfLife": "5 days refrigerated / 1 month frozen in 1-quart portions",
        "prepFrequency": "1x / week",
        "haccp": "Thaw frozen truffle paste portion cups in refrigerator. Do not warm on stove.",
        "yields": {
            "1 Quart": [
                {"name": "Butter (room temperature)", "qty": "1 lb 3.5 oz"},
                {"name": "Black Truffle Paste", "qty": "1.5 oz"},
                {"name": "White Truffle Oil", "qty": "1 T + 1/2 t"},
                {"name": "Fine Salt", "qty": "1.75 t"},
                {"name": "Coarse Black Pepper", "qty": "1.75 t"}
            ]
        },
        "steps": [
            "Place room-temperature butter into stand mixer bowl fitted with paddle attachment.",
            "Whip on medium speed until doubled in volume, airy, and pale cream in color (approx. 5-7 minutes).",
            "Add black truffle paste, white truffle oil, salt, and black pepper. Mix on low speed until evenly streaked and incorporated.",
            "Scrape down sides of bowl and whip for 1 additional minute.",
            "Portion into 1-quart deli cups or roll into parchment logs; refrigerate or freeze."
        ],
        "scienceNote": "Aerating butter incorporates tiny air pockets that increase surface contact on the palate. Lipid molecules dissolve and trap 2,4-dithiapentane (the key truffle aroma molecule), delaying volatilization until the butter melts on a hot steak."
    },
    {
        "id": "prep-confit-garlic",
        "title": "Slow-Simmered Confit Garlic & Golden Garlic Oil",
        "category": "Compound Butters & Fats",
        "station": "Prep Station / Sauté",
        "shelfLife": "Confit Garlic: 10 days / Reserved Garlic Oil: 1 month",
        "prepFrequency": "1x / week",
        "haccp": "Refrigerate immediately after cooling. Never store confit garlic or garlic oil at room temperature due to Clostridium botulinum anaerobic spores on root alliums.",
        "yields": {
            "1 Quart": [
                {"name": "Peeled Garlic Cloves", "qty": "3 lb"},
                {"name": "Neutral Vegetable Oil", "qty": "1 lb 8 oz"}
            ]
        },
        "steps": [
            "Place whole peeled garlic cloves and vegetable oil into a heavy saucepot over medium-low heat.",
            "Bring to a gentle simmer with lazy bubbles breaking gently (around 200°F-210°F).",
            "Simmer gently for 1 hour, stirring occasionally, until cloves turn deep golden amber and are soft as butter.",
            "Drain cloves, reserving the golden garlic oil for vinaigrettes, finishing oils, or pan frying.",
            "Purée the softened cloves in a food processor until completely smooth. Label, date, and refrigerate."
        ],
        "scienceNote": "Low-temperature thermal breakdown converts harsh pungent allicin into sweet, nutty allyl sulfides and complex oligosaccharides without scorched bitterness."
    },
    {
        "id": "prep-dashi-mayo",
        "title": "Dashi Emulsion Mayonnaise",
        "category": "Sauces & Emulsions",
        "station": "Garde Manger / Sushi Bar",
        "shelfLife": "5 days refrigerated",
        "prepFrequency": "2x / week",
        "haccp": "Keep chilled at <38°F. Never overmix during ribbon stage.",
        "yields": {
            "1 Quart": [
                {"name": "Liquid Egg Yolks", "qty": "7 oz"},
                {"name": "Dijon Mustard", "qty": "1 oz"},
                {"name": "Vegetable Oil", "qty": "1 lb 2 oz"},
                {"name": "Sugar", "qty": "0.7 oz"},
                {"name": "Fine Salt", "qty": "0.6 oz"},
                {"name": "Hon Dashi Powder", "qty": "0.5 oz"},
                {"name": "Fresh Lemon Juice", "qty": "1 oz"},
                {"name": "Rice Vinegar", "qty": "1 oz"}
            ]
        },
        "steps": [
            "Whip egg yolks and Dijon mustard in stand mixer with balloon whisk on high speed until ribbon stage is reached and volume increases by 50% (approx. 2 minutes).",
            "Lower speed to medium. Drizzle in half of the vegetable oil in a steady thread to initiate the emulsion.",
            "When half the oil is emulsified, add sugar, fine salt, and dashi powder.",
            "Slowly stream in remaining vegetable oil until dense and creamy.",
            "Stream in lemon juice and rice vinegar; mix for exactly 15 seconds until homogenous. Do not overmix."
        ],
        "scienceNote": "Dashi powder contains concentrated disodium inosinate and sodium glutamate. When suspended in an oil-in-water yolk emulsion, the glutamate ions bind umami receptors on the tongue, creating persistent savory depth."
    },
    {
        "id": "prep-citrus-soy",
        "title": "Citrus Soy & Sambal Oelek Vinaigrette",
        "category": "Sauces & Emulsions",
        "station": "Garde Manger / Wok Station",
        "shelfLife": "9 days refrigerated (let stand 4 hours before first use)",
        "prepFrequency": "1x / week",
        "haccp": "Store in clean squeeze bottles with fitted caps. Do not leave at room temperature.",
        "yields": {
            "1 Quart": [
                {"name": "White Vinegar", "qty": "2.25 oz"},
                {"name": "Fresh Ginger (peeled, rough chop)", "qty": "2.25 oz"},
                {"name": "Sambal Oelek Chili Paste", "qty": "1.75 oz"},
                {"name": "Soy Sauce", "qty": "7.5 oz"},
                {"name": "Water", "qty": "4.5 oz"},
                {"name": "Fresh Lime Juice", "qty": "4 oz"},
                {"name": "Toasted Sesame Oil", "qty": "4 oz"},
                {"name": "Pure Maple Syrup", "qty": "2.75 oz"},
                {"name": "Dijon Mustard", "qty": "2.25 oz"}
            ]
        },
        "steps": [
            "Part A: Combine white vinegar, roughly chopped ginger, and sambal oelek in a Vitamix blender. Blend on medium speed until smooth and no visible ginger fibers remain.",
            "Part B: Whisk together soy sauce, water, lime juice, toasted sesame oil, maple syrup, and Dijon mustard.",
            "Combine blended ginger puree with Part B using an immersion hand blender until homogenous.",
            "Transfer to airtight Cambro, label, and refrigerate. Must age for at least 4 hours before service to allow ginger heat to mellow into citrus sugars."
        ],
        "scienceNote": "The natural protease gingerol in fresh ginger softens sharp soy tannins, while Dijon mustard's sinigrin and maple syrup polysaccharides create a stable semi-permanent emulsion with the toasted sesame oil."
    },
    {
        "id": "prep-shiro-miso-marinade",
        "title": "Shiro Miso & White Vermouth Marinade (Nobu Style)",
        "category": "Sauces & Emulsions",
        "station": "Line Prep / Sauté",
        "shelfLife": "9 days refrigerated",
        "prepFrequency": "1x / week",
        "haccp": "Cool completely before coating raw fish to prevent par-cooking the protein.",
        "yields": {
            "1 Quart": [
                {"name": "White Vermouth (Martini Bianco)", "qty": "9 oz"},
                {"name": "White Miso Paste (Shiro Miso)", "qty": "1 lb 10 oz"},
                {"name": "Granulated Sugar", "qty": "1 lb"},
                {"name": "Rice Vinegar", "qty": "1 oz"}
            ]
        },
        "steps": [
            "Combine white vermouth, white miso paste, sugar, and rice vinegar in a heavy stainless saucepot.",
            "Bring the mixture to a gentle rolling boil over medium heat while whisking constantly to prevent the dense miso sugars from scorching on the bottom.",
            "Once dissolved and simmering smoothly, immediately remove from heat.",
            "Transfer to hotel pan or Cambro and cool completely to 38°F before marinating sea bass, salmon, or tofu."
        ],
        "scienceNote": "Boiling vermouth cooks out the raw ethanol while activating the koji enzymes and dissolving sucrose. When applied to fish, the high sugar and glutamate content forms a lacquer that caramelizes into a deep mahogany glaze under the salamander."
    },

    # PASTRY & DESSERT FOUNDATIONS
    {
        "id": "prep-vanilla-creme-anglaise",
        "title": "Vanilla Crème Anglaise (Combi Steam & Sous-Vide Circulator Methods)",
        "category": "Pastry & Baking Foundations",
        "station": "Pastry / Line Dessert",
        "shelfLife": "5 days refrigerated",
        "prepFrequency": "2x / week",
        "haccp": "Cook to exactly 180°F (82°C) to pasteurize eggs without coagulation. Shock in ice water bath immediately.",
        "yields": {
            "1 Quart": [
                {"name": "Whole Milk (3.25%)", "qty": "11 oz"},
                {"name": "Heavy Whipping Cream", "qty": "11 oz"},
                {"name": "Granulated Sugar", "qty": "7 oz"},
                {"name": "Liquid Egg Yolks", "qty": "5 oz"},
                {"name": "Pure Vanilla Bean Extract", "qty": "1.5 t"}
            ]
        },
        "steps": [
            "Whisk milk, cream, sugar, egg yolks, and vanilla in a stainless bowl until sugar dissolves.",
            "Combi Steam Method: Transfer into double-sealed heavy-duty freezer Ziploc bags (max 1 quart per bag), expelling all air. Lay flat on perforated trays; steam at 180°F (82°C), 100% steam, fan speed 4 for 25 minutes.",
            "Sous-Vide Immersion Method: Cook sealed bags submerged in water bath at 180°F for 45 minutes.",
            "Immediately remove bags and strain through a fine mesh conical chinois into an ice water bath. Stir occasionally until chilled to 38°F.",
            "Bottle, label, and refrigerate."
        ],
        "scienceNote": "Cooking inside sealed bags in a combi or water bath at precisely 180°F prevents the localized pan hot-spots that curdle egg yolks on a stovetop, guaranteeing a silky, uniform custard with zero curdling risk."
    },
    {
        "id": "prep-coconut-pastry-cream",
        "title": "Silky Coconut Pastry Cream (Crème Pâtissière à la Noix de Coco)",
        "category": "Pastry & Baking Foundations",
        "station": "Pastry Station",
        "shelfLife": "3 days refrigerated",
        "prepFrequency": "3x / week",
        "haccp": "Must reach 180°F-190°F to gelatinize cornstarch and deactivate alpha-amylase in egg yolks. Cover with plastic wrap touching surface to prevent skin.",
        "yields": {
            "15 Pies Batch": [
                {"name": "Sugar", "qty": "11 oz"},
                {"name": "Cornstarch", "qty": "2.5 oz"},
                {"name": "Fine Salt", "qty": "1 t"},
                {"name": "Egg Yolks", "qty": "3 oz"},
                {"name": "Liquid Egg Whites", "qty": "2.2 oz"},
                {"name": "Whole Milk", "qty": "2 lb 13 oz"},
                {"name": "Vanilla Extract", "qty": "1 t"},
                {"name": "Medium Shredded Coconut", "qty": "8 oz"},
                {"name": "Cold Butter (1\" diced)", "qty": "4.5 oz"}
            ]
        },
        "steps": [
            "Part A: Combine sugar, cornstarch, salt, yolks, and whites in stand mixer. Whisk on medium-high for 2 minutes until light yellow, aerated, and ribbon stage.",
            "Part B: Heat whole milk and vanilla in pot to 180°F, then remove from heat.",
            "Temper: Slowly ladle 4 fl oz hot milk into egg mixture while whisking vigorously. Add another 4 fl oz. Then pour tempered egg mixture back into pot with remaining milk.",
            "Cook over medium-low heat. Add shredded coconut and cold butter cubes. Whisk constantly until butter melts, cornstarch gelatinizes, and custard thickens to 180°F-190°F (approx. 4 minutes).",
            "Pour into 2\" metal inserts. Immediately press plastic wrap directly against the hot custard surface to eliminate air and stop skin formation. Chill to <40°F before filling pie shells."
        ],
        "scienceNote": "Cornstarch requires 180°F-190°F (82°C-88°C) to fully hydrate and swell amylose chains. Additionally, egg yolks contain heat-resistant salivary-type amylase enzymes that will digest and liquefy starch custard over 24 hours if not denatured by boiling temperatures."
    },
    {
        "id": "prep-stabilized-chantilly",
        "title": "Stabilized Vanilla Chantilly Cream & Golden Rules",
        "category": "Pastry & Baking Foundations",
        "station": "Pastry / Line Dessert",
        "shelfLife": "2 days refrigerated",
        "prepFrequency": "Daily",
        "haccp": "Keep whipped cream refrigerated below 38°F at all times. Never whip warm cream.",
        "yields": {
            "1 Quart Whipped": [
                {"name": "Heavy Whipping Cream (36% fat, ice cold)", "qty": "1 Quart"},
                {"name": "Powdered Sugar (contains cornstarch)", "qty": "3 oz"},
                {"name": "Pure Vanilla Bean Paste", "qty": "1 T"}
            ]
        },
        "steps": [
            "Chill the stainless mixer bowl and wire whip attachment in the freezer for 15 minutes before whipping.",
            "Pour ice-cold cream, sifted powdered sugar, and vanilla paste into chilled bowl.",
            "Start on low speed for 30 seconds to dissolve sugar without splashing. Increase to medium speed.",
            "Whip to soft peaks, then reduce speed to low to tighten the bubble structure into velvety medium-firm peaks.",
            "GOLDEN RULE: Never whip on high speed throughout—high speed creates large, fragile air pockets that weep liquid (syneresis). Medium speed builds a dense, stable lipid network that holds for 48 hours without collapsing."
        ],
        "scienceNote": "Chilling keeps butterfat globules solid. As fat crystals collide, they partially rupture and form a continuous crystalline network that traps air cells and liquid water. Powdered sugar contains 3% cornstarch, which absorbs weeping moisture and provides structural stability."
    },

    # PROTEIN & SEAFOOD SPECS
    {
        "id": "prep-citrus-ahi-tuna",
        "title": "Flash-Blanched Citrus Ahi Tuna (Saku Block Technique)",
        "category": "Protein & Seafood Specs",
        "station": "Garde Manger / Sushi Bar",
        "shelfLife": "3 days refrigerated",
        "prepFrequency": "3x / week",
        "haccp": "Puncture vacuum bags immediately upon pulling from freezer to allow aerobic respiration and eliminate Clostridium botulinum toxin formation.",
        "yields": {
            "3 Portions": [
                {"name": "Frozen Ahi Tuna Saku Block", "qty": "2 blocks (approx. 4 oz each)"},
                {"name": "Fine Sea Salt", "qty": "Medium seasoning"},
                {"name": "Yuzu Citrus Broth", "qty": "2 t"}
            ]
        },
        "steps": [
            "Prepare an ice bath in a clean stainless bowl.",
            "Lower tuna blocks in a wire sifting basket into rapidly boiling water for exactly 20 seconds. Do not overcrowd.",
            "Remove instantly and plunge into the ice water for 1 minute to arrest cooking immediately.",
            "Pat dry with clean lint-free paper towels. Season all sides evenly with fine sea salt and yuzu broth.",
            "Wrap tightly in plastic film and place in freezer for 20 minutes to firm up for precision slicing.",
            "Slice across the grain in uniform 1/4\" slices (approx. 7-8 slices per 2.2 oz portion). Wrap neatly and refrigerate."
        ],
        "scienceNote": "The 20-second boiling dip denatures superficial sarcoplasmic proteins on the exterior 1mm, setting the muscle fibers and neutralizing surface microbes, while preserving the raw, translucent myoglobin-rich core."
    },
    {
        "id": "prep-lobster-tail",
        "title": "Lobster Tail Splitting & Shell-Perched Presentation",
        "category": "Protein & Seafood Specs",
        "station": "Butchery / Seafood Prep",
        "shelfLife": "2 days refrigerated",
        "prepFrequency": "Daily",
        "haccp": "Thaw frozen lobster tails on perforated sheet pans stacked over solid pans to catch drip for minimum 8 hours.",
        "yields": {
            "1 Portion": [
                {"name": "Cold Water Lobster Tail", "qty": "1 each"}
            ]
        },
        "steps": [
            "Place thawed lobster tail on its side on a clean cutting board. Press firmly down with palm until the carapace audibly cracks.",
            "Reposition flat with shell facing up. Using heavy kitchen shears, cut straight through the center of the dorsal shell, stopping right before the tail fan.",
            "Insert two fingers under the meat and gently separate the lobster flesh from the inner shell membrane.",
            "Pull the lobster meat upward through the split shell so it sits perched proudly on top of the shell, keeping the base anchored in the fin.",
            "Remove the intestinal vein along the spine and rinse with cold water. Trim any frayed stringy bits for clean edges.",
            "Steam in Combi at 212°F / 100% steam for 8 minutes until internal temp reaches 140°F (60°C). Chill immediately."
        ],
        "scienceNote": "Perching the meat above the shell exposes maximum surface area to heat and butter basting, while the underlying shell acts as a heat shield and presentation vessel."
    },
    {
        "id": "prep-bacon-lardons",
        "title": "Double-Smoked Slab Bacon Lardons",
        "category": "Protein & Seafood Specs",
        "station": "Butchery / Sauté",
        "shelfLife": "3 days refrigerated",
        "prepFrequency": "3x / week",
        "haccp": "Bake on perforated trays over drip trays to drain rendered fat. Render at 325°F.",
        "yields": {
            "15 oz Cooked Yield": [
                {"name": "Double Smoked Slab Bacon", "qty": "2 lb raw"}
            ]
        },
        "steps": [
            "Cut slab bacon in half along length. Slice on meat slicer to 1/2\" thick slabs (1/2\" x 10\").",
            "Stack slices 2-4 high and cut across into 1/2\" batons (final raw dimensions: 1/2\" x 1/2\" x 1.5\").",
            "Arrange evenly spaced in a single layer on a perforated bake tray with a solid drip tray underneath to catch rendered liquid fat (max 2 lb per tray).",
            "Bake in combi/convection oven at 325°F (163°C) with low fan for 30 minutes until fat has rendered, edges are caramelized, and lardons are tender with a crisp exterior.",
            "Cool completely in refrigerator; portion into deli containers."
        ],
        "scienceNote": "Gentle 325°F rendering melts crystalline triacylglycerols while slowly caramelizing connective collagen into tender gelatin without charring the meat sugars."
    },
    {
        "id": "prep-chicken-flapping",
        "title": "Chicken Breast Flapping & Tendon Release Technique",
        "category": "Protein & Seafood Specs",
        "station": "Butchery / Poultry Station",
        "shelfLife": "3 days refrigerated",
        "prepFrequency": "Daily",
        "haccp": "Process on dedicated yellow poultry board. Wash and sanitize hands and tools immediately after.",
        "yields": {
            "Per Breast": [
                {"name": "Boneless Skinless Chicken Half Breast", "qty": "1 each"}
            ]
        },
        "steps": [
            "Grade breasts: reserve the thickest lobes for Entrée Cajun Grilling; thinner ones for salad chicken.",
            "Peel skin from thin point to thick lobe if skin is still attached.",
            "Position half breast with tip pointing away from you on the yellow cutting board.",
            "Hook the tip of your index finger through the tendon that anchors the large heart-shaped lobe folded over.",
            "Pull firmly towards yourself through the tendon without tearing downward through the meat.",
            "Smooth out the breast from the keel bone line outward by pressing with the palms of both hands. This opens the breast 3/4\" wider and creates uniform thickness.",
            "Layer onto bake trays separated by parchment (maximum 3 layers high)."
        ],
        "scienceNote": "Chicken breast is naturally tapered (thick at cranial end, paper-thin at caudal end). Flapping creates an even cross-sectional plane, ensuring the thin tip does not dry out while waiting for the thick core to reach 165°F (74°C)."
    },
    {
        "id": "prep-salmon-aburi",
        "title": "Salmon Aburi Press & Tartare Grading",
        "category": "Protein & Seafood Specs",
        "station": "Sushi Bar / Garde Manger",
        "shelfLife": "36 hours refrigerated",
        "prepFrequency": "Daily",
        "haccp": "Sashimi-grade Norwegian Atlantic Salmon must be deep-frozen below -35°C (-31°F) for minimum 15 hours to guarantee parasite destruction. Never substitute with store fresh fish.",
        "yields": {
            "10 Portions Aburi": [
                {"name": "Sashimi Grade Norwegian Salmon Filet", "qty": "2 lb"}
            ]
        },
        "steps": [
            "Inspect and run fingertips over presentation side of filet to detect any pin bones; remove with bone tweezers.",
            "Grade filet: reserve wide center cuts for dinner entrée; narrow belly and tail (2\"-2.5\" width) for Aburi and Tartare.",
            "Cut 24\" x 16\" parchment sheets into 16 rectangles (8\" x 3\" each).",
            "Place partially thawed salmon on board with thin belly facing left. Slice across on a slight 30° bias at 1/8\" thickness.",
            "Overlap slices onto parchment rectangles to create an even 2\" x 8\" sheet weighing exactly 2.0 oz.",
            "Stack portions up to 10 high separated by parchment, wrap in plastic, and chill for line service."
        ],
        "scienceNote": "Partial thawing (semi-frozen crusting) firms lipid matrices, allowing knife blades to make pristine paper-thin 1/8\" cuts without dragging or crushing delicate salmon myotome flakes."
    },
    {
        "id": "prep-squid-pineapple-scoring",
        "title": "Squid Pineapple Scoring & Buttermilk Marinating",
        "category": "Protein & Seafood Specs",
        "station": "Seafood / Fryer Station",
        "shelfLife": "2 days refrigerated",
        "prepFrequency": "4x / week",
        "haccp": "Thaw frozen squid in perforated inserts nested in solid inserts for minimum 8 hours.",
        "yields": {
            "10 Portions (7 oz squid + 1 fl oz batter)": [
                {"name": "Pineapple-Cut Squid Tubes", "qty": "4 lb 6 oz"},
                {"name": "Buttermilk", "qty": "6 oz"},
                {"name": "Cold Water", "qty": "4 oz"},
                {"name": "Cornstarch", "qty": "1.5 oz"},
                {"name": "Minced Garlic & Ginger", "qty": "1.5 oz each"},
                {"name": "Guar Gum", "qty": "1 t"},
                {"name": "Baking Powder", "qty": "1/2 t"},
                {"name": "Salt", "qty": "1/2 t"}
            ]
        },
        "steps": [
            "Thaw squid tubes and drain well. Lay tubes flat on blue seafood cutting board.",
            "Score the interior surface at 1/8\" intervals diagonally in both directions to create a 45° diamond grid (pineapple cut).",
            "Cut scored squid into 2\"-3\" length x 3/8\"-1/2\" width strips. Portion 7.0 oz into portion cups.",
            "Whisk buttermilk, water, cornstarch, garlic, ginger, guar gum, baking powder, and salt until smooth and starch dissolves.",
            "Add 1 fl oz marinade to each portion cup; seal and shake to coat. Marinate minimum 3 hours before dredging."
        ],
        "scienceNote": "Scoring cuts the dense collagen fibril network, allowing rapid heat penetration and curling the squid into tender 'pinecone' tubes in 45 seconds of frying instead of becoming rubbery."
    },
    {
        "id": "prep-pork-chop-brine",
        "title": "Bone-In Pork Chop 24-Hour Brining Protocol",
        "category": "Protein & Seafood Specs",
        "station": "Butchery / Grill Station",
        "shelfLife": "3 days refrigerated after brining",
        "prepFrequency": "3x / week",
        "haccp": "CRITICAL: Do not leave pork chops in brine for more than 24 hours. Exceeding 24 hours causes over-salted, mushy pork from muscle fiber breakdown.",
        "yields": {
            "8 Portions": [
                {"name": "Cold Water", "qty": "4 lb"},
                {"name": "Fine Sea Salt", "qty": "4 oz (approx. 6% salinity)"},
                {"name": "Bone-In Center Cut Pork Chops", "qty": "8 each"}
            ]
        },
        "steps": [
            "Whisk cold water and salt in a Cambro until salt is 100% dissolved.",
            "Submerge bone-in pork chops completely in the salt brine. Chops must not peek above water line or discoloration occurs.",
            "Lid, label, and refrigerate for exactly 24 hours.",
            "After 24 hours, pull chops from brine, blot bone-dry with paper towels, grade by thickness, and wrap tightly for line service."
        ],
        "scienceNote": "A 6% brine draws water and salt into the muscle through osmotic diffusion. Salt solubilizes myosin filaments, relaxing the protein grid so it retains 15% more juice during grilling and oven finishing."
    },

    # LINESET & OPERATIONAL STANDARDS
    {
        "id": "prep-crispy-potato-garnish",
        "title": "Crispy Spiralized Potato Garnish & Starch Stripping",
        "category": "Lineset & Operational Standards",
        "station": "Fryer / Line Garnish",
        "shelfLife": "36 hours at room temperature in sealed container with silica gel pack",
        "prepFrequency": "Daily",
        "haccp": "Test daily for crispness. Stored airtight with food-safe silica gel packs.",
        "yields": {
            "16 Portions (8 oz)": [
                {"name": "Russet Potatoes (peeled)", "qty": "1 lb 6 oz"},
                {"name": "Cold Running Water", "qty": "As needed"},
                {"name": "Fine Sea Salt", "qty": "Medium seasoning"}
            ]
        },
        "steps": [
            "Peel Russet potatoes. Cut in half across the axis to fit into turning spiralizer.",
            "Spiralize using the 1/16\" thickness blade, applying steady thumb pressure to create unbroken delicate curls.",
            "Submerge spiralized strands in a large container of cold running water. Agitate vigorously, draining and replenishing water for approx. 6 minutes until the water runs 100% crystal clear.",
            "CRITICAL NOTE: Removing all surface starch is mandatory. Excess starch caramelizes prematurely, causing scorched brown bitter potatoes before moisture can escape.",
            "Drain potatoes thoroughly. Spread across paper towel-lined baking sheets and blot firmly with dry towels until bone dry.",
            "Drop into 350°F (177°C) fryer for 30 seconds, flip entire cluster with tongs, and fry 30 seconds more until golden and crisp. Maximum batch: 8 oz raw potato per fryer vat.",
            "Drain immediately onto paper towels, season hot with fine salt, and divide gently into 0.5 oz lofty 2\" high clusters. Store with silica pack."
        ],
        "scienceNote": "Rinsing removes amylose granules ruptured by slicing. When blotted dry and submerged in 350°F oil, water boils off violently without steam-cushioning, producing an ultra-thin, glassy, crunchy starch-fat matrix."
    },
    {
        "id": "prep-pasta-cooking-protocol",
        "title": "Commercial Dried Pasta Precooking & Oil Glazing",
        "category": "Lineset & Operational Standards",
        "station": "Pasta / Panfry Station",
        "shelfLife": "36 hours refrigerated",
        "prepFrequency": "Daily",
        "haccp": "Cool on baking sheets in single layers for 15 minutes. Bag tightly within 30 minutes to prevent surface dehydration.",
        "yields": {
            "Cooking Ratios": [
                {"name": "Water", "qty": "6 Gallons in 44 qt pot"},
                {"name": "Coarse Kosher Salt", "qty": "9 fl oz (1.5 fl oz per gallon water)"},
                {"name": "Max Pasta Batch", "qty": "5 lb dry pasta (yields 10 lb cooked)"},
                {"name": "Finishing Vegetable Oil", "qty": "5 fl oz per 5 lb cooked pasta (1 fl oz / lb)"}
            ]
        },
        "steps": [
            "Bring 6 gallons of water with 9 fl oz coarse salt to a violent rolling boil with the perforated strainer basket already immersed.",
            "Add pasta and start the digital timer ONLY after the water returns to a full boil:",
            "  - Rigatoni (DeCecco): exactly 12 minutes",
            "  - Fettuccine: exactly 9 minutes",
            "  - Bucatini: exactly 8 minutes",
            "  - Orecchiette (max 2 lb batch, stir continuously): 8 minutes",
            "  - Linguine: exactly 6 minutes",
            "  - Spaghettini: exactly 4 minutes",
            "  - Gnocchetti: exactly 2 minutes",
            "Pull basket immediately, rush to sink, and drain for 1 minute. DO NOT rinse under cold water! The pasta emerges 80% cooked and reaches 95% al dente from residual heat.",
            "Dump onto clean baking sheets (approx. 5 lb per sheet). While steaming hot, immediately ladle 5 fl oz neutral oil over the pasta and gently toss with tongs until every strand is coated.",
            "Leave at room temperature for 15 minutes, tossing halfway through. Verify a tiny white al dente line ('punto al dente') in the center. Bag within 30 minutes and refrigerate."
        ],
        "scienceNote": "Heavily salting water (1.5 fl oz/gal ≈ 1.2% salinity) flavors the gluten matrix while strengthening the protein network. Ladling oil while pasta is steaming hot creates a hydrophobic lipid barrier that seals in internal moisture and prevents amylose gelatinization from gluing strands together."
    },
    {
        "id": "prep-soft-boiled-eggs",
        "title": "Precision Soft-Boiled Eggs (Ramen & Salad Standard)",
        "category": "Lineset & Operational Standards",
        "station": "Line Prep / Salad Station",
        "shelfLife": "3 days refrigerated",
        "prepFrequency": "3x / week",
        "haccp": "Cool in ice bath for minimum 30 minutes before peeling to contract egg proteins away from shell membrane.",
        "yields": {
            "12 Eggs / Stovetop": [
                {"name": "Water", "qty": "1 Gallon"},
                {"name": "Large Grade A Eggs", "qty": "12 each"}
            ]
        },
        "steps": [
            "Combi Method: Place whole eggs in cardboard cartons on bake trays into preheated combi oven at 212°F (100°C), 100% steam, fan speed 4 for exactly 8 minutes. Plunge into ice bath 30 minutes.",
            "Stovetop Method: Bring water to a heavy boil, then lower to a gentle simmer so eggs do not smash and crack. Lower eggs with slotted spoon. Set digital timer for EXACTLY 9 minutes.",
            "If eggs cook for even 15 seconds over time, yolk perimeter begins to set solid.",
            "Transfer immediately to a 50/50 ice water bath. Leave for 30 minutes.",
            "Gently roll egg along board to fracture shell across its entire surface, then peel under cold water."
        ],
        "scienceNote": "Egg white ovalbumin coagulates firmly between 144°F and 180°F, while yolk livetin and vitellin thicken into a jammy fudge between 149°F and 158°F. At 8-9 minutes, the heat wave penetrates through the white while leaving the core yolk at 152°F (66.5°C)."
    },
    {
        "id": "prep-squeeze-bottle-rules",
        "title": "Squeeze Bottle Protocols & Emulsion Integrity",
        "category": "Lineset & Operational Standards",
        "station": "All Line Stations",
        "shelfLife": "Operational Standard",
        "prepFrequency": "Every Restock",
        "haccp": "NEVER MARRY BOTTLES. Pouring old sauce into fresh product inoculates the entire batch with bacteria and voids freshness dating.",
        "yields": {
            "Bottle Specs": [
                {"name": "Restock Rule", "qty": "Wash & sanitize bottle on every fill"},
                {"name": "Suspended Solids", "qty": "Stir with chopstick before service"},
                {"name": "Tip Diameter", "qty": "Cut to recipe specification line"}
            ]
        },
        "steps": [
            "Squeeze bottles must be completely emptied, washed, and sanitized before every single refill. Never top off or marry partially empty bottles.",
            "Fill using clean funnels to keep exterior threads pristine.",
            "Select and attach nozzle caps calibrated to sauce viscosity (small gauge for herb oils, medium gauge for aiolis, wide gauge for chunky tartares).",
            "For emulsions with suspended solids (e.g. Sesame Soy Dressing, Citrus Vinaigrette), insert a clean chopstick and vigorously stir up settled seeds and solids before every rush."
        ],
        "scienceNote": "Marrying sauces violates first-in-first-out (FIFO) inventory and causes bacterial contamination from aged oils. Stirring with chopsticks resuspends hydrophilic particulate matter that slowly drops out of suspension over 4 hours."
    },
    {
        "id": "prep-vito-fryer-filtration",
        "title": "VITO Fryer Oil Filtration & Polar Compound Management",
        "category": "Lineset & Operational Standards",
        "station": "Deep Fryer Bank",
        "shelfLife": "Operational Protocol",
        "prepFrequency": "Daily Night Routine",
        "haccp": "Filter oil between 200°F and 350°F. Test polar compounds daily with 3M Oil Quality Test Strips.",
        "yields": {
            "Testing Standards": [
                {"name": "Filter Operating Temp", "qty": "200°F - 350°F"},
                {"name": "Filtration Cycle", "qty": "8 Minutes per vat"},
                {"name": "Oil Life Test", "qty": "3M Polar Compound Strip (Discard if >24% TPM)"}
            ]
        },
        "steps": [
            "Near close of service, skim loose crumbs from oil surface and beach. Remove fryer crumb basket.",
            "Scrape browned crumb buildup from vat sidewalls using a long-handled paint scraper so debris settles into filtration zone.",
            "Ensure oil is between 200°F and 350°F (never filter cold oil).",
            "Assemble VITO filtration unit with 1 fresh cellulose filter paper (visible writing facing up). 1 filter handles up to 4 fryers.",
            "Lower unit into fryer grate, plug in, and run the 8-minute pressure filtration cycle. The micro-filtration removes carbonized particles down to 5 microns.",
            "Lift unit, allow 15 seconds drain, and move to next fryer.",
            "Test with 3M Oil Quality Test Strip. If polar compounds exceed threshold, flag fryer for morning dump and clean."
        ],
        "scienceNote": "Thermal cycling breaks triglycerides down into free fatty acids (FFAs), polar compounds, and acrolein. Filtering carbonized particles prevents particulate catalysis, doubling the usable life of frying oil and eliminating burnt acrid flavors."
    },

    # PRODUCE & KNIFE WORK
    {
        "id": "prep-produce-washing-34f",
        "title": "Produce Sanitation & 34°F Water Washing Standard",
        "category": "Produce & Precision Knife Work",
        "station": "Prep Sink / Garde Manger",
        "shelfLife": "Operational Standard",
        "prepFrequency": "Daily",
        "haccp": "Ideal washing water temperature is 34°F (1°C). Never use detergents or soaps on food products.",
        "yields": {
            "Temperature Rules": [
                {"name": "Water Temperature", "qty": "34°F (near freezing)"},
                {"name": "Firm Produce", "qty": "Scrub with food nylon brush"},
                {"name": "Leafy Greens", "qty": "Submerge, agitate, drain 12 hours"}
            ]
        },
        "steps": [
            "Wash hands thoroughly and sanitize double prep sinks before receiving vegetables.",
            "Fill prep sink with clean water chilled to exactly 34°F. Ice may be added if tap water is warm.",
            "Wash all fresh produce before peeling or slicing—never before long storage, as excess surface water causes rapid rot.",
            "Firm produce (potatoes, melons, apples): scrub with dedicated nylon bristle brush to dislodge soil microbes.",
            "Leafy lettuces (Romaine, Gem): plunge into 34°F water, pump up and down vigorously to flush sand from root cores, and place core-up on perforated drain racks into cooler for overnight draining."
        ],
        "scienceNote": "Washing in 34°F water closes vegetable stomata and turgor pores, preventing bacterial internalization while crisping plant cell walls through osmotic water uptake."
    },
    {
        "id": "prep-fresh-herb-garnish-holding",
        "title": "Fresh Herb Garnishes & Microgreen Storage Law",
        "category": "Produce & Precision Knife Work",
        "station": "Garde Manger / Line Set",
        "shelfLife": "Herbs: 24-36h / Microgreens: 3-5 days",
        "prepFrequency": "Daily",
        "haccp": "Microgreens: Store in 16 oz cups with DRY paper towels top and bottom. Herbs: Cover with DAMP paper towels. Never reverse these!",
        "yields": {
            "Garnish Storage Methods": [
                {"name": "Chopped/Shaved Herbs", "qty": "Chilled container + DAMP paper towel"},
                {"name": "Microgreens", "qty": "16 oz cup + DRY paper towel top & bottom"},
                {"name": "Cilantro Sprigs", "qty": "Submerged in clean ice cold water"}
            ]
        },
        "steps": [
            "Receiving: Transfer microgreens into 16 oz clear portion cups with a folded DRY paper towel on the bottom and a DRY paper towel on top to wick away ambient condensation.",
            "Chopped Herbs (Parsley, Chives): Slice with razor-sharp knife without bruising. Place in line inserts and drape with a lightly DAMP paper towel to prevent edge desiccation.",
            "Shaved Herbs: Twist a tennis ball-sized bunch in palm into an explosive tight golf-ball bundle. Shave with chef knife to 1/16\" ribbons. Cover with damp paper towel.",
            "Cilantro & Mint Sprigs: Trim stems to 3\"; store standing submerged in cold water like flowers in a vase to maintain rigid turgor pressure."
        ],
        "scienceNote": "Microgreens have paper-thin cell walls with high surface area; any moisture film accelerates fungal decay and slime. Mature cut herbs have severed xylem vessels that rapidly transpire water into dry cooler air, requiring damp paper towels to maintain 100% relative micro-humidity."
    },

    # GOLDEN RULES & HACCP
    {
        "id": "prep-golden-rules-soup",
        "title": "Golden Rules of Soup: Reheating, Bain-Marie Holding & Ice Wands",
        "category": "Golden Rules & HACCP Protocols",
        "station": "Line Pass / Soup Station",
        "shelfLife": "Operational Standard",
        "prepFrequency": "Every Service",
        "haccp": "Reheat to 180°F before service. Hot hold at 165°F minimum. Cool to <40°F within 2 hours using ice wands.",
        "yields": {
            "Standard Operating Limits": [
                {"name": "Reheating Temp", "qty": "180°F (82°C) on medium-high"},
                {"name": "Minimum Hot Hold", "qty": "165°F (74°C) in steam table"},
                {"name": "Service Pass Temp", "qty": "170°F (77°C) checked by expediter"},
                {"name": "Max Bain-Marie Hold", "qty": "4 Hours maximum"}
            ]
        },
        "steps": [
            "All soups must be rapidly reheated to 180°F on medium-high heat with constant spatula scraping just before the rush, rushing through the danger zone (40°F to 140°F) as fast as possible. Never reheat in a steam table or bain-marie—steam tables are built to maintain heat, not create it.",
            "Never try to 'fix' a split, discolored, or over-thickened cream soup by adding cold milk or cream. If split or discolored, discard immediately.",
            "Soup bowls must be untouchably hot. Never, ever ladle hot soup into a room-temperature or cold bowl. Cover plated soups with an inverted pan until run to prevent skin formation.",
            "Cooling Soups & Sauces: Submerge pot in ice bath (75% ice + 25% water) with a sanitized ice wand. Ice level must be higher than soup level. Keep containers UNLIDDED during cooling to promote airflow and prevent condensation moisture from dripping back in.",
            "Soup must reach below 40°F within 2 hours. Transfer to 4-quart or 6-quart Cambros; do not use 22-quart containers as solid-to-liquid ratio will separate."
        ],
        "scienceNote": "Slow reheating in a bain-marie leaves food in the 90°F-120°F zone where Clostridium perfringens can double every 10 minutes. Condensation from lids dripping back into cooling soup creates anaerobic moisture pockets that accelerate spoilage."
    },
    {
        "id": "prep-golden-rules-oysters",
        "title": "Golden Rules of Raw Oysters & 90-Day Shell-Stock Retention",
        "category": "Golden Rules & HACCP Protocols",
        "station": "Raw Bar / Oyster Station",
        "shelfLife": "West Coast: 10 days / East Coast: 14 days / North Atlantic: 21 days from harvest",
        "prepFrequency": "Daily",
        "haccp": "Keep shell-stock harvest tags on file for a minimum of 90 days. Record first-sold and last-sold dates directly on tag with permanent marker.",
        "yields": {
            "Harvest Viability Limits": [
                {"name": "West Coast Oysters", "qty": "Max 7-10 days from harvest"},
                {"name": "East Coast Oysters", "qty": "Max 8-14 days from harvest"},
                {"name": "Storage Cooler Temp", "qty": "Coldest zone <40°F (preferably 34°F-36°F)"}
            ]
        },
        "steps": [
            "Receiving: Check harvest date on tag immediately. Reject any broken, cracked, or gaping oysters that do not close when tapped.",
            "Never allow oysters to sit submerged in fresh melt water! Melting ice will drown live oysters and turn nectar foul. Store on perforated drain pans completely buried in crushed ice and wet towels.",
            "Shucking Technique: Place folded dry towel with rolled 3\" lip. Sit oyster cup-down, flat shell up, hinge facing you. Cover top with towel. Insert shucker blade at hinge, wiggle with gentle pressure, twist 90° to pop seal, slide along top shell to sever top adductor muscle.",
            "Flip oyster cleanly in bottom cup to display pristine unblemished belly. Never spill the oyster liquor (nectar).",
            "Keep shell-stock tags in protected station sleeve. Wash and dry tag when batch is finished, write first-sold and last-sold dates, and archive in binder for 90 days."
        ],
        "scienceNote": "Oysters are live bivalves. Fresh water causes osmotic cell rupture, killing the oyster and allowing Vibrio vulnificus to proliferate rapidly. The 90-day shell-stock tag retention is a federal health requirement to trace bivalve harvesting waters in the event of an outbreak."
    },
    {
        "id": "prep-golden-rules-portioning",
        "title": "Golden Rules of Precision Portioning & Station Flow",
        "category": "Golden Rules & HACCP Protocols",
        "station": "All Kitchen Stations",
        "shelfLife": "Operational Standard",
        "prepFrequency": "Every Shift",
        "haccp": "Portioning target: 5 to 7 seconds per item. Exact weight or 0.1 oz under, NEVER over.",
        "yields": {
            "Portion Standards": [
                {"name": "Portion Cadence", "qty": "5 - 7 seconds per portion"},
                {"name": "Scale Accuracy", "qty": "Zeroed before every batch"},
                {"name": "Weight Tolerance", "qty": "Exact to -0.1 oz, never over"},
                {"name": "Batch-10 System", "qty": "Weigh bulk for 10 units, portion by feel"}
            ]
        },
        "steps": [
            "Station Ergonomics: Arrange raw product on your dominant side and scale directly in front. Non-dominant hand manipulates cups/bags; dominant hand portions and feels weight. Arms should never cross over.",
            "Portion Speed: Grab container with non-dominant hand, place on scale, fill with dominant hand, adjust weight, move to non-dominant counter. Count 1-2-3-4-5-6-7. Average portion time must be 5-7 seconds.",
            "Lidding Strategy: When using portion cups, never lid cups on trays. Spread 20-30 cups out on the prep table, snap lids on rapidly with both hands, then transfer neatly into trays.",
            "Batch-10 System: For high-volume multi-ingredient items, weigh out bulk ingredients for exactly 10 portions in order, then portion into 10 cups by feel without re-weighing each unit."
        ],
        "scienceNote": "Cross-body arm movements increase ergonomic fatigue by 300% during 4-hour prep shifts. The Batch-10 technique eliminates 90% of scale stabilization latency while preserving accurate batch yield."
    },
    {
        "id": "prep-golden-rules-breading",
        "title": "Golden Rules of Commercial Breading & Sifting",
        "category": "Golden Rules & HACCP Protocols",
        "station": "Fryer / Breading Station",
        "shelfLife": "Breading discard at end of day / prepped chicken max 6h",
        "prepFrequency": "3x Daily",
        "haccp": "Discard used egg wash daily. When sifting breading on the line, ensure flour dust does not drift into adjacent line sauces.",
        "yields": {
            "Station Setup": [
                {"name": "Pan 1", "qty": "Seasoned Flour & Sifter"},
                {"name": "Pan 2", "qty": "Fresh Egg Wash & Skimmer"},
                {"name": "Pan 3", "qty": "Panko / Breadcrumb Bin"}
            ]
        },
        "steps": [
            "Ensure station flow is strictly linear from left to right: Seasoned Flour -> Egg Wash -> Panko Breading -> Holding Tray.",
            "Never attempt to portion while breading: bread the entire batch first, then portion and adjust weights at the end.",
            "Do not overcrowd the breading pans. Flour and breading bins should be 1/3 to 1/2 full to allow easy tossing.",
            "Use wire coarse skimmer to lift proteins out of egg wash; shake off excess liquid before dropping into breadcrumbs.",
            "The final breaded protein must feel dry to the touch to prevent excess shortening absorption during frying.",
            "Sift seasoned flour through drum sifter and panko through 1/4\" basket sifter after every batch to remove wet dough balls."
        ],
        "scienceNote": "Wet clumps in breading insulate cold moisture against frying oil, leading to soggy spots and oil breakdown. Sifting keeps breadcrumbs uniformly dry and allows instant flash-vaporization of surface steam upon hitting 350°F oil."
    }
]

with open('data-prep-manual.js', 'w', encoding='utf-8') as f:
    f.write('// L\'Atelier Professional Kitchen Prep & Station Manual\n')
    f.write('// Authentic culinary operations, butchery specs, sauce builds, and HACCP protocols\n')
    f.write('window.ATELIER_PREP_MANUAL = ' + json.dumps(prep_items, indent=2, ensure_ascii=False) + ';\n')

print(f"Generated data-prep-manual.js with {len(prep_items)} comprehensive kitchen specs.")
