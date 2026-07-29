import json
from bs4 import BeautifulSoup

# 1. Update products.js
with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()
products = json.loads(content.replace('const window_products = ', '').rstrip(';\n'))

for pid, p in products.items():
    if 'Estrado Metálico' in p['name']:
        p['price'] = 50.00
        p['buy_link'] = "#klarna_estrado"
    if 'Pack 4 Cadeiras Charly' in p['name']:
        p['price'] = 120.00
        p['buy_link'] = "#klarna_cadeiras"

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# 2. Update produto-detalhe.html
with open('produto-detalhe.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to add logic for p.buy_link
# Find: btn.dataset.itemName     = p.name;
old_js = "btn.dataset.itemName     = p.name;"
new_js = """btn.dataset.itemName     = p.name;
        if (p.buy_link) {
          btn.href = p.buy_link;
          btn.onclick = null; // Disable add to cart popup
          btn.innerHTML = '<i class="fas fa-shopping-bag mr-2"></i> COMPRAR AGORA';
          btn.style.backgroundColor = '#16a34a'; // Green
        } else {
          btn.href = 'javascript:void(0)';
          btn.innerHTML = '<i class="fas fa-shopping-bag mr-2"></i> Adicionar ao Carrinho';
        }"""

if old_js in html and 'btn.href = p.buy_link;' not in html:
    html = html.replace(old_js, new_js)
    with open('produto-detalhe.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Updated produto-detalhe.html")

