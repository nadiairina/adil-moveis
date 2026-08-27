import os

# 1. Update pack-detalhe.html
with open('pack-detalhe.html', 'r', encoding='utf-8') as f:
    content = f.read()

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
                name: "Base Sommier Soft (À Escolha)",
                detail: "Base de apoio estofada com tecido personalizável",
                image: "images/produtos/sommier-bestbed-soft-tecido-elastron-seatle-light-grey.jpg",
                productId: "sommier-soft"
              },
              {
                name: "Cabeceira Divine (À Escolha)",
                detail: "Design contemporâneo acolchoado com tecido à sua medida",
                image: "images/produtos/cabeceira-bestbed-divine.jpg",
                productId: "cabeceira-divine"
              },
              {
                name: "Colchão Premium (À Escolha)",
                detail: "Escolha o colchão ideal para noites de repouso absoluto",
                image: "images/produtos/colchao-bestbed-v2.jpg",
                productId: "colchao-ortopedico-premium"
              }
            ],
            description: "O <strong>Pack Sonhos Tranquilos</strong> é a combinação perfeita de conforto e personalização para o seu quarto.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Base (à escolha):</strong> Base de apoio estofada com acabamento personalizável.<br>• <strong>Cabeceira Estofada (à escolha):</strong> Elegância e conforto à sua medida.<br>• <strong>Colchão de Alta Gama (à escolha):</strong> Escolha entre os nossos modelos de topo para um sono perfeito.<br><br><em>Fale connosco no WhatsApp para escolher a sua combinação e pedir orçamento!</em>"
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

if old_pack_5 in content:
    content = content.replace(old_pack_5, new_pack_5)
    with open('pack-detalhe.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated pack-detalhe.html successfully!")
else:
    print("Error: Could not find exact old_pack_5 in pack-detalhe.html")

# 2. Update packs.html
with open('packs.html', 'r', encoding='utf-8') as f:
    packs_content = f.read()

old_packs_card = '''          <!-- Pack 5: Pack Sonhos Tranquilos -->
          <div class="product pack-card bg-white rounded-xl overflow-hidden border border-[#E8E3DC] shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-1 flex flex-col justify-between" data-category="quarto">
            <div>
              <a href="pack-detalhe.html?id=pack-5" class="block relative w-full" style="aspect-ratio: 16/10; overflow:hidden; background:#F7F4F0;">
                <img src="images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg" alt="pack-5" class="absolute inset-0 w-full h-full object-cover" style="mix-blend-mode: darken;" />
                <div style="position:absolute; top:12px; left:12px; background:rgba(26,26,26,0.85); color:#fff; font-size:8px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; padding:4px 10px; border-radius:20px;">DESCANSO MOTORIZADO</div>
              </a>
              <div class="p-5">
                <span style="font-size:9px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#C8B598; display:block; margin-bottom:4px;">Pack Descanso Motorizado</span>
                <h3 style="font-family:'Playfair Display',serif; font-size:1.2rem; font-weight:400; color:#1a1a1a; margin-bottom:0.5rem;"><a href="pack-detalhe.html?id=pack-5" style="color:inherit; text-decoration:none;" class="hover:text-[#C8B598] transition-colors">"Pack Sonhos Tranquilos"</a></h3>
                <p style="font-size:0.8rem; color:#6b6b6b; line-height:1.5; margin-bottom:0.75rem;">
                  Base Arca Elevatória c/ Motor Mindol + Cabeceira Estofada + Colchão à Escolha.
                </p>
              </div>
            </div>'''

new_packs_card = '''          <!-- Pack 5: Pack Sonhos Tranquilos -->
          <div class="product pack-card bg-white rounded-xl overflow-hidden border border-[#E8E3DC] shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-1 flex flex-col justify-between" data-category="quarto">
            <div>
              <a href="pack-detalhe.html?id=pack-5" class="block relative w-full" style="aspect-ratio: 16/10; overflow:hidden; background:#F7F4F0;">
                <img src="images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg" alt="pack-5" class="absolute inset-0 w-full h-full object-cover" style="mix-blend-mode: darken;" />
                <div style="position:absolute; top:12px; left:12px; background:rgba(26,26,26,0.85); color:#fff; font-size:8px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; padding:4px 10px; border-radius:20px;">QUARTO & DESCANSO</div>
              </a>
              <div class="p-5">
                <span style="font-size:9px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#C8B598; display:block; margin-bottom:4px;">Pack Quarto & Descanso</span>
                <h3 style="font-family:'Playfair Display',serif; font-size:1.2rem; font-weight:400; color:#1a1a1a; margin-bottom:0.5rem;"><a href="pack-detalhe.html?id=pack-5" style="color:inherit; text-decoration:none;" class="hover:text-[#C8B598] transition-colors">"Pack Sonhos Tranquilos"</a></h3>
                <p style="font-size:0.8rem; color:#6b6b6b; line-height:1.5; margin-bottom:0.75rem;">
                  Base estofada + Cabeceira estofada + Colchão à escolha (Oferta de 1 protetor e 2 almofadas).
                </p>
              </div>
            </div>'''

if old_packs_card in packs_content:
    packs_content = packs_content.replace(old_packs_card, new_packs_card)
    with open('packs.html', 'w', encoding='utf-8') as f:
        f.write(packs_content)
    print("Updated packs.html successfully!")
else:
    print("Error: Could not find exact old_packs_card in packs.html")

# 3. Update search.html
with open('search.html', 'r', encoding='utf-8') as f:
    search_content = f.read()

old_search_pack_5 = 'description: "Pack de quarto com sommier soft, cabeceira Divine e colchão de alta gama.",'
new_search_pack_5 = 'description: "Pack Sonhos Tranquilos: Base e cabeceira estofadas em vários tecidos e medidas, colchão com aconselhamento gratuito + Oferta de 1 protetor e 2 almofadas.",'

if old_search_pack_5 in search_content:
    search_content = search_content.replace(old_search_pack_5, new_search_pack_5)
    with open('search.html', 'w', encoding='utf-8') as f:
        f.write(search_content)
    print("Updated search.html successfully!")
