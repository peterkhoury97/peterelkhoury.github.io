// A URL explicitly choosing a language wins over a remembered preference.
// Static language links also work when scripts or browser storage are unavailable.
(() => {
  const base = new URL('.', document.currentScript.src);
  const url = new URL(location.href);
  const route = url.pathname.slice(base.pathname.length);
  const current = document.documentElement.lang;
  const explicit = url.searchParams.get('lang');
  let stored;
  try { stored = localStorage.getItem('portfolio-language'); } catch {}
  const chosen = explicit === 'ar' || explicit === 'en'
    ? explicit
    : current === 'ar' ? 'ar' : stored === 'ar' ? 'ar' : 'en';
  try { localStorage.setItem('portfolio-language', chosen); } catch {}
  if (chosen !== current) {
    const destination = new URL(chosen === 'ar' ? 'ar/' + route : route.replace(/^ar\//, ''), base);
    destination.search = url.search;
    destination.hash = url.hash;
    location.replace(destination.href);
  }
})();
