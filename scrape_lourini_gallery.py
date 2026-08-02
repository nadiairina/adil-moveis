import requests
from bs4 import BeautifulSoup
import json
import os
import urllib.parse
import re

os.makedirs('images/produtos', exist_ok=True)

with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()
products = json.loads(content.replace('const window_products = ', '').rstrip(';\n'))

def get_core_query(name):
    name = re.sub(r'\(Composição\)', '', name).strip()
    name = name.replace('Sala Linha', '').strip()
    name = name.replace('Quarto Louro -', '').strip()
    name = name.replace('Quarto Louro', '').strip()
    name = name.replace('Sofá', '').strip()
    name = name.replace('Cadeirão', '').strip()
    name = name.replace('Cadeira', '').strip()
    name = name.replace('Linha', '').strip()
    return name.strip()

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

def extract_gallery(soup):
    gallery_urls = []
    gallery = soup.find_all('div', class_='woocommerce-product-gallery__image')
    for g in gallery:
        a_tag = g.find('a')
        if a_tag and a_tag.get('href') and a_tag.get('href') not in gallery_urls:
            gallery_urls.append(a_tag.get('href'))
    return gallery_urls

found_count = 0
for pid, p in products.items():
    if 'gallery' in p and len(p['gallery']) > 1:
        continue # Already processed
        
    query = get_core_query(p['name'])
    if not query:
        continue
        
    print(f"Searching gallery for: '{query}'")
    url = f"https://lourini.pt/?s={urllib.parse.quote(query)}&post_type=product"
    try:
        res = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        gallery_urls = extract_gallery(soup)
        
        if not gallery_urls:
            # Maybe it didn't redirect, try to find the first product link
            product_links = soup.find_all('a', class_='woocommerce-LoopProduct-link')
            for link in product_links:
                href = link.get('href')
                if href:
                    p_res = requests.get(href, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                    p_soup = BeautifulSoup(p_res.text, 'html.parser')
                    gallery_urls = extract_gallery(p_soup)
                    if gallery_urls:
                        break
        
        if gallery_urls:
            print(f"  -> Found {len(gallery_urls)} images")
            local_gallery = []
            
            # If the product already has a main image, ensure we don't duplicate or we can just replace the gallery entirely.
            # It's better to just download them all and set as the new gallery.
            for idx, img_url in enumerate(gallery_urls):
                ext = img_url.split('.')[-1].split('?')[0]
                if len(ext) > 4 or not ext.isalnum(): ext = 'jpg'
                save_path = f"images/produtos/{pid}_gallery_{idx}.{ext}"
                if download_image(img_url, save_path):
                    local_gallery.append(save_path)
                    
            if local_gallery:
                # Set the main image to the first one in the gallery
                p['image'] = local_gallery[0]
                p['gallery'] = local_gallery
                found_count += 1
                
                # Save progressively just in case
                with open('products.js', 'w', encoding='utf-8') as f:
                    f.write("const window_products = ")
                    json.dump(products, f, indent=2, ensure_ascii=False)
                    f.write(";\n")
    except Exception as e:
        print("  -> Error:", e)

print(f"Updated {found_count} products with galleries.")
