import glob
import re

# 1. Reorder sections and remove period in index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the period
html = html.replace("Explore por divisão.", "Explore por divisão")

# Extract sections
# We need to find the "Familia/Historia" section and the "Explore por divisoes" section.
# They are <section ...> ... </section>

historia_match = re.search(r'(<section class="py-24".*?</section>\s*)<section class="py-12 bg-white', html, re.DOTALL)
explore_match = re.search(r'(<section class="py-24 bg-\[\#FDFBF7\]">\s*<div class="container.*?Explore por divisão.*?</section>)', html, re.DOTALL)

if historia_match and explore_match:
    historia_html = historia_match.group(1)
    explore_html = explore_match.group(1)
    
    # Remove both from their original places
    html = html.replace(historia_html, "")
    html = html.replace(explore_html, "")
    
    # Now we insert them back in the new order.
    # We want Explore right after Hero. Hero ends around line 223
    # Look for </section>\s*(<!--) before Historia was
    hero_end_pattern = r'</section>\s*(<!-- ?)'
    # Actually, let's just find the Hero section end:
    hero_match = re.search(r'<!-- Hero -->.*?</section>', html, re.DOTALL)
    if hero_match:
        hero_end_pos = hero_match.end()
        # Insert explore_html then historia_html
        html = html[:hero_end_pos] + "\n\n" + explore_html + "\n\n" + historia_html + html[hero_end_pos:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html")

# 2. Modernize filters to be more elegant (serif, no caps, soft colors)
html_files = [
    "quartos.html", "salas.html", "cozinha.html", "colchoes.html", 
    "conjuntos.html", "kids.html", "escritorio.html", "complementos.html"
]

old_inactive = r'class="filter-button pb-2 text-gray-400 hover:text-black uppercase tracking-widest text-xs font-bold border-b-2 border-transparent hover:border-black transition-all"'
old_active = r'class="filter-button pb-2 text-black uppercase tracking-widest text-xs font-bold border-b-2 border-black transition-all active"'

new_inactive = 'class="filter-button pb-1 px-2 text-gray-400 hover:text-black font-medium text-sm border-b border-transparent hover:border-gray-300 transition-all"'
new_active = 'class="filter-button pb-1 px-2 text-black font-medium text-sm border-b border-black transition-all active"'

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Update HTML classes
        content = content.replace(old_inactive, new_inactive)
        content = content.replace(old_active, new_active)
        
        # Change words from ALL CAPS to Title Case (e.g. TODOS -> Todos)
        # We already did Todos in HTML actually, it's just the CSS text-transform uppercase that made it caps.
        # So removing uppercase fixes it. But let's make sure the HTML text is capitalized nicely.
        # "Todos" -> "Todos", "Camas" -> "Camas", "Mesas de Cabeceira", etc. (they already are in HTML!)
        
        # Update JS logic that toggles classes
        js_old_remove = r"btn\.classList\.remove\('text-black', 'border-black'\);\s*btn\.classList\.add\('text-gray-400', 'border-transparent'\);"
        js_new_remove = r"btn.classList.remove('text-black', 'border-black');\n        btn.classList.add('text-gray-400', 'border-transparent');"
        
        # Actually the classes to toggle are the same: text-black, border-black, text-gray-400, border-transparent
        # I just removed uppercase, tracking-widest, etc. from the HTML.
        # Let's also remove border-b-2 and use border-b
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated filters in {filepath}")
        
    except Exception as e:
        print(f"Error {filepath}: {e}")
