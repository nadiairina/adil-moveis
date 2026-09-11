import os
import bs4

def get_category_quartos(name):
    name = name.lower()
    if 'mesa' in name and 'cabeceira' in name:
        return 'mesasCabeceira'
    if 'cabeceira' in name:
        return 'cabeceiras'
    if 'cama' in name:
        return 'camas'
    if 'cómoda' in name or 'comoda' in name:
        return 'comodas'
    if 'camiseiro' in name:
        return 'camiseiros'
    if 'sommier' in name:
        return 'sommiers'
    return 'all'

def get_category_salas(name):
    name = name.lower()
    if 'sofá' in name or 'sofa' in name:
        return 'sofas'
    if 'cadeirão' in name or 'cadeirao' in name or 'poltrona' in name:
        return 'cadeiroes'
    if 'mesa' in name or 'cadeira' in name or 'banqueta' in name or 'banco' in name:
        return 'mesasEcadeiras'
    if 'móvel' in name or 'movel' in name or 'aparador' in name or 'estante' in name or 'vitrine' in name or 'sapateira' in name or 'secretária' in name or 'secretaria' in name or 'base tv' in name or 'prateleira' in name:
        return 'moveis'
    return 'all'

def get_category_colchoes(name):
    name = name.lower()
    if 'colchão' in name or 'colchao' in name:
        return 'colchoes'
    return 'complementos'

def fix_file(filepath, get_category_func):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    
    products = soup.find_all('a', class_=lambda c: c and 'product' in c)
    for p in products:
        h3 = p.find('h3')
        if not h3:
            continue
        name = h3.text.strip()
        cat = get_category_func(name)
        p['data-category'] = cat
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Fixed {filepath}")

fix_file('quartos.html', get_category_quartos)
fix_file('salas.html', get_category_salas)
fix_file('colchoes.html', get_category_colchoes)
