import os

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert size back
    content = content.replace(
        'padding:14px 0;font-size:16px;',
        'padding:8px 0;font-size:13px;'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Promo banner size reverted.")
