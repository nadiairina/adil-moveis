import requests
from bs4 import BeautifulSoup

def get_yahoo_image(query):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = f"https://images.search.yahoo.com/search/images?p={query}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    # Yahoo images usually store the URL in a data attribute
    for li in soup.find_all("li", class_="ld"):
        img = li.find("img")
        if img:
            src = img.get("data-src") or img.get("src")
            if src and "yimg" not in src:
                return src
            # Also sometimes the URL is in the anchor href
            a = li.find("a")
            if a and a.get("href"):
                # parse the imgurl from href?
                pass
    # If standard parse fails, regex for imgurl
    import re
    match = re.search(r'imgurl=(http[^&]+)', res.text)
    if match:
        import urllib.parse
        return urllib.parse.unquote(match.group(1))
    return None

print(get_yahoo_image("Sofá Trevor Lourini"))
