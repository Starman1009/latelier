/* Conservative source-quantity arithmetic. Unsupported expressions remain explicit. */
(()=>{'use strict';
const fractions={'¼':'1/4','½':'1/2','¾':'3/4','⅛':'1/8','⅜':'3/8','⅝':'5/8','⅞':'7/8','⅓':'1/3','⅔':'2/3'};
function scale(value,factor){
 if(typeof value!=='string'||!Number.isFinite(factor)||factor<=0)return null;
 if(factor===1)return value;
 let rest=value.replace(/[¼½¾⅛⅜⅝⅞⅓⅔]/g,x=>' '+fractions[x]).replace(/\s+/g,' ').trim();
 const terms=[];
 const number='((?:\\d+\\s+)?\\d+/\\d+|\\d+(?:\\.\\d+)?)';
 const term=new RegExp('^'+number+'\\s*(fl\\s*oz|tbsp|tsp|gallons?|quarts?|pints?|cups?|lbs?|oz|kg|mg|ml|qt|pt|lb|g|l|t|ea|each|ct)?(?=\\s|\\+|$)','i');
 while(rest){
  const m=rest.match(term);if(!m)return null;
  const parts=m[1].split(/\s+/);let amount=0;
  for(const p of parts){if(p.includes('/')){const [a,b]=p.split('/').map(Number);if(!b)return null;amount+=a/b;}else amount+=Number(p);}
  if(!Number.isFinite(amount)||amount<0)return null;
  terms.push(Number((amount*factor).toFixed(6))+(m[2]?' '+m[2]:''));
  rest=rest.slice(m[0].length).trim();
  if(rest.startsWith('+')){rest=rest.slice(1).trim();if(!rest)return null;}
  if(rest&&!m[2])return null;
 }
 return terms.length?terms.join(' + '):null;
}
window.VaultQuantities={scale};
})();
