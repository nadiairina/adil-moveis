import requests
from bs4 import BeautifulSoup
import json
import os
import urllib.parse
import re

os.makedirs('images/produtos', exist_ok=True)

def get_yahoo_image(query):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = f"https://images.search.yahoo.com/search/images?p={urllib.parse.quote(query)}"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Try finding the image URL directly in data-src of li > img
        for li in soup.find_all("li", class_="ld"):
            img = li.find("img")
            if img:
                src = img.get("data-src") or img.get("src")
                if src and "yimg" not in src:
                    return src
        
        # Fallback regex
        match = re.search(r'imgurl=(http[^&]+)', res.text)
        if match:
            return urllib.parse.unquote(match.group(1))
    except:
        pass
    return None

def download_image(url, save_path):
    try:
        res = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if res.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(res.content)
            return True
    except:
        pass
    return False

# 1. Update products.js
with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()
products = json.loads(content.replace('const window_products = ', '').rstrip(';\n'))

found_missing = []
still_missing = []

for pid, p in products.items():
    if 'sem-imagem' not in p['image']:
        continue
    
    query = p['name'].replace('Louro', 'Lourini') + ' móveis'
    img_url = get_yahoo_image(query)
    if img_url:
        ext = img_url.split('.')[-1].split('?')[0]
        if len(ext) > 4 or not ext.isalnum(): ext = 'jpg'
        save_path = f"images/produtos/{pid}.{ext}"
        if download_image(img_url, save_path):
            p['image'] = save_path
            found_missing.append(p['name'])
            print(f"Yahoo found: {p['name']}")
        else:
            still_missing.append(p['name'])
    else:
        still_missing.append(p['name'])

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# 2. Update Colchoes
colchoes_queries = [
    ("colchao-evolution.jpg", "Colchão Evolution Mindol"),
    ("colchao-freshcool.jpg", "Colchão Freshcool Molaflex"),
    ("colchao-maxbody.jpg", "Colchão Max Body Bestbed"),
    ("colchao-airflow.jpg", "Colchão Airflow Colmed")
]

for filename, q in colchoes_queries:
    img_url = get_yahoo_image(q)
    if img_url:
        save_path = f"images/produtos/{filename}"
        if download_image(img_url, save_path):
            print(f"Yahoo found Colchão: {q}")

# Let's inject into colchoes.html
with open('colchoes.html', 'r', encoding='utf-8') as f:
    col_html = f.read()

col_html = col_html.replace('images/sem-imagem.svg', 'images/produtos/colchao-evolution.jpg', 1)
col_html = col_html.replace('images/sem-imagem.svg', 'images/produtos/colchao-freshcool.jpg', 1)
col_html = col_html.replace('images/sem-imagem.svg', 'images/produtos/colchao-maxbody.jpg', 1)
col_html = col_html.replace('images/sem-imagem.svg', 'images/produtos/colchao-airflow.jpg', 1)

with open('colchoes.html', 'w', encoding='utf-8') as f:
    f.write(col_html)

print("Found via Yahoo:", found_missing)
print("Still missing:", still_missing)
