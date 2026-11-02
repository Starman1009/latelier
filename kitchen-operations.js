/* Buildless kitchen tools. No recipe quantities or yield percentages are inferred. */
(()=>{'use strict';
const stations = [
 ['Sauté','Pans · induction or range','Arrange pans and utensils within reach; group your selected recipe’s finishing ingredients.'],
 ['Grill','Grates · tongs · resting area','Separate raw and cooked food tools and reserve a clean landing area.'],
 ['Fry','Fryer · basket · draining rack','Keep wet preparation away from hot oil and provide an unobstructed draining area.'],
 ['Garde Manger','Cold preparation · assembly','Keep cold ingredients organized and separate ready-to-eat preparation from raw proteins.'],
 ['Pastry','Scales · mixer · finishing bench','Arrange weighed ingredients in recipe order and keep the finishing bench clear.']
];
function yieldCalculation(amount, percent, mode) {
 if(!Number.isFinite(amount)||amount<=0||!Number.isFinite(percent)||percent<=0||percent>100) return null;
 const ap=mode==='ep'?amount/(percent/100):amount, ep=ap*percent/100;
 return {ap,ep,loss:ap-ep};
}
function voiceCommand(text) {
 const t=text.toLowerCase().trim().replace(/[.!?]+$/g,'').replace(/-/g,' ');
 if(/^(next|next step)$/.test(t))return {type:'next'};
 if(/^(previous|previous step|go back|back)$/.test(t))return {type:'previous'};
 if(/^(repeat|repeat step|read|read step)$/.test(t))return {type:'repeat'};
 const m=t.match(/^start (?:a )?(\d+(?:\.\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|fifteen|twenty|thirty|sixty) minute(?:s)? timer$/);
 if(m){const words={one:1,two:2,three:3,four:4,five:5,six:6,seven:7,eight:8,nine:9,ten:10,fifteen:15,twenty:20,thirty:30,sixty:60}; const minutes=words[m[1]]||Number(m[1]);if(minutes>0&&minutes<=1440)return {type:'timer',minutes};}
 return null;
}
function render(container){
 container.innerHTML=`<section class="ops-intro"><span class="card-badge">KITCHEN OPERATIONS</span><h1>Set your station. Plan your yield.</h1><p>A practical layout for your kitchen, with quantities calculated from your own measured yield.</p><a class="btn-secondary" href="vault.html">Unlock private manuals & prep cards →</a></section>
 <section class="bento-card"><h2>Station line map</h2><p>Select a station to plan its work area. This is a conceptual map, not a specification for your kitchen.</p><div class="station-map" role="group" aria-label="Kitchen stations">${stations.map((s,i)=>`<button class="btn-secondary" data-station="${i}" aria-pressed="${i===0}"><span>0${i+1}</span>${s[0]}</button>`).join('')}</div><article id="station-detail" aria-live="polite"></article></section>
 <section class="bento-card yield-panel"><h2>Buy what you actually need</h2><p>AP is as-purchased weight. EP is edible weight after trimming. Enter a measured yield; no ingredient defaults are assumed.</p><div class="yield-fields"><label>Calculate from<select id="yield-mode" class="form-select"><option value="ep">Edible weight needed (EP)</option><option value="ap">Purchased weight (AP)</option></select></label><label>Weight<input id="yield-amount" type="number" min="0.001" step="any" inputmode="decimal" placeholder="e.g. 1000"></label><label>Unit<select id="yield-unit" class="form-select"><option>g</option><option>kg</option></select></label><label>Measured yield (%)<input id="yield-percent" type="number" min="0.001" max="100" step="any" inputmode="decimal" placeholder="e.g. 80"></label></div><output id="yield-result" aria-live="polite">Enter a weight and yield to calculate.</output><p class="text-muted">Yield = edible weight ÷ purchased weight × 100. This models trimming loss only; cooking loss needs a separate measured yield.</p></section>`;
 const detail=container.querySelector('#station-detail');
 function select(i){const s=stations[i];detail.innerHTML=`<h3>${s[0]}</h3><p><strong>${s[1]}</strong></p><p>${s[2]}</p>`;container.querySelectorAll('[data-station]').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.station)===i)));}
 container.querySelectorAll('[data-station]').forEach(b=>b.onclick=()=>select(Number(b.dataset.station)));select(0);
 function calculate(){const q=id=>container.querySelector('#yield-'+id), result=yieldCalculation(Number(q('amount').value),Number(q('percent').value),q('mode').value),unit=q('unit').value;
 q('result').textContent=result?`Purchase: ${result.ap.toLocaleString(undefined,{maximumFractionDigits:2})} ${unit} · Edible: ${result.ep.toLocaleString(undefined,{maximumFractionDigits:2})} ${unit} · Trim: ${result.loss.toLocaleString(undefined,{maximumFractionDigits:2})} ${unit}`:'Enter a weight greater than zero and a yield greater than 0% and at most 100%.';}
 container.querySelectorAll('input,select').forEach(el=>el.addEventListener('input',calculate));
}
window.KitchenOperations={render,yieldCalculation,voiceCommand};
})();
