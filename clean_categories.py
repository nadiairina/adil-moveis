import os
import re

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
categories = ["quartos.html", "salas.html", "colchoes.html", "kids.html", "escritorio.html", "complementos.html"]

for file in categories:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the grid start
    grid_start_str = 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">'
    grid_start = content.find(grid_start_str)
    
    if grid_start != -1:
        grid_start += len(grid_start_str)
        # Find the end of the grid. It usually ends with "</div>\n        </div>\n      </section>"
        grid_end = content.find('</section>', grid_start)
        # to be precise, the grid div ends right before another </div> of the container.
        
        grid_content = content[grid_start:grid_end]
        
        # Split by product tags
        # Each product starts with: <a href="produto-detalhe.html
        products = re.split(r'(<a href="produto-detalhe\.html[^>]*class="product[^>]*>)', grid_content)
        
        # products[0] is whitespace before first product
        # products[1] is the opening tag of product 1
        # products[2] is the content of product 1 + closing </a>
        # products[3] is the opening tag of product 2 ...
        
        new_grid_content = products[0]
        
        product_count = 0
        for i in range(1, len(products), 2):
            if product_count < 20:
                new_grid_content += products[i] + products[i+1]
                product_count += 1
            else:
                pass # skip
                
        # What about the closing divs? 
        # Actually products list might end with some trailing divs like: </a>\n          </div>\n        </div>\n
        # The last chunk in products might contain the closing tags of the grid if it's after the last </a>.
        # Let's extract the closing divs by finding the last </a> in the original grid_content
        last_a_end = grid_content.rfind('</a>')
        if last_a_end != -1:
            trailing = grid_content[last_a_end+4:]
        else:
            trailing = ""
            
        # Re-assemble the 20 products
        final_grid = new_grid_content 
        # wait, the trailing divs are already in products[-1] if we didn't slice them off.
        # Let's check products[-1]
        
        # Safer way: Find all occurrences of product blocks
        # A product block starts with <a href="..." class="product"... and ends with </a>.
        # There might be spaces between them.
        
        # Let's use re.findall or re.finditer to find exactly 20 products
        all_matches = list(re.finditer(r'<a href="produto-detalhe\.html[^>]*class="product[\s\S]*?</a>', grid_content))
        
        if len(all_matches) > 20:
            print(f"{file} has {len(all_matches)} products. Keeping only the first 20.")
            # We want to keep everything from grid_content start to the end of the 20th match
            keep_until = all_matches[19].end()
            # And then we want to keep the trailing tags at the end of the grid_content
            # The trailing tags start after the last match's end
            trailing_start = all_matches[-1].end()
            new_grid = grid_content[:keep_until] + grid_content[trailing_start:]
            
            new_content = content[:grid_start] + new_grid + content[grid_end:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            print(f"{file} has {len(all_matches)} products.")

print("Cleanup complete.")
