import os
import re

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
categories = ['quartos.html', 'salas.html', 'colchoes.html', 'kids.html', 'escritorio.html', 'cozinha.html', 'complementos.html']

for cat in categories:
    filepath = os.path.join(directory, cat)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix shopping bag size
    content = content.replace('style="width:16px;height:16px;"', 'style="width:20px;height:20px;"')

    # Find the grid section
    grid_start_str = 'class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8"'
    if grid_start_str in content:
        grid_start_idx = content.find(grid_start_str)
        # We need to find all product <a> tags after the grid start.
        # Products are structured as `<a href="produto-detalhe... class="product...`
        
        # A simpler way is to find all products using regex
        # We want to keep the first 20 products and delete the rest.
        
        # Let's split the content into before grid, grid, after grid
        # Actually, let's just find all <a href="produto-detalhe... 
        # But wait, there might be other a tags. 
        # The products have class="product bg-white rounded overflow-hidden block border border-[#E8E3DC] hover:shadow-md transition-shadow relative"
        # Let's use re.split on the product start tag
        product_pattern = r'(<!-- Product Box \d+ -->\s*<a href="produto-detalhe\.html\?id=.*?" class="product.*?</p>\s*</div>\s*</a>)'
        
        parts = re.split(product_pattern, content, flags=re.DOTALL)
        
        # parts will be [non-product, product, non-product, product, ...]
        # We only want the first 20 products.
        
        new_content = ""
        product_count = 0
        for i, part in enumerate(parts):
            if part.strip().startswith('<!-- Product Box'):
                product_count += 1
                if product_count <= 20:
                    new_content += part
            else:
                new_content += part
                
        content = new_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Categories fixed!")
