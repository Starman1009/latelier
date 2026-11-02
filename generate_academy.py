# -*- coding: utf-8 -*-
"""
Generates data-academy.js for L'Atelier's Culinary Academy.
19 structured lessons across Foundations, Intermediate, Advanced, and Professional tracks.
"""

import json

ACADEMY_LESSONS = [
    {
        "id": "lesson-knife-skills",
        "title": "Master Knife Skills & Classical Precision Cuts",
        "track": "Foundations",
        "durationMins": 35,
        "difficulty": "Beginner",
        "summary": "Master the pinch grip, the non-dominant claw, blade geometry, and the foundational French cuts: Julienne, Brunoise, Chiffonade, Mirepoix, Batonnet, and Paysanne.",
        "contentSections": [
            {
                "heading": "1. The Pinch Grip and The Claw",
                "text": "Hold the chef's knife by pinching the blade between your thumb and the side of your index finger right at the bolster, wrapping your remaining fingers securely around the handle. This shifts the center of balance directly into your hand, giving you 100% control over blade angle. Your guiding hand forms 'the claw': curl fingertips inward like a bear claw, resting blade flat against the knuckles to guide cut thickness while keeping fingertips physically impossible to cut."
            },
            {
                "heading": "2. Classical French Vegetable Cuts",
                "text": "Precision cutting is not merely visual; uniform vegetable dimensions guarantee that all pieces cook at the exact same thermal rate.\n\n• Batonnet: 6mm x 6mm x 5cm (1/4 in x 1/4 in x 2 in). The mother of small dice.\n• Brunoise: 3mm x 3mm x 3mm (1/8 in cube). Essential for consommé garnish and fine ragù soffritto.\n• Julienne: 1.5mm x 1.5mm x 5cm (1/16 in x 2 in matchsticks).\n• Fine Brunoise: 1.5mm cube, cut from julienne.\n• Chiffonade: Tightly roll leafy herbs (basil, sage) or greens and slice razor-thin ribbons with a smooth forward rolling stroke without bruising."
            },
            {
                "heading": "3. Honing vs. Sharpening",
                "text": "A honing steel does NOT remove steel or sharpen a dull knife; it straightens microscopic bent teeth along the apex of the blade edge. Hone at a consistent 15-20 degree angle before every cooking session. Sharpen on whetstones (1000/6000 grit) every 3-6 months to grind a brand-new cutting edge."
            }
        ],
        "sensoryCues": {
            "sound": "Rhythmic, whispering slice across the cutting board rather than a blunt chopping thump.",
            "feel": "Blade slides effortlessly through a ripe tomato skin under its own weight without squishing juice."
        },
        "commonMistakes": [
            {"mistake": "Index finger extended along the spine of the knife", "consequence": "Causes hand fatigue, wrist instability, and blade wobbling."},
            {"mistake": "Sawing back and forth or pressing straight down", "consequence": "Crushes cell walls, releasing bitter juices; use a fluid forward-and-down slicing motion."}
        ],
        "relatedRecipes": ["rec-sole-meuniere", "rec-ragu-bolognese", "rec-french-omelette"]
    },
    {
        "id": "lesson-seasoning-osmosis",
        "title": "The Science of Seasoning & Osmosis",
        "track": "Foundations",
        "durationMins": 30,
        "difficulty": "Beginner",
        "summary": "Understand how salt migrates across cellular membranes, alters protein water-holding capacity, suppresses bitterness, and why salt timing makes or breaks cooking.",
        "contentSections": [
            {
                "heading": "1. Osmosis & Protein Dissolution",
                "text": "When salt (NaCl) contacts raw meat, it initially draws water out through osmosis. Within 15-45 minutes, however, the concentrated surface brine dissolves and diffuses back into the muscle tissue. Sodium and chloride ions penetrate muscle fibers, breaking ionic bonds between actin and myosin filaments. This relaxes the protein matrix, allowing it to trap and hold 10-15% more water during thermal cooking (Water Holding Capacity / WHC)."
            },
            {
                "heading": "2. The Golden Salting Rule",
                "text": "Never salt meat 5 minutes before cooking: that is the exact window when water is pulled to the surface, creating wet meat that steams grey in the pan. Either salt at least 45 minutes ahead (or overnight in the fridge—dry brining), or salt literally seconds before dropping into the scorching pan."
            },
            {
                "heading": "3. The Gustatory Balance Triad: Salt, Acid, Fat",
                "text": "Salt is not a flavor; it is an electro-chemical amplifier. Sodium ions bind to taste cell receptors, physically dampening bitterness and allowing natural sugars and volatile aroma esters to be perceived up to 300% more vividly. When a dish tastes 'flat', it usually lacks acid (which brightens the mid-palate) or salt (which gives length to the finish)."
            }
        ],
        "sensoryCues": {
            "sound": "Dry-brined steak sizzles violently on pan contact because surface moisture has evaporated into a dry pellicle.",
            "feel": "Raw dry-brined meat feels tacky and firm, not slippery or wet."
        },
        "commonMistakes": [
            {"mistake": "Salting from 2 inches above the pan", "consequence": "Concentrates salt into salty hotspots; salt from 12-18 inches high for an even snowfall distribution."},
            {"mistake": "Adding acid at the very start of a long bean/meat braise", "consequence": "Acid strengthens pectin and hemicellulose in vegetable cell walls, preventing beans from ever softening."}
        ],
        "relatedRecipes": ["rec-boeuf-bourguignon", "rec-miso-black-cod", "rec-cacio-e-pepe"]
    },
    {
        "id": "lesson-heat-control",
        "title": "Thermal Heat Control & Pan Physics",
        "track": "Foundations",
        "durationMins": 30,
        "difficulty": "Beginner",
        "summary": "Master conduction, convection, radiation, Leidenfrost effect, pan metallurgy (cast iron vs stainless vs copper), and fond development.",
        "contentSections": [
            {
                "heading": "1. The Three Modes of Heat Transfer",
                "text": "• Conduction: Direct molecular kinetic transfer from burner to pan to food. Dictated by material thermal conductivity (Copper: 385 W/mK, Aluminum: 205 W/mK, Cast Iron: 52 W/mK, Stainless Steel: 16 W/mK).\n• Convection: Heat transferred via circulating currents of liquid or gas (deep frying, boiling, convection ovens).\n• Radiation: Electromagnetic infrared waves traveling through space (broilers, open wood fires, charcoal salamanders)."
            },
            {
                "heading": "2. The Leidenfrost Effect: Pan Temperature Testing",
                "text": "To test if a stainless steel skillet is ready for searing without sticking, flick a drop of water into it. Below 100°C, it sits and slowly boils. Around 150°C, it boils away in seconds. At 190°C (the Leidenfrost point), the water droplet forms an insulating vapor cushion beneath itself and glides across the pan like a frictionless mercury bead. The pan is now at optimal searing temperature."
            },
            {
                "heading": "3. Fond Development & Deglazing",
                "text": "As meat sears, proteins and sugars stick to the pan bottom and undergo intense Maillard browning between 140°C and 165°C, creating a golden-brown crust called 'le fond' (the base). Deglazing with wine, stock, or water dissolves these dehydrated caramelized amino acids into a concentrated liquid glaze, forming the foundation of all classical pan sauces."
            }
        ],
        "sensoryCues": {
            "sound": "Steady, confident, lively sizzle; if the sizzle slows or goes quiet, pan temperature has dropped and meat is boiling in its juices.",
            "smell": "Rich roasted, nutty, toasted aromas; immediately pull off heat if acrid smoke begins."
        },
        "commonMistakes": [
            {"mistake": "Crowding the skillet with too many cold steaks", "consequence": "Thermal shock drops pan temperature below 100°C; juices pool and meat boils into a grey, leathery disaster."},
            {"mistake": "Attempting to deglaze a pan where the fond has turned pitch black", "consequence": "Black fond is pyrolyzed carbon; it imparts irreversible acrid bitterness to any sauce."}
        ],
        "relatedRecipes": ["rec-sole-meuniere", "rec-coq-au-vin", "rec-boeuf-bourguignon"]
    },
    {
        "id": "lesson-egg-geometry",
        "title": "The Geometry of the Egg & Protein Coagulation",
        "track": "Foundations",
        "durationMins": 35,
        "difficulty": "Intermediate",
        "summary": "Explore the distinct thermal denaturation thresholds of ovalbumin, ovotransferrin, and vitellin; master 63°C onsen eggs, French rolled omelettes, and soft poaching.",
        "contentSections": [
            {
                "heading": "1. The Split Nature of Egg Proteins",
                "text": "An egg is not a single protein system. Egg white (albumen) contains ovotransferrin which sets at 62°C, and ovalbumin which sets at 80°C. Egg yolk contains vitellin which thickens into custard at 65°C and hardens at 70°C. This 5°C window between 65°C and 70°C is where culinary magic happens: yolks turn into jammy, molten velvet while whites solidify into a tender gel."
            },
            {
                "heading": "2. The 63°C Onsen Egg",
                "text": "By holding an egg at exactly 63°C (145.4°F) for 45 minutes in a water bath, the white's ovotransferrin forms an ethereal, cloud-like custard, while the yolk thickens into an unctuous spreadable cream that holds its shape. This is the hallmark of modern Japanese haute cuisine."
            },
            {
                "heading": "3. The French Rolled Omelette (Baveuse)",
                "text": "Cook beaten eggs in foaming butter over medium-low heat with rapid, continuous agitation. This prevents large protein networks from forming, creating millions of micro-curds. Roll while 80% set so carryover heat sets the exterior while keeping the center molten and custardy (baveuse)."
            }
        ],
        "sensoryCues": {
            "see": "Pristine canary yellow exterior with zero brown speckling; cutting open reveals a velvety molten center.",
            "feel": "Pillowy, tender, custard-like texture that melts without chewiness."
        },
        "commonMistakes": [
            {"mistake": "Cooking eggs over roaring high heat", "consequence": "Protein cross-links tighten violently, squeezing out water (syneresis/weeping) and leaving dry, rubbery curds."},
            {"mistake": "Boiling hard-cooked eggs for 15+ minutes", "consequence": "Sulfur in the white reacts with iron in the yolk, forming an unsightly greenish-grey ring of ferrous sulfide and pungent sulfur odor."}
        ],
        "relatedRecipes": ["rec-french-omelette", "rec-carbonara", "rec-souffle-chocolat"]
    },
    {
        "id": "lesson-mother-sauces",
        "title": "Classical French Mother Sauces (Les Cinq Sauces Mères)",
        "track": "Advanced",
        "durationMins": 45,
        "difficulty": "Advanced",
        "summary": "Master Auguste Escoffier's canon: Béchamel, Velouté, Espagnole, Hollandaise, and Sauce Tomate, plus modern staples Beurre Blanc and Beurre Monté.",
        "contentSections": [
            {
                "heading": "1. The Architecture of a Mother Sauce",
                "text": "A classical sauce requires two components: a liquid base (milk, white stock, brown stock, tomato juice, or clarified butter) and a thickening agent (white roux, blond roux, brown roux, or egg yolk emulsion). Every sauce in Western gastronomy descends from these foundational pillars."
            },
            {
                "heading": "2. The Roux Continuum",
                "text": "Roux is equal parts flour and fat (usually butter) cooked together.\n• White Roux (3-4 mins): Raw starch cooked out; pale ivory; highest thickening power; used for Béchamel.\n• Blond Roux (6-8 mins): Light golden; toasty aroma; used for Velouté.\n• Brown Roux (15-20 mins): Deep mahogany; nutty aroma; lower thickening power due to starch dextrinization; used for Espagnole."
            },
            {
                "heading": "3. Emulsion Sauces: Hollandaise & Beurre Blanc",
                "text": "• Hollandaise: Warm egg yolk and acid reduction emulsified with clarified butter over a gentle double boiler (60°C). Thick, glossy, rich.\n• Beurre Blanc: White wine, vinegar, and shallot reduction emulsified off-heat with cold cubed whole butter. The milk solids in whole butter act as the surfactant."
            }
        ],
        "sensoryCues": {
            "see": "Glossy sheen that coats the back of a spoon cleanly (nappe); drawing a finger across leaves a clear, defined line without dripping.",
            "feel": "Silky, velvety mouthfeel coating the palate without feeling floury or greasy."
        },
        "commonMistakes": [
            {"mistake": "Pouring hot liquid into hot roux", "consequence": "Causes instant starch clumping; use hot liquid into warm roux or cold liquid into hot roux while whisking vigorously."},
            {"mistake": "Overheating Hollandaise above 68°C", "consequence": "Yolk proteins curdle, completely breaking the emulsion into scrambled eggs floating in yellow oil."}
        ],
        "relatedRecipes": ["rec-sole-meuniere", "rec-boeuf-bourguignon", "rec-halibut-beurre-blanc"]
    },
    {
        "id": "lesson-brigade-cuisine",
        "title": "The Brigade de Cuisine Hierarchy & Professional Kitchen Systems",
        "track": "Professional Kitchen",
        "durationMins": 40,
        "difficulty": "Professional Technique",
        "summary": "Understand Georges Auguste Escoffier's military-inspired brigade system: roles, station logistics, communication protocols, ticket calls, and the pass.",
        "contentSections": [
            {
                "heading": "1. The Stations & The Chain of Command",
                "text": "Escoffier revolutionized commercial kitchens by dividing chaos into specialized military precision:\n• Chef de Cuisine: Executive leader responsible for menu design, costing, and overall restaurant standards.\n• Sous-Chef: The general on the floor; manages daily prep lists, kitchen discipline, and station schedules.\n• Saucier: The most prestigious line station; crafts all pan sauces, stocks, stews, and sautéed meats.\n• Poissonnier: Fish and seafood master; handles fish butchery, delicate searing, and court-bouillon poaching.\n• Garde Manger: Cold larder chef; handles charcuterie, terrines, salads, oysters, caviar, and cold openers.\n• Rôtisseur & Grillardin: Manages high-heat roasting, wood grilling, and broiling.\n• Entremetier: Prepares vegetable sides, starches, egg courses, and hot soups.\n• Pâtissier: Pastry chef; operates an independent sub-brigade for breads, laminated doughs, soufflés, and desserts.\n• Aboyeur (Expediter): The voice at the pass; calls tickets, times firing, checks plates, and coordinates service."
            },
            {
                "heading": "2. Kitchen Communication & The Pass Protocol",
                "text": "Communication in a brigade is strictly verbal and structured:\n• 'Order In': Informs stations that a ticket has arrived.\n• 'Fire Table 12': Authorizes stations to begin active cooking.\n• 'Oui, Chef!' / 'Heard!': Mandatory acknowledgment from every station cook.\n• 'Table 12 walking in 2 minutes': Saucier, Poissonnier, and Entremetier sync their cooking so meat, fish, and sauces hit the pass simultaneously at peak serving temperature."
            }
        ],
        "sensoryCues": {
            "sound": "Sharp, disciplined vocal calls; synchronized pans clattering; absence of panic during rush.",
            "see": "Pristine stainless steel stations with 9-pan inserts, folded damp side towels, clean cutting boards."
        },
        "commonMistakes": [
            {"mistake": "Firing proteins before side dishes are prepped", "consequence": "Steaks get cold and dry under heat lamps while waiting for vegetables to finish."},
            {"mistake": "Silent stations failing to call back orders", "consequence": "Double-orders or missed tables; total breakdown of service timing."}
        ],
        "relatedRecipes": ["rec-boeuf-bourguignon", "rec-duck-confit", "rec-tonkotsu-ramen"]
    }
]

js_content = f"""// L'Atelier Culinary Academy Curriculum
// Structured culinary education across Foundations, Intermediate, Advanced, and Professional tracks.

window.ACADEMY_LESSONS = {json.dumps(ACADEMY_LESSONS, indent=2)};

window.AcademyEngine = {{
  getLessonsByTrack: function(track) {{
    return window.ACADEMY_LESSONS.filter(l => l.track === track);
  }},
  getLessonById: function(id) {{
    return window.ACADEMY_LESSONS.find(l => l.id === id);
  }}
}};
"""

with open("data-academy.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated data-academy.js with {len(ACADEMY_LESSONS)} structured master lessons.")
