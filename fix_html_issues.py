import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. Fix floating bar text
    content = content.replace('📍 Como Chegar', '📍 Loja')
    content = content.replace('📅 Agendar Visita', '📅 Agendar')
    content = content.replace('💬 Pedir Orçamento', '💬 Orçamento')

    # 2. Force image styles on product cards
    # Look for images inside .relative.overflow-hidden (or similar container)
    # Actually, we can just find any <img> that has 'class="absolute inset-0 w-full h-full object-cover'
    # and inject the style attribute if it doesn't have one, or append to it.
    
    # Let's match all <img> tags that are product images. They generally have 'absolute inset-0'
    def replace_img(match):
        img_tag = match.group(0)
        # Don't modify if it already has the style
        if 'style="width: 100% !important;' in img_tag:
            return img_tag
            
        style_string = 'style="width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;"'
        
        # If it has a style attribute, append to it
        if 'style="' in img_tag:
            return re.sub(r'style="([^"]*)"', r'style="\1; width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;"', img_tag)
        else:
            # Inject style before class or at the end
            return img_tag.replace('<img ', f'<img {style_string} ')

    # Regex to match <img> tags with absolute and inset-0 classes
    content = re.sub(r'<img[^>]+class="[^"]*absolute inset-0[^"]*"[^>]*>', replace_img, content)

    with open(file, 'w') as f:
        f.write(content)

print("Done fixing HTML files.")
