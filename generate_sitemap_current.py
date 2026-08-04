from pathlib import Path
from datetime import date

root = Path(r'H:\accio\hsone_publish')
domain = 'https://www.hsoneglobal.com'
urls = [domain + '/']
for p in root.rglob('index.html'):
    rel = p.parent.relative_to(root).as_posix()
    if rel != '.':
        urls.append(f'{domain}/{rel}/')
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml += ''.join(f'  <url><loc>{u}</loc><lastmod>{date.today().isoformat()}</lastmod></url>\n' for u in sorted(set(urls)))
xml += '</urlset>\n'
(root / 'sitemap.xml').write_text(xml, encoding='utf-8')
print(f'Generated {len(set(urls))} sitemap URLs')
