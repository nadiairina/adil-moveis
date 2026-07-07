import os
import re
import json

html_files = ["quartos.html", "salas.html", "cozinha.html", "colchoes.html", "kids.html", "escritorio.html", "complementos.html", "conjuntos.html"]

products = {}

# We look for <button class="...snipcart-add-item..."> or similar
button_pattern = re.compile(r'<button[^>]*snipcart-add-item[^>]*>(.*?)</button>', re.DOTALL)
attr_pattern = re.compile(r'data-item-([a-zA-Z0-9_-]+)="([^"]*)"')

for file in html_files:
    if not os.path.exists(file): continue
    with open(file, "r") as f:
        content = f.read()
    
    # Find all product cards to try to extract images
    # A product card is usually a div containing snipcart-add-item
    cards = re.split(r'class="[^"]*product[^"]*"|class="[^"]*group[^"]*bg-\[\#FDFBF7\]', content)
    for card in cards[1:]:
        if 'snipcart-add-item' not in card: continue
        
        # extract button
        btn_match = re.search(r'<button[^>]*snipcart-add-item[^>]*>', card)
        if not btn_match: continue
        
        btn_tag = btn_match.group(0)
        attrs = dict(attr_pattern.findall(btn_tag))
        
        if 'id' in attrs:
            pid = attrs['id']
            
            # try to find image in card
            img_match = re.search(r'<img[^>]*src="([^"]+)"', card)
            img_url = img_match.group(1) if img_match else 'images/logo.png'
            
            # Special case for "Imagem Brevemente"
            if "feather=\"image\"" in card and not img_match:
                img_url = 'images/logo.png'
                
            products[pid] = {
                'id': pid,
                'name': attrs.get('name', ''),
                'price': float(attrs.get('price', '0.00')),
                'url': attrs.get('url', file),
                'description': attrs.get('description', ''),
                'custom1_name': attrs.get('custom1-name', ''),
                'custom1_options': attrs.get('custom1-options', ''),
                'custom2_name': attrs.get('custom2-name', ''),
                'custom2_options': attrs.get('custom2-options', ''),
                'image': attrs.get('image', img_url)
            }

with open("products.js", "w") as f:
    f.write("const window_products = " + json.dumps(products, indent=2) + ";\n")
    f.write("if (typeof window !== 'undefined') window.produtos = window_products;")

print(f"Extracted {len(products)} products into products.js")
