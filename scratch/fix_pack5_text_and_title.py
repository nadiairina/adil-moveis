import os

# 1. Fix pack-detalhe.html
with open('pack-detalhe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix duplicate dynamic-title IDs
content = content.replace(
    '<h1 id="dynamic-title" style="font-family:\'Playfair Display\',serif;font-size:clamp(2rem,4vw,3.5rem);font-weight:400;color:#1a1a1a;line-height:1.1;">Produto</h1>',
    '<h1 id="dynamic-title-top" style="font-family:\'Playfair Display\',serif;font-size:clamp(2rem,4vw,3.5rem);font-weight:400;color:#1a1a1a;line-height:1.1;">Produto</h1>'
)
content = content.replace(
    '<h1 id="dynamic-title" style="font-family:\'Playfair Display\',serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:400;color:#1a1a1a;line-height:1.2;margin-bottom:1.25rem;">Produto</h1>',
    '<h1 id="dynamic-title-side" style="font-family:\'Playfair Display\',serif;font-size:clamp(1.6rem,3vw,2.4rem);font-weight:400;color:#1a1a1a;line-height:1.2;margin-bottom:1.25rem;">Produto</h1>'
)

# Update Title setter in JS
old_title_js = "document.getElementById('dynamic-title').textContent = p.name;"
new_title_js = """var tTop = document.getElementById('dynamic-title-top'); if (tTop) tTop.textContent = p.name;
        var tSide = document.getElementById('dynamic-title-side'); if (tSide) tSide.textContent = p.name;
        var tMain = document.getElementById('dynamic-title'); if (tMain) tMain.textContent = p.name;"""
content = content.replace(old_title_js, new_title_js)

# Update pack-5 data
old_pack_5 = '''          "pack-5": {
            id: "pack-5",
            name: "Pack Sonhos Tranquilos",
            category: "Packs Especiais",
            price: 0,
            image: "images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg",
            gallery: [
              "images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg",
              "images/produtos/sommier-bestbed-soft-tecido-elastron-seatle-light-grey.jpg",
              "images/produtos/cabeceira-bestbed-divine.jpg",
              "images/produtos/colchao-bestbed-v2.jpg",
              "images/produtos/SOFT.jpg"
            ],
            items: [
              {
                name: "Base Estofada",
                detail: "Base de cama estofada disponível em vários tecidos e medidas",
                image: "images/produtos/sommier-bestbed-soft-tecido-elastron-seatle-light-grey.jpg",
                productId: "sommier-soft"
              },
              {
                name: "Cabeceira Estofada",
                detail: "Cabeceira estofada disponível em vários tecidos e medidas",
                image: "images/produtos/cabeceira-bestbed-divine.jpg",
                productId: "cabeceira-divine"
              },
              {
                name: "Colchão Adequado a Si",
                detail: "Com diagnóstico e aconselhamento gratuito na nossa loja",
                image: "images/produtos/colchao-bestbed-v2.jpg",
                productId: "colchao-ortopedico-premium"
              },
              {
                name: "Oferta de 1 Protetor + 2 Almofadas",
                detail: "🎁 Oferta exclusiva incluída neste pack",
                image: "images/produtos/SOFT.jpg",
                productId: "almofadas-soft"
              }
            ],
            description: "O <strong>Pack Sonhos Tranquilos</strong> é a combinação perfeita para noites de descanso revigorante feitas à sua medida.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Base Estofada:</strong> Base de cama estofada disponível em vários tecidos e medidas.<br>• <strong>Cabeceira Estofada:</strong> Cabeceira estofada disponível em vários tecidos e medidas.<br>• <strong>Colchão:</strong> Colchão adequado a si, com diagnóstico e aconselhamento gratuito.<br>🎁 <strong>OFERTA EXCLUSIVA:</strong> Oferta de 1 protetor de colchão e 2 almofadas!<br><br><em>Fale connosco no WhatsApp ou visite a nossa loja no Feijó para experimentar e personalizar o seu pack!</em>"
          }'''

new_pack_5 = '''          "pack-5": {
            id: "pack-5",
            name: "Pack Sonhos Tranquilos",
            category: "Packs Especiais",
            price: 0,
            image: "images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg",
            gallery: [
              "images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg",
              "images/produtos/sommier-bestbed-soft-tecido-elastron-seatle-light-grey.jpg",
              "images/produtos/cabeceira-bestbed-divine.jpg",
              "images/produtos/colchao-bestbed-v2.jpg"
            ],
            items: [
              {
                name: "Base Estofada",
                detail: "Base de cama estofada disponível em vários tecidos e medidas",
                image: "images/produtos/sommier-bestbed-soft-tecido-elastron-seatle-light-grey.jpg",
                productId: "sommier-soft"
              },
              {
                name: "Cabeceira Estofada",
                detail: "Cabeceira estofada disponível em vários tecidos e medidas",
                image: "images/produtos/cabeceira-bestbed-divine.jpg",
                productId: "cabeceira-divine"
              },
              {
                name: "Colchão Adequado a Si",
                detail: "Com diagnóstico e aconselhamento gratuito na nossa loja",
                image: "images/produtos/colchao-bestbed-v2.jpg",
                productId: "colchao-ortopedico-premium"
              }
            ],
            description: "O <strong>Pack Sonhos Tranquilos</strong> é a combinação perfeita para noites de descanso revigorante feitas à sua medida.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Base Estofada:</strong> Base de cama estofada disponível em vários tecidos e medidas.<br>• <strong>Cabeceira Estofada:</strong> Cabeceira estofada disponível em vários tecidos e medidas.<br>• <strong>Colchão:</strong> Colchão adequado a si, com diagnóstico e aconselhamento gratuito.<br><br><em>Fale connosco no WhatsApp ou visite a nossa loja no Feijó para experimentar e personalizar o seu pack!</em>"
          }'''

content = content.replace(old_pack_5, new_pack_5)

with open('pack-detalhe.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated pack-detalhe.html!")

# 2. Fix packs.html
with open('packs.html', 'r', encoding='utf-8') as f:
    packs_content = f.read()

packs_content = packs_content.replace(
    'Base estofada + Cabeceira estofada + Colchão à escolha (Oferta de 1 protetor e 2 almofadas).',
    'Base estofada + Cabeceira estofada + Colchão adequado a si com aconselhamento gratuito.'
)

with open('packs.html', 'w', encoding='utf-8') as f:
    f.write(packs_content)
print("Updated packs.html!")

# 3. Fix search.html
with open('search.html', 'r', encoding='utf-8') as f:
    search_content = f.read()

search_content = search_content.replace(
    'description: "Pack Sonhos Tranquilos: Base e cabeceira estofadas em vários tecidos e medidas, colchão com aconselhamento gratuito + Oferta de 1 protetor e 2 almofadas.",',
    'description: "Pack Sonhos Tranquilos: Base e cabeceira estofadas em vários tecidos e medidas, e colchão adequado a si com diagnóstico gratuito.",'
)

with open('search.html', 'w', encoding='utf-8') as f:
    f.write(search_content)
print("Updated search.html!")
