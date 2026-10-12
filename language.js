// A URL explicitly choosing a language wins over a remembered preference.
// Static language links also work when scripts or browser storage are unavailable.
(() => {
  const base = new URL('.', document.currentScript.src);
  const url = new URL(location.href);
  const route = url.pathname.slice(base.pathname.length);
  const neutralRoute = route.replace(/^(?:ar|fr)\//, '');
  const current = document.documentElement.lang;
  const explicit = url.searchParams.get('lang');
  const languages = ['en', 'ar', 'fr'];
  let stored;
  try { stored = localStorage.getItem('portfolio-language'); } catch {}
  const chosen = languages.includes(explicit)
    ? explicit
    : current !== 'en' && languages.includes(current) ? current
    : languages.includes(stored) ? stored : 'en';
  try { localStorage.setItem('portfolio-language', chosen); } catch {}
  if (chosen !== current) {
    const destination = new URL((chosen === 'en' ? '' : chosen + '/') + neutralRoute, base);
    destination.search = url.search;
    destination.hash = url.hash;
    location.replace(destination.href);
  }
})();
