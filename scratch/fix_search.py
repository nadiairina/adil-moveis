import os

filepath = 'search.html'
if not os.path.exists(filepath):
    print('File not found:', filepath)
    exit(1)

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. We will replace the catalog declarations (kidsCatalog, mattressCatalog, packsCatalog)
# and getSearchableCatalog and renderCard logic.
# Let's locate from "// 1. Kids Products (10 official items from kids.html)" to "// Plural mappings for robust Portuguese search"

start_idx = html.find('  // 1. Kids Products (10 official items from kids.html)')
end_idx = html.find('  // Plural mappings for robust Portuguese search')

if start_idx != -1 and end_idx != -1:
    new_js_block = r'''  // Packs Catalog (5 official packs with correct paths and descriptions)
  const packsCatalog = [
    {
      id: "pack-1",
      name: "Pack Sala de Sonho",
      category: "Packs Especiais",
      subcategory: "Packs Sala",
      url: "pack-detalhe.html?id=pack-1",
      image: "images/produtos/pack-sala-sonho-hq.jpg",
      description: "Pack completo para sala de estar: sofá Orly e base de TV Madrid.",
      keywords: ["pack", "packs", "sala", "sofa", "sofá", "base tv", "madrid", "orly", "sala de estar", "sala de sonho"]
    },
    {
      id: "pack-2",
      name: "Pack Sala de Sonho Premium",
      category: "Packs Especiais",
      subcategory: "Packs Sala",
      url: "pack-detalhe.html?id=pack-2",
      image: "images/produtos/saladesonhopremium.jpg",
      description: "Pack premium para sala: sofá Luna Chaise, base de TV Malmo e mesa de centro Malmo.",
      keywords: ["pack", "packs", "sala", "sofa", "sofá", "premium", "luna", "malmo", "sala de estar", "sala de sonho premium"]
    },
    {
      id: "pack-3",
      name: "Pack Aconchego Essencial",
      category: "Packs Especiais",
      subcategory: "Packs Quarto",
      url: "pack-detalhe.html?id=pack-3",
      image: "images/produtos/quarto-casal-madrid-bluewall.jpg",
      description: "Pack de quarto completo: cama de casal Madrid, colchão Super Ortopédico e 2 almofadas Soft de oferta.",
      keywords: ["pack", "packs", "quarto", "cama", "casal", "madrid", "colchao", "colchão", "ortopedico", "almofadas", "soft", "dormir", "aconchego", "pack quarto"]
    },
    {
      id: "pack-4",
      name: "Pack À Mesa",
      category: "Packs Especiais",
      subcategory: "Packs Jantar",
      url: "pack-detalhe.html?id=pack-4",
      image: "images/produtos/amesa.jpg",
      description: "Pack sala de jantar: mesa extensível Paris e 4 cadeiras estofadas Paris.",
      keywords: ["pack", "packs", "mesa", "jantar", "sala de jantar", "cadeiras", "paris", "comer", "refeicao", "refeição", "pack jantar", "a mesa", "à mesa"]
    },
    {
      id: "pack-5",
      name: "Pack Sonhos Tranquilos",
      category: "Packs Especiais",
      subcategory: "Packs Quarto",
      url: "pack-detalhe.html?id=pack-5",
      image: "images/produtos/colchao-bestbed-sublime-grafen-conjunto-1.jpg",
      description: "Pack de quarto com sommier soft, cabeceira Divine e colchão de alta gama.",
      keywords: ["pack", "packs", "quarto", "cama", "sommier", "soft", "cabeceira", "divine", "colchao", "colchão", "dormir", "descanso", "sonhos tranquilos"]
    }
  ];

  function getSearchableCatalog() {
    const list = [];
    
    // Add all products dynamically from products.js (window_products)
    if (typeof window_products !== 'undefined') {
      for (const [key, p] of Object.entries(window_products)) {
        list.push({
          id: p.id || key,
          name: p.name || "",
          category: p.category || "Mobiliário",
          subcategory: p.subcategory || "",
          url: "produto-detalhe.html?id=" + encodeURIComponent(p.id || key),
          image: p.image || "images/logo_sem_fundo.png",
          description: p.description || "",
          keywords: [
            p.name,
            p.category,
            p.subcategory || "",
            p.description || "",
            ...(p.id ? p.id.split('-') : [])
          ]
        });
      }
    }

    // Add Packs
    list.push(...packsCatalog);

    return list;
  }
  
  '''
    html = html[:start_idx] + new_js_block + html[end_idx:]
    print('Updated search catalog to be 100% dynamic!')
else:
    print('Error: Could not locate catalog start/end index!')

# 2. Let's update renderCard function in search.html to remove border and background-color
old_render_card = '''  function renderCard(p) {
    return `
      <a href="${p.url}" class="product bg-white rounded overflow-hidden block hover:shadow-md transition-shadow relative" style="text-decoration:none; color:inherit; border:1px solid #E8E3DC;">
        <div class="relative w-full" style="aspect-ratio: 1 / 1; overflow:hidden; background:#F7F4F0;">
          <img src="${p.image}" alt="${p.name}" class="absolute inset-0 w-full h-full object-contain transition-transform duration-500 hover:scale-105" style="mix-blend-mode: darken;" onerror="this.src='images/logo_sem_fundo.png'; this.style.objectFit='contain'; this.style.padding='20px';" />
        </div>
        <div class="p-4 text-center" style="background:#FDFCFA; border-top:1px solid #E8E3DC;">
          <h3 style="font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:0.05em; text-transform:uppercase; color:#1a1a1a; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${p.name}</h3>
          <p style="font-family:'Inter',sans-serif; font-size:11px; margin:0;">
            <span class="price-discounted" style="font-weight:600; color:#c8b598;">Preço Sob Consulta</span>
          </p>
        </div>
      </a>
    `;
  }'''

new_render_card = '''  function renderCard(p) {
    return `
      <a href="${p.url}" class="product bg-white rounded overflow-hidden block hover:shadow-md transition-shadow relative" style="text-decoration:none; color:inherit;">
        <div class="relative w-full" style="aspect-ratio: 1 / 1; overflow:hidden; background:transparent;">
          <img src="${p.image}" alt="${p.name}" class="absolute inset-0 w-full h-full object-contain transition-transform duration-500 hover:scale-105" style="mix-blend-mode: darken;" onerror="this.src='images/logo_sem_fundo.png'; this.style.objectFit='contain'; this.style.padding='20px';" />
        </div>
        <div class="p-4 text-center" style="background:#FDFCFA; border-top:1px solid #E8E3DC;">
          <h3 style="font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:0.05em; text-transform:uppercase; color:#1a1a1a; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${p.name}</h3>
          <p style="font-family:'Inter',sans-serif; font-size:11px; margin:0;">
            <span class="price-discounted" style="font-weight:600; color:#c8b598;">Preço Sob Consulta</span>
          </p>
        </div>
      </a>
    `;
  }'''

if old_render_card in html:
    html = html.replace(old_render_card, new_render_card)
    print('Updated renderCard layout in search.html successfully!')
else:
    # Try with minor variant in formatting
    print('Error: Could not locate renderCard function exactly in search.html!')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
