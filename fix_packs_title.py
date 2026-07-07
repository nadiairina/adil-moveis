filepath = '/Users/nadiairina/Desktop/adil móveis/adil-moveis/packs.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Salas" title and description in packs.html
content = content.replace(
    '<h1 style="font-family:\'Playfair Display\',serif; font-size:clamp(2rem,4vw,3.25rem); font-weight:400; color:#1a1a1a; letter-spacing:0.05em; margin-bottom:1rem; text-transform:uppercase;">Salas</h1>',
    '<h1 style="font-family:\'Playfair Display\',serif; font-size:clamp(2rem,4vw,3.25rem); font-weight:400; color:#1a1a1a; letter-spacing:0.05em; margin-bottom:1rem; text-transform:uppercase;">Packs Especiais</h1>'
)

content = content.replace(
    'Conforto e sofisticação para a sua sala. Sofás de canto, poltronas e mesas desenhadas para momentos de convívio perfeitos.',
    'Conjuntos completos de mobiliário concebidos para equipar a sua casa. Quartos completos, conjuntos de sala e combinações exclusivas com o melhor preço.'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Packs page hero title fixed.")
