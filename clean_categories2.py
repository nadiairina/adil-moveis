import os
import re

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
categories = ["quartos.html", "salas.html", "colchoes.html", "kids.html", "escritorio.html", "complementos.html", "packs.html"]

for file in categories:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the section containing the products
    # They are always inside <main> and before the newsletter section or footer.
    # We can just find all products in the file.
    all_matches = list(re.finditer(r'<a href="produto-detalhe\.html[^>]*class="product[\s\S]*?</a>', content))
    
    if len(all_matches) > 20:
        print(f"{file} has {len(all_matches)} products. Keeping only the first 20.")
        
        # The end of the 20th product:
        keep_until = all_matches[19].end()
        
        # We want to remove everything from here until the end of the last product
        remove_until = all_matches[-1].end()
        
        new_content = content[:keep_until] + "\n          " + content[remove_until:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(f"{file} has {len(all_matches)} products.")

print("Cleanup complete.")
