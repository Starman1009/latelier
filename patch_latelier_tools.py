# -*- coding: utf-8 -*-
"""
Expands renderToolsView and adds openEncyclopediaModal in latelier.js
"""

new_tools_code = '''  // =========================================================================
  // VIEW: 8. CULINARY STUDIO, SAUCE BUILDER, CALCULATORS & ENCYCLOPEDIA
  // =========================================================================
  function renderToolsView(container) {
    const ingredients = window.ENCYCLOPEDIA_INGREDIENTS || [];
    const categories = ["All", "Alliums", "Produce", "Herbs", "Acids & Citrus", "Dairy & Fats", "Seafood", "Meat & Poultry", "Ferments & Umami", "Spices", "Grains & Starches"];
    let activeCategory = "All";
    let searchQuery = "";

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">THE CULINARY STUDIO & WORKSHOP</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Culinary Studio & Workshop Tools</h1>
        <p style="color:var(--text-secondary); max-width:760px;">Interactive ceramic plating canvas, Classical French Sauce Builder, precision kitchen calculators, diagnostic troubleshooter, and the complete Master Ingredient Encyclopedia.</p>
      </section>

      <!-- Advanced Studios Gateway -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1rem; margin-bottom:2.5rem;">
        <a href="studio.html" class="bento-card" style="text-decoration:none; display:flex; justify-content:space-between; align-items:center; border:1px solid var(--gold-border); background:linear-gradient(135deg, rgba(212,175,55,0.06), transparent);">
          <div>
            <span class="card-badge">LAB WORKSPACE 01</span>
            <h3 style="font-size:1.2rem; font-family:var(--font-serif); color:var(--text-primary); margin:0.25rem 0;">3D Stoneware CAD & Volatiles</h3>
            <p style="font-size:0.75rem; color:var(--text-muted);">45° seated guest perspective, GC-MS compound graphs, and thermal physics.</p>
          </div>
          <span style="font-size:1.5rem; color:var(--gold-primary);">→</span>
        </a>

        <a href="brigade.html" class="bento-card" style="text-decoration:none; display:flex; justify-content:space-between; align-items:center; border:1px solid rgba(16,185,129,0.3); background:linear-gradient(135deg, rgba(16,185,129,0.06), transparent);">
          <div>
            <span class="card-badge" style="color:var(--emerald); border-color:var(--emerald);">LAB WORKSPACE 02</span>
            <h3 style="font-size:1.2rem; font-family:var(--font-serif); color:var(--text-primary); margin:0.25rem 0;">Sous-Chef Brigade & Live Pass KDS</h3>
            <p style="font-size:0.75rem; color:var(--text-muted);">13-Point conversion, multi-recipe backward timeline from T-0, and kitchen stations.</p>
          </div>
          <span style="font-size:1.5rem; color:var(--emerald);">→</span>
        </a>
      </div>

      <!-- Plating Canvas Studio -->
      <div class="bento-card" style="margin-bottom:3rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
          <div>
            <span class="card-badge">PLATING STUDIO</span>
            <h2 style="font-size:1.6rem; font-family:var(--font-serif);">Ceramic Plating Canvas</h2>
            <p style="font-size:0.8rem; color:var(--text-muted);">Design visual presentations: swooshes, quenelles, emulsion drops, and garnish scatters.</p>
          </div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <select id="plating-vessel" class="form-select" style="font-size:0.8rem; padding:0.3rem 0.6rem;">
              <option value="slate">Dark Slate Stoneware</option>
              <option value="porcelain">White Limoges Porcelain</option>
              <option value="bowl">Rimmed Coupe Bowl</option>
            </select>
            <select id="plating-brush" class="form-select" style="font-size:0.8rem; padding:0.3rem 0.6rem;">
              <option value="puree">Purée Swoosh</option>
              <option value="dots">Sauce Dots</option>
              <option value="protein">Main Protein</option>
              <option value="herbs">Micro-Greens</option>
            </select>
            <button id="btn-clear-canvas" class="btn-secondary" style="font-size:0.8rem; padding:0.3rem 0.7rem;">Clear Canvas</button>
          </div>
        </div>

        <div style="display:flex; justify-content:center; background:var(--bg-elevated); padding:1.5rem; border-radius:var(--radius-lg); overflow:hidden;">
          <canvas id="plating-canvas" width="600" height="400" style="border-radius:var(--radius-md); box-shadow:var(--shadow-lg); cursor:crosshair; max-width:100%; height:auto;"></canvas>
        </div>
      </div>

      <!-- Interactive Sauce Builder -->
      <div class="bento-card" style="margin-bottom:3rem;">
        <span class="card-badge">GASTRONOMIC ARCHITECTURE</span>
        <h2 style="font-size:1.6rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Classical Sauce Builder</h2>
        <p style="font-size:0.85rem; color:var(--text-secondary); margin-bottom:1.5rem;">Select your liquid base, aromatic reduction, and finish to architect Escoffier derivative sauces.</p>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label class="form-label">1. Foundational Base:</label>
            <select id="sauce-base" class="form-select" style="width:100%;">
              <option value="hollandaise">Egg Yolk & Acid Emulsion (Hollandaise/Béarnaise)</option>
              <option value="veloute">Blond Roux & White Stock (Velouté)</option>
              <option value="bechamel">White Roux & Whole Milk (Béchamel)</option>
              <option value="espagnole">Brown Roux & Veal Stock (Espagnole / Demi-Glace)</option>
              <option value="beurre_blanc">White Wine Reduction & Cold Butter (Beurre Blanc)</option>
              <option value="fond">Seared Pan Fond & Wine Deglaze (Pan Sauce)</option>
            </select>
          </div>

          <div>
            <label class="form-label">2. Aromatic Infusion / Reduction:</label>
            <select id="sauce-aromatic" class="form-select" style="width:100%;">
              <option value="shallot_tarragon">French Grey Shallots, Tarragon & White Wine Vinegar</option>
              <option value="mushrooms_madeira">Sautéed Morels, Shallots & Sweet Madeira Wine</option>
              <option value="peppercorn_cognac">Cracked Tellicherry Peppercorns & Flambéed Cognac</option>
              <option value="tomato_choron">Concentrated Tomato Purée & Fresh Chervil</option>
              <option value="mornay_cheese">Aged Gruyère AOP, Parmigiano-Reggiano & Nutmeg</option>
              <option value="fines_herbes">Fresh Chives, Parsley, Tarragon & Chervil</option>
            </select>
          </div>

          <div>
            <label class="form-label">3. Finishing Technique:</label>
            <select id="sauce-finish" class="form-select" style="width:100%;">
              <option value="monter_beurre">Monter au Beurre (Cold Cubed Cultured Butter Off-Heat)</option>
              <option value="creme_fraiche">Swirled Cultured Crème Fraîche</option>
              <option value="liaison_egg">Liaison of Egg Yolks & Heavy Cream</option>
              <option value="citrus_drops">Fresh Lemon Juice & Chopped Herbs</option>
            </select>
          </div>
        </div>

        <div id="sauce-builder-result" style="background:var(--bg-elevated); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle);">
          <!-- Dynamic sauce output -->
        </div>
      </div>

      <!-- Calculators & Diagnostics Grid -->
      <div class="bento-grid" style="margin-bottom:3.5rem;">
        <!-- Baker's Percentage Calculator -->
        <article class="bento-card">
          <span class="card-badge">BAKER'S MATH</span>
          <h3 class="card-title">Baker's Percentage Calculator</h3>
          <p class="card-desc">Calculate exact hydration and dough weights where total flour equals 100%.</p>
          <div style="display:flex; flex-direction:column; gap:0.6rem; margin:1rem 0;">
            <label class="form-label">Total Flour (g): <input type="number" id="calc-flour" class="form-input" value="500"></label>
            <label class="form-label">Hydration (%): <input type="number" id="calc-hydration" class="form-input" value="75"></label>
            <label class="form-label">Salt (%): <input type="number" id="calc-salt-pct" class="form-input" value="2.2" step="0.1"></label>
          </div>
          <div id="bakers-output" style="background:var(--bg-elevated); padding:0.75rem; border-radius:var(--radius-md); font-family:var(--font-mono); font-size:0.8rem;">
            <!-- Output calculated -->
          </div>
        </article>

        <!-- EQ Brining Matrix -->
        <article class="bento-card">
          <span class="card-badge">PRECISE SALTING</span>
          <h3 class="card-title">Equilibrium (EQ) Brine Calculator</h3>
          <p class="card-desc">Calculate exact salt to reach equilibrium without danger of over-salting.</p>
          <div style="display:flex; flex-direction:column; gap:0.6rem; margin:1rem 0;">
            <label class="form-label">Meat Weight (g): <input type="number" id="eq-meat" class="form-input" value="1000"></label>
            <label class="form-label">Water Weight (g): <input type="number" id="eq-water" class="form-input" value="1000"></label>
            <label class="form-label">Target Salinity (%): <input type="number" id="eq-target" class="form-input" value="1.25" step="0.05"></label>
          </div>
          <div id="eq-output" style="background:var(--bg-elevated); padding:0.75rem; border-radius:var(--radius-md); font-family:var(--font-mono); font-size:0.8rem;">
            <!-- Output calculated -->
          </div>
        </article>

        <!-- Meat Temperature & Carryover Guide -->
        <article class="bento-card">
          <span class="card-badge">THERMAL KINETICS</span>
          <h3 class="card-title">Internal Doneness & Resting Guide</h3>
          <p class="card-desc">Thermal carryover calculation and intra-muscular moisture reabsorption.</p>
          <div style="display:flex; flex-direction:column; gap:0.6rem; margin:1rem 0;">
            <label class="form-label">Protein Cut:
              <select id="meat-cut-select" class="form-select">
                <option value="ribeye">Prime Beef Ribeye / Strip</option>
                <option value="lamb">Rack of Lamb</option>
                <option value="duck">Moulard Duck Breast</option>
                <option value="salmon">King Salmon Fillet</option>
                <option value="pork">Pork Loin / Tenderloin</option>
              </select>
            </label>
            <label class="form-label">Desired Doneness:
              <select id="meat-done-select" class="form-select">
                <option value="rare">Rare (50°C - 52°C)</option>
                <option value="med_rare" selected>Medium-Rare (54°C - 56°C)</option>
                <option value="med">Medium (58°C - 60°C)</option>
              </select>
            </label>
          </div>
          <div id="meat-output" style="background:var(--bg-elevated); padding:0.75rem; border-radius:var(--radius-md); font-family:var(--font-mono); font-size:0.8rem;">
            <!-- Output calculated -->
          </div>
        </article>

        <!-- Recipe Troubleshooter -->
        <article class="bento-card">
          <span class="card-badge">DIAGNOSTICS</span>
          <h3 class="card-title">Culinary Troubleshooter</h3>
          <p class="card-desc">Instant scientific remedies for broken sauces, dry meats, or oversalted soups.</p>
          <select id="troubleshoot-select" class="form-select" style="width:100%; margin:1rem 0;">
            <option value="broken-emulsion">My butter / Hollandaise sauce broke into oil</option>
            <option value="dry-meat">My seared steak is tough and grey inside</option>
            <option value="oversalted">My reduction or soup is too salty</option>
            <option value="dense-bread">My bread didn't rise and crumb is dense</option>
            <option value="scorched-garlic">My garlic turned brown and smells bitter in the pan</option>
            <option value="soggy-skin">My fish skin is soft and stuck to the stainless pan</option>
          </select>
          <div id="troubleshoot-output" style="background:var(--bg-elevated); padding:1rem; border-radius:var(--radius-md); font-size:0.85rem; color:var(--text-secondary);">
            Whisk 1 tablespoon of boiling water into a clean bowl, then slowly whisk the broken sauce into it off heat. The fresh water phase restores the continuous phase.
          </div>
        </article>
      </div>

      <!-- MASTER INGREDIENT ENCYCLOPEDIA -->
      <section style="margin-top:4rem;">
        <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:1rem; margin-bottom:1.5rem;">
          <div>
            <span class="card-badge">INGREDIENT ENCYCLOPEDIA</span>
            <h2 style="font-size:2rem; font-family:var(--font-serif); margin-top:0.25rem;">Master Ingredient Encyclopedia</h2>
            <p style="font-size:0.875rem; color:var(--text-muted);">${ingredients.length} comprehensive dossiers on culinary behaviors, cellular chemistry, storage, and affinities.</p>
          </div>

          <div style="width:100%; max-width:320px;">
            <input type="text" id="encyclopedia-search" class="form-input" placeholder="Search 61 dossiers by name, science role, or affinity..." style="width:100%;">
          </div>
        </div>

        <!-- Category Filter Pills -->
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:2rem;">
          ${categories.map((c, i) => `
            <button class="nav-pill btn-encyclo-cat ${i === 0 ? 'active' : ''}" data-cat="${c}">
              ${esc(c)}
            </button>
          `).join('')}
        </div>

        <!-- Dossiers Grid -->
        <div id="encyclopedia-grid" class="bento-grid">
          <!-- Rendered dynamically -->
        </div>
      </section>
    `;

    // Plating Studio Canvas Engine
    const canvas = $("#plating-canvas", container);
    if (canvas) {
      const ctx = canvas.getContext("2d");
      let currentVessel = "slate";

      function drawVessel(vessel) {
        currentVessel = vessel;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (vessel === "slate") {
          ctx.fillStyle = "#121218";
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.beginPath();
          ctx.arc(canvas.width / 2, canvas.height / 2, 180, 0, Math.PI * 2);
          ctx.fillStyle = "#181822";
          ctx.fill();
          ctx.strokeStyle = "rgba(255,255,255,0.06)";
          ctx.lineWidth = 4;
          ctx.stroke();
        } else if (vessel === "porcelain") {
          ctx.fillStyle = "#EAEAEA";
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.beginPath();
          ctx.arc(canvas.width / 2, canvas.height / 2, 180, 0, Math.PI * 2);
          ctx.fillStyle = "#FFFFFF";
          ctx.fill();
          ctx.strokeStyle = "rgba(0,0,0,0.08)";
          ctx.lineWidth = 4;
          ctx.stroke();
        } else {
          ctx.fillStyle = "#26262B";
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.beginPath();
          ctx.arc(canvas.width / 2, canvas.height / 2, 150, 0, Math.PI * 2);
          ctx.fillStyle = "#16161B";
          ctx.fill();
        }
      }

      drawVessel("slate");

      $("#plating-vessel", container).onchange = (e) => drawVessel(e.target.value);
      $("#btn-clear-canvas", container).onclick = () => drawVessel(currentVessel);

      let isDrawing = false;
      canvas.onmousedown = (e) => { isDrawing = true; paint(e); };
      canvas.onmousemove = (e) => { if (isDrawing) paint(e); };
      window.addEventListener("mouseup", () => { isDrawing = false; });

      function paint(e) {
        const rect = canvas.getBoundingClientRect();
        const x = (e.clientX - rect.left) * (canvas.width / rect.width);
        const y = (e.clientY - rect.top) * (canvas.height / rect.height);
        const brush = $("#plating-brush", container).value;

        if (brush === "puree") {
          ctx.fillStyle = "rgba(212, 175, 55, 0.75)";
          ctx.beginPath();
          ctx.arc(x, y, 16, 0, Math.PI * 2);
          ctx.fill();
        } else if (brush === "dots") {
          ctx.fillStyle = "rgba(225, 29, 72, 0.9)";
          ctx.beginPath();
          ctx.arc(x, y, 6, 0, Math.PI * 2);
          ctx.fill();
        } else if (brush === "protein") {
          ctx.fillStyle = "#78350F";
          ctx.beginPath();
          ctx.roundRect(x - 30, y - 20, 60, 40, 6);
          ctx.fill();
        } else if (brush === "herbs") {
          ctx.fillStyle = "#10B981";
          ctx.fillRect(x, y, 4, 8);
        }
      }
    }

    // Dynamic Sauce Builder
    function updateSauceBuilder() {
      const b = $("#sauce-base", container).value;
      const a = $("#sauce-aromatic", container).value;
      const f = $("#sauce-finish", container).value;

      let name = "Classical French Emulsion";
      let classification = "Derivative Mother Sauce";
      let pairing = "Prime beef, roasted poultry, or poached fish";
      let procedure = "Deglaze pan fond, reduce aromatics to au sec, and whisk in finishing fat off-heat.";

      if (b === "hollandaise" && a === "shallot_tarragon") {
        name = "Sauce Béarnaise";
        classification = "Escoffier Classical Warm Emulsion";
        pairing = "Grilled Côte de Boeuf, dry-aged ribeye, chateaubriand";
        procedure = "Reduce white wine vinegar with French grey shallots and tarragon stems to 1 tablespoon. Whisk egg yolks over gentle double boiler (60°C) until ribbony. Slowly stream in clarified butter. Finish with chopped fresh tarragon and chervil.";
      } else if (b === "hollandaise" && a === "tomato_choron") {
        name = "Sauce Choron";
        classification = "Derivative of Sauce Béarnaise";
        pairing = "Steak frites, roasted duck, grilled lamb chops";
        procedure = "Prepare a classic Béarnaise emulsion base. Off-heat, gently fold in warm, reduced San Marzano tomato fondue and fresh chervil until the sauce takes on a luxurious coral-pink hue.";
      } else if (b === "bechamel" && a === "mornay_cheese") {
        name = "Sauce Mornay";
        classification = "Enriched Mother Sauce";
        pairing = "Gratin of endives, seafood coquilles St-Jacques, Macaroni au Gratin";
        procedure = "Whisk whole warm milk into pale white roux until thick and bubbling. Pull off flame; fold in shredded aged Gruyère AOP, Parmigiano-Reggiano, and a grating of fresh nutmeg. Broil until bubbling and bronzed.";
      } else if (b === "veloute" && f === "liaison_egg") {
        name = "Sauce Allemande / Parisienne";
        classification = "Supreme Velouté Derivative";
        pairing = "Poached capon, veal sweetbreads, steamed white asparagus";
        procedure = "Enrich white chicken/veal velouté with a liaison of egg yolks and heavy cream tempered slowly over low heat without boiling (keep below 72°C to prevent curdling). Finish with lemon drops.";
      } else if (b === "espagnole" && a === "peppercorn_cognac") {
        name = "Sauce Poivrade / au Poivre";
        classification = "Classic Grand Brown Sauce";
        pairing = "Steak au Poivre, venison loin, roasted squab";
        procedure = "Crush Tellicherry peppercorns coarsely in a mortar. Flambé with French Cognac in the fond skillet. Add veal brown stock / demi-glace and reduce by half. Monter au beurre with cold cultured butter off-heat.";
      } else if (b === "beurre_blanc") {
        name = "Sauce Beurre Blanc Nantais";
        classification = "Warm Cultured Butter Emulsion";
        pairing = "Pan-seared sole, wild salmon, diver sea scallops";
        procedure = "Simmer minced French shallots in dry Muscadet wine and white wine vinegar until syrupy (au sec). Whisk in ice-cold cubed butter piece by piece over very low heat. Milk solids in butter act as surfactant.";
      } else {
        name = "Sauce Pan Glaze Gastronomique";
        classification = "Modern Classical Pan Reduction";
        pairing = "Pan-roasted proteins and roasted seasonal root vegetables";
        procedure = "Pour off scorched grease. Sweat aromatics in fond residue. Deglaze with wine, reduce by 80%, and swirl in cold butter off-heat until sauce forms a mirror glaze that coats the back of a spoon.";
      }

      $("#sauce-builder-result", container).innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem;">
          <div>
            <span class="card-badge" style="color:var(--gold-primary); border-color:var(--gold-primary);">${esc(classification)}</span>
            <h3 style="font-size:1.5rem; font-family:var(--font-serif); margin-top:0.25rem;">${esc(name)}</h3>
          </div>
          <span style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted);">RECOMMENDED PAIRING: <strong>${esc(pairing)}</strong></span>
        </div>
        <p style="font-size:0.875rem; color:var(--text-secondary); line-height:1.6;">${esc(procedure)}</p>
      `;
    }

    $("#sauce-base", container).onchange = updateSauceBuilder;
    $("#sauce-aromatic", container).onchange = updateSauceBuilder;
    $("#sauce-finish", container).onchange = updateSauceBuilder;
    updateSauceBuilder();

    // Calculators
    function updateBakers() {
      const flour = parseFloat($("#calc-flour", container).value) || 0;
      const hyd = parseFloat($("#calc-hydration", container).value) || 0;
      const salt = parseFloat($("#calc-salt-pct", container).value) || 0;
      const water = (flour * (hyd / 100)).toFixed(1);
      const saltG = (flour * (salt / 100)).toFixed(1);
      const total = (+flour + +water + +saltG).toFixed(1);
      $("#bakers-output", container).innerHTML = `
        <div>Water: <strong>${water} g</strong></div>
        <div>Salt: <strong>${saltG} g</strong></div>
        <div style="color:var(--gold-primary); margin-top:0.25rem;">Total Dough Weight: <strong>${total} g</strong></div>
      `;
    }

    function updateEQ() {
      const meat = parseFloat($("#eq-meat", container).value) || 0;
      const water = parseFloat($("#eq-water", container).value) || 0;
      const target = parseFloat($("#eq-target", container).value) || 0;
      const res = window.ScienceEngine ? window.ScienceEngine.calculateEQBrine(meat, water, target) : { saltGrams: (meat + water) * (target / 100), totalMassGrams: meat + water, hoursRecommended: 24 };
      $("#eq-output", container).innerHTML = `
        <div style="color:var(--gold-primary);">EXACT SALT REQUIRED: <strong>${res.saltGrams} g</strong></div>
        <div>Total System Mass: ${res.totalMassGrams} g</div>
        <div>Time to Equilibrium: ${res.hoursRecommended} Hours</div>
      `;
    }

    function updateMeatGuide() {
      const cut = $("#meat-cut-select", container).value;
      const done = $("#meat-done-select", container).value;

      const guides = {
        "ribeye": { rare: { pull: 48, final: 52, rest: 10, note: "Carryover brings core to ruby rare; resting relaxes actin fibers." }, med_rare: { pull: 51, final: 55, rest: 12, note: "Peak intramuscular fat rendering without moisture loss." }, med: { pull: 56, final: 60, rest: 10, note: "Warm pink center throughout." } },
        "lamb": { rare: { pull: 48, final: 52, rest: 8, note: "Delicate pastoral sweetness; avoids gamey tallow rendering." }, med_rare: { pull: 52, final: 56, rest: 10, note: "Optimal tenderness for herb-crusted rack." }, med: { pull: 57, final: 61, rest: 10, note: "Firm texture, juices remain pink." } },
        "duck": { rare: { pull: 49, final: 53, rest: 8, note: "Red meat steak texture; skin must be crisp." }, med_rare: { pull: 52, final: 56, rest: 8, note: "Classical French bistro doneness for Magret." }, med: { pull: 57, final: 61, rest: 8, note: "Firm, slightly chewy." } },
        "salmon": { rare: { pull: 42, final: 46, rest: 5, note: "Translucent, sashimi-grade molten center." }, med_rare: { pull: 46, final: 50, rest: 5, note: "Flakes effortlessly with zero chalky albumin weeping." }, med: { pull: 50, final: 54, rest: 5, note: "Firm, traditional flaked salmon." } },
        "pork": { rare: { pull: 56, final: 60, rest: 8, note: "Safe for modern heritage pork; juicy and tender." }, med_rare: { pull: 59, final: 63, rest: 10, note: "Delicate blush pink with maximum natural juices." }, med: { pull: 63, final: 67, rest: 10, note: "White with faint pink blush." } }
      };

      const g = (guides[cut] && guides[cut][done]) || { pull: 52, final: 56, rest: 10, note: "Standard culinary rest." };
      $("#meat-output", container).innerHTML = `
        <div style="color:var(--gold-primary);">PULL OFF FLAME AT: <strong>${g.pull}°C (${Math.round(g.pull * 1.8 + 32)}°F)</strong></div>
        <div>Target Finished Temp: <strong>${g.final}°C (${Math.round(g.final * 1.8 + 32)}°F)</strong></div>
        <div>Minimum Resting Window: <strong>${g.rest} Minutes</strong></div>
        <div style="color:var(--text-muted); font-size:0.75rem; margin-top:0.35rem;">${esc(g.note)}</div>
      `;
    }

    $("#calc-flour", container).oninput = updateBakers;
    $("#calc-hydration", container).oninput = updateBakers;
    $("#calc-salt-pct", container).oninput = updateBakers;
    $("#eq-meat", container).oninput = updateEQ;
    $("#eq-water", container).oninput = updateEQ;
    $("#eq-target", container).oninput = updateEQ;
    $("#meat-cut-select", container).onchange = updateMeatGuide;
    $("#meat-done-select", container).onchange = updateMeatGuide;

    updateBakers();
    updateEQ();
    updateMeatGuide();

    $("#troubleshoot-select", container).onchange = (e) => {
      const remedies = {
        "broken-emulsion": "Whisk 1 tablespoon of boiling water (or fresh egg yolk) into a clean warm bowl, then slowly whisk the broken sauce into it off heat. The fresh continuous water phase re-suspends oil droplets.",
        "dry-meat": "Allow meat to rest at least 10 minutes before slicing. If already dry, slice razor thin across the grain and dress in warm melted butter, pan drippings, and flaky sea salt.",
        "oversalted": "Do NOT add raw potatoes (a debunked myth that absorbs liquid equally with salt). Dilute by adding unseasoned stock, whole milk, cream, or a touch of acid and honey to raise the perceptual threshold.",
        "dense-bread": "Check yeast viability in warm 38°C water with pinch of sugar. Ensure dough proofs until doubled and bake with a heavy cast iron Dutch oven or baking steel preheated at 240°C for at least 60 minutes.",
        "scorched-garlic": "Burnt garlic contains bitter pyrazines that cannot be masked. Discard immediately, wipe pan with paper towel, and restart with fresh cold oil and minced garlic sweated over low heat.",
        "soggy-skin": "Skin was likely wet or the pan was below Leidenfrost temperature (190°C). Always scrape fish skin dry with a knife spine and press flat against hot pan with a fish spatula for the first 30 seconds."
      };
      $("#troubleshoot-output", container).textContent = remedies[e.target.value];
    };

    // Ingredient Encyclopedia Render Engine
    function renderEncyclopediaGrid() {
      let filtered = ingredients;
      if (activeCategory !== "All") {
        filtered = filtered.filter(i => i.category === activeCategory);
      }
      if (searchQuery) {
        filtered = window.EncyclopediaEngine.search(searchQuery);
      }

      const grid = $("#encyclopedia-grid", container);
      if (!filtered.length) {
        grid.innerHTML = `<div style="grid-column:1/-1; text-align:center; padding:3rem; color:var(--text-muted);">No ingredient dossiers match your filter.</div>`;
        return;
      }

      grid.innerHTML = filtered.map(item => `
        <article class="bento-card">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem;">
            <span class="card-badge">${esc(item.category.toUpperCase())}</span>
            <span style="font-size:0.7rem; font-family:var(--font-mono); color:var(--text-muted);">${esc(item.season)}</span>
          </div>
          <h3 class="card-title">${esc(item.name)}</h3>
          <p class="card-desc" style="display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden;">${esc(item.flavorProfile)}</p>
          
          <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:0.75rem; color:var(--gold-primary); font-family:var(--font-mono);">${(item.affinities || []).slice(0, 3).join(', ')}</span>
            <button class="btn-primary btn-open-dossier" data-id="${item.id}" style="font-size:0.75rem; padding:0.35rem 0.75rem;">
              View Dossier →
            </button>
          </div>
        </article>
      `).join('');

      $$(".btn-open-dossier", grid).forEach(btn => {
        btn.onclick = () => openEncyclopediaModal(btn.dataset.id);
      });
    }

    $$(".btn-encyclo-cat", container).forEach(btn => {
      btn.onclick = () => {
        $$(".btn-encyclo-cat", container).forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        activeCategory = btn.dataset.cat;
        renderEncyclopediaGrid();
      };
    });

    $("#encyclopedia-search", container).oninput = (e) => {
      searchQuery = e.target.value;
      renderEncyclopediaGrid();
    };

    renderEncyclopediaGrid();
  }

  // Master Ingredient Encyclopedia Modal
  function openEncyclopediaModal(ingredientId) {
    const item = window.EncyclopediaEngine ? window.EncyclopediaEngine.getById(ingredientId) : (window.ENCYCLOPEDIA_INGREDIENTS || []).find(i => i.id === ingredientId);
    if (!item) return;

    let modal = $("#atelier-generic-modal");
    if (!modal) {
      modal = document.createElement("dialog");
      modal.id = "atelier-generic-modal";
      modal.className = "atelier-modal";
      document.body.appendChild(modal);
    }

    modal.innerHTML = `
      <button class="modal-close-btn" onclick="this.closest('dialog').close()">✕</button>
      <span class="card-badge">${esc(item.category.toUpperCase())} · ${esc(item.season)}</span>
      <h2 style="font-size:2.2rem; font-family:var(--font-serif); margin:0.5rem 0 1rem 0;">${esc(item.name)}</h2>
      
      <div style="background:var(--bg-elevated); padding:1rem 1.25rem; border-radius:var(--radius-md); border-left:3px solid var(--gold-primary); margin-bottom:1.5rem;">
        <span style="font-size:0.75rem; font-family:var(--font-mono); color:var(--gold-primary); text-transform:uppercase; display:block; margin-bottom:0.25rem;">Storage & Longevity Rules</span>
        <p style="font-size:0.9rem; color:var(--text-secondary); margin:0;">${esc(item.storage)}</p>
      </div>

      <div style="display:flex; flex-direction:column; gap:1.5rem; margin-bottom:2rem;">
        <div>
          <h4 style="font-size:1.1rem; font-family:var(--font-serif); color:var(--text-primary); margin-bottom:0.4rem;">Sensory & Flavor Profile</h4>
          <p style="font-size:0.95rem; color:var(--text-secondary); line-height:1.6;">${esc(item.flavorProfile)}</p>
        </div>

        <div>
          <h4 style="font-size:1.1rem; font-family:var(--font-serif); color:var(--gold-primary); margin-bottom:0.4rem;">Culinary Science & Cellular Function</h4>
          <p style="font-size:0.95rem; color:var(--text-secondary); line-height:1.6;">${esc(item.scienceRole)}</p>
        </div>

        <div>
          <h4 style="font-size:1.1rem; font-family:var(--font-serif); color:var(--text-primary); margin-bottom:0.4rem;">Optimal Culinary Techniques</h4>
          <ul style="font-size:0.9rem; color:var(--text-secondary); margin-left:1.2rem; display:flex; flex-direction:column; gap:0.4rem;">
            ${(item.bestTechniques || []).map(t => `<li>${esc(t)}</li>`).join('')}
          </ul>
        </div>

        <div>
          <h4 style="font-size:1.1rem; font-family:var(--font-serif); color:var(--text-primary); margin-bottom:0.4rem;">Substitutions & Culinary Impact</h4>
          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6;">${esc(item.substitutions)}</p>
        </div>

        <div>
          <h4 style="font-size:1.1rem; font-family:var(--font-serif); color:var(--text-primary); margin-bottom:0.5rem;">Flavor Affinities & Pairings</h4>
          <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
            ${(item.affinities || []).map(a => `<span class="nav-pill" style="font-size:0.75rem; border:1px solid var(--border-subtle);">${esc(a)}</span>`).join('')}
          </div>
        </div>
      </div>

      <div style="display:flex; justify-content:flex-end;">
        <button class="btn-primary" onclick="this.closest('dialog').close()">Close Dossier</button>
      </div>
    `;

    modal.showModal();
  }
'''

with open("latelier.js", "r", encoding="utf-8") as f:
    content = f.read()

# Locate renderToolsView block
start_marker = "  function renderToolsView(container) {"
end_marker = "  // VIEW: 9. PERSONAL RECIPE NOTEBOOK & VAULT"

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = content.split(end_marker)[1]
    # Check if there is an existing comment before start_marker
    if "  // VIEW: 8. CULINARY STUDIO" in pre:
        pre = pre.split("  // VIEW: 8. CULINARY STUDIO")[0]
    elif "  // =========================================================================\n  // VIEW: 8." in pre:
        pre = pre.split("  // =========================================================================\n  // VIEW: 8.")[0]
    
    updated = pre + new_tools_code + "\n  // =========================================================================\n  // VIEW: 9. PERSONAL RECIPE NOTEBOOK & VAULT" + post
    with open("latelier.js", "w", encoding="utf-8") as f:
        f.write(updated)
    print("Successfully patched latelier.js with enhanced Tools and Encyclopedia!")
else:
    print("Markers not found in latelier.js")
