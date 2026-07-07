import re

with open('empresa.html', 'r', encoding='utf-8') as f:
    empresa_content = f.read()

# Extract the history blocks
# From "<!-- Story Section -->" to "<!-- Values & Brands -->"
match = re.search(r'(<!-- Story Section -->.*?)(?=<!-- Values & Brands -->)', empresa_content, re.DOTALL)
if match:
    history_block = match.group(1)
    
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    target_string = "<!-- 8-GRID CATEGORIAS (Pedido da Cliente) -->"
    
    if "UMA TRADIÇÃO FAMILIAR" not in index_content:
        new_index = index_content.replace(target_string, history_block + "\n" + target_string)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_index)
        print("Injected history block successfully.")
    else:
        print("History block already present.")
else:
    print("Could not extract history block.")
