import os

# Read quartos.html to grab the scripts block
with open('quartos.html', 'r', encoding='utf-8') as f:
    quartos_content = f.read()

# Grab everything from the Gallery modal to just before </body>
start_idx = quartos_content.find('<!-- Gallery Modal -->')
end_idx = quartos_content.find('</body>')

if start_idx != -1 and end_idx != -1:
    scripts_block = quartos_content[start_idx:end_idx]
    
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    # Remove existing scripts block if it somehow exists (just in case)
    if '<!-- AOS Animation Script -->' in index_content:
        # Already has it? No, but let's be safe.
        pass
    else:
        # Inject right before </body>
        index_content = index_content.replace('</body>', scripts_block + '\n</body>')
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_content)
        print("Scripts restored to index.html!")
else:
    print("Could not find scripts block in quartos.html")
