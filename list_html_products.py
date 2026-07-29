from bs4 import BeautifulSoup
import glob

html_files = ['quartos.html', 'salas.html', 'sofas.html', 'colchoes.html']

for file in html_files:
    print(f"\n--- {file} ---")
    try:
        with open(file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
        products = soup.find_all('a', class_='product')
        for p in products:
            h3 = p.find('h3')
            if h3:
                print(f"Product: {h3.text.strip()}")
    except Exception as e:
        print(f"Error reading {file}: {e}")
