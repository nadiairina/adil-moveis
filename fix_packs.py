import os

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
packs_path = os.path.join(directory, "packs.html")
salas_path = os.path.join(directory, "salas.html")

with open(salas_path, 'r', encoding='utf-8') as f:
    salas_content = f.read()

with open(packs_path, 'r', encoding='utf-8') as f:
    packs_content = f.read()

# Extract from salas.html:
# 1. footer starting at </main>
# 2. everything up to <!-- Snipcart Configuration -->
footer_start = salas_content.find('</main>')
snipcart_start = salas_content.find('<!-- Snipcart Configuration -->')

if footer_start != -1 and snipcart_start != -1:
    footer_code = salas_content[footer_start:snipcart_start]

    # In packs.html, replace everything from <!-- Snipcart Configuration --> with the footer + snipcart
    packs_snipcart = packs_content.find('<!-- Snipcart Configuration -->')
    
    # We also need to add </main> but packs.html doesn't have <main>. 
    # Let's check if it has <main>.
    has_main = '<main' in packs_content
    
    if packs_snipcart != -1:
        new_packs = packs_content[:packs_snipcart] 
        if not has_main:
            # If it doesn't have <main>, we should remove the </main> from footer_code
            footer_code = footer_code.replace('</main>', '')
        
        new_packs += footer_code + packs_content[packs_snipcart:]
        
        with open(packs_path, 'w', encoding='utf-8') as f:
            f.write(new_packs)
        print("Fixed packs.html")

