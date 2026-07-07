import os

directory = '/Users/nadiairina/Desktop/adil móveis/adil-moveis'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old footer styles (black footer):
    # padding:4rem 0 2rem;
    # margin-bottom:3rem;
    content = content.replace(
        'padding:4rem 0 2rem;',
        'padding:2rem 0 1rem;'
    ).replace(
        'margin-bottom:3rem;',
        'margin-bottom:2rem;'
    )

    # Some files might have the older Tailwind footer class: class="bg-black text-white py-10"
    content = content.replace('class="bg-black text-white py-10"', 'class="bg-black text-white py-6"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Footer size reduced across all pages.')
