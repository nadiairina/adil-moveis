import re

# 1. Update products.js
js_path = '/Users/nadiairina/Desktop/adil móveis/adil-moveis/products.js'

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Find the end of window_products (just before the closing }; and window.produtos assignment)
# The file ends with:
#   }
# };
# 
# if (typeof window !== 'undefined') {
#   window.produtos = window_products;
# }

packs_data = """,
  "pack-1": {
    "id": "pack-1",
    "name": "Pack Sala de Sonho",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Sofá + Móvel de TV. Mobiliário Lourini de alta qualidade. Cores, acabamentos e tecidos personalizáveis na nossa loja física.",
    "custom1_name": "Opções de Sofá",
    "custom1_options": "Standard[+0.00]|Chaise Longue (sob consulta)[+0.00]",
    "custom2_name": "Tecido / Cor",
    "custom2_options": "Ver Catálogo de Tecidos[+0.00]",
    "image": "images/sem-imagem.svg"
  },
  "pack-2": {
    "id": "pack-2",
    "name": "Pack Sala de Sonho Premium",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Sofá + Mesa de Centro + Móvel de TV. Mobiliário Lourini de alta qualidade. Cores, acabamentos e tecidos personalizáveis na nossa loja física.",
    "custom1_name": "Opções de Sofá",
    "custom1_options": "Standard[+0.00]|Chaise Longue (sob consulta)[+0.00]",
    "custom2_name": "Tecido / Cor",
    "custom2_options": "Ver Catálogo de Tecidos[+0.00]",
    "image": "images/sem-imagem.svg"
  },
  "pack-3": {
    "id": "pack-3",
    "name": "Pack Aconchego Essencial",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Cama de Casal + Colchão + Almofadas. Mobiliário Lourini de alta qualidade e conforto superior.",
    "custom1_name": "Medida do Colchão",
    "custom1_options": "140x190cm[+0.00]|150x190cm[+0.00]|160x200cm[+0.00]",
    "custom2_name": "Tipo de Cama",
    "custom2_options": "Estofada[+0.00]|Madeira[+0.00]",
    "image": "images/sem-imagem.svg"
  },
  "pack-4": {
    "id": "pack-4",
    "name": "Pack À Mesa",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Mesa de Refeição + Cadeiras. Perfeito para momentos de convívio em família. Medidas e acabamentos personalizáveis.",
    "custom1_name": "Número de Cadeiras",
    "custom1_options": "4 Cadeiras[+0.00]|6 Cadeiras (sob consulta)[+0.00]",
    "custom2_name": "Mesa Extensível",
    "custom2_options": "Não[+0.00]|Sim (sob consulta)[+0.00]",
    "image": "images/sem-imagem.svg"
  },
  "pack-5": {
    "id": "pack-5",
    "name": "Pack Sonhos Tranquilos",
    "price": 0.0,
    "url": "packs.html",
    "description": "Conjunto completo composto por: Sommier de Casal + Cabeceira Estofada + Colchão. Conforto e elegância garantidos para o seu quarto.",
    "custom1_name": "Sommier Elevatório (Arrumação)",
    "custom1_options": "Fixo[+0.00]|Elevatório (sob consulta)[+0.00]",
    "custom2_name": "Medidas",
    "custom2_options": "140x190cm[+0.00]|150x190cm[+0.00]|160x200cm[+0.00]",
    "image": "images/sem-imagem.svg"
  }
"""

# Let's insert the packs before the last closing brace
# Search for:
#   }
# };
# 
# if (typeof window !== 'undefined') {

target = """  }
};

if (typeof window !== 'undefined') {"""

replacement = """  }""" + packs_data + """};

if (typeof window !== 'undefined') {"""

if target in js_content:
    js_content = js_content.replace(target, replacement)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("products.js updated successfully.")
else:
    print("Target not found in products.js!")


# 2. Update packs.html to reflect the real packs
packs_html_path = '/Users/nadiairina/Desktop/adil móveis/adil-moveis/packs.html'

with open(packs_html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's replace the first 5 boxes
# Box 1
html = html.replace(
    'data-category="quarto" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Especial Quarto Ref. 1"',
    'data-category="sala" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Sala de Sonho"'
)
html = html.replace(
    'Pack Quarto Ref. 1</h3>',
    'Pack Sala de Sonho</h3>'
)

# Box 2
html = html.replace(
    'data-category="sala" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Especial Sala de Estar Ref. 2"',
    'data-category="sala" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Sala de Sonho Premium"'
)
html = html.replace(
    'Pack Sala de Estar Ref. 2</h3>',
    'Pack Sala de Sonho Premium</h3>'
)

# Box 3
html = html.replace(
    'data-category="casal" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Especial Casal Completo Ref. 3"',
    'data-category="quarto" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Aconchego Essencial"'
)
html = html.replace(
    'Pack Casal Completo Ref. 3</h3>',
    'Pack Aconchego Essencial</h3>'
)

# Box 4
html = html.replace(
    'data-category="quarto" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Especial Quarto Ref. 4"',
    'data-category="sala" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack À Mesa"'
)
html = html.replace(
    'Pack Quarto Ref. 4</h3>',
    'Pack À Mesa</h3>'
)

# Box 5
html = html.replace(
    'data-category="sala" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Especial Sala de Estar Ref. 5"',
    'data-category="casal" style="text-decoration:none; color:inherit;">\n              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">\n                <img src="images/sem-imagem.svg" alt="Pack Sonhos Tranquilos"'
)
html = html.replace(
    'Pack Sala de Estar Ref. 5</h3>',
    'Pack Sonhos Tranquilos</h3>'
)

with open(packs_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("packs.html updated successfully.")
