import os

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'

# 1. Delete files
files_to_delete = ['escritorio.html', 'complementos.html']
for f in files_to_delete:
    path = os.path.join(directory, f)
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted {f}")

# 2. Update menus in all html files
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Footer links to remove
desktop_links_to_remove = [
    '<li><a href="escritorio.html" class="hover:opacity-80 transition-opacity">ESCRITÓRIO</a></li>',
    '<li><a href="complementos.html" class="hover:opacity-80 transition-opacity">COMPLEMENTOS</a></li>',
    '<li><a href="escritorio.html" class="hover:text-black transition-colors">Escritório</a></li>',
    '<li><a href="complementos.html" class="hover:text-black transition-colors">Complementos</a></li>'
]

# Mobile menu links to remove (approximate patterns)
mobile_escritorio = '<a href="escritorio.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color=\'#1a1a1a\'" onmouseout="this.style.color=\'#6b6b6b\'">Escritório</a>'
mobile_complementos = '<a href="complementos.html" style="font-size:0.85rem;color:#6b6b6b;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color=\'#1a1a1a\'" onmouseout="this.style.color=\'#6b6b6b\'">Complementos</a>'

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove desktop links
    for link in desktop_links_to_remove:
        content = content.replace(link, '')
        
    # Remove mobile links
    content = content.replace(mobile_escritorio, '')
    content = content.replace(mobile_complementos, '')

    # We also need to remove them from the top Header desktop menu
    # <a href="escritorio.html" class="text-[10px] font-bold text-gray-800 hover:text-gray-500 tracking-[0.2em]">ESCRITÓRIO</a>
    content = content.replace('<a href="escritorio.html" class="text-[10px] font-bold text-gray-800 hover:text-gray-500 tracking-[0.2em]">ESCRITÓRIO</a>', '')
    content = content.replace('<a href="complementos.html" class="text-[10px] font-bold text-gray-800 hover:text-gray-500 tracking-[0.2em]">COMPLEMENTOS</a>', '')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Menus updated across all files.")
