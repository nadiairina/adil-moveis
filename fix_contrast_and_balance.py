import os
import glob
import re

# 1. FIX HERO TEXT CONTRAST IN INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '<!-- OVERLAY ADDED FOR CONTRAST -->' not in content:
    content = content.replace(
        '<img src="https://lourini.pt/app/uploads/2024/07/dennis-32-1200x1200.webp" class="w-full h-full object-cover opacity-40 scale-105 transform origin-center" alt="Hero" data-aos="zoom-out" data-aos-duration="2000">',
        '<img src="https://lourini.pt/app/uploads/2024/07/dennis-32-1200x1200.webp" class="w-full h-full object-cover scale-105 transform origin-center" alt="Hero" data-aos="zoom-out" data-aos-duration="2000">\n          <!-- OVERLAY ADDED FOR CONTRAST -->\n          <div class="absolute inset-0 bg-black/60 z-10"></div>'
    )
    # The text container needs to be higher z-index
    content = content.replace('<div class="relative z-10 text-center px-4 mt-20"', '<div class="relative z-20 text-center px-4 mt-20"')

    # Add text shadow
    content = content.replace('text-white text-5xl md:text-7xl', 'text-white text-5xl md:text-7xl drop-shadow-2xl')
    content = content.replace('text-white/80 text-2xl md:text-3xl', 'text-white/90 text-2xl md:text-3xl drop-shadow-lg')
    content = content.replace('text-white/60 text-lg md:text-xl', 'text-white/80 text-lg md:text-xl drop-shadow-md')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

# 2. BALANCE PRODUCTS ACROSS CATEGORIES (WITHOUT BS4)
TARGET_COUNT = 6
html_files = ['quartos.html', 'salas.html', 'cozinha.html', 'colchoes.html', 'escritorio.html', 'complementos.html', 'kids.html']

PRODUCT_TEMPLATE = """
          <div class="product group cursor-pointer" data-category="all">
            <div class="relative overflow-hidden bg-[#f0f0f0] rounded-xl mb-4 aspect-square">
              <img src="IMAGE_URL" alt="Produto" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
            <h3 class="text-lg font-bold text-black mb-1">PROD_TITLE</h3>
            <p class="text-gray-500 text-sm mb-3">Qualidade Premium</p>
            <button class="snipcart-add-item w-full py-3 border border-black text-black font-bold uppercase tracking-widest text-xs hover:bg-black hover:text-white transition-colors"
              data-item-id="prod-adil"
              data-item-price="0.00"
              data-item-name="PROD_TITLE"
              data-item-image="IMAGE_URL">
              Ver Detalhes
            </button>
          </div>
"""

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find where products are
    grid_start = content.find('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">')
    if grid_start == -1:
        grid_start = content.find('<div class="grid grid-cols-1 md:grid-cols-3 gap-10">')
        
    if grid_start == -1:
        continue
        
    grid_end = content.find('</div>', grid_start) # this is dangerous but we know the structure has nested divs
    # Actually, better to split by '<div class="product'
    
    parts = content.split('<div class="product')
    if len(parts) <= 1:
        continue
        
    pre_products = parts[0]
    
    # Each part except the first one contains a product and maybe trailing tags
    # The last part will contain the closing tags of the grid and main.
    
    products_raw = []
    for p in parts[1:]:
        products_raw.append('<div class="product' + p)
        
    # Rebuild
    current_count = len(products_raw)
    
    if current_count > TARGET_COUNT:
        # We need to preserve the trailing HTML from the last element!
        # The last element in products_raw has all the </div></main><footer> stuff.
        trailing_html = products_raw[-1][products_raw[-1].rfind('</div>') + 6:]
        
        # Keep only the first TARGET_COUNT products
        kept_products = products_raw[:TARGET_COUNT]
        
        # We need to make sure the NEW last product has the trailing html
        last_kept = kept_products[-1]
        
        # find where the product div ends
        # Count divs to find the matching closing div for the product
        
        new_content = pre_products
        for i in range(TARGET_COUNT - 1):
            # for all except the last one, we just need the product code. 
            # wait, the parts splitting is tricky.
            pass
            
    # Actually, a much safer string manipulation strategy:
    # Use regex to find all products
    products = list(re.finditer(r'<div class="product.*?(?=<!--|$)', content, re.DOTALL))
    
    # Just skip if my regex strategy is too complex, I will write a simple marker replacement.
"""

# Let's use a very reliable way: regex to extract all products.
def extract_and_balance():
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the start of the grid
        grid_marker = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">'
        if grid_marker not in content:
            grid_marker = '<div class="grid grid-cols-1 md:grid-cols-3 gap-10">'
            
        if grid_marker not in content:
            continue
            
        grid_idx = content.find(grid_marker) + len(grid_marker)
        
        # Find the end of the grid. Usually right before </main> or <!-- Gallery Modal -->
        end_idx = content.find('</main>')
        if end_idx == -1:
            end_idx = content.find('<!--')
            
        grid_content = content[grid_idx:end_idx]
        
        # Split by <!-- Product --> or '<div class="product'
        # Since I generated these with python, they might not have comments.
        product_blocks = grid_content.split('<div class="product')
        
        if len(product_blocks) < 2:
            continue
            
        # Remove empty strings
        product_blocks = [p for p in product_blocks if p.strip()]
        
        current_count = len(product_blocks)
        
        if current_count == TARGET_COUNT:
            continue
            
        new_grid_content = ""
        
        if current_count > TARGET_COUNT:
            # Keep first 6
            for i in range(TARGET_COUNT):
                new_grid_content += '<div class="product' + product_blocks[i]
                
            # The last block in product_blocks might contain closing tags for the grid container itself
            # Wait, no. The closing tags are at the very end of the LAST block.
            last_original_block = product_blocks[-1]
            # Find where the product ends. Usually after its closing </div>
            # We can just extract everything after the last </div>
            
            # This is risky. Let's just do a simple string replace for the ones that have 8 items.
            pass

extract_and_balance()
