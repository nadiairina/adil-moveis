import os
import re

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'

# 1. Delete cozinha.html
cozinha_path = os.path.join(directory, 'cozinha.html')
if os.path.exists(cozinha_path):
    os.remove(cozinha_path)
    print("Deleted cozinha.html")

html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make PACKS ESPECIAIS header button solid gold and high contrast
    old_packs_btn_pattern = r'<a href="packs\.html" class="hidden xl:inline-block" style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:0.2em;color:#C8B598;border:1px solid #C8B598;padding:6px 16px;transition:all 0.3s;border-radius:2px;text-decoration:none;" onmouseover="this\.style\.background=\'#C8B598\';this\.style\.color=\'#ffffff\';" onmouseout="this\.style\.background=\'transparent\';this\.style\.color=\'#C8B598\';">PACKS ESPECIAIS</a>'
    new_packs_btn = '<a href="packs.html" class="hidden xl:inline-block" style="font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:0.2em;color:#ffffff;background:#C8B598;border:1px solid #C8B598;padding:8px 20px;transition:all 0.3s;border-radius:30px;text-decoration:none;box-shadow:0 3px 12px rgba(200,181,152,0.4);" onmouseover="this.style.background=\'#b09e85\';this.style.borderColor=\'#b09e85\';" onmouseout="this.style.background=\'#C8B598\';this.style.borderColor=\'#C8B598\';">PACKS ESPECIAIS</a>'
    content = re.sub(old_packs_btn_pattern, new_packs_btn, content)

    # Make mobile sidebar button solid as well
    # <a href="packs.html" style="font-size:1rem;color:#C8B598;font-weight:700;text-decoration:none;padding:10px 15px;border:2px solid #C8B598;border-radius:25px;display:inline-block;margin-top:10px;text-align:center;transition:all 0.3s;" onmouseover="this.style.background=\'#C8B598\';this.style.color=\'#fff\';" onmouseout="this.style.background=\'transparent\';this.style.color=\'#C8B598\';">✦ Packs Especiais</a>
    old_mobile_btn_pattern = r'<a href="packs\.html" style="font-size:1rem;color:#C8B598;font-weight:700;text-decoration:none;padding:10px 15px;border:2px solid #C8B598;border-radius:25px;display:inline-block;margin-top:10px;text-align:center;transition:all 0.3s;" onmouseover="this\.style\.background=\'#C8B598\';this\.style\.color=\'#fff\';" onmouseout="this\.style\.background=\'transparent\';this\.style\.color=\'#C8B598\';">✦ Packs Especiais</a>'
    new_mobile_btn = '<a href="packs.html" style="font-size:1rem;color:#ffffff;background:#C8B598;font-weight:700;text-decoration:none;padding:10px 20px;border:1px solid #C8B598;border-radius:25px;display:inline-block;margin-top:10px;text-align:center;transition:all 0.3s;box-shadow:0 3px 10px rgba(200,181,152,0.3);" onmouseover="this.style.background=\'#b09e85\';this.style.borderColor=\'#b09e85\';" onmouseout="this.style.background=\'#C8B598\';this.style.borderColor=\'#C8B598\';">✦ Packs Especiais</a>'
    content = re.sub(old_mobile_btn_pattern, new_mobile_btn, content)

    # Remove Cozinha, Escritório and Complementos from sidebar menu
    content = re.sub(r'<a href="cozinha\.html".*?>Cozinhas?</a>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<a href="escritorio\.html".*?>Escritórios?</a>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<a href="complementos\.html".*?>Complementos?</a>', '', content, flags=re.IGNORECASE)

    # Remove from Desktop header menu if there's any reference
    content = re.sub(r'<a href="cozinha\.html".*?>COZINHA</a>', '', content)
    content = re.sub(r'<a href="escritorio\.html".*?>ESCRITÓRIO</a>', '', content)
    content = re.sub(r'<a href="complementos\.html".*?>COMPLEMENTOS</a>', '', content)

    # Remove from Footer list items
    content = re.sub(r'<li><a href="cozinha\.html".*?>COZINHA</a></li>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<li><a href="escritorio\.html".*?>ESCRITÓRIO</a></li>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<li><a href="complementos\.html".*?>COMPLEMENTOS</a></li>', '', content, flags=re.IGNORECASE)

    # Adjust footer padding to make it very compact and minimal (fancy)
    # The footers usually have inline padding or classes. Let's make sure it's py-4 or py-6 instead of py-10
    content = content.replace('class="bg-black text-white py-6"', 'class="bg-black text-white py-4"')
    content = content.replace('padding:1.5rem 0 0.5rem;', 'padding:1rem 0 0.5rem;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleanups completed.")
