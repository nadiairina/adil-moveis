import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Revert logo
    content = content.replace('images/logo_transparent.png', 'images/logo.png')
    
    # Re-add mix-blend-mode to logo if it's missing
    # Find <img src="images/logo.png" ... style="..."> and ensure mix-blend-mode is there
    def fix_logo_style(match):
        tag = match.group(0)
        if 'mix-blend-mode:multiply' not in tag.replace(' ', ''):
            return tag.replace('style="', 'style="mix-blend-mode:multiply; ')
        return tag
    content = re.sub(r'<img[^>]+src="images/logo\.png"[^>]*>', fix_logo_style, content)

    # Revert image styles
    # We injected: ; width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;
    # or width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;
    
    content = content.replace('; width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;', '')
    content = content.replace('style="width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;" ', '')
    content = content.replace('width: 100% !important; height: 100% !important; position: absolute !important; object-fit: cover !important; top: 0 !important; left: 0 !important;', '')
    
    with open(file, 'w') as f:
        f.write(content)

print("Reverted logo and inline image styles.")
