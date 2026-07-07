import re

with open('/Users/nadiairina/Desktop/adil móveis/adil-moveis/tecidos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to remove this block from the cards:
# <div style="display:flex; flex-direction:column; gap:1rem; width:100%; border-top:1px solid #D4E4EE; padding-top:1.5rem;">
#   <img src="images/tecidos/tecido_capa_X.jpg" ...>
#   <img src="images/tecidos/tecido_capa_Y.jpg" ...>
# </div>

# Let's use regex to remove that div
new_content = re.sub(
    r'<div style="display:flex; flex-direction:column; gap:1rem; width:100%; border-top:1px solid #D4E4EE; padding-top:1\.5rem;">\s*<img[^>]+>\s*<img[^>]+>\s*</div>',
    '',
    content
)

with open('/Users/nadiairina/Desktop/adil móveis/adil-moveis/tecidos.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed extra images from tecidos.")
