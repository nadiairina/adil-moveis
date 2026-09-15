import os, glob, re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace raw HTML forms
    form_regex = r'<form style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center; max-width:500px; margin:0 auto;" action="https://formsubmit\.co/adil\.moveis@hotmail\.com" method="POST">.*?<\/form>'
    new_btn = r'<a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20receber%20o%20meu%20cup%C3%A3o%20de%2010%25%20de%20desconto." target="_blank" rel="noopener" style="display:inline-block; background:#1a1a1a; color:#fff; padding:15px 30px; font-weight:bold; letter-spacing:0.1em; text-transform:uppercase; font-size:13px; border-radius:4px; text-decoration:none; transition:background 0.3s;" onmouseover="this.style.background=\'#333\'" onmouseout="this.style.background=\'#1a1a1a\'">Pedir Cupão no WhatsApp ➔</a>'
    
    content = re.sub(form_regex, new_btn, content, flags=re.DOTALL)

    # 2. Update floating bar Agendar Visita to open WhatsApp directly
    content = re.sub(r'href="contactos\.html\?agendar=true"', r'href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Quero%20agendar%20uma%20visita%20%C3%A0%20loja%3A%0A%0ANome%3A%0ADia%20e%20Hora%3A%0AProcuro%20por%3A"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

