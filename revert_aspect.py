import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Revert aspect-ratio back to padding-top
    content = content.replace('aspect-ratio: 1 / 1.1;', 'padding-top:110%;')
    
    with open(file, 'w') as f:
        f.write(content)

print("Reverted aspect ratio.")
