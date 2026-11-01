const CACHE = 'atelier-kitchen-v3';
const SHELL = ['./','./index.html','./kitchen.css','./culinary.js','./kitchen.js','./menu.js','./cooking.js','./tools.js','./manifest.json','./icon-192.png','./icon-512.png'];
const LOCAL = [...SHELL,'./recipes.json','./data-review.json','./brigade.html','./studio.html','./curator.html'].map(path=>new URL(path,self.registration.scope).href);
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(SHELL))));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>(key.startsWith('atelier-kitchen-')||key.startsWith('latelier-os-'))&&key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
 const url=new URL(event.request.url);
 if(event.request.method!=='GET'||!/^https?:$/.test(url.protocol)||url.origin!==self.location.origin)return;
 const canonical=url.origin+url.pathname;
 if(!LOCAL.includes(canonical))return;
 event.respondWith((async()=>{
  const cache=await caches.open(CACHE);
  try {const response=await fetch(event.request);if(response.ok){const copy=response.clone();event.waitUntil(cache.put(canonical,copy))}return response}
  catch {return await cache.match(canonical)||new Response('This page is not available offline yet. Open the menu home page to use saved recipes.',{status:503,headers:{'Content-Type':'text/plain'}})}
 })());
});
