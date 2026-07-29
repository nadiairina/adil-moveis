import requests
from bs4 import BeautifulSoup

url = "https://lourini.pt/?s=Trevor&post_type=product"
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')

product_link = soup.find('a', class_='woocommerce-LoopProduct-link')
if product_link:
    print("Found product link:", product_link['href'])
    p_res = requests.get(product_link['href'], headers={'User-Agent': 'Mozilla/5.0'})
    p_soup = BeautifulSoup(p_res.text, 'html.parser')
    
    gallery = p_soup.find_all('div', class_='woocommerce-product-gallery__image')
    for g in gallery:
        img = g.find('img')
        if img:
            print("Gallery img:", img.get('src') or img.get('data-src') or img.get('data-large_image'))
else:
    print("Product link not found")
