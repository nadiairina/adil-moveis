import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Eyebrow text
    content = content.replace('CAMPANHAS &amp; NOVIDADES', 'OFERTA DE BOAS-VINDAS')
    content = content.replace('CAMPANHAS & NOVIDADES', 'OFERTA DE BOAS-VINDAS')
    
    # 2. Title
    content = content.replace('Acesso a Campanhas &amp; Novidades · Ganhe 10% de Desconto', 'Ganhe 10% de Desconto na Sua Primeira Compra')
    content = content.replace('Acesso a Campanhas & Novidades · Ganhe 10% de Desconto', 'Ganhe 10% de Desconto na Sua Primeira Compra')
    
    # 3. Paragraph
    content = content.replace('Envie-nos uma mensagem no WhatsApp para ter acesso a novidades exclusivas e receber um vale de 10% de desconto na sua primeira compra!', 'Envie-nos uma mensagem no WhatsApp para receber o seu vale de 10% de desconto, válido para a sua primeira compra na nossa loja física!')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

