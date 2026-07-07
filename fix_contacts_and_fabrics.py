import os

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix phone numbers
    content = content.replace('912 582 788', '960 209 396')
    content = content.replace('912582788', '960209396')
    
    # Remove 'Guia de Tecidos' links from menus
    # It usually looks like: <a href="tecidos.html"...>TECIDOS</a> or similar
    # Let's just remove the <li><a href="tecidos.html"...>TECIDOS</a></li> block in footer
    content = content.replace('<li><a href="tecidos.html" class="hover:opacity-80 transition-opacity">TECIDOS</a></li>', '')
    # And in mobile menu
    content = content.replace('<a href="tecidos.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color=\'#1a1a1a\'" onmouseout="this.style.color=\'#6b6b6b\'">Guia de Tecidos</a>', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Phones and links updated.")
