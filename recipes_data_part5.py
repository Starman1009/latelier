# recipes_data_part5.py
# High-precision culinary master recipes 32-41 for 150+ master threshold

PART_5_RECIPES = [
    {
        "id": "rec-chocolate-entremet",
        "title": "Dark Chocolate & Raspberry Mirror Glaze Entremet (Glaçage Miroir)",
        "cuisine": "French / Modern Haute Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Advanced",
        "prepMins": 90,
        "cookMins": 25,
        "totalMins": 115,
        "yieldServings": 10,
        "heroImage": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=80",
        "summary": "The showpiece of modern French pastry architecture: multi-layered entremet featuring dark chocolate pain de gênes sponge, crispy hazelnut praliné feuilletine base, tart raspberry gelee insert, cloud-like 66% Valrhona dark chocolate mousse, and a flawless gleaming dark chocolate mirror glaze (glaçage miroir).",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Ultra-glossy mirror reflection, crisp praline crunch, vibrant tart raspberry acid, silky melt-in-mouth mousse",
        "ingredients": [
            {"name": "Valrhona Caraïbe 66% Dark Chocolate", "qty": 280, "unit": "g", "prep": "chopped fine for mousse & glaze", "dept": "Baking & Pantry"},
            {"name": "Heavy Whipping Cream (36% fat)", "qty": 450, "unit": "ml", "prep": "chilled (whipped to soft peaks)", "dept": "Dairy & Fats"},
            {"name": "Whole Milk", "qty": 150, "unit": "ml", "prep": "for custard base", "dept": "Dairy & Fats"},
            {"name": "Egg Yolks", "qty": 3, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 180, "unit": "g", "prep": "divided for sponge, gelee, glaze", "dept": "Baking & Pantry"},
            {"name": "Pure Raspberry Puree (Boiron)", "qty": 200, "unit": "g", "prep": "100% fruit seedless", "dept": "Produce"},
            {"name": "Silver Gelatin Sheets (160 Bloom)", "qty": 14, "unit": "g", "prep": "bloomed in cold ice water (divided)", "dept": "Baking & Pantry"},
            {"name": "Hazelnut Praline Paste", "qty": 80, "unit": "g", "prep": "50% hazelnut caramel paste", "dept": "Baking & Pantry"},
            {"name": "Crêpes Dentelles (Feuilletine Flakes)", "qty": 50, "unit": "g", "prep": "crispy wafer flakes", "dept": "Baking & Pantry"},
            {"name": "Glucose Syrup / Corn Syrup", "qty": 100, "unit": "g", "prep": "prevents glaze crystallization", "dept": "Baking & Pantry"},
            {"name": "Sweetened Condensed Milk", "qty": 100, "unit": "g", "prep": "for mirror glaze opacity", "dept": "Dairy & Fats"},
            {"name": "Gold Luster Dust & Fresh Raspberries", "qty": 1, "unit": "pack", "prep": "for final presentation", "dept": "Produce"}
        ],
        "equipment": [
            {"name": "Silicone Eclipse or Silikomart 7-inch Dome Entremet Mold", "type": "Pâtisserie Tool"},
            {"name": "6-inch Round Cake Ring (for insert)", "type": "Bakeware"},
            {"name": "Digital Probe Thermometer", "type": "Precision Tool"},
            {"name": "Immersion Blender (without aerating head)", "type": "Small Appliance"}
        ],
        "miseEnPlace": [
            "Bloom gelatin sheets in ice-cold water.",
            "Make raspberry gelee insert: heat raspberry puree with 30g sugar, stir in 4g bloomed gelatin, pour into 6-inch ring and freeze solid for 3 hours.",
            "Mix melted chocolate, praline paste, and feuilletine; press into thin 6-inch disc and chill."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Bake Chocolate Biscuit: Whip whole eggs with sugar until pale ribbons form. Fold in sifted flour, cocoa powder, and melted butter. Bake 6-inch round at 350°F (175°C) for 10 minutes. Cool and place crunchy feuilletine disc directly on top.",
                "sensoryCue": "Tender sponge topped with a brittle, wafer-crisp praline layer.",
                "scienceNote": "Feuilletine flakes coated in fat (cocoa butter/praline) remain crisp because fat prevents moisture from migrating from the mousse.",
                "timerMins": 12
            },
            {
                "stepNum": 2,
                "text": "Make Dark Chocolate Bavarian Mousse: Scald milk and pour over whisked egg yolks and 25g sugar; cook over low heat to 180°F (82°C) to form crème anglaise. Strain over chopped 66% chocolate and 4g bloomed gelatin; whisk until silky. Cool to 88°F (31°C). Gently fold in 450ml soft-whipped cream.",
                "sensoryCue": "Velvety, airy, glossy chocolate mousse.",
                "scienceNote": "Folding whipped cream into chocolate at exactly 88-90°F prevents premature cocoa butter solidification (grainy mousse) while preventing the hot base from deflating cream air bubbles.",
                "timerMins": 15
            },
            {
                "stepNum": 3,
                "text": "Assembly (Upside Down): Pour 2/3 of the mousse into the 7-inch silicone mold. Press frozen raspberry gelee insert into center. Cover with remaining mousse. Top with biscuit-feuilletine disc (sponge side facing up, level with mold rim). Freeze solid at 0°F (-18°C) for minimum 8 hours (or overnight).",
                "sensoryCue": "Level base with zero air gaps.",
                "scienceNote": "Entremets must be frozen rock-hard to unmold from silicone without tearing delicate edges.",
                "timerMins": 480
            },
            {
                "stepNum": 4,
                "text": "Make Mirror Glaze (Glaçage Miroir): In a saucepan, boil water, sugar, and glucose syrup to 218°F (103°C). Off heat, stir in 6g bloomed gelatin. Pour hot syrup over condensed milk and 120g chopped chocolate. Emulsify with immersion blender kept strictly submerged on bottom of pitcher (do not lift or pump, to avoid bubbles). Cool to exactly 89-91°F (32-33°C).",
                "sensoryCue": "Gleaming, mirror-reflective, bubble-free dark chocolate glaze.",
                "scienceNote": "Keeping the immersion blender blade below liquid level eliminates air bubbles; temperature window of 89-91°F gives ideal viscosity to coat frozen dome without running off completely.",
                "timerMins": 15
            },
            {
                "stepNum": 5,
                "text": "The Glaze Pour: Unmold frozen entremet onto a wire rack set over a rimmed baking sheet. Pour mirror glaze in one smooth continuous pour over top center, allowing it to sheet effortlessly down curved sides. Let drip 5 minutes; trim bottom drips with palette knife. Transfer to presentation platter and refrigerate 4 hours to thaw before slicing with a warm knife.",
                "sensoryCue": "Breathtaking mirror reflection showing room interior; flawless glassy black dome with fresh raspberries and gold leaf.",
                "scienceNote": "Thermal shock between 90°F glaze and 0°F frozen dome instantly sets gelatin, creating a 1mm uniform glossy shell.",
                "timerMins": 10
            }
        ],
        "sensoryIndicators": {
            "aroma": "Intense dark cocoa roast, bright fresh raspberry perfume, toasted hazelnut praline",
            "texture": "Multi-textural symphony: glossy mirror slip, melting airy mousse, tart firm gelee, and shattering praline crunch",
            "finish": "Bittersweet 66% cacao tannins illuminated by vibrant raspberry acidity"
        },
        "scienceNotes": "Mirror glazes rely on a precise balance of sucrose, glucose, and gelatin. Glucose prevents sucrose recrystallization into matte grains, while gelatin and condensed milk provide cohesive tensile strength and light opacity.",
        "troubleshooting": {
            "Glaze has micro air bubbles": "Immersion blender was pumped or lifted above liquid; tap pitcher on counter and strain through fine mesh.",
            "Glaze slides off leaving bald patches": "Glaze was too hot (above 95°F) or entremet surface was frosted with ice crystals; wipe frost off before glazing.",
            "Torn edges when unmolding": "Entremet was not frozen solid; must freeze at least 8 hours."
        },
        "substitutions": [
            {"ingredient": "Raspberry Puree", "substitute": "Passionfruit Puree or Mango Puree", "ratio": "1:1 for tropical profile"},
            {"ingredient": "Feuilletine Flakes", "substitute": "Crushed Cornflakes or Puffed Rice with Praline", "ratio": "1:1"}
        ],
        "flavorPairings": ["Vintage Champagne", "Single Malt Scotch", "Espresso Ristretto", "Fresh Mint"],
        "advancedTechnique": "Spiderweb effect: dropping 1 tbsp neutral white glaze on offset spatula and swiping across hot dark glaze for marble webs.",
        "storageAndReheating": "Store in refrigerator up to 3 days. Do not refreeze once thawed.",
        "nutritionEstimates": {"calories": 480, "protein": 7, "carbs": 52, "fat": 28},
        "relatedRecipes": ["rec-mousse-chocolat", "rec-opera-cake", "rec-panna-cotta"],
        "relatedTechniques": ["Mirror glaze rheology temperature window", "Immersion blender air bubble elimination", "Upside-down silicone mold assembly"]
    },
    {
        "id": "rec-french-meringues",
        "title": "Meringues Suisses aux Baies Sauvages (Crisp Swiss Shells with Raspberry Powder & Chantilly)",
        "cuisine": "French / Classical Pâtisserie",
        "category": "dessert",
        "slot": "predessert",
        "difficulty": "Easy",
        "prepMins": 20,
        "cookMins": 90,
        "totalMins": 110,
        "yieldServings": 12,
        "heroImage": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pure art of sugar and egg albumin: Swiss method meringues gently heated over a water bath to dissolve all sugar crystals, whipped into a blindingly glossy, stiff marshmallow meringue, piped into elegant rosettes, dusted with freeze-dried raspberry powder, and dehydrated to porcelain-crisp perfection.",
        "dietary": ["Vegetarian", "Gluten-Free", "Dairy-Free Option"],
        "sensoryRole": "Porcelain-crisp exterior that melts into sweet spun sugar on the tongue, tart berry dust contrast",
        "ingredients": [
            {"name": "Egg Whites", "qty": 150, "unit": "g", "prep": "approx 5 large eggs, room temp, no yolk traces", "dept": "Dairy & Fats"},
            {"name": "Superfine Castor Sugar", "qty": 300, "unit": "g", "prep": "strict 1:2 ratio to egg whites", "dept": "Baking & Pantry"},
            {"name": "Cream of Tartar (Potassium Bitartrate)", "qty": 1.5, "unit": "g", "prep": "acid protein stabilizer", "dept": "Baking & Pantry"},
            {"name": "Pure Vanilla Bean Paste", "qty": 5, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Freeze-Dried Raspberry Powder", "qty": 15, "unit": "g", "prep": "pulverized for dusting", "dept": "Produce"},
            {"name": "Stabilized Vanilla Chantilly Cream", "qty": 200, "unit": "ml", "prep": "for sandwiching (optional)", "dept": "Dairy & Fats"}
        ],
        "equipment": [
            {"name": "Stand Mixer with Whisk Attachment", "type": "Small Appliance"},
            {"name": "Heatproof Glass or Copper Whisking Bowl", "type": "Cookware"},
            {"name": "Piping Bag with French Star Tip (866)", "type": "Pâtisserie Tool"},
            {"name": "Silpat Baking Mats", "type": "Baking Supply"}
        ],
        "miseEnPlace": [
            "Wipe mixer bowl and whisk with lemon juice or white vinegar to remove all traces of fat.",
            "Preheat oven to 200°F (95°C) with convection fan on low.",
            "Line baking sheets with Silpat mats."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Bain-Marie Heating: Combine egg whites, castor sugar, and cream of tartar in heatproof bowl set over a pot of barely simmering water (water must not touch bowl). Whisk constantly for 4-5 minutes until sugar is completely dissolved and mixture reaches 140-145°F (60-63°C). Rub between fingers: it must feel completely smooth without a single sugar grain.",
                "sensoryCue": "Frothy, warm liquid with zero gritty texture.",
                "scienceNote": "Heating to 140°F dissolves 100% of sucrose crystals while denaturing egg ovalbumin proteins, allowing them to stretch around air pockets with unprecedented tensile strength.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Whip to Glossy Peaks: Transfer hot bowl immediately to stand mixer fitted with whisk attachment. Whip on high speed for 7 to 8 minutes until meringue is stiff, blindingly glossy, holds razor-sharp peaks, and bowl has cooled to room temperature. Whisk in vanilla paste.",
                "sensoryCue": "Brilliant porcelain gleam; peaks stand straight up like marble sculptures.",
                "scienceNote": "Swiss meringue creates a far more stable, dense micro-foam than French meringue, completely resistant to weeping or collapse.",
                "timerMins": 8
            },
            {
                "stepNum": 3,
                "text": "Pipe Rosettes: Transfer meringue into piping bag fitted with French star tip. Pipe uniform 2-inch rosettes onto Silpat-lined baking sheets holding tip perpendicular. Dust lightly through a fine sieve with freeze-dried raspberry powder.",
                "sensoryCue": "Sharp fluted ridges holding crisp architectural definition; dusting of ruby raspberry powder.",
                "scienceNote": "Freeze-dried fruit powder provides intense natural acid and color without introducing water that would dissolve the sugar matrix.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "Dehydrate: Bake at 200°F (95°C) for 90 minutes. (Do not allow oven to exceed 210°F, or meringues will turn yellow). Turn oven off, prop door open 1 inch with a wooden spoon, and let meringues cool completely inside the dry oven for 2 hours.",
                "sensoryCue": "Pristine snowy white shells that lift cleanly off the Silpat with zero sticking.",
                "scienceNote": "Meringues are not baked; they are dehydrated. Low temperature evaporates water while preserving white color and solidifying sugar-protein walls.",
                "timerMins": 90
            },
            {
                "stepNum": 5,
                "text": "Serve or Store: Serve standalone as crisp sweet kisses, or sandwich two shells with stabilized vanilla Chantilly cream and fresh wild berries.",
                "sensoryCue": "Shattering dry crunch followed instantly by melting sweet silk.",
                "scienceNote": "Pure sucrose-protein matrix dissolves instantly upon saliva contact via rapid sugar solubilization.",
                "timerMins": 2
            }
        ],
        "sensoryIndicators": {
            "aroma": "Sweet vanilla bean, spun sugar, tart fruity raspberry notes",
            "texture": "Porcelain-brittle snap, wafer-light hollow lightness, dissolving like cotton candy on the tongue",
            "finish": "Clean sweet finish cut by the sharp electric tang of raspberry powder"
        },
        "scienceNotes": "Cream of tartar supplies tartaric acid, lowering egg white pH to ~4.5. This optimal acidic environment stabilizes the egg ovalbumin and conalbumin proteins against excessive coagulation, preventing the meringue from weeping liquid (syneresis).",
        "troubleshooting": {
            "Meringues turn beige or yellow": "Oven was too hot (over 215°F), causing sugar caramelization; bake at strictly 200°F.",
            "Sticky chewy center": "Meringues were not dried long enough, or room humidity was high; leave in dry oven longer.",
            "Beads of syrup weep onto surface": "Undissolved sugar crystals; heat over water bath until completely dissolved in step 1."
        },
        "substitutions": [
            {"ingredient": "Raspberry Powder", "substitute": "Matcha Green Tea Powder, Cocoa Powder, or Passionfruit Powder", "ratio": "1:1 for stunning color contrasts"},
            {"ingredient": "Cream of Tartar", "substitute": "1/2 tsp fresh lemon juice", "ratio": "1:1"}
        ],
        "flavorPairings": ["Earl Grey Tea", "Champagne Rosé", "Fresh Strawberries", "Espresso"],
        "advancedTechnique": "Painting interior lines of piping bag with gel food color before filling with meringue for two-tone striped ribbon rosettes.",
        "storageAndReheating": "Store in an airtight container with silica gel packets at room temperature for up to 3 weeks. Do not refrigerate (humidity ruins meringue).",
        "nutritionEstimates": {"calories": 65, "protein": 1, "carbs": 15, "fat": 0},
        "relatedRecipes": ["rec-passionfruit-pavlova", "rec-french-macarons", "rec-shattered-lemon-tart"],
        "relatedTechniques": ["Swiss meringue water bath dissolution", "Oven dehydration desiccation", "Acid protein stabilization"]
    },
    {
        "id": "rec-flan-patissier",
        "title": "Parisian Flan Pâtissier (Custard Tart with Madagascar Vanilla Bean in Crisp Shortcrust)",
        "cuisine": "French / Classical Boulangerie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 40,
        "totalMins": 70,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
        "summary": "The beloved Parisian boulangerie masterpiece: a tall 2-inch slice of ultra-creamy, wobbly Madagascar vanilla custard baked inside a crisp, buttery pâte brisée until the top blisters into dark caramelized leopard spots.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Deep Madagascar vanilla perfume, unctuous wobbling custard cream, caramelized top blister, buttery crisp crust",
        "ingredients": [
            {"name": "Pâte Brisée (Flaky French Pastry)", "qty": 300, "unit": "g", "prep": "chilled all-butter dough", "dept": "Baking & Pantry"},
            {"name": "Whole Farm Milk (3.5% fat)", "qty": 700, "unit": "ml", "prep": "fresh", "dept": "Dairy & Fats"},
            {"name": "Heavy Cream (36% fat)", "qty": 300, "unit": "ml", "prep": "fresh dairy", "dept": "Dairy & Fats"},
            {"name": "Madagascar Bourbon Vanilla Beans", "qty": 2, "unit": "whole", "prep": "split and seeds scraped", "dept": "Spices & Botanicals"},
            {"name": "Egg Yolks", "qty": 5, "unit": "whole", "prep": "approx 90g", "dept": "Dairy & Fats"},
            {"name": "Whole Eggs", "qty": 2, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 180, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Cornstarch (Maizena)", "qty": 90, "unit": "g", "prep": "sifted starch binder", "dept": "Baking & Pantry"},
            {"name": "Unsalted European Butter", "qty": 40, "unit": "g", "prep": "cubed cold", "dept": "Dairy & Fats"},
            {"name": "Fleur de Sel", "qty": 2, "unit": "g", "prep": "fine pinch", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "Deep 8-inch Springform Pan or Pastry Ring (2-inch deep)", "type": "Bakeware"},
            {"name": "Heavy Stainless Steel Saucier / Pot", "type": "Cookware"},
            {"name": "Balloon Whisk", "type": "Small Tool"}
        ],
        "miseEnPlace": [
            "Roll pâte brisée to 3.5mm thickness; line the deep 8-inch ring/pan, pressing into corners; freeze 30 minutes.",
            "Infuse milk, cream, vanilla pod, and scraped seeds in saucepan over medium heat; bring to gentle simmer and let steep 20 minutes.",
            "Preheat oven to 350°F (175°C) to blind-bake crust."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Blind-Bake Shell: Line frozen pastry shell with parchment and pie weights. Bake at 350°F (175°C) for 20 minutes. Remove weights; bake 8 more minutes until pale golden and dry. Cool completely. Raise oven to 390°F (200°C).",
                "sensoryCue": "Pastry is crisp, pale gold, and buttery.",
                "scienceNote": "Blind-baking prevents the massive 1-liter liquid custard volume from turning the bottom crust into soggy raw dough.",
                "timerMins": 28
            },
            {
                "stepNum": 2,
                "text": "Make Vanilla Custard: Reheat vanilla milk/cream to a simmer. In a large bowl, whisk egg yolks, whole eggs, sugar, and cornstarch until smooth and pale. Temper hot milk into egg mixture while whisking. Return to pan; bring to a full boil over medium heat while whisking vigorously for 2 minutes until very thick and glossy.",
                "sensoryCue": "Thick, satiny custard densely peppered with black vanilla bean seeds.",
                "scienceNote": "Boiling for 2 minutes activates cornstarch amylose gelatinization and deactivates alpha-amylase enzymes in egg yolks that would otherwise liquefy the starch custard.",
                "timerMins": 6
            },
            {
                "stepNum": 3,
                "text": "Off heat, whisk cold butter and fleur de sel into hot custard until completely emulsified and glossy.",
                "sensoryCue": "Velvety sheen; buttery vanilla aroma.",
                "scienceNote": "Whisking cold butter into hot starch creates a micro-emulsion that imparts luxurious mouthfeel.",
                "timerMins": 2
            },
            {
                "stepNum": 4,
                "text": "Pour hot custard immediately into the par-baked pastry shell, smoothing top with spatula. Bake at 390°F (200°C) for 35 to 40 minutes until top develops dark caramelized blistered spots and center has a firm wobble.",
                "sensoryCue": "Golden-bronzed top with dark leopard patches of caramelized milk sugar.",
                "scienceNote": "High 390°F heat caramelizes surface lactose and sucrose (creating the signature Paris boulangerie blistered crown) while the dense interior sets gently.",
                "timerMins": 38
            },
            {
                "stepNum": 5,
                "text": "Cool completely at room temperature for 3 hours, then refrigerate for at least 4 hours (or overnight) before slicing with a clean sharp chef's knife.",
                "sensoryCue": "Pristine tall 2-inch slices; silky wobbly custard texture that holds clean shape.",
                "scienceNote": "Cornstarch retrogradation and butterfat solidification require full chilling to build a sliceable yet wobbly gel matrix.",
                "timerMins": 240
            }
        ],
        "sensoryIndicators": {
            "aroma": "Intense bourbon vanilla bean, caramelized milk skin, toasted butter shortcrust",
            "texture": "Crisp flaky pastry base meeting dense, silky, ultra-smooth wobbly custard",
            "finish": "Persistent vanilla bean sweetness balanced by clean dairy richness"
        },
        "scienceNotes": "Flan Pâtissier is the gold standard of starch-thickened custards. Unlike crème brûlée (pure egg yolk coagulation), Flan Pâtissier relies on a high concentration of cornstarch (90g/liter) which sets into a rigid, freestanding gel that can be sliced cleanly at room temperature.",
        "troubleshooting": {
            "Custard liquefies after cooling": "Custard was not boiled for full 2 minutes; egg yolk amylase digested the cornstarch.",
            "Soggy bottom crust": "Crust was not blind-baked sufficiently before filling.",
            "Custard curdles or splits": "Too much butter was added or custard was scorched on pan bottom; whisk continuously during boiling."
        },
        "substitutions": [
            {"ingredient": "Madagascar Vanilla", "substitute": "Pistachio Paste (80g) or Melted Dark Chocolate (150g)", "ratio": "For Flan Pistache or Flan Chocolat"},
            {"ingredient": "Pâte Brisée", "substitute": "Pâte Feuilletée (Puff Pastry)", "ratio": "1:1 for flaky layered rim"}
        ],
        "flavorPairings": ["Espresso", "Café Crème", "Fresh Red Berries", "Earl Grey Tea"],
        "advancedTechnique": "Cold-infusing split vanilla beans in milk in refrigerator for 24 hours prior to simmering for maximum extraction of delicate vanillin compounds.",
        "storageAndReheating": "Store in refrigerator covered up to 4 days. Serve chilled or slightly tempered 20 minutes before enjoying.",
        "nutritionEstimates": {"calories": 390, "protein": 7, "carbs": 44, "fat": 21},
        "relatedRecipes": ["rec-creme-brulee", "rec-creme-caramel", "rec-eclairs-chocolat"],
        "relatedTechniques": ["Cornstarch amylase deactivation boil", "High-heat lactose surface blistering", "Deep-ring tart blind-baking"]
    },
    {
        "id": "rec-tarte-bourdaloue",
        "title": "Tarte Bourdaloue (French Poached Pear & Almond Frangipane Tart)",
        "cuisine": "French / Classical Pâtisserie",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Intermediate",
        "prepMins": 40,
        "cookMins": 45,
        "totalMins": 85,
        "yieldServings": 8,
        "heroImage": "https://images.unsplash.com/photo-1568571780765-9276ac8b75a2?auto=format&fit=crop&w=1200&q=80",
        "summary": "The Parisian classic created on Rue Bourdaloue in the 19th century: sweet buttery pâte sucrée tart shell filled with rich almond frangipane cream, topped with tender vanilla-poached William pears fanned across the surface, baked until golden and glazed with warm apricot confiture and toasted sliced almonds.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Floral juicy poached pears, rich nutty almond frangipane, buttery crumbly crust, shiny apricot glaze",
        "ingredients": [
            {"name": "Pâte Sucrée (French Sweet Tart Dough)", "qty": 300, "unit": "g", "prep": "chilled all-butter sweet crust", "dept": "Baking & Pantry"},
            {"name": "Firm William or Bosc Pears", "qty": 3, "unit": "whole", "prep": "peeled, cored, poached in vanilla syrup, halved", "dept": "Produce"},
            {"name": "Blanched Almond Flour", "qty": 120, "unit": "g", "prep": "superfine sifted", "dept": "Baking & Pantry"},
            {"name": "Unsalted European Butter", "qty": 100, "unit": "g", "prep": "softened at room temp", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 100, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "Large Eggs", "qty": 2, "unit": "whole", "prep": "room temperature (approx 100g)", "dept": "Dairy & Fats"},
            {"name": "Poire Williams Eau-de-Vie or Dark Rum", "qty": 20, "unit": "ml", "prep": "pear brandy", "dept": "Pantry"},
            {"name": "All-Purpose Pastry Flour", "qty": 15, "unit": "g", "prep": "sifted", "dept": "Baking & Pantry"},
            {"name": "Pure Vanilla Bean Paste", "qty": 5, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Apricot Jam / Confiture", "qty": 60, "unit": "g", "prep": "warmed and strained for pastry glaze", "dept": "Baking & Pantry"},
            {"name": "Toasted Sliced Almonds", "qty": 30, "unit": "g", "prep": "golden roasted", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "9-inch Fluted Tart Pan with Removable Bottom", "type": "Bakeware"},
            {"name": "Pastry Brush", "type": "Small Tool"},
            {"name": "Chef's Knife for Pear Fanning", "type": "Cutlery"}
        ],
        "miseEnPlace": [
            "Poach pear halves in simple syrup with vanilla bean and lemon peel for 15 minutes; drain thoroughly on paper towels.",
            "Blind-bake pâte sucrée shell at 350°F (175°C) for 15 minutes; cool.",
            "Preheat oven to 350°F (175°C)."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Make Crème Frangipane: In a stand mixer fitted with paddle, beat softened butter and sugar for 2 minutes until creamy. Add eggs one at a time, beating until emulsified. Fold in almond flour, 15g pastry flour, vanilla paste, and Poire Williams brandy until smooth.",
                "sensoryCue": "Fluffy, pale ivory almond cream with rich perfume of toasted nuts and brandy.",
                "scienceNote": "Adding a tiny amount of flour (15g) binds free water, preventing the almond butter emulsion from separating into grease during baking.",
                "timerMins": 5
            },
            {
                "stepNum": 2,
                "text": "Spread Frangipane: Spread the frangipane evenly into the cooled par-baked tart shell, smoothing with offset spatula to within 1/4-inch of the rim.",
                "sensoryCue": "Even, fragrant bed of almond cream.",
                "scienceNote": "Frangipane puffs during baking; leaving 1/4-inch space prevents it from spilling over tart walls.",
                "timerMins": 2
            },
            {
                "stepNum": 3,
                "text": "Fan & Arrange Pears: Slice poached pear halves crosswise into thin 1/8-inch slices, keeping the pear shape intact. Gently press pear half with hand to fan slices outward. Use spatula to transfer 5-6 fanned pear halves onto frangipane in a pinwheel star pattern, pressing lightly into the cream.",
                "sensoryCue": "Elegant symmetrical pinwheel of poached pear fans across almond cream.",
                "scienceNote": "Draining pears thoroughly prevents excess syrup from making the frangipane soggy around the fruit.",
                "timerMins": 5
            },
            {
                "stepNum": 4,
                "text": "Bake: Bake at 350°F (175°C) for 40 to 45 minutes until frangipane is puffed, set in center, and deep golden-brown between pear slices.",
                "sensoryCue": "Golden-bronzed almond cake surrounding succulent translucent pears; toasted nut aroma.",
                "scienceNote": "Almond fats and egg proteins coagulate into a tender cake crumb while pear juices concentrate and caramelize slightly.",
                "timerMins": 42
            },
            {
                "stepNum": 5,
                "text": "Glaze & Finish: Warm apricot jam with 1 tbsp water; strain. Brush warm glaze over warm pears and frangipane to create a brilliant glassy sheen. Scatter toasted sliced almonds around tart perimeter. Cool to room temp before serving.",
                "sensoryCue": "Gleaming golden tart with glossy apricot shine and crunchy almond border.",
                "scienceNote": "Apricot glaze seals exposed fruit from oxidation and imparts professional patisserie luster.",
                "timerMins": 5
            }
        ],
        "sensoryIndicators": {
            "aroma": "Poached sweet pears, roasted almonds, Poire Williams eau-de-vie, buttery shortcrust",
            "texture": "Crisp sweet shortbread base, tender moist almond cake, and silky melting juicy pears",
            "finish": "Subtle fruit acidity from apricot glaze balancing sweet almond marzipan richness"
        },
        "scienceNotes": "Pears and almonds share natural chemical flavor affinities: both contain benzaldehyde precursors and stone-fruit volatile ketones, which amplify each other when baked together in frangipane.",
        "troubleshooting": {
            "Soggy frangipane around pears": "Pears were not drained on paper towels before placing onto frangipane.",
            "Frangipane separates into greasy butter slick": "Eggs were too cold when added to butter, breaking emulsion; use room temp ingredients.",
            "Tart edges burn": "Shield fluted tart perimeter with aluminum foil ring if browning too quickly."
        },
        "substitutions": [
            {"ingredient": "William Pears", "substitute": "Bosc Pears, Ripe Apricots, or Poached Figs", "ratio": "1:1"},
            {"ingredient": "Poire Williams", "substitute": "Calvados, Cognac, or Amaretto", "ratio": "1:1"}
        ],
        "flavorPairings": ["Crème Fraîche", "Poire Williams Digestif", "Earl Grey Tea", "Sauternes"],
        "advancedTechnique": "Poaching pears in a spiced Riesling syrup with star anise and lemon verbena before fanning.",
        "storageAndReheating": "Keep at room temp for 2 days covered with foil, or refrigerate up to 4 days.",
        "nutritionEstimates": {"calories": 420, "protein": 8, "carbs": 46, "fat": 24},
        "relatedRecipes": ["rec-tarte-tatin", "rec-financiers-amandes", "rec-shattered-lemon-tart"],
        "relatedTechniques": ["Pear crosswise fanning pinwheel", "Frangipane fat emulsion stabilization", "Apricot confiture glazing"]
    },
    {
        "id": "rec-clafoutis-cerises",
        "title": "Clafoutis Limousin aux Cerises Noires (Whole Dark Cherry Custard Cake)",
        "cuisine": "French / Limousin Classical",
        "category": "dessert",
        "slot": "dessert",
        "difficulty": "Easy",
        "prepMins": 15,
        "cookMins": 35,
        "totalMins": 50,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1568571780765-9276ac8b75a2?auto=format&fit=crop&w=1200&q=80",
        "summary": "The rustic soul of central France: sweet, plump dark cherries baked in a delicate flan-like batter of farm eggs, whole milk, heavy cream, Kirsch, and vanilla, served warm straight from a buttered ceramic dish dusted with powdered sugar.",
        "dietary": ["Vegetarian"],
        "sensoryRole": "Warm juicy cherry bursts, delicate custardy pancake-flan crumb, sweet almond and Kirsch perfume",
        "ingredients": [
            {"name": "Fresh Sweet Dark Cherries (Burlat or Bing)", "qty": 500, "unit": "g", "prep": "stemmed (traditionally unpitted for almond flavor, or pitted)", "dept": "Produce"},
            {"name": "Large Whole Eggs", "qty": 3, "unit": "whole", "prep": "room temperature", "dept": "Dairy & Fats"},
            {"name": "Egg Yolk", "qty": 1, "unit": "whole", "prep": "adds tenderness", "dept": "Dairy & Fats"},
            {"name": "Whole Milk", "qty": 200, "unit": "ml", "prep": "farm fresh", "dept": "Dairy & Fats"},
            {"name": "Heavy Cream (36% fat)", "qty": 100, "unit": "ml", "prep": "fresh cream", "dept": "Dairy & Fats"},
            {"name": "Granulated Castor Sugar", "qty": 100, "unit": "g", "prep": "fine crystals", "dept": "Baking & Pantry"},
            {"name": "All-Purpose Pastry Flour", "qty": 70, "unit": "g", "prep": "sifted (low flour ensures flan texture)", "dept": "Baking & Pantry"},
            {"name": "Kirschwasser (Cherry Brandy)", "qty": 25, "unit": "ml", "prep": "adds classic stone-fruit aroma", "dept": "Pantry"},
            {"name": "Pure Vanilla Bean Paste", "qty": 5, "unit": "ml", "prep": "bourbon vanilla", "dept": "Spices & Botanicals"},
            {"name": "Unsalted European Butter", "qty": 30, "unit": "g", "prep": "melted and cooled", "dept": "Dairy & Fats"},
            {"name": "Powdered Sugar", "qty": 15, "unit": "g", "prep": "for dusting", "dept": "Baking & Pantry"}
        ],
        "equipment": [
            {"name": "10-inch Oval Ceramic Gratin Dish or Cast Iron Skillet", "type": "Bakeware"},
            {"name": "Whisk & Mixing Bowl", "type": "Cookware"}
        ],
        "miseEnPlace": [
            "Butter baking dish heavily and coat with granulated sugar, tapping out excess.",
            "Preheat oven to 375°F (190°C).",
            "Macerate cherries in Kirsch and 1 tbsp sugar for 15 minutes."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Arrange Cherries: Spread macerated dark cherries in a single dense layer across bottom of prepared ceramic dish.",
                "sensoryCue": "Glossy crimson cherries glistening with sugar and Kirsch.",
                "scienceNote": "Traditional purists leave pits intact because cherry pits contain amygdalin, releasing a delicate bitter almond aroma during baking.",
                "timerMins": 2
            },
            {
                "stepNum": 2,
                "text": "Make Crêpe Batter: Whisk whole eggs, extra yolk, and sugar in a bowl for 1 minute. Whisk in sifted flour and pinch of salt until smooth paste forms. Slowly pour in milk, heavy cream, melted butter, vanilla paste, and remaining Kirsch from maceration until a smooth, thin batter forms.",
                "sensoryCue": "Thin, fluid batter similar to French crêpe batter.",
                "scienceNote": "Low flour-to-liquid ratio (70g flour to 300ml dairy) ensures a delicate baked flan texture rather than a heavy cake.",
                "timerMins": 4
            },
            {
                "stepNum": 3,
                "text": "Pour Batter: Pour batter gently over cherries in the dish.",
                "sensoryCue": "Cherries peek out through the ivory batter.",
                "scienceNote": "Cherries stay anchored on the bottom while the light batter surrounds them, puffing slightly during baking.",
                "timerMins": 1
            },
            {
                "stepNum": 4,
                "text": "Bake: Bake at 375°F (190°C) for 32 to 36 minutes until edges are puffed and golden brown, and center is set with a tender custard wobble.",
                "sensoryCue": "Puffed golden rim, dark glistening cherries, warm aroma of vanilla and roasted stone fruit.",
                "scienceNote": "Egg and dairy proteins coagulate at 170-175°F, locking the cherries inside a custardy matrix.",
                "timerMins": 35
            },
            {
                "stepNum": 5,
                "text": "Rest & Serve Warm: Rest 10 minutes (it will gently settle as it cools). Dust heavily with sifted powdered sugar. Serve warm directly from dish.",
                "sensoryCue": "Snowy powdered sugar melting against warm purple cherries; warm custard melt.",
                "scienceNote": "Clafoutis is best served warm (110-120°F) when the custard fats are soft and supple on the palate.",
                "timerMins": 10
            }
        ],
        "sensoryIndicators": {
            "aroma": "Warm roasted cherries, Kirschwasser brandy, vanilla bean, caramelized butter crust",
            "texture": "Juicy sweet-tart cherry bursts against velvety, tender, melt-in-mouth custardy crumb",
            "finish": "Lingering almond and cherry blossom notes with clean dairy sweetness"
        },
        "scienceNotes": "In French culinary law, a clafoutis can only be named 'Clafoutis' if made with cherries; if made with other fruits (plums, pears, berries), it is technically a 'Flognarde'.",
        "troubleshooting": {
            "Rubbery texture": "Too much flour was added or batter was over-whipped; whisk just until flour dissolves.",
            "Watery puddle around cherries": "Frozen cherries were used without thawing and draining; use fresh dry cherries.",
            "Batter didn't set in center": "Baking time was too short; center should feel springy and custardy to the touch."
        },
        "substitutions": [
            {"ingredient": "Dark Sweet Cherries", "substitute": "Sour Morello Cherries (increase sugar by 20g) or Blackberries", "ratio": "1:1"},
            {"ingredient": "Kirschwasser", "substitute": "Amaretto or Cognac", "ratio": "1:1"}
        ],
        "flavorPairings": ["Cold Whole Milk", "Riesling Demi-Sec", "Vanilla Bean Ice Cream", "Café au Lait"],
        "advancedTechnique": "Lightly roasting pitted cherries in a hot pan with butter for 2 minutes to concentrate sugars before baking in custard.",
        "storageAndReheating": "Best enjoyed day of baking. Refrigerate leftovers up to 3 days; re-warm in 325°F oven for 8 minutes.",
        "nutritionEstimates": {"calories": 240, "protein": 6, "carbs": 32, "fat": 10},
        "relatedRecipes": ["rec-creme-caramel", "rec-tarte-bourdaloue", "rec-madeleines-commercy"],
        "relatedTechniques": ["Low-hydration crêpe batter baking", "Kirsch fruit maceration", "Ceramic gratin heat retention"]
    }
]

print(f"Loaded {len(PART_5_RECIPES)} recipes in PART_5_RECIPES.")
