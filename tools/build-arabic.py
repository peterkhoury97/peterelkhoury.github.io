"""Regenerate static Arabic pages from English HTML and reviewed translations.

Run from the repository root: python tools/build-arabic.py
No package installation or website build step is required for deployment.
"""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
import json
import posixpath
import re

BASE = 'https://peterkhoury97.github.io/peterelkhoury.github.io/'
ROOT = Path(__file__).resolve().parents[1]
TRANSLATIONS = json.loads((ROOT/'translations/ar.json').read_text(encoding='utf-8'))
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
    'Cloudflare D1','Cloudflare R2','5K+'
}

def translate(value):
    key = value.strip()
    if not key: return value
    if key in TRANSLATIONS: return value.replace(key,TRANSLATIONS[key],1)
    if key in IDENTITIES or not re.search('[A-Za-z]',key): return value
    raise ValueError(f'Missing Arabic translation: {key}')

def body_text(value):
    translated=translate(value)
    # Isolate Latin names so .NET, C# and multi-word technologies keep their order.
    if translated.strip() in IDENTITIES:
        return '<bdi dir="ltr">'+escape(translated,quote=False)+'</bdi>'
    pattern=r'(?:\.[A-Za-z][A-Za-z0-9.#]*|[A-Za-z][A-Za-z0-9.#]*)(?:[ \t]+(?:[A-Z][A-Za-z0-9.#]*|\d+))*'
    parts=[]
    start=0
    for match in re.finditer(pattern,translated):
        parts.append(escape(translated[start:match.start()],quote=False))
        parts.append('<bdi dir="ltr">'+escape(match.group(),quote=False)+'</bdi>')
        start=match.end()
    parts.append(escape(translated[start:],quote=False))
    return ''.join(parts)

class ArabicPage(HTMLParser):
    def __init__(self,source):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.result = []
        self.skip = 0
        self.language_link = False
    def handle_decl(self,decl): self.result.append('<!'+decl+'>')
    def handle_comment(self,data): self.result.append('<!--'+data+'-->')
    def handle_starttag(self,tag,attrs):
        pairs = dict(attrs)
        if tag in ('script','style'): self.skip += 1
        self.language_link = tag == 'a' and 'language-link' in pairs.get('class','').split() or self.language_link
        if tag == 'html': pairs.update(lang='ar',dir='rtl')
        for key,value in list(pairs.items()):
            if value is None: continue
            if key in ('alt','aria-label','data-title','data-caption'): pairs[key] = translate(value)
            if tag == 'meta' and key == 'content' and pairs.get('name',pairs.get('property')) in ('description','og:title','og:description','og:image:alt'):
                pairs[key] = translate(value)
            if key in ('href','src') and value.startswith(('assets/','../assets/','styles.css','../styles.css','script.js','../script.js','language.js','../language.js')):
                pairs[key] = '../'+value
            if (tag == 'link' and pairs.get('rel') == 'canonical' and key == 'href') or (tag == 'meta' and pairs.get('property') == 'og:url' and key == 'content'):
                pairs[key] = value.replace(BASE,BASE+'ar/',1)
        if tag == 'a' and 'language-link' in pairs.get('class','').split():
            parent = posixpath.dirname('ar/'+self.source.as_posix())
            pairs.update(href=posixpath.relpath(self.source.as_posix(),parent)+'?lang=en',lang='en',hreflang='en')
            pairs['aria-label'] = 'View this page in English'
        if pairs.get('class') == 'monogram' or pairs.get('class') == 'impact-number': pairs['dir'] = 'ltr'
        if tag == 'li': pairs['dir'] = 'auto'
        if tag == 'script' and pairs.get('type') == 'application/ld+json':
            self.structured_data = True
        else: self.structured_data = False
        attr_text = ''.join(' '+key+(f'="{escape(value,quote=True)}"' if value is not None else '') for key,value in pairs.items())
        self.result.append('<'+tag+attr_text+'>')
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
    def handle_endtag(self,tag):
        self.result.append('</'+tag+'>')
        if tag in ('script','style'): self.skip -= 1
        if tag == 'a': self.language_link = False
    def handle_data(self,data):
        if self.skip:
            if getattr(self,'structured_data',False):
                obj=json.loads(data)
                if obj.get('@type') == 'Person':
                    obj.update(name='بيتر الخوري',jobTitle='مهندس برمجيات أول')
                data=json.dumps(obj,ensure_ascii=False,separators=(',',':'))
            self.result.append(data)
        elif self.language_link and data.strip(): self.result.append('English')
        else: self.result.append(body_text(data))

for source in [Path('index.html'),*sorted((ROOT/'projects').glob('*.html'))]:
    if source.is_absolute(): source=source.relative_to(ROOT)
    parser=ArabicPage(source)
    parser.feed((ROOT/source).read_text(encoding='utf-8'))
    target=ROOT/'ar'/source
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(''.join(parser.result),encoding='utf-8')
    print('Translated:',target.relative_to(ROOT))

routes=['', 'projects/pektrix.html','projects/freshops.html','projects/personal-trainer.html']
sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for prefix in ('','ar/'):
    for route in routes: sitemap+=f'  <url><loc>{BASE}{prefix}{route}</loc><lastmod>2026-10-11</lastmod></url>\n'
(ROOT/'sitemap.xml').write_text(sitemap+'</urlset>\n',encoding='utf-8')
