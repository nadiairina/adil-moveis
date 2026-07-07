import os
import re
import json

html_files = ["quartos.html", "salas.html", "cozinha.html", "colchoes.html", "kids.html", "escritorio.html", "complementos.html", "conjuntos.html"]

products = {}

attr_pattern = re.compile(r'data-item-([a-zA-Z0-9_-]+)="([^"]*)"')

for file in html_files:
    if not os.path.exists(file): continue
    with open(file, "r") as f:
        content = f.read()
    
    cards = re.split(r'(class="[^"]*product[^"]*"|class="[^"]*group[^"]*bg-\[\#FDFBF7\])', content)
    
    if len(cards) == 1:
        continue
        
    new_content = cards[0]
    
    for i in range(1, len(cards), 2):
        class_attr = cards[i]
        card_body = cards[i+1]
        
        if 'snipcart-add-item' not in card_body:
            new_content += class_attr + card_body
            continue
            
        btn_match = re.search(r'<button[^>]*snipcart-add-item[^>]*>(.*?)</button>', card_body, re.DOTALL)
        if not btn_match:
            new_content += class_attr + card_body
            continue
            
        btn_tag = btn_match.group(0)
        attrs = dict(attr_pattern.findall(btn_tag))
        
        if 'id' in attrs:
            pid = attrs['id']
            img_match = re.search(r'<img[^>]*src="([^"]+)"', card_body)
            img_url = img_match.group(1) if img_match else 'images/logo.png'
            if "feather=\"image\"" in card_body and not img_match:
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
            
            # Replace the button with a normal link
            new_btn = f'<a href="produto-detalhe.html?id={pid}" class="mt-auto bg-black text-white w-full py-3 text-[10px] font-bold uppercase tracking-wider hover:bg-[#C8B598] transition-colors rounded shadow-sm flex items-center justify-center"><i data-feather="eye" class="w-4 h-4 mr-2"></i> Ver Detalhes</a>'
            card_body = card_body.replace(btn_tag, new_btn)
            
            # If the card contains an image block, wrap it in a link to PDP
            if img_match:
                img_tag_full = img_match.group(0)
                if f'<a href="produto-detalhe.html?id={pid}">{img_tag_full}</a>' not in card_body:
                    new_img_tag = f'<a href="produto-detalhe.html?id={pid}" class="block w-full h-full">{img_tag_full}</a>'
                    card_body = card_body.replace(img_tag_full, new_img_tag)
                
        new_content += class_attr + card_body
        
    with open(file, "w") as f:
        f.write(new_content)

with open("products.js", "w") as f:
    f.write("const window_products = " + json.dumps(products, indent=2) + ";\n")
    f.write("if (typeof window !== 'undefined') window.produtos = window_products;")

print(f"Extracted {len(products)} products into products.js and updated HTML files.")
