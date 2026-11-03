/* ==========================================================================
   L'ATELIER · SALON PRIVÉ & CONFIDENTIAL ARCHIVES
   Secure Client-Side Decrypted Operations Engine
   ========================================================================== */

(() => {
  'use strict';

  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const e = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const safe = u => { try { const x = new URL(u); return ['https:', 'http:'].includes(x.protocol) ? x.href : ''; } catch { return ''; } };
  const youtube = u => { try { return ['youtube.com', 'www.youtube.com', 'm.youtube.com', 'youtu.be'].includes(new URL(u).hostname); } catch { return false; } };

  let key, data, rows = [], menu = [], checks = new Set(), notes = '', shopping = '', urls = [], view = 'library', current = null, session = 0, readerVersion = 0;
  let filters = { q: '', manual: '', kind: 'all', page: 0 };
  let lightboxZoom = 1;
  let isPanning = false;
  let panStart = { x: 0, y: 0 };
  let panOffset = { x: 0, y: 0 };

  function updateLightboxTransform() {
    const img = $('#vault-lightbox-img');
    const zoomText = $('#vault-zoom-level');
    if (img) {
      img.style.transform = `translate(${panOffset.x}px, ${panOffset.y}px) scale(${lightboxZoom})`;
    }
    if (zoomText) {
      zoomText.textContent = `${Math.round(lightboxZoom * 100)}%`;
    }
  }

  let modalReturnFocus = null;
  function openLightbox(src, title, tag) {
    modalReturnFocus = document.activeElement;
    const modal = $('#vault-lightbox');
    const img = $('#vault-lightbox-img');
    const titleEl = $('#vault-lightbox-title');
    const tagEl = $('#vault-lightbox-tag');
    const download = $('#vault-lightbox-download');
    if (!modal || !img) return;

    lightboxZoom = 1;
    panOffset = { x: 0, y: 0 };
    img.src = src;
    if (titleEl) titleEl.textContent = title;
    if (tagEl) tagEl.textContent = tag;
    if (download) download.href = src;
    updateLightboxTransform();
    modal.hidden = false;
    $("#vault-lightbox-close")?.focus();
  }

  function closeLightbox() {
    const modal = $('#vault-lightbox');
    if (modal) modal.hidden = true;
    if (modalReturnFocus?.isConnected) modalReturnFocus.focus();
    modalReturnFocus = null;
    lightboxZoom = 1;
    panOffset = { x: 0, y: 0 };
    updateLightboxTransform();
  }

  function scaleNumberString(value, factor) {
    return window.VaultQuantities.scale(value, factor);
  }

  function syncToPublicProvisions() {
    if (!$('#allow-public-export')?.checked) return;
    const raw = shopping.trim();
    if (!raw) {
      notifyVault('Private provisions list is empty. Add batch items from recipe tables first.', false);
      return;
    }
    try {
      const existing = JSON.parse(localStorage.getItem('atelier_shopping_v2') || '[]');
      const lines = raw.split('\n').map(l => l.replace(/^[☐☑✓]\s*/, '').trim()).filter(l => l && !l.startsWith('/*'));
      let addedCount = 0;
      const seenNames = new Set(existing.map(i => ((i.name || '') + '|' + (i.qty || '')).toLowerCase()));

      lines.forEach(line => {
        let name = line;
        let qty = '';
        if (line.includes('—')) {
          const parts = line.split('—');
          qty = parts[0].trim();
          name = parts[1].trim();
        }
        const identity = (name + '|' + qty).toLowerCase();
        if (!seenNames.has(identity)) {
          existing.push({
            id: 'priv-' + Math.random().toString(36).substring(2, 9),
            name: name,
            qty: qty,
            unit: '',
            dept: 'Pantry',
            done: false,
            timestamp: Date.now()
          });
          seenNames.add(identity);
          addedCount++;
        }
      });

      localStorage.setItem('atelier_shopping_v2', JSON.stringify(existing));
      notifyVault(`Synced ${addedCount} private items into Public Atelier Provisions! (Available on your mobile device)`);
    } catch (err) {
      notifyVault('Could not sync to public provisions.', false);
    }
  }

  function openBrigadeSheet() {
    const modal = $('#vault-brigade-sheet-modal');
    const content = $('#vault-brigade-sheet-content');
    if (!modal || !content) return;

    const bookmarkedPages = menu.map(id => rows.find(r => r.id === id)).filter(Boolean);
    const dateStr = new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });

    content.innerHTML = `
      <div class="brigade-pass-header">
        <div>
          <span style="font-family:var(--font-mono); font-size:0.75rem; letter-spacing:0.15em; color:var(--gold-primary); text-transform:uppercase;">
            L'Atelier · Salon Privé Operations Pass
          </span>
          <h2 style="font-family:var(--font-serif); font-size:2rem; color:#FFFFFF; margin:0.35rem 0 0 0;">
            Brigade Service Firing &amp; Pass Sheet
          </h2>
          <p style="font-size:0.85rem; color:var(--text-muted); margin:0.25rem 0 0 0;">
            Service Date: ${e(dateStr)} · Active Firing Sequence (${bookmarkedPages.length} Dishes)
          </p>
        </div>
        <div style="text-align:right;">
          <span class="vault-manual-pill" style="font-size:0.85rem; padding:0.4rem 0.8rem;">
            ${checks.size} / ${bookmarkedPages.length} STATIONS VERIFIED
          </span>
        </div>
      </div>

      <div style="margin-bottom:1.5rem;">
        <h4 style="font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; color:var(--gold-primary); margin-bottom:0.75rem;">
          Firing Sequence &amp; Station Assignments
        </h4>
        ${bookmarkedPages.map((p, idx) => {
          const isVerified = checks.has(p.id);
          const tables = (p.content || []).filter(c => c.kind === 'table');
          return `
            <div class="brigade-course-item">
              <div class="brigade-course-meta">
                <div style="display:flex; align-items:center; gap:0.6rem;">
                  <span style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--gold-primary);">
                    COURSE ${idx + 1}
                  </span>
                  <strong style="font-family:var(--font-serif); font-size:1.25rem; color:#FFFFFF;">${e(p.title)}</strong>
                </div>
                <div style="display:flex; align-items:center; gap:0.5rem;">
                  <span class="vault-manual-pill">${e(p.manual)} · P. ${p.number}</span>
                  <span style="font-family:var(--font-mono); font-size:0.75rem; color:${isVerified ? 'var(--emerald)' : 'var(--text-muted)'}; font-weight:600;">
                    ${isVerified ? '✓ VERIFIED' : '⏱ PENDING'}
                  </span>
                </div>
              </div>
              <div style="font-size:0.85rem; color:var(--text-secondary); line-height:1.6;">
                <p style="margin:0.25rem 0;"><strong>Operational Summary:</strong> ${e(p.text ? p.text.slice(0, 220) + '…' : 'Standard station preparation')}</p>
                ${tables.length ? `<p style="margin:0.25rem 0; font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-light);">✦ ${tables.length} Batch Formulation Table(s) Recorded</p>` : ''}
              </div>
            </div>
          `;
        }).join('') || '<p style="color:var(--text-muted);">No pages currently in Tasting Menu.</p>'}
      </div>
    `;

    modal.hidden = false;
  }
  document.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const modal = [...document.querySelectorAll('[role="dialog"]')].reverse().find(m => !m.hidden);
    if (!modal) return;
    const items = [...modal.querySelectorAll('button:not([disabled]),a[href],input,select,textarea,[tabindex="0"]')].filter(el => el.getClientRects().length);
    if (!items.length) return;
    const first=items[0],last=items[items.length-1];
    if (!modal.contains(document.activeElement) || (!event.shiftKey && document.activeElement===last)) {event.preventDefault();first.focus();}
    else if (event.shiftKey && document.activeElement===first) {event.preventDefault();last.focus();}
  });
  const PAGE_SIZE = 40;

  async function decrypt(file, activeKey = key) {
    const res = await fetch('private-vault/' + file, { cache: 'no-store' });
    if (!res.ok) throw Error('Unavailable encrypted file');
    const bytes = new Uint8Array(await res.arrayBuffer());
    return crypto.subtle.decrypt(
      { name: 'AES-GCM', iv: bytes.slice(0, 12), additionalData: new TextEncoder().encode('latelier-vault-v1') },
      activeKey,
      bytes.slice(12)
    );
  }

  // Toast Notification inside Vault
  function notifyVault(msg, isSuccess = true) {
    let toast = $('#vault-status');
    if (!toast) {
      toast = document.createElement('p');
      toast.id = 'vault-status';
      toast.setAttribute('role', 'status');
      document.body.appendChild(toast);
    }
    toast.innerHTML = `<span>${isSuccess ? '✦' : '⚠️'}</span> <span>${e(msg)}</span>`;
    clearTimeout(toast._timeout);
    toast._timeout = setTimeout(() => {
      toast.textContent = '';
    }, 4000);
  }

  // Unlock Submission
  $('#unlock').onsubmit = async event => {
    event.preventDefault();
    const ticket = ++session;
    const button = $('#unlock button');
    button.disabled = true;
    $('#message').textContent = 'Decrypting cryptographic archive in memory…';
    $('#message').style.color = 'var(--gold-primary)';

    try {
      const config = await (await fetch('private-vault/config.json', { cache: 'no-store' })).json();
      const material = await crypto.subtle.importKey(
        'raw',
        new TextEncoder().encode($('#password').value),
        'PBKDF2',
        false,
        ['deriveKey']
      );
      const derived = await crypto.subtle.deriveKey(
        {
          name: 'PBKDF2',
          salt: Uint8Array.from(atob(config.salt), c => c.charCodeAt(0)),
          iterations: config.iterations,
          hash: 'SHA-256'
        },
        material,
        { name: 'AES-GCM', length: 256 },
        false,
        ['decrypt']
      );

      const decoded = JSON.parse(new TextDecoder().decode(await decrypt('index.bin', derived)));
      if (ticket !== session) return;

      key = derived;
      data = decoded;
      rows = data.manuals.flatMap(m => m.pages.map(p => ({
        ...p,
        manual: m.name,
        mid: m.id,
        id: m.id + ':' + p.number
      })));

      $('#password').value = '';
      $('#login').hidden = true;
      $('#workspace').hidden = false;
      $('#lock').hidden = false;
      render();
      notifyVault('Private archive decrypted successfully. Session active.');
    } catch (err) {
      if (ticket === session) {
        key = null;
        $('#message').textContent = 'Authentication failed. Invalid master passphrase or connection error.';
        $('#message').style.color = '#ef4444';
      }
    } finally {
      button.disabled = false;
    }
  };

  function releaseImages() {
    closeLightbox();
    $('#vault-lightbox-img')?.removeAttribute('src');
    $('#vault-lightbox-download')?.removeAttribute('href');
    if ($('#vault-lightbox-title')) $('#vault-lightbox-title').textContent = '';
    if ($('#vault-lightbox-tag')) $('#vault-lightbox-tag').textContent = '';
    urls.forEach(URL.revokeObjectURL);
    urls = [];
    readerVersion++;
  }

  function lock() {
    session++;
    releaseImages();
    $("#vault-brigade-sheet-content")?.replaceChildren();
    if ($("#vault-brigade-sheet-modal")) $("#vault-brigade-sheet-modal").hidden = true;
    key = null;
    data = null;
    rows = [];
    menu = [];
    checks.clear();
    notes = '';
    shopping = '';
    current = null;
    filters = { q: '', manual: '', kind: 'all', page: 0 };
    view = 'library';
    $('#workspace').replaceChildren();
    $('#workspace').hidden = true;
    $('#login').hidden = false;
    $('#lock').hidden = true;
    $('#password').value = '';
    $('#message').textContent = 'Vault locked. Session pages and notes cleared. Any items explicitly exported to public provisions remain there.';
    $('#message').style.color = 'var(--text-muted)';
    $('#password').focus();
  }

  $('#lock').onclick = lock;
  window.addEventListener('pagehide', lock);

  function pageButton(p) {
    const inMenu = menu.includes(p.id);
    const isCurrent = current === p.id;
    return `
      <button class="vault-page-card ${isCurrent ? 'active-page' : ''}" data-open="${e(p.id)}">
        <div class="vault-page-card-top">
          <span class="vault-manual-pill">${e(p.manual)}</span>
          <span class="vault-page-num">P. ${p.number}</span>
        </div>
        <strong class="vault-page-title">${e(p.title)}</strong>
        <div class="vault-page-card-meta">
          ${p.hasIngredientTable ? '<span class="vault-tag-table">📊 Batch Table</span>' : ''}
          ${p.imageCount > 0 ? '<span class="vault-tag-photo">🖼️ Photo</span>' : ''}
          ${inMenu ? '<span class="vault-tag-table" style="color:var(--emerald); border-color:var(--emerald);">★ In Menu</span>' : ''}
        </div>
      </button>
    `;
  }

  function bindPages(root = document) {
    root.querySelectorAll('[data-open]').forEach(b => {
      b.onclick = () => openPage(b.dataset.open);
    });
  }

  // Master Render Function
  function render() {
    releaseImages();
    current = null;
    const w = $('#workspace');

    const navTabs = [
      ['library', '📖 Source Library'],
      ['inventory', '🗂️ Manual Inventory'],
      ['menu', '🍽️ Tasting Menu'],
      ['mise', '⏱️ Mise en Place'],
      ['shopping', '🛒 Private Provisions'],
      ['notes', '📓 Chef\'s Notebook'],
      ['videos', '🎥 Video Masterclasses'],
      ['prep', '📋 Brigade Prep Specs']
    ];

    w.innerHTML = `
      <div class="vault-header-hero">
        <span class="vault-hero-badge">CONFIDENTIAL RESTAURANT BRIGADE ARCHIVE</span>
        <h1 class="vault-hero-title">The Complete Kitchen Library</h1>
        <p class="vault-hero-lead">
          Authentic culinary specifications, batch formulas, high-resolution line scans, and station operating procedures. Decrypted in-memory on this device.
        </p>
      </div>

      <!-- Metrics Strip -->
      <div class="vault-stats-grid">
        <div class="vault-stat-card">
          <span class="vault-stat-value">${data.inventory?.length || data.manuals.length + data.aliases.length}</span>
          <span class="vault-stat-label">Supplied Files</span>
        </div>
        <div class="vault-stat-card">
          <span class="vault-stat-value">${rows.length}</span>
          <span class="vault-stat-label">Complete Pages</span>
        </div>
        <div class="vault-stat-card">
          <span class="vault-stat-value">${data.manuals.length}</span>
          <span class="vault-stat-label">Unique Manuals</span>
        </div>
        <div class="vault-stat-card">
          <span class="vault-stat-value" id="vault-stat-menu-count">${menu.length}</span>
          <span class="vault-stat-label">Active Menu Pages</span>
        </div>
      </div>

      <!-- Navigation Ribbon -->
      <nav class="vault-nav-ribbon" aria-label="Private workspace">
        ${navTabs.map(([v, label]) => `
          <button data-view="${v}" aria-pressed="${view === v}">
            ${label}
          </button>
        `).join('')}
      </nav>

      <!-- Dynamic View Body -->
      <div id="vault-body"></div>
      <p id="vault-status" role="status"></p>
    `;

    w.querySelectorAll('[data-view]').forEach(b => {
      b.onclick = () => {
        view = b.dataset.view;
        render();
      };
    });

    const body = $('#vault-body');

    // VIEW: 1. SOURCE LIBRARY (SPLIT PANE)
    if (view === 'library') {
      body.innerHTML = `
        <div class="vault-search-toolbar">
          <label>
            <span>Search All ${rows.length} Pages</span>
            <input id="q" type="search" placeholder="Recipe, ingredient, equipment, procedure, temperature…" value="${e(filters.q)}">
          </label>
          <label>
            <span>Station Manual</span>
            <select id="manual">
              <option value="">All 12 Manuals</option>
              ${data.manuals.map(m => `
                <option value="${m.id}" ${filters.manual === m.id ? 'selected' : ''}>${e(m.name)}</option>
              `).join('')}
            </select>
          </label>
          <label>
            <span>Filter By Content</span>
            <select id="kind">
              ${[
                ['all', 'Everything (All Pages)'],
                ['recipes', 'Pages with Ingredient Tables'],
                ['photos', 'Pages with Photo Scans']
              ].map(([v, t]) => `
                <option value="${v}" ${filters.kind === v ? 'selected' : ''}>${t}</option>
              `).join('')}
            </select>
          </label>
        </div>

        <div class="vault-grid">
          <aside class="vault-sidebar">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <p id="count" class="vault-results-count" role="status"></p>
              <div class="vault-toolbar" style="margin:0; gap:0.25rem;">
                <button id="previous-results" style="padding:0.35rem 0.6rem; font-size:0.75rem;">← Prev</button>
                <button id="next-results" style="padding:0.35rem 0.6rem; font-size:0.75rem;">Next →</button>
              </div>
            </div>
            <div id="results" class="vault-results"></div>
          </aside>
          
          <article class="vault-page" id="page">
            <div style="text-align:center; padding:4rem 1rem; color:var(--text-muted);">
              <span style="font-size:3rem; display:block; margin-bottom:1rem; opacity:0.4;">📖</span>
              <h2 style="font-family:var(--font-serif); font-size:1.8rem; color:#FFFFFF; margin-bottom:0.5rem;">Select a Page from the Library</h2>
              <p style="font-size:0.9rem; max-width:480px; margin:0 auto; line-height:1.6;">
                Choose any page on the left to inspect its formatted batch tables, original line scan photographs, and verbatim operating procedures.
              </p>
            </div>
          </article>
        </div>
      `;

      for (const [id, field] of [['q', 'q'], ['manual', 'manual'], ['kind', 'kind']]) {
        $('#' + id).oninput = ev => {
          filters[field] = ev.target.value;
          filters.page = 0;
          search();
        };
      }

      $('#previous-results').onclick = () => {
        filters.page--;
        search();
      };
      $('#next-results').onclick = () => {
        filters.page++;
        search();
      };

      search();
    }

    // VIEW: 2. INVENTORY OF ALL SUPPLIED FILES
    if (view === 'inventory') {
      const inventory = data.inventory || data.manuals.map(m => ({ ...m, manualId: m.id, pages: m.pages.length }));
      body.innerHTML = `
        <div style="margin-bottom:2rem;">
          <h2 style="font-family:var(--font-serif); font-size:2.2rem; color:#FFFFFF; margin-bottom:0.5rem;">Authentic Supplied Manuals</h2>
          <p style="color:var(--text-secondary); max-width:760px;">Complete cryptographic inventory of the 12 master operational files and aliases. Zero pages or procedures discarded.</p>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap:1.25rem;">
          ${inventory.map(m => `
            <article class="vault-page" style="display:flex; flex-direction:column; gap:0.75rem; border-top:3px solid var(--gold-primary);">
              <div style="display:flex; justify-content:space-between; align-items:start;">
                <span class="vault-manual-pill">${m.pages} PAGES</span>
                <span style="font-family:var(--font-mono); font-size:0.7rem; color:${m.duplicate ? 'var(--text-muted)' : 'var(--emerald)'};">
                  ${m.duplicate ? '🔗 Shared Master' : '✓ Verified Original'}
                </span>
              </div>
              <h3 style="font-family:var(--font-serif); font-size:1.35rem; color:#FFFFFF; margin:0;">${e(m.name)}</h3>
              <button class="vault-submit-btn" data-open="${e(m.manualId)}:1" style="font-size:0.8rem; padding:0.5rem 1rem; margin-top:auto;">
                Browse Page 1 of this Manual →
              </button>
              <details style="margin-top:0.5rem;">
                <summary>SHA-256 Cryptographic Hash</summary>
                <code style="display:block; padding:0.5rem; background:rgba(0,0,0,0.4); border-radius:4px; font-size:0.7rem; color:var(--text-muted); word-break:break-all;">${e(m.sha256)}</code>
              </details>
            </article>
          `).join('')}
        </div>
        <article class="vault-page" id="page" style="display:none;"></article>
      `;
      bindPages(body);
    }

    // VIEW: 3. TASTING MENU & 4. MISE EN PLACE
    if (view === 'menu' || view === 'mise') {
      const isMise = view === 'mise';
      body.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:2rem; flex-wrap:wrap; gap:1rem;">
          <div>
            <h2 style="font-family:var(--font-serif); font-size:2.2rem; color:#FFFFFF; margin-bottom:0.5rem;">
              ${isMise ? 'Mise en Place Station Checklist' : 'Your Selected Degustation Menu'}
            </h2>
            <p style="color:var(--text-secondary); max-width:760px; margin:0;">
              ${isMise ? 'Review each station requirement, equipment setup, and ingredient staging before service firing.' : 'Curated collection of source pages for tonight\'s dinner service.'}
            </p>
          </div>
          ${menu.length ? `
            <button type="button" id="btn-generate-brigade-sheet" class="vault-submit-btn" style="width:auto; padding:0.6rem 1.25rem; font-size:0.85rem;">
              🖨️ Brigade Service Sheet (${menu.length} Dishes)
            </button>
          ` : ''}
        </div>

        <div class="vault-grid">
          <aside class="vault-sidebar">
            <span class="vault-results-count">${menu.length} Bookmarked Pages in Session</span>
            <div class="vault-results">
              ${menu.map(id => {
                const p = rows.find(r => r.id === id);
                if (!p) return '';
                return `
                  <div style="background:rgba(18,18,26,0.65); border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:0.75rem;">
                    ${pageButton(p)}
                    ${isMise ? `
                      <label style="display:flex; align-items:center; gap:0.5rem; margin-top:0.5rem; font-size:0.8rem; color:var(--text-secondary); cursor:pointer;">
                        <input type="checkbox" data-check="${e(id)}" ${checks.has(id) ? 'checked' : ''}>
                        <span>SOP & Equipment Verified</span>
                      </label>
                    ` : ''}
                  </div>
                `;
              }).join('') || `
                <div style="text-align:center; padding:2rem 1rem; color:var(--text-muted);">
                  <p>Your session menu is currently empty.</p>
                  <p style="font-size:0.8rem;">Open any page in the Source Library and click <strong>"Add to Menu"</strong>.</p>
                </div>
              `}
            </div>
          </aside>

          <article class="vault-page" id="page">
            <div style="text-align:center; padding:3rem 1rem; color:var(--text-muted);">
              <p>Select any bookmarked menu page to inspect its full specs.</p>
            </div>
          </article>
        </div>
      `;
      bindPages(body);
      body.querySelectorAll('[data-check]').forEach(b => {
        b.onchange = () => {
          if (b.checked) checks.add(b.dataset.check);
          else checks.delete(b.dataset.check);
        };
      });
      const genBrigadeBtn = $('#btn-generate-brigade-sheet');
      if (genBrigadeBtn) genBrigadeBtn.onclick = openBrigadeSheet;
    }

    // VIEW: 5. PRIVATE PROVISIONS (SHOPPING) & 6. NOTEBOOK
    if (view === 'shopping' || view === 'notes') {
      const shop = view === 'shopping';
      body.innerHTML = `
        <div style="margin-bottom:2rem;">
          <h2 style="font-family:var(--font-serif); font-size:2.2rem; color:#FFFFFF; margin-bottom:0.5rem;">
            ${shop ? 'Private Provisions & Batch Shopping' : 'Chef\'s Private Service Notebook'}
          </h2>
          <p style="color:var(--text-secondary); max-width:760px;">
            ${shop ? 'Batches added from ingredient tables are recorded here with original restaurant units. Edit, append, or copy.' : 'Record table adjustments, timing notes, wine pairings, and technique observations.'}
          </p>
        </div>

        <div class="vault-page">
          ${shop ? `
            <label><input type="checkbox" id="allow-public-export"> Export outside the password-protected workspace. These items will stay in browser storage after locking.</label>
            <div class="vault-action-chips">
              <button type="button" class="btn-chip" id="btn-sync-public-provisions" disabled style="color:var(--gold-primary); border-color:rgba(212,175,55,0.4); background:rgba(212,175,55,0.1); font-weight:600;">
                🛒 Sync to Public Provisions
              </button>
              <button type="button" class="btn-chip" id="btn-format-provisions-check">
                ✓ Format as Checkbox List
              </button>
              <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-left:auto;">
                ${(shopping.match(/\n/g) || []).length} items recorded
              </span>
            </div>
          ` : `
            <div class="vault-action-chips">
              <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Quick Inserts:</span>
              <button type="button" class="btn-chip" id="btn-ins-date">+ Service Timestamp</button>
              <button type="button" class="btn-chip" id="btn-ins-yield">+ Yield Audit</button>
              <button type="button" class="btn-chip" id="btn-ins-pair">+ Sommelier Pairing</button>
              <button type="button" class="btn-chip" id="btn-ins-mise">+ Station Mise Setup</button>
            </div>
          `}
          <div class="vault-page-toolbar" style="margin-bottom:1rem;">
            <button id="btn-copy-vault-notes">📋 Copy to Clipboard</button>
            <button id="btn-clear-vault-notes" style="color:#ef4444;">🗑️ Clear</button>
            <span style="margin-left:auto; font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">
              EPHEMERAL SESSION MEMORY
            </span>
          </div>
          <textarea id="writing" style="width:100%; min-height:420px; padding:1.25rem; font-family:${shop ? 'var(--font-mono)' : 'var(--font-sans)'}; font-size:0.95rem; line-height:1.7; background:rgba(10,10,16,0.85); border:1px solid rgba(212,175,55,0.25); border-radius:var(--radius-md); color:#FFFFFF; resize:vertical;">${e(shop ? shopping : notes)}</textarea>
        </div>
      `;

      $('#writing').oninput = ev => {
        if (shop) shopping = ev.target.value;
        else notes = ev.target.value;
      };

      $('#btn-copy-vault-notes').onclick = () => {
        const val = $('#writing').value;
        navigator.clipboard.writeText(val).then(() => {
          notifyVault('Copied private notes to clipboard!');
        });
      };

      $('#btn-clear-vault-notes').onclick = () => {
        if (confirm('Clear current notes?')) {
          $('#writing').value = '';
          if (shop) shopping = '';
          else notes = '';
          notifyVault('Notes cleared.');
        }
      };

      if (shop) {
        const syncBtn = $('#btn-sync-public-provisions');
        if (syncBtn) {
          syncBtn.onclick = syncToPublicProvisions;
          $("#allow-public-export").onchange = ev => { syncBtn.disabled = !ev.target.checked; };
        }

        const checkBtn = $('#btn-format-provisions-check');
        if (checkBtn) {
          checkBtn.onclick = () => {
            const lines = shopping.split('\n');
            shopping = lines.map(l => {
              const trimmed = l.trim();
              if (!trimmed || trimmed.startsWith('/*') || trimmed.startsWith('[ ]') || trimmed.startsWith('[x]')) return l;
              return '[ ] ' + trimmed;
            }).join('\n');
            $('#writing').value = shopping;
            notifyVault('Formatted provisions as checkbox checklist.');
          };
        }
      } else {
        const insertSnippet = (snippet) => {
          const area = $('#writing');
          const pos = area.selectionStart || area.value.length;
          const before = area.value.substring(0, pos);
          const after = area.value.substring(pos);
          area.value = before + snippet + after;
          notes = area.value;
          area.focus();
          area.selectionStart = area.selectionEnd = pos + snippet.length;
          notifyVault('Snippet inserted.');
        };

        const insDate = $('#btn-ins-date');
        if (insDate) insDate.onclick = () => {
          const d = new Date().toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
          insertSnippet(`\n[SERVICE PASS · ${d}]\n`);
        };
        const insYield = $('#btn-ins-yield');
        if (insYield) insYield.onclick = () => insertSnippet(`\n* [YIELD AUDIT] Stated Yield: _____ | Actual Yield: _____ | Variance: _____\n`);
        const insPair = $('#btn-ins-pair');
        if (insPair) insPair.onclick = () => insertSnippet(`\n* [SOMMELIER PAIRING] Varietal: _____ | Producer: _____ | Vintage: _____\n`);
        const insMise = $('#btn-ins-mise');
        if (insMise) insMise.onclick = () => insertSnippet(`\n* [STATION MISE & EQUIPMENT] Pans: _____ | Temp: _____ | Pickup Timing: _____\n`);
      }
    }

    // VIEW: 7. VIDEO MASTERCLASSES
    if (view === 'videos') {
      const links = rows.flatMap(p => p.links.filter(youtube).map(url => ({ p, url })));
      body.innerHTML = `
        <div style="margin-bottom:2rem;">
          <h2 style="font-family:var(--font-serif); font-size:2.2rem; color:#FFFFFF; margin-bottom:0.5rem;">Authentic Line Training Videos</h2>
          <p style="color:var(--text-secondary); max-width:760px;">${links.length} video demonstrations referenced directly in the operational manuals.</p>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap:1.25rem;">
          ${links.map(({ p, url }) => `
            <article class="vault-page" style="display:flex; flex-direction:column; gap:0.75rem; border-top:3px solid var(--emerald);">
              <span class="vault-manual-pill">${e(p.manual)} · PAGE ${p.number}</span>
              <h3 style="font-family:var(--font-serif); font-size:1.25rem; color:#FFFFFF; margin:0;">${e(p.title)}</h3>
              <div style="display:flex; gap:0.5rem; margin-top:auto; flex-wrap:wrap;">
                <a href="${e(safe(url))}" target="_blank" rel="noopener noreferrer" class="vault-submit-btn" style="flex:1; text-decoration:none; font-size:0.8rem; padding:0.5rem; text-align:center;">
                  ▶ Watch Training Video ↗
                </a>
                <button class="btn-lock-vault" data-open="${e(p.id)}" style="color:var(--text-primary); border-color:var(--border-subtle); background:rgba(255,255,255,0.05); font-size:0.8rem;">
                  Read Page
                </button>
              </div>
            </article>
          `).join('')}
        </div>
        <article class="vault-page" id="page" style="display:none;"></article>
      `;
      bindPages(body);
    }

    // VIEW: 8. LEGACY PREP CARDS
    if (view === 'prep') {
      body.innerHTML = `
        <div style="margin-bottom:2rem;">
          <h2 style="font-family:var(--font-serif); font-size:2.2rem; color:#FFFFFF; margin-bottom:0.5rem;">Brigade Prep Transcriptions</h2>
          <p style="color:var(--text-secondary); max-width:760px;">Legacy operational summaries retained for quick glance reference.</p>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 360px), 1fr)); gap:1.25rem;">
          ${(data.prepCards || []).map(c => `
            <details class="vault-page" style="border-top:3px solid var(--gold-primary);">
              <summary style="font-family:var(--font-serif); font-size:1.2rem; color:#FFFFFF; cursor:pointer;">
                ${e(c.title)}
              </summary>
              <div style="margin-top:0.75rem; font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                <p><strong>Station:</strong> ${e(c.station)} · <strong>Category:</strong> ${e(c.category)}</p>
                <p><strong>Shelf Life:</strong> ${e(c.shelfLife)} · <strong>Prep Frequency:</strong> ${e(c.prepFrequency)}</p>
                <div style="background:rgba(239,68,68,0.1); border-left:3px solid #ef4444; padding:0.5rem; margin:0.5rem 0;">
                  <strong>HACCP:</strong> ${e(c.haccp)}
                </div>
                ${Object.entries(c.yields || {}).map(([batch, items]) => `
                  <h4 style="color:var(--gold-primary); margin-top:0.75rem; font-family:var(--font-mono);">${e(batch)}</h4>
                  <ul style="padding-left:1.25rem;">
                    ${items.map(i => `<li><strong>${e(i.qty)}</strong> ${e(i.name)}</li>`).join('')}
                  </ul>
                `).join('')}
                <h4 style="color:var(--gold-primary); margin-top:0.75rem; font-family:var(--font-mono);">Procedure</h4>
                <ol style="padding-left:1.25rem;">
                  ${(c.steps || []).map(s => `<li>${e(s)}</li>`).join('')}
                </ol>
                ${c.scienceNote ? `
                  <p style="background:rgba(16,185,129,0.08); border-left:3px solid var(--emerald); padding:0.5rem; margin-top:0.75rem;">
                    <strong>Science:</strong> ${e(c.scienceNote)}
                  </p>
                ` : ''}
              </div>
            </details>
          `).join('')}
        </div>
      `;
    }
  }

  // Filter Search
  function search() {
    const terms = filters.q.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const matches = rows.filter(p =>
      (!filters.manual || p.mid === filters.manual) &&
      (filters.kind !== 'recipes' || p.hasIngredientTable) &&
      (filters.kind !== 'photos' || p.imageCount > 0) &&
      terms.every(t => p.text.toLowerCase().includes(t))
    );

    const max = Math.max(0, Math.ceil(matches.length / PAGE_SIZE) - 1);
    filters.page = Math.max(0, Math.min(max, filters.page));
    const start = filters.page * PAGE_SIZE;

    const countEl = $('#count');
    if (countEl) {
      countEl.textContent = matches.length
        ? `${matches.length} matching pages · Showing ${start + 1}–${Math.min(start + PAGE_SIZE, matches.length)}`
        : 'No matching pages found.';
    }

    const resEl = $('#results');
    if (resEl) {
      resEl.innerHTML = matches.slice(start, start + PAGE_SIZE).map(pageButton).join('');
      bindPages(resEl);
    }

    const prevBtn = $('#previous-results');
    const nextBtn = $('#next-results');
    if (prevBtn) prevBtn.disabled = filters.page === 0;
    if (nextBtn) nextBtn.disabled = filters.page === max || matches.length === 0;
  }

  // Table Generator with Batch Column Selector & Dynamic Scaling
  function tableHTML(item, index) {
    const tableRows = item.rows;
    const width = Math.max(...tableRows.map(r => r.length));
    const head = tableRows[0] || [];
    const ingredient = head.findIndex(c => /ingredients?/i.test(c || ''));

    return `
      <section class="source-table" data-table-index="${index}" data-ingredient-col="${ingredient}">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.6rem; flex-wrap:wrap; gap:0.6rem;">
          ${ingredient >= 0 ? `<div class="vault-scaling-strip" data-scale-strip="${index}">
            <label>Yield Scale:</label>
            <button type="button" class="btn-vault-scale-pill active" data-scale-val="1">1x</button>
            <button type="button" class="btn-vault-scale-pill" data-scale-val="0.5">0.5x</button>
            <button type="button" class="btn-vault-scale-pill" data-scale-val="1.5">1.5x</button>
            <button type="button" class="btn-vault-scale-pill" data-scale-val="2">2x</button>
            <button type="button" class="btn-vault-scale-pill" data-scale-val="3">3x</button>
            <button type="button" class="btn-vault-scale-pill" data-scale-val="4">4x</button>
          </div>` : ''}
          <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted);">
            ✦ Click column header to trace batch
          </span>
        </div>
        <div class="table-scroll" tabindex="0" role="region" aria-label="Source table ${index + 1}">
          <table data-table-ref="${index}">
            <caption>Source Specification Table ${index + 1} · Quantities retained exactly as written</caption>
            <thead>
              <tr>
                ${Array.from({ length: width }, (_, i) => `<th scope="col" data-col-idx="${i}" title="Click to highlight batch column">${e(head[i] || '')}</th>`).join('')}
              </tr>
            </thead>
            <tbody>
              ${tableRows.slice(1).map(row => `
                <tr>
                  ${Array.from({ length: width }, (_, i) => {
                    const cellVal = row[i] || '';
                    return `<td data-col-idx="${i}" data-raw-val="${e(cellVal)}">${e(cellVal)}</td>`;
                  }).join('')}
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
        <div class="vault-table-controls">
          <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap;">
            <button class="btn-vault-copy-tsv" data-copy-table="${index}" style="font-family:var(--font-mono); font-size:0.72rem; padding:0.4rem 0.8rem; background:rgba(255,255,255,0.05); border:1px solid var(--border-subtle); border-radius:var(--radius-md); color:var(--text-secondary); cursor:pointer;">
              📋 Copy TSV (Excel / Sheets)
            </button>
            ${ingredient >= 0 ? `
              <div style="display:flex; align-items:center; gap:0.4rem;">
                <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Select Batch:</span>
                <select data-column="${index}">
                  ${head.map((h, i) => h && i !== ingredient && !/custom/i.test(h) ? `<option value="${i}">${e(h)}</option>` : '').join('')}
                </select>
              </div>
            ` : ''}
          </div>
          ${ingredient >= 0 ? `
            <button data-shop-table="${index}" data-ingredient="${ingredient}">
              🛒 Add Batch to Private Provisions
            </button>
          ` : ''}
        </div>
      </section>
    `;
  }

  // Open Page Reader
  async function openPage(id) {
    const p = rows.find(r => r.id === id);
    const el = $('#page');
    if (!p || !el) return;

    releaseImages();
    current = id;
    const ticket = readerVersion;
    const activeSession = session;

    // Highlight active card in left sidebar
    $$('.vault-page-card').forEach(c => {
      c.classList.toggle('active-page', c.dataset.open === id);
    });

    const previous = rows.find(r => r.mid === p.mid && r.number === p.number - 1);
    const next = rows.find(r => r.mid === p.mid && r.number === p.number + 1);
    const tables = (p.content || []).filter(c => c.kind === 'table');
    let ti = 0;

    const isBookmarked = menu.includes(id);

    el.innerHTML = `
      <div style="border-bottom:1px solid rgba(212,175,55,0.2); padding-bottom:1rem; margin-bottom:1.5rem;">
        <span class="vault-reader-kicker">${e(p.manual)} · PAGE ${p.number}</span>
        <h2 class="vault-reader-title" tabindex="-1">${e(p.title)}</h2>
        
        <div class="vault-page-toolbar">
          ${previous ? `<button data-open="${e(previous.id)}" data-prev-nav="true" title="Shortcut: [ or Alt+Left">← Prev Page (${previous.number}) <kbd style="font-size:0.65rem;opacity:0.6;background:rgba(0,0,0,0.4);padding:1px 4px;border-radius:3px;">[</kbd></button>` : ''}
          ${next ? `<button data-open="${e(next.id)}" data-next-nav="true" title="Shortcut: ] or Alt+Right">Next Page (${next.number}) → <kbd style="font-size:0.65rem;opacity:0.6;background:rgba(0,0,0,0.4);padding:1px 4px;border-radius:3px;">]</kbd></button>` : ''}
          <button id="add-page" style="${isBookmarked ? 'border-color:var(--emerald); color:var(--emerald); background:rgba(16,185,129,0.1);' : ''}">
            ${isBookmarked ? '✓ In Menu (Remove)' : '★ Add Page to Menu'}
          </button>
          <button id="pdf">📄 View Original PDF Scan</button>
        </div>
      </div>

      <!-- Exact High-Resolution Source Scan -->
      <details open class="source-original">
        <summary>Exact Source Scan · Original Line Photography & Layout</summary>
        <div id="page-image" role="status" style="padding:1.5rem; text-align:center; color:var(--text-muted);">
          <span style="display:inline-block; animation:vault-pulse 1.5s infinite;">⏳</span> Decrypting authenticated page scan…
        </div>
      </details>

      <!-- Extracted Formatted Recipe & Tables -->
      <div style="margin:2rem 0;">
        <h3 style="font-family:var(--font-serif); font-size:1.6rem; color:#FFFFFF; margin-bottom:0.4rem;">
          Structured Recipe & Operational Specs
        </h3>
        <p style="font-size:0.825rem; color:var(--text-muted); margin-bottom:1.25rem;">
          Formatted extraction from the source manual. Compare table alignment and quantities with the original scan; calculated batches are labeled separately.
        </p>
        
        <div class="source-content">
          ${(p.content || []).map(item => item.kind === 'table' ? tableHTML(item, ti++) : `<p style="font-size:0.95rem; line-height:1.7; color:var(--text-secondary); margin:1rem 0;">${e(item.text)}</p>`).join('') || `<pre>${e(p.text)}</pre>`}
        </div>
      </div>

      <!-- Verbatim OCR Text Accordion -->
      <details>
        <summary>Complete Verbatim Searchable Text</summary>
        <pre>${e(p.text)}</pre>
      </details>

      <!-- External References -->
      ${p.links && p.links.length ? `
        <div style="margin-top:1.5rem; padding-top:1rem; border-top:1px solid var(--border-subtle);">
          <h4 style="font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; color:var(--gold-primary); margin-bottom:0.5rem;">Links on this Page</h4>
          ${p.links.filter(safe).map(u => `
            <a href="${e(safe(u))}" target="_blank" rel="noopener noreferrer" style="color:var(--gold-primary); font-size:0.85rem; text-decoration:none; display:inline-block; margin-right:1rem; margin-bottom:0.5rem;">
              ↗ ${e(u)}
            </a>
          `).join('')}
        </div>
      ` : ''}

      <div id="pdf-view" style="margin-top:2rem;"></div>
    `;

    bindPages(el);

    // Add to Menu Toggle
    $('#add-page').onclick = () => {
      if (menu.includes(id)) {
        menu = menu.filter(x => x !== id);
        notifyVault(`Removed "${p.title}" from tasting menu.`);
      } else {
        menu = [...menu, id];
        notifyVault(`Added "${p.title}" to tasting menu! ★`);
      }
      const statMenu = $('#vault-stat-menu-count');
      if (statMenu) statMenu.textContent = menu.length;
      openPage(id);
    };

    // Column Highlighting on Table Header Click
    el.querySelectorAll('.source-table th[data-col-idx]').forEach(th => {
      th.onclick = () => {
        const table = th.closest('table');
        const colIdx = th.dataset.colIdx;
        const isActive = th.classList.contains('active-table-column');
        table.querySelectorAll('.active-table-column').forEach(cell => cell.classList.remove('active-table-column'));
        if (!isActive) {
          th.classList.add('active-table-column');
          table.querySelectorAll(`td[data-col-idx="${colIdx}"]`).forEach(td => td.classList.add('active-table-column'));
        }
      };
    });

    // Dynamic Batch Scaling Pills
    el.querySelectorAll('.btn-vault-scale-pill').forEach(btn => {
      btn.onclick = () => {
        const strip = btn.closest('.vault-scaling-strip');
        const tableSec = btn.closest('.source-table');
        const table = tableSec.querySelector('table');
        const factor = parseFloat(btn.dataset.scaleVal) || 1;
        tableSec.dataset.factor = factor;
        tableSec.querySelectorAll("[data-shop-table]").forEach(b => { b.disabled = false; b.textContent = "Add Batch to Private Provisions"; });
        const ingCol = parseInt(tableSec.dataset.ingredientCol, 10);

        strip.querySelectorAll('.btn-vault-scale-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        table.querySelectorAll('tbody td').forEach(td => {
          const colIdx = parseInt(td.dataset.colIdx, 10);
          const raw = td.dataset.rawVal;
          if (colIdx === ingCol || !raw) return;
          if (factor === 1) {
            td.innerHTML = e(raw);
          } else {
            const scaled = scaleNumberString(raw, factor);
            if (scaled === null) {
              td.innerHTML = `${e(raw)} <strong class="vault-scaled-badge">Not scaled — review manually</strong>`;
            } else if (scaled !== raw) {
              td.innerHTML = `${e(scaled)} <span class="vault-scaled-badge">${factor}x</span>`;
            } else {
              td.innerHTML = e(raw);
            }
          }
        });
        table.querySelector("caption").textContent = `Calculated batch × ${factor}. Original quantities remain in the source scan. Flagged entries need manual scaling.`;
        notifyVault(`Batch factor ${factor}x selected. Review any entries marked not scaled.`);
      };
    });

    // TSV Table Copy Listener
    el.querySelectorAll('[data-copy-table]').forEach(b => {
      b.onclick = () => {
        const idx = Number(b.dataset.copyTable);
        const t = tables[idx].rows;
        const section = b.closest('.source-table');
        const factor = Number(section.dataset.factor || 1);
        const ingredient = Number(section.dataset.ingredientCol);
        const tsv = `Calculated batch factor: ${factor}x (column headings identify original source batches)\n` + t.map((row, n) => row.map((cell, col) => {
          if (!n || col === ingredient || !cell || ingredient < 0) return cell || '';
          return scaleNumberString(cell, factor) ?? ('NOT SCALED: '+cell);
        }).join('\t')).join('\n');
        navigator.clipboard.writeText(tsv).then(() => {
          notifyVault('Table data copied to clipboard as TSV for spreadsheet paste!');
          const orig = b.textContent;
          b.textContent = '✓ Copied TSV!';
          b.style.borderColor = 'var(--emerald)';
          b.style.color = 'var(--emerald)';
          setTimeout(() => {
            b.textContent = orig;
            b.style.borderColor = '';
            b.style.color = '';
          }, 2500);
        }).catch(() => {
          notifyVault('Could not copy table to clipboard.', false);
        });
      };
    });

    // Table Batch Add Listeners
    el.querySelectorAll('[data-shop-table]').forEach(b => {
      b.onclick = () => {
        const i = Number(b.dataset.shopTable);
        const col = Number(el.querySelector(`[data-column="${i}"]`).value);
        const ing = Number(b.dataset.ingredient);
        const t = tables[i].rows;
        const factor = Number(b.closest('.source-table').dataset.factor || 1);
        const lines = t.slice(1).filter(row => row[col] && row[ing]).map(row => {
          const value = scaleNumberString(row[col], factor);
          return `${value === null ? 'MANUAL SCALING REQUIRED: '+row[col] : value} — ${row[ing]}`;
        });
        
        if (!lines.length) {
          notifyVault('No paired quantity and ingredient cells found.', false);
          return;
        }

        shopping += `\n/* ${p.title} · ${p.manual} p.${p.number} · ${t[0][col]} × ${factor} */\n${lines.join('\n')}\n`;
        notifyVault(`Added ${lines.length} items from ${p.title} (${t[0][col]}) to Private Provisions!`);
        b.textContent = '✓ Batch Added to Provisions';
        b.style.borderColor = 'var(--emerald)';
        b.style.color = 'var(--emerald)';
        b.disabled = true;
      };
    });

    el.querySelectorAll('[data-column]').forEach(select => {
      select.onchange = () => {
        const button=el.querySelector(`[data-shop-table="${select.dataset.column}"]`);
        if(button){button.disabled=false;button.textContent='Add Batch to Private Provisions';}
      };
    });

    // PDF Viewer Launch
    $('#pdf').onclick = async () => {
      const b = $('#pdf');
      b.disabled = true;
      b.textContent = '⏳ Decrypting PDF…';
      try {
        const bytes = await decrypt(p.mid + '.bin');
        if (ticket !== readerVersion || activeSession !== session) return;
        const url = URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' }));
        urls.push(url);
        $('#pdf-view').innerHTML = `
          <div style="background:rgba(0,0,0,0.5); border:1px solid var(--border-subtle); border-radius:var(--radius-lg); padding:1rem; margin-top:1.5rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
              <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-primary);">AUTHENTIC MANUAL PDF</span>
              <a href="${url}#page=${p.number}" target="_blank" rel="noopener" style="font-size:0.8rem; color:var(--gold-primary); text-decoration:none;">
                Open in Full Tab ↗
              </a>
            </div>
            <iframe title="Original manual PDF" src="${url}#page=${p.number}" style="width:100%; height:75vh; border:0; border-radius:var(--radius-md);"></iframe>
          </div>
        `;
        b.textContent = '✓ PDF Loaded Below';
      } catch (err) {
        if (ticket === readerVersion) {
          b.textContent = 'Could not load PDF. Retry';
          notifyVault('Failed to decrypt original PDF.', false);
        }
      } finally {
        if (ticket === readerVersion) b.disabled = false;
      }
    };

    el.querySelector('h2').focus({ preventScroll: true });

    if (view !== 'library' || matchMedia('(max-width:900px)').matches) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    if (!p.preview) {
      $('#page-image').textContent = 'Use "View Original PDF Scan" to view this page in high resolution.';
      return;
    }

    try {
      const bytes = await decrypt(p.preview);
      if (ticket !== readerVersion || activeSession !== session) return;
      const url = URL.createObjectURL(new Blob([bytes], { type: 'image/webp' }));
      urls.push(url);
      $('#page-image').innerHTML = `
        <div class="vault-scan-container">
          <img src="${url}" alt="Original page ${p.number}: ${e(p.title)}" width="${p.width * 1.5}" height="${p.height * 1.5}" class="vault-scan-img" id="scan-img-${p.number}">
          <div class="vault-scan-actions">
            <button type="button" class="btn-scan-action btn-scan-zoom" id="btn-enlarge-lightbox">
              🔍 Inspect High-Res Lightbox
            </button>
            <a href="${url}" target="_blank" rel="noopener" class="btn-scan-action">
              ↗ Open Raw in New Tab
            </a>
          </div>
        </div>
        <p style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-top:0.6rem; text-align:center;">
          ✦ Authentic Restaurant Scan · Click to inspect fine print & station diagrams
        </p>
      `;

      const triggerLightbox = () => openLightbox(url, p.title, `${p.manual} · Page ${p.number}`);
      const scanImg = $('#scan-img-' + p.number);
      if (scanImg) scanImg.onclick = triggerLightbox;
      const enlargeBtn = $('#btn-enlarge-lightbox');
      if (enlargeBtn) enlargeBtn.onclick = triggerLightbox;
    } catch {
      if (ticket === readerVersion) {
        $('#page-image').textContent = 'Preview scan unavailable. Use "View Original PDF Scan" above.';
      }
    }
  }

  // Lightbox Viewport & Controls Setup
  const lbViewport = $('#vault-lightbox-viewport');
  if (lbViewport) {
    lbViewport.onmousedown = ev => {
      if (ev.button !== 0) return;
      isPanning = true;
      panStart = { x: ev.clientX - panOffset.x, y: ev.clientY - panOffset.y };
    };
    window.addEventListener('mousemove', ev => {
      if (!isPanning) return;
      panOffset = { x: ev.clientX - panStart.x, y: ev.clientY - panStart.y };
      updateLightboxTransform();
    });
    window.addEventListener('mouseup', () => { isPanning = false; });
    lbViewport.onwheel = ev => {
      ev.preventDefault();
      const delta = ev.deltaY < 0 ? 0.2 : -0.2;
      lightboxZoom = Math.max(0.5, Math.min(5, lightboxZoom + delta));
      updateLightboxTransform();
    };
  }

  const zoomInBtn = $('#vault-zoom-in');
  if (zoomInBtn) zoomInBtn.onclick = () => { lightboxZoom = Math.min(5, lightboxZoom + 0.25); updateLightboxTransform(); };
  const zoomOutBtn = $('#vault-zoom-out');
  if (zoomOutBtn) zoomOutBtn.onclick = () => { lightboxZoom = Math.max(0.5, lightboxZoom - 0.25); updateLightboxTransform(); };
  const zoomResetBtn = $('#vault-zoom-reset');
  if (zoomResetBtn) zoomResetBtn.onclick = () => { lightboxZoom = 1; panOffset = { x: 0, y: 0 }; updateLightboxTransform(); };
  const lbCloseBtn = $('#vault-lightbox-close');
  if (lbCloseBtn) lbCloseBtn.onclick = closeLightbox;
  const lbBackdrop = $('#vault-lightbox');
  if (lbBackdrop) lbBackdrop.onclick = ev => { if (ev.target.id === 'vault-lightbox') closeLightbox(); };

  // Shortcuts Modal Setup
  const shortcutsModal = $('#vault-shortcuts-modal');
  const openShortcutsBtn = $('#btn-vault-shortcuts');
  const closeShortcutsBtn = $('#vault-shortcuts-close');
  const gotitShortcutsBtn = $('#vault-shortcuts-gotit');
  const toggleShortcuts = () => {
    if (!shortcutsModal) return;
    shortcutsModal.hidden = !shortcutsModal.hidden;
  };
  if (openShortcutsBtn) openShortcutsBtn.onclick = toggleShortcuts;
  if (closeShortcutsBtn) closeShortcutsBtn.onclick = () => { shortcutsModal.hidden = true; };
  if (gotitShortcutsBtn) gotitShortcutsBtn.onclick = () => { shortcutsModal.hidden = true; };
  if (shortcutsModal) shortcutsModal.onclick = ev => { if (ev.target.id === 'vault-shortcuts-modal') shortcutsModal.hidden = true; };

  // Brigade Sheet Modal Setup
  const sheetModal = $('#vault-brigade-sheet-modal');
  const closeSheetBtn = $('#vault-sheet-close');
  if (closeSheetBtn) closeSheetBtn.onclick = () => { sheetModal.hidden = true; };
  if (sheetModal) sheetModal.onclick = ev => { if (ev.target.id === 'vault-brigade-sheet-modal') sheetModal.hidden = true; };
  const printSheetBtn = $('#btn-print-brigade-sheet');
  if (printSheetBtn) printSheetBtn.onclick = () => window.print();
  const copyBriefBtn = $('#btn-copy-brigade-brief');
  if (copyBriefBtn) {
    copyBriefBtn.onclick = () => {
      const bookmarked = menu.map(id => rows.find(r => r.id === id)).filter(Boolean);
      const text = `L'ATELIER SALON PRIVÉ · BRIGADE SERVICE BRIEF\n` +
        `Date: ${new Date().toLocaleDateString()}\n` +
        `Total Dishes: ${bookmarked.length}\n\n` +
        bookmarked.map((p, i) => `${i + 1}. ${p.title} (${p.manual} p.${p.number})`).join('\n');
      navigator.clipboard.writeText(text).then(() => notifyVault('Copied brigade service brief to clipboard!'));
    };
  }

  // Global Keyboard Shortcuts for Salon Privé
  document.addEventListener('keydown', (ev) => {
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
      if (ev.key === 'Escape') document.activeElement.blur();
      return;
    }

    if (ev.key === 'Escape') {
      if (shortcutsModal && !shortcutsModal.hidden) { shortcutsModal.hidden = true; return; }
      if (sheetModal && !sheetModal.hidden) { sheetModal.hidden = true; return; }
      if (lbBackdrop && !lbBackdrop.hidden) { closeLightbox(); return; }
    }

    if (ev.key === '?') {
      ev.preventDefault();
      toggleShortcuts();
      return;
    }

    const ws = $('#workspace');
    if (!ws || ws.hidden) return;

    if (ev.key === '/' && !ev.ctrlKey && !ev.metaKey) {
      const qInput = $('#q');
      if (qInput) {
        ev.preventDefault();
        qInput.focus();
        qInput.select();
      }
    } else if (ev.key === '[' || (ev.key === 'ArrowLeft' && ev.altKey)) {
      const prevBtn = document.querySelector('[data-prev-nav="true"]');
      if (prevBtn) {
        ev.preventDefault();
        prevBtn.click();
      }
    } else if (ev.key === ']' || (ev.key === 'ArrowRight' && ev.altKey)) {
      const nextBtn = document.querySelector('[data-next-nav="true"]');
      if (nextBtn) {
        ev.preventDefault();
        nextBtn.click();
      }
    } else if (ev.altKey && (ev.key === 'm' || ev.key === 'M')) {
      const addPageBtn = $('#add-page');
      if (addPageBtn) {
        ev.preventDefault();
        addPageBtn.click();
      }
    } else if (ev.altKey && (ev.key === 'p' || ev.key === 'P')) {
      const pdfBtn = $('#pdf');
      if (pdfBtn) {
        ev.preventDefault();
        pdfBtn.click();
      }
    } else if (ev.altKey && (ev.key === 't' || ev.key === 'T')) {
      const tsvBtn = document.querySelector('.btn-vault-copy-tsv');
      if (tsvBtn) {
        ev.preventDefault();
        tsvBtn.click();
      }
    }
  });
})();
