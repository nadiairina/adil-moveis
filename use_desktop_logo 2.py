import glob
import re

# We want to replace the logo in all files to use images/logo.png
for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current logo might look like:
    # <img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-10 md:h-12 w-auto bg-white rounded border border-gray-200 shadow-sm px-2 py-1">
    # Or something similar.
    # We will use regex to find ANY img tag with src="images/adil-moveis-logo.png" and replace it.
    
    pattern = r'<img src="images/adil-moveis-logo\.png"[^>]*>'
    # For the new circle logo, we use h-14 w-14 (a perfect square) and rounded-full to make it a circle, with a tiny border.
    new_logo = '<img src="images/logo.png" alt="Adil Móveis" class="h-12 md:h-14 w-12 md:w-14 object-contain bg-white rounded-full border border-gray-200 shadow-sm p-0.5">'
    
    content = re.sub(pattern, new_logo, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Swapped logo to the exact circle image (images/logo.png) across all pages.")
