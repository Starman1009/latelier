/* Private source collection. Decrypted pages, selections and notes stay in memory. */
(() => {
'use strict';
const $ = (s, root=document) => root.querySelector(s);
const e = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const safe = u => { try { const x=new URL(u); return ['https:','http:'].includes(x.protocol)?x.href:''; } catch { return ''; } };
const youtube = u => { try { return ['youtube.com','www.youtube.com','m.youtube.com','youtu.be'].includes(new URL(u).hostname); } catch { return false; } };
let key, data, rows=[], menu=[], checks=new Set(), notes='', shopping='', urls=[], view='library', current=null, session=0, readerVersion=0;
let filters={q:'',manual:'',kind:'all',page:0};
const PAGE_SIZE=40;
async function decrypt(file, activeKey=key) {
 const res=await fetch('private-vault/'+file,{cache:'no-store'}); if(!res.ok) throw Error('Unavailable encrypted file');
 const bytes=new Uint8Array(await res.arrayBuffer());
 return crypto.subtle.decrypt({name:'AES-GCM',iv:bytes.slice(0,12),additionalData:new TextEncoder().encode('latelier-vault-v1')},activeKey,bytes.slice(12));
}
$('#unlock').onsubmit=async event => {
 event.preventDefault(); const ticket=++session, button=$('#unlock button'); button.disabled=true; $('#message').textContent='Unlocking collection…';
 try {
  const config=await (await fetch('private-vault/config.json',{cache:'no-store'})).json();
  const material=await crypto.subtle.importKey('raw',new TextEncoder().encode($('#password').value),'PBKDF2',false,['deriveKey']);
  const derived=await crypto.subtle.deriveKey({name:'PBKDF2',salt:Uint8Array.from(atob(config.salt),c=>c.charCodeAt(0)),iterations:config.iterations,hash:'SHA-256'},material,{name:'AES-GCM',length:256},false,['decrypt']);
  const decoded=JSON.parse(new TextDecoder().decode(await decrypt('index.bin',derived)));
  if(ticket!==session)return;
  key=derived;data=decoded;rows=data.manuals.flatMap(m=>m.pages.map(p=>({...p,manual:m.name,mid:m.id,id:m.id+':'+p.number})));
  $('#password').value='';$('#login').hidden=true;$('#workspace').hidden=false;$('#lock').hidden=false;render();
 } catch { if(ticket===session){key=null;$('#message').textContent='Could not unlock. Check the password and connection.';} }
 finally {button.disabled=false;}
};
function releaseImages(){urls.forEach(URL.revokeObjectURL);urls=[];readerVersion++;}
function lock(){session++;releaseImages();key=null;data=null;rows=[];menu=[];checks.clear();notes='';shopping='';current=null;filters={q:'',manual:'',kind:'all',page:0};view='library';$('#workspace').replaceChildren();$('#workspace').hidden=true;$('#login').hidden=false;$('#lock').hidden=true;$('#password').value='';$('#message').textContent='Locked. Decrypted pages and session notes cleared.';$('#password').focus();}
$('#lock').onclick=lock;window.addEventListener('pagehide',lock);
function pageButton(p){return `<button data-open="${e(p.id)}"><strong>${e(p.title)}</strong><span class="vault-meta">${e(p.manual)} · page ${p.number}${p.hasIngredientTable?' · Ingredient table':''}</span></button>`;}
function bindPages(root=document){root.querySelectorAll('[data-open]').forEach(b=>b.onclick=()=>openPage(b.dataset.open));}
function render(){
 releaseImages();current=null;
 const w=$('#workspace');
 w.innerHTML=`<p class="vault-kicker">YOUR PRIVATE SOURCE COLLECTION</p><h1>The complete kitchen library.</h1><div class="vault-stats"><span><strong>${data.inventory?.length || data.manuals.length+data.aliases.length}</strong> supplied files</span><span><strong>${rows.length}</strong> complete pages</span><span><strong>${data.manuals.length}</strong> unique manuals</span></div><p class="vault-meta">Original quantities, batch columns, photographs and procedures. Formatted text is extracted from the PDFs; compare the source page before cooking. Notes and selections clear when you lock or close.</p><nav class="vault-toolbar" aria-label="Private workspace">${[['library','Source library'],['inventory','All files'],['menu','Menu'],['mise','Mise en place'],['shopping','Shopping'],['notes','Notebook'],['videos','Source videos'],['prep','Legacy prep cards']].map(([v,label])=>`<button data-view="${v}" aria-pressed="${view===v}">${label}</button>`).join('')}</nav><div id="vault-body"></div><p id="vault-status" role="status"></p>`;
 w.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>{view=b.dataset.view;render();});
 const body=$('#vault-body');
 if(view==='library'){
  body.innerHTML=`<div class="vault-toolbar"><label>Search all pages<input id="q" type="search" placeholder="Recipe, ingredient, equipment, procedure…" value="${e(filters.q)}"></label><label>Manual<select id="manual"><option value="">All manuals</option>${data.manuals.map(m=>`<option value="${m.id}" ${filters.manual===m.id?'selected':''}>${e(m.name)}</option>`).join('')}</select></label><label>Show<select id="kind">${[['all','Everything'],['recipes','Pages with ingredient tables'],['photos','Pages containing images']].map(([v,t])=>`<option value="${v}" ${filters.kind===v?'selected':''}>${t}</option>`).join('')}</select></label></div><div class="vault-grid"><aside><p id="count" role="status"></p><div id="results" class="vault-results"></div><div class="vault-toolbar"><button id="previous-results">Previous results</button><button id="next-results">Next results</button></div></aside><article class="vault-page" id="page"><h2>Every page, in context.</h2><p>Select a page to read its formatted tables and procedures alongside the exact source image. Adjacent pages remain one click away.</p></article></div>`;
  for(const [id,field] of [['q','q'],['manual','manual'],['kind','kind']])$('#'+id).oninput=ev=>{filters[field]=ev.target.value;filters.page=0;search();};
  $('#previous-results').onclick=()=>{filters.page--;search();};$('#next-results').onclick=()=>{filters.page++;search();};search();
 }
 if(view==='inventory'){
  const inventory=data.inventory||data.manuals.map(m=>({...m,manualId:m.id,pages:m.pages.length}));
  body.innerHTML=`<h2>Every supplied file</h2><p>Identical copies share the same original document. No pages are discarded.</p><div class="vault-inventory">${inventory.map(m=>`<article class="vault-page"><h3>${e(m.name)}</h3><p>${m.pages} pages · ${m.duplicate?'Identical duplicate — linked to the original':'Original preserved'}</p><button data-open="${e(m.manualId)}:1">Browse this manual</button><details><summary>File integrity</summary><code>${e(m.sha256)}</code></details></article>`).join('')}</div><article class="vault-page" id="page"></article>`;bindPages(body);
 }
 if(view==='menu'||view==='mise'){
  body.innerHTML=`<h2>${view==='menu'?'Your source-page menu':'Mise en place checklist'}</h2><p>Add the required pages from the source library, including continuation pages. Quantities and timing remain those stated in the source.</p><div class="vault-results">${menu.map(id=>{const p=rows.find(r=>r.id===id);return `<div>${pageButton(p)}${view==='mise'?`<label><input type="checkbox" data-check="${e(id)}" ${checks.has(id)?'checked':''}> Ingredients, equipment and procedure reviewed</label>`:''}</div>`;}).join('')||'<p>Your menu is empty. Add a source page from the library.</p>'}</div><article id="page" class="vault-page"></article>`;bindPages(body);body.querySelectorAll('[data-check]').forEach(b=>b.onchange=()=>b.checked?checks.add(b.dataset.check):checks.delete(b.dataset.check));
 }
 if(view==='shopping'||view==='notes'){
  const shop=view==='shopping';body.innerHTML=`<h2>${shop?'Private shopping notes':'Private kitchen notebook'}</h2><p>${shop?'Choose a stated batch column from a source ingredient table, or enter your own list. Different units are kept as written.':'Record service plans, source pages and observations.'}</p><label>${shop?'Ingredients to buy':'Notes'}<textarea id="writing">${e(shop?shopping:notes)}</textarea></label>`;
  $('#writing').oninput=ev=>{if(shop)shopping=ev.target.value;else notes=ev.target.value;};
 }
 if(view==='videos'){
  const links=rows.flatMap(p=>p.links.filter(youtube).map(url=>({p,url})));
  body.innerHTML=`<h2>Videos linked in your manuals</h2><p>${links.length} source references. External video availability is controlled by YouTube.</p><div class="vault-inventory">${links.map(({p,url})=>`<article class="vault-page"><h3>${e(p.title)}</h3><p>${e(p.manual)} · page ${p.number}</p><a href="${e(safe(url))}" target="_blank" rel="noopener noreferrer">Watch source video ↗</a><button data-open="${e(p.id)}">Read source page</button></article>`).join('')}</div><article id="page" class="vault-page"></article>`;bindPages(body);
 }
 if(view==='prep'){
  body.innerHTML=`<h2>Legacy prep transcriptions</h2><p>These earlier summaries are retained for reference. Use the complete source library for the actual specifications.</p><div class="vault-inventory">${(data.prepCards||[]).map(c=>`<details class="vault-page"><summary>${e(c.title)}</summary><p>${e(c.station)} · ${e(c.category)}</p><p>Needs source review · ${e(c.prepFrequency)} · ${e(c.shelfLife)}</p><p>${e(c.haccp)}</p>${Object.entries(c.yields||{}).map(([batch,items])=>`<h4>${e(batch)}</h4><ul>${items.map(i=>`<li>${e(i.qty)} ${e(i.name)}</li>`).join('')}</ul>`).join('')}<ol>${(c.steps||[]).map(s=>`<li>${e(s)}</li>`).join('')}</ol><p>${e(c.scienceNote)}</p></details>`).join('')}</div>`;
 }
}
function search(){
 const terms=filters.q.toLowerCase().trim().split(/\s+/);
 const matches=rows.filter(p=>(!filters.manual||p.mid===filters.manual)&&(filters.kind!=='recipes'||p.hasIngredientTable)&&(filters.kind!=='photos'||p.imageCount>0)&&terms.every(t=>p.text.toLowerCase().includes(t)));
 const max=Math.max(0,Math.ceil(matches.length/PAGE_SIZE)-1);filters.page=Math.max(0,Math.min(max,filters.page));
 const start=filters.page*PAGE_SIZE;
 $('#count').textContent=matches.length?`${matches.length} matching pages · ${start+1}–${Math.min(start+PAGE_SIZE,matches.length)}`:'No matching pages. Try another term or choose Everything.';
 $('#results').innerHTML=matches.slice(start,start+PAGE_SIZE).map(pageButton).join('');
 $('#previous-results').disabled=filters.page===0;$('#next-results').disabled=filters.page===max;bindPages($('#results'));
}
function tableHTML(item,index){
 const rows=item.rows,width=Math.max(...rows.map(r=>r.length)),head=rows[0]||[];
 const ingredient=head.findIndex(c=>/ingredients?/i.test(c||''));
 return `<section class="source-table"><div class="table-scroll" tabindex="0" role="region" aria-label="Source table ${index+1}"><table><caption>Source table ${index+1} · quantities retained as written</caption><thead><tr>${Array.from({length:width},(_,i)=>`<th scope="col">${e(head[i]||'')}</th>`).join('')}</tr></thead><tbody>${rows.slice(1).map(row=>`<tr>${Array.from({length:width},(_,i)=>`<td>${e(row[i]||'')}</td>`).join('')}</tr>`).join('')}</tbody></table></div>${ingredient>=0?`<div class="vault-toolbar"><label>Stated batch<select data-column="${index}">${head.map((h,i)=>h&&i!==ingredient&&!/custom/i.test(h)?`<option value="${i}">${e(h)}</option>`:'').join('')}</select></label><button data-shop-table="${index}" data-ingredient="${ingredient}">Add this batch to private shopping</button></div>`:''}</section>`;
}
async function openPage(id){
 const p=rows.find(p=>p.id===id),el=$('#page');if(!p||!el)return;
 releaseImages();current=id;const ticket=readerVersion,activeSession=session;
 const previous=rows.find(r=>r.mid===p.mid&&r.number===p.number-1),next=rows.find(r=>r.mid===p.mid&&r.number===p.number+1);
 const tables=(p.content||[]).filter(c=>c.kind==='table');let ti=0;
 el.innerHTML=`<p class="vault-kicker">${e(p.manual)} · PAGE ${p.number}</p><h2 tabindex="-1">${e(p.title)}</h2><div class="vault-toolbar">${previous?`<button data-open="${e(previous.id)}">← Previous page</button>`:''}${next?`<button data-open="${e(next.id)}">Next page →</button>`:''}<button id="add-page">${menu.includes(id)?'Remove from menu':'Add page to menu'}</button><button id="pdf">Open original PDF</button></div><details open class="source-original"><summary>Exact source page · original photos and layout</summary><div id="page-image" role="status">Loading encrypted page image…</div></details><h3>Formatted source text</h3><p class="vault-meta">Automatically extracted. Merged cells and reading order may need comparison with the original page above. No ingredients or instructions have been inferred.</p><div class="source-content">${(p.content||[]).map(item=>item.kind==='table'?tableHTML(item,ti++):`<p class="source-paragraph">${e(item.text)}</p>`).join('')||`<pre>${e(p.text)}</pre>`}</div><details><summary>Complete searchable text</summary><pre>${e(p.text)}</pre></details><h3>Links on this page</h3>${p.links.filter(safe).map(u=>`<a href="${e(safe(u))}" target="_blank" rel="noopener noreferrer">${e(u)}</a>`).join('<br>')||'<p>No embedded links.</p>'}<div id="pdf-view"></div>`;
 bindPages(el);$('#add-page').onclick=()=>{menu=menu.includes(id)?menu.filter(x=>x!==id):[...menu,id];$('#add-page').textContent=menu.includes(id)?'Remove from menu':'Add page to menu';};
 el.querySelectorAll('[data-shop-table]').forEach(b=>b.onclick=()=>{
  const i=Number(b.dataset.shopTable),col=Number(el.querySelector(`[data-column="${i}"]`).value),ing=Number(b.dataset.ingredient),t=tables[i].rows;
  const lines=t.slice(1).filter(row=>row[col]&&row[ing]).map(row=>`${row[col]} — ${row[ing]}`);
  if(!lines.length){$('#vault-status').textContent='No paired quantity and ingredient cells found. Use the original table.';return;}
  shopping+=`\n${p.title} · ${p.manual} p.${p.number} · ${t[0][col]}\n${lines.join('\n')}\n`;
  $('#vault-status').textContent=`Added ${lines.length} lines to private shopping notes.`;b.textContent='Batch added';b.disabled=true;
 });
 $('#pdf').onclick=async()=>{const b=$('#pdf');b.disabled=true;try{const bytes=await decrypt(p.mid+'.bin');if(ticket!==readerVersion||activeSession!==session)return;const url=URL.createObjectURL(new Blob([bytes],{type:'application/pdf'}));urls.push(url);$('#pdf-view').innerHTML=`<a href="${url}#page=${p.number}" target="_blank" rel="noopener">Open PDF at page ${p.number} ↗</a><iframe title="Original manual PDF" src="${url}#page=${p.number}"></iframe>`;}catch{if(ticket===readerVersion)b.textContent='Could not load. Retry';}finally{if(ticket===readerVersion)b.disabled=false;}};
 el.querySelector('h2').focus({preventScroll:true});
 if(view!=='library'||matchMedia('(max-width:700px)').matches)el.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth',block:'start'});
 if(!p.preview){$('#page-image').textContent='Use Open original PDF to view this page.';return;}
 try{const bytes=await decrypt(p.preview);if(ticket!==readerVersion||activeSession!==session)return;const url=URL.createObjectURL(new Blob([bytes],{type:'image/webp'}));urls.push(url);$('#page-image').innerHTML=`<a href="${url}" target="_blank" rel="noopener" aria-label="Enlarge original page ${p.number}"><img src="${url}" alt="Original page ${p.number}: ${e(p.title)}. Full text follows below." width="${p.width*1.5}" height="${p.height*1.5}"></a><p class="vault-meta">Select the image to enlarge. Open the PDF for full-resolution detail.</p>`;}catch{if(ticket===readerVersion)$('#page-image').textContent='Preview unavailable. Open the original PDF instead.';}
}
})();
