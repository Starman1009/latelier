# L’Atelier kitchen

Run `python -m http.server 8000 --bind 127.0.0.1` from this folder and open http://localhost:8000.

The new home page supports local title/ingredient search, online TheMealDB name search, attributed recipe detail, cooking steps, local saved recipes, shopping lists, and backup export/restore. User recipes support known-yield scaling. Online measures remain exactly as returned; unknown yields disable scaling. No private API key or backend is used.

The original interface is preserved at curator.html. Its legacy calculations are not validated. recipes.json and existing local-storage keys were preserved. data-review.json summarizes known catalog defects. Legacy recipes are explicitly discovery-only in the new interface. Automatic catalog rewriting/synthesis is disabled; the workflow now performs a manual read-only JSON check.

TheMealDB test API is for development/personal use. Check https://www.themealdb.com/api.php and current terms before public release; production access may require a supporter key. Provider availability and completeness are not guaranteed. No provider images are copied. Online searches are by recipe name, local searches also search ingredients.

The service worker caches only the app shell. Saved recipes and shopping items live in browser storage. Export backups regularly; there is no cloud recovery. HTTPS or localhost is needed for service workers. PWA installation varies by browser; native app packaging, production icons, and mobile installation validation remain future work.

Remaining: reviewed recipe yields, vetted equipment metadata, timed steps, verified dietary/allergy filters, richer imports/editing, safe unit-aware list aggregation, and production provider configuration. No allergy-safety claims are made.

## Meal generator
The default homepage now composes breakfast, brunch, lunch, or dinner with 2–4 courses. Selected recipe pools are fetched from the live TheMealDB lookup API and checked for ingredients, measures, and instruction content. Locks survive regeneration; individual courses can be swapped. The current menu and prep checks persist locally. Whole-menu shopping retains original quantities. Mise en place includes ingredient staging, source-mentioned equipment, and verbatim preparation excerpts. Source checks do not constitute culinary testing, and no serving yield or schedule is invented.
