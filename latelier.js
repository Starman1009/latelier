/**
 * L'ATELIER · THE DIGITAL CULINARY WORKSHOP & ACADEMY
 * Core Application Engine & View Orchestrator
 */

(function () {
  "use strict";

  // Application State
  const AppState = {
    currentView: "discovery",
    theme: localStorage.getItem("atelier_theme") || "dark",
    activeOccasion: "dinner",
    courseCount: 3,
    activeMenu: null,
    lockedCourses: {},
    savedRecipeIds: JSON.parse(localStorage.getItem("atelier_saved_recipes") || "[]"),
    userNotes: JSON.parse(localStorage.getItem("atelier_user_notes") || "{}"),
    shoppingList: JSON.parse(localStorage.getItem("atelier_shopping_v2") || "[]"),
    activeRecipe: null,
    activeRecipeServings: 4,
    // Kitchen Mode State
    kitchenModeActive: false,
    kitchenStepIndex: 0,
    activeTimers: [],
    timerAudioCtx: null,
    wakeLock: null,
    speechRecognition: null,
    isVoiceActive: false,
    // Flavor Lab Simulator
    flavorProfile: { sweetness: 4, saltiness: 5, sourness: 6, bitterness: 2, umami: 7, richness: 6, heat: 3, aroma: 7 },
    // Science Lab State
    panMaterial: "cast_iron",
    panThickness: 4.5,
    flamePower: 2200,
    oilMl: 180,
    waterMl: 30,
    eggYolks: 2,
    whiskRpm: 650,
    surfaceMoisture: 35,
    panTempC: 175,
    meatWeight: 800,
    brineWater: 800,
    targetSalinity: 1.25,
    braiseTemp: 82,
    braiseHours: 4
  };

  // Utilities
  const $ = (selector, parent = document) => parent.querySelector(selector);
  const $$ = (selector, parent = document) => [...parent.querySelectorAll(selector)];
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // Notification helper
  function showNotification(message, type = "info") {
    let toast = $("#atelier-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "atelier-toast";
      toast.style.cssText = "position:fixed;bottom:24px;right:24px;z-index:9999;padding:12px 20px;border-radius:10px;background:var(--bg-elevated);color:var(--text-primary);border:1px solid var(--border-active);box-shadow:var(--shadow-lg);font-size:0.875rem;display:flex;align-items:center;gap:8px;transition:opacity 0.3s var(--ease-spring);";
      document.body.appendChild(toast);
    }
    toast.innerHTML = `<span style="color:var(--gold-primary)">✦</span> ${esc(message)}`;
    toast.style.opacity = "1";
    clearTimeout(showNotification._timeout);
    showNotification._timeout = setTimeout(() => { toast.style.opacity = "0"; }, 4000);
  }

  // Audio Chime Synthesizer
  function initAudio() {
    if (!AppState.timerAudioCtx) {
      AppState.timerAudioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (AppState.timerAudioCtx.state === "suspended") {
      AppState.timerAudioCtx.resume();
    }
    return AppState.timerAudioCtx;
  }

  function playChime() {
    try {
      const ctx = initAudio();
      if (!ctx) return;
      const now = ctx.currentTime;
      [523.25, 659.25, 783.99, 1046.5].forEach((freq, i) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(freq, now + i * 0.12);
        gain.gain.setValueAtTime(0, now + i * 0.12);
        gain.gain.linearRampToValueAtTime(0.2, now + i * 0.12 + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.12 + 1.2);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + i * 0.12);
        osc.stop(now + i * 0.12 + 1.3);
      });
    } catch (e) {
      console.warn("Audio unavailable:", e);
    }
  }

  // Screen Wake-Lock API
  async function requestWakeLock() {
    if ("wakeLock" in navigator && !AppState.wakeLock) {
      try {
        AppState.wakeLock = await navigator.wakeLock.request("screen");
        AppState.wakeLock.addEventListener("release", () => { AppState.wakeLock = null; });
      } catch (err) {
        console.warn("Wake lock failed:", err);
      }
    }
  }

  function releaseWakeLock() {
    if (AppState.wakeLock) {
      AppState.wakeLock.release().catch(() => {});
      AppState.wakeLock = null;
    }
  }

  // Theme Management
  function applyTheme(theme) {
    AppState.theme = theme;
    localStorage.setItem("atelier_theme", theme);
    if (theme === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
    const themeBtn = $("#theme-toggle");
    if (themeBtn) {
      themeBtn.innerHTML = theme === "dark" ? "☼" : "☾";
      themeBtn.setAttribute("title", theme === "dark" ? "Switch to Ivory Light Theme" : "Switch to Obsidian Dark Theme");
    }
  }

  // View Router
  function navigateTo(view) {
    AppState.currentView = view;
    $$(".nav-pill").forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.view === view);
    });

    const mainContent = $("#main-viewport");
    if (!mainContent) return;

    window.scrollTo({ top: 0, behavior: "smooth" });

    switch (view) {
      case "techniques": window.renderMastery(mainContent); break;
      case "botanicals": window.renderBotanicals(mainContent); break;
      case "discovery":
        renderDiscoveryView(mainContent);
        break;
      case "recipes":
        renderRecipeCatalogView(mainContent);
        break;
      case "prep":
        renderPrepManualView(mainContent);
        break;
      case "flavor":
        renderFlavorLabView(mainContent);
        break;
      case "palate":
        renderPalateAcademyView(mainContent);
        break;
      case "mise":
        renderMiseEnPlaceView(mainContent);
        break;
      case "academy":
        renderAcademyView(mainContent);
        break;
      case "science":
        renderScienceLabView(mainContent);
        break;
      case "tools":
        renderToolsView(mainContent);
        break;
      case "notebook":
        renderNotebookView(mainContent);
        break;
      case "shopping":
        renderShoppingListView(mainContent);
        break;
      default:
        renderDiscoveryView(mainContent);
    }
  }

  // =========================================================================
  // VIEW: 1. MEAL DISCOVERY & WHAT SHOULD I COOK?
  // =========================================================================
  function renderDiscoveryView(container) {
    const occasions = ["breakfast", "brunch", "lunch", "dinner", "dessert"];
    const activeOcc = AppState.activeOccasion;
    const courses = AppState.activeMenu || generateMenuCourses(activeOcc, AppState.courseCount);
    AppState.activeMenu = courses;

    container.innerHTML = `
      <section class="hero-editorial">
        <p class="hero-eyebrow">L'ATELIER · THE CULINARY WORKSHOP</p>
        <h1 class="hero-title">What Shall We Cook Today?</h1>
        <p class="hero-lead">Explore authentic global culinary traditions, compose harmonious degustation menus, and discover the food science behind every technique.</p>
        
        <div class="occasion-bar">
          ${occasions.map(occ => `
            <button class="occasion-btn ${activeOcc === occ ? 'active' : ''}" data-occ="${occ}">
              ${occ.charAt(0).toUpperCase() + occ.slice(1)}
            </button>
          `).join('')}
        </div>
      </section>

      <div class="surprise-box">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
          <div>
            <span class="card-badge">DEGUSTATION ARC</span>
            <h2 style="font-size:1.8rem; font-family:var(--font-serif); margin-top:0.25rem;">
              Your Composed ${activeOcc.charAt(0).toUpperCase() + activeOcc.slice(1)} Menu
            </h2>
            <p style="font-size:0.875rem; color:var(--text-muted);">${courses.length} harmonized courses balanced for sensory contrast, temperature, and texture.</p>
          </div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <label style="font-size:0.8rem; font-family:var(--font-mono); color:var(--text-muted);">
              COURSES:
              <select id="select-course-count" class="form-select" style="margin-left:0.5rem; padding:0.3rem 0.6rem;">
                <option value="2" ${AppState.courseCount === 2 ? 'selected' : ''}>2 Courses</option>
                <option value="3" ${AppState.courseCount === 3 ? 'selected' : ''}>3 Courses</option>
                <option value="4" ${AppState.courseCount === 4 ? 'selected' : ''}>4 Courses</option>
                <option value="5" ${AppState.courseCount === 5 ? 'selected' : ''}>5-Course Grand Degustation</option>
              </select>
            </label>
            <button id="btn-surprise-me" class="btn-primary">
              <span>↻</span> Surprise Me
            </button>
          </div>
        </div>

        <div class="bento-grid">
          ${courses.map((course, idx) => `
            <article class="bento-card" style="border-top: 3px solid var(--gold-primary);">
              <div style="display:flex; justify-content:space-between; align-items:start; margin-bottom:0.75rem;">
                <span class="card-badge">COURSE 0${idx + 1} · ${esc(course.slot.toUpperCase())}</span>
                <button class="btn-icon btn-lock-course" data-index="${idx}" title="${AppState.lockedCourses[idx] ? 'Unlock this course' : 'Lock this course'}" style="width:30px;height:30px;">
                  ${AppState.lockedCourses[idx] ? '🔒' : '🔓'}
                </button>
              </div>
              <h3 class="card-title">${esc(course.recipe.title)}</h3>
              <p style="font-size:0.825rem; font-family:var(--font-mono); color:var(--gold-primary); margin-bottom:0.5rem;">
                ${esc(course.recipe.cuisine)} · ${course.recipe.totalMins} mins · ${esc(course.recipe.difficulty)}
              </p>
              <p class="card-desc">${esc(course.recipe.summary)}</p>
              
              <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:auto;">
                <button class="btn-primary btn-open-recipe" data-id="${course.recipe.id}" style="font-size:0.8rem; padding:0.45rem 0.9rem;">
                  View Recipe →
                </button>
                <button class="btn-secondary btn-swap-course" data-index="${idx}" ${AppState.lockedCourses[idx] ? 'disabled' : ''} style="font-size:0.8rem; padding:0.45rem 0.9rem;">
                  Swap
                </button>
              </div>
            </article>
          `).join('')}
        </div>

        <!-- Refinement Toolbar -->
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:1.5rem; padding-top:1.25rem; border-top:1px solid var(--border-subtle); align-items:center;">
          <span style="font-size:0.8rem; font-family:var(--font-mono); color:var(--text-muted); text-transform:uppercase;">Refine Menu:</span>
          <button class="btn-secondary btn-refine" data-action="easier">Make it easier</button>
          <button class="btn-secondary btn-refine" data-action="fancier">Make it fancier</button>
          <button class="btn-secondary btn-refine" data-action="faster">Make it faster (&lt;30m)</button>
          <button class="btn-secondary btn-refine" data-action="similar">Show similar cuisine</button>
          <button class="btn-secondary btn-refine" data-action="different">Completely different</button>
          <button class="btn-secondary" id="btn-shop-entire-menu" style="border-color:var(--gold-border); color:var(--gold-primary);">
            🛒 Add All Menu Ingredients to Provisions
          </button>
          <button class="btn-primary" id="btn-coordinate-menu" style="margin-left:auto;">
            Coordinate in Mise en Place Studio →
          </button>
        </div>
      </div>

      <!-- Quick Feature Showcase Bento -->
      <section style="margin-top:3rem;">
        <div style="text-align:center; margin-bottom:2rem;">
          <p class="hero-eyebrow">EXPLORE THE UNIVERSE</p>
          <h2 style="font-size:2.2rem; font-family:var(--font-serif);">The Atelier Ecosystem</h2>
        </div>
        <div class="bento-grid">
          <div class="bento-card" style="cursor:pointer;" onclick="window.AtelierApp.navigateTo('recipes')">
            <span class="card-badge">LIBRARY</span>
            <h3 class="card-title">153+ Master Recipes</h3>
            <p class="card-desc">Detailed recipes from French classical mother sauces and authentic regional Italian pastas to Edomae sushi and Sichuan wok techniques.</p>
            <span style="color:var(--gold-primary); font-size:0.85rem; font-weight:600;">Browse collection →</span>
          </div>
          <div class="bento-card" style="cursor:pointer;" onclick="window.AtelierApp.navigateTo('flavor')">
            <span class="card-badge">FLAGSHIP</span>
            <h3 class="card-title">The Flavor Lab</h3>
            <p class="card-desc">Interactive volatile aroma network, 8-axis flavor balance simulator with dynamic radar charts, and side-by-side culinary ingredient comparisons.</p>
            <span style="color:var(--gold-primary); font-size:0.85rem; font-weight:600;">Launch Flavor Lab →</span>
          </div>
          <div class="bento-card" style="cursor:pointer;" onclick="window.AtelierApp.navigateTo('science')">
            <span class="card-badge">LABORATORY</span>
            <h3 class="card-title">The Science of Cooking</h3>
            <p class="card-desc">Five interactive simulations exploring heat transfer kinetics, emulsion micro-physics, Maillard reaction curves, and collagen-to-gelatin conversion.</p>
            <span style="color:var(--gold-primary); font-size:0.85rem; font-weight:600;">Open food science →</span>
          </div>
          <div class="bento-card" style="cursor:pointer;" onclick="window.AtelierApp.navigateTo('mise')">
            <span class="card-badge">PROFESSIONAL</span>
            <h3 class="card-title">Mise en Place Studio</h3>
            <p class="card-desc">Backward-scheduled cooking timelines from pickup (T-0), station assignments, prep staging checklists, and full-screen hands-free Kitchen Mode.</p>
            <span style="color:var(--gold-primary); font-size:0.85rem; font-weight:600;">Enter the kitchen →</span>
          </div>
        </div>
      </section>
    `;

    // Event Bindings
    $$(".occasion-btn", container).forEach(btn => {
      btn.onclick = () => {
        AppState.activeOccasion = btn.dataset.occ;
        AppState.lockedCourses = {};
        AppState.activeMenu = null;
        renderDiscoveryView(container);
      };
    });

    $("#select-course-count", container).onchange = (e) => {
      AppState.courseCount = parseInt(e.target.value);
      AppState.activeMenu = null;
      renderDiscoveryView(container);
    };

    $("#btn-surprise-me", container).onclick = () => {
      AppState.activeMenu = generateMenuCourses(AppState.activeOccasion, AppState.courseCount);
      renderDiscoveryView(container);
      showNotification("New culinary degustation arc composed!");
    };

    $$(".btn-lock-course", container).forEach(btn => {
      btn.onclick = () => {
        const idx = parseInt(btn.dataset.index);
        AppState.lockedCourses[idx] = !AppState.lockedCourses[idx];
        renderDiscoveryView(container);
      };
    });

    $$(".btn-swap-course", container).forEach(btn => {
      btn.onclick = () => {
        const idx = parseInt(btn.dataset.index);
        swapSingleCourse(idx);
        renderDiscoveryView(container);
      };
    });

    $$(".btn-open-recipe", container).forEach(btn => {
      btn.onclick = () => openRecipeModal(btn.dataset.id);
    });

    $$(".btn-refine", container).forEach(btn => {
      btn.onclick = () => refineMenu(btn.dataset.action, container);
    });

    $("#btn-coordinate-menu", container).onclick = () => {
      navigateTo("mise");
    };

    const btnShopMenu = $("#btn-shop-entire-menu", container);
    if (btnShopMenu) {
      btnShopMenu.onclick = () => {
        let addedCount = 0;
        courses.forEach(c => {
          c.recipe.ingredients.forEach(ing => {
            AppState.shoppingList.push({
              name: ing.name,
              qty: ing.qty,
              unit: ing.unit,
              dept: ing.dept || "Pantry",
              done: false
            });
            addedCount++;
          });
        });
        localStorage.setItem("atelier_shopping_v2", JSON.stringify(AppState.shoppingList));
        showNotification(`Added ${addedCount} ingredients across ${courses.length} courses to Provisions!`);
      };
    }
  }

  function generateMenuCourses(occasion, count) {
    const all = window.MASTER_RECIPES || [];
    const pool = occasion === "dessert" 
      ? all.filter(r => r.category === "dessert")
      : all.filter(r => r.category === occasion || r.category === "dinner" || r.category === "lunch");

    const slots = count === 2 
      ? ["opener", "climax"]
      : count === 3 
      ? ["opener", "mid", "climax"]
      : count === 5
      ? ["opener", "mid", "climax", "predessert", "dessert"]
      : ["opener", "mid", "climax", "dessert"];

    const chosen = [];
    const usedIds = new Set();

    slots.forEach((slot, i) => {
      if (AppState.activeMenu && AppState.lockedCourses[i] && AppState.activeMenu[i]) {
        chosen.push(AppState.activeMenu[i]);
        usedIds.add(AppState.activeMenu[i].recipe.id);
        return;
      }

      let matches = pool.filter(r => r.slot === slot && !usedIds.has(r.id));
      if (!matches.length) matches = all.filter(r => r.slot === slot && !usedIds.has(r.id));
      if (!matches.length) matches = all.filter(r => !usedIds.has(r.id));

      const selected = matches[Math.floor(Math.random() * matches.length)] || all[0];
      usedIds.add(selected.id);
      chosen.push({ slot: slot, recipe: selected });
    });

    return chosen;
  }

  function swapSingleCourse(index) {
    const all = window.MASTER_RECIPES || [];
    const current = AppState.activeMenu[index];
    const pool = all.filter(r => r.slot === current.slot && r.id !== current.recipe.id);
    if (pool.length) {
      AppState.activeMenu[index].recipe = pool[Math.floor(Math.random() * pool.length)];
      showNotification(`Swapped course 0${index + 1} for ${AppState.activeMenu[index].recipe.title}`);
    }
  }

  function refineMenu(action, container) {
    const all = window.MASTER_RECIPES || [];
    AppState.activeMenu.forEach((course, idx) => {
      if (AppState.lockedCourses[idx]) return;
      let filtered = all.filter(r => r.slot === course.slot && r.id !== course.recipe.id);
      if (action === "easier") {
        filtered = filtered.filter(r => r.difficulty === "Beginner" || r.difficulty === "Intermediate");
      } else if (action === "fancier") {
        filtered = filtered.filter(r => r.difficulty === "Advanced" || r.difficulty === "Professional Technique");
      } else if (action === "faster") {
        filtered = filtered.filter(r => r.totalMins <= 35);
      } else if (action === "similar") {
        filtered = filtered.filter(r => r.cuisine.toLowerCase().includes(course.recipe.cuisine.split(' ')[0].toLowerCase()));
      }
      if (filtered.length) {
        course.recipe = filtered[Math.floor(Math.random() * filtered.length)];
      }
    });
    renderDiscoveryView(container);
    showNotification(`Menu refined: ${action}`);
  }

  // =========================================================================
  // VIEW: 2. MASTER RECIPE CATALOG & LIBRARY
  // =========================================================================
  function renderRecipeCatalogView(container) {
    const allRecipes = window.MASTER_RECIPES || [];
    const cuisines = [...new Set(allRecipes.map(r => r.cuisine))].sort();
    const categories = ["All Categories", "breakfast", "lunch", "dinner", "dessert", "sauce_stock", "bread", "appetizer"];

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">THE ARCHIVE</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">The Master Recipe Library</h1>
        <p style="color:var(--text-secondary); max-width:720px;">A growing collection of recipes with stated yields, detailed mise en place, sensory doneness cues, scientific transformations, and flavor pairings.</p>
      </section>

      <!-- Search & Filters -->
      <div class="toolbar-container">
        <div class="form-group">
          <label class="form-label" for="search-input">Search Dishes or Ingredients</label>
          <input type="search" id="search-input" class="form-input" placeholder="e.g. Salmon, duck, saffron, pasta, brown butter...">
        </div>
        <div class="form-group">
          <label class="form-label" for="filter-cuisine">Cuisine Tradition</label>
          <select id="filter-cuisine" class="form-select">
            <option value="">All Cuisines (${cuisines.length})</option>
            ${cuisines.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join('')}
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="filter-category">Meal Category</label>
          <select id="filter-category" class="form-select">
            ${categories.map(c => `<option value="${c === 'All Categories' ? '' : c}">${c === 'All Categories' ? c : c.charAt(0).toUpperCase() + c.slice(1)}</option>`).join('')}
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="filter-time">Maximum Time</label>
          <select id="filter-time" class="form-select">
            <option value="">Any Duration</option>
            <option value="20">Under 20 Mins</option>
            <option value="35">Under 35 Mins</option>
            <option value="60">Under 60 Mins</option>
            <option value="120">Under 2 Hours</option>
          </select>
        </div>
        <button id="btn-reset-filters" class="btn-secondary" style="height:38px;">Reset</button>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
        <span id="results-count" style="font-size:0.85rem; font-family:var(--font-mono); color:var(--gold-primary);">
          Showing ${allRecipes.length} recipes
        </span>
      </div>

      <details class="bento-card" style="margin-bottom:1.5rem"><summary>Cook from published chef recipes · 10 source links</summary><p>Open the publisher’s complete recipe for its quantities, yield and method. These links are not imported recipes and are not counted in the local catalog.</p><div class="station-map">${(window.ATELIER_RECIPE_SOURCES || []).map(r=>`<a class="btn-secondary" href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">${esc(r.title)}<br><small>${esc(r.author)}</small></a>`).join('')}</div></details>
      <p class="text-muted">Local catalog source verification is pending. Consult an authoritative recipe before cooking; structured fields alone do not certify accuracy.</p>
      <div id="recipe-catalog-grid" class="bento-grid">
        <!-- Recipe Cards -->
      </div>
    `;

    function filterAndRender() {
      const q = $("#search-input", container).value.toLowerCase().trim();
      const cui = $("#filter-cuisine", container).value;
      const cat = $("#filter-category", container).value;
      const maxTime = parseInt($("#filter-time", container).value) || Infinity;

      const filtered = allRecipes.filter(r => {
        const matchesQ = !q || r.title.toLowerCase().includes(q) || r.cuisine.toLowerCase().includes(q) || r.summary.toLowerCase().includes(q) || (r.ingredients || []).some(i => i.name.toLowerCase().includes(q));
        const matchesCui = !cui || r.cuisine === cui;
        const matchesCat = !cat || r.category === cat;
        const matchesTime = r.totalMins <= maxTime;
        return matchesQ && matchesCui && matchesCat && matchesTime;
      });

      $("#results-count", container).textContent = `Showing ${filtered.length} of ${allRecipes.length} recipes`;

      const grid = $("#recipe-catalog-grid", container);
      if (!filtered.length) {
        grid.innerHTML = `<div style="grid-column:1/-1; padding:3rem; text-align:center; color:var(--text-muted);">No dishes match your active criteria. Try broadening your search or clearing filters.</div>`;
        return;
      }

      grid.innerHTML = filtered.map(r => `
        <article class="bento-card">
          ${window.culinaryImage(r)}
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span class="card-badge">${esc(r.cuisine)}</span>
            <span style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted);">${r.totalMins}m · ${esc(r.difficulty)}</span>
          </div>
          <h3 class="card-title">${esc(r.title)}</h3>
          <p class="card-desc">${esc(r.summary)}</p>
          
          <div class="card-meta">
            <span>${r.ingredients.length} ingredients · ${r.steps.length} steps</span>
            <div style="display:flex; gap:0.5rem;">
              <button class="btn-icon btn-star-recipe" data-id="${r.id}" title="Save to Recipe Box">
                ${AppState.savedRecipeIds.includes(r.id) ? '★' : '☆'}
              </button>
              <button class="btn-primary btn-open-recipe" data-id="${r.id}" style="font-size:0.8rem; padding:0.35rem 0.8rem;">
                View →
              </button>
            </div>
          </div>
        </article>
      `).join('');

      $$(".btn-open-recipe", grid).forEach(b => {
        b.onclick = () => openRecipeModal(b.dataset.id);
      });

      $$(".btn-star-recipe", grid).forEach(b => {
        b.onclick = (e) => {
          e.stopPropagation();
          toggleSaveRecipe(b.dataset.id);
          b.innerHTML = AppState.savedRecipeIds.includes(b.dataset.id) ? '★' : '☆';
        };
      });
    }

    $("#search-input", container).oninput = filterAndRender;
    $("#filter-cuisine", container).onchange = filterAndRender;
    $("#filter-category", container).onchange = filterAndRender;
    $("#filter-time", container).onchange = filterAndRender;
    $("#btn-reset-filters", container).onclick = () => {
      $("#search-input", container).value = "";
      $("#filter-cuisine", container).value = "";
      $("#filter-category", container).value = "";
      $("#filter-time", container).value = "";
      filterAndRender();
    };

    filterAndRender();
  }

  // =========================================================================
  // VIEW: 3. THE FLAVOR LAB (Aroma Network & Balance Simulator)
  // =========================================================================
  function renderFlavorLabView(container) {
    const nodes = window.FLAVOR_NODES || [];
    const comparisons = window.INGREDIENT_COMPARISONS || [];

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">THE FLAVOR LAB</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Aroma Affinities & Flavor Simulator</h1>
        <p style="color:var(--text-secondary); max-width:760px;">Explore the chemical and sensory mechanisms that cause ingredients to harmonize. Experiment with the live 8-axis Flavor Balance Simulator and compare culinary behaviors side by side.</p>
      </section>

      <!-- Two-Column Simulator Layout -->
      <div class="simulator-layout">
        <!-- Left: Sliders -->
        <div class="bento-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
            <div>
              <span class="card-badge">SENSORY SIMULATOR</span>
              <h2 style="font-size:1.5rem; font-family:var(--font-serif);">Dish Flavor Balance</h2>
            </div>
            <button id="btn-reset-profile" class="btn-secondary" style="font-size:0.75rem; padding:0.3rem 0.6rem;">Reset</button>
          </div>

          <div id="sliders-container">
            ${Object.keys(AppState.flavorProfile).map(axis => `
              <div class="slider-group">
                <div class="slider-header">
                  <span style="font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase;">${axis}</span>
                  <span id="val-${axis}" style="font-family:var(--font-mono); font-weight:600; color:var(--gold-primary);">${AppState.flavorProfile[axis]}/10</span>
                </div>
                <input type="range" min="0" max="10" value="${AppState.flavorProfile[axis]}" class="range-slider" data-axis="${axis}">
              </div>
            `).join('')}
          </div>

          <!-- Real-Time Sensory Diagnosis Engine -->
          <div id="flavor-diagnosis-box" style="margin-top:1.5rem; padding:1.25rem; background:var(--bg-elevated); border-radius:var(--radius-md); border:1px solid var(--border-subtle);">
            <!-- Dynamic Diagnosis Output -->
          </div>
        </div>

        <!-- Right: Radar Chart Visualization -->
        <div class="bento-card" style="display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:480px;">
          <h3 style="font-size:1.2rem; font-family:var(--font-serif); margin-bottom:1rem; align-self:flex-start;">
            Gustatory Polygon Map
          </h3>
          <div id="radar-chart-svg-container" style="width:100%; max-width:380px; aspect-ratio:1;">
            <!-- SVG Radar Chart rendered here -->
          </div>
          <p style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted); margin-top:1rem; text-align:center;">
            Balanced dishes exhibit harmonious multi-axial equilibrium. Extreme imbalances prompt automatic culinary adjustments.
          </p>
        </div>
      </div>

      <!-- Interactive Aroma Network Node Explorer -->
      <section style="margin-top:3.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:end; margin-bottom:1.5rem;">
          <div>
            <span class="card-badge">AROMA CONNECTIONS</span>
            <h2 style="font-size:2rem; font-family:var(--font-serif); margin-top:0.25rem;">Interactive Flavor Network</h2>
            <p style="font-size:0.875rem; color:var(--text-muted);">Select any ingredient node to reveal its molecular pairings, volatile shared compounds, and dish applications.</p>
          </div>
        </div>

        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1.5rem;">
          ${nodes.map(n => `
            <button class="nav-pill btn-flavor-node" data-id="${n.id}" style="border:1px solid var(--border-subtle);">
              ${esc(n.name)}
            </button>
          `).join('')}
        </div>

        <div id="flavor-node-detail" class="bento-card" style="min-height:180px;">
          <p style="color:var(--text-muted); text-align:center; padding:2rem;">Click any ingredient node above to investigate its chemical affinities and culinary applications.</p>
        </div>
      </section>

      <!-- Side-by-Side Ingredient Comparison -->
      <section style="margin-top:3.5rem;">
        <span class="card-badge">CULINARY COMPARISONS</span>
        <h2 style="font-size:2rem; font-family:var(--font-serif); margin:0.25rem 0 1.5rem 0;">Side-by-Side Ingredient Science</h2>
        <div class="bento-grid">
          ${comparisons.map((c, i) => `
            <article class="bento-card">
              <span class="card-badge">${c.pair[0]} vs ${c.pair[1]}</span>
              <h3 class="card-title">${esc(c.title)}</h3>
              <p class="card-desc">${esc(c.overview)}</p>
              
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; font-size:0.8rem; background:var(--bg-elevated); padding:0.75rem; border-radius:var(--radius-md); margin-bottom:1rem;">
                <div>
                  <strong style="color:var(--gold-primary);">${esc(c.itemA.name)}</strong>
                  <p style="color:var(--text-muted); margin-top:0.25rem;">${esc(c.itemA.culinaryBehavior)}</p>
                </div>
                <div>
                  <strong style="color:var(--emerald);">${esc(c.itemB.name)}</strong>
                  <p style="color:var(--text-muted); margin-top:0.25rem;">${esc(c.itemB.culinaryBehavior)}</p>
                </div>
              </div>

              <p style="font-size:0.8rem; color:var(--text-secondary); margin-bottom:0.5rem;">
                <strong>When to choose ${esc(c.pair[0])}:</strong> ${esc(c.whenToChooseA)}
              </p>
              <p style="font-size:0.8rem; color:var(--text-secondary);">
                <strong>Substitution consequence:</strong> ${esc(c.substitutionImpact)}
              </p>
            </article>
          `).join('')}
        </div>
      </section>
    `;

    function updateRadar() {
      const p = AppState.flavorProfile;
      const axes = Object.keys(p);
      const values = axes.map(a => p[a]);
      const container = $("#radar-chart-svg-container");
      if (!container) return;

      const size = 340;
      const center = size / 2;
      const radius = size * 0.38;
      const angleStep = (Math.PI * 2) / axes.length;

      let webSvg = "";
      [0.25, 0.5, 0.75, 1.0].forEach(level => {
        let pts = [];
        for (let i = 0; i < axes.length; i++) {
          const a = i * angleStep - Math.PI / 2;
          const r = radius * level;
          pts.push(`${center + r * Math.cos(a)},${center + r * Math.sin(a)}`);
        }
        webSvg += `<polygon points="${pts.join(' ')}" fill="none" stroke="var(--border-subtle)" stroke-dasharray="2,2" stroke-width="1"/>`;
      });

      let axisLinesSvg = "";
      let labelsSvg = "";
      let polygonPts = [];

      axes.forEach((axis, i) => {
        const a = i * angleStep - Math.PI / 2;
        const x2 = center + radius * Math.cos(a);
        const y2 = center + radius * Math.sin(a);
        axisLinesSvg += `<line x1="${center}" y1="${center}" x2="${x2}" y2="${y2}" stroke="var(--border-subtle)" stroke-width="1"/>`;

        const lx = center + (radius + 22) * Math.cos(a);
        const ly = center + (radius + 22) * Math.sin(a);
        labelsSvg += `<text x="${lx}" y="${ly}" fill="var(--text-muted)" font-size="10" font-family="var(--font-mono)" text-anchor="middle" dominant-baseline="central">${axis.toUpperCase()}</text>`;

        const valRatio = p[axis] / 10;
        const px = center + radius * valRatio * Math.cos(a);
        const py = center + radius * valRatio * Math.sin(a);
        polygonPts.push(`${px},${py}`);
      });

      const polySvg = `<polygon points="${polygonPts.join(' ')}" fill="var(--gold-muted)" stroke="var(--gold-primary)" stroke-width="2.5"/>`;

      container.innerHTML = `
        <svg viewBox="0 0 ${size} ${size}" style="width:100%;height:100%;">
          ${webSvg}
          ${axisLinesSvg}
          ${labelsSvg}
          ${polySvg}
        </svg>
      `;

      // Update real-time diagnosis
      const diag = window.FlavorEngine.evaluateBalance(p);
      const box = $("#flavor-diagnosis-box");
      if (box) {
        box.innerHTML = `
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <strong style="font-family:var(--font-serif); font-size:1.1rem;">Sensory Diagnosis</strong>
            <span style="font-family:var(--font-mono); font-size:0.8rem; font-weight:700; color:${diag.harmony > 75 ? 'var(--emerald)' : diag.harmony > 50 ? 'var(--amber)' : 'var(--crimson)'};">
              HARMONY: ${diag.harmony}%
            </span>
          </div>
          <ul style="font-size:0.825rem; color:var(--text-secondary); margin-left:1.2rem; margin-bottom:0.75rem;">
            ${diag.issues.map(iss => `<li>${esc(iss)}</li>`).join('')}
          </ul>
          <div style="padding-top:0.5rem; border-top:1px solid var(--border-subtle); font-size:0.8rem; color:var(--gold-primary);">
            <strong>Culinary Action:</strong> ${esc(diag.balancingActions ? diag.balancingActions[0] : diag.recommendations[0])}
          </div>
        `;
      }
    }

    $$(".range-slider", container).forEach(slider => {
      slider.oninput = (e) => {
        const axis = e.target.dataset.axis;
        const val = parseInt(e.target.value);
        AppState.flavorProfile[axis] = val;
        $(`#val-${axis}`).textContent = `${val}/10`;
        updateRadar();
      };
    });

    $("#btn-reset-profile", container).onclick = () => {
      AppState.flavorProfile = { sweetness: 4, saltiness: 5, sourness: 6, bitterness: 2, umami: 7, richness: 6, heat: 3, aroma: 7 };
      $$(".range-slider", container).forEach(s => { s.value = AppState.flavorProfile[s.dataset.axis]; });
      Object.keys(AppState.flavorProfile).forEach(axis => {
        $(`#val-${axis}`).textContent = `${AppState.flavorProfile[axis]}/10`;
      });
      updateRadar();
    };

    $$(".btn-flavor-node", container).forEach(btn => {
      btn.onclick = () => {
        $$(".btn-flavor-node", container).forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        renderNodeDetail(btn.dataset.id);
      };
    });

    function renderNodeDetail(nodeId) {
      const node = nodes.find(n => n.id === nodeId);
      const edges = (window.FLAVOR_EDGES || []).filter(e => e.source === nodeId || e.target === nodeId);
      const box = $("#flavor-node-detail");
      if (!box || !node) return;

      box.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:start; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
          <div>
            <span class="card-badge">${node.category.toUpperCase()}</span>
            <h3 style="font-size:1.8rem; font-family:var(--font-serif); margin-top:0.25rem;">${esc(node.name)}</h3>
            <p style="font-size:0.85rem; color:var(--gold-primary); font-family:var(--font-mono);">
              Dominant Taste: ${node.dominantTaste.toUpperCase()} · Volatiles: ${(node.primaryVolatiles || []).join(', ')}
            </p>
          </div>
        </div>
        <p style="font-size:0.9rem; color:var(--text-secondary); margin-bottom:1.5rem;">${esc(node.culinaryRole)}</p>

        <h4 style="font-size:1.1rem; font-family:var(--font-serif); margin-bottom:0.75rem;">Documented Chemical & Sensory Pairings (${edges.length})</h4>
        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:1rem;">
          ${edges.map(e => {
            const partnerId = e.source === nodeId ? e.target : e.source;
            const partner = nodes.find(n => n.id === partnerId) || { name: partnerId };
            return `
              <div style="background:var(--bg-elevated); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
                  <strong style="color:var(--text-primary);">${esc(partner.name)}</strong>
                  <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-primary);">${Math.round(e.affinityScore * 100)}% AFFINITY</span>
                </div>
                <p style="font-size:0.8rem; color:var(--text-secondary); margin-bottom:0.5rem;">${esc(e.aromaAffinity)}</p>
                <p style="font-size:0.75rem; color:var(--text-muted); font-style:italic;">"${esc(e.tasteInteraction)}"</p>
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    updateRadar();
  }

  // =========================================================================
  // VIEW: 4. PALATE CLEANSING ACADEMY
  // =========================================================================
  function renderPalateAcademyView(container) {
    const cleansers = [
      { name: "Green Apple Sorbet with Lime", category: "Acid & Cryo Reset", bestFor: "Between heavy fatty courses (Wagyu, Pork Belly)", mechanism: "Cold temperature constricts taste pore papillae while malic/citric acids cleave lipid tongue coatings, restoring receptor sensitivity." },
      { name: "Pickled Young Ginger (Gari)", category: "Trigeminal Reset", bestFor: "During Edomae Sushi / Raw Seafood progression", mechanism: "Gingerol stimulates trigeminal mechanoreceptors, clearing oily omega-3 fish aldehydes from taste buds between distinct fish species." },
      { name: "Neutral Water Cracker", category: "Physical Starch Sponge", bestFor: "Wine tastings and cheese evaluations", mechanism: "Bland porous starch absorbs residual saliva tannins and bound astringent proteins without imparting flavor." },
      { name: "Sparkling Mineral Water (San Pellegrino)", category: "Carbonic Acid Effervescence", bestFor: "Universal multi-course service", mechanism: "Dissolved carbon dioxide bubbles trigger gentle mechanosensory stimulation, mechanically dislodging food debris from papillae." },
      { name: "Lukewarm Sencha Green Tea", category: "Polyphenol Astringency", bestFor: "Post-dessert or rich poultry", mechanism: "Catechins bind loosely to salivary proteins, refreshing mouth moisture without thermal shock." }
    ];

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">TASTING SCIENCE</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Palate Cleansing Academy</h1>
        <p style="color:var(--text-secondary); max-width:760px;">Understand sensory adaptation, lipid palate fatigue, and how temperature, acidity, and carbonation reset taste receptors during a grand degustation menu.</p>
      </section>

      <div class="bento-grid" style="margin-bottom:3rem;">
        <article class="bento-card">
          <span class="card-badge">THE NEUROLOGY</span>
          <h3 class="card-title">What is Palate Fatigue?</h3>
          <p class="card-desc">When taste receptor cells (TRCs) are repeatedly exposed to the same chemical stimulus—such as high sodium, intense sweetness, or heavy animal fats—receptor signaling diminishes via neural adaptation. The dish begins to taste flat, dull, and heavy, even though the chemical composition has not changed.</p>
        </article>
        <article class="bento-card">
          <span class="card-badge">THE MECHANICS</span>
          <h3 class="card-title">The Four Cleansing Vectors</h3>
          <p class="card-desc">1. Thermal Shock (sub-zero sorbets reduce papillae swelling)<br>2. Acidic Cleavage (malic/acetic acid dissolves hydrophobic lipid coatings)<br>3. Carbonic Cavitation (micro-bubbles dislodge bound proteins)<br>4. Neutral Starch Adsorption (dry crackers absorb tannins).</p>
        </article>
      </div>

      <div class="bento-card" style="margin-bottom:3rem;">
        <span class="card-badge">INTERACTIVE SCENARIO SIMULATOR</span>
        <h2 style="font-size:1.8rem; font-family:var(--font-serif); margin:0.25rem 0 1rem 0;">Test Your Palate Cleanser Knowledge</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; align-items:start;">
          <div>
            <label class="form-label" style="margin-bottom:0.5rem; display:block;">Select Preceding Course:</label>
            <select id="scenario-course" class="form-select" style="width:100%; margin-bottom:1rem;">
              <option value="fatty-wagyu">High-Fat A5 Wagyu Ribeye (Lipid saturation)</option>
              <option value="oily-mackerel">Shime Saba Cured Mackerel (Strong marine oils)</option>
              <option value="sweet-souffle">Molten Chocolate Soufflé (Heavy sucrose/cocoa butter)</option>
              <option value="tannic-barolo">Aged Barolo Wine (High tannin astringency)</option>
            </select>

            <label class="form-label" style="margin-bottom:0.5rem; display:block;">Choose Proposed Cleanser:</label>
            <select id="scenario-cleanser" class="form-select" style="width:100%; margin-bottom:1rem;">
              ${cleansers.map((c, i) => `<option value="${i}">${esc(c.name)}</option>`).join('')}
            </select>
            <button id="btn-eval-cleanser" class="btn-primary" style="width:100%;">Evaluate Sensory Reset</button>
          </div>

          <div id="scenario-result-box" style="background:var(--bg-elevated); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle); min-height:160px;">
            <p style="color:var(--text-muted); font-size:0.875rem;">Select a tasting scenario on the left to analyze the physiological reset efficacy.</p>
          </div>
        </div>
      </div>

      <h2 style="font-size:1.8rem; font-family:var(--font-serif); margin-bottom:1rem;">Classical Cleanser Directory</h2>
      <div class="bento-grid">
        ${cleansers.map(c => `
          <div class="bento-card">
            <span class="card-badge">${esc(c.category)}</span>
            <h3 class="card-title">${esc(c.name)}</h3>
            <p style="font-size:0.8rem; color:var(--gold-primary); font-family:var(--font-mono); margin-bottom:0.5rem;">BEST APPLICATION: ${esc(c.bestFor)}</p>
            <p class="card-desc">${esc(c.mechanism)}</p>
          </div>
        `).join('')}
      </div>
    `;

    $("#btn-eval-cleanser", container).onclick = () => {
      const course = $("#scenario-course", container).value;
      const cleanserIdx = parseInt($("#scenario-cleanser", container).value);
      const chosen = cleansers[cleanserIdx];
      const res = $("#scenario-result-box", container);

      let score = 95;
      let notes = "";

      if (course === "fatty-wagyu") {
        if (cleanserIdx === 0) { // Sorbet
          score = 98;
          notes = "PERFECT HARMONY: The sharp acid cuts the rendered tallow, and sub-zero chill numbs fat saturation, preparing the tongue for the next delicate course.";
        } else if (cleanserIdx === 2) { // Cracker
          score = 45;
          notes = "POOR FIT: A dry cracker cannot dissolve dense beef tallow coating the lingual papillae; it turns pasty in the mouth.";
        } else {
          score = 80;
          notes = "EFFECTIVE: Provides moderate relief, though an acidic element is preferred for heavy mammal fats.";
        }
      } else if (course === "oily-mackerel") {
        if (cleanserIdx === 1) { // Pickled ginger
          score = 99;
          notes = "AUTHENTIC MASTER MATCH: Gingerol and vinegar volatility purge oily fish aldehydes instantaneously without destroying sushi shari balance.";
        } else {
          score = 70;
          notes = "MODERATE: Partially refreshes, but lacks the specific volatile compounds to neutralize fish aldehydes.";
        }
      } else {
        score = 85;
        notes = "GOOD COMPATIBILITY: Refreshes taste receptor response and resets oral pH.";
      }

      res.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
          <strong style="font-family:var(--font-serif); font-size:1.2rem;">Sensory Reset Score</strong>
          <span style="font-family:var(--font-mono); font-size:1.1rem; font-weight:700; color:${score > 90 ? 'var(--emerald)' : score > 70 ? 'var(--amber)' : 'var(--crimson)'};">
            ${score}/100
          </span>
        </div>
        <p style="font-size:0.875rem; color:var(--text-secondary);">${esc(notes)}</p>
      `;
    };
  }

  // =========================================================================
  // VIEW: 5. MISE EN PLACE STUDIO & KITCHEN MODE
  // =========================================================================
  function renderMiseEnPlaceView(container) {
    const menu = AppState.activeMenu || generateMenuCourses("dinner", 3);
    const primaryRecipe = menu[0].recipe;
    let selectedKitchenCourseIdx = 0;

    // Collect all prep items dynamically from all active recipes
    const allPrepTasks = [];
    menu.forEach((c, cIdx) => {
      if (c.recipe.miseEnPlace && c.recipe.miseEnPlace.length) {
        c.recipe.miseEnPlace.forEach(task => {
          allPrepTasks.push({ course: c.recipe.title, slot: c.slot, text: task, type: 'mise' });
        });
      }
      if (c.recipe.equipment && c.recipe.equipment.length) {
        c.recipe.equipment.forEach(eq => {
          allPrepTasks.push({ course: c.recipe.title, slot: c.slot, text: `Stage equipment: ${eq.name} (${eq.type || 'Cookware'})`, type: 'equipment' });
        });
      }
    });

    // Compute dynamic backward timeline from T-0 (19:30 default service)
    const maxTotalMins = Math.max(...menu.map(c => c.recipe.totalMins || 45), 45);
    const timelineEntries = [
      {
        offset: `T - ${maxTotalMins + 30} MINS`,
        title: "Cold Prep, Precision Knife Work & Marinades",
        station: "Garde Manger",
        desc: "Wash and dry tender produce. Execute julienne, brunoise, and chiffonade knife cuts. Season and brine proteins to establish osmotic equilibrium."
      },
      {
        offset: `T - ${Math.round(maxTotalMins * 0.75)} MINS`,
        title: "Foundational Stocks, Emulsions & Reductions",
        station: "Saucier Station",
        desc: "Bring foundational stocks and court-bouillons to simmer. Prepare cold herb oils, purées, and reduction syrups. Mount warm emulsions."
      },
      {
        offset: `T - ${Math.round(maxTotalMins * 0.4)} MINS`,
        title: "Thermal Preheating, Baking & Par-Baking",
        station: "Rôtisseur / Ovens",
        desc: "Preheat ovens and heavy cast iron. Par-bake tart shells and crusts. Initiate slow braises or oven roasting arcs."
      },
      {
        offset: `T - 15 MINS`,
        title: "Direct Searing, Sautéing & Butter Basting",
        station: "Panfry / Sauté",
        desc: "High-heat protein searing to trigger rapid surface Maillard browning. Foam butter with aromatics (arrosé) for convection basting."
      },
      {
        offset: `T - 6 MINS`,
        title: "Protein Resting & Pan Sauce Mounting",
        station: "Saucier & Resting Board",
        desc: "Rest proteins on warmed cutting boards to redistribute intracellular juices. Deglaze roasting fond with wine and mount with cold butter cubes (monter au beurre)."
      },
      {
        offset: `T - 0 (SERVICE PICKUP)`,
        title: "Service Assembly, Precision Saucing & The Pass",
        station: "The Pass / Plating Table",
        desc: "Wipe rim of warmed porcelain. Ladle glossy warm sauces, carve rested proteins across grain, arrange microgreens with offset tweezers. Serve immediately."
      }
    ];

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <div style="display:flex; justify-content:space-between; align-items:start; flex-wrap:wrap; gap:1rem;">
          <div>
            <span class="card-badge">THE WORKSPACE</span>
            <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Mise en Place Studio</h1>
            <p style="color:var(--text-secondary); max-width:720px;">The professional preparation workspace: dynamic multi-course checklists, parallel station synchronization, backward-scheduled timeline from T-0 pickup, and hands-free Kitchen Mode.</p>
          </div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <select id="select-kitchen-course" class="form-select" style="padding:0.6rem 1rem; font-size:0.875rem;">
              ${menu.map((c, i) => `
                <option value="${i}">Course 0${i+1}: ${esc(c.recipe.title)}</option>
              `).join('')}
            </select>
            <button id="btn-launch-kitchen-mode" class="btn-primary" style="font-size:0.95rem; padding:0.6rem 1.4rem;">
              ▶ Launch Kitchen Mode
            </button>
          </div>
        </div>
      </section>

      <!-- Coordinated Multi-Course Menu Bar -->
      <div class="bento-card" style="margin-bottom:2rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.75rem;">
          <span class="card-badge">ACTIVE MULTI-COURSE SESSION (${menu.length} COURSES)</span>
          <button id="btn-add-all-mise-shopping" class="btn-secondary" style="font-size:0.75rem; padding:0.3rem 0.7rem;">
            🛒 Send All Ingredients to Provisions
          </button>
        </div>
        <div style="display:flex; gap:1rem; flex-wrap:wrap;">
          ${menu.map((c, i) => `
            <div style="background:var(--bg-elevated); padding:0.6rem 1rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle); display:flex; align-items:center; gap:0.5rem;">
              <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-primary);">0${i+1}</span>
              <strong style="font-size:0.875rem;">${esc(c.recipe.title)}</strong>
              <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">(${c.recipe.totalMins}m)</span>
            </div>
          `).join('')}
        </div>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; align-items:start;">
        <!-- Intelligent Dynamic Prep Checklist -->
        <div class="bento-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span class="card-badge">STATION CHECKLIST</span>
            <span id="mise-progress-label" style="font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-primary);">0 / ${allPrepTasks.length} Ready</span>
          </div>
          <h2 style="font-size:1.6rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Pre-Service Preparation</h2>
          <div class="mise-progress-track" role="progressbar" aria-label="Prep completion progress">
            <div id="mise-progress-bar" class="mise-progress-fill"></div>
          </div>

          ${menu.map((c, i) => `
            <div style="margin-bottom:1.5rem; background:var(--bg-elevated); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1rem;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <h4 style="font-size:0.9rem; font-family:var(--font-mono); color:var(--gold-primary); margin:0; text-transform:uppercase;">
                  COURSE 0${i+1}: ${esc(c.recipe.title)}
                </h4>
                <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${esc(c.slot.toUpperCase())}</span>
              </div>
              <div style="display:flex; flex-direction:column; gap:0.5rem;">
                ${(c.recipe.miseEnPlace || []).map(task => `
                  <label style="display:flex; align-items:flex-start; gap:0.6rem; font-size:0.85rem; cursor:pointer; line-height:1.4;">
                    <input type="checkbox" class="mise-check" style="margin-top:0.2rem;">
                    <span>${esc(task)}</span>
                  </label>
                `).join('')}
                ${(c.recipe.equipment || []).map(eq => `
                  <label style="display:flex; align-items:flex-start; gap:0.6rem; font-size:0.85rem; cursor:pointer; line-height:1.4; color:var(--text-muted);">
                    <input type="checkbox" class="mise-check" style="margin-top:0.2rem;">
                    <span>Stage ${esc(eq.name)} (${esc(eq.type || 'Cookware')})</span>
                  </label>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>

        <!-- Backward Scheduled Timeline -->
        <div class="bento-card">
          <span class="card-badge">SYNCHRONIZATION</span>
          <h2 style="font-size:1.6rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Backward Service Timeline</h2>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:1.25rem;">Target Service Pickup: <strong>T-0 (19:30)</strong>. Timed so all multi-course components hit the pass simultaneously.</p>

          <div style="border-left:2px solid var(--border-active); padding-left:1.25rem; display:flex; flex-direction:column; gap:1.25rem;">
            ${timelineEntries.map(entry => `
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.25rem;">
                  <span style="font-family:var(--font-mono); font-size:0.75rem; color:${entry.offset.includes('T - 0') ? 'var(--emerald)' : 'var(--gold-primary)'}; font-weight:700;">
                    ${entry.offset}
                  </span>
                  <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); background:var(--bg-elevated); padding:0.15rem 0.4rem; border-radius:var(--radius-sm);">
                    ${entry.station}
                  </span>
                </div>
                <h4 style="font-size:1rem; font-family:var(--font-serif); margin:0 0 0.25rem 0;">${entry.title}</h4>
                <p style="font-size:0.8rem; color:var(--text-secondary); margin:0; line-height:1.45;">${entry.desc}</p>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;

    // Interactive Checklist Tracker
    const checkBoxes = $$(".mise-check", container);
    checkBoxes.forEach(cb => {
      cb.onchange = () => {
        const checkedCount = $$(".mise-check:checked", container).length;
        const total = checkBoxes.length;
        const label = $("#mise-progress-label", container);
        const bar = $("#mise-progress-bar", container);
        const parentLabel = cb.closest("label");
        if (parentLabel) {
          parentLabel.classList.toggle("task-completed", cb.checked);
        }
        const pct = total > 0 ? (checkedCount / total) * 100 : 0;
        if (bar) {
          bar.style.width = `${pct}%`;
        }
        if (label) {
          label.textContent = `${checkedCount} / ${total} Ready (${Math.round(pct)}%)`;
          if (checkedCount === total) {
            label.textContent = `★ ALL ${total} TASKS READY!`;
            label.style.color = "var(--emerald)";
          } else {
            label.style.color = "var(--gold-primary)";
          }
        }
      };
    });

    // Kitchen Mode Launch
    $("#btn-launch-kitchen-mode", container).onclick = () => {
      const select = $("#select-kitchen-course", container);
      const idx = select ? parseInt(select.value) : 0;
      const targetRecipe = menu[idx] ? menu[idx].recipe : primaryRecipe;
      launchKitchenMode(targetRecipe);
    };

    // Send all ingredients to shopping
    const btnShopAll = $("#btn-add-all-mise-shopping", container);
    if (btnShopAll) {
      btnShopAll.onclick = () => {
        let count = 0;
        menu.forEach(c => {
          c.recipe.ingredients.forEach(ing => {
            AppState.shoppingList.push({
              name: ing.name,
              qty: ing.qty,
              unit: ing.unit,
              dept: ing.dept || "Pantry",
              done: false
            });
            count++;
          });
        });
        localStorage.setItem("atelier_shopping_v2", JSON.stringify(AppState.shoppingList));
        showNotification(`Added ${count} ingredients from all ${menu.length} courses to Provisions!`);
      };
    }
  }

  // Full Screen Kitchen Mode Implementation
  function launchKitchenMode(recipe) {
    AppState.kitchenModeActive = true;
    AppState.kitchenStepIndex = 0;
    requestWakeLock();
    initAudio();

    let overlay = $("#kitchen-mode-container");
    if (!overlay) {
      overlay = document.createElement("div");
      overlay.id = "kitchen-mode-container";
      overlay.className = "kitchen-mode-overlay";
      document.body.appendChild(overlay);
    }
    overlay.style.display = "flex";
    document.body.style.overflow = "hidden";

    renderKitchenStep(overlay, recipe);
  }

  function renderKitchenStep(overlay, recipe) {
    const step = recipe.steps[AppState.kitchenStepIndex];
    const totalSteps = recipe.steps.length;

    overlay.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem; margin-bottom:2rem;">
        <div>
          <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--gold-primary);">L'ATELIER · KITCHEN MODE</span>
          <h2 style="font-family:var(--font-serif); font-size:1.4rem;">${esc(recipe.title)}</h2>
        </div>
        <div style="display:flex; gap:0.75rem; align-items:center;">
          <button id="btn-read-aloud" class="btn-secondary" style="font-size:0.85rem;">
            🔊 Read Aloud
          </button>
          <button id="btn-toggle-voice" class="btn-secondary" style="font-size:0.85rem;">
            ${AppState.isVoiceActive ? '🎙 Stop Voice' : '🎙 Voice Control'}
          </button>
          <button id="btn-test-chime" class="btn-secondary" style="font-size:0.85rem;">
            🔔 Test Chime
          </button>
          <button id="btn-exit-kitchen" class="btn-icon" style="width:40px;height:40px;" title="Exit Kitchen Mode">✕</button>
        </div>
      </div>

      <div style="flex:1; display:flex; flex-direction:column; justify-content:center; max-width:1000px; margin:0 auto; width:100%;">
        <span style="font-family:var(--font-mono); font-size:1.1rem; color:var(--gold-primary); margin-bottom:0.75rem; font-weight:600;">
          STEP 0${AppState.kitchenStepIndex + 1} OF 0${totalSteps}
        </span>
        <h1 class="kitchen-step-title">${esc(step.text)}</h1>

        ${step.sensoryCue ? `
          <div style="background:var(--bg-elevated); padding:1.25rem; border-radius:var(--radius-md); border-left:4px solid var(--gold-primary); margin-bottom:1.5rem;">
            <strong style="font-family:var(--font-mono); font-size:0.8rem; color:var(--gold-primary); text-transform:uppercase;">What to Watch & Listen For:</strong>
            <p style="font-size:1.1rem; color:var(--text-secondary); margin-top:0.25rem;">${esc(step.sensoryCue)}</p>
          </div>
        ` : ''}

        ${true ? `
          <div style="display:flex; align-items:center; gap:2rem; background:var(--bg-card); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-active); margin-bottom:2rem; width:fit-content;">
            <div>
              <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">${step.timerMins ? "Step timer" : "Optional timer — not a recipe duration"}</span>
              <div id="kitchen-timer-clock" class="kitchen-timer-display">${step.timerMins || 5}:00</div>
            </div>
            <button id="btn-start-kitchen-timer" class="btn-primary" style="font-size:1.1rem; padding:0.8rem 1.6rem;">
              ▶ Start ${step.timerMins || 5} Minute Timer
            </button>
          </div>
        ` : ''}
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border-subtle); padding-top:1.5rem; margin-top:2rem;">
        <button id="btn-prev-step" class="btn-secondary" style="font-size:1.1rem; padding:0.8rem 1.8rem;" ${AppState.kitchenStepIndex === 0 ? 'disabled' : ''}>
          ← Previous Step
        </button>
        <span style="font-family:var(--font-mono); color:var(--text-muted);">
          Voice: Next step · Previous step · Repeat step · Start 5 minute timer
        </span>
        <button id="btn-next-step" class="btn-primary" style="font-size:1.1rem; padding:0.8rem 1.8rem;">
          ${AppState.kitchenStepIndex === totalSteps - 1 ? 'Finish Cooking ✦' : 'Next Step →'}
        </button>
      </div>
    `;

    // Bindings
    $("#btn-prev-step", overlay).onclick = () => {
      if (AppState.kitchenStepIndex > 0) {
        AppState.kitchenStepIndex--;
        renderKitchenStep(overlay, recipe);
      }
    };

    $("#btn-next-step", overlay).onclick = () => {
      if (AppState.kitchenStepIndex < totalSteps - 1) {
        AppState.kitchenStepIndex++;
        renderKitchenStep(overlay, recipe);
      } else {
        exitKitchenMode();
      }
    };

    $("#btn-exit-kitchen", overlay).onclick = exitKitchenMode;

    $("#btn-read-aloud", overlay).onclick = () => {
      if ("speechSynthesis" in window) {
        window.speechSynthesis.cancel();
        const utter = new SpeechSynthesisUtterance(step.text);
        window.speechSynthesis.speak(utter);
      } else {
        showNotification("Speech synthesis unavailable in this browser.");
      }
    };

    $("#btn-test-chime", overlay).onclick = () => {
      playChime();
      showNotification("Synthesized chime played.");
    };

    $("#btn-toggle-voice", overlay).onclick = () => {
      try { initAudio(); } catch {}
      toggleVoiceNavigation(overlay, recipe);
    };

    const timerBtn = $("#btn-start-kitchen-timer", overlay);
    if (timerBtn) {
      timerBtn.onclick = () => {
        try { initAudio(); } catch {}
        startStepTimer(step.timerMins || 5);
        timerBtn.textContent = "Timer Running...";
        timerBtn.disabled = true;
      };
    }
  }

  let kitchenTimerInterval = null;
  let kitchenTimerDeadline = 0;
  function startStepTimer(minutes) {
    if (!Number.isFinite(minutes) || minutes <= 0 || minutes > 1440) return;
    clearInterval(kitchenTimerInterval);
    kitchenTimerDeadline = Date.now() + minutes * 60000;
    const tick = () => {
      const remaining = Math.max(0, Math.ceil((kitchenTimerDeadline - Date.now()) / 1000));
      const clock = $("#kitchen-timer-clock");
      if (clock) clock.textContent = `${Math.floor(remaining / 60)}:${String(remaining % 60).padStart(2, '0')}`;
      if (!remaining) { clearInterval(kitchenTimerInterval); kitchenTimerInterval = null; playChime(); showNotification("Kitchen timer finished!"); }
    };
    tick(); kitchenTimerInterval = setInterval(tick, 250);
    showNotification(`${minutes} minute timer started. Replaces the previous kitchen timer.`);
  }

  function toggleVoiceNavigation(overlay, recipe) {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
      showNotification("Speech recognition is not supported in this browser.");
      return;
    }
    if (AppState.isVoiceActive) {
      AppState.speechRecognition?.stop();
      AppState.isVoiceActive = false;
      showNotification("Voice navigation stopped.");
      renderKitchenStep(overlay, recipe);
      return;
    }

    try {
      const rec = new SR();
      rec.continuous = true;
      rec.lang = "en-US";
      rec.onresult = (e) => {
        const transcript = e.results[e.results.length - 1][0].transcript.toLowerCase().trim();
        const command = window.KitchenOperations.voiceCommand(transcript);
        if (!command) return;
        if (command.type === "next") {
          if (AppState.kitchenStepIndex < recipe.steps.length - 1) {
            AppState.kitchenStepIndex++;
            renderKitchenStep(overlay, recipe);
          }
        } else if (command.type === "previous") {
          if (AppState.kitchenStepIndex > 0) {
            AppState.kitchenStepIndex--;
            renderKitchenStep(overlay, recipe);
          }
        } else if (command.type === "repeat") {
          $("#btn-read-aloud", overlay)?.click();
        } else if (command.type === "timer") {
          startStepTimer(command.minutes);
        }
      };
      rec.onerror = () => { AppState.isVoiceActive = false; showNotification("Voice stopped. Check microphone permission or use the step buttons."); };
      rec.onend = () => { AppState.isVoiceActive = false; if (AppState.kitchenModeActive) renderKitchenStep(overlay, recipe); };
      rec.start();
      AppState.speechRecognition = rec;
      AppState.isVoiceActive = true;
      showNotification("Voice navigation active: Say 'Next step', 'Previous step', 'Repeat step', or 'Start 5 minute timer'.");
      renderKitchenStep(overlay, recipe);
    } catch (err) {
      showNotification("Could not start voice recognition.");
    }
  }

  function exitKitchenMode() {
    AppState.kitchenModeActive = false;
    clearInterval(kitchenTimerInterval); kitchenTimerInterval = null;
    releaseWakeLock();
    if (AppState.speechRecognition) {
      AppState.speechRecognition.stop();
      AppState.isVoiceActive = false;
    }
    window.speechSynthesis?.cancel();
    const overlay = $("#kitchen-mode-container");
    if (overlay) overlay.style.display = "none";
    document.body.style.overflow = "auto";
  }

  // =========================================================================
  // VIEW: 6. THE CULINARY ACADEMY
  // =========================================================================
  function renderAcademyView(container) {
    const lessons = window.ACADEMY_LESSONS || [];
    const tracks = ["Foundations", "Intermediate", "Advanced", "Professional Kitchen"];

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">THE ACADEMY</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Culinary Academy Curriculum</h1>
        <p style="color:var(--text-secondary); max-width:760px;">A structured professional culinary curriculum from basic knife grips and egg protein geometry to classical mother sauces and Escoffier brigade command systems.</p>
      </section>

      <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:2rem;">
        ${tracks.map((t, i) => `
          <button class="nav-pill btn-academy-track ${i === 0 ? 'active' : ''}" data-track="${t}">
            ${esc(t)}
          </button>
        `).join('')}
      </div>

      <div id="academy-lessons-grid" class="bento-grid">
        <!-- Lessons rendered here -->
      </div>
    `;

    function renderLessons(track) {
      const filtered = lessons.filter(l => l.track === track || (!lessons.some(x => x.track === track) && l.track.includes(track.split(' ')[0])));
      const grid = $("#academy-lessons-grid", container);
      grid.innerHTML = filtered.map(l => `
        <article class="bento-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span class="card-badge">${esc(l.track.toUpperCase())}</span>
            <span style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted);">${l.durationMins} MINS · ${esc(l.difficulty)}</span>
          </div>
          <h3 class="card-title">${esc(l.title)}</h3>
          <p class="card-desc">${esc(l.summary)}</p>
          
          <div style="margin-top:auto; padding-top:1rem; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:0.75rem; color:var(--text-muted);">${(l.contentSections || []).length} instructional modules</span>
            <button class="btn-primary btn-open-lesson" data-id="${l.id}" style="font-size:0.8rem; padding:0.4rem 0.9rem;">
              Study Lesson →
            </button>
          </div>
        </article>
      `).join('');

      $$(".btn-open-lesson", grid).forEach(b => {
        b.onclick = () => openLessonModal(b.dataset.id);
      });
    }

    $$(".btn-academy-track", container).forEach(btn => {
      btn.onclick = () => {
        $$(".btn-academy-track", container).forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        renderLessons(btn.dataset.track);
      };
    });

    renderLessons(tracks[0]);
  }

  function openLessonModal(lessonId) {
    const lesson = (window.ACADEMY_LESSONS || []).find(l => l.id === lessonId);
    if (!lesson) return;

    let modal = $("#atelier-generic-modal");
    if (!modal) {
      modal = document.createElement("dialog");
      modal.id = "atelier-generic-modal";
      modal.className = "atelier-modal";
      document.body.appendChild(modal);
    }

    modal.innerHTML = `
      <button class="modal-close-btn" onclick="this.closest('dialog').close()">✕</button>
      <span class="card-badge">${esc(lesson.track.toUpperCase())} TRACK · ${lesson.durationMins} MINS</span>
      <h2 style="font-size:2.2rem; font-family:var(--font-serif); margin:0.5rem 0 1rem 0;">${esc(lesson.title)}</h2>
      <p style="font-size:1.05rem; color:var(--text-secondary); line-height:1.6; margin-bottom:2rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1.25rem;">
        ${esc(lesson.summary)}
      </p>

      <div style="display:flex; flex-direction:column; gap:2rem;">
        ${(lesson.contentSections || []).map(sec => `
          <div>
            <h3 style="font-size:1.35rem; font-family:var(--font-serif); color:var(--gold-primary); margin-bottom:0.5rem;">${esc(sec.heading)}</h3>
            <div style="font-size:0.95rem; color:var(--text-secondary); line-height:1.7; white-space:pre-line;">${esc(sec.text)}</div>
          </div>
        `).join('')}
      </div>

      ${lesson.commonMistakes ? `
        <div style="margin-top:2.5rem; background:var(--bg-elevated); padding:1.5rem; border-radius:var(--radius-lg); border-left:4px solid var(--crimson);">
          <h4 style="font-family:var(--font-mono); font-size:0.85rem; color:var(--crimson); text-transform:uppercase; margin-bottom:0.75rem;">Common Pitfalls & Mistakes</h4>
          <ul style="font-size:0.9rem; color:var(--text-secondary); margin-left:1.2rem; display:flex; flex-direction:column; gap:0.5rem;">
            ${lesson.commonMistakes.map(m => `<li><strong>${esc(m.mistake)}:</strong> ${esc(m.consequence)}</li>`).join('')}
          </ul>
        </div>
      ` : ''}

      <div style="margin-top:2rem; display:flex; justify-content:flex-end;">
        <button class="btn-primary" onclick="this.closest('dialog').close()">Close Lesson</button>
      </div>
    `;

    modal.showModal();
  }

  // =========================================================================
  // VIEW: 7. INTERACTIVE FOOD SCIENCE LABORATORY
  // =========================================================================
  function renderScienceLabView(container) {
    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">THE FOOD LABORATORY</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">The Science of Cooking</h1>
        <p style="color:var(--text-secondary); max-width:760px;">Accurate mathematical and physical models of culinary phenomena: thermal diffusivity in pan metallurgy, emulsion surfactant micro-physics, Maillard reaction kinetics, and collagen unwinding.</p>
      </section>

      <div class="bento-grid" style="margin-bottom:3rem;">
        <!-- 1. Heat Transfer -->
        <article class="bento-card">
          <span class="card-badge">SIMULATION 01 · THERMAL PHYSICS</span>
          <h3 class="card-title">Pan Metallurgy & Thermal Diffusivity</h3>
          <p class="card-desc">Compare the thermal response of Copper, Clad Aluminum, Cast Iron, and Stainless Steel.</p>
          
          <div style="margin:1rem 0;">
            <label class="form-label">Select Pan Metal:</label>
            <select id="sim-pan-metal" class="form-select" style="width:100%; margin-bottom:0.75rem;">
              <option value="copper">Copper (k = 385 W/mK)</option>
              <option value="aluminum">Clad Aluminum (k = 205 W/mK)</option>
              <option value="cast_iron" selected>Cast Iron (k = 52 W/mK)</option>
              <option value="stainless">Stainless Steel (k = 16 W/mK)</option>
            </select>

            <label class="form-label">Burner Power (Watts):</label>
            <input type="range" id="sim-burner-watts" min="1000" max="3500" step="100" value="2200" class="range-slider">
            <span id="disp-burner-watts" style="font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-primary);">2200 W</span>
          </div>

          <div id="sim-pan-results" style="background:var(--bg-elevated); padding:1rem; border-radius:var(--radius-md); font-size:0.8rem; font-family:var(--font-mono);">
            <!-- Dynamic pan results -->
          </div>
        </article>

        <!-- 2. Emulsion Micro-Physics -->
        <article class="bento-card">
          <span class="card-badge">SIMULATION 02 · COLLOIDS</span>
          <h3 class="card-title">Emulsion Stability & Droplet Diameter</h3>
          <p class="card-desc">Simulate droplet packing and calculate the catastrophic phase inversion limit (74%).</p>
          
          <div style="margin:1rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-family:var(--font-mono);">
              <span>OIL VOLUME</span> <span id="disp-oil-ml">180 ml</span>
            </div>
            <input type="range" id="sim-oil-ml" min="50" max="350" value="180" class="range-slider">

            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-family:var(--font-mono); margin-top:0.75rem;">
              <span>WHISK SHEAR SPEED</span> <span id="disp-shear-rpm">650 RPM</span>
            </div>
            <input type="range" id="sim-shear-rpm" min="60" max="1200" value="650" class="range-slider">
          </div>

          <div id="sim-emulsion-results" style="background:var(--bg-elevated); padding:1rem; border-radius:var(--radius-md); font-size:0.8rem; font-family:var(--font-mono);">
            <!-- Dynamic emulsion results -->
          </div>
        </article>

        <!-- 3. Maillard Moisture Delay -->
        <article class="bento-card">
          <span class="card-badge">SIMULATION 03 · ORGANIC CHEMISTRY</span>
          <h3 class="card-title">Maillard Kinetics & Moisture Delay</h3>
          <p class="card-desc">Discover why surface moisture suppresses browning (latent heat: 2,260 kJ/kg).</p>
          
          <div style="margin:1rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-family:var(--font-mono);">
              <span>SURFACE MOISTURE</span> <span id="disp-moisture-pct">35%</span>
            </div>
            <input type="range" id="sim-moisture-pct" min="0" max="100" value="35" class="range-slider">

            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-family:var(--font-mono); margin-top:0.75rem;">
              <span>PAN TEMPERATURE</span> <span id="disp-pan-temp">175°C</span>
            </div>
            <input type="range" id="sim-pan-temp" min="110" max="230" value="175" class="range-slider">
          </div>

          <div id="sim-maillard-results" style="background:var(--bg-elevated); padding:1rem; border-radius:var(--radius-md); font-size:0.8rem; font-family:var(--font-mono);">
            <!-- Dynamic Maillard results -->
          </div>
        </article>

        <!-- 4. Collagen Conversion -->
        <article class="bento-card">
          <span class="card-badge">SIMULATION 04 · BIOCHEMISTRY</span>
          <h3 class="card-title">Collagen-to-Gelatin Kinetics</h3>
          <p class="card-desc">Arrhenius thermal rate model for dissolving connective tissue in braises.</p>
          
          <div style="margin:1rem 0;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-family:var(--font-mono);">
              <span>BRAISE TEMPERATURE</span> <span id="disp-braise-temp">82°C</span>
            </div>
            <input type="range" id="sim-braise-temp" min="60" max="100" value="82" class="range-slider">

            <div style="display:flex; justify-content:space-between; font-size:0.75rem; font-family:var(--font-mono); margin-top:0.75rem;">
              <span>TIME IN OVEN</span> <span id="disp-braise-hours">4 Hours</span>
            </div>
            <input type="range" id="sim-braise-hours" min="1" max="8" value="4" class="range-slider">
          </div>

          <div id="sim-collagen-results" style="background:var(--bg-elevated); padding:1rem; border-radius:var(--radius-md); font-size:0.8rem; font-family:var(--font-mono);">
            <!-- Dynamic Collagen results -->
          </div>
        </article>
      </div>
    `;

    // Bindings for Simulators
    function updatePanSim() {
      const metal = $("#sim-pan-metal", container).value;
      const watts = parseInt($("#sim-burner-watts", container).value);
      $("#disp-burner-watts", container).textContent = `${watts} W`;
      const res = window.ScienceEngine.simulatePanHeating(metal, 4.0, watts);
      $("#sim-pan-results", container).innerHTML = `
        <div style="color:var(--gold-primary); font-weight:700;">TIME TO 180°C SEAR: ${res.timeToSearSeconds} SECONDS</div>
        <div>Thermal Diffusivity: ${res.thermalDiffusivity} mm²/s</div>
        <div>Pan Mass: ${res.massKg} kg</div>
        <div style="color:var(--text-muted); margin-top:0.35rem;">Thermal Uniformity: ${res.uniformityScore}%</div>
      `;
    }

    function updateEmulsionSim() {
      const oil = parseInt($("#sim-oil-ml", container).value);
      const rpm = parseInt($("#sim-shear-rpm", container).value);
      $("#disp-oil-ml", container).textContent = `${oil} ml`;
      $("#disp-shear-rpm", container).textContent = `${rpm} RPM`;
      const res = window.ScienceEngine.simulateEmulsion(oil, 35, 2, rpm);
      $("#sim-emulsion-results", container).innerHTML = `
        <div style="color:${res.isBroken ? 'var(--crimson)' : 'var(--emerald)'}; font-weight:700;">
          STATUS: ${res.isBroken ? 'BROKEN / PHASE INVERSION' : 'STABLE COLLOID'}
        </div>
        <div>Oil Volume Fraction: ${res.oilFraction}% (Max: 74%)</div>
        <div>Droplet Diameter: ${res.dropletDiameterMicrons} µm</div>
        <div style="color:var(--text-muted); margin-top:0.35rem;">${res.diagnostic}</div>
      `;
    }

    function updateMaillardSim() {
      const moisture = parseInt($("#sim-moisture-pct", container).value);
      const temp = parseInt($("#sim-pan-temp", container).value);
      $("#disp-moisture-pct", container).textContent = `${moisture}%`;
      $("#disp-pan-temp", container).textContent = `${temp}°C`;
      const res = window.ScienceEngine.simulateMaillard(moisture, temp);
      $("#sim-maillard-results", container).innerHTML = `
        <div style="color:var(--gold-primary); font-weight:700;">STEAMING DELAY: ${res.delaySeconds} SECONDS</div>
        <div>Browning Rate Rating: ${res.browningRateScore}%</div>
        <div style="color:var(--text-muted); margin-top:0.35rem;">${res.status}</div>
      `;
    }

    function updateCollagenSim() {
      const temp = parseInt($("#sim-braise-temp", container).value);
      const hrs = parseInt($("#sim-braise-hours", container).value);
      $("#disp-braise-temp", container).textContent = `${temp}°C`;
      $("#disp-braise-hours", container).textContent = `${hrs} Hours`;
      const res = window.ScienceEngine.simulateCollagenConversion(temp, hrs);
      $("#sim-collagen-results", container).innerHTML = `
        <div style="color:var(--emerald); font-weight:700;">CONVERSION TO GELATIN: ${res.conversionPct}%</div>
        <div>Mouthfeel: ${res.tendernessScore}</div>
        <div style="color:var(--text-muted); margin-top:0.35rem;">Richness Body: ${res.gelatinConcentrationRating}/100</div>
      `;
    }

    $("#sim-pan-metal", container).onchange = updatePanSim;
    $("#sim-burner-watts", container).oninput = updatePanSim;
    $("#sim-oil-ml", container).oninput = updateEmulsionSim;
    $("#sim-shear-rpm", container).oninput = updateEmulsionSim;
    $("#sim-moisture-pct", container).oninput = updateMaillardSim;
    $("#sim-pan-temp", container).oninput = updateMaillardSim;
    $("#sim-braise-temp", container).oninput = updateCollagenSim;
    $("#sim-braise-hours", container).oninput = updateCollagenSim;

    updatePanSim();
    updateEmulsionSim();
    updateMaillardSim();
    updateCollagenSim();
  }

  // =========================================================================
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
            <button id="btn-export-canvas" class="btn-primary" style="font-size:0.8rem; padding:0.3rem 0.7rem;">Export PNG ⬇</button>
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
      $("#btn-export-canvas", container).onclick = () => {
        const link = document.createElement("a");
        link.download = "latelier-plating-design.png";
        link.href = canvas.toDataURL("image/png");
        link.click();
        showNotification("Plating composition exported as PNG.");
      };

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

  // =========================================================================
  // VIEW: 9. PERSONAL RECIPE NOTEBOOK & VAULT
  // =========================================================================
  function renderNotebookView(container) {
    const allRecipes = window.MASTER_RECIPES || [];
    const saved = allRecipes.filter(r => AppState.savedRecipeIds.includes(r.id));

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">THE PERSONAL VAULT</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Your Culinary Notebook & Recipe Box</h1>
        <p style="color:var(--text-secondary); max-width:760px;">Your saved master recipes, personal tasting notes, and session customizations. Export a complete JSON backup to safeguard your collection.</p>
      </section>

      <div style="display:flex; gap:0.75rem; margin-bottom:2rem;">
        <button id="btn-export-backup" class="btn-primary">Export JSON Backup</button>
        <label class="btn-secondary" style="cursor:pointer;">
          Restore Backup
          <input type="file" id="file-restore-backup" accept="application/json" style="display:none;">
        </label>
      </div>

      <h2 style="font-size:1.8rem; font-family:var(--font-serif); margin-bottom:1rem;">Saved Dishes (${saved.length})</h2>
      ${saved.length ? `
        <div class="bento-grid">
          ${saved.map(r => `
            <article class="bento-card">
              <div style="display:flex; justify-content:space-between; align-items:start;">
                <span class="card-badge">${esc(r.cuisine)}</span>
                <button class="btn-icon btn-remove-saved" data-id="${r.id}" title="Remove from Recipe Box">✕</button>
              </div>
              <h3 class="card-title">${esc(r.title)}</h3>
              <p class="card-desc">${esc(r.summary)}</p>
              
              <!-- Personal Notes Area -->
              <div style="margin:1rem 0; padding-top:0.75rem; border-top:1px solid var(--border-subtle);">
                <label style="font-size:0.75rem; font-family:var(--font-mono); color:var(--text-muted); display:block; margin-bottom:0.35rem;">YOUR TASTING NOTES:</label>
                <textarea class="form-input user-notes-input" data-id="${r.id}" style="width:100%; height:60px; font-size:0.8rem;" placeholder="Record seasonings, pan temperature tweaks, or wine pairings...">${esc(AppState.userNotes[r.id] || '')}</textarea>
              </div>

              <button class="btn-primary btn-open-recipe" data-id="${r.id}" style="width:100%; justify-content:center; margin-top:auto;">
                Open Full Recipe →
              </button>
            </article>
          `).join('')}
        </div>
      ` : `
        <div class="bento-card" style="text-align:center; padding:3rem;">
          <p style="color:var(--text-muted);">You have not starred any recipes yet. Browse the Master Library and click the star icon to save your favorites here.</p>
          <button class="btn-secondary" onclick="window.AtelierApp.navigateTo('recipes')" style="margin-top:1rem;">Explore Recipe Library →</button>
        </div>
      `}
    `;

    $$(".btn-remove-saved", container).forEach(b => {
      b.onclick = () => {
        toggleSaveRecipe(b.dataset.id);
        renderNotebookView(container);
      };
    });

    $$(".user-notes-input", container).forEach(textarea => {
      textarea.onchange = (e) => {
        AppState.userNotes[e.target.dataset.id] = e.target.value;
        localStorage.setItem("atelier_user_notes", JSON.stringify(AppState.userNotes));
        showNotification("Notes saved.");
      };
    });

    $$(".btn-open-recipe", container).forEach(b => {
      b.onclick = () => openRecipeModal(b.dataset.id);
    });

    $("#btn-export-backup", container).onclick = () => {
      const backup = {
        version: "2.0",
        timestamp: new Date().toISOString(),
        savedRecipeIds: AppState.savedRecipeIds,
        userNotes: AppState.userNotes,
        shoppingList: AppState.shoppingList,
        flavorProfile: AppState.flavorProfile
      };
      const blob = new Blob([JSON.stringify(backup, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `latelier-backup-${new Date().toISOString().split('T')[0]}.json`;
      a.click();
      URL.revokeObjectURL(url);
      showNotification("Backup downloaded successfully.");
    };

    $("#file-restore-backup", container).onchange = async (e) => {
      const file = e.target.files[0];
      if (!file) return;
      try {
        const text = await file.text();
        const data = JSON.parse(text);
        if (data.savedRecipeIds) AppState.savedRecipeIds = data.savedRecipeIds;
        if (data.userNotes) AppState.userNotes = data.userNotes;
        if (data.shoppingList) AppState.shoppingList = data.shoppingList;
        localStorage.setItem("atelier_saved_recipes", JSON.stringify(AppState.savedRecipeIds));
        localStorage.setItem("atelier_user_notes", JSON.stringify(AppState.userNotes));
        localStorage.setItem("atelier_shopping_v2", JSON.stringify(AppState.shoppingList));
        renderNotebookView(container);
        showNotification("Backup restored successfully!");
      } catch (err) {
        showNotification("Failed to parse backup file.");
      }
    };
  }

  // =========================================================================
  // VIEW: 10. SMART CONSOLIDATED SHOPPING LIST
  // =========================================================================
  function renderShoppingListView(container) {
    const items = AppState.shoppingList || [];
    const aisles = ["Produce", "Butchery", "Seafood", "Dairy", "Dry Goods", "Pantry"];

    container.innerHTML = `
      <section style="margin-bottom:2rem;">
        <span class="card-badge">PROVISIONS</span>
        <h1 style="font-size:2.4rem; font-family:var(--font-serif); margin:0.25rem 0 0.5rem 0;">Smart Grocery Provisions</h1>
        <p style="color:var(--text-secondary); max-width:720px;">Automatically normalized and grouped by grocery store aisle. Quantities combined across courses.</p>
      </section>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:0.5rem;">
        <div style="display:flex; gap:0.5rem;">
          <button id="btn-copy-shopping" class="btn-primary" style="font-size:0.85rem;">Copy List</button>
          <button id="btn-print-shopping" class="btn-secondary" style="font-size:0.85rem;">Print List</button>
        </div>
        <button id="btn-clear-shopping" class="btn-secondary" style="font-size:0.85rem; color:var(--crimson);">Clear List</button>
      </div>

      ${items.length ? `
        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:1.25rem;">
          ${aisles.map(aisle => {
            const aisleItems = items.filter(it => (it.dept || 'pantry').toLowerCase() === aisle.toLowerCase() || (aisle === 'Dry Goods' && it.dept === 'drygoods'));
            if (!aisleItems.length) return '';
            return `
              <div class="bento-card">
                <span class="card-badge">${esc(aisle.toUpperCase())}</span>
                <div style="display:flex; flex-direction:column; gap:0.6rem; margin-top:0.75rem;">
                  ${aisleItems.map((item, idx) => `
                    <label style="display:flex; align-items:center; gap:0.6rem; font-size:0.9rem; cursor:pointer;">
                      <input type="checkbox" class="shopping-item-check" data-name="${esc(item.name)}" ${item.done ? 'checked' : ''}>
                      <span style="${item.done ? 'text-decoration:line-through; color:var(--text-muted);' : ''}">
                        <strong>${item.qty} ${item.unit}</strong> ${esc(item.name)}
                      </span>
                    </label>
                  `).join('')}
                </div>
              </div>
            `;
          }).join('')}
        </div>
      ` : `
        <div class="bento-card" style="text-align:center; padding:3rem;">
          <p style="color:var(--text-muted);">Your shopping list is empty. Open any master recipe and click "Add Ingredients to Shopping List".</p>
        </div>
      `}
    `;

    $$(".shopping-item-check", container).forEach(box => {
      box.onchange = (e) => {
        const item = items.find(it => it.name === e.target.dataset.name);
        if (item) item.done = e.target.checked;
        localStorage.setItem("atelier_shopping_v2", JSON.stringify(items));
        renderShoppingListView(container);
      };
    });

    $("#btn-copy-shopping", container)?.addEventListener("click", () => {
      const text = items.map(it => `[${it.done ? 'X' : ' '}] ${it.qty} ${it.unit} ${it.name}`).join('\n');
      navigator.clipboard.writeText(text).then(() => showNotification("Shopping list copied to clipboard."));
    });

    $("#btn-print-shopping", container)?.addEventListener("click", () => window.print());

    $("#btn-clear-shopping", container)?.addEventListener("click", () => {
      if (confirm("Clear all items from your shopping list?")) {
        AppState.shoppingList = [];
        localStorage.setItem("atelier_shopping_v2", "[]");
        renderShoppingListView(container);
        showNotification("Shopping list cleared.");
      }
    });
  }

  // =========================================================================
  // RECIPE DETAIL MODAL (Complete 20-Field Editorial Presentation)
  // =========================================================================
  function openRecipeModal(recipeId) {
    const recipe = (window.MASTER_RECIPES || []).find(r => r.id === recipeId);
    if (!recipe) return;

    AppState.activeRecipe = recipe;
    AppState.activeRecipeServings = recipe.yieldServings || 4;

    let modal = $("#atelier-recipe-modal");
    if (!modal) {
      modal = document.createElement("dialog");
      modal.id = "atelier-recipe-modal";
      modal.className = "atelier-modal";
      document.body.appendChild(modal);
    }

    renderRecipeModalContent(modal, recipe);
    modal.showModal();
  }

  function renderRecipeModalContent(modal, recipe) {
    const scaleFactor = AppState.activeRecipeServings / (recipe.yieldServings || 4);

    modal.innerHTML = `
      ${window.culinaryImage(recipe)}
      <p class="card-badge">Needs source review</p>
      <button class="modal-close-btn" onclick="this.closest('dialog').close()">✕</button>

      <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:0.75rem;">
        <span class="card-badge">${esc(recipe.cuisine)}</span>
        <span class="card-badge">${recipe.totalMins} MINS TOTAL</span>
        <span class="card-badge">${esc(recipe.difficulty.toUpperCase())}</span>
      </div>

      <h1 style="font-size:clamp(2rem, 3.5vw, 2.8rem); font-family:var(--font-serif); margin-bottom:0.5rem; line-height:1.15;">
        ${esc(recipe.title)}
      </h1>
      <p style="font-size:1.1rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.5rem;">
        ${esc(recipe.summary)}
      </p>

      <!-- Sensory Role Callout -->
      <div style="background:var(--bg-elevated); padding:1.25rem; border-radius:var(--radius-md); border-left:4px solid var(--gold-primary); margin-bottom:2rem;">
        <strong style="font-family:var(--font-mono); font-size:0.8rem; color:var(--gold-primary); text-transform:uppercase;">Sensory Profile:</strong>
        <p style="font-size:0.95rem; color:var(--text-secondary); margin-top:0.25rem;">${esc(recipe.sensoryRole)}</p>
      </div>

      <!-- Controls: Yield Scaler & Action Buttons -->
      <div style="display:flex; justify-content:space-between; align-items:center; background:var(--bg-elevated); padding:1rem 1.25rem; border-radius:var(--radius-lg); margin-bottom:2rem; flex-wrap:wrap; gap:1rem;">
        <div style="display:flex; align-items:center; gap:0.75rem;">
          <label style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-muted); text-transform:uppercase;">Servings / Yield:</label>
          <div style="display:flex; align-items:center; gap:0.35rem;">
            <button id="btn-scale-down" class="btn-secondary" style="padding:0.2rem 0.6rem;">-</button>
            <span id="disp-servings" style="font-family:var(--font-mono); font-weight:700; width:30px; text-align:center;">${AppState.activeRecipeServings}</span>
            <button id="btn-scale-up" class="btn-secondary" style="padding:0.2rem 0.6rem;">+</button>
          </div>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button id="btn-modal-cook" class="btn-primary">▶ Cook in Kitchen Mode</button>
          <button id="btn-modal-add-shopping" class="btn-secondary">+ Add to Shopping List</button>
          <button id="btn-modal-print" class="btn-secondary" title="Print recipe card">⎙ Print</button>
          <button id="btn-modal-star" class="btn-icon">
            ${AppState.savedRecipeIds.includes(recipe.id) ? '★' : '☆'}
          </button>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1.3fr; gap:2rem; margin-bottom:2.5rem;">
        <!-- Ingredients List -->
        <div>
          <h3 style="font-size:1.4rem; font-family:var(--font-serif); margin-bottom:1rem; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
            Ingredients
          </h3>
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.6rem; font-size:0.95rem;">
            ${recipe.ingredients.map(ing => {
              const scaledQty = +(ing.qty * scaleFactor).toFixed(ing.qty % 1 === 0 ? 0 : 2);
              return `
                <li style="padding-bottom:0.4rem; border-bottom:1px solid rgba(255,255,255,0.03);">
                  <strong style="color:var(--gold-primary); font-family:var(--font-mono);">${scaledQty} ${esc(ing.unit)}</strong> 
                  ${esc(ing.name)}
                  ${ing.prep ? `<span style="color:var(--text-muted); font-size:0.85rem;">(${esc(ing.prep)})</span>` : ''}
                </li>
              `;
            }).join('')}
          </ul>
        </div>

        <!-- Equipment & Mise en Place -->
        <div>
          <h3 style="font-size:1.4rem; font-family:var(--font-serif); margin-bottom:1rem; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
            Mise en Place & Equipment
          </h3>
          <div style="margin-bottom:1.25rem;">
            <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.5rem;">Required Equipment:</h4>
            <ul style="font-size:0.875rem; color:var(--text-secondary); margin-left:1.2rem; display:flex; flex-direction:column; gap:0.35rem;">
              ${(recipe.equipment || []).map(eq => `<li>${esc(eq.name)} ${eq.type === 'specialty' ? '<span class="card-badge" style="display:inline;padding:0.1rem 0.4rem;font-size:0.6rem;">SPECIALTY</span>' : ''}</li>`).join('')}
            </ul>
          </div>
          <div>
            <h4 style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.5rem;">Preparation Checklist:</h4>
            <ul style="font-size:0.875rem; color:var(--text-secondary); margin-left:1.2rem; display:flex; flex-direction:column; gap:0.35rem;">
              ${(recipe.miseEnPlace || []).map(m => `<li>${esc(m)}</li>`).join('')}
            </ul>
          </div>
        </div>
      </div>

      <!-- Step-by-Step Instructions -->
      <div style="margin-bottom:2.5rem;">
        <h3 style="font-size:1.6rem; font-family:var(--font-serif); margin-bottom:1.25rem; border-bottom:1px solid var(--border-subtle); padding-bottom:0.5rem;">
          Step-by-Step Culinary Method
        </h3>
        <div style="display:flex; flex-direction:column; gap:1.5rem;">
          ${recipe.steps.map(s => `
            <div style="display:flex; gap:1.25rem; background:var(--bg-elevated); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-subtle);">
              <div style="font-family:var(--font-display); font-size:1.4rem; font-weight:700; color:var(--gold-primary); width:32px;">
                0${s.stepNum}
              </div>
              <div style="flex:1;">
                <p style="font-size:1rem; line-height:1.6; margin-bottom:0.5rem;">${esc(s.text)}</p>
                ${s.sensoryCue ? `
                  <p style="font-size:0.85rem; color:var(--text-muted); font-style:italic;">
                    <strong>Sensory Indicator:</strong> ${esc(s.sensoryCue)}
                  </p>
                ` : ''}
                ${s.scienceNote ? `
                  <p style="font-size:0.825rem; color:var(--gold-primary); margin-top:0.4rem;">
                    <strong>Science Note:</strong> ${esc(s.scienceNote)}
                  </p>
                ` : ''}
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- Science & Troubleshooting Bento -->
      <div class="bento-grid" style="margin-bottom:2rem;">
        ${recipe.scienceNotes ? `
          <div class="bento-card">
            <span class="card-badge">FOOD SCIENCE</span>
            <h4 style="font-family:var(--font-serif); font-size:1.2rem; margin-bottom:0.5rem;">Molecular Transformation</h4>
            <ul style="font-size:0.85rem; color:var(--text-secondary); margin-left:1.2rem; display:flex; flex-direction:column; gap:0.4rem;">
              ${recipe.scienceNotes.map(sn => `<li>${esc(sn)}</li>`).join('')}
            </ul>
          </div>
        ` : ''}

        ${recipe.troubleshooting ? `
          <div class="bento-card">
            <span class="card-badge">TROUBLESHOOTING</span>
            <h4 style="font-family:var(--font-serif); font-size:1.2rem; margin-bottom:0.5rem;">Chef's Diagnostics</h4>
            <div style="font-size:0.85rem; color:var(--text-secondary); display:flex; flex-direction:column; gap:0.6rem;">
              ${recipe.troubleshooting.map(t => `
                <div>
                  <strong style="color:var(--crimson);">${esc(t.issue)}:</strong> ${esc(t.solution)}
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        ${recipe.flavorPairings ? `
          <div class="bento-card">
            <span class="card-badge">SOMMELIER & PAIRING</span>
            <h4 style="font-family:var(--font-serif); font-size:1.2rem; margin-bottom:0.5rem;">Harmonious Pairings</h4>
            <div style="font-size:0.85rem; color:var(--text-secondary); display:flex; flex-direction:column; gap:0.4rem;">
              ${recipe.flavorPairings.wine ? `<div><strong>Wine:</strong> ${esc(recipe.flavorPairings.wine)}</div>` : ''}
              ${recipe.flavorPairings.zeroProof ? `<div><strong>Zero-Proof:</strong> ${esc(recipe.flavorPairings.zeroProof)}</div>` : ''}
            </div>
          </div>
        ` : ''}
      </div>
    `;

    // Modal Events
    $("#btn-scale-down", modal).onclick = () => {
      if (AppState.activeRecipeServings > 1) {
        AppState.activeRecipeServings--;
        renderRecipeModalContent(modal, recipe);
      }
    };

    $("#btn-scale-up", modal).onclick = () => {
      if (AppState.activeRecipeServings < 20) {
        AppState.activeRecipeServings++;
        renderRecipeModalContent(modal, recipe);
      }
    };

    $("#btn-modal-cook", modal).onclick = () => {
      modal.close();
      launchKitchenMode(recipe);
    };

    $("#btn-modal-add-shopping", modal).onclick = () => {
      recipe.ingredients.forEach(ing => {
        const scaledQty = +(ing.qty * scaleFactor).toFixed(ing.qty % 1 === 0 ? 0 : 2);
        AppState.shoppingList.push({
          name: ing.name,
          qty: scaledQty,
          unit: ing.unit,
          dept: ing.dept || 'pantry',
          done: false
        });
      });
      localStorage.setItem("atelier_shopping_v2", JSON.stringify(AppState.shoppingList));
      showNotification(`Added ${recipe.ingredients.length} ingredients to shopping list.`);
    };

    $("#btn-modal-print", modal).onclick = () => window.print();

    $("#btn-modal-star", modal).onclick = () => {
      toggleSaveRecipe(recipe.id);
      $("#btn-modal-star", modal).innerHTML = AppState.savedRecipeIds.includes(recipe.id) ? '★' : '☆';
    };
  }

  function toggleSaveRecipe(id) {
    if (AppState.savedRecipeIds.includes(id)) {
      AppState.savedRecipeIds = AppState.savedRecipeIds.filter(x => x !== id);
      showNotification("Removed from Recipe Box.");
    } else {
      AppState.savedRecipeIds.push(id);
      showNotification("Saved to your Recipe Box! ★");
    }
    localStorage.setItem("atelier_saved_recipes", JSON.stringify(AppState.savedRecipeIds));
  }


  // =========================================================================
  // VIEW: KITCHEN PREP MANUAL (AUTHENTIC RESTAURANT BRIGADE STANDARDS)
  // =========================================================================
  function renderPrepManualView(container) {
    window.KitchenOperations.render(container);
  }


  // Initialization
  document.addEventListener("DOMContentLoaded", () => {
    applyTheme(AppState.theme);

    const themeToggleBtn = $("#theme-toggle");
    if (themeToggleBtn) {
      themeToggleBtn.onclick = () => {
        applyTheme(AppState.theme === "dark" ? "light" : "dark");
      };
    }

    $$(".nav-pill").forEach(btn => {
      btn.onclick = () => navigateTo(btn.dataset.view);
    });

    navigateTo(AppState.currentView);
  });

  // Global Export for console / cross-module access
  window.AtelierApp = {
    state: AppState,
    navigateTo: navigateTo,
    openRecipe: openRecipeModal,
    launchKitchen: launchKitchenMode
  };

})();
