import os
import re

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
categories = ["quartos.html", "salas.html", "colchoes.html", "kids.html", "escritorio.html", "complementos.html", "packs.html"]

for file in categories:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's find the closing main tag
    main_end = content.find('</main>')
    grid_end = content.find('</div>\n        </div>\n      </section>') # typical grid end
    
    if grid_end != -1 and main_end != -1:
        between = content[grid_end:main_end]
        if '<img' in between:
            print(f"Found images at bottom of {file}:")
            imgs = re.findall(r'<img[^>]*>', between)
            for img in imgs:
                print("  ", img[:100])
        else:
            print(f"No extra images in {file}")

