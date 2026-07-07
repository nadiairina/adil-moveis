import os
import re
import json

base_dir = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
html_files = ["quartos.html", "kids.html", "escritorio.html", "complementos.html"]

def slugify(text):
    text = text.lower()
    text = text.replace('á', 'a').replace('à', 'a').replace('ã', 'a').replace('â', 'a')
    text = text.replace('é', 'e').replace('ê', 'e').replace('í', 'i').replace('ó', 'o').replace('ô', 'o').replace('õ', 'o')
    text = text.replace('ú', 'u').replace('ç', 'c')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

for file in html_files:
    path = os.path.join(base_dir, file)
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to replace <div class="product..." ...> with <a href="..." class="product..." ...>
    # The end of the block is </div> which corresponds to that div. This is tricky with regex.
    # Actually, we can just replace `<div class="product` with `<a href="produto-detalhe.html?id=ID" class="product`
    # How to find the ID? We can look ahead to find the Linha and Product Name.
    
    blocks = re.split(r'(<div class="product\s+[^>]*>)', content)
    new_content = blocks[0]
    
    for i in range(1, len(blocks), 2):
        div_start = blocks[i]
        block_content = blocks[i+1]
        
        # Extract Linha
        linha_match = re.search(r'<span class="[^"]*">([^<]+)</span>', block_content)
        linha = linha_match.group(1).strip() if linha_match else ""
        
        # Extract Name
        name_match = re.search(r'<h3 class="[^"]*">([^<]+)</h3>', block_content)
        name = name_match.group(1).strip() if name_match else ""
        
        # Some items don't have Linha in the span, just name.
        if linha:
            full_name = f"{linha} {name}"
        else:
            full_name = name
            
        product_id = slugify(full_name)
        # special case adjustments to match products.js
        if "cama-casal" in product_id and not "gavetas" in product_id:
            # Some IDs have -cama-casal but the name is "Cama casal simples"
            pass
        
        # Let's generate ID similarly to what we see: "linha-malmo-modulo-1-gaveta-60"
        # Full name was "Linha Malmo Módulo 1 gaveta 60" => "linha-malmo-modulo-1-gaveta-60"
        
        # Actually, replace `<div class="product` with `<a href="produto-detalhe.html?id={product_id}" class="product block`
        # And replace the matching closing </div> with </a>
        # Since the product div ends right before the next <div class="product or the end of the grid:
        
        # Find the last </div> before the end of this block
        last_div_idx = block_content.rfind('</div>')
        if last_div_idx != -1:
            block_content = block_content[:last_div_idx] + '</a>' + block_content[last_div_idx+6:]
            
        new_content += f'<a href="produto-detalhe.html?id={product_id}"' + div_start[4:] + block_content
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file}")
