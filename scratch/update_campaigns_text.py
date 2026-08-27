import glob

html_files = glob.glob('*.html')
count = 0

old_pill = '<p style="font-family:\'Inter\',sans-serif; font-size:10px; font-weight:700; letter-spacing:0.3em; text-transform:uppercase; color:#C8B598; margin-bottom:1rem;">OFERTA EXCLUSIVA</p>'
new_pill = '<p style="font-family:\'Inter\',sans-serif; font-size:10px; font-weight:700; letter-spacing:0.3em; text-transform:uppercase; color:#C8B598; margin-bottom:1rem;">CAMPANHAS & NOVIDADES</p>'

# Various possible headline variants from recent edits
headlines_to_replace = [
    'Subscreva e receba 10% de desconto na primeira compra (Válido na nossa loja física!)',
    'Subscreva e receba 10% de desconto na primeira compra (Válido online e em loja!)',
    'Subscreva e receba 10% de desconto na primeira compra'
]

new_headline = 'Acesso a Campanhas & Novidades · Ganhe 10% de Desconto'

old_desc = 'Registe o seu e-mail para receber novidades, coleções exclusivas e um vale de 10% de desconto para a sua primeira encomenda de mobiliário.'
new_desc = 'Registe o seu e-mail para ter acesso exclusivo a novidades, novas coleções e receber um vale de 10% de desconto na primeira compra na nossa loja física.'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if old_pill in content:
        content = content.replace(old_pill, new_pill)
        modified = True
        
    for h in headlines_to_replace:
        if h in content:
            content = content.replace(h, new_headline)
            modified = True
            
    if old_desc in content:
        content = content.replace(old_desc, new_desc)
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {file}")

print(f"Total files updated: {count}")
