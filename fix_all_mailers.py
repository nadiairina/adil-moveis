import os, glob, re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The same regex I used for index.html but applied to all files
    content = re.sub(
        r'<style>\.ml-form-embedContent.*?</div>', 
        r'<a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20receber%20o%20meu%20cup%C3%A3o%20de%2010%25%20de%20desconto." target="_blank" rel="noopener" style="display:inline-block; background:#1a1a1a; color:#fff; padding:15px 30px; font-weight:bold; letter-spacing:0.1em; text-transform:uppercase; font-size:13px; border-radius:4px; text-decoration:none; transition:background 0.3s;" onmouseover="this.style.background=\'#333\'" onmouseout="this.style.background=\'#1a1a1a\'">Pedir Cupão no WhatsApp ➔</a>', 
        content, flags=re.DOTALL
    )
    
    content = re.sub(
        r'Registe o seu e-mail para ter acesso exclusivo a novidades, novas coleções e receber um vale de 10% de desconto na primeira compra na nossa loja física\.', 
        r'Envie-nos uma mensagem no WhatsApp para ter acesso a novidades exclusivas e receber um vale de 10% de desconto na sua primeira compra!', 
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

