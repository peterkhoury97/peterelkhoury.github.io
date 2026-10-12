"""Generate Arabic/French static pages from English sources and reviewed text.

Run: python tools/build_localizations.py
The published website does not need Python or a build service.
"""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
import json
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://peterkhoury97.github.io/peterelkhoury.github.io/'
LOCALES = {'en': ('English', 'Choose language'), 'ar': ('العربية', 'اختر اللغة'), 'fr': ('Français', 'Choisir la langue')}
IDENTITIES = {
    'p','Pektrix','FreshOps','LeadBot','ASP.NET Core','JavaScript','PostgreSQL',
    'Pine Script','.NET','TradingView.','Python','Flask','Redis','Google Sheets',
    'SQL Server','SignalR','Flutter','React','TypeScript','Cloudflare','Drizzle ORM',
    'Emcrey','Clover Broker','Onsite Snagging','Exquitech · Neorcha · GridPos',
    'Java · C# · Spring Boot · ASP.NET Core','SQL Server · PostgreSQL · MySQL',
    'Entity Framework · Dapper · Kafka · IBM MQ',
    'JavaScript · TypeScript · React · Python · Flutter',
    'Azure · AWS · Docker · GitHub Actions','peterelkhoury97@gmail.com','GitHub',
    'ASP.NET Core · PostgreSQL · JavaScript · Entity Framework Core',
    'Entity Framework Core','React · TypeScript · Cloudflare D1 · Cloudflare R2 · Drizzle ORM',
    'Cloudflare D1','Cloudflare R2','5K+','nicoexplorer','Next.js','Tailwind CSS',
}
VOID_TAGS = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

def language_menu(locale, source):
    current_path = ('' if locale == 'en' else locale + '/') + source.as_posix()
    parent = posixpath.dirname(current_path) or '.'
    asset_prefix = posixpath.relpath('assets/flags', parent)
    label = LOCALES[locale][1]
    summary = (f'<summary aria-label="{label}: {LOCALES[locale][0]}">'
               f'<img class="language-flag" src="{asset_prefix}/{locale}.svg" width="24" height="16" alt="" aria-hidden="true">'
               f'<span class="language-code" aria-hidden="true">{locale.upper()}</span>'
               '<span class="language-chevron" aria-hidden="true">⌄</span></summary>')
    items = []
    for target, (name, _) in LOCALES.items():
        target_path = ('' if target == 'en' else target + '/') + source.as_posix()
        href = posixpath.relpath(target_path, parent) + '?lang=' + target
        current = ' aria-current="page"' if locale == target else ''
        items.append(f'<li><a class="language-link" href="{href}" lang="{target}" hreflang="{target}"{current}>'
                     f'<img class="language-flag" src="{asset_prefix}/{target}.svg" width="24" height="16" alt="" aria-hidden="true">'
                     f'<span dir="auto">{name}</span></a></li>')
    return f'<details class="language-picker">{summary}<ul aria-label="{label}">{"".join(items)}</ul></details>'

class LocalizedPage(HTMLParser):
    def __init__(self, source, locale):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.locale = locale
        self.translations = json.loads((ROOT/'translations'/f'{locale}.json').read_text(encoding='utf-8'))
        self.result = []
        self.ignored_depth = 0
        self.raw_tag = None
        self.structured_data = False

    def translate(self, value):
        key = value.strip()
        if not key: return value
        if key in self.translations: return value.replace(key, self.translations[key], 1)
        if key in IDENTITIES or not re.search('[A-Za-z]', key): return value
        raise ValueError(f'Missing {self.locale} translation: {key}')

    def body_text(self, value):
        translated = self.translate(value)
        if self.locale != 'ar': return escape(translated, quote=False)
        if translated.strip() in IDENTITIES:
            return '<bdi dir="ltr">' + escape(translated, quote=False) + '</bdi>'
        pattern = r'(?:\.[A-Za-z][A-Za-z0-9.#]*|[A-Za-z][A-Za-z0-9.#]*)(?:[ \t]+(?:[A-Z][A-Za-z0-9.#]*|\d+))*'
        parts, start = [], 0
        for match in re.finditer(pattern, translated):
            parts += [escape(translated[start:match.start()], quote=False),
                      '<bdi dir="ltr">' + escape(match.group(), quote=False) + '</bdi>']
            start = match.end()
        parts.append(escape(translated[start:], quote=False))
        return ''.join(parts)

    def handle_decl(self, decl): self.result.append('<!' + decl + '>')
    def handle_comment(self, data):
        if not self.ignored_depth: self.result.append('<!--' + data + '-->')

    def handle_starttag(self, tag, attrs):
        if self.ignored_depth:
            if tag not in VOID_TAGS: self.ignored_depth += 1
            return
        pairs = dict(attrs)
        if tag == 'details' and 'language-picker' in pairs.get('class', '').split():
            self.result.append(language_menu(self.locale, self.source))
            self.ignored_depth = 1
            return
        if tag == 'html': pairs.update(lang=self.locale, dir='rtl' if self.locale == 'ar' else 'ltr')
        if tag in ('script','style'):
            self.raw_tag = tag
            self.structured_data = pairs.get('type') == 'application/ld+json'
        for key, value in list(pairs.items()):
            if value is None: continue
            if key in ('alt','aria-label','data-title','data-caption'): pairs[key] = self.translate(value)
            if tag == 'meta' and key == 'content' and pairs.get('name', pairs.get('property')) in ('description','og:title','og:description','og:image:alt'):
                pairs[key] = self.translate(value)
            if key in ('href','src') and value.startswith(('assets/','../assets/','styles.css','../styles.css','script.js','../script.js','language.js','../language.js')):
                pairs[key] = '../' + value
            if (tag == 'link' and pairs.get('rel') == 'canonical' and key == 'href') or (tag == 'meta' and pairs.get('property') == 'og:url' and key == 'content'):
                pairs[key] = value.replace(BASE, BASE + self.locale + '/', 1)
        if self.locale == 'ar':
            if pairs.get('class') in ('monogram','impact-number'): pairs['dir'] = 'ltr'
            if tag == 'li': pairs['dir'] = 'auto'
        attr_text = ''.join(' ' + key + (f'="{escape(value,quote=True)}"' if value is not None else '') for key,value in pairs.items())
        self.result.append('<' + tag + attr_text + '>')

    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs)
    def handle_endtag(self, tag):
        if self.ignored_depth:
            self.ignored_depth -= 1
            return
        self.result.append('</' + tag + '>')
        if tag == self.raw_tag:
            self.raw_tag = None
            self.structured_data = False

    def handle_data(self, data):
        if self.ignored_depth: return
        if self.raw_tag:
            if self.structured_data:
                obj = json.loads(data)
                if obj.get('@type') == 'Person':
                    obj.update(name=self.translate('Peter El-Khoury'), jobTitle='مهندس برمجيات أول' if self.locale == 'ar' else 'Ingénieur logiciel senior')
                data = json.dumps(obj, ensure_ascii=False, separators=(',',':'))
            self.result.append(data)
        else: self.result.append(self.body_text(data))

def build():
    sources = [Path('index.html'), *[p.relative_to(ROOT) for p in sorted((ROOT/'projects').glob('*.html'))]]
    for source in sources:
        original = (ROOT/source).read_text(encoding='utf-8')
        original = re.sub(r'<details class="language-picker">.*?</details>', language_menu('en', source), original, flags=re.S)
        (ROOT/source).write_text(original, encoding='utf-8')
        for locale in ('ar','fr'):
            parser = LocalizedPage(source, locale)
            parser.feed(original)
            target = ROOT/locale/source
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(''.join(parser.result), encoding='utf-8')
            print('Translated:', target.relative_to(ROOT))
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for prefix in ('','ar/','fr/'):
        for source in sources:
            route = '' if source.as_posix() == 'index.html' else source.as_posix()
            sitemap += f'  <url><loc>{BASE}{prefix}{route}</loc><lastmod>2026-10-12</lastmod></url>\n'
    (ROOT/'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')

if __name__ == '__main__': build()
