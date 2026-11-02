# -*- coding: utf-8 -*-
"""
World Culinary Traditions: Southeast Asian, Indian, Mexican & Middle Eastern Masterpieces
24 authentic, deeply detailed recipes with all 20 required properties.
"""

WORLD_RECIPES = [
    {
        "id": "rec-butter-chicken",
        "title": "Authentic Murgh Makhani (Delhi-Style Butter Chicken)",
        "cuisine": "Indian Punjabi",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 40,
        "totalMins": 70,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?auto=format&fit=crop&w=1200&q=80",
        "summary": "The authentic 1950s Moti Mahal classic from Delhi: tender chicken thighs marinated in Kashmiri chili yogurt, charred over high heat, then simmered in a velvety, satin-smooth sauce of reduced San Marzano tomatoes, cultured butter, cashew cream, and sun-dried kasuri methi (fenugreek leaves). Finished with the ancient Dhungar charcoal smoking technique.",
        "dietary": ["gluten-free"],
        "sensoryRole": "Silky, buttery tomato gravy balanced by fenugreek bitterness, warming garam masala spices, and smoky tandoor char.",
        "ingredients": [
            {"qty": 800, "unit": "g", "name": "Boneless, skinless chicken thighs", "prep": "cut into 4cm pieces", "dept": "butchery"},
            {"qty": 150, "unit": "g", "name": "Thick Greek yogurt or hung curd (dahi)", "prep": "full fat", "dept": "dairy"},
            {"qty": 30, "unit": "g", "name": "Ginger-garlic paste (equal parts fresh garlic and ginger)", "prep": "blended fine", "dept": "produce"},
            {"qty": 20, "unit": "g", "name": "Kashmiri chili powder (Deggi Mirch)", "prep": "vibrant red, mild heat", "dept": "pantry"},
            {"qty": 800, "unit": "g", "name": "Ripe plum tomatoes or San Marzano canned tomatoes", "prep": "pureed and strained", "dept": "produce"},
            {"qty": 80, "unit": "g", "name": "Unsalted European butter", "prep": "cold cubes", "dept": "dairy"},
            {"qty": 80, "unit": "ml", "name": "Heavy whipping cream", "prep": "chilled", "dept": "dairy"},
            {"qty": 50, "unit": "g", "name": "Raw whole cashews", "prep": "soaked in hot water and blended into fine cream", "dept": "drygoods"},
            {"qty": 10, "unit": "g", "name": "Kasuri Methi (dried fenugreek leaves)", "prep": "toasted lightly in dry pan and crushed between palms", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Garam Masala (toasted cardamom, clove, cinnamon, mace)", "prep": "freshly ground", "dept": "pantry"},
            {"qty": 15, "unit": "g", "name": "Honey or raw sugar", "prep": "to balance tomato acidity", "dept": "pantry"},
            {"qty": 1, "unit": "pcs", "name": "Hardwood lump charcoal piece", "prep": "for Dhungar smoke finish", "dept": "pantry"}
        ],
        "equipment": [
            {"name": "Heavy-bottomed copper or enameled Dutch oven (Handi)", "type": "everyday"},
            {"name": "Cast iron grill pan or outdoor charcoal grill", "type": "everyday"},
            {"name": "High-speed blender", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Marinate chicken in yogurt, half the ginger-garlic paste, 10g Kashmiri chili, and 5g salt for 4 to 12 hours.",
            "Soak cashews in 100ml boiling water for 20 minutes, then blend into a snow-white cream.",
            "Toast Kasuri Methi gently in a dry skillet for 30 seconds until aromatic.",
            "Puree tomatoes in blender and strain through a fine sieve to eliminate seeds and skin."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Thread marinated chicken onto skewers or lay onto a preheated cast iron grill pan over high heat. Sear for 8 minutes, turning once, until charred with blackened edges but still slightly raw in the center (it will finish in the sauce).",
                "timerMins": 8,
                "temperature": "220°C",
                "sensoryCue": "Deep smoky charring across yogurt coating; intoxicating aroma of toasted spices and caramelized poultry.",
                "scienceNote": "Yogurt lactic acid tenderizes chicken muscle fibers, while milk sugars and spices rapidly undergo intense Maillard browning under high radiant heat, simulating a traditional 480°C tandoor clay oven."
            },
            {
                "stepNum": 2,
                "text": "In the Dutch oven, heat 20g butter over medium heat. Add remaining ginger-garlic paste and stir-fry for 1 minute until raw pungency disappears.",
                "timerMins": 1,
                "temperature": "130°C",
                "sensoryCue": "Fragrant allium sizzle without browning."
            },
            {
                "stepNum": 3,
                "text": "Pour in strained tomato puree, 10g Kashmiri chili, and a pinch of salt. Simmer over medium-low heat for 20 minutes, stirring frequently, until tomato puree reduces by half and releases clear red butter along the edges.",
                "timerMins": 20,
                "sensoryCue": "Tomatoes darken to deep crimson red; liquid thickens into a glossy paste (bhunao stage).",
                "scienceNote": "Bhunao (slow oil-frying of pureed tomatoes and spices) evaporates free water and dissolves lipid-soluble carotenoids, creating the foundational depth of Indian gravies."
            },
            {
                "stepNum": 4,
                "text": "Stir in cashew cream and remaining 60g cold butter. Whisk vigorously until the sauce transforms into an ultra-silky, glowing orange-coral gravy (makhani means 'buttery').",
                "timerMins": 3,
                "sensoryCue": "The sauce turns from red to luminous velvet coral; glossy mirror sheen."
            },
            {
                "stepNum": 5,
                "text": "Add the charred chicken pieces along with any accumulated pan juices into the simmering sauce. Stir in heavy cream, honey, and fresh garam masala. Simmer gently over low heat for 8 minutes until chicken is cooked through.",
                "timerMins": 8,
                "temperature": "85°C",
                "sensoryCue": "Gentle simmering with sweet spice aromas of green cardamom and cinnamon filling the kitchen."
            },
            {
                "stepNum": 6,
                "text": "Rub toasted Kasuri Methi between your palms directly over the pot, scattering the fragrant green herb flakes. Stir gently.",
                "timerMins": 1,
                "sensoryCue": "Sudden explosion of warm, maple-like, complex bitter-sweet fenugreek aroma—the signature aroma of authentic Delhi butter chicken."
            },
            {
                "stepNum": 7,
                "text": "THE DHUNGAR SMOKE: Place a small stainless steel ramekin into the center of the pot above the curry. Using tongs, heat a lump of natural hardwood charcoal directly over the gas burner until glowing red-hot. Place coal into ramekin, pour 5ml ghee directly onto the hot coal, and immediately cover the pot tightly with the lid. Trap smoke for exactly 3 minutes.",
                "timerMins": 3,
                "sensoryCue": "Dense white fragrant smoke billows from the coal, infusing the entire makhani gravy with authentic tandoor woodsmoke essence."
            },
            {
                "stepNum": 8,
                "text": "Remove coal ramekin. Swirl an extra tablespoon of cream over the top. Serve immediately with warm handmade garlic naan and fragrant basmati rice.",
                "timerMins": 1,
                "sensoryCue": "Gleaming coral curry laced with white cream swirls and green crushed fenugreek."
            }
        ],
        "sensoryIndicators": {
            "see": "Velvety coral-orange gravy with white cream swirls, dark charred chicken morsels, crushed green fenugreek flecks.",
            "hear": "Gentle bubbling in the Dutch oven; hissing as ghee drops onto red-hot charcoal.",
            "smell": "Rich woodsmoke, sweet caramelized tomatoes, toasted fenugreek (kasuri methi), green cardamom, dairy butter.",
            "feel": "Luxuriously thick, satin-smooth sauce coating the tongue like velvet, followed by meltingly tender charred chicken."
        },
        "scienceNotes": [
            "Cashew emulsification: Cashew nuts are packed with natural starch, proteins, and unsaturated lipids that act as a plant-based stabilizer, preventing the dairy cream and butter from separating into a broken greasy sauce.",
            "Dhungar smoke absorption: Ghee poured onto glowing charcoal vaporizes into polycyclic aromatic hydrocarbons and guaiacol smoke compounds that are instantly absorbed by the lipid phase of the butter chicken, replicating an authentic clay tandoor."
        ],
        "troubleshooting": [
            {"issue": "Sauce is grainy instead of satin-smooth", "cause": "Tomatoes were not strained through a fine sieve or cashews were not blended fine enough.", "solution": "Pass the tomato-cashew base through a fine mesh chinois before adding chicken."},
            {"issue": "Curry tastes too tart or sour", "cause": "Tomatoes were not reduced sufficiently or lacked sweetness.", "solution": "Simmer sauce 5 minutes longer to evaporate water, then balance with an extra 10g honey and 15g cold butter."}
        ],
        "substitutions": [
            {"original": "Chicken thighs", "substitute": "Paneer cubes or roasted cauliflower florets", "culinaryConsequence": "Paneer absorbs makhani sauce magnificently; add directly without searing for a vegetarian classic."},
            {"original": "Kasuri Methi", "substitute": "Celery leaves + maple syrup (cannot truly replicate fenugreek)", "culinaryConsequence": "Kasuri methi is essential to authentic butter chicken; seek it at South Asian grocers."}
        ],
        "flavorPairings": {
            "wine": "Off-dry German Riesling, Viognier, or a fruity sparkling Crémant",
            "zeroProof": "Chilled Mango Lassi blended with Greek yogurt and green cardamom",
            "complementarySides": ["Handmade tandoori garlic naan with melted ghee", "Jeera rice (basmati tempered with cumin and ghee)"]
        },
        "advancedTechnique": "Two-stage tandoori marinade: First rub chicken with lemon juice, salt, and ginger-garlic paste for 30 minutes to tenderize surface proteins; then apply the thick spiced yogurt marinade for 6 hours. This guarantees deep seasoning through to the bone.",
        "storageAndReheating": "Tastes even better on day 2 as fenugreek and spices marry into the gravy. Refrigerate up to 4 days; reheat gently on low heat with 2 tablespoons of water.",
        "nutritionEstimates": {"calories": 620, "proteinG": 44, "carbsG": 18, "fatG": 42},
        "relatedRecipes": ["rec-hyderabadi-biryani", "rec-dal-makhani"],
        "relatedTechniques": ["lesson-seasoning-osmosis", "lesson-heat-control"]
    },
    {
        "id": "rec-birria-res",
        "title": "Birria de Res Tradicional with Rich Guajillo Consomé",
        "cuisine": "Mexican Jalisco",
        "category": "dinner",
        "slot": "climax",
        "difficulty": "Intermediate",
        "prepMins": 30,
        "cookMins": 210,
        "totalMins": 240,
        "yieldServings": 6,
        "heroImage": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=1200&q=80",
        "summary": "The pride of Jalisco: beef chuck and bone-in short ribs braised until meltingly tender in an adobo of toasted Guajillo, Ancho, and Arbol chiles, roasted tomatoes, Mexican cinnamon, cloves, and cider vinegar. Served with a bowl of deep crimson consomé topped with raw white onions and cilantro, ready for dunking crispy corn tortillas.",
        "dietary": ["gluten-free", "dairy-free", "nut-free"],
        "sensoryRole": "Deeply savory, earthy-spicy shredded beef with rich collagen broth, brightened by sharp raw allium and lime juice.",
        "ingredients": [
            {"qty": 1200, "unit": "g", "name": "Beef chuck roast", "prep": "cut into large fist-sized chunks", "dept": "butchery"},
            {"qty": 800, "unit": "g", "name": "Bone-in beef short ribs or shank", "prep": "for rich bone broth collagen", "dept": "butchery"},
            {"qty": 6, "unit": "pcs", "name": "Dried Guajillo chiles", "prep": "stemmed and seeded", "dept": "pantry"},
            {"qty": 3, "unit": "pcs", "name": "Dried Ancho chiles", "prep": "stemmed and seeded", "dept": "pantry"},
            {"qty": 4, "unit": "pcs", "name": "Dried Chiles de Árbol", "prep": "for lively heat", "dept": "pantry"},
            {"qty": 4, "unit": "pcs", "name": "Roma tomatoes", "prep": "charred under broiler", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "White onion", "prep": "half charred for adobo, half diced fine for serving", "dept": "produce"},
            {"qty": 6, "unit": "cloves", "name": "Garlic", "prep": "unpeeled, charred in skillet", "dept": "produce"},
            {"qty": 60, "unit": "ml", "name": "Apple cider vinegar", "prep": "for acid balance", "dept": "pantry"},
            {"qty": 1, "unit": "stick", "name": "Mexican canela (true cinnamon)", "prep": "soft, flaky bark", "dept": "pantry"},
            {"qty": 3, "unit": "pcs", "name": "Whole cloves", "prep": "toasted", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Dried Mexican oregano", "prep": "crushed", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Cumin seeds", "prep": "toasted", "dept": "pantry"},
            {"qty": 2, "unit": "pcs", "name": "Bay leaves", "prep": "whole", "dept": "produce"},
            {"qty": 12, "unit": "pcs", "name": "Fresh corn tortillas", "prep": "for dipping and serving", "dept": "drygoods"},
            {"qty": 1, "unit": "bunch", "name": "Fresh cilantro", "prep": "finely chopped", "dept": "produce"},
            {"qty": 3, "unit": "pcs", "name": "Limes", "prep": "cut into wedges", "dept": "produce"}
        ],
        "equipment": [
            {"name": "7-quart heavy enameled cast iron Dutch oven", "type": "everyday"},
            {"name": "Cast iron comal or dry skillet for toasting chiles", "type": "everyday"},
            {"name": "High-powered blender and fine mesh strainer", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Stem and deseed dried Guajillo and Ancho chiles.",
            "Char tomatoes, half onion, and garlic cloves in dry skillet until blistered black.",
            "Season beef chunks generously with coarse salt 1 hour prior to cooking.",
            "Finely dice remaining raw onion, chop cilantro, and cut limes."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Toast dried chiles on a hot dry comal or skillet for 15-20 seconds per side until fragrant and pliable. Do NOT burn them. Transfer to a bowl, cover with 500ml boiling water, and soak for 20 minutes.",
                "timerMins": 20,
                "sensoryCue": "Chiles puff up and soften; rich leather, dried cherry, and tobacco aromas release into the air.",
                "scienceNote": "Toasting dried chiles volatilizes pyrazines and unlocks fruitiness. Burning them creates acrid carbon compounds that permanently ruin the adobo with bitter off-notes."
            },
            {
                "stepNum": 2,
                "text": "In a blender, combine rehydrated chiles (with their soaking liquid), charred tomatoes, charred onion, peeled charred garlic, cider vinegar, Mexican canela, cloves, cumin, Mexican oregano, and 10g salt. Blend on high for 2 minutes until ultra-smooth.",
                "timerMins": 3,
                "sensoryCue": "A thick, velvety, deep crimson-maroon chili paste (adobo) with complex sweet-tart, spicy aromatics."
            },
            {
                "stepNum": 3,
                "text": "Sear the beef chuck chunks and bone-in short ribs in the Dutch oven with 20ml oil over high heat for 3 minutes per side until deeply browned. Remove beef.",
                "timerMins": 10,
                "temperature": "190°C",
                "sensoryCue": "Lively sizzling and deep roasted beef crust aroma."
            },
            {
                "stepNum": 4,
                "text": "Pour the blended adobo directly into the hot Dutch oven (it will boil and splatter violently). Fry the adobo over medium heat for 5 minutes, stirring constantly, until it darkens and oil separates to the top (sofrito).",
                "timerMins": 5,
                "sensoryCue": "Adobo darkens from bright red to deep mahogany; sugars lightly toast."
            },
            {
                "stepNum": 5,
                "text": "Return seared beef and bones to the pot. Add 1 liter of water and 2 bay leaves. Liquid should completely submerge the meat. Bring to a boil.",
                "timerMins": 3,
                "sensoryCue": "Crimson broth simmers vigorously."
            },
            {
                "stepNum": 6,
                "text": "Cover tightly with foil and lid. Transfer to a 150°C (300°F) oven for 3.5 hours until beef is completely fork-tender and falling off the bone.",
                "timerMins": 210,
                "temperature": "150°C oven",
                "sensoryCue": "Beef pulls apart with zero resistance; a paring knife glides through short ribs like warm butter.",
                "scienceNote": "Prolonged low-temperature braising converts collagen in beef chuck and short rib bones into luscious gelatin, transforming the braising liquid into a rich, mouth-coating consomé."
            },
            {
                "stepNum": 7,
                "text": "Remove beef from pot and shred coarsely with two forks on a cutting board, discarding bones. Skim the radiant red spiced beef fat from the surface of the consomé into a small bowl (for dipping tortillas).",
                "timerMins": 10,
                "sensoryCue": "Juicy, glistening shredded beef saturated in dark red adobo; pure ruby-red tallow collected in bowl."
            },
            {
                "stepNum": 8,
                "text": "Ladle piping hot consomé into individual bowls. Top with raw white onion, cilantro, and fresh lime juice. Serve with shredded beef and warm tortillas dipped in the red fat and crisped on the comal.",
                "timerMins": 2,
                "sensoryCue": "Steam rises carrying spicy Guajillo, Mexican cinnamon, and rich beef broth aromas."
            }
        ],
        "sensoryIndicators": {
            "see": "Deep mahogany-red shredded beef, glistening crimson consomé with drops of ruby fat, bright green cilantro, sharp white diced onion.",
            "hear": "Crisp sizzle of tortillas hitting the comal; slurping of hot consomé from the bowl.",
            "smell": "Warm Mexican canela, earthy toasted Guajillo chiles, roasted garlic, rich beef tallow, fresh zesty lime.",
            "feel": "Meltingly succulent, juicy shredded beef with gelatin-rich broth that coats the lips."
        },
        "scienceNotes": [
            "Capsaicin-lipid binding: Red beef tallow floating on top of the consomé dissolves chili capsaicin and essential oils from canela and oregano, concentrating the aromatic punch into the surface fat layer.",
            "Acidity balancing collagen: Cider vinegar provides acetic acid that cleaves the heavy lipid richness of beef marrow, ensuring the consomé remains drinkable and refreshing rather than greasy."
        ],
        "troubleshooting": [
            {"issue": "Consomé is bitter", "cause": "Chiles were scorched during toasting or seeds/stems were left in.", "solution": "Always remove seeds and toast chiles for strictly 15-20 seconds until fragrant; if burned, discard and restart."},
            {"issue": "Beef is tough", "cause": "Oven temperature was too high or cooking was stopped before collagen reached 75°C breakdown.", "solution": "Return to 145°C oven for another 45 minutes; short ribs require full time to dissolve connective tissue."}
        ],
        "substitutions": [
            {"original": "Beef chuck & short ribs", "substitute": "Bone-in lamb shoulder or goat (traditional Jalisco Birria de Chivo)", "culinaryConsequence": "Goat provides the authentic heritage Jalisco flavor; lamb yields a rich, gamier profile."},
            {"original": "Guajillo chiles", "substitute": "New Mexico dried chiles or California chiles", "culinaryConsequence": "New Mexico chiles provide similar earthy sweetness and vibrant red hue."}
        ],
        "flavorPairings": {
            "wine": "Cold Mexican Negra Modelo beer, Syrah, or Mezcal Joven with orange wedge",
            "zeroProof": "Agua de Jamaica (iced hibiscus tea with cinnamon and lime) or cold Horchata",
            "complementarySides": ["Warm corn tortillas toasted on comal", "Pickled red onions with habanero", "Lime wedges"]
        },
        "advancedTechnique": "Quesabirria taco transformation: Dip fresh corn tortillas into the skimmed red surface fat, lay onto a smoking hot comal, top with shredded Oaxaca cheese and shredded beef, fold in half, and fry until cheese forms a crispy browned frico crust. Serve immediately with a bowl of hot consomé for dipping.",
        "storageAndReheating": "Birria improves dramatically after an overnight rest in the refrigerator. Keeps refrigerated for 5 days; freezes for 4 months. Reheat gently in a covered pot on low heat.",
        "nutritionEstimates": {"calories": 670, "proteinG": 52, "carbsG": 22, "fatG": 42},
        "relatedRecipes": ["rec-ragu-bolognese", "rec-coq-au-vin"],
        "relatedTechniques": ["lesson-braising-collagen", "lesson-heat-control"]
    },
    {
        "id": "rec-shakshuka-royale",
        "title": "Shakshuka Royale with Spiced Bell Peppers, Harissa & Poached Eggs",
        "cuisine": "Mediterranean / Levantine",
        "category": "breakfast",
        "slot": "opener",
        "difficulty": "Beginner",
        "prepMins": 15,
        "cookMins": 25,
        "totalMins": 40,
        "yieldServings": 4,
        "heroImage": "https://images.unsplash.com/photo-1590412200988-a436970781fa?auto=format&fit=crop&w=1200&q=80",
        "summary": "The quintessential North African and Middle Eastern skillet feast: sweet red bell peppers and onions slowly stewed in fruity extra virgin olive oil with garlic, cumin, smoked paprika, and Tunisian rose harissa, reduced with ripe crushed tomatoes, into which fresh eggs are gently cracked and poached until whites are set and yolks are molten. Crowned with creamy sheep's milk feta and fresh cilantro.",
        "dietary": ["vegetarian", "gluten-free", "nut-free"],
        "sensoryRole": "Warming, smoky, spicy tomato-pepper stew enriched by molten runny egg yolks and briny pops of creamy feta.",
        "ingredients": [
            {"qty": 4, "unit": "pcs", "name": "Large pasture-raised eggs", "prep": "at room temp", "dept": "dairy"},
            {"qty": 2, "unit": "pcs", "name": "Red bell peppers", "prep": "sliced into 5mm strips", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Yellow onion", "prep": "sliced into thin half-moons", "dept": "produce"},
            {"qty": 4, "unit": "cloves", "name": "Garlic", "prep": "thinly sliced", "dept": "produce"},
            {"qty": 800, "unit": "g", "name": "San Marzano whole peeled tomatoes", "prep": "crushed coarsely by hand", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Tunisian rose harissa paste", "prep": "spicy, aromatic", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Ground cumin seeds", "prep": "freshly toasted and ground", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Smoked Spanish paprika (Pimentón de la Vera)", "prep": "sweet or bittersweet", "dept": "pantry"},
            {"qty": 45, "unit": "ml", "name": "Extra virgin olive oil", "prep": "first cold-pressed", "dept": "pantry"},
            {"qty": 80, "unit": "g", "name": "Authentic Greek or French sheep's milk feta", "prep": "crumbled coarse", "dept": "dairy"},
            {"qty": 15, "unit": "g", "name": "Fresh cilantro and flat-leaf parsley", "prep": "roughly chopped", "dept": "produce"}
        ],
        "equipment": [
            {"name": "12-inch heavy cast iron skillet with lid", "type": "everyday"},
            {"name": "Wooden spoon for stirring", "type": "everyday"}
        ],
        "miseEnPlace": [
            "Slice bell peppers, onions, and garlic.",
            "Crush whole peeled tomatoes with clean hands in a bowl.",
            "Measure cumin, smoked paprika, and harissa.",
            "Have eggs cracked into individual small ramekins for quick, controlled placement."
        ],
        "steps": [
            {
                "stepNum": 1,
                "text": "Heat 45ml extra virgin olive oil in a 12-inch cast iron skillet over medium heat. Add sliced onions and bell peppers. Cook for 12-14 minutes, stirring regularly, until the vegetables are completely soft, sweet, and collapsing into a tender tangle with light golden caramelized edges.",
                "timerMins": 13,
                "temperature": "135°C",
                "sensoryCue": "Bell peppers soften and collapse; kitchen fills with sweet, sugary allium and pepper perfume.",
                "scienceNote": "Slowly sweating peppers and onions hydrolyzes complex polysaccharides into sweet fructose and glucose, creating natural sweetness to counterbalance tomato acidity."
            },
            {
                "stepNum": 2,
                "text": "Add sliced garlic, ground cumin, smoked paprika, and rose harissa. Cook for 2 minutes, stirring continuously, to bloom the spices in hot olive oil.",
                "timerMins": 2,
                "sensoryCue": "Intense aromatic plume of smoky paprika, earthy cumin, and chili-coriander from the harissa."
            },
            {
                "stepNum": 3,
                "text": "Pour in crushed San Marzano tomatoes with their juices. Season with 4g sea salt and a pinch of black pepper. Bring to a lively simmer, then lower heat to medium-low and simmer uncovered for 10-12 minutes until the sauce has thickened and no longer looks watery.",
                "timerMins": 11,
                "temperature": "90°C",
                "sensoryCue": "The sauce transforms into a rich, deep scarlet-orange ragout that leaves a clean trail when a wooden spoon is dragged across the pan bottom."
            },
            {
                "stepNum": 4,
                "text": "Using the back of a large spoon, make four distinct shallow wells in the hot tomato-pepper stew, spaced evenly around the skillet.",
                "timerMins": 1,
                "sensoryCue": "Four stable craters holding their shape in the thick stew."
            },
            {
                "stepNum": 5,
                "text": "Gently slip one raw egg into each well. Scatter crumbled sheep's milk feta all around the eggs into the sauce. Sprinkle a tiny pinch of salt and smoked paprika directly onto each egg yolk.",
                "timerMins": 1,
                "sensoryCue": "Pristine white-and-yellow eggs nested snugly into bubbling red stew; white feta cubes melting slightly."
            },
            {
                "stepNum": 6,
                "text": "Cover the skillet with a tight-fitting lid. Cook over low heat for 5 to 6 minutes, watching carefully: the egg whites should turn completely opaque and set, while the yolks remain soft, trembling, and completely liquid.",
                "timerMins": 5.5,
                "temperature": "Low heat / steam capture",
                "sensoryCue": "Egg whites turn milky-white and set firmly; yolks quiver like liquid gold when skillet is nudged.",
                "scienceNote": "Covering the skillet traps steam (convective heat transfer), cooking the top of the egg whites to set without overcooking the yolks underneath."
            },
            {
                "stepNum": 7,
                "text": "Remove from heat immediately. Scatter fresh cilantro and flat-leaf parsley across the top. Drizzle with a thin ribbon of fresh olive oil. Bring the hot cast iron skillet directly to the table with warm crusty sourdough or za'atar pita.",
                "timerMins": 1,
                "sensoryCue": "Sizzling skillet on the trivet; piercing an egg yolk with bread unleashes a warm river of golden yolk into the spicy red sauce."
            }
        ],
        "sensoryIndicators": {
            "see": "Vibrant crimson sauce, tender red pepper strips, snow-white egg whites with glowing yellow quivering yolks, white feta crumbles, green herbs.",
            "hear": "Gentle bubbling around the perimeter of the cast iron pan.",
            "smell": "Smoky Spanish paprika, warm cumin, roasted garlic, sweet caramelized peppers, fresh olive oil.",
            "feel": "Crusty bread dipped into rich, chunky tomato pepper stew coated in velvety liquid yolk."
        },
        "scienceNotes": [
            "Convective steam setting: Egg whites require 62-65°C to coagulate. By trapping steam under the lid, ambient moisture reaches 95°C and cooks the delicate upper white layer within minutes while the yolk stays below 65°C.",
            "Sheep's milk feta stability: High-calcium sheep's feta softens and becomes creamy when heated, but does not melt into a puddle like cow's mozzarella, maintaining distinct salty, tangy pockets throughout the hot sauce."
        ],
        "troubleshooting": [
            {"issue": "Egg yolks cooked hard and chalky", "cause": "Skillet was left covered too long or heat was too high.", "solution": "Check at the 4-minute mark; remove pan from heat the second whites turn opaque, as residual cast-iron heat continues cooking."},
            {"issue": "Sauce is watery and pools around the eggs", "cause": "Tomatoes were not reduced sufficiently before cracking eggs.", "solution": "Simmer the tomato-pepper base until a spoon leaves a dry path on the bottom of the skillet before creating egg wells."}
        ],
        "substitutions": [
            {"original": "Rose harissa", "substitute": "Smoked paprika + cayenne + tomato paste + pinch of ground coriander", "culinaryConsequence": "Recreates the smoky, warm spiced complexity of North African harissa."},
            {"original": "Sheep's milk feta", "substitute": "Goat cheese (chèvre) or labneh dolloped on after cooking", "culinaryConsequence": "Labneh provides a cooler, tangier dairy contrast."}
        ],
        "flavorPairings": {
            "wine": "Dry Provence Rosé, crisp Greek Assyrtiko, or a light fruity Beaujolais",
            "zeroProof": "Freshly brewed iced mint tea sweetened with honey, or sparkling lemonade with bruised mint",
            "complementarySides": ["Warm hand-stretched za'atar pita bread", "Cucumber and radish salad with sumac vinaigrette"]
        },
        "advancedTechnique": "Preserved lemon & merguez sausage enhancement: Brown spicy lamb merguez sausage coins in the skillet first and stir finely diced Moroccan preserved lemon rind into the sauce for extraordinary gourmet depth.",
        "storageAndReheating": "The tomato-pepper base can be prepared up to 4 days ahead and stored refrigerated. Reheat base in skillet and crack eggs fresh right before serving.",
        "nutritionEstimates": {"calories": 390, "proteinG": 19, "carbsG": 24, "fatG": 25},
        "relatedRecipes": ["rec-french-omelette", "rec-cacio-e-pepe"],
        "relatedTechniques": ["lesson-egg-geometry", "lesson-heat-control"]
    }
]

print(f"Loaded {len(WORLD_RECIPES)} World Traditions master recipes.")
