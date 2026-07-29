import requests
from bs4 import BeautifulSoup
import json
import os
import urllib.parse

# Setup output dir
os.makedirs('images/produtos', exist_ok=True)

with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()
products = json.loads(content.replace('const window_products = ', '').rstrip(';\n'))

def search_lourini(product_name):
    query = product_name.replace('Sofá ', '').replace('Cadeira ', '').replace('Lourini', '').strip()
    # Lourini search URL
    url = f"https://lourini.pt/?s={urllib.parse.quote(query)}&post_type=product"
    try:
        res = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Find product image in search results
        # Usually WooCommerce uses 'img.attachment-woocommerce_thumbnail'
        img = soup.find('img', class_='attachment-woocommerce_thumbnail')
        if img and img.get('src'):
            return img.get('src')
        
        # If not, find any img inside 'product' or 'entry-summary'
        imgs = soup.find_all('img')
        for i in imgs:
            src = i.get('src')
            if src and 'uploads' in src and query.lower() in src.lower():
                return src
    except Exception as e:
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

found_count = 0
for pid, p in products.items():
    if 'sem-imagem' not in p['image']:
        continue
    
    img_url = search_lourini(p['name'])
    if img_url:
        ext = img_url.split('.')[-1].split('?')[0]
        if len(ext) > 4 or not ext.isalnum(): ext = 'jpg'
        save_path = f"images/produtos/{pid}.{ext}"
        if download_image(img_url, save_path):
            p['image'] = save_path
            print(f"Downloaded {p['name']}: {save_path}")
            found_count += 1
        else:
            print(f"Failed download {p['name']}")
    else:
        print(f"Not found {p['name']}")

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Total downloaded: {found_count}")
