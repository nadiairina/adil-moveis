import os

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Logo size in header and footer
    # Header: style="width:52px;height:52px;border-radius:50%;
    # Header container: style="height:72px;"
    content = content.replace(
        'style="height:72px;"',
        'style="height:86px;"'
    ).replace(
        'width:52px;height:52px;border-radius:50%;',
        'width:76px;height:76px;border-radius:50%;'
    )
    
    # 2. Change PACKS to PACKS ESPECIAIS in header
    content = content.replace(
        '>PACKS</a>',
        '>PACKS ESPECIAIS</a>'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Globals fixed: Logo bigger, Packs renamed.")
