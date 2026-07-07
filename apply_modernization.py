import os
import glob

# The changes we want to make
NAV_TARGET = """            <a href="tecidos.html" class="text-base py-3 px-4 hover:bg-gray-100 hover:text-navy">
              TECIDOS
            </a>"""

NAV_REPLACE = """            <a href="conjuntos.html" class="text-base py-3 px-4 hover:bg-gray-100 hover:text-navy font-bold" style="color: #b3923b;">
              CONJUNTOS ⭐
            </a>
            <a href="tecidos.html" class="text-base py-3 px-4 hover:bg-gray-100 hover:text-navy">
              TECIDOS
            </a>"""

BANNER_TARGET = """  <body>"""
BANNER_REPLACE = """  <body>
    <!-- Global Promo Banner -->
    <div style="background: linear-gradient(90deg, #b3923b 0%, #d4af37 50%, #b3923b 100%); color: #000; text-align: center; padding: 0.6rem 1rem; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; z-index: 9999; position: relative; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
      🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS!
    </div>"""

for filepath in glob.glob("*.html"):
    if filepath == "carreira.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already patched to avoid double patching
    if "CONJUNTOS" not in content and NAV_TARGET in content:
        content = content.replace(NAV_TARGET, NAV_REPLACE)
        
    if "Entrega, Montagem e Recolha" not in content and BANNER_TARGET in content:
        content = content.replace(BANNER_TARGET, BANNER_REPLACE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All HTML files updated with banner and Conjuntos link!")
