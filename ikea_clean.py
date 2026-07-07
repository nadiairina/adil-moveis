import os
import glob
import re

OLD_BANNER = """    <!-- Global Promo Banner -->
    <div style="background: linear-gradient(90deg, #b3923b 0%, #d4af37 50%, #b3923b 100%); color: #000; text-align: center; padding: 0.6rem 1rem; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; z-index: 9999; position: relative; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
      🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS!
    </div>"""

NEW_BANNER = """    <!-- Global Promo Banner -->
    <div class="bg-black text-white text-center py-3 text-sm font-bold tracking-wide z-50 relative">
      🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS em Todo o Lado!
    </div>"""

def apply_ikea_cleanliness(content):
    # 1. Replace the gold banner with a clean black one
    if OLD_BANNER in content:
        content = content.replace(OLD_BANNER, NEW_BANNER)
        
    # 2. Remove fancy serif fonts
    content = content.replace('style="font-family: \'Playfair Display\', serif; font-style: italic;"', '')
    content = content.replace('style="font-family: \'Playfair Display\', serif;"', '')
    content = content.replace('font-serif', 'font-sans')
    content = content.replace('italic', '') # Remove italic classes
    
    # 3. Clean up the shadow texts that look dated
    content = content.replace('text-shadow', '')
    
    # 4. Remove any gold colors explicitly set (#b3923b) to standard tailwind gray or black
    content = content.replace('style="color: #b3923b;"', 'class="text-gray-900"')
    content = content.replace('style="border-color: #b3923b;"', 'class="border-gray-900"')
    
    # 5. Fix Almada e Seixal in index.html specifically (or anywhere it appears)
    content = content.replace('Entrega e Montagem Grátis no Concelho de Almada e Seixal', 'Entrega e Montagem Grátis')
    
    return content

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = apply_ikea_cleanliness(content)
    
    # Write back if changed
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("IKEA cleanliness applied to all files!")
