import os
import re

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix mobile menu - robust removal of Escritório and Complementos
    # Using regex to remove the <li> or <a> containing Escritório/Complementos in the mobile menu context.
    # The screenshot shows a list of <a> tags in the sidebar. Let's find them.
    content = re.sub(r'<a href="[^"]*escritorio\.html".*?Escritório</a>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<a href="[^"]*complementos\.html".*?Complementos</a>', '', content, flags=re.IGNORECASE)
    # The previous script might have left the surrounding <li> or div. Let's do a wider sweep if needed, 
    # but based on the previous view of the sidebar, it's just raw <a> tags.
    # Let's also remove them if they are wrapped in <li>:
    content = re.sub(r'<li[^>]*>\s*<a href="[^"]*escritorio\.html".*?Escritório</a>\s*</li>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<li[^>]*>\s*<a href="[^"]*complementos\.html".*?Complementos</a>\s*</li>', '', content, flags=re.IGNORECASE)
    
    # Let's also make sure to remove "Guia de Tecidos" if it's still there
    content = re.sub(r'<a href="[^"]*tecidos\.html".*?Tecidos</a>', '', content, flags=re.IGNORECASE)
    
    # 2. Fix the Packs button link (make sure it goes to packs.html, not salas.html)
    # Search for any link that has "Packs Especiais" and ensure href is packs.html
    # Desktop nav:
    content = re.sub(r'<a href="[^"]*"\s+class="[^"]*"\s*>PACKS ESPECIAIS</a>', r'<a href="packs.html" class="text-[11px] font-extrabold text-[#C8B598] hover:text-[#b09e85] tracking-[0.2em] px-4 py-2 border-2 border-[#C8B598] rounded-full shadow-sm hover:shadow-md transition-all" style="background-color:rgba(200,181,152,0.1);">PACKS ESPECIAIS</a>', content)
    
    # Mobile nav (usually ✦ Packs Especiais):
    content = re.sub(r'<a href="[^"]*"\s+style="[^"]*"\s*(onmouseover="[^"]*")?\s*(onmouseout="[^"]*")?\s*>✦ Packs Especiais</a>', r'<a href="packs.html" style="font-size:1rem;color:#C8B598;font-weight:700;text-decoration:none;padding:10px 15px;border:2px solid #C8B598;border-radius:25px;display:inline-block;margin-top:10px;text-align:center;transition:all 0.3s;" onmouseover="this.style.background=\'#C8B598\';this.style.color=\'#fff\';" onmouseout="this.style.background=\'transparent\';this.style.color=\'#C8B598\';">✦ Packs Especiais</a>', content)
    
    # 3. Shrink the footer even more
    # If it has padding:2rem 0 1rem; change to padding:1rem 0 0.5rem;
    content = content.replace('padding:2rem 0 1rem;', 'padding:1.5rem 0 0.5rem;')
    content = content.replace('padding:4rem 0 2rem;', 'padding:1.5rem 0 0.5rem;')
    # If there's margin-bottom:2rem; change to margin-bottom:1rem;
    content = content.replace('margin-bottom:2rem;', 'margin-bottom:1rem;')
    content = content.replace('margin-bottom:3rem;', 'margin-bottom:1rem;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("UI fixes applied.")
