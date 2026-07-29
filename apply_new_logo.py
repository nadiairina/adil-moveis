import os
import glob
import shutil

# Move the logo to the images directory
src_logo = '../logo sem fundo.png'
dest_logo = 'images/logo_sem_fundo.png'

if os.path.exists(src_logo):
    shutil.move(src_logo, dest_logo)
    print("Moved logo to images folder.")
else:
    print("Logo not found in parent directory. Perhaps it was already moved?")

# Update all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace logo path
    content = content.replace('images/logo.png', 'images/logo_sem_fundo.png')
    
    # Remove mix-blend-mode: multiply
    content = content.replace('mix-blend-mode:multiply;', '')
    content = content.replace('mix-blend-mode: multiply;', '')
    
    # Also clean up any extra spaces or empty style tags if needed, but the browser handles it fine
    
    with open(file, 'w') as f:
        f.write(content)

print("Updated HTML files to use the new logo.")
