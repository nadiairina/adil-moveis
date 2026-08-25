import urllib.request
import urllib.parse
import json
import re
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def search_ddg_images(query):
    print(f"Searching for: {query}")
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            html = response.read().decode('utf-8')
            # Extract first URL that might contain an image, or just use DuckDuckGo's image search if we can.
            # DDG html doesn't show images directly. Let's try to find an og:image from the first result.
            links = re.findall(r'href="([^"]+)" class="result__url"', html)
            for link in links:
                if link.startswith('//'):
                    link = 'https:' + link
                elif link.startswith('/l/?'):
                    # Parse DDG redirect
                    match = re.search(r'uddg=([^&]+)', link)
                    if match:
                        link = urllib.parse.unquote(match.group(1))
                print(f"  Checking {link}")
                try:
                    req2 = urllib.request.Request(link, headers=headers)
                    with urllib.request.urlopen(req2, context=ctx, timeout=5) as res2:
                        page_html = res2.read().decode('utf-8', errors='ignore')
                        og_img = re.search(r'<meta\s+(?:property|name)="og:image"\s+content="([^"]+)"', page_html, re.I)
                        if og_img:
                            img_url = og_img.group(1)
                            if img_url.startswith('/'):
                                parsed_link = urllib.parse.urlparse(link)
                                img_url = f"{parsed_link.scheme}://{parsed_link.netloc}{img_url}"
                            return img_url
                        # Try to find any large image
                        imgs = re.findall(r'<img[^>]+src="([^"]+)"', page_html, re.I)
                        for img in imgs:
                            if 'logo' not in img.lower() and 'icon' not in img.lower() and ('.jpg' in img.lower() or '.png' in img.lower() or '.webp' in img.lower()):
                                if img.startswith('/'):
                                    parsed_link = urllib.parse.urlparse(link)
                                    img = f"{parsed_link.scheme}://{parsed_link.netloc}{img}"
                                return img
                except Exception as e:
                    print(f"  Error fetching {link}: {e}")
    except Exception as e:
        print(f"Error searching {query}: {e}")
    return None

products = {
    "colchoes-ibiza": "Colchão Molaflex Ibiza",
    "colchoes-faro": "Colchão Molaflex Faro",
    "colchoes-toronto": "Colchão Molaflex Toronto",
    "colchoes-estoril": "Colchão Molaflex Estoril",
    "colchoes-dream": "Colchão Molaflex Dream",
    "colchoes-dubai": "Colchão Molaflex Dubai",
    "colchoes-comp-1": "Almofada Viscoelástica Ergonomia Molaflex",
    "colchoes-comp-2": "Almofada Cervical Molaflex",
    "colchoes-comp-3": "Almofada de Penas Plumagem Molaflex",
    "colchoes-comp-4": "Protetor de Colchão Impermeável Molaflex",
    "colchoes-comp-5": "Capa de Colchão Respirável Molaflex",
    "colchoes-comp-6": "Topper Viscoelástico Conforto Extra Molaflex"
}

out_dir = "/Users/nadiairina/Downloads/adil-moveis-a3bbe83355cd00f6a3e79a0e24e05ba31fc541d9/images/produtos"
os.makedirs(out_dir, exist_ok=True)

for slug, query in products.items():
    img_url = search_ddg_images(query)
    if img_url:
        print(f"Found image for {query}: {img_url}")
        ext = 'jpg'
        if '.png' in img_url.lower(): ext = 'png'
        elif '.webp' in img_url.lower(): ext = 'webp'
        
        filepath = os.path.join(out_dir, f"{slug}.{ext}")
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Saved to {filepath}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
    else:
        print(f"Could not find image for {query}")

