// L'Atelier Food Science Simulation Engine
// Mathematical models for thermal physics, emulsion stability, Maillard kinetics, and osmosis.

window.SCIENCE_MODULES = [
  {
    "id": "sci-heat-transfer",
    "title": "Thermal Heat Transfer & Pan Metallurgy",
    "category": "Physics of Cooking",
    "summary": "Understand how conduction, convection, and radiation dictate core cooking curves, and how pan material diffusivity controls hot spots and crust formation.",
    "materials": {
      "copper": {
        "name": "Copper (2.5mm)",
        "conductivity": 385,
        "diffusivity": 111.0,
        "density": 8960,
        "heatCapacity": 385,
        "responsiveness": "Instantaneous (< 2 sec)",
        "description": "Supreme thermal responsiveness; heats with zero hot spots; drops heat instantly when pulled from flame."
      },
      "aluminum": {
        "name": "Clad Aluminum (3.0mm)",
        "conductivity": 205,
        "diffusivity": 84.0,
        "density": 2700,
        "heatCapacity": 900,
        "responsiveness": "Rapid (4-6 sec)",
        "description": "Excellent lateral heat spreader; standard in professional tri-ply restaurant cookware."
      },
      "cast_iron": {
        "name": "Cast Iron (4.5mm)",
        "conductivity": 52,
        "diffusivity": 12.0,
        "density": 7200,
        "heatCapacity": 450,
        "responsiveness": "High Thermal Mass (Slow)",
        "description": "Poor thermal conductor prone to hot spots, but acts as a massive thermal battery that does not drop temperature when cold meat hits the pan."
      },
      "stainless": {
        "name": "Pure Stainless Steel (2.0mm)",
        "conductivity": 16,
        "diffusivity": 4.2,
        "density": 7900,
        "heatCapacity": 500,
        "responsiveness": "Very Slow / Poor Spreader",
        "description": "Poor conductor that hot-spots easily; requires an aluminum or copper core (tri-ply) for effective pan searing."
      }
    },
    "formula": "Heat Flux q = -k * (dT / dx) + h * (T_s - T_inf) + eps * sigma * (T_s^4 - T_surr^4)"
  },
  {
    "id": "sci-emulsion-physics",
    "title": "Emulsion Micro-Physics & Phase Inversion",
    "category": "Physical Chemistry",
    "summary": "How mechanical shear forces break oil into microscopic droplets, how surfactant lecithin stabilizes droplet interfaces, and what triggers catastrophic sauce breaking.",
    "mechanics": {
      "dispersedPhase": "Oil droplets (hydrophobic triglycerides)",
      "continuousPhase": "Aqueous liquid (water, vinegar, lemon juice, milk)",
      "surfactant": "Lecithin (phosphatidylcholine from egg yolk) and casein protein (from milk/butter)",
      "criticalPackingLimit": 0.74,
      "description": "Spheres of equal size cannot physically occupy more than 74% of a given volume. When oil volume fraction exceeds 74% without adding more water, oil droplets are forced into direct physical contact and coalesce into a broken greasy sauce (Phase Inversion Point)."
    }
  },
  {
    "id": "sci-maillard-kinetics",
    "title": "The Maillard Reaction & Caramelization Kinetics",
    "category": "Organic Chemistry",
    "summary": "How reducing sugars and amino acids condense at high heat to create hundreds of volatile flavor compounds, and why surface moisture completely halts the reaction.",
    "parameters": {
      "temperatureThreshold": 140,
      "optimalRange": "140\u00b0C to 165\u00b0C (284\u00b0F to 330\u00b0F)",
      "pyrolysisThreshold": 180,
      "moistureInhibition": "Latent heat of vaporization of water is 2,260 kJ/kg. As long as water is present on meat surface, pan energy is consumed boiling water at 100\u00b0C, pinning temperature far below the 140\u00b0C Maillard threshold."
    }
  },
  {
    "id": "sci-osmosis-brining",
    "title": "Equilibrium (EQ) Brining & Protein Solubilization",
    "category": "Cellular Biology",
    "summary": "Calculate precise equilibrium salt absorption and muscle fiber relaxation without over-salting.",
    "equation": "Target Salt (g) = (Meat Weight + Water Weight) * (Target Salinity % / 100)",
    "salinityBenchmarks": {
      "subtle": 1.0,
      "balanced": 1.25,
      "robust": 1.5,
      "cured": 2.2
    }
  },
  {
    "id": "sci-collagen-gelatin",
    "title": "Collagen Denaturation & Gelatinization Kinetics",
    "category": "Biochemistry",
    "summary": "The thermal conversion of insoluble triple-helix collagen connective tissue into succulent soluble gelatin.",
    "kinetics": {
      "unwindingTemp": "60\u00b0C to 68\u00b0C (tight triple helix relaxes)",
      "hydrolysisTemp": "70\u00b0C to 85\u00b0C (cross-links dissolve into water-soluble gelatin)",
      "boilingToughening": "> 95\u00b0C (myosin and actin severely contract, expressing moisture before gelatin can lubricate fibers)"
    }
  }
];

window.ScienceEngine = {
  // 1. Heat Transfer Pan Simulator
  simulatePanHeating: function(materialKey, thicknessMm, flamePowerWatts) {
    const materials = {
      copper: { k: 385, cp: 385, rho: 8960 },
      aluminum: { k: 205, cp: 900, rho: 2700 },
      cast_iron: { k: 52, cp: 450, rho: 7200 },
      stainless: { k: 16, cp: 500, rho: 7900 }
    };
    const mat = materials[materialKey] || materials.cast_iron;
    const thicknessM = thicknessMm / 1000;
    const areaM2 = 0.05; // 25cm skillet approx
    const massKg = areaM2 * thicknessM * mat.rho;
    
    // Time to reach 180°C searing threshold from 20°C
    const deltaT = 160;
    const heatRequiredJoules = massKg * mat.cp * deltaT;
    const efficiency = 0.55; // gas/induction burner efficiency
    const timeSeconds = heatRequiredJoules / (flamePowerWatts * efficiency);
    
    // Thermal Diffusivity alpha = k / (rho * cp) in mm^2/s
    const alphaMm2s = (mat.k / (mat.rho * mat.cp)) * 1000000;

    return {
      timeToSearSeconds: Math.round(timeSeconds),
      thermalDiffusivity: +alphaMm2s.toFixed(1),
      massKg: +massKg.toFixed(2),
      uniformityScore: Math.min(100, Math.round(alphaMm2s * 0.9))
    };
  },

  // 2. Emulsion Stability Calculator
  simulateEmulsion: function(oilMl, waterMl, yolkCount, shearRpm) {
    const totalMl = oilMl + waterMl;
    const oilFraction = oilMl / totalMl;
    const lecithinG = yolkCount * 1.5; // ~1.5g active phospholipids per egg yolk
    
    // Theoretical droplet diameter (microns): inversely proportional to shear RPM and surfactant
    const dropletMicrons = Math.max(0.5, +(25000 / (shearRpm * Math.sqrt(lecithinG + 0.1))).toFixed(1));
    
    let isBroken = false;
    let reason = "Stable colloidal suspension.";

    if (oilFraction > 0.74) {
      isBroken = true;
      reason = "Oil volume fraction (" + (oilFraction*100).toFixed(0) + "%) exceeds maximum sphere packing limit of 74%. Sauce has inverted and separated.";
    } else if (lecithinG < (oilMl * 0.005)) {
      isBroken = true;
      reason = "Insufficient surfactant to coat the expanded droplet surface area.";
    } else if (shearRpm < 150) {
      isBroken = true;
      reason = "Inadequate mechanical shear force to break bulk oil into micron droplets.";
    }

    const stabilityScore = isBroken ? 0 : Math.round(Math.min(100, (1 - dropletMicrons / 30) * 100));

    return {
      oilFraction: +(oilFraction * 100).toFixed(1),
      dropletDiameterMicrons: dropletMicrons,
      isBroken: isBroken,
      stabilityScore: stabilityScore,
      diagnostic: reason
    };
  },

  // 3. Maillard Reaction Time Delay Calculator
  simulateMaillard: function(surfaceMoisturePct, panTempC) {
    // Moisture in grams per cm2 approx
    const moistureG = surfaceMoisturePct / 100 * 2.5;
    const boilingEnergyJ = moistureG * 2.26; // 2.26 kJ/g latent heat
    const delaySeconds = panTempC <= 100 ? 999 : Math.round((moistureG * 2260) / (panTempC - 100) * 0.6);
    
    let status = "Rapid browning within 10 seconds.";
    if (surfaceMoisturePct > 40) {
      status = "Severe delay: meat will steam grey for " + delaySeconds + " seconds before browning begins.";
    } else if (panTempC < 140) {
      status = "Pan temperature below 140°C threshold: Maillard browning cannot occur.";
    } else if (panTempC > 185) {
      status = "Excessive heat: Risk of surface carbonization (pyrolysis) before core is cooked.";
    }

    return {
      delaySeconds: delaySeconds,
      status: status,
      browningRateScore: Math.max(0, Math.min(100, Math.round((panTempC - 130) * 1.5 - surfaceMoisturePct * 0.8)))
    };
  },

  // 4. Equilibrium Brining Formula
  calculateEQBrine: function(meatGrams, waterGrams, targetSalinityPct) {
    const totalMass = meatGrams + waterGrams;
    const saltGrams = +(totalMass * (targetSalinityPct / 100)).toFixed(1);
    const estHoursToEquilibrium = Math.round(Math.sqrt(meatGrams) * 0.8);

    return {
      saltGrams: saltGrams,
      totalMassGrams: totalMass,
      hoursRecommended: Math.max(8, estHoursToEquilibrium),
      estimatedWaterRetentionGainPct: 11.5
    };
  },

  // 5. Collagen Conversion Kinetic Model
  simulateCollagenConversion: function(braiseTempC, hours) {
    // Simplified Arrhenius model for collagen hydrolysis
    if (braiseTempC < 60) return { conversionPct: 0, tendernessScore: "Tough / Fibrous" };
    const rateConstant = 0.005 * Math.exp(0.065 * (braiseTempC - 60));
    const conversionPct = Math.min(98, Math.round((1 - Math.exp(-rateConstant * hours)) * 100));

    let tenderness = "Spoon-tender, melting gelatin.";
    if (conversionPct < 40) tenderness = "Tough, chewy, under-braised.";
    else if (conversionPct < 70) tenderness = "Softening, but collagen cross-links still noticeable.";

    return {
      conversionPct: conversionPct,
      tendernessScore: tenderness,
      gelatinConcentrationRating: Math.round(conversionPct * 0.9)
    };
  }
};
