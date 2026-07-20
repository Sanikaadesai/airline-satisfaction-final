import base64, sys
F = "/root/.claude/skills/canvas-design/canvas-fonts/"
b64 = lambda p: base64.b64encode(open(p,'rb').read()).decode()

tpl = open('site-template-v2.html').read()
for tok, path in [('{{OUTFIT_BOLD}}','Outfit-Bold.ttf'),('{{OUTFIT_REG}}','Outfit-Regular.ttf'),
                  ('{{WORK_REG}}','WorkSans-Regular.ttf'),('{{WORK_BOLD}}','WorkSans-Bold.ttf'),
                  ('{{GEIST_REG}}','GeistMono-Regular.ttf')]:
    tpl = tpl.replace(tok, b64(F+path))

IMGS = {
 '{{IMG_HERO}}':   sys.argv[1],  # dusk house 16:9
 '{{IMG_ROOF}}':   "https://d8j0ntlcm91z4.cloudfront.net/user_3GHhv4aECqtSGF3f8o6vZA1A4d1/hf_20260720_152253_26d39299-c261-47f3-874b-8fdbed012681.png",
 '{{IMG_SIDING}}': "https://d8j0ntlcm91z4.cloudfront.net/user_3GHhv4aECqtSGF3f8o6vZA1A4d1/hf_20260720_153305_3f812010-873c-4c01-a5fb-a04f61bf4261.png",
 '{{IMG_GUTTER}}': "https://d8j0ntlcm91z4.cloudfront.net/user_3GHhv4aECqtSGF3f8o6vZA1A4d1/hf_20260720_152255_870f4a53-f1cd-4de6-873d-db1dbeb70dfe.png",
 '{{IMG_MASON}}':  "https://d8j0ntlcm91z4.cloudfront.net/user_3GHhv4aECqtSGF3f8o6vZA1A4d1/hf_20260720_152257_af8b1e0e-0156-40fd-91c7-808b5e0e8db9.png",
 '{{IMG_STEPS}}':  "https://d8j0ntlcm91z4.cloudfront.net/user_3GHhv4aECqtSGF3f8o6vZA1A4d1/hf_20260720_153306_15d9edfd-bd0f-49c5-870e-006529d07924.png",
}
final = tpl
for k,v in IMGS.items(): final = final.replace(k, v)
open('index.html','w').write(final)
print("index.html", len(final)//1024, "KB")

svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#16233c"/><stop offset="1" stop-color="#0b1322"/></linearGradient><linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4F8DFF"/><stop offset="1" stop-color="#38E1C6"/></linearGradient></defs><rect width="1200" height="800" fill="url(#g)"/><g stroke="url(#a)" stroke-width="7" fill="none" opacity="0.8" stroke-linecap="round" stroke-linejoin="round"><path d="M300 520 L600 330 L900 520"/><path d="M760 400 V330 h55 v110"/><path d="M340 520 h520"/></g><text x="600" y="620" text-anchor="middle" font-family="monospace" font-size="30" letter-spacing="8" fill="#93A0B4">CLIENT PHOTO</text></svg>'''
ph = "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
prev = tpl
for k in IMGS: prev = prev.replace(k, ph)
open('preview-render-v2.html','w').write(prev)
print("preview ok")
