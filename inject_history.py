import re

with open('empresa.html', 'r', encoding='utf-8') as f:
    empresa_content = f.read()

# Extract the history blocks
# From "<!-- Story Section -->" to "<!-- Values & Brands -->"
match = re.search(r'(<!-- Story Section -->.*?)(?=<!-- Values & Brands -->)', empresa_content, re.DOTALL)
if match:
    history_block = match.group(1)
    
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # We want to inject it after the Hero section in index.html.
    # The Hero section ends right before the first `<section class="py-24 bg-[#FDFBF7]">`
    # Let's find the end of the Hero section.
    # The Hero is `<!-- Hero --> ... </section>`
    hero_end_pattern = r'(<!-- Hero -->.*?</section>)'
    
    if history_block not in index_content:
        # We will inject right after the Hero
        new_index = re.sub(hero_end_pattern, r'\1\n\n' + history_block, index_content, count=1, flags=re.DOTALL)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_index)
        print("Injected history block into index.html")
    else:
        print("History block already in index.html")
else:
    print("Could not find history block in empresa.html")
