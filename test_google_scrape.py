import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def search_google_image(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        # Find all img tags that might have a data-src or src with an actual image URL
        imgs = soup.find_all("img")
        for img in imgs:
            src = img.get("data-src") or img.get("src")
            if src and src.startswith("http") and "gstatic" not in src:
                return src
    except Exception as e:
        print(f"Error: {e}")
    return None

url = search_google_image("Sofá Trevor Lourini")
print(f"Found: {url}")
