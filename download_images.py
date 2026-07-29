import json
import time
import requests
import os
from duckduckgo_search import DDGS

if not os.path.exists('images/produtos'):
    os.makedirs('images/produtos')

ddgs = DDGS()

with open('products.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace('const window_products = ', '').rstrip(';\n')
products = json.loads(json_str)

def download_image(url, save_path):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        pass
    return False

for pid, p in products.items():
    if 'sem-imagem' not in p['image']:
        continue # Already has an image
    
    query = p['name']
    if 'Louro' in query:
        query = query.replace('Louro', 'Lourini')
    else:
        query += " Lourini" # Adding Lourini to get better matches
        
    print(f"Searching for: {query}")
    try:
        results = ddgs.images(query, max_results=3)
        if results:
            for res in results:
                img_url = res['image']
                ext = img_url.split('.')[-1].split('?')[0]
                if len(ext) > 4 or not ext.isalnum():
                    ext = 'jpg' # fallback
                
                save_path = f"images/produtos/{pid}.{ext}"
                if download_image(img_url, save_path):
                    p['image'] = save_path
                    print(f"Downloaded: {save_path}")
                    break
        else:
            print(f"No results for {query}")
    except Exception as e:
        print(f"Search failed for {query}: {e}")
        
    time.sleep(1) # Be nice to DDG API

with open('products.js', 'w', encoding='utf-8') as f:
    f.write("const window_products = ")
    json.dump(products, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print("Done processing products.js")
