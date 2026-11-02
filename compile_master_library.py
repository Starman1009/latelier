# -*- coding: utf-8 -*-
"""
Full Master Recipe Builder for L'Atelier Culinary Platform.
Generates 105+ complete, gourmet, scientifically documented, fully-cookable recipes.
Outputs:
- data-recipes.js
- recipes_master.json
"""

import json
import os
import sys

from catalog_french import FRENCH_RECIPES
from catalog_italian import ITALIAN_RECIPES
from catalog_asian import ASIAN_RECIPES
from catalog_world_traditions import WORLD_RECIPES

ALL_RECIPES = list(FRENCH_RECIPES) + list(ITALIAN_RECIPES) + list(ASIAN_RECIPES) + list(WORLD_RECIPES)

def build_recipe(
    r_id, title, cuisine, category, slot, difficulty,
    prep_mins, cook_mins, servings, hero_img, summary,
    dietary, sensory_role, ingredients, equipment,
    mise_en_place, steps, sensory_indicators,
    science_notes, troubleshooting, substitutions,
    flavor_pairings, storage, nutrition,
    advanced_technique=None, related_recipes=None, related_techniques=None
):
    total_mins = prep_mins + cook_mins
    return {
        "id": r_id,
        "title": title,
        "cuisine": cuisine,
        "category": category,
        "slot": slot,
        "difficulty": difficulty,
        "prepMins": prep_mins,
        "cookMins": cook_mins,
        "totalMins": total_mins,
        "yieldServings": servings,
        "heroImage": hero_img,
        "summary": summary,
        "dietary": dietary,
        "sensoryRole": sensory_role,
        "ingredients": ingredients,
        "equipment": equipment,
        "miseEnPlace": mise_en_place,
        "steps": steps,
        "sensoryIndicators": sensory_indicators,
        "scienceNotes": science_notes,
        "troubleshooting": troubleshooting,
        "substitutions": substitutions,
        "flavorPairings": flavor_pairings,
        "advancedTechnique": advanced_technique,
        "storageAndReheating": storage,
        "nutritionEstimates": nutrition,
        "relatedRecipes": related_recipes or [],
        "relatedTechniques": related_techniques or []
    }

# Additional Master Recipes
ADDITIONAL_RECIPES = [
    # 1. Eggs Benedict
    build_recipe(
        "rec-eggs-benedict", "Classic Eggs Benedict with Velvety Hollandaise",
        "American / French Brunch", "breakfast", "opener", "Intermediate", 15, 15, 2,
        "https://images.unsplash.com/photo-1608039829572-78524f79c4c7?auto=format&fit=crop&w=1200&q=80",
        "Toasted English muffin halves topped with thick-cut Canadian bacon, gently poached eggs with molten running yolks, and blanketed in warm, lemony, buttery Sauce Hollandaise.",
        ["nut-free"], "Rich, buttery citrus emulsion flowing over tender poached egg and smoky pork onto a toasted, crunchy crumb.",
        [
            {"qty": 4, "unit": "pcs", "name": "Grade-AA large eggs", "prep": "cold from the fridge", "dept": "dairy"},
            {"qty": 4, "unit": "slices", "name": "Thick-cut Canadian bacon or artisanal ham", "prep": "pan-seared", "dept": "butchery"},
            {"qty": 2, "unit": "pcs", "name": "English muffins", "prep": "split with a fork and toasted crisp", "dept": "drygoods"},
            {"qty": 3, "unit": "pcs", "name": "Large egg yolks", "prep": "for Hollandaise", "dept": "dairy"},
            {"qty": 150, "unit": "g", "name": "Clarified butter", "prep": "warm (60°C)", "dept": "dairy"},
            {"qty": 20, "unit": "ml", "name": "Fresh lemon juice", "prep": "strained", "dept": "produce"},
            {"qty": 15, "unit": "ml", "name": "Distilled white vinegar", "prep": "for poaching water", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Fresh chives", "prep": "minced fine for garnish", "dept": "produce"},
            {"qty": 1, "unit": "pinch", "name": "Cayenne pepper", "prep": "in sauce", "dept": "pantry"}
        ],
        [
            {"name": "Deep skillet or wide saucepan for poaching", "type": "everyday"},
            {"name": "Heatproof glass or copper bowl for Hollandaise", "type": "everyday"},
            {"name": "Fine wire balloon whisk and slotted spoon", "type": "everyday"}
        ],
        [
            "Crack each egg into an individual fine-mesh strainer over a bowl to drain watery outer albumen.",
            "Bring 3 inches of water with vinegar to a bare simmer (88°C).",
            "Melt clarified butter and keep warm at 60°C.",
            "Split English muffins with a fork to create nooks and crannies."
        ],
        [
            {"stepNum": 1, "text": "Prepare Hollandaise: Whisk 3 egg yolks, lemon juice, and 15ml water in a heatproof bowl over a double boiler of barely simmering water until pale, thick, and ribbon-like.", "timerMins": 4, "temperature": "60°C", "sensoryCue": "Whisk leaves distinct tracks through the thickened yolks."},
            {"stepNum": 2, "text": "Slowly drizzle in warm clarified butter in a thin, steady thread while whisking continuously until a thick, glossy, spoonable emulsion forms. Season with salt and cayenne. Keep warm at 55°C.", "timerMins": 4, "sensoryCue": "Sauce turns radiant golden yellow, coating the back of a spoon."},
            {"stepNum": 3, "text": "Poach eggs: Stir simmering water to create a gentle vortex. Slip eggs into the center one by one. Poach for 3 minutes until whites are completely set and yolks remain molten. Remove with slotted spoon to paper towels.", "timerMins": 3, "temperature": "88°C", "sensoryCue": "Egg whites wrap cleanly around yolk; gentle wobble when touched."},
            {"stepNum": 4, "text": "Brown Canadian bacon in a dry skillet for 1.5 minutes per side. Toast English muffins golden brown.", "timerMins": 3, "sensoryCue": "Bacon edges sizzle; muffins are deeply toasted."},
            {"stepNum": 5, "text": "Assemble: Place muffin halves cut-side up on warm plates. Top each with Canadian bacon, a poached egg, and a generous ladle of warm Hollandaise. Garnish with minced chives and serve immediately.", "timerMins": 1, "sensoryCue": "Hollandaise drapes luxuriously over the poached egg dome."}
        ],
        {"see": "Golden yellow Hollandaise cascading over white poached egg, toasted muffin, pink bacon, green chives.", "hear": "Crunch of English muffin under fork; silence of running yolk.", "smell": "Warm citrus butter, toasted bread, smoky ham.", "feel": "Crisp muffin yielding to velvety warm liquid yolk and thick buttery sauce."},
        ["Egg yolks contain lecithin, an amphiphilic phospholipid that binds water and butterfat droplets into a stable emulsion.", "Adding vinegar to poaching water lowers pH, speeding up egg white coagulation so it wraps tightly around the yolk rather than feathering into strands."],
        [{"issue": "Hollandaise separated into liquid butter and curd", "cause": "Butter was added too quickly or bowl became hotter than 68°C.", "solution": "Whisk 1 tablespoon boiling water into a clean bowl, then slowly whisk the broken sauce back in off heat."}],
        [{"original": "Canadian bacon", "substitute": "Smoked salmon (Eggs Royale) or buttered sautéed spinach (Eggs Florentine)", "culinaryConsequence": "Salmon provides luxurious omega-3 richness; spinach provides earthy vegetal contrast."}],
        {"wine": "Champagne Brut or dry Prosecco Superiore", "zeroProof": "Fresh cold-pressed blood orange juice with sparkling mineral water", "complementarySides": ["Crispy skillet home fries with rosemary"]},
        "Clarified butter temperature precision: Keep butter strictly between 55°C and 62°C when emulsifying; cold butter hardens, while boiling butter curdles yolk protein.",
        "Eat immediately. Hollandaise cannot be refrigerated and reheated safely.",
        {"calories": 620, "proteinG": 28, "carbsG": 32, "fatG": 44},
        ["rec-french-omelette", "rec-salmon-cornets"], ["lesson-egg-geometry", "lesson-mother-sauces"]
    ),

    # 2. Neapolitan Pizza Margherita
    build_recipe(
        "rec-pizza-margherita", "Neapolitan Pizza Margherita DOC (48-Hour Cold Fermentation)",
        "Italian Campanian", "dinner", "climax", "Intermediate", 30, 8, 4,
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=1200&q=80",
        "The authentic Vera Pizza Napoletana: 65% hydration dough made with Italian Tipo 00 flour, cold-fermented for 48 hours for extraordinary digestibility and blistered cornicione leopard-spotting. Topped with hand-crushed San Marzano tomatoes, fresh Fior di Latte mozzarella, fragrant basil leaves, and peppery extra virgin olive oil.",
        ["vegetarian", "nut-free"], "Charred, smoky, pillowy crust with sweet-acidic raw tomato, milky melted mozzarella, and fresh peppery basil.",
        [
            {"qty": 500, "unit": "g", "name": "Italian Tipo 00 wheat flour (Caputo Pizzeria)", "prep": "high protein (12.5%)", "dept": "drygoods"},
            {"qty": 325, "unit": "ml", "name": "Cold filtered water (65% hydration)", "prep": "18°C", "dept": "pantry"},
            {"qty": 14, "unit": "g", "name": "Fine sea salt (2.8%)", "prep": "dissolved in water", "dept": "pantry"},
            {"qty": 1.5, "unit": "g", "name": "Fresh brewer's yeast or 0.5g active dry yeast", "prep": "bloomed", "dept": "pantry"},
            {"qty": 350, "unit": "g", "name": "San Marzano DOP canned whole tomatoes", "prep": "crushed by hand with 3g salt", "dept": "pantry"},
            {"qty": 250, "unit": "g", "name": "Fresh Fior di Latte or Mozzarella di Bufala Campana DOP", "prep": "sliced, drained on paper towels 2 hours", "dept": "dairy"},
            {"qty": 15, "unit": "leaves", "name": "Fresh Genovese basil", "prep": "whole leaves", "dept": "produce"},
            {"qty": 30, "unit": "ml", "name": "Extra virgin olive oil", "prep": "for finishing spiral", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Parmigiano-Reggiano DOP", "prep": "freshly grated", "dept": "dairy"}
        ],
        [
            {"name": "Pizza steel or heavy cordierite pizza stone (1/4 or 3/8 inch thick)", "type": "everyday"},
            {"name": "Wooden pizza peel and perforated aluminum turning peel", "type": "everyday"},
            {"name": "Dough proofing container with lid", "type": "everyday"}
        ],
        [
            "Knead dough, bulk ferment 2 hours at room temp, shape into 250g dough balls, and cold ferment in refrigerator for 48 hours.",
            "Remove dough balls from fridge 2 hours before baking to reach room temperature (20°C).",
            "Preheat oven with pizza steel on the highest rack at 260°C (500°F) or 290°C (550°F) for at least 60 minutes.",
            "Drain sliced mozzarella thoroughly; wet cheese creates a soggy pizza lake."
        ],
        [
            {"stepNum": 1, "text": "Dough shaping: Dust dough ball in semolina. Using fingertips, press gently from the center outward to push trapped CO2 gas into the outer rim, leaving a raised 2cm border (cornicione). Never use a rolling pin.", "timerMins": 2, "sensoryCue": "Dough expands into a supple, translucent 12-inch disc with puffed airy edges."},
            {"stepNum": 2, "text": "Sauce: Spread 75g hand-crushed San Marzano tomatoes in a thin, circular spiral starting from center outward, leaving the cornicione bare.", "timerMins": 1, "sensoryCue": "Vibrant red sauce coats the pale dough evenly."},
            {"stepNum": 3, "text": "Cheese & herbs: Scatter 60g drained mozzarella and 3 fresh basil leaves across the sauce. Dust with a tablespoon of grated Parmigiano-Reggiano and drizzle with extra virgin olive oil in a figure-six motion.", "timerMins": 1, "sensoryCue": "Classic Italian tricolore: red tomato, white mozzarella, green basil."},
            {"stepNum": 4, "text": "Bake: Slide pizza off the wooden peel directly onto the scorching pizza steel. Bake for 5 to 6 minutes, switching oven to HIGH BROILER for the final 2 minutes, until the cornicione puffs into airy blisters with dark charred leopard spots.", "timerMins": 6, "temperature": "Broiler / 290°C steel", "sensoryCue": "Crust balloons dramatically; bubbling mozzarella blisters golden; smoky wood-oven aroma fills the kitchen."},
            {"stepNum": 5, "text": "Remove with peel. Top with fresh raw basil leaves and a final swirl of raw olive oil. Slice and eat immediately while crust crackles.", "timerMins": 1, "sensoryCue": "Audible crunch when sliced; soft, light, airy honeycomb interior crumb."}
        ],
        {"see": "Blistered cornicione with dark leopard spots, molten milky mozzarella, crimson tomato sauce, fresh bright green basil.", "hear": "Shattering crisp crunch as the crust is cut, followed by airy yielding silence.", "smell": "Charred fermented wheat, sweet volcanic tomato, creamy milk, pungent aromatic basil.", "feel": "Crisp exterior with an extraordinarily light, pillowy, cloud-like interior crumb."},
        ["Long 48-hour cold fermentation allows fungal and bacterial enzymes (amylases and proteases) to break down complex starches into simple sugars and gluten into smaller peptides, creating complex flavor and dramatic blistered leopard spotting (canotto).", "Baking on high-thermal-mass pizza steel transfers heat 18 times faster than ceramic stones, achieving explosive oven spring."],
        [{"issue": "Crust is pale and tough like cardboard", "cause": "Baking surface was not preheated long enough, or dough was rolled with a rolling pin.", "solution": "Preheat pizza steel for at least 60 minutes and stretch dough gently by hand only to preserve gas bubbles."}],
        [{"original": "Tipo 00 flour", "substitute": "High-protein bread flour (12.7% protein)", "culinaryConsequence": "Produces excellent chew and structure; requires slightly higher water absorption (67%)."}],
        {"wine": "Campanian Greco di Tufo, Aglianico, or a crisp Birra Moretti lager", "zeroProof": "Chilled sparkling San Pellegrino with a bruised sprig of fresh basil and lemon twist", "complementarySides": ["Insalata Caprese with heirloom tomatoes"]},
        "The Slap-and-Stretch (Schiaffo) technique: Neapolitan pizzaioli flip the dough rapidly between their palms and the marble counter, letting gravity and centrifugal force expand the disc without stretching out trapped gas bubbles.",
        "Best eaten within 3 minutes of pulling from the oven. Leftovers can be reheated on a dry cast iron skillet covered with a lid for 3 minutes to restore crispness.",
        {"calories": 780, "proteinG": 34, "carbsG": 104, "fatG": 24},
        ["rec-focaccia-genovese", "rec-ragu-bolognese"], ["lesson-dough-fermentation", "lesson-heat-control"]
    ),

    # 3. Traditional Tiramisù Classico
    build_recipe(
        "rec-tiramisu", "Traditional Tiramisù Classico (Treviso Style with Mascarpone Sabayon)",
        "Italian Veneto", "dessert", "dessert", "Intermediate", 30, 0, 8,
        "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=1200&q=80",
        "The authentic 1960s Treviso masterpiece: crisp Italian savoiardi ladyfingers soaked rapidly in dark espresso infused with Marsala wine, layered with a cloud-like sabayon cream of egg yolks, mascarpone, and whipped egg whites, dusted with an avalanche of bitter Dutch-process cocoa powder. Strictly zero gelatin, zero whipped cream, and zero liquor extracts.",
        ["vegetarian", "nut-free"], "Bitter, roasted espresso contrasting rich, velvety sweet mascarpone cream and airy, espresso-soaked biscuit crumb.",
        [
            {"qty": 500, "unit": "g", "name": "Italian Mascarpone cheese", "prep": "full-fat, chilled", "dept": "dairy"},
            {"qty": 4, "unit": "pcs", "name": "Large pasture-raised eggs", "prep": "separated into yolks and whites", "dept": "dairy"},
            {"qty": 100, "unit": "g", "name": "Granulated sugar", "prep": "divided: 70g for yolks, 30g for whites", "dept": "pantry"},
            {"qty": 300, "unit": "g", "name": "Italian Savoiardi ladyfinger biscuits", "prep": "crisp, sugary coating", "dept": "drygoods"},
            {"qty": 350, "unit": "ml", "name": "Freshly pulled dark espresso coffee", "prep": "cooled to room temperature", "dept": "beverage"},
            {"qty": 45, "unit": "ml", "name": "Dry Marsala Superiore or dark Jamaican rum", "prep": "for coffee soak", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Dutch-process unsweetened dark cocoa powder", "prep": "for heavy dusting", "dept": "pantry"},
            {"qty": 1, "unit": "g", "name": "Fine sea salt", "prep": "in egg whites", "dept": "pantry"}
        ],
        [
            {"name": "9x13 inch rectangular glass or ceramic baking dish", "type": "everyday"},
            {"name": "Electric hand mixer or stand mixer with balloon whisk", "type": "everyday"},
            {"name": "Fine wire mesh cocoa shaker/sieve", "type": "everyday"}
        ],
        [
            "Pull dark espresso and stir in Marsala wine; let cool to room temperature in a wide shallow dish.",
            "Separate eggs cleanly; egg whites must be entirely free of yolk fat.",
            "Bring mascarpone out of fridge 15 minutes before mixing so it incorporates smoothly without clumping."
        ],
        [
            {"stepNum": 1, "text": "Prepare yolk sabayon: Whisk egg yolks and 70g sugar in a bowl over a double boiler of simmering water for 5 minutes until pale, thick, and registering 65°C (safe pasteurization). Cool 5 minutes.", "timerMins": 5, "temperature": "65°C", "sensoryCue": "Yolks triple in volume, turning pale ivory with a thick, glossy ribbon stage."},
            {"stepNum": 2, "text": "Gently fold room-temperature mascarpone into the yolk sabayon using a silicone spatula until completely smooth and lump-free.", "timerMins": 3, "sensoryCue": "A dense, velvety custard of creamy pale yellow hue."},
            {"stepNum": 3, "text": "Whip egg whites with 30g sugar and pinch of salt on medium-high speed until glossy medium-stiff peaks form.", "timerMins": 4, "sensoryCue": "Snow-white peaks hold their shape with a slight tip curl when whisk is lifted."},
            {"stepNum": 4, "text": "Fold whipped egg whites into the mascarpone mixture in three gentle batches, folding in wide sweeping motions until homogenous and light as air.", "timerMins": 3, "sensoryCue": "A billowy, cloud-like mousse that holds soft ripples."},
            {"stepNum": 5, "text": "Soak ladyfingers: Dip each Savoiardi biscuit into the espresso-Marsala mixture for exactly ONE second on each side (never soak or they turn into mush). Arrange in a tight single layer in the baking dish.", "timerMins": 3, "sensoryCue": "Biscuits absorb coffee without disintegrating; cores remain firm."},
            {"stepNum": 6, "text": "Spread half of the mascarpone cream evenly over the soaked biscuits. Dust with a thin layer of cocoa powder. Add a second layer of soaked ladyfingers running perpendicular to the first. Top with remaining cream and smooth the surface.", "timerMins": 5, "sensoryCue": "Clean, distinct alternating layers of coffee biscuit and pale cream."},
            {"stepNum": 7, "text": "Refrigerate for at least 8 hours (ideally 24 hours). The biscuits soften into cake while the cream sets firmly. Right before serving, dust generously with dark cocoa powder.", "timerMins": 480, "sensoryCue": "A dense, velvety matte chocolate snow covering the pale cream."}
        ],
        {"see": "Pristine dark cocoa powder surface, distinct alternating layers of coffee-soaked sponge and pale ivory mascarpone cream.", "hear": "Silent, soft sinking of the dessert spoon through the tender layers.", "smell": "Intense dark roasted espresso, rich dairy mascarpone, sweet Marsala wine, bittersweet cocoa.", "feel": "Cloud-like, melting cream dissolving on the tongue, followed by moist, spongy, coffee-soaked biscuit."},
        ["Mascarpone is high in milk fat (approx 75%), which acts as a stabilizing structural matrix that solidifies when chilled without requiring gelatin.", "Egg white proteins trap air bubbles that give traditional tiramisù its ethereal lightness; heavy cream makes tiramisù heavy and greasy."],
        [{"issue": "Tiramisù is watery and collapsed into soup", "cause": "Ladyfingers were soaked too long in the coffee, or mascarpone curdled from violent over-whipping.", "solution": "Dip ladyfingers for strictly 1 second per side; fold mascarpone gently by hand."}],
        [{"original": "Marsala wine", "substitute": "Dark Jamaican rum, Amaretto di Saronno, or omit for alcohol-free", "culinaryConsequence": "Amaretto imparts sweet almond-marzipan depth; rum gives robust Caribbean warmth."}],
        {"wine": "Vin Santo del Chianti, Recioto della Valpolicella, or espresso", "zeroProof": "Chilled cold brew coffee infused with orange peel and vanilla bean", "complementarySides": ["Cantucci almond biscotti"]},
        "Piped cloud presentation: In modern Italian pastry, the top cream layer is piped into neat Hershey-kiss-like peaks using a round piping tip before dusting with cocoa powder, creating a breathtaking architectural landscape.",
        "Improves significantly over 24-48 hours as espresso and mascarpone flavors marry. Keeps refrigerated for 4 days.",
        {"calories": 460, "proteinG": 9, "carbsG": 42, "fatG": 28},
        ["rec-souffle-chocolat", "rec-panna-cotta"], ["lesson-egg-geometry", "lesson-emulsions-mastery"]
    ),

    # 4. Vietnamese Pho Bo
    build_recipe(
        "rec-pho-bo", "Traditional Vietnamese Pho Bo (12-Hour Beef Bone Broth with Rice Noodles)",
        "Vietnamese Heritage", "dinner", "climax", "Advanced", 40, 720, 6,
        "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=1200&q=80",
        "The soul of Hanoi: beef marrow bones and brisket blanched and simmered gently for 12 hours with charred ginger, charred yellow onions, toasted whole star anise, cassia bark, black cardamom, and coriander seeds. Poured boiling hot over silky flat rice noodles, thinly shaved raw eye of round steak, braised brisket, and finished with fresh Thai basil, cilantro, and lime.",
        ["gluten-free", "dairy-free", "nut-free"], "Crystal-clear, deeply restorative beef broth shimmering with spice aromatics, sweet onion, and fresh herbal brightness.",
        [
            {"qty": 2000, "unit": "g", "name": "Beef marrow and knuckle bones", "prep": "soaked in salted water 2 hours", "dept": "butchery"},
            {"qty": 800, "unit": "g", "name": "Beef brisket or flank", "prep": "whole piece, to simmer in broth", "dept": "butchery"},
            {"qty": 300, "unit": "g", "name": "Beef eye of round steak", "prep": "frozen 20 mins, shaved paper-thin across the grain", "dept": "butchery"},
            {"qty": 2, "unit": "pcs", "name": "Large yellow onions", "prep": "halved, charred on open flame", "dept": "produce"},
            {"qty": 100, "unit": "g", "name": "Fresh ginger", "prep": "halved lengthwise, charred on flame", "dept": "produce"},
            {"qty": 5, "unit": "pcs", "name": "Whole star anise", "prep": "toasted dry", "dept": "pantry"},
            {"qty": 1, "unit": "stick", "name": "Cassia bark or cinnamon stick", "prep": "toasted dry", "dept": "pantry"},
            {"qty": 2, "unit": "pcs", "name": "Black cardamom pods (Thao Qua)", "prep": "cracked lightly, toasted", "dept": "pantry"},
            {"qty": 5, "unit": "g", "name": "Coriander seeds", "prep": "toasted dry", "dept": "pantry"},
            {"qty": 60, "unit": "ml", "name": "Authentic Vietnamese fish sauce (Phu Quoc 40°N)", "prep": "high protein", "dept": "pantry"},
            {"qty": 30, "unit": "g", "name": "Yellow rock sugar (Duong Phen)", "prep": "for mellow sweetness", "dept": "pantry"},
            {"qty": 500, "unit": "g", "name": "Fresh or dried flat rice noodles (Banh Pho)", "prep": "soaked, blanched 10 seconds", "dept": "drygoods"},
            {"qty": 1, "unit": "bunch", "name": "Thai basil, cilantro, and culantro (sawtooth herb)", "prep": "fresh herbs", "dept": "produce"},
            {"qty": 200, "unit": "g", "name": "Fresh bean sprouts", "prep": "rinsed", "dept": "produce"},
            {"qty": 2, "unit": "pcs", "name": "Limes", "prep": "quartered", "dept": "produce"}
        ],
        [
            {"name": "16-quart tall stockpot", "type": "everyday"},
            {"name": "Spice sachet bag (muslin or stainless steel ball)", "type": "everyday"},
            {"name": "Fine conical skimmer and chinois strainer", "type": "everyday"}
        ],
        [
            "Blanch bones in boiling water for 15 minutes; drain and scrub every bone clean under cold water.",
            "Char onions and ginger over an open gas flame until blackened; wash away loose burnt skin.",
            "Toast spices in a dry skillet until intensely fragrant, then seal in a spice sachet.",
            "Freeze eye of round steak for 20 minutes before shaving razor-thin with a sharp knife."
        ],
        [
            {"stepNum": 1, "text": "Place clean bones and brisket into clean stockpot. Cover with 6 liters of fresh cold water. Bring to a gentle simmer over medium-high heat, skimming off all rising foam and scum.", "timerMins": 30, "temperature": "95°C", "sensoryCue": "Clear liquid comes to gentle simmer; white foam rises and is skimmed clean."},
            {"stepNum": 2, "text": "Add charred onions, charred ginger, rock sugar, and 30ml fish sauce. Lower heat so liquid maintains lazy, gentle bubbles (never a violent boil, which turns broth cloudy). Simmer uncovered for 3 hours.", "timerMins": 180, "temperature": "88°C", "sensoryCue": "Broth turns clear golden amber; sweet aroma of charred allium and ginger fills the air.", "scienceNote": "Gentle sub-boiling temperature prevents lipids and proteins from emulsifying into an opaque broth, keeping the broth crystalline and clear (unlike tonkotsu)."},
            {"stepNum": 3, "text": "At hour 3, remove the cooked brisket. Submerge in cold water for 5 minutes (prevents darkening), then wrap and refrigerate until slicing.", "timerMins": 5, "sensoryCue": "Brisket is fork-tender."},
            {"stepNum": 4, "text": "Add the toasted spice sachet to the stockpot. Simmer for an additional 2 hours (do not leave spices in for more than 3 hours or broth turns bitter and muddy).", "timerMins": 120, "sensoryCue": "Intoxicating fragrance of star anise, cinnamon, and black cardamom blooms."},
            {"stepNum": 5, "text": "Remove bones and spices. Strain broth through a chinois lined with cheesecloth. Season with remaining fish sauce and salt to taste. Broth should taste slightly over-salted, as unseasoned noodles will dilute it in the bowl.", "timerMins": 10, "sensoryCue": "Crystalline, shimmering amber broth with golden drops of clean beef oil."},
            {"stepNum": 6, "text": "Assemble: Blanch rice noodles in boiling water for 10 seconds; shake dry and place in heated bowls. Top with thinly sliced cooked brisket and raw shaved eye of round steak.", "timerMins": 2, "sensoryCue": "Silky white noodles topped with dark braised beef and delicate pink raw beef slices."},
            {"stepNum": 7, "text": "Ladle boiling hot broth (approx 95°C) directly over the raw steak. The boiling broth will cook the shaved meat instantly to a tender pink-blush (tai). Serve with herb platter, bean sprouts, and lime wedges.", "timerMins": 1, "sensoryCue": "Raw beef turns instantly opaque and tender; aromatic herbal steam rises from the bowl."}
        ],
        {"see": "Crystalline amber broth with drops of clear fat, snow-white flat rice noodles, pink tender beef slices, green cilantro, purple Thai basil.", "hear": "Sizzling hiss as boiling broth hits raw meat; slurping of hot noodles.", "smell": "Intoxicating star anise, warm cassia, charred ginger, rich beef marrow, fresh pungent fish sauce.", "feel": "Silky, slippery rice noodles and meltingly tender beef in a clean, restorative broth that leaves zero greasy film."},
        ["Rock sugar (sucrose) provides a rounded, mellow sweetness that softens fish sauce salinity without the sharp sweet spike of refined white sugar.", "Black cardamom (Amomum tsaoko) contains cineole and camphor, contributing a distinctive smoky, medicinal coolness essential to authentic Northern Pho."],
        [{"issue": "Broth turned murky and cloudy", "cause": "Broth was boiled vigorously instead of gently simmered, emulsifying bone fat.", "solution": "Always simmer at 88-90°C with gentle lazy bubbles; never cover with tight lid while simmering."}],
        [{"original": "Eye of round steak", "substitute": "Beef tenderloin, sirloin, or wagyu carpaccio slices", "culinaryConsequence": "Tenderloin provides even more tender texture when cooked by boiling broth."}],
        {"wine": "Off-dry German Riesling, French Viognier, or a crisp cold Bia Saigon beer", "zeroProof": "Vietnamese iced lime tea (Tra Chanh) or coconut water with mint", "complementarySides": ["Cha Gio (crispy fried Vietnamese spring rolls)"]},
        "Northern (Hanoi) vs Southern (Saigon) Pho: Northern Pho focuses entirely on the pure, austere elegance of the broth with minimal garnishes; Southern Pho embraces bean sprouts, hoisin sauce, Sriracha, and culantro at the table.",
        "Broth stores refrigerated for up to 5 days; freezes for 6 months. Reheat to boiling before pouring over fresh noodles.",
        {"calories": 520, "proteinG": 38, "carbsG": 64, "fatG": 14},
        ["rec-tonkotsu-ramen", "rec-dan-dan-noodles"], ["lesson-seasoning-osmosis", "lesson-braising-collagen"]
    ),

    # 5. Pan-Seared Dry-Aged Ribeye
    build_recipe(
        "rec-pan-seared-ribeye", "Cast-Iron Dry-Aged Ribeye with Bone Marrow Butter & Pommes Fondue",
        "American Modern Steakhouse", "dinner", "climax", "Intermediate", 15, 18, 2,
        "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        "The ultimate steakhouse triumph: a 45-day dry-aged bone-in ribeye salted overnight, seared in smoking hot cast iron to forge a deeply caramelized, savory mahogany crust, and basted continuously (arroser) with foamy cultured butter, smashed garlic, and woody thyme. Served with melting bone marrow compound butter and golden thyme-braised Pommes Fondue.",
        ["gluten-free", "nut-free"], "Intense dry-aged funk, rich caramelized crust, buttery red core, aromatic garlic-thyme baste.",
        [
            {"qty": 1, "unit": "pcs", "name": "Bone-in dry-aged Ribeye steak (approx 800g, 2 inches thick)", "prep": "dry-brined with 8g kosher salt 24 hours", "dept": "butchery"},
            {"qty": 30, "unit": "ml", "name": "Avocado oil or beef tallow", "prep": "high smoke point, for searing", "dept": "pantry"},
            {"qty": 60, "unit": "g", "name": "European cultured butter", "prep": "for pan basting (arrosé)", "dept": "dairy"},
            {"qty": 4, "unit": "cloves", "name": "Garlic", "prep": "smashed with flat of cleaver, skin-on", "dept": "produce"},
            {"qty": 6, "unit": "sprigs", "name": "Fresh woody thyme", "prep": "whole sprigs", "dept": "produce"},
            {"qty": 2, "unit": "sprigs", "name": "Fresh rosemary", "prep": "whole sprig", "dept": "produce"},
            {"qty": 40, "unit": "g", "name": "Roasted bone marrow butter", "prep": "whipped with sea salt and shallots", "dept": "butchery"},
            {"qty": 4, "unit": "pcs", "name": "Yukon Gold potatoes", "prep": "trimmed into flat cylinders for Pommes Fondue", "dept": "produce"},
            {"qty": 200, "unit": "ml", "name": "Brown chicken or veal stock", "prep": "for fondue braising", "dept": "pantry"}
        ],
        [
            {"name": "12-inch heavy seasoned cast-iron skillet", "type": "everyday"},
            {"name": "Instant-read digital thermocouple thermometer", "type": "everyday"},
            {"name": "Heavy stainless chef's basting spoon", "type": "everyday"}
        ],
        [
            "Dry-brine steak: Salt generously on all sides 24 hours ahead; rest on an elevated wire rack in refrigerator uncovered to form a dry surface pellicle.",
            "Remove steak from fridge 45 minutes prior to cooking to take off chill.",
            "Trim potatoes into 4cm tall flat cylinders; pat dry.",
            "Whip roasted bone marrow with softened butter, minced chives, and flaky salt."
        ],
        [
            {"stepNum": 1, "text": "Prepare Pommes Fondue: In a medium skillet, brown potato cylinders in butter on both flat ends for 10 minutes until deep golden. Pour in chicken stock and thyme sprigs. Cover and braise over low heat for 20 minutes until tender as butter.", "timerMins": 30, "sensoryCue": "Potatoes absorb stock, turning translucent, creamy, and golden with crisp ends."},
            {"stepNum": 2, "text": "Preheat cast iron skillet over high heat for 6 minutes until smoking hot (approx 230°C / 450°F). Add 20ml beef tallow or avocado oil.", "timerMins": 6, "temperature": "230°C", "sensoryCue": "Oil shimmers and smokes faintly; radiant heat hits your hand 6 inches above pan."},
            {"stepNum": 3, "text": "Lay steak gently into pan away from yourself. Sear undisturbed for 2.5 minutes until a deep, dark mahogany Maillard crust forms. Flip and cook reverse side for 2.5 minutes.", "timerMins": 5, "temperature": "230°C", "sensoryCue": "Violent, roaring sizzle; intense nutty, blue-cheese dry-aged roasting aroma.", "scienceNote": "Dry-brining evaporates surface water into a dehydrated pellicle. Pan thermal energy goes 100% into Maillard browning immediately without wasting energy boiling water."},
            {"stepNum": 4, "text": "Turn heat to medium. Drop in 60g cold butter, smashed garlic, thyme, and rosemary. The butter will melt and froth into a violent white foam.", "timerMins": 1, "temperature": "145°C", "sensoryCue": "Roaring sizzle subsides into gentle nutty crackle; garlic and herbs fragrance fills the air."},
            {"stepNum": 5, "text": "THE ARROSÉ BASTE: Tilt the skillet toward yourself. Use the large spoon to rapidly scoop the bubbling, herb-infused browned butter and pour it continuously over the top of the steak for 3 to 4 minutes.", "timerMins": 3.5, "sensoryCue": "Foaming butter cascades over steak; edges turn dark amber; herbs crisp up against meat.", "scienceNote": "Basting transfers heat from foaming butterfat (145°C) to the top of the steak via convective conduction, cooking the meat evenly from both sides without flipping continuously."},
            {"stepNum": 6, "text": "Check core temp with instant-read probe: pull at exactly 49°C (120°F) for medium-rare. Transfer steak to a warm wooden board or resting rack.", "timerMins": 1, "temperature": "49°C core pull temp", "sensoryCue": "Thermometer glides smoothly into the center without resistance."},
            {"stepNum": 7, "text": "THE REST: Top the hot steak with a thick disc of bone marrow butter. Rest for 10 minutes undisturbed. Carryover heat will gently elevate internal core temp to a perfect 54°C (130°F) medium-rare while muscle fibers relax.", "timerMins": 10, "sensoryCue": "Bone marrow butter melts across the crusted surface into a glistening savory glaze.", "scienceNote": "During cooking, heat contracts muscle fibers, forcing water toward the cooler center. Resting allows muscle fibers to relax and reabsorb juices throughout the steak so it doesn't bleed out when cut."},
            {"stepNum": 8, "text": "Carve off the bone, slice into 1cm thick medallions, season cut faces with flaky Maldon sea salt, and serve with melting Pommes Fondue.", "timerMins": 2, "sensoryCue": "Shattering crisp crust surrounding a ruby-pink, glistening succulent interior."}
        ],
        {"see": "Dark mahogany-crusted exterior with crispy thyme sprigs, melting bone marrow glaze, vibrant ruby-red warm center, golden potato cylinders.", "hear": "Audible crunch when knife cuts through crust; silence of resting meat.", "smell": "Intense nutty dry-aged beef, toasted brown butter, roasted garlic, resinous thyme and rosemary.", "feel": "Crisp exterior crust followed by tender, buttery beef that melts with astonishing succulence."},
        ["Dry aging evaporates up to 15% water and activates endogenous proteolytic enzymes (calpains and cathepsins) that break down collagen and muscle proteins into savory glutamates and nutty aroma esters.", "Resting steak allows denatured actin-myosin fibers to cool below 50°C, increasing cellular capillary pressure to retain intracellular meat juices."],
        [{"issue": "Steak developed a grey band beneath the crust", "cause": "Steak was cold from the fridge when added to pan, or pan was not hot enough during initial sear.", "solution": "Always bring steak to room temp for 45 minutes before searing, and sear in smoking hot cast iron."}],
        [{"original": "Bone-in ribeye", "substitute": "New York strip, Porterhouse, or bone-in rib pork chop", "culinaryConsequence": "Strip steak has firmer texture and cleaner beef flavor; cook pork chop to 60°C core."}],
        {"wine": "Napa Valley Cabernet Sauvignon, Barolo, or Saint-Julien Bordeaux", "zeroProof": "Tart cherry and black currant shrub with sparkling mineral water and bruised thyme", "complementarySides": ["Pommes Fondue", "Charred broccolini with lemon and red pepper flakes"]},
        "Reverse-sear adaptation for thick cuts (>2.5 inches): Bake on a wire rack at 105°C (225°F) until core reaches 43°C (110°F), then flash-sear in smoking cast iron with butter for 60 seconds per side. Zero grey band, edge-to-edge pink perfection.",
        "Eat immediately after resting. Leftover cold sliced ribeye is extraordinary in sandwiches.",
        {"calories": 880, "proteinG": 58, "carbsG": 22, "fatG": 64},
        ["rec-steak-bearnaise", "rec-boeuf-bourguignon"], ["lesson-heat-control", "lesson-seasoning-osmosis"]
    ),

    # 6. Oops! I Dropped the Lemon Tart
    build_recipe(
        "rec-shattered-lemon-tart", "Oops! I Dropped the Lemon Tart (Shattered Limoncello Sabayon)",
        "Modern Italian Gastronomy", "dessert", "dessert", "Advanced", 30, 20, 4,
        "https://images.unsplash.com/photo-1519915028121-7d3463d20b13?auto=format&fit=crop&w=1200&q=80",
        "Inspired by Chef Massimo Bottura's legendary 3-Michelin-star masterpiece from Osteria Francescana in Modena: a celebration of serendipity and deliberate imperfection. A velvety, sharp Limoncello-infused lemon curd sabayon splattered dramatically across an asymmetric plate, scattered with golden shards of baked Pâte Sablée crust, candied capers, bergamot fluid gel, and sweet basil oil.",
        ["vegetarian", "nut-free"], "Electrifying lemon acidity tempered by sweet sablé biscuit, floral limoncello, and surprising savory pops of candied caper.",
        [
            {"qty": 200, "unit": "g", "name": "Fresh Meyer lemon juice", "prep": "strained", "dept": "produce"},
            {"qty": 4, "unit": "pcs", "name": "Large egg yolks", "prep": "fresh", "dept": "dairy"},
            {"qty": 2, "unit": "pcs", "name": "Large whole eggs", "prep": "fresh", "dept": "dairy"},
            {"qty": 140, "unit": "g", "name": "Granulated sugar", "prep": "divided", "dept": "pantry"},
            {"qty": 120, "unit": "g", "name": "Unsalted European butter", "prep": "cubed cold", "dept": "dairy"},
            {"qty": 30, "unit": "ml", "name": "Artisanal Limoncello di Sorrento", "prep": "high-proof lemon liqueur", "dept": "beverage"},
            {"qty": 150, "unit": "g", "name": "Pâte Sablée dough (flour, butter, powdered sugar, yolk)", "prep": "baked crisp until golden brown", "dept": "drygoods"},
            {"qty": 20, "unit": "g", "name": "Salted capers", "prep": "desalted, candied in simple syrup and dehydrated crisp", "dept": "pantry"},
            {"qty": 2, "unit": "g", "name": "Agar-agar powder", "prep": "for bergamot fluid gel", "dept": "pantry"},
            {"qty": 100, "unit": "ml", "name": "Bergamot or Earl Grey tea infusion", "prep": "for fluid gel", "dept": "beverage"},
            {"qty": 20, "unit": "ml", "name": "Sweet basil chlorophyll oil", "prep": "vibrant emerald green", "dept": "produce"}
        ],
        [
            {"name": "Large matte black or slate presentation plates", "type": "everyday"},
            {"name": "Immersion blender", "type": "everyday"},
            {"name": "Pastry offset spatula and squeeze bottles", "type": "everyday"}
        ],
        [
            "Bake Pâte Sablée crust at 175°C until deep golden brown; cool and break by hand into rustic, jagged geometric shards.",
            "Desalt capers in warm water for 2 hours, then simmer in 50% sugar syrup and bake at 100°C until crisp and shiny.",
            "Boil bergamot tea with agar-agar for 1 minute; chill to a firm gel, then blend on high speed until a silky, glistening fluid gel forms.",
            "Zest Meyer lemons fine."
        ],
        [
            {"stepNum": 1, "text": "Prepare Lemon-Limoncello Sabayon Curd: In a heatproof bowl set over simmering water, whisk egg yolks, whole eggs, lemon juice, lemon zest, and 120g sugar continuously for 8-10 minutes until thick, custardy, and registering 82°C (180°F).", "timerMins": 9, "temperature": "82°C", "sensoryCue": "Whisk leaves clean ribbon trails; mixture thickens dramatically into custard."},
            {"stepNum": 2, "text": "Remove from heat. Let cool to 55°C. Add cold cubed butter piece by piece while blending with an immersion blender to shear butter into a silky micro-emulsion. Blend in Limoncello. Chill for 2 hours.", "timerMins": 4, "temperature": "55°C", "sensoryCue": "Curd transforms into an ultra-glossy, luminous canary-yellow silk."},
            {"stepNum": 3, "text": "THE PLATING PERFORMANCE: Take a large soup spoon of the cold lemon curd. Hold it 18 inches above the asymmetric matte plate, and drop it with deliberate force onto one corner of the plate to shatter and splatter naturally across the porcelain.", "timerMins": 1, "sensoryCue": "A dramatic, dynamic yellow splash radiating across the dark canvas."},
            {"stepNum": 4, "text": "Scatter crisp golden Pâte Sablée crust shards deliberately across and around the splatter, as if the tart fell from the sky and shattered on impact.", "timerMins": 1, "sensoryCue": "Golden geometric shards resting in the glossy curd."},
            {"stepNum": 5, "text": "Dot the plate with drops of translucent bergamot fluid gel, scatter crunchy candied capers, and drizzle beads of emerald green basil oil.", "timerMins": 1, "sensoryCue": "Vibrant contrast: canary yellow, golden biscuit, black capers, emerald green drops."}
        ],
        {"see": "Avant-garde splatter of radiant yellow curd on dark slate, broken biscuit shards, emerald green oil dots, glistening candied capers.", "hear": "Sharp crunch of sablé crust and crisp capers.", "smell": "Intense volatile lemon oil, floral bergamot, sweet toasted butter crust, fresh basil.", "feel": "Silky, melting tart curd contrasted by brittle buttery biscuit and surprising sweet-briny crunch."},
        ["Immersion blending at 55°C creates tiny butterfat droplets that refract light, giving the lemon curd its luminous, pale yellow sheen while preventing butter separation.", "Candied capers contain sinigrin and sulfur compounds that mimic umami-rich citrus notes when tempered by simple sugar syrup."],
        [{"issue": "Curd was runny and failed to hold shape on plate", "cause": "Curd was pulled from heat before reaching the 82°C egg coagulation threshold.", "solution": "Cook until thick enough to coat a spoon heavily before chilling."}],
        [{"original": "Bergamot tea", "substitute": "Earl Grey tea or Yuzu juice", "culinaryConsequence": "Earl Grey contains natural bergamot oil, matching the floral citrus profile beautifully."}],
        {"wine": "Moscato d'Asti, Limoncello di Capri, or Franciacorta Rosé", "zeroProof": "Chilled sparkling Earl Grey iced tea with fresh lemon zest and candied lemon peel", "complementarySides": ["Fresh wild blackberries"]},
        "Philosophy of the broken dish: Massimo Bottura created this dish when his pastry chef dropped the final lemon tart of the evening on the floor; instead of discarding it, they recognized the extraordinary beauty of the fractured form and revolutionized modern pastry.",
        "Components can be held separately for 2 days. Assemble tableside in under 60 seconds.",
        {"calories": 420, "proteinG": 6, "carbsG": 46, "fatG": 24},
        ["rec-tarte-tatin", "rec-panna-cotta"], ["lesson-egg-geometry", "lesson-emulsions-mastery"]
    ),

    # 7. Classical Sauce Hollandaise
    build_recipe(
        "rec-sauce-hollandaise", "Classical Sauce Hollandaise (Clarified Butter & Lemon Emulsion)",
        "French Classical", "sauce_stock", "accompaniment", "Advanced", 10, 10, 4,
        "https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=1200&q=80",
        "The queen of classical French mother sauces: warm pasture-raised egg yolks whisked with a strained reduction of white wine vinegar, shallots, and cracked peppercorns over a gentle double-boiler, then slowly emulsified with warm clarified European butter into an opulent, velvety, lemon-scented pale-gold ribbon.",
        ["vegetarian", "gluten-free", "nut-free"], "Decadent, rich warm butterfat tempered by sharp lemon acidity and floral pepper reduction.",
        [
            {"qty": 3, "unit": "pcs", "name": "Large pasture-raised egg yolks", "prep": "room temp", "dept": "dairy"},
            {"qty": 200, "unit": "g", "name": "Clarified butter (beurre noisette option)", "prep": "warm (58°C)", "dept": "dairy"},
            {"qty": 30, "unit": "ml", "name": "Dry white wine", "prep": "for reduction", "dept": "pantry"},
            {"qty": 15, "unit": "ml", "name": "White wine vinegar", "prep": "for reduction", "dept": "pantry"},
            {"qty": 1, "unit": "pcs", "name": "Shallot", "prep": "minced fine for reduction", "dept": "produce"},
            {"qty": 10, "unit": "pcs", "name": "Whole black peppercorns", "prep": "cracked", "dept": "pantry"},
            {"qty": 15, "unit": "ml", "name": "Fresh lemon juice", "prep": "strained", "dept": "produce"},
            {"qty": 1, "unit": "pinch", "name": "Cayenne pepper or piment d'Espelette", "prep": "to finish", "dept": "pantry"}
        ],
        [
            {"name": "Stainless steel or copper round-bottomed bowl (cul-de-poule)", "type": "everyday"},
            {"name": "Saucepan for water bath (bain-marie)", "type": "everyday"},
            {"name": "Fine wire balloon whisk", "type": "everyday"}
        ],
        [
            "Simmer white wine, vinegar, shallot, and peppercorns until reduced to 1 tablespoon; strain and cool.",
            "Clarify butter: melt gently, skim milk solids, and keep clear liquid fat warm at 58°C.",
            "Have a folded damp kitchen towel ready on the counter to anchor the bowl while whisking."
        ],
        [
            {"stepNum": 1, "text": "Combine egg yolks, strained vinegar reduction, and 10ml cold water in the round-bottom bowl. Whisk vigorously for 1 minute before heating.", "timerMins": 1, "sensoryCue": "Yolks turn frothy and lemon-yellow."},
            {"stepNum": 2, "text": "Set bowl over barely simmering water (the bowl bottom must NOT touch water). Whisk in a rapid figure-eight motion for 3-4 minutes until the sabayon thickens, triples in volume, and forms ribbons when lifted.", "timerMins": 3.5, "temperature": "62°C", "sensoryCue": "The whisk leaves clear lines showing the bowl bottom; thick, creamy texture."},
            {"stepNum": 3, "text": "Remove bowl to the damp towel. Whisking continuously, begin drizzling in the warm clarified butter, literally drop by drop for the first 30 seconds to establish the emulsion.", "timerMins": 1, "sensoryCue": "Drops of butter disappear seamlessly into the thick yolk base."},
            {"stepNum": 4, "text": "Once established, pour the remaining butter in a thin, steady thread while whisking rhythmically until all butter is absorbed into an opulent, glossy ribbon.", "timerMins": 3, "sensoryCue": "Sauce thickens into a pale golden velvet that coats a spoon luxuriously."},
            {"stepNum": 5, "text": "Whisk in fresh lemon juice, sea salt, and a pinch of cayenne. Taste: balance should be rich yet distinctly bright and clean. Hold warm in a thermos or near the stove at 50°C.", "timerMins": 1, "sensoryCue": "Gleaming pale gold sauce with a warm, tangy lemon aroma."}
        ],
        {"see": "Luminous pale-gold velvet, thick ribbon consistency, mirror gloss.", "hear": "Rhythmic whipping of the whisk against the copper bowl.", "smell": "Clarified sweet dairy, fresh volatile lemon, peppery reduction.", "feel": "Decadently rich, unctuous warmth melting instantly on the tongue."},
        ["One egg yolk can theoretically emulsify up to 5 liters of butterfat, provided enough water is present to maintain the continuous phase.", "Clarified butter has milk solids removed, preventing premature casein curdling."],
        [{"issue": "Hollandaise broke into oily separated liquid", "cause": "Butter was added too hot (>68°C) or too quickly before emulsion was stable.", "solution": "Whisk 1 teaspoon of warm water and 1 raw egg yolk in a clean bowl, then slowly whisk the broken sauce into it."}],
        [{"original": "Clarified butter", "substitute": "Brown butter (Sauce Noisette) or cold whole butter (Beurre Blanc method)", "culinaryConsequence": "Brown butter Hollandaise delivers intoxicating toasted hazelnut notes."}],
        {"wine": "White Burgundy (Chablis), Sancerre, or Champagne", "zeroProof": "Chilled sparkling water with Meyer lemon twist", "complementarySides": ["Steamed white asparagus", "Poached wild salmon"]},
        "Thermos holding hack: In high-volume fine dining kitchens, freshly emulsified Hollandaise is transferred immediately into a pre-warmed stainless thermos flask, keeping it at a safe 52°C for up to 2 hours without breaking.",
        "Hollandaise cannot be refrigerated. Discard after 2 hours for food safety.",
        {"calories": 380, "proteinG": 3, "carbsG": 1, "fatG": 42},
        ["rec-eggs-benedict", "rec-sole-meuniere"], ["lesson-mother-sauces", "lesson-emulsions-mastery"]
    ),

    # 8. Classical Master Brown Veal Stock (Fond Brun de Veau)
    build_recipe(
        "rec-fond-brun-veau", "Master Brown Veal Stock (Fond Brun de Veau Classique)",
        "French Classical", "sauce_stock", "accompaniment", "Advanced", 30, 480, 8,
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1200&q=80",
        "The majestic cornerstone of classical French haute cuisine: veal knuckle and marrow bones roasted to deep mahogany, caramelized with mirepoix and tomato paste (pincé), deglazed with red wine, and simmered gently for 8 hours with aromatics until it yields a crystal-clear, deep amber, gelatin-dense nectar that solidifies into jelly when cooled.",
        ["gluten-free", "dairy-free", "nut-free"], "Deep, clean, roasted savory beef essence with silky natural gelatin body and subtle allium sweetness.",
        [
            {"qty": 3000, "unit": "g", "name": "Veal knuckle and neck bones", "prep": "cut into 5cm pieces to expose collagen and marrow", "dept": "butchery"},
            {"qty": 500, "unit": "g", "name": "Beef shin or veal trimmings", "prep": "for meat protein flavor", "dept": "butchery"},
            {"qty": 300, "unit": "g", "name": "Yellow onions", "prep": "coarsely chopped mirepoix", "dept": "produce"},
            {"qty": 200, "unit": "g", "name": "Carrots", "prep": "coarsely chopped mirepoix", "dept": "produce"},
            {"qty": 200, "unit": "g", "name": "Celery ribs", "prep": "coarsely chopped mirepoix", "dept": "produce"},
            {"qty": 60, "unit": "g", "name": "Tomato paste", "prep": "for caramelization (pincé)", "dept": "pantry"},
            {"qty": 300, "unit": "ml", "name": "Dry red wine", "prep": "for deglazing roasting pans", "dept": "pantry"},
            {"qty": 6, "unit": "cloves", "name": "Garlic", "prep": "halved", "dept": "produce"},
            {"qty": 1, "unit": "pcs", "name": "Classic Bouquet Garni (thyme, parsley stems, 3 bay leaves, leek green)", "prep": "tied tightly with twine", "dept": "produce"},
            {"qty": 5, "unit": "g", "name": "Black peppercorns", "prep": "cracked", "dept": "pantry"}
        ],
        [
            {"name": "Heavy stainless steel roasting pans", "type": "everyday"},
            {"name": "16 to 20-quart tall stockpot", "type": "everyday"},
            {"name": "Fine conical chinois and cheesecloth", "type": "specialty", "substitute": "Fine mesh wire strainer"}
        ],
        [
            "Rinse bones in cold water; dry thoroughly on towels.",
            "Chop onions, carrots, and celery into uniform 3cm mirepoix chunks.",
            "Tie bouquet garni tightly with butcher's twine.",
            "Preheat oven to 220°C (425°F)."
        ],
        [
            {"stepNum": 1, "text": "Roast bones: Place veal bones and meat trimmings in roasting pans without crowding. Roast at 220°C for 45-50 minutes, turning once, until deeply browned and caramelized on all sides.", "timerMins": 50, "temperature": "220°C", "sensoryCue": "Bones turn dark mahogany; kitchen fills with rich roasted meat aroma.", "scienceNote": "High dry heat induces Maillard browning and sugar caramelization, generating pyrazines and furans that give brown stock its color and roasted depth."},
            {"stepNum": 2, "text": "Caramelize mirepoix: Add onions, carrots, and celery to the roasting pan. Smear tomato paste over the bones and vegetables. Return to oven for 15 minutes until vegetables are golden and tomato paste is brick-red (pincer).", "timerMins": 15, "sensoryCue": "Tomato paste darkens to deep mahogany without burning."},
            {"stepNum": 3, "text": "Transfer roasted bones and mirepoix to the tall stockpot using tongs. Pour off excess rendered fat from roasting pans.", "timerMins": 5, "sensoryCue": "Pan bottom is coated in thick brown caramelized fond."},
            {"stepNum": 4, "text": "Deglaze roasting pans: Place pans over burners on medium-high heat. Pour in red wine, scraping up all brown fond with a wooden spatula. Pour deglazed liquid into the stockpot.", "timerMins": 5, "sensoryCue": "Wine boils vigorously, dissolving caramelized pan drippings into dark liquid."},
            {"stepNum": 5, "text": "Fill stockpot with 7 liters of cold filtered water (bones must be submerged by 3 inches). Bring to a gentle simmer over medium heat. Skim off all grey scum and rendered fat that rises to the surface.", "timerMins": 30, "temperature": "92°C", "sensoryCue": "A dense foam cap forms; skim continuously until surface is clean."},
            {"stepNum": 6, "text": "Add bouquet garni, garlic, and black peppercorns. Lower heat to the lowest setting: the surface should show only gentle, lazy ripples (88°C–92°C). Never allow a rolling boil. Simmer undisturbed for 8 hours, skimming hourly.", "timerMins": 480, "temperature": "88°C - 92°C", "sensoryCue": "Liquid reduces slowly, concentrating into a crystal-clear, glistening dark amber stock.", "scienceNote": "Veal knuckle bones contain immature type-I collagen that hydrolyzes into gelatin at 70-85°C. Boiling turbulently would shatter fat into droplets, clouding the stock."},
            {"stepNum": 7, "text": "Strain without pressing: Ladle stock gently through a chinois lined with damp cheesecloth into a clean pot. Do NOT press or squeeze bones/vegetables, which forces cloudiness into the stock.", "timerMins": 15, "sensoryCue": "Crystal-clear amber liquid flows like liquid stained glass."},
            {"stepNum": 8, "text": "Chill rapidly in an ice bath. When refrigerated overnight, it sets into a firm, glistening, jiggly block of pure gelatin with a solid fat cap on top that can be lifted off in one piece.", "timerMins": 10, "sensoryCue": "Firm jelly that melts instantaneously into liquid upon touching a warm spoon."}
        ],
        {"see": "Pristine, crystal-clear, deep translucent amber liquid that jiggles like firm jelly when chilled.", "hear": "Absolute quiet during the 8-hour lazy simmer.", "smell": "Deep roasted veal, caramelized alliums, wine reduction, fragrant bay and thyme.", "feel": "Silky, mouth-coating body with natural gelatin viscosity that leaves a subtle tackiness on the lips."},
        ["Veal bones contain significantly higher concentrations of soluble collagen than adult beef bones, producing double the natural gelatin concentration without needing gelatin powders.", "Never salt a foundational stock: reducing 1 liter of salted stock into 100ml demi-glace would multiply the salinity by 10, rendering the sauce inedible."],
        [{"issue": "Stock is cloudy and grey instead of clear amber", "cause": "Stock was allowed to boil vigorously, emulsifying bone marrow fat and proteins.", "solution": "Clarify using a classical egg-white raft (consommé technique) or accept a slightly cloudy rustic stock."}],
        [{"original": "Veal knuckle bones", "substitute": "Beef shank bones and chicken wings", "culinaryConsequence": "Chicken wings provide abundant collagen to mimic veal's gelatinous body."}],
        {"wine": "N/A (Foundational stock)", "zeroProof": "N/A", "complementarySides": ["Base for Espagnole, Demi-Glace, Bordelaise, and red wine reductions"]},
        "Glace de Viande reduction: Simmer 2 liters of strained brown veal stock until reduced by 90% into 200ml of thick, syrupy meat glaze. Cool in ice cube trays; one cube dropped into any pan sauce provides instant 3-star restaurant depth.",
        "Keeps refrigerated for 6 days (reboil on day 5); freezes indefinitely.",
        {"calories": 90, "proteinG": 18, "carbsG": 2, "fatG": 1},
        ["rec-boeuf-bourguignon", "rec-coq-au-vin"], ["lesson-mother-sauces", "lesson-heat-control"]
    )
]

ALL_RECIPES.extend(ADDITIONAL_RECIPES)

print(f"Total compiled master recipes so far: {len(ALL_RECIPES)}")
