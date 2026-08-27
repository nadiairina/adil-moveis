import glob

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Update newsletter banner text
    if '(Válido online e em loja!)' in content:
        content = content.replace('(Válido online e em loja!)', '(Válido na nossa loja física!)')
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {file}")

print(f"Total files updated: {count}")
