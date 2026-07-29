import glob

def fix_file(filename, expected_url_substring):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Replace the faulty line
    # Old line: if ("{category_filter}" !== "all" && p.url !== "{category_filter}.html" && p.category !== "{category_filter}") continue;
    # New line: if (!p.url.includes("expected_url_substring")) continue;
    
    import re
    # We find the script tag logic
    pattern = re.compile(r'if \(".*?" !== "all" && p\.url !== ".*?" && p\.category !== ".*?"\) continue;')
    new_logic = f'if (!p.url.includes("{expected_url_substring}")) continue;'
    
    content = pattern.sub(new_logic, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Fixed {filename}")

fix_file('quartos.html', 'quartos')
fix_file('salas.html', 'salas')
fix_file('kids.html', 'kids')

# Note: our kids items right now are in "quartos.html" in products.js, but she said "1 of them is kids". Let me quickly check if we added any kids item.
