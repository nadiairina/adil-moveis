import glob
import os
import re

# 1. READ THE MASTER HEADER AND FOOTER FROM INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Fix the logo in index.html first (Remove mix-blend-multiply which caused the black background issue)
index_content = index_content.replace('mix-blend-multiply drop-shadow-sm', '')
index_content = index_content.replace('mix-blend-multiply', '')

# Extract the corrected Header
header_start = index_content.find('<header class="sticky top-0')
header_end = index_content.find('</header>') + 9
master_header = index_content[header_start:header_end]

# Extract the Master Footer
footer_start = index_content.find('<footer')
footer_end = index_content.find('</footer>') + 9
master_footer = index_content[footer_start:footer_end]

# Ensure index.html is saved with the fixed logo
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)


# 2. APPLY TO ALL OTHER HTML FILES
for filepath in glob.glob("*.html"):
    if filepath in ["dashboard.html", "index.html"]:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply Master Header
    h_start = content.find('<header')
    h_end = content.find('</header>') + 9
    if h_start != -1 and h_end != -1:
        content = content[:h_start] + master_header + content[h_end:]
    
    # Apply Master Footer
    f_start = content.find('<footer')
    f_end = content.find('</footer>') + 9
    if f_start != -1 and f_end != -1:
        content = content[:f_start] + master_footer + content[f_end:]

    # Apply Consistent Body Tag
    # Some might have 'bg-white', we want 'bg-[#FDFBF7] text-[#2c2a29] font-sans antialiased'
    body_pattern = r'<body[^>]*>'
    match = re.search(body_pattern, content)
    if match:
        body_tag = match.group(0)
        new_body_tag = '<body class="bg-[#FDFBF7] text-[#2c2a29] font-sans antialiased">'
        content = content.replace(body_tag, new_body_tag)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Global consistency enforced: Header, Footer, and Body tags are now exactly identical across all pages. Logo black background removed.")
