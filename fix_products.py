import json
import re

with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()

# products.js format is "const window_products = { ... };\n"
# Extract the JSON part
json_str = content.replace('const window_products = ', '').rstrip(';\n')
products = json.loads(json_str)

for pid, p in products.items():
    if p['url'] == 'sofas.html':
        p['url'] = 'salas.html'
    # Check if this is the kids line
    if 'kids' in p['name'].lower() or 'play' in p['name'].lower():
        p['url'] = 'kids.html'

# Also let's add the "Linha Play (Kids)" product since the user mentioned 1 kids line
products["quartos-kids"] = {
    "id": "quartos-kids",
    "name": "Quarto Louro - Linha Play (Kids)",
    "price": 0.0,
    "url": "kids.html",
    "category": "Quartos",
    "description": "Cores e medidas personalizáveis. Preço sob consulta.",
    "custom1_name": "Dimensões",
    "custom1_options": "Standard[+0.00]|Personalizado (sob consulta)[+0.00]",
    "custom2_name": "Tecido / Cor",
    "custom2_options": "Ver Catálogo na Loja[+0.00]",
    "image": "images/sem-imagem.svg"
}

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print("Fixed products.js URLs and added Kids item")
