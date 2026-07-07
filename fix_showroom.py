import os

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

replacements = {
    "Showroom no Feijó, Almada": "Loja no Feijó, Almada",
    "Showroom em Almada": "Loja em Almada",
    "visitar o nosso showroom": "visitar a nossa loja",
    "diretamente no nosso showroom": "diretamente na nossa loja",
    "nosso Showroom": "nossa Loja"
}

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for target, replacement in replacements.items():
        if target in content:
            content = content.replace(target, replacement)
            changed = True
            
    # Also do case-insensitive fallback just in case
    # e.g. "showroom" to "loja" where it fits
    if "showroom" in content.lower():
        content = content.replace("showroom", "loja")
        content = content.replace("Showroom", "Loja")
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Showroom replacements completed.")
