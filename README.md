\# L'Atelier: Haute Cuisine Tasting Menu Engine \& Studio



\[!\[Live App](https://img.shields.io/badge/Live-Demo-d4af37?style=for-the-badge\&logo=googlechrome\&logoColor=black)](https://starman1009.github.io/latelier/)

\[!\[License: MIT](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)](LICENSE)



An autonomous gastronomic curation engine designed for high-end degustation menu planning, palate-weight balancing, and back-of-house kitchen logistics.



\---



\## Live Deployment

Access the interactive web app anywhere:

👉 \*\*\[https://starman1009.github.io/latelier/](https://starman1009.github.io/latelier/)\*\*



\---



\## Core Capabilities



\- \*\*Algorithmic Degustation Arc:\*\* Curates 3, 5, or 7-course progressions respecting strict sensory physics:

&#x20; - `Opener`: High-acid raw seafood, amuses, and crudos.

&#x20; - `Mid`: Emulsified shellfish, beurre monté poaches, and handmade pasta.

&#x20; - `Climax`: Deep Maillard roasted proteins (dry-aged duck, calotte de bœuf, squab).

&#x20; - `Predessert`: Palate-cleansing granitas and citrus infusions.

&#x20; - `Dessert`: Technical pâtisserie, ganaches, and deconstructed tarts.

\- \*\*Hero Ingredient Filtering:\*\* Filter the entire corpus by proteins and produce (Wagyu, Duck, Caviar, Scallops, Truffles, Citrus).

\- \*\*Provisions Matrix:\*\* Unified, cross-department grocery consolidation scaled dynamically for 2, 4, 6, or 8 covers with one-click clipboard copying.

\- \*\*Synthesized Audio Timers:\*\* Zero-dependency crystal harmonic chimes powered by the browser's Web Audio API for delicate holding and searing windows.

\- \*\*Local Vault:\*\* Save custom menus directly to persistent browser storage.



\---



\## Local Architecture



```text

latelier/

├── index.html            # Single-page client dashboard \& audio synthesizer

├── recipes.json          # Master metric recipe database

├── super\_harvest.py      # Multi-source scraper (RSS feeds, APIs, culinary archives)

├── audit\_database.py     # Schema auditor, cleaner, and unit validator

├── export\_menu.py        # Plaintext \& print sheet formatter

├── run\_atelier.bat       # 1-click Windows desktop local server launcher

└── manifest.json         # PWA configuration for mobile installation

