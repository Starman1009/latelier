/* Meal generation uses a deliberately selected pool, never the legacy archive. */
const menuPools = {
  morningSmall:['52965','53080'],
  morningMain:['52962','53225'],
  morningSweet:['52855','53331'],
  light:['53173','53484','53309'],
  soup:['52841','52842','53173'],
  main:['52959','52773','52839','52982'],
  sweet:['52893','52891','52961'],
  side:['52965','53309','53484']
};
const mealArcs={
 breakfast:[['Small plate','morningSmall'],['Savory centerpiece','morningMain'],['Sweet finish','morningSweet']],
 brunch:[['Fresh opening','light'],['Brunch centerpiece','morningMain'],['Sweet finish','morningSweet']],
 lunch:[['Light opening','light'],['Main course','main'],['Dessert','sweet']],
 dinner:[['First course','soup'],['Main course','main'],['Dessert','sweet']]
};
let menu={occasion:'dinner',count:3,courses:[],checks:{}},menuBusy=false;
try{const stored=JSON.parse(localStorage.getItem('atelier_menu_v1'));if(stored&&mealArcs[stored.occasion]&&Array.isArray(stored.courses)&&[2,3,4].includes(stored.count))menu=stored}catch{}
function keepMenu(){try{localStorage.setItem('atelier_menu_v1',JSON.stringify(menu))}catch{$('#status').textContent='Menu could not be saved. Export it before leaving.'}}
function arc(){let a=mealArcs[menu.occasion].map(x=>[...x]);if(menu.count===2)a=a.slice(0,2);if(menu.count===4)a.splice(2,0,['Side course',menu.occasion==='breakfast'?'light':'side']);return a}
function shuffle(a){const out=[...a];for(let i=out.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[out[i],out[j]]=[out[j],out[i]]}return out}
async function sourceRecipe(id){
 const response=await fetch('https://www.themealdb.com/api/json/v1/1/lookup.php?i='+encodeURIComponent(id),{signal:AbortSignal.timeout(12000)});
 if(!response.ok)throw Error('Recipe source unavailable');const m=(await response.json()).meals?.[0];
 if(!m||String(m.idMeal)!==id||!m.strMeal?.trim()||!m.strInstructions||m.strInstructions.trim().length<100)throw Error('Incomplete recipe');
 const ingredients=Array.from({length:20},(_,i)=>({name:m['strIngredient'+(i+1)]?.trim(),raw:m['strMeasure'+(i+1)]?.trim()})).filter(i=>i.name);
 if(ingredients.length<2||ingredients.some(i=>!i.raw))throw Error('Missing measurements');
 const steps=m.strInstructions.split(/\r?\n/).map(s=>s.trim()).filter(s=>s&&!/^(step\s*)?\d+\.?$/i.test(s));
 const equipment=['whisk','saucepan','skillet','frying pan','baking tray','baking dish','bowl','blender','colander','sieve','oven','pot','knife','spatula','wooden spoon','grater','chinois','tamis','sous-vide','siphon'].filter(w=>new RegExp('\\b'+w+'s?\\b','i').test(m.strInstructions));
 return {id:'online-'+id,title:m.strMeal,source:safeURL(m.strSource)||'https://www.themealdb.com/meal/'+id,sourceLabel:'TheMealDB',cuisine:m.strArea||'',ingredients,steps,equipment,yield:null,online:true,checkedAt:new Date().toISOString(),sourceChecked:true};
}
async function generateMenuPlan(only=null){
 if(menuBusy)return;menuBusy=true;view='menu';request++;$('#status').textContent='Choosing courses and checking the original recipe records…';renderMenu();
 const previous=menu.courses;const proposed=previous.map(c=>({...c}));const slots=arc();const used=new Set(previous.filter((c,i)=>only!==null?i!==only:c.locked).map(c=>c.recipe.id));
 try{
 for(let i=0;i<slots.length;i++){
  if((only!==null&&i!==only)||(only===null&&previous[i]?.locked))continue;
  const [role,pool]=slots[i];let chosen;
  const choices=shuffle(menuPools[pool]).filter(id=>!used.has('online-'+id));
  choices.sort((a,b)=>(('online-'+a===previous[i]?.recipe.id)?1:0)-(('online-'+b===previous[i]?.recipe.id)?1:0));
  for(const id of choices){try{chosen=await sourceRecipe(id);break}catch{}}
  if(!chosen)throw Error('A complete recipe could not be loaded for '+role+'.');
  used.add(chosen.id);proposed[i]={role,recipe:chosen,locked:false};
 }
 menu.courses=proposed.slice(0,slots.length);menu.checks={};keepMenu();$('#status').textContent='Your menu is ready. Each recipe was checked against its live source record.';
 }catch(e){$('#status').textContent=e.message+' Your previous menu is preserved. Try again when the recipe source is available.'}
 finally{menuBusy=false;if(view==='menu')renderMenu()}
}
function renderMenu(){
 view='menu';$('#recipe-search').hidden=true;
 const c=menu.courses;
 $('#content').innerHTML=`<section class="menu-controls"><div><p class="eyebrow">WHAT ARE WE COOKING?</p><div class="occasion-picker">${Object.keys(mealArcs).map(k=>`<button data-occasion="${k}" aria-pressed="${menu.occasion===k}" ${menuBusy?'disabled':''}>${k[0].toUpperCase()+k.slice(1)}</button>`).join('')}</div></div><label>Courses<select id="course-count" ${menuBusy?'disabled':''}>${[2,3,4].map(n=>`<option ${menu.count===n?'selected':''}>${n}</option>`).join('')}</select></label><button id="generate-menu" ${menuBusy?'disabled':''}>${menuBusy?'Checking recipes…':c.length?'Surprise me again ↻':'Generate my menu ↗'}</button></section><p class="muted">Random within a selected pool for each occasion. Lock a dish you love, or swap a single course.</p>${c.length?`<div class="menu-heading"><h2>Your ${esc(menu.occasion)} menu</h2><span>${c.length} courses · source measurements</span></div><div class="grid menu-grid">${c.map((course,i)=>`<article class="card"><p class="eyebrow">0${i+1} / ${esc(course.role)}</p><h3>${esc(course.recipe.title)}</h3><span class="tag">Source record checked</span><p class="muted">${course.recipe.ingredients.length} ingredients · ${course.recipe.steps.length} instruction sections</p><div class="actions"><button data-menu-open="${i}">Recipe & cook</button><button data-lock="${i}" aria-pressed="${course.locked}" ${menuBusy?'disabled':''}>${course.locked?'Unlock':'Lock'}</button><button data-swap="${i}" ${menuBusy||course.locked?'disabled':''}>Swap</button></div><a href="${esc(course.recipe.source)}" target="_blank" rel="noopener">Original recipe ↗</a></article>`).join('')}</div><div class="actions"><button id="menu-shopping">Shop this whole menu</button><button id="menu-prep">Mise en place ↓</button><button id="export-menu">Export menu</button></div><p class="muted">Source checked means the live record contains named ingredients, measurements, and instructions. These dishes have not been kitchen-tested by L’Atelier. Source yields are unavailable: recipes retain their original batch sizes, not assumed portions per guest.</p><section id="mise"><p class="eyebrow">BEFORE THE FIRST PAN GOES ON</p><h2>Your mise en place</h2><p>Measure each recipe’s ingredients, gather the tools mentioned in its method, and review the preparation excerpts below. Follow the full recipe for cooking order and temperatures.</p>${c.map((course,i)=>prepCard(course,i)).join('')}</section>`:'<div class="menu-empty"><h2>Your next meal starts with a surprise.</h2><p>Choose an occasion and generate a complete sequence of dishes, with real recipes and a prep checklist for each course.</p><p class="muted">Breakfast & brunch: a small opening, a savory centerpiece, and a sweet finish. Lunch & dinner: an opening course, main, and dessert. Two courses omit the finish; four add a side.</p></div>'}`;
 document.querySelectorAll('[data-occasion]').forEach(b=>b.onclick=()=>{if(menu.occasion===b.dataset.occasion)return;menu.occasion=b.dataset.occasion;menu.courses=[];menu.checks={};keepMenu();renderMenu();$('#status').textContent='Choose Generate my menu to compose your '+menu.occasion+'.'});
 $('#course-count').onchange=e=>{menu.count=+e.target.value;menu.courses=[];menu.checks={};keepMenu();renderMenu()};$('#generate-menu').onclick=()=>generateMenuPlan();
 document.querySelectorAll('[data-menu-open]').forEach(b=>b.onclick=()=>openRecipe(menu.courses[+b.dataset.menuOpen].recipe));
 document.querySelectorAll('[data-lock]').forEach(b=>b.onclick=()=>{const c=menu.courses[+b.dataset.lock];c.locked=!c.locked;keepMenu();renderMenu()});document.querySelectorAll('[data-swap]').forEach(b=>b.onclick=()=>generateMenuPlan(+b.dataset.swap));
 document.querySelectorAll('[data-prep]').forEach(b=>b.onchange=()=>{menu.checks[b.dataset.prep]=b.checked;keepMenu()});
 $('#menu-prep')?.addEventListener('click',()=>$('#mise').scrollIntoView({behavior:'smooth'}));
 $('#menu-shopping')?.addEventListener('click',()=>{for(const c of menu.courses)for(const i of c.recipe.ingredients){if(!state.shopping.some(s=>s.name===i.name&&s.amount===i.raw&&s.dish===c.recipe.title))state.shopping.push({name:i.name,amount:i.raw,dish:c.recipe.title,done:false})}persist();shopping();$('#status').textContent='All menu ingredients added. Exact duplicate entries were kept once; different quantities remain separate.'});
 $('#export-menu')?.addEventListener('click',()=>{const u=URL.createObjectURL(new Blob([JSON.stringify(menu,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=u;a.download='latelier-'+menu.occasion+'-menu.json';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)});
}
function prepCard(course,index){const r=course.recipe;const prep=r.steps.flatMap(s=>s.split(/(?<=[.!?])\s+/)).filter(s=>/\b(chop|slice|dice|peel|wash|rinse|measure|preheat|grease|line|grate|finely|chopped|sliced|diced|peeled)\b/i.test(s));
 const check=(key,text)=>`<label class="prep-check"><input type="checkbox" data-prep="${key}" ${menu.checks[key]?'checked':''}><span>${esc(text)}</span></label>`;
 return `<article class="prep-card"><h3>0${index+1} · ${esc(r.title)}</h3><details open><summary>Measure & set out ingredients</summary>${r.ingredients.map((i,n)=>check(index+'-ingredient-'+n,i.raw+' — '+i.name)).join('')}</details><details><summary>Gather equipment mentioned in the method</summary>${r.equipment.length?r.equipment.map((e,n)=>check(index+'-tool-'+n,e)).join(''):'<p>No separate tool names detected. Check the full method for your setup.</p>'}<p class="muted">Tools are extracted from the source text; this is not an exhaustive equipment specification.</p></details><details><summary>Preparation excerpts from the original recipe</summary>${prep.length?'<ul>'+prep.map(s=>'<li>'+esc(s)+'</li>').join('')+'</ul>':'<p>No standalone preparation excerpts detected. Read the full recipe before beginning.</p>'}<p class="muted">Excerpts may include cooking actions. Keep the source recipe’s sequence; this is not a timed schedule.</p></details></article>`}
$('#menu-home').onclick=()=>{request++;renderMenu();$('#status').textContent=menu.courses.length?'Your last menu is restored on this device.':''};renderMenu();
