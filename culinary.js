/* Pure data helpers, shared by the kitchen and regression checks. */
const Culinary = (() => {
  const fold = s => String(s || '').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
  const units = {g:'g',gram:'g',grams:'g',kg:'kg',kilogram:'kg',kilograms:'kg',ml:'ml',milliliter:'ml',milliliters:'ml',l:'l',litre:'l',liter:'l',litres:'l',liters:'l',tsp:'tsp',teaspoon:'tsp',teaspoons:'tsp',tbs:'tbsp',tblsp:'tbsp',tbsp:'tbsp',tablespoon:'tbsp',tablespoons:'tbsp',cup:'cup',cups:'cup',oz:'oz',ounce:'oz',ounces:'oz',lb:'lb',pound:'lb',pounds:'lb',pcs:'pcs',piece:'pcs',pieces:'pcs'};
  function measure(raw) {
    const s=String(raw).trim().replace(/½/g,' 1/2').replace(/¼/g,' 1/4').replace(/¾/g,' 3/4');
    const m=s.match(/^(\d+\s+\d+\/\d+|\d+\/\d+|\d+(?:\.\d+)?)\s*([a-z]+)$/i);
    if(!m||!units[m[2].toLowerCase()])return null;
    const q=m[1].split(/\s+/).reduce((sum,n)=>{const [a,b]=n.split('/').map(Number);return sum+(b===undefined?a:a/b)},0);
    return Number.isFinite(q)&&q>0?{qty:q,unit:units[m[2].toLowerCase()]}:null;
  }
  function aisle(name) {
    const n=fold(name);
    if(/\b(salmon|prawn|shrimp|fish|tuna|scallop|lobster|oyster|anchov|cod)\w*\b/.test(n))return 'Seafood';
    if(/\b(beef|chicken|pork|lamb|duck|bacon|sausage|turkey)\b/.test(n))return 'Butchery';
    if(/\b(coconut|almond|oat|soy)\b/.test(n)&&/milk|cream/.test(n))return 'Pantry';
    if(/\b(egg|eggs|milk|butter|cream|cheese|yogurt|ricotta|stilton|parmesan)\b/.test(n))return 'Dairy';
    if(/\b(onion|garlic|celery|leek|potato|tomato|lemon|lime|broccoli|fennel|parsley|basil|carrot|apple|strawberr|blueberr|raspberr|berry|berries|spinach)\w*\b/.test(n))return 'Produce';
    if(/\b(flour|rice|pasta|penne|spaghetti|sugar|oat|oats|bread)\b/.test(n))return 'Dry Goods';
    return 'Pantry';
  }
  function groceries(items) {
    const groups=new Map();
    items.forEach((item,index)=>{
      const m=measure(item.amount); const key=m?fold(item.name)+'|'+m.unit:'raw|'+index;
      if(!groups.has(key))groups.set(key,{name:item.name,unit:m?.unit,qty:0,raw:item.amount,indices:[],dishes:[],aisle:aisle(item.name)});
      const g=groups.get(key);g.qty+=m?.qty||0;g.indices.push(index);if(!g.dishes.includes(item.dish))g.dishes.push(item.dish);
    });
    return [...groups.values()].map(g=>({...g,amount:g.unit?`${+g.qty.toFixed(3)} ${g.unit}`:g.raw,done:g.indices.every(i=>items[i].done)}));
  }
  function validRecipe(r) {return !!r&&typeof r.id==='string'&&typeof r.title==='string'&&Array.isArray(r.ingredients)&&r.ingredients.every(i=>i&&typeof i.name==='string'&&(typeof i.raw==='string'||(Number.isFinite(i.qty)&&i.qty>0&&typeof i.unit==='string')))&&Array.isArray(r.steps)&&r.steps.every(s=>typeof s==='string')&&Array.isArray(r.equipment)&&r.equipment.every(s=>typeof s==='string')&&(r.yield===null||r.yield===undefined||(Number.isFinite(r.yield)&&r.yield>0));}
  function quality(r){return r.legacy||r.cookable===false||!Number.isFinite(r.yield)||r.yield<=0||!r.ingredients.length||!r.steps.length||r.ingredients.some(i=>!i.name.trim()||(!i.qty&&(!i.raw?.trim()||i.raw==='Quantity not supplied')))||r.steps.join(' ').length<100?'Needs Review':r.provenance==='verified_sourced'?'Verified Sourced':r.online?'Source record checked':'User Created'}
  function provenance(r){if(r.provenance)return ({verified_sourced:'Verified Sourced',adapted_publisher:'Adapted Publisher',user_created:'User Created',gc_ms_synthesis:'GC-MS Experimental Synthesis'})[r.provenance]||'Needs Review';return r.experimental?'GC-MS Experimental Synthesis':r.adapted?'Adapted Publisher':r.legacy?'Needs Review':r.online?'Sourced · TheMealDB':'User Created'}
  function scale(i,yieldCount,covers){return Number.isFinite(i.qty)&&yieldCount>0?`${+(i.qty*covers/yieldCount).toFixed(3)} ${i.unit}`:i.raw||'Quantity not supplied'}
  return {fold,measure,aisle,groceries,validRecipe,quality,provenance,scale};
})();
