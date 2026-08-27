import os

# 1. Update pack-detalhe.html
with open('pack-detalhe.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_description_html = """Dormir com estilo nunca foi tão fácil! ✨<br><br>Esqueça a cama básica. Aqui, você é o designer do seu descanso!<br><br>• <strong>Medidas sob medida:</strong> Do solteiro ao king, temos o tamanho exato para o seu espaço.<br>• <strong>Cores infinitas:</strong> Do neutro sofisticado ao tom ousado, a cor que combina com a sua personalidade.<br>• <strong>Modelos para todos os gostos:</strong> Bases modernas, cabeceiras estofadas, clássicas ou minimalistas. O seu quarto, a sua cara!<br><br><strong>E o melhor: o colchão perfeito espera por si!</strong><br>🛌 Faça um diagnóstico gratuito e descubra, em minutos, o nível de firmeza ideal para as suas costas e noites de sono.<br><br><strong>Tudo junto e com um empurrãozinho no bolso:</strong><br>💰 <strong>Descontos até 50%</strong> na compra de conjunto (cama + colchão)!<br><br>Crie a cama dos seus sonhos, peça por peça, e poupe a sério.<br>👑 <em>Conforto que se vê, estilo que se sente, preço que se agrade.</em><br><br>👉 <strong>Venha fazer o seu diagnóstico gratuito na nossa loja no Feijó</strong> – A sua combinação perfeita espera por si! 🛏️"""

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

new_pack_5 = f'''          "pack-5": {{
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
              {{"name": "Base Estofada", "detail": "Disponível em vários tecidos e medidas sob medida", "image": "images/produtos/sommier-bestbed-soft-tecido-elastron-seatle-light-grey.jpg", "productId": "sommier-soft"}},
              {{"name": "Cabeceira Estofada", "detail": "Modelos clássicos, modernos ou minimalistas à sua medida", "image": "images/produtos/cabeceira-bestbed-divine.jpg", "productId": "cabeceira-divine"}},
              {{"name": "Colchão Adequado a Si", "detail": "Com diagnóstico de firmeza gratuito na nossa loja", "image": "images/produtos/colchao-bestbed-v2.jpg", "productId": "colchao-ortopedico-premium"}}
            ],
            description: "{new_description_html}"
          }}'''

if old_pack_5 in content:
    content = content.replace(old_pack_5, new_pack_5)
    with open('pack-detalhe.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated pack-detalhe.html with new copy!")
else:
    print("Error: Could not find exact old_pack_5")

# 2. Update packs.html summary
with open('packs.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

p_content = p_content.replace(
    'Base estofada + Cabeceira estofada + Colchão adequado a si com aconselhamento gratuito.',
    'Descontos até 50% em Conjunto: Base estofada + Cabeceira à medida + Colchão com diagnóstico gratuito.'
)

with open('packs.html', 'w', encoding='utf-8') as f:
    f.write(p_content)
print("Updated packs.html with new copy!")
