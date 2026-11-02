# L’ATELIER · ARCHITECTURAL SPECIFICATION & TECHNICAL BLUEPRINT

## 1. Core Technical Architecture

L’Atelier is engineered as a **Zero-Build, High-Performance Static Web Application & PWA**. It operates entirely client-side with no bundlers, compilation steps, or server-side dependencies.

- **Frontend Runtime:** Vanilla ECMAScript 2022+ (ES6+), Modular IIFE namespaces, Web Components / Template Strings.
- **Styling Architecture:** Modern CSS Grid & Flexbox, CSS Custom Properties (`latelier.css`, `vault.css`, `kitchen.css`).
- **Persistence Layer:** LocalStorage + Web Storage APIs (`atelier_saved_recipes`, `atelier_shopping_v2`, `atelier_user_notes`, `atelier_theme`, `atelier_accomplishments`, `atelier_unit_system`).
- **Hardware & Web APIs:**
  - **Service Worker (`sw.js`):** Offline shell and dataset caching (`atelier-kitchen-v15`).
  - **Web Audio API:** Oscillator-synthesized acoustic chimes for kitchen timers.
  - **Screen Wake Lock API:** Prevents screen dimming during active cooking sessions.
  - **Web Speech API:** SpeechSynthesis for step reading aloud; SpeechRecognition for hands-free voice commands.
  - **SubtleCrypto API:** PBKDF2 key derivation and AES-256-GCM authenticated in-memory decryption for private archives.
  - **Capacitor Mobile Runtime:** Configured native bridge (`capacitor.config.json`) wrapping static assets into Apple Xcode (`WKWebView`).

---

## 2. File Organization & Data Models

```
latelier/
├── index.html                   # Primary entrypoint (13 public views)
├── vault.html                   # Salon Privé (Confidential brigade workspace)
├── latelier.js                  # Core application engine, routing, state, views
├── latelier.css                 # Unified editorial design system & responsive tokens
├── vault.js                     # Private vault decryption and split-pane reader
├── vault.css                    # Private vault luxury executive styling
├── sw.js                        # Progressive Web App offline caching engine
├── manifest.json                # PWA manifest for iOS/Android home screen
├── capacitor.config.json        # Native iOS deployment configuration
├── package.json                 # Dependency manifests for Capacitor iOS builds
├── IOS_DEPLOYMENT_GUIDE.md      # Xcode & TestFlight compilation instructions
│
├── Culinary Datasets:
│   ├── data-recipes.js          # 153 Master recipes (strict 28-field schema)
│   ├── data-flavor.js           # 50 Aroma nodes & molecular pairings
│   ├── data-academy.js          # 4 Culinary tracks & 12 structured lessons
│   ├── data-science.js          # 5 Interactive food physics & kinetics simulations
│   ├── data-encyclopedia.js     # Comprehensive ingredient taxonomy & seasonality
│   ├── data-mastery.js          # Modernist techniques & 19 botanical field notes
│   ├── data-prep-manual.js      # Public operational stub (cards encrypted in vault)
│   └── recipe-sources.js        # Verified external chef recipe references
│
└── Secondary Specialized Views:
    ├── brigade.html             # Multi-recipe backwards timeline & station map
    ├── studio.html              # Plating design studio & Stoneware CAD
    └── curator.html             # Recipe verification & audit workbench
```

---

## 3. Strict 28-Field Recipe Schema Specification

Every recipe in `window.MASTER_RECIPES` adheres to 28 mandatory keys:
1. `id` (unique slug string)
2. `title` (formal title)
3. `cuisine` (geographical or regional tradition)
4. `category` (`breakfast`, `lunch`, `dinner`, `dessert`, `sauce_stock`, `bread`, `appetizer`)
5. `slot` (`opener`, `mid`, `climax`, `predessert`, `dessert`)
6. `difficulty` (`Beginner`, `Intermediate`, `Advanced`, `Professional Technique`)
7. `prepMins` (integer prep minutes)
8. `cookMins` (integer cook minutes)
9. `totalMins` (integer total minutes)
10. `yieldServings` (integer base servings)
11. `heroImage` (URL or verified identifier)
12. `summary` (editorial culinary summary)
13. `dietary` (string array: `vegetarian`, `vegan`, `gluten-free`, `dairy-free`, etc.)
14. `sensoryRole` (sensory balance in a multi-course arc)
15. `ingredients` (array of objects: `name`, `qty`, `unit`, `prep`, `dept`)
16. `equipment` (array of objects: `name`, `type`)
17. `miseEnPlace` (ordered checklist strings)
18. `steps` (array of objects: `stepNum`, `text`, `sensoryCue`, `scienceNote`, `timerMins`)
19. `sensoryIndicators` (visual, tactile, auditory, olfactory doneness cues)
20. `scienceNotes` (molecular transformations)
21. `troubleshooting` (array of objects: `issue`, `solution`)
22. `substitutions` (array of objects: `original`, `substitute`, `notes`)
23. `flavorPairings` (object: `wine`, `zeroProof`, `aromaticComplements`)
24. `advancedTechnique` (specialized chef technique)
25. `storageAndReheating` (refrigeration limits, reheating protocols)
26. `nutritionEstimates` (caloric & macro breakdown estimates)
27. `relatedRecipes` (string array of related recipe IDs)
28. `relatedTechniques` (string array of related technique IDs)

---

## 4. Verification & Quality Gates

The test script `validate_platform.py` verifies:
- UTF-8 encoding across all assets (zero replacement chars `\ufffd`).
- Exact 28-key schema compliance and uniqueness for 150+ master recipes.
- Public/private data boundary isolation (zero confidential text leaked in public stubs).
- Service worker asset caching and version alignment.
- Complete 13-view navigation routing in `index.html`.
