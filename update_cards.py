import os
import re
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update the outer card container
    content = re.sub(
        r'class="product[^"]*rounded-lg[^"]*"',
        'class="product group bg-transparent overflow-hidden transition-all duration-700 flex flex-col"',
        content
    )
    
    # 2. Update the image container
    content = re.sub(
        r'class="relative h-[0-9]+[^"]*"',
        'class="relative aspect-[4/5] bg-[#f9f6f0] flex items-center justify-center overflow-hidden border-b border-[#EAE6DF]"',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated cards in {filepath}")
