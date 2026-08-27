import os

filepath = 'pack-detalhe.html'
if not os.path.exists(filepath):
    print('File not found:', filepath)
    exit(1)

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. New officialPacks data
new_packs_data = r'''        window.officialPacks = {
          "pack-1": {
            id: "pack-1",
            name: "Pack Sala de Sonho",
            category: "Packs Especiais",
            price: 0,
            image: "images/produtos/pack-sala-sonho-hq.jpg",
            gallery: [
              "images/produtos/pack-sala-sonho-hq.jpg",
              "images/produtos/sofa-orly-2-lugares.jpg",
              "images/produtos/base-tv-madrid-brancostone.jpg"
            ],
            items: [
              {
                name: "Sofá Orly (2 Lugares)",
                detail: "Encostos reclináveis, elevado conforto e tecido personalizável",
                image: "images/produtos/sofa-orly-2-lugares-1.jpg",
                productId: "sofas-7"
              },
              {
                name: "Base TV Madrid (1 Gaveta)",
                detail: "L1555 x A500 x P450 mm",
                image: "images/produtos/base-tv-madrid-brancostone.jpg",
                productId: "basetv-madrid"
              }
            ],
            description: "O <strong>Pack Sala de Sonho</strong> foi especialmente desenhado para quem procura conforto e elegância na sala de estar.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Sofá Orly (2 lugares):</strong> Estofado de elevado conforto e durabilidade.<br>• <strong>Base TV Madrid (1 gaveta):</strong> L1555 x A500 x P450 mm.<br><br><em>Disponível para personalização de cores e tecidos. Fale connosco no WhatsApp para obter orçamento imediato!</em>"
          },
          "pack-2": {
            id: "pack-2",
            name: "Pack Sala de Sonho Premium",
            category: "Packs Especiais",
            price: 0,
            image: "images/produtos/saladesonhopremium.jpg",
            gallery: [
              "images/produtos/saladesonhopremium.jpg",
              "images/produtos/base-tv-malmo-capuccinocarvalho.jpg",
              "images/produtos/mesa-de-centro-malmo-dark-greycarvalho.jpg"
            ],
            items: [
              {
                name: "Sofá Luna Chaise",
                detail: "Chaise longue de elevada qualidade, reversível e encostos reclináveis",
                image: "images/produtos/saladesonhopremium.jpg",
                productId: "sofa-luna-chaise"
              },
              {
                name: "Base TV Malmo 180 (1 Gaveta)",
                detail: "L1800 x A500 x P455 mm (Disponível em 3 Cores)",
                image: "images/produtos/base-tv-malmo-capuccinocarvalho.jpg",
                productId: "basetv-malmo"
              },
              {
                name: "Mesa de Centro Malmo MC90",
                detail: "L900 x A380 x P600 mm (Disponível em 3 Cores)",
                image: "images/produtos/mesa-de-centro-malmo-dark-greycarvalho.jpg",
                productId: "mesa-centro-malmo"
              }
            ],
            description: "O <strong>Pack Sala de Sonho Premium</strong> combina linhas contemporâneas e máxima arrumação para a sua sala.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Sofá Luna Chaise:</strong> Chaise longue de elevada qualidade e conforto.<br>• <strong>Base TV Malmo (Módulo 1 gaveta 180):</strong> L1800 x A500 x P455 mm (Disponível em 3 Cores).<br>• <strong>Mesa de Centro Malmo (Módulo MC90):</strong> L900 x A380 x P600 mm (Disponível em 3 Cores).<br><br><em>Fale connosco no WhatsApp para escolher as cores e obter o melhor preço!</em>"
          },
          "pack-3": {
            id: "pack-3",
            name: "Pack Aconchego Essencial",
            category: "Packs Especiais",
            price: 0,
            image: "images/produtos/quarto-casal-madrid-bluewall.jpg",
            gallery: [
              "images/produtos/quarto-casal-madrid-bluewall.jpg",
              "images/produtos/Cama-Casal-Madrid.webp",
              "images/produtos/Cama-Casal-Madrid-4.webp",
              "images/produtos/super_ortopedico_1.jpg",
              "images/produtos/super_ortopedico_2.jpg",
              "images/produtos/SOFT.jpg"
            ],
            items: [
              {
                name: "Cama Casal Madrid",
                detail: "L1610 x A1100 x P2090 mm (Opção 4 gavetas com estrado incluído)",
                image: "images/produtos/Cama-Casal-Madrid.webp",
                productId: "quartos-41"
              },
              {
                name: "Colchão Super Ortopédico",
                detail: "Suporte anatómico de elevada densidade",
                image: "images/produtos/super_ortopedico_1.jpg",
                productId: "colchao-super-ortopedico"
              },
              {
                name: "2 Almofadas Soft (Oferta)",
                detail: "🎁 Oferta especial de 2 almofadas Soft com o pack",
                image: "images/produtos/SOFT.jpg",
                productId: "almofadas-soft"
              }
            ],
            description: "O <strong>Pack Aconchego Essencial</strong> é o conjunto de quarto de casal completo pensado para o seu descanso total.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Cama de Casal Madrid:</strong> L1610 x A1100 x P2090 mm (Opção com 4 gavetas e estrado incluído).<br>• <strong>Colchão Super Ortopédico:</strong> Suporte ergonómico de elevada densidade.<br>🎁 <strong>OFERTA EXCLUSIVA:</strong> 2 Almofadas Soft de presente!<br><br><em>Fale connosco no WhatsApp para personalizar o seu pack!</em>"
          },
          "pack-4": {
            id: "pack-4",
            name: "Pack À Mesa",
            category: "Packs Especiais",
            price: 0,
            image: "images/produtos/amesa.jpg",
            gallery: [
              "images/produtos/amesa.jpg",
              "images/produtos/mesa-de-jantar-paris-cinzabranco.png",
              "images/produtos/mesa-de-jantar-paris-cinzabranco-1.png",
              "images/produtos/paris-cadeira-lourini-1200x1200.png"
            ],
            items: [
              {
                name: "Mesa de Jantar Extensível Paris",
                detail: "Fechada L1400 / Aberta L2300 x A790 x P900 mm (2 Cores)",
                image: "images/produtos/mesa-de-jantar-paris-cinzabranco.png",
                productId: "mesa-sala-paris"
              },
              {
                name: "4x Cadeiras Estofadas Paris",
                detail: "Pés e tecido totalmente personalizáveis",
                image: "images/produtos/paris-cadeira-lourini-1200x1200.png",
                productId: "cadeira-paris"
              }
            ],
            description: "O <strong>Pack À Mesa</strong> é a solução perfeita para reuniões de família e jantares confortáveis.<br><br><strong>O conjunto inclui:</strong><br>• <strong>Mesa de Jantar Extensível Paris:</strong> Fechada L1400 x A790 x P900 mm | Aberta L2300 x A790 x P900 mm (Disponível em 2 Cores: Carvalho Cinza - Branco e Carvalho Natura - Branco).<br>• <strong>4x Cadeiras Estofadas Paris:</strong> Pés e tecido totalmente personalizáveis.<br><br><em>Fale connosco no WhatsApp para escolher os tecidos das cadeiras e obter orçamento!</em>"
          },
          "pack-5": {
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
          }
        };'''

start_mark = 'window.officialPacks = {'
end_mark = 'p = (window.officialPacks && window.officialPacks[productId])'
start_idx = html.find(start_mark)
end_idx = html.find(end_mark)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_packs_data + '\n        ' + html[end_idx:]
    print('1. Updated window.officialPacks database successfully!')
else:
    print('1. Error: Failed to find officialPacks data marks!')

# 2. Update rendering logic with raw string to preserve backslashes in JS output
new_render_js = r'''itemsContainer.innerHTML = p.items.map(function(item) {
            var targetUrl = '#';
            if (item.productId) {
              targetUrl = 'produto-detalhe.html?id=' + item.productId;
            } else if (item.linkUrl) {
              targetUrl = item.linkUrl;
            }
            return '<a href="' + targetUrl + '" style="background:#fff; border:1px solid #E8E3DC; border-radius:10px; overflow:hidden; transition:all 0.3s; cursor:pointer; text-decoration:none; color:inherit;" class="hover:shadow-md hover:border-[#C8B598] flex flex-col">' +
                   '  <div style="aspect-ratio:1/1; background:#F7F4F0; overflow:hidden; position:relative;">' +
                   '    <img src="' + item.image + '" alt="' + item.name + '" style="position:absolute; inset:0; width:100%; height:100%; object-fit:contain; mix-blend-mode:darken; padding:8px; transition:transform 0.4s;" class="hover:scale-105" onerror="this.src=\'images/logo_sem_fundo.png\'" />' +
                   '  </div>' +
                   '  <div style="padding:12px 14px; text-align:center; border-top:1px solid #E8E3DC; background:#FDFCFA; margin-top:auto;">' +
                   '    <h4 style="font-family:\'Inter\',sans-serif; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.04em; color:#1a1a1a; margin-bottom:4px; line-height:1.3;">' + item.name + '</h4>' +
                   '    <p style="font-size:10px; color:#6b6b6b; margin:0 0 8px 0; line-height:1.3; min-height:26px;">' + item.detail + '</p>' +
                   '    <span style="display:inline-block; font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#C8B598; border-bottom:1px solid transparent; transition:all 0.2s;">Ver Detalhe &rarr;</span>' +
                   '  </div>' +
                   '</a>';
          }).join('');'''

start_marker = 'itemsContainer.innerHTML = p.items.map(function(item) {'
end_marker = '}).join(\'\');'

start_idx = html.find(start_marker)
if start_idx != -1:
    end_idx = html.find(end_marker, start_idx)
    if end_idx != -1:
        end_idx += len(end_marker)
        html = html[:start_idx] + new_render_js + html[end_idx:]
        print('2. Successfully replaced items rendering loop!')
    else:
        print('2. Error: Failed to find end marker!')
else:
    print('2. Error: Failed to find start marker!')

with open('pack-detalhe.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
