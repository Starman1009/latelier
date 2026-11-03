/* ==========================================================================
   L'ATELIER · THE DIGITAL CULINARY WORKSHOP & ACADEMY
   Techniques Mastery, Gastronomy Workbench & Botanical Guide
   ========================================================================== */

(() => {
  "use strict";
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  }[c]));

  // Editorial & Accomplished Culinary Image Engine
  window.culinaryImage = (r) => {
    // 1. Check if user logged their own dish photo in accomplishments
    const userAcc = (window.AtelierApp?.state || {})?.accomplishments?.recipes?.[r.id];
    const userPhoto = userAcc?.attempts?.find(a => typeof a.photo === 'string' && /^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+/=]+$/.test(a.photo))?.photo;
    if (userPhoto) {
      return `
        <figure class="culinary-image culinary-image--user-photo">
          <img src="${esc(userPhoto)}" alt="Your cooked preparation of ${esc(r.title)}" class="loaded" style="opacity:1;">
          <figcaption class="culinary-image-badge" style="background:rgba(16,185,129,0.92); color:#fff; box-shadow:0 2px 8px rgba(0,0,0,0.5);">
            ★ Your Dish (${esc(userAcc.resultRating || 5)}/5)
          </figcaption>
        </figure>
      `;
    }

    // 2. Check verified official photography
    const image = window.ATELIER_VERIFIED_IMAGES?.[r.id];
    let src = "";
    if (image?.verified === true && image.src && image.alt && image.source) {
      try {
        const u = new URL(image.src, location.href);
        if (u.protocol === "https:" || u.origin === location.origin) src = u.href;
      } catch {}
    }

    if (src) {
      return `
        <figure class="culinary-image">
          <img src="${esc(src)}" alt="${esc(image.alt)}" loading="lazy" decoding="async" onload="this.classList.add('loaded')" onerror="this.remove()">
          <figcaption class="culinary-image-badge">${esc(r.category || "The culinary workshop")}</figcaption>
        </figure>
      `;
    }

    // 3. Luxurious Bespoke Editorial Art Motif
    const categoryThemes = {
      dessert: { icon: "🍰", gradient: "radial-gradient(ellipse at 70% 30%, rgba(236,72,153,0.18), rgba(212,175,55,0.08) 55%, #08080d 100%)", accent: "#EC4899" },
      breakfast: { icon: "🍳", gradient: "radial-gradient(ellipse at 70% 30%, rgba(245,158,11,0.18), rgba(212,175,55,0.08) 55%, #08080d 100%)", accent: "#F59E0B" },
      lunch: { icon: "🥗", gradient: "radial-gradient(ellipse at 70% 30%, rgba(16,185,129,0.18), rgba(212,175,55,0.08) 55%, #08080d 100%)", accent: "#10B981" },
      dinner: { icon: "🍷", gradient: "radial-gradient(ellipse at 70% 30%, rgba(220,38,38,0.18), rgba(212,175,55,0.1) 55%, #08080d 100%)", accent: "#D4AF37" },
      sauce_stock: { icon: "🥘", gradient: "radial-gradient(ellipse at 70% 30%, rgba(212,175,55,0.22), rgba(180,83,9,0.12) 55%, #08080d 100%)", accent: "#D4AF37" },
      bread: { icon: "🌾", gradient: "radial-gradient(ellipse at 70% 30%, rgba(217,119,6,0.18), rgba(212,175,55,0.08) 55%, #08080d 100%)", accent: "#D97706" },
      appetizer: { icon: "✨", gradient: "radial-gradient(ellipse at 70% 30%, rgba(139,92,246,0.18), rgba(212,175,55,0.08) 55%, #08080d 100%)", accent: "#8B5CF6" }
    };
    const theme = categoryThemes[r.category] || categoryThemes.dinner;

    return `
      <figure class="culinary-image culinary-image--bespoke" style="background:${theme.gradient};">
        <div class="culinary-motif-art">
          <div class="culinary-motif-ring" style="border-color:${theme.accent}35;">
            <span class="culinary-motif-icon">${theme.icon}</span>
          </div>
          <div class="culinary-motif-meta">
            <span class="culinary-motif-cuisine" style="color:${theme.accent};">${esc(r.cuisine)}</span>
            <span class="culinary-motif-title">${esc(r.title)}</span>
          </div>
        </div>
        <figcaption class="culinary-image-badge">${esc((r.category||'').replace('_',' ').toUpperCase())}</figcaption>
      </figure>
    `;
  };

  // =========================================================================
  // VIEW: TECHNIQUES & MODERNIST GASTRONOMY MASTERY
  // =========================================================================
  window.renderMastery = (el) => {
    const data = window.ATELIER_MASTERY || {};
    const techniques = data.techniques || [];

    const categories = [
      "All Techniques",
      "Sauces & Purées",
      "Emulsions & Oils",
      "Modernist Gels",
      "Molecular Transformations"
    ];

    let activeCategory = "All Techniques";
    let searchQuery = "";

    function renderView() {
      const filtered = techniques.filter((t) => {
        const matchesCat = activeCategory === "All Techniques" || t.category === activeCategory;
        const q = searchQuery.toLowerCase().trim();
        const matchesQ = !q ||
          t.title.toLowerCase().includes(q) ||
          t.summary.toLowerCase().includes(q) ||
          t.category.toLowerCase().includes(q) ||
          (t.pairings || []).some((p) => p.toLowerCase().includes(q)) ||
          (t.method || []).some((m) => m.toLowerCase().includes(q));
        return matchesCat && matchesQ;
      });

      el.innerHTML = `
        <section class="hero-editorial">
          <p class="hero-eyebrow">L'ATELIER · MODERNIST GASTRONOMY & TECHNIQUE MASTERY</p>
          <h1 class="hero-title">Culinary Mastery & Sauce Architecture</h1>
          <p class="hero-lead">
            Master the molecular transformations, hydrocolloid kinetics, and vegetable puree techniques that define world-class sauces, fluid gels, and stable emulsions.
          </p>

          <!-- Category Filter Pills -->
          <div class="occasion-bar" style="margin-top:1.5rem;">
            ${categories.map((cat) => `
              <button class="occasion-btn ${activeCategory === cat ? 'active' : ''}" data-cat="${esc(cat)}">
                ${esc(cat)}
              </button>
            `).join('')}
          </div>
        </section>

        <!-- Search Toolbar -->
        <div class="toolbar-container" style="margin-bottom:1.75rem;">
          <div class="form-group" style="grid-column: 1 / -1;">
            <label class="form-label" for="technique-search">Search Techniques, Purees, Gels or Ingredients</label>
            <input type="search" id="technique-search" class="form-input" placeholder="Try 'puree', 'gastrique', 'agar', 'beurre monte', 'spherification'..." value="${esc(searchQuery)}">
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
          <span style="font-size:0.85rem; font-family:var(--font-mono); color:var(--gold-primary);">
            Showing ${filtered.length} of ${techniques.length} master techniques
          </span>
        </div>

        <!-- Techniques Grid -->
        <div class="mastery-cards-grid">
          ${filtered.length ? filtered.map((t) => `
            <article class="bento-card mastery-card" style="border-top: 3px solid ${t.color || 'var(--gold-primary)'};">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem; flex-wrap:wrap; gap:0.5rem;">
                <span class="card-badge" style="border-color:${t.color || 'var(--gold-primary)'}30; color:${t.color || 'var(--gold-primary)'};">
                  ${esc(t.badge || t.category.toUpperCase())}
                </span>
                <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">
                  ${esc(t.category)}
                </span>
              </div>

              <h2 style="font-family:var(--font-serif); font-size:1.6rem; color:var(--text-primary); margin-bottom:0.75rem; line-height:1.2;">
                ${esc(t.title)}
              </h2>

              <p style="font-size:0.95rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
                ${esc(t.summary)}
              </p>

              <!-- Elevation Role Callout -->
              <div class="mastery-callout" style="border-left-color:${t.color || 'var(--gold-primary)'}; margin-bottom:1.25rem;">
                <strong style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:${t.color || 'var(--gold-primary)'}; display:block; margin-bottom:0.35rem;">
                  ✦ The Culinary Elevation
                </strong>
                <p style="font-size:0.875rem; color:var(--text-secondary); line-height:1.6;">
                  ${esc(t.elevationRole)}
                </p>
              </div>

              <!-- Critical Controls Table -->
              ${t.controls ? `
                <div class="mastery-controls-strip" style="margin-bottom:1.25rem;">
                  ${Object.entries(t.controls).map(([k, v]) => `
                    <div class="mastery-control-cell">
                      <span class="mastery-control-label">${esc(k)}</span>
                      <span class="mastery-control-val">${esc(v)}</span>
                    </div>
                  `).join('')}
                </div>
              ` : ''}

              <!-- Method Steps Accordion -->
              <details class="mastery-accordion" open style="margin-bottom:1rem;">
                <summary class="mastery-accordion-summary">
                  Step-by-Step Culinary Method (${t.method.length} Steps)
                </summary>
                <div class="mastery-accordion-body">
                  <ol style="margin-left:1.25rem; display:flex; flex-direction:column; gap:0.6rem; font-size:0.875rem; color:var(--text-secondary); line-height:1.6;">
                    ${t.method.map((step) => `<li>${esc(step)}</li>`).join('')}
                  </ol>
                </div>
              </details>

              <!-- Food Science Note -->
              ${t.scienceNote ? `
                <details class="mastery-accordion" style="margin-bottom:1rem;">
                  <summary class="mastery-accordion-summary" style="color:var(--gold-primary);">
                    🔬 The Molecular Transformation & Chemistry
                  </summary>
                  <div class="mastery-accordion-body">
                    <p style="font-size:0.875rem; color:var(--text-secondary); line-height:1.6;">
                      ${esc(t.scienceNote)}
                    </p>
                  </div>
                </details>
              ` : ''}

              <!-- Troubleshooting -->
              ${(t.troubleshooting && t.troubleshooting.length) ? `
                <details class="mastery-accordion" style="margin-bottom:1rem;">
                  <summary class="mastery-accordion-summary" style="color:var(--amber);">
                    🛠 Chef's Diagnostics & Troubleshooting
                  </summary>
                  <div class="mastery-accordion-body">
                    <div style="display:flex; flex-direction:column; gap:0.6rem; font-size:0.85rem;">
                      ${t.troubleshooting.map((tr) => `
                        <div>
                          <strong style="color:var(--crimson);">${esc(tr.issue)}:</strong>
                          <span style="color:var(--text-secondary);"> ${esc(tr.solution)}</span>
                        </div>
                      `).join('')}
                    </div>
                  </div>
                </details>
              ` : ''}

              <!-- Recipe Pairings -->
              ${(t.pairings && t.pairings.length) ? `
                <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border-subtle);">
                  <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); text-transform:uppercase; display:block; margin-bottom:0.4rem;">
                    Harmonious Plating & Applications:
                  </span>
                  <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
                    ${t.pairings.map((p) => `
                      <span class="recipe-diet-tag" style="background:var(--bg-elevated); color:var(--text-secondary); border-color:var(--border-subtle);">
                        ${esc(p)}
                      </span>
                    `).join('')}
                  </div>
                </div>
              ` : ''}
            </article>
          `).join('') : `
            <div class="bento-card" style="grid-column:1/-1; text-align:center; padding:3rem; color:var(--text-muted);">
              No techniques matched your search criteria. Try a different keyword or select "All Techniques".
            </div>
          `}
        </div>

        <!-- ===================================================================
             HYDROCOLLOID & PUREE DOSING WORKBENCH
             =================================================================== -->
        <section class="bento-card dose-panel-lux" style="margin-top:3.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem; margin-bottom:1.5rem;">
            <div>
              <span class="card-badge" style="color:var(--gold-primary); border-color:var(--border-active);">
                INTERACTIVE CULINARY WORKBENCH
              </span>
              <h2 style="font-family:var(--font-serif); font-size:2rem; margin-top:0.25rem;">
                Hydrocolloid Dosing & Puree Ratio Workbench
              </h2>
              <p style="color:var(--text-secondary); font-size:0.9rem; max-width:680px; margin-top:0.25rem;">
                Calculate exact precision gram weights for hydrocolloid stabilizers, agar fluid gels, sodium alginate baths, and vegetable puree sauce additions based on total liquid weight.
              </p>
            </div>
            <a href="https://www.amazingfoodmadeeasy.com/info/modernist-cooking-blog/more/how-to-measure-modernist-ingredients-ratios" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="font-size:0.8rem;">
              Modernist Ratio Reference ↗
            </a>
          </div>

          <div class="dose-grid-lux">
            <div class="form-group">
              <label class="form-label" for="dose-preset">Culinary Agent & Preset Formulation</label>
              <select id="dose-preset" class="form-select">
                <option value="agar-fluid" data-pct="0.8" data-agent="Agar-Agar">Agar-Agar Fluid Gel (0.80% · Velvet pourable squeeze gel)</option>
                <option value="agar-firm" data-pct="1.2" data-agent="Agar-Agar">Agar-Agar Firm Sliceable Gel (1.20% · Elastic gel)</option>
                <option value="xanthan-light" data-pct="0.15" data-agent="Xanthan Gum">Xanthan Sauce Stabilizer (0.15% · Silk cling, anti-separation)</option>
                <option value="xanthan-coulis" data-pct="0.35" data-agent="Xanthan Gum">Xanthan Coulis Thickener (0.35% · Heavy fruit/herb suspension)</option>
                <option value="kappa-carr" data-pct="0.5" data-agent="Kappa Carrageenan">Kappa Carrageenan Sheet (0.50% · Brittle thermo-reversible gel)</option>
                <option value="alginate-bath" data-pct="0.5" data-agent="Sodium Alginate">Sodium Alginate Bath (0.50% · Distilled water curing bath)</option>
                <option value="calcium-lactate" data-pct="2.0" data-agent="Calcium Lactate Gluconate">Calcium Lactate Gluconate (2.00% · Tasteless core for reverse spheres)</option>
                <option value="puree-sauce" data-pct="25.0" data-agent="Vegetable Puree">Vegetable Puree Sauce Mount (25.0% · Whisked directly into reduced jus)</option>
                <option value="custom" data-pct="1.0" data-agent="Custom Hydrocolloid">Custom Percentage (User-defined tested recipe)</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label" for="dose-mass">Liquid Batch Weight (grams)</label>
              <input id="dose-mass" class="form-input" type="number" min="1" max="100000" value="500" placeholder="e.g. 500">
            </div>

            <div class="form-group">
              <label class="form-label" for="dose-percent">Concentration Percentage (%)</label>
              <input id="dose-percent" class="form-input" type="number" min="0.01" max="100" step="0.01" value="0.80">
            </div>

            <div class="form-group">
              <label class="form-label" for="dose-acid">Liquid Acidity & pH Environment</label>
              <select id="dose-acid" class="form-select">
                <option value="neutral">Near Neutral (pH 5.0–7.0 · Broths, dairy, water)</option>
                <option value="mild-acid">Mildly Acidic (pH 3.5–5.0 · Fruit purees, light wine)</option>
                <option value="high-acid">Highly Acidic (pH < 3.5 · Vinegar, citrus juices, passion fruit)</option>
              </select>
            </div>
          </div>

          <!-- Dynamic Output Card -->
          <div class="dose-result-card">
            <div class="dose-result-primary">
              <span class="dose-result-label">EXACT QUANTITY REQUIRED:</span>
              <output id="dose-result" class="dose-result-value" aria-live="polite">4.000 g Agar-Agar for 500 g liquid</output>
            </div>
            <div id="dose-scale-warning" class="dose-scale-pill">
              ⚖ Precision 0.01g Jeweler Scale Recommended
            </div>
          </div>

          <div id="dose-guidance-box" class="dose-guidance-box">
            <!-- Dynamically populated guidance -->
          </div>
        </section>
      `;

      // Event bindings
      $$(".occasion-btn", el).forEach((btn) => {
        btn.onclick = () => {
          activeCategory = btn.dataset.cat;
          renderView();
        };
      });

      const searchInput = $("#technique-search", el);
      if (searchInput) {
        searchInput.oninput = (e) => {
          searchQuery = e.target.value;
          renderView();
          const updatedInput = $("#technique-search", el);
          if (updatedInput) {
            updatedInput.focus();
            updatedInput.setSelectionRange(updatedInput.value.length, updatedInput.value.length);
          }
        };
      }

      // Workbench Logic
      const presetSel = $("#dose-preset", el);
      const massInput = $("#dose-mass", el);
      const pctInput = $("#dose-percent", el);
      const acidSel = $("#dose-acid", el);
      const resultOut = $("#dose-result", el);
      const scalePill = $("#dose-scale-warning", el);
      const guidanceBox = $("#dose-guidance-box", el);

      function updateCalculator() {
        const mass = parseFloat(massInput.value) || 0;
        const pct = parseFloat(pctInput.value) || 0;
        const selectedOpt = presetSel.options[presetSel.selectedIndex];
        const agent = selectedOpt.getAttribute("data-agent") || "Agent";
        const acid = acidSel.value;

        if (mass <= 0 || pct <= 0) {
          resultOut.textContent = "Please enter valid positive liquid weight and percentage.";
          return;
        }

        const exactGrams = (mass * pct) / 100;
        const formattedGrams = exactGrams >= 10 ? exactGrams.toFixed(1) : exactGrams.toFixed(3);

        resultOut.innerHTML = `<strong>${formattedGrams} g</strong> of ${esc(agent)} for ${mass} g liquid`;

        // Scale resolution guidance
        if (exactGrams < 2.0) {
          scalePill.innerHTML = "⚖ Requires 0.01g Micro-Jeweler Scale (standard kitchen 1g scales cannot measure sub-2g accurately)";
          scalePill.style.color = "var(--amber)";
        } else if (exactGrams < 10.0) {
          scalePill.innerHTML = "⚖ 0.1g Scale Precision Required";
          scalePill.style.color = "var(--gold-primary)";
        } else {
          scalePill.innerHTML = "✓ Standard 1g Digital Kitchen Scale Sufficient";
          scalePill.style.color = "var(--emerald)";
        }

        // Hydration & Chemical Guidance
        let guidanceHtml = "";
        if (agent === "Agar-Agar") {
          guidanceHtml = `
            <strong>Hydration Protocol:</strong> Disperse agar cold with an immersion blender. Bring liquid to a full boil (>90°C / 195°F) and simmer for 2 minutes to completely hydrate polysaccharide double helices.
            ${acid === "high-acid" ? "<br><span style='color:var(--crimson);'>⚠️ High Acidity Warning:</span> Prolonged boiling in high acid weakens agar. Hydrate agar in water/sugar first, then whisk in hot acid reduction at the end of the boil." : ""}
          `;
        } else if (agent === "Xanthan Gum") {
          guidanceHtml = `
            <strong>Hydration Protocol:</strong> Xanthan hydrates equally well in cold or hot liquids without boiling. Sprinkle gradually into a moving blender vortex to prevent insoluble fish-eye clumps.
            ${pct > 0.3 ? "<br><span style='color:var(--amber);'>Note:</span> Concentrations above 0.3% produce thick mucilaginous body; reduce to 0.15% if a clean, pourable pan-sauce cling is desired." : ""}
          `;
        } else if (agent === "Kappa Carrageenan") {
          guidanceHtml = `
            <strong>Hydration Protocol:</strong> Heat to minimum 80°C (176°F) while whisking. Sets rapidly upon cooling below 45°C. Requires potassium (K⁺) or calcium (Ca²⁺) ions in the liquid to form its rigid helical network.
          `;
        } else if (agent === "Sodium Alginate") {
          guidanceHtml = `
            <strong>Hydration Protocol:</strong> Disperse into low-calcium distilled water. Must rest 6–12 hours in refrigerator (or undergo vacuum chamber degassing) to release all microscopic air bubbles before spherification.
          `;
        } else if (agent === "Calcium Lactate Gluconate") {
          guidanceHtml = `
            <strong>Flavor Core Protocol:</strong> Completely tasteless calcium salt. Dissolve directly in your juice, pureed broth, or dairy. If base liquid is thin like water, add 0.2% Xanthan gum to prevent flat droplet spreading.
          `;
        } else if (agent === "Vegetable Puree") {
          guidanceHtml = `
            <strong>Sauce Elevation Protocol:</strong> Cook root vegetables completely tender, blend at maximum shear speed for 2 minutes, and pass through a fine tamis. Whisk directly into reduced pan drippings or deglazed stocks over low heat to add rich body and velvet gloss.
          `;
        } else {
          guidanceHtml = `
            <strong>Precision Protocol:</strong> Confirm dosage against a verified modernist formulation. Always record liquid pH, hydration temperature, and blender shear time for reproducible kitchen results.
          `;
        }

        guidanceBox.innerHTML = guidanceHtml;
      }

      presetSel.onchange = () => {
        const selectedOpt = presetSel.options[presetSel.selectedIndex];
        const defaultPct = selectedOpt.getAttribute("data-pct");
        if (defaultPct && presetSel.value !== "custom") {
          pctInput.value = defaultPct;
        }
        updateCalculator();
      };

      massInput.oninput = updateCalculator;
      pctInput.oninput = () => {
        presetSel.value = "custom";
        updateCalculator();
      };
      acidSel.onchange = updateCalculator;

      updateCalculator();
    }

    renderView();
  };

  // =========================================================================
  // VIEW: BOTANICALS & FINE DINING FINISHING TOUCHES
  // =========================================================================
  window.renderBotanicals = (el) => {
    const data = window.ATELIER_MASTERY || {};
    const flowers = data.flowers || [];
    const microgreens = data.microgreens || [];
    const garnishes = data.garnishes || [];

    const allItems = [
      ...flowers.map((f) => ({ ...f, type: "flower", typeLabel: "Edible Flower" })),
      ...microgreens.map((m) => ({ ...m, type: "microgreen", typeLabel: "Microgreen" })),
      ...garnishes.map((g) => ({ ...g, type: "garnish", typeLabel: "Modernist Finish" }))
    ];

    let activeType = "all";
    let activeFlavorFilter = "all";
    let searchQuery = "";

    const flavorPills = [
      "all",
      "Peppery",
      "Citrus",
      "Cucumber",
      "Floral",
      "Earthy",
      "Tart",
      "Anise"
    ];

    function renderView() {
      const q = searchQuery.toLowerCase().trim();
      const filtered = allItems.filter((item) => {
        const matchesType = activeType === "all" || item.type === activeType;
        const matchesFlavor = activeFlavorFilter === "all" ||
          (item.flavorTags || []).some((ft) => ft.toLowerCase().includes(activeFlavorFilter.toLowerCase()));
        const matchesQ = !q ||
          item.name.toLowerCase().includes(q) ||
          (item.latin || "").toLowerCase().includes(q) ||
          (item.sensory || "").toLowerCase().includes(q) ||
          (item.pairings || "").toLowerCase().includes(q) ||
          (item.flavorTags || []).some((ft) => ft.toLowerCase().includes(q));
        return matchesType && matchesFlavor && matchesQ;
      });

      el.innerHTML = `
        <section class="hero-editorial">
          <p class="hero-eyebrow">L'ATELIER · INGREDIENT FIELD NOTES & FINISHING TOUCHES</p>
          <h1 class="hero-title">Botanicals, Microgreens & Plating Garnishes</h1>
          <p class="hero-lead">
            Select, source, and store edible flowers, microgreens, and luxury modernist garnishes with culinary intent, sensory contrast, and verified food safety.
          </p>

          <!-- Type Navigation Tabs -->
          <div class="occasion-bar" style="margin-top:1.5rem;">
            <button class="occasion-btn ${activeType === 'all' ? 'active' : ''}" data-type="all">All Botanicals (${allItems.length})</button>
            <button class="occasion-btn ${activeType === 'flower' ? 'active' : ''}" data-type="flower">🌸 Edible Flowers (${flowers.length})</button>
            <button class="occasion-btn ${activeType === 'microgreen' ? 'active' : ''}" data-type="microgreen">🌱 Microgreens & Shoots (${microgreens.length})</button>
            <button class="occasion-btn ${activeType === 'garnish' ? 'active' : ''}" data-type="garnish">✨ Modernist Finishes (${garnishes.length})</button>
          </div>
        </section>

        <!-- Critical Food Safety Notice Banner -->
        <aside class="bento-card botanical-safety-card" style="margin-bottom:2rem;">
          <div style="display:flex; gap:1rem; align-items:flex-start;">
            <div style="font-size:2rem; line-height:1; flex-shrink:0;">🛡️</div>
            <div>
              <h2 style="font-family:var(--font-serif); font-size:1.35rem; color:#FFFFFF; margin-bottom:0.35rem;">
                Botanical Identification & Food Safety Standard
              </h2>
              <p style="font-size:0.875rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
                Never use florist flowers, nursery plants, or road-side cuttings: commercial decorative flowers are heavily sprayed with systemic toxic pesticides not approved for human consumption. Use only explicitly certified food-grade botanicals from reputable culinary purveyors.
              </p>
              <div style="display:flex; flex-wrap:wrap; gap:1rem; font-size:0.8rem; font-family:var(--font-mono);">
                <a href="https://www.rhs.org.uk/education-learning/school-gardening/resources/food-growing/edible-flowers" target="_blank" rel="noopener noreferrer" style="color:var(--gold-primary); text-decoration:none;">
                  RHS Edible Flower Standards ↗
                </a>
                <span style="color:var(--border-active);">·</span>
                <span style="color:var(--crimson);">Toxic Lookalikes: Foxglove (Digitalis), Lily of the Valley (Convallaria), Sweet Pea (Lathyrus) are lethal.</span>
              </div>
            </div>
          </div>
        </aside>

        <!-- Search & Flavor Filter Strip -->
        <div class="toolbar-container" style="margin-bottom:1.25rem;">
          <div class="form-group" style="grid-column: 1 / -1;">
            <label class="form-label" for="botanical-search">Search Botanicals by Name, Latin Binomial, Flavor, or Dish Pairing</label>
            <input type="search" id="botanical-search" class="form-input" placeholder="Try 'shiso', 'nasturtium', 'borage', 'peppery', 'crudo', 'duck'..." value="${esc(searchQuery)}">
          </div>
        </div>

        <!-- Flavor Filter Pills -->
        <div class="dietary-filter-row" style="margin-bottom:1.75rem;">
          <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); align-self:center; margin-right:0.5rem; text-transform:uppercase;">
            Flavor Profiles:
          </span>
          ${flavorPills.map((fp) => `
            <button class="dietary-pill ${activeFlavorFilter === fp ? 'active' : ''}" data-flavor="${esc(fp)}">
              ${fp === 'all' ? 'All Flavors' : fp}
            </button>
          `).join('')}
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
          <span style="font-size:0.85rem; font-family:var(--font-mono); color:var(--gold-primary);">
            Showing ${filtered.length} of ${allItems.length} botanical ingredients
          </span>
        </div>

        <!-- Botanicals Grid -->
        <div class="mastery-cards-grid">
          ${filtered.length ? filtered.map((item) => `
            <article class="bento-card botanical-card" style="border-top: 3px solid ${item.color || 'var(--gold-primary)'};">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem; flex-wrap:wrap; gap:0.5rem;">
                <span class="card-badge" style="border-color:${item.color || 'var(--gold-primary)'}35; color:${item.color || 'var(--gold-primary)'};">
                  ${esc(item.typeLabel.toUpperCase())}
                </span>
                <div style="display:flex; align-items:center; gap:0.35rem; font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">
                  <span>INTENSITY:</span>
                  <span style="color:${item.color || 'var(--gold-primary)'}; font-size:0.85rem;">
                    ${'●'.repeat(item.intensity || 3)}${'○'.repeat(5 - (item.intensity || 3))}
                  </span>
                </div>
              </div>

              <h2 style="font-family:var(--font-serif); font-size:1.6rem; color:var(--text-primary); margin:0.25rem 0 0.15rem 0; line-height:1.2;">
                ${esc(item.name)}
              </h2>

              ${item.latin ? `
                <div style="font-family:var(--font-serif); font-style:italic; font-size:0.95rem; color:var(--gold-primary); margin-bottom:0.75rem;">
                  ${esc(item.latin)}
                </div>
              ` : ''}

              <!-- Flavor Pills -->
              ${(item.flavorTags && item.flavorTags.length) ? `
                <div style="display:flex; flex-wrap:wrap; gap:0.35rem; margin-bottom:1rem;">
                  ${item.flavorTags.map((tag) => `
                    <span class="recipe-diet-tag" style="background:${item.color || 'var(--gold-primary)'}15; color:${item.color || 'var(--gold-primary)'}; border-color:${item.color || 'var(--gold-primary)'}30;">
                      ${esc(tag)}
                    </span>
                  `).join('')}
                </div>
              ` : ''}

              <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
                ${esc(item.sensory)}
              </p>

              <!-- Plating & Pairings Callout -->
              ${item.pairings ? `
                <div class="mastery-callout" style="border-left-color:${item.color || 'var(--gold-primary)'}; margin-bottom:1rem;">
                  <strong style="font-family:var(--font-mono); font-size:0.72rem; text-transform:uppercase; color:${item.color || 'var(--gold-primary)'}; display:block; margin-bottom:0.3rem;">
                    ✦ Fine Dining Pairings & Plating
                  </strong>
                  <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                    ${esc(item.pairings)}
                  </p>
                </div>
              ` : ''}

              <!-- Preparation & Parts Used -->
              ${item.prepNotes ? `
                <div style="background:var(--bg-elevated); padding:0.85rem 1rem; border-radius:var(--radius-md); margin-bottom:1rem; font-size:0.825rem; line-height:1.5; color:var(--text-secondary);">
                  <strong style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); text-transform:uppercase; display:block; margin-bottom:0.25rem;">
                    Preparation & Anatomy:
                  </strong>
                  ${esc(item.prepNotes)}
                </div>
              ` : ''}

              <!-- Storage & Longevity Footer -->
              <div style="margin-top:auto; padding-top:0.85rem; border-top:1px solid var(--border-subtle); display:flex; flex-direction:column; gap:0.35rem; font-size:0.78rem; font-family:var(--font-mono); color:var(--text-muted);">
                ${item.storage ? `<div><span style="color:var(--text-secondary);">Storage:</span> ${esc(item.storage)}</div>` : ''}
                ${item.sourcing ? `<div><span style="color:var(--text-secondary);">Source:</span> ${esc(item.sourcing)}</div>` : ''}
              </div>
            </article>
          `).join('') : `
            <div class="bento-card" style="grid-column:1/-1; text-align:center; padding:3rem; color:var(--text-muted);">
              No botanicals matched your search criteria. Try a different keyword or filter.
            </div>
          `}
        </div>

        <!-- ===================================================================
             SOURCING & KITCHEN STAGING DIRECTORY
             =================================================================== -->
        <section class="bento-card" style="margin-top:3.5rem;">
          <span class="card-badge">PROFESSIONAL KITCHEN STANDARDS</span>
          <h2 style="font-family:var(--font-serif); font-size:2rem; margin-top:0.25rem; margin-bottom:0.5rem;">
            Sourcing, Germination & Kitchen Staging Protocols
          </h2>
          <p style="color:var(--text-secondary); line-height:1.6; max-width:760px; margin-bottom:1.75rem;">
            How Michelin-starred kitchens manage microgreens, fresh blossoms, and delicate finishing botanicals to guarantee peak visual turgor, aroma, and longevity.
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:1.5rem;">
            <div class="bento-card" style="background:var(--bg-elevated); padding:1.25rem;">
              <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--gold-primary); margin-bottom:0.5rem;">
                Verified Purveyors
              </h3>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
                Order from specialized regenerative farms that declare botanical species, harvest day, and zero synthetic systemic sprays.
              </p>
              <ul style="font-size:0.825rem; color:var(--text-muted); display:flex; flex-direction:column; gap:0.4rem; padding-left:1.2rem;">
                <li><strong>The Chef's Garden (Huron, OH):</strong> Global leader in microgreens and edible blooms.</li>
                <li><strong>Gourmet Sweet Botanicals (Central Coast, CA):</strong> Overnight fine dining flower shipping.</li>
                <li><strong>Modernist Pantry:</strong> Tested food-grade pure hydrocolloids and calcium salts.</li>
                <li><strong>Kalustyan's (NYC):</strong> Rare dried botanicals, saffron, and floral waters.</li>
              </ul>
            </div>

            <div class="bento-card" style="background:var(--bg-elevated); padding:1.25rem;">
              <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--emerald); margin-bottom:0.5rem;">
                Kitchen Storage & Turgor
              </h3>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
                Moisture control is paramount. Excess water breeds fungal rot; dry air causes instantaneous wilting.
              </p>
              <ul style="font-size:0.825rem; color:var(--text-muted); display:flex; flex-direction:column; gap:0.4rem; padding-left:1.2rem;">
                <li><strong>Temperature:</strong> Hold at 36°F–38°F (2°C–3°C) in high-humidity crispers.</li>
                <li><strong>The Lint-Free Towel Method:</strong> Line airtight plastic deli containers with lightly damp, wrung-out paper towels.</li>
                <li><strong>Ethylene Protection:</strong> Store away from apples, melons, and bananas to prevent petal drop.</li>
                <li><strong>Wash Timing:</strong> Never wash in advance. Pluck dry with tweezers at pickup.</li>
              </ul>
            </div>

            <div class="bento-card" style="background:var(--bg-elevated); padding:1.25rem;">
              <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:var(--amber); margin-bottom:0.5rem;">
                Microgreen Germination
              </h3>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
                Growing on-site ensures ultimate crispness and zero transit damage.
              </p>
              <ul style="font-size:0.825rem; color:var(--text-muted); display:flex; flex-direction:column; gap:0.4rem; padding-left:1.2rem;">
                <li><strong>Seed Quality:</strong> Use untreated, certified pathogen-tested seeds specifically meant for sprouting.</li>
                <li><strong>Air Circulation:</strong> Small oscillating fans prevent damping-off mold.</li>
                <li><strong>Harvest Stage:</strong> Cut at 7–14 days as first true leaves emerge past the initial cotyledons.</li>
                <li><a href="https://extension.psu.edu/the-abcs-of-microgreens" target="_blank" rel="noopener noreferrer" style="color:var(--gold-primary);">Penn State Microgreen Guide ↗</a></li>
              </ul>
            </div>
          </div>
        </section>
      `;

      // Event bindings
      $$(".occasion-btn", el).forEach((btn) => {
        btn.onclick = () => {
          activeType = btn.dataset.type;
          renderView();
        };
      });

      $$(".dietary-pill", el).forEach((pill) => {
        pill.onclick = () => {
          activeFlavorFilter = pill.dataset.flavor;
          renderView();
        };
      });

      const searchInput = $("#botanical-search", el);
      if (searchInput) {
        searchInput.oninput = (e) => {
          searchQuery = e.target.value;
          renderView();
          const updatedInput = $("#botanical-search", el);
          if (updatedInput) {
            updatedInput.focus();
            updatedInput.setSelectionRange(updatedInput.value.length, updatedInput.value.length);
          }
        };
      }
    }

    renderView();
  };
})();
