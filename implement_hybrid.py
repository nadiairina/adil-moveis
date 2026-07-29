import json
import re
from bs4 import BeautifulSoup

# 1. Update products.js
with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()
products = json.loads(content.replace('const window_products = ', '').rstrip(';\n'))

for pid, p in products.items():
    if 'Estrado Metálico' in p['name']:
        p['price'] = "€ 50,00" # Placeholder
        p['buy_link'] = "#"
    if p['name'] == 'Cadeira Charly':
        p['name'] = 'Pack 4 Cadeiras Charly (Bege)'
        p['price'] = "€ 120,00" # Placeholder
        p['buy_link'] = "#"
        p['description'] = "Pack económico de 4 cadeiras Charly estofadas em bege. Prontas a entregar."

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# 2. Update quartos.html and salas.html JS logic
for file in ['quartos.html', 'salas.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We need to replace the price and button rendering logic
    # Currently it is:
    # <p class="text-gray-500 mb-4">${p.description}</p>
    # <a href="https://wa.me/351910000000" target="_blank" class="block w-full text-center bg-gray-900 text-white py-2 rounded hover:bg-gray-800 transition">Pedir Orçamento</a>
    
    old_js = """<p class="text-gray-500 mb-4">${p.description}</p>
                        <a href="https://wa.me/351910000000" target="_blank" class="block w-full text-center bg-gray-900 text-white py-2 rounded hover:bg-gray-800 transition">Pedir Orçamento</a>"""
    
    new_js = """<p class="text-gray-500 mb-4">${p.description}</p>
                        ${p.price 
                            ? `<div class="text-2xl font-bold text-gray-900 mb-4">${p.price}</div>
                               <a href="${p.buy_link || '#'}" class="block w-full text-center bg-green-600 text-white font-bold py-3 rounded-lg shadow-lg hover:bg-green-500 hover:shadow-xl transition transform hover:-translate-y-1">🛒 COMPRAR AGORA</a>` 
                            : `<a href="https://wa.me/351910000000" target="_blank" class="block w-full text-center bg-gray-900 text-white py-2 rounded hover:bg-gray-800 transition">Pedir Orçamento</a>`
                        }"""
    
    if old_js in html:
        html = html.replace(old_js, new_js)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
            print(f"Updated {file}")

# 3. Update colchoes.html
with open('colchoes.html', 'r', encoding='utf-8') as f:
    col_html = f.read()
    soup = BeautifulSoup(col_html, 'html.parser')
    
    # Find all product cards in mattresses
    cards = soup.find_all('div', class_='bg-white')
    for card in cards:
        # Find the title
        title = card.find('h3')
        if title:
            name = title.text.strip()
            # If it's a mattress, add price and buy button
            if name in ['Evolution', 'Freshcool', 'Max Body', 'Airflow']:
                # Ensure we don't add it twice
                if not card.find('div', class_='text-2xl'):
                    # Create the price and button
                    price_div = soup.new_tag('div', attrs={'class': 'text-2xl font-bold text-gray-900 mt-4 mb-2'})
                    price_div.string = "€ 299,00" # Placeholder
                    
                    buy_btn = soup.new_tag('a', href="#", attrs={
                        'class': 'block w-full text-center bg-green-600 text-white font-bold py-3 rounded-lg shadow-lg hover:bg-green-500 hover:shadow-xl transition transform hover:-translate-y-1 mt-2'
                    })
                    buy_btn.string = "🛒 COMPRAR AGORA"
                    
                    # Append them after the description (which is the p tag)
                    p_tag = card.find('p')
                    if p_tag:
                        p_tag.insert_after(buy_btn)
                        p_tag.insert_after(price_div)

    with open('colchoes.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        print("Updated colchoes.html")
