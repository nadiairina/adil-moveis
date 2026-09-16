import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine a good title
    title = "Adil Móveis | Loja de Mobiliário"
    if "quartos.html" in filepath: title = "Quartos e Camas de Casal | Adil Móveis"
    elif "salas.html" in filepath: title = "Salas e Sofás | Adil Móveis"
    elif "colchoes.html" in filepath: title = "Colchões e Almofadas | Adil Móveis"
    elif "kids.html" in filepath: title = "Quartos de Criança e Juvenil | Adil Móveis"
    elif "packs.html" in filepath: title = "Packs de Mobiliário | Adil Móveis"
    elif "contactos.html" in filepath: title = "Contactos e Lojas no Feijó | Adil Móveis"
    elif "index.html" in filepath: title = "Adil Móveis | Loja de Mobiliário em Almada (Feijó)"
    
    # Replace old title
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    
    # Add meta description if not exists
    if '<meta name="description"' not in content:
        desc = "Visite a Adil Móveis no Feijó, Almada. Mais de 37 anos de experiência. Especialistas em quartos, salas, sofás e colchões. Entrega e montagem grátis num raio de 50km."
        meta_tags = f"""<meta name="description" content="{desc}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://adilmoveis.pt/{filepath}" />"""
        # Insert after <meta charset="utf-8"/>
        content = re.sub(r'<meta charset="utf-8"\s*/>', f'<meta charset="utf-8"/>\n{meta_tags}', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("SEO Tags injected.")
