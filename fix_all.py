import glob
import re
import os

# --- 1. RESTORE PACKS to products.js ---
with open('products.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Check if packs are missing
if '"pack-3"' not in js_content:
    # Find the last closing brace of the object
    last_brace_idx = js_content.rfind('};')
    
    packs_data = """,
  "pack-1": {
    "id": "pack-1",
    "name": "Pack Sala de Sonho",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Sofá + Móvel de TV. Mobiliário Lourini de alta qualidade. Cores, acabamentos e tecidos personalizáveis na nossa loja física.",
    "image": "images/produtos/sofas-monika_main.jpg",
    "gallery": ["images/produtos/sofas-monika_main.jpg", "images/produtos/movel-tv-malmo.jpg"]
  },
  "pack-2": {
    "id": "pack-2",
    "name": "Pack Sala de Sonho Premium",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Sofá + Mesa de Centro + Móvel de TV. Mobiliário Lourini de alta qualidade. Cores, acabamentos e tecidos personalizáveis na nossa loja física.",
    "image": "images/produtos/sofas-monika_main.jpg",
    "gallery": ["images/produtos/sofas-monika_main.jpg", "images/produtos/mesa-centro-malmo.jpg", "images/produtos/movel-tv-malmo.jpg"]
  },
  "pack-3": {
    "id": "pack-3",
    "name": "Pack Aconchego Essencial",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Cama de Casal + Colchão + Almofadas. Mobiliário Lourini de alta qualidade e conforto superior.",
    "image": "images/produtos/cama-estofada-alison-bege-200x150.jpg",
    "gallery": ["images/produtos/cama-estofada-alison-bege-200x150.jpg", "images/produtos/colchao-mindol.jpg", "images/produtos/almofada-viscoprata.jpg"]
  },
  "pack-4": {
    "id": "pack-4",
    "name": "Pack À Mesa",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Mesa de Refeição + Cadeiras. Perfeito para momentos de convívio em família. Medidas e acabamentos personalizáveis.",
    "image": "images/produtos/mesa-jantar-extensivel-paris.jpg",
    "gallery": ["images/produtos/mesa-jantar-extensivel-paris.jpg", "images/produtos/cadeira-paris.jpg"]
  },
  "pack-5": {
    "id": "pack-5",
    "name": "Pack Sonhos Tranquilos",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Sommier de Casal + Cabeceira Estofada + Colchão. Conforto e elegância garantidos para o seu quarto.",
    "image": "images/produtos/cama-estofada-colchao-pack.jpg",
    "gallery": ["images/produtos/cama-estofada-colchao-pack.jpg", "images/produtos/sommier-new-33-37-branco.jpg", "images/produtos/cabeceira-luxe-estofada.jpg", "images/produtos/colchao-mindol.jpg"]
  }
};
"""
    # Replace the last `};` with the new packs and a new `};`
    js_content = js_content[:last_brace_idx] + packs_data + js_content[last_brace_idx+2:]
    
    with open('products.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Packs restored to products.js!")


# --- 2. REMOVE SNIPCART FROM HTML ---
html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Snipcart tags
    content = re.sub(r'<!-- Snipcart Configuration -->\s*<div hidden id="snipcart".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script src="https://cdn\.snipcart\.com.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="stylesheet" href="https://cdn\.snipcart\.com.*?/>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="preconnect" href="https://app\.snipcart\.com.*?/>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="preconnect" href="https://cdn\.snipcart\.com.*?/>', '', content, flags=re.DOTALL)

    # In pack-detalhe and produto-detalhe, remove the Add to Cart button and make WhatsApp default
    if filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
        # Remove the button entirely
        add_to_cart_block = r'<!-- Add to Cart -->(?:\s*<button id="addToCartBtn" class="snipcart-add-item".*?</button>)'
        content = re.sub(add_to_cart_block, '', content, flags=re.DOTALL)
        
        # Primary actions version
        add_to_cart_block_primary = r'<!-- Primary Actions -->(?:\s*<button id="addToCartBtn" class="snipcart-add-item".*?</button>)'
        content = re.sub(add_to_cart_block_primary, '<!-- Primary Actions -->', content, flags=re.DOTALL)

        # Make WhatsApp button display:flex instead of none
        content = content.replace('id="quoteWhatsAppBtn" href="#" target="_blank" style="display:none;', 'id="quoteWhatsAppBtn" href="#" target="_blank" style="display:flex;')
        
        # Remove JS logic that manipulated snipcart
        snipcart_js_block = r'// Prices hidden - always show WhatsApp quote button only.*?(?=\s*\}\s*else \{)'
        content = re.sub(snipcart_js_block, '', content, flags=re.DOTALL)
        content = re.sub(r'document\.getElementById\(\'addToCartBtn\'\)\.style\.display = \'none\';', '', content)
        content = re.sub(r'document\.getElementById\(\'quoteWhatsAppBtn\'\)\.style\.display = \'flex\';', '', content)
        
        # Remove any snipcart attribute assignment
        content = re.sub(r'var btn = document\.getElementById\(\'addToCartBtn\'\);.*?btn\.dataset\.itemCustom2Options = p\.custom2_options;', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Snipcart removed and templates updated.")
