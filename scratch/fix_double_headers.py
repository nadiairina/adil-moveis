import os

files_to_fix = [
    'catalogos.html',
    'contactos.html',
    'parceiros.html',
    'servicos.html',
    'testemunhos.html',
    'old_testemunhos.html'
]

for filename in files_to_fix:
    if not os.path.exists(filename):
        print(f"Skipping {filename} (not found)")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if there is <header> right after <body>
    # Usually:
    # <body>
    #   <header>
    #     <!-- Global Promo Banner -->
    
    # We want to remove the first <header> that is opened on line 63
    # Let's inspect the content structure:
    # <body>\n    <header>\n                              <!-- Global Promo Banner -->
    # or similar
    
    # We can replace the specific pattern:
    # <body>\n    <header>\n                              <!-- Global Promo Banner -->
    # or similar.
    # Let's do a more robust replacement by replacing the exact lines.
    
    lines = content.splitlines()
    fixed_lines = []
    removed = False
    
    for i, line in enumerate(lines):
        # Find <header> close to <body> and before another <header>
        # Let's just target the specific line containing <header> right after <body> or around line 62-66.
        if i in (61, 62, 63, 64) and line.strip() == '<header>' and not removed:
            print(f"Removing extra <header> on line {i+1} in {filename}")
            removed = True
            continue
        fixed_lines.append(line)
        
    if removed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(fixed_lines) + '\n')
        print(f"Successfully fixed {filename}!")
    else:
        print(f"Warning: Could not find extra <header> in {filename}")
