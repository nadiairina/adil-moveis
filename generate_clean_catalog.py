import pandas as pd
import json

excel_file = '../Excel de produtos - Site-finalporagora.xlsx'
xls = pd.ExcelFile(excel_file)
df = pd.read_excel(xls, sheet_name='Folha1')

# Define the exact names we want to match from the OCR
wanted_sofas = ['Trevor', 'Robson', 'Amazónia', 'Argo', 'Eros', 'Daytona', 'Orly', 'Alvin', 'George', 'Mónika', 'Megan', 'Robbie', 'Mistik', 'Philipe', 'Ozil']
wanted_cadeiroes = ['Sirio', 'Fredy', 'Connor', 'Lion', 'Dover', 'Stick', 'Star']
wanted_cadeiras = ['Charly', 'Moon', 'Paris', 'Sagres', 'Madrid', 'Milão', 'Chiado', 'Viena']
wanted_salas = ['Linha Malmo', 'Linha Madrid', 'Linha Paris', 'Linha Chiado']
wanted_quartos = ['Cama casal', 'Mesa cabeceira', 'Cómoda', 'Camiseiro', 'Estrado Metálico', 'Jones']

products = {}
id_counter = 1

def add_product(category, url, name, description=""):
    global id_counter
    pid = f"{url.replace('.html', '')}-{id_counter}"
    id_counter += 1
    products[pid] = {
        "id": pid,
        "name": name,
        "price": 0.0,
        "url": url,
        "category": category,
        "description": description or "Cores e medidas personalizáveis. Preço sob consulta.",
        "custom1_name": "Dimensões",
        "custom1_options": "Standard[+0.00]|Personalizado (sob consulta)[+0.00]",
        "custom2_name": "Tecido / Cor",
        "custom2_options": "Ver Catálogo na Loja[+0.00]",
        "image": "images/sem-imagem.svg"
    }

# For sofas
for s in wanted_sofas:
    add_product("Sofás", "sofas.html", f"Sofá {s}")
for c in wanted_cadeiroes:
    add_product("Cadeirões", "sofas.html", f"Cadeirão {c}")
for c in wanted_cadeiras:
    add_product("Cadeiras", "salas.html", f"Cadeira {c}")
for s in wanted_salas:
    add_product("Salas", "salas.html", f"Sala {s} (Composição)")
for q in wanted_quartos:
    add_product("Quartos", "quartos.html", f"Quarto Louro - {q}")

# Additional known highlights from OCR
add_product("Quartos", "quartos.html", "Cabeceira Jones com laterais")
add_product("Quartos", "quartos.html", "Cama Casal Paris")
add_product("Quartos", "quartos.html", "Cómoda Paris")
add_product("Quartos", "quartos.html", "Camiseiro Paris")
add_product("Quartos", "quartos.html", "Mesa de Cabeceira Paris")
add_product("Quartos", "quartos.html", "Estrado Metálico")

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Generated {len(products)} products in products.js")
