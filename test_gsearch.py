from googlesearch import search
import requests
from bs4 import BeautifulSoup

def get_image(query):
    try:
        # Search for top 3 pages
        urls = list(search(query, num_results=3))
        for url in urls:
            try:
                res = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(res.text, 'html.parser')
                # Find an image that likely belongs to the product
                # Just grab the biggest image or first og:image
                og_img = soup.find('meta', property='og:image')
                if og_img and og_img.get('content'):
                    return og_img.get('content')
            except:
                pass
    except Exception as e:
        print(e)
    return None

print(get_image("Colchão Evolution Mindol"))
