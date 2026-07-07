import glob
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The Family + Gallery block
family_pattern = r'(<!-- Story Section -->.*?<!-- Classic Gallery -->.*?</section>)'
# The 8-grid block
explore_pattern = r'(<!-- 8-GRID CATEGORIAS \(Pedido da Cliente\) -->\s*<section class="py-24 bg-\[\#FDFBF7\]">.*?</section>)'

family_match = re.search(family_pattern, html, re.DOTALL)
explore_match = re.search(explore_pattern, html, re.DOTALL)

if family_match and explore_match:
    family_text = family_match.group(1)
    explore_text = explore_match.group(1)
    
    # We want to replace the whole block (which currently is Family followed by Explore) 
    # with Explore followed by Family.
    
    # Let's find the combined block
    # It might be family_text \n\n explore_text or similar.
    # We can just replace both with empty strings and then insert them at the right place, 
    # but it's safer to find the position of the first one, delete both, and insert in new order.
    
    pos1 = html.find(family_text)
    
    if pos1 != -1:
        # Remove them
        html = html.replace(family_text, "")
        html = html.replace(explore_text, "")
        
        # Insert them back at pos1: explore first, then family
        html = html[:pos1] + explore_text + "\n\n" + family_text + html[pos1:]
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Successfully reordered index.html")
    else:
        print("Could not find family_text index")
else:
    print("Could not match the regex patterns.")
