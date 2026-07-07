import glob

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Restore the price placeholder but use the Portuguese formatting to minimize any visual jump
    content = content.replace('<span class="snipcart-total-price hidden sm:block text-sm font-semibold"></span>',
                              '<span class="snipcart-total-price hidden sm:block text-sm font-semibold">0,00 €</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored initial cart value placeholder to avoid empty delay.")
