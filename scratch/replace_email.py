import os
import glob

html_files = glob.glob('*.html')
replaced_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'adil.moveis@hotmail.com' in content:
        content = content.replace('adil.moveis@hotmail.com', 'geral@adilmoveis.pt')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Replaced email in {filepath}")
        replaced_count += 1

print(f"Done! Updated email in {replaced_count} HTML files.")
