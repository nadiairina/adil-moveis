import pandas as pd
import json

excel_file = '../Excel de produtos - Site-finalporagora.xlsx'
xls = pd.ExcelFile(excel_file)
df = pd.read_excel(xls, sheet_name='Folha1')

# Define the keywords to match
keywords = {
    'sofas': ['Trevor', 'Robson', 'Amazónia', 'Argo', 'Eros', 'Daytona', 'Orly', 'Alvin', 'George', 'Mónika', 'Megan', 'Robbie', 'Mistik', 'Philipe', 'Ozil'],
    'cadeiroes': ['Sirio', 'Fredy', 'Connor', 'Lion', 'Dover', 'Stick', 'Star'],
    'cadeiras': ['Charly', 'Moon', 'Paris', 'Sagres', 'Madrid', 'Milão', 'Chiado', 'Viena'],
    'salas': ['Linha Malmo', 'Linha Madrid', 'Linha Paris', 'Linha Chiado'],
    'quartos': ['Cama casal simples com estrado', 'Módulo', 'Cama estofada', 'Cabeceira Estofada', 'Sommier', 'Roupeiro', 'Estrado Metálico', 'Jones']
}

products = {}
product_id_counter = 1

def generate_id(cat, name):
    global product_id_counter
    pid = f"{cat}-{product_id_counter}"
    product_id_counter += 1
    return pid

for index, row in df.iterrows():
    row_str = " ".join([str(x) for x in row.values if pd.notna(x)])
    
    category = None
    for cat, kw_list in keywords.items():
        if any(kw.lower() in row_str.lower() for kw in kw_list):
            category = cat
            break
            
    if category:
        # Extract name (usually first or second non-empty cell)
        cells = [str(x) for x in row.values if pd.notna(x)]
        if not cells:
            continue
        name = cells[0] if len(cells) == 1 else f"{cells[0]} {cells[1]}"
        if len(name) > 100: name = name[:100]
        
        # Build product
        pid = generate_id(category, name)
        products[pid] = {
            "id": pid,
            "name": name,
            "price": 0.0,
            "url": f"{category}.html",
            "description": "Cores e medidas personalizáveis. Preço sob consulta.",
            "custom1_name": "Dimensões",
            "custom1_options": "Standard[+0.00]|Personalizado (sob consulta)[+0.00]",
            "custom2_name": "Tecido / Cor",
            "custom2_options": "Ver Catálogo na Loja[+0.00]",
            "image": "images/sem-imagem.svg"
        }

with open('new_products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")
print(f"Generated {len(products)} products in new_products.js")
