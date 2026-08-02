import requests
from bs4 import BeautifulSoup
import urllib.parse

query = "Robson"
url = f"https://lourini.pt/?s={urllib.parse.quote(query)}&post_type=product"
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')

gallery = soup.find_all('div', class_='woocommerce-product-gallery__image')
for g in gallery:
    a_tag = g.find('a')
    if a_tag:
        print("Gallery image:", a_tag.get('href'))
