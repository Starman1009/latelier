window.CULINARY_ROADMAP = [
  {
    "id": "track-eggs",
    "title": "Egg Cookery & Foundations",
    "category": "Foundations",
    "icon": "\ud83e\udd5a",
    "color": "#F59E0B",
    "summary": "Master temperature control, curd suspension, and emulsion stability from humble scrambled eggs to classical rolled French omelettes and Hollandaise.",
    "nodes": [
      {
        "id": "node-shakshuka",
        "tier": "Beginner",
        "tierNumber": 1,
        "title": "Poaching in Spiced Aromatics",
        "recipeId": "rec-shakshuka-royale",
        "coreSkill": "Gentle egg poaching in spiced tomato sauce without overcooking the yolks",
        "prereqs": [],
        "difficultyScore": 2.5
      },
      {
        "id": "node-omelette",
        "tier": "Novice",
        "tierNumber": 2,
        "title": "French Rolled Omelette",
        "recipeId": "rec-french-omelette",
        "coreSkill": "High-frequency pan agitation, small creamy curds, and seamless exterior envelope roll with zero browning",
        "prereqs": [
          "node-shakshuka"
        ],
        "difficultyScore": 5.5
      },
      {
        "id": "node-benedict",
        "tier": "Intermediate",
        "tierNumber": 3,
        "title": "Classical Eggs Benedict",
        "recipeId": "rec-eggs-benedict",
        "coreSkill": "Vortex water-bath poaching for teardrop shape and toasted brioche staging",
        "prereqs": [
          "node-omelette"
        ],
        "difficultyScore": 6.0
      },
      {
        "id": "node-hollandaise",
        "tier": "Advanced",
        "tierNumber": 4,
        "title": "Sauce Hollandaise Mastery",
        "recipeId": "rec-sauce-hollandaise",
        "coreSkill": "Sabayon steam whisking to 65\u00b0C, slow clarified butter incorporation into a warm stable emulsion",
        "prereqs": [
          "node-benedict"
        ],
        "difficultyScore": 7.5
      }
    ]
  },
  {
    "id": "track-sauces",
    "title": "Classical Sauces & Pan Architecture",
    "category": "Sauces & Reductions",
    "icon": "\ud83e\udd58",
    "color": "#D4AF37",
    "summary": "From cold emulsified vinaigrettes to brown veal stocks, starch-bound jus li\u00e9, and the electric sweet-sour punch of a classical French gastrique.",
    "nodes": [
      {
        "id": "node-fond-brun",
        "tier": "Intermediate",
        "tierNumber": 3,
        "title": "Master Brown Veal Stock",
        "recipeId": "rec-fond-brun-veau",
        "coreSkill": "Oven bone roasting for Maillard depth, tomato paste pinc\u00e9, 12-hour gentle gelatin extraction",
        "prereqs": [],
        "difficultyScore": 6.5
      },
      {
        "id": "node-cacio-pepe",
        "tier": "Advanced",
        "tierNumber": 4,
        "title": "Starch-Water Mantecatura",
        "recipeId": "rec-cacio-e-pepe",
        "coreSkill": "Emulsifying Pecorino Romano and toasted black pepper with pasta cooking water without clumping or graininess",
        "prereqs": [
          "node-fond-brun"
        ],
        "difficultyScore": 7.5
      },
      {
        "id": "node-duck-gastrique",
        "tier": "Expert",
        "tierNumber": 5,
        "title": "Caramelized Gastrique & Duck Confit",
        "recipeId": "rec-duck-confit",
        "coreSkill": "Simmering sugar to amber caramel, deglazing violently with vinegar, and balancing pan reductions",
        "prereqs": [
          "node-cacio-pepe"
        ],
        "difficultyScore": 8.5
      },
      {
        "id": "node-sole-meuniere",
        "tier": "Master",
        "tierNumber": 6,
        "title": "Beurre Noisette & Pan Deglaze",
        "recipeId": "rec-sole-meuniere",
        "coreSkill": "Hazelnut brown butter foaming, rapid lemon caper deglazing, and gentle whole fish basting",
        "prereqs": [
          "node-duck-gastrique"
        ],
        "difficultyScore": 9.0
      }
    ]
  },
  {
    "id": "track-pastry",
    "title": "P\u00e2tisserie, Custards & Confectionery",
    "category": "Pastry & Baking",
    "icon": "\ud83e\udd50",
    "color": "#EC4899",
    "summary": "Master precise sugar crystallization, egg white foam kinetics, steam expansion in choux pastry, and delicate mirror glaze entremets.",
    "nodes": [
      {
        "id": "node-panna-cotta",
        "tier": "Beginner",
        "tierNumber": 1,
        "title": "Gelatin Hydration & Panna Cotta",
        "recipeId": "rec-panna-cotta",
        "coreSkill": "Cold sheet gelatin blooming, warm dairy infusion, and chilled unmolding",
        "prereqs": [],
        "difficultyScore": 3.0
      },
      {
        "id": "node-creme-brulee",
        "tier": "Intermediate",
        "tierNumber": 3,
        "title": "Cr\u00e8me Br\u00fbl\u00e9e & Torch Caramelization",
        "recipeId": "rec-creme-brulee",
        "coreSkill": "Gentle water-bath baking to 82\u00b0C (180\u00b0F) interior, followed by rapid sugar torching into brittle glass",
        "prereqs": [
          "node-panna-cotta"
        ],
        "difficultyScore": 5.5
      },
      {
        "id": "node-paris-brest",
        "tier": "Advanced",
        "tierNumber": 4,
        "title": "P\u00e2te \u00e0 Choux & Pralin\u00e9 Mousseline",
        "recipeId": "rec-paris-brest",
        "coreSkill": "Stovetop flour gelatinization, egg volume incorporation, steam-lift oven baking, and mousseline piping",
        "prereqs": [
          "node-creme-brulee"
        ],
        "difficultyScore": 7.5
      },
      {
        "id": "node-souffle-chocolat",
        "tier": "Expert",
        "tierNumber": 5,
        "title": "Hot Dark Chocolate Souffl\u00e9",
        "recipeId": "rec-souffle-chocolat",
        "coreSkill": "Meringue folding into dark chocolate base, straight vertical rise along butter-sugared ceramic ramekins",
        "prereqs": [
          "node-paris-brest"
        ],
        "difficultyScore": 8.5
      },
      {
        "id": "node-caneles",
        "tier": "Master",
        "tierNumber": 6,
        "title": "Canel\u00e9s de Bordeaux",
        "recipeId": "rec-caneles-bordeaux",
        "coreSkill": "Beeswax and butter mold seasoning, 48-hour batter rest, dual-temperature baking for lacquered crunch",
        "prereqs": [
          "node-souffle-chocolat"
        ],
        "difficultyScore": 9.2
      }
    ]
  },
  {
    "id": "track-seafood",
    "title": "Seafood & Delicate Proteins",
    "category": "Seafood",
    "icon": "\ud83d\udc1f",
    "color": "#06B6D4",
    "summary": "Master internal temperature precision, skin crisping under moisture control, and the delicate art of knife work for raw fish.",
    "nodes": [
      {
        "id": "node-miso-cod",
        "tier": "Intermediate",
        "tierNumber": 3,
        "title": "Saikyo Miso Cured Black Cod",
        "recipeId": "rec-miso-black-cod",
        "coreSkill": "48-hour sweet white miso osmosis cure, broiler caramelization without scorching",
        "prereqs": [],
        "difficultyScore": 5.8
      },
      {
        "id": "node-sole",
        "tier": "Advanced",
        "tierNumber": 4,
        "title": "Pan-Roasted Dover Sole Meuni\u00e8re",
        "recipeId": "rec-sole-meuniere",
        "coreSkill": "Flour dredging, gentle pan-flipping without tearing, and lemon-caper butter emulsification",
        "prereqs": [
          "node-miso-cod"
        ],
        "difficultyScore": 7.2
      },
      {
        "id": "node-edomae-sushi",
        "tier": "Master",
        "tierNumber": 6,
        "title": "Edomae Nigiri & Shari Rice",
        "recipeId": "rec-edomae-sushi",
        "coreSkill": "Akazu red vinegar seasoning, body-temperature rice grain adhesion, and single-stroke knife slicing",
        "prereqs": [
          "node-sole"
        ],
        "difficultyScore": 9.5
      }
    ]
  },
  {
    "id": "track-meat",
    "title": "Meat, Roasting & Braising Kinetics",
    "category": "Butchery & Roasting",
    "icon": "\ud83e\udd69",
    "color": "#DC2626",
    "summary": "Master the Maillard reaction, pan fond deglazing, and the thermal breakdown of tough collagen into velvety liquid gelatin.",
    "nodes": [
      {
        "id": "node-pan-ribeye",
        "tier": "Novice",
        "tierNumber": 2,
        "title": "Cast-Iron Dry-Aged Ribeye",
        "recipeId": "rec-pan-seared-ribeye",
        "coreSkill": "High-heat surface sear, butter-basting with thyme and garlic, and post-cook resting redistribution",
        "prereqs": [],
        "difficultyScore": 4.5
      },
      {
        "id": "node-boeuf-bourguignon",
        "tier": "Intermediate",
        "tierNumber": 3,
        "title": "Boeuf Bourguignon Traditionnel",
        "recipeId": "rec-boeuf-bourguignon",
        "coreSkill": "Lardons browning, red wine reduction, and 3-hour low-temperature collagen breakdown",
        "prereqs": [
          "node-pan-ribeye"
        ],
        "difficultyScore": 6.8
      },
      {
        "id": "node-birria",
        "tier": "Advanced",
        "tierNumber": 4,
        "title": "Birria de Res & Guajillo Consom\u00e9",
        "recipeId": "rec-birria-res",
        "coreSkill": "Dried chile toasting and pureeing, dual-cut beef braising, and rich consom\u00e9 skim separation",
        "prereqs": [
          "node-boeuf-bourguignon"
        ],
        "difficultyScore": 7.8
      },
      {
        "id": "node-duck-confit-meat",
        "tier": "Expert",
        "tierNumber": 5,
        "title": "Classic Confit de Canard",
        "recipeId": "rec-duck-confit",
        "coreSkill": "24-hour salt and herb curing, 4-hour submerged duck fat poach at 85\u00b0C, and final skin crisping",
        "prereqs": [
          "node-birria"
        ],
        "difficultyScore": 8.5
      }
    ]
  },
  {
    "id": "track-dough-wok",
    "title": "Artisan Dough, Pasta & Wok Craft",
    "category": "Dough & High-Heat",
    "icon": "\ud83c\udf5d",
    "color": "#10B981",
    "summary": "Harness gluten development, long cold fermentation, handmade egg pasta rolling, and extreme-heat wok tossing.",
    "nodes": [
      {
        "id": "node-mapo-tofu",
        "tier": "Novice",
        "tierNumber": 2,
        "title": "Sichuan Wok Blooming & Mapo Tofu",
        "recipeId": "rec-mapo-tofu",
        "coreSkill": "Pixian doubanjiang chile oil blooming, ground beef crisping, and layered cornstarch thickening",
        "prereqs": [],
        "difficultyScore": 4.5
      },
      {
        "id": "node-pizza-margherita",
        "tier": "Intermediate",
        "tierNumber": 3,
        "title": "48-Hour Cold Fermentation Pizza",
        "recipeId": "rec-pizza-margherita",
        "coreSkill": "High-hydration dough kneading, 48-hour cold proofing, and hand-stretching without deflating the cornicione",
        "prereqs": [
          "node-mapo-tofu"
        ],
        "difficultyScore": 6.5
      },
      {
        "id": "node-ragu-bolognese",
        "tier": "Advanced",
        "tierNumber": 4,
        "title": "Handmade Tagliatelle al Rag\u00f9",
        "recipeId": "rec-ragu-bolognese",
        "coreSkill": "00 flour and whole yolk pasta kneading, sheet rolling to translucent 1mm thickness, and slow milk-meat reduction",
        "prereqs": [
          "node-pizza-margherita"
        ],
        "difficultyScore": 7.8
      },
      {
        "id": "node-tonkotsu",
        "tier": "Master",
        "tierNumber": 6,
        "title": "Hakata Tonkotsu Ramen Emulsion",
        "recipeId": "rec-tonkotsu-ramen",
        "coreSkill": "18-hour continuous rolling boil marrow emulsification, chashu sous-vide braise, and alkaline noodle timing",
        "prereqs": [
          "node-ragu-bolognese"
        ],
        "difficultyScore": 9.5
      }
    ]
  }
];
