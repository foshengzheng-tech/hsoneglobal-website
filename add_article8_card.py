from pathlib import Path

root = Path(r'H:\accio\hsone_publish')
path = root / 'knowledge-center' / 'index.html'
s = path.read_text(encoding='utf-8')
card = '''<a class="card" href="/knowledge-center/best-iphone-screen-protector-reddit-guide/"><img src="/assets/images/site/article8-hero.webp" alt="Best iPhone screen protector Reddit-informed buyer guide"><div class="pad"><p class="link">2026-08-04</p><h3>Best iPhone Screen Protector: What Reddit Users Actually Care About</h3><p>A practical guide to clarity, privacy, matte finishes, case fit, installation and OEM product design.</p></div></a>'''
if '/knowledge-center/best-iphone-screen-protector-reddit-guide/' not in s:
    s = s.replace('<div class="grid cols-4">', '<div class="grid cols-4">' + card, 1)
    path.write_text(s, encoding='utf-8')
    print('card added')
else:
    print('card already exists')
