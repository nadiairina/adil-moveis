import os
import re

html_files = ['quartos.html', 'colchoes.html', 'salas.html', 'escritorio.html', 'cozinha.html', 'complementos.html', 'kids.html']

def generate_products(category_name, count=8):
    # Depending on category, pick a nice default image
    img = "https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp"
    if category_name == 'quartos':
        img = "https://nadiairina.github.io/adil-moveis/images/Lourini-Majestic.jpg"
    elif category_name == 'colchoes':
        img = "https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp"
    elif category_name == 'salas':
        img = "https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp"
    elif category_name == 'escritorio':
        img = "https://lourini.pt/app/uploads/2024/09/escritorio-nizza-1200x1200.png"
    elif category_name == 'complementos':
        img = "https://lourini.pt/app/uploads/2024/07/camiseiro-1200x1200.png"
    elif category_name == 'kids':
        img = "https://lourini.pt/app/uploads/2024/07/quarto-juvenil-1200x1200.png"

    html = ""
    for i in range(1, count + 1):
        html += f"""
          <div class="product group cursor-pointer" data-category="all">
            <div class="relative overflow-hidden bg-[#f0f0f0] rounded-xl mb-4 aspect-square">
              <img src="{img}" alt="Produto" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
            <h3 class="text-lg font-bold text-black mb-1">Coleção {category_name.capitalize()} {i}</h3>
            <p class="text-gray-500 text-sm mb-3">Qualidade Adil Móveis</p>
            <button class="snipcart-add-item w-full py-3 border border-black text-black font-bold uppercase tracking-widest text-xs hover:bg-black hover:text-white transition-colors"
              data-item-id="prod-{category_name}-{i}"
              data-item-price="0.00"
              data-item-name="Coleção {category_name.capitalize()} {i}"
              data-item-image="{img}">
              Ver Detalhes
            </button>
          </div>
"""
    return html

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to find where the products start and end.
    # The grid usually starts with `<div class="grid` after a title.
    # Let's find the first `<div class="product`
    first_prod_idx = content.find('<div class="product')
    if first_prod_idx == -1:
        continue
        
    # Find the end of the products. 
    # Usually it's before the `</main>` or `<!-- Gallery Modal -->`
    # Let's find the last occurrence of a closing div that comes before </main>
    # Better yet, regex to replace EVERYTHING from the first `<div class="product"` 
    # up until `</div>\n      </div>\n    </main>` or similar.
    
    # A safer way: find the start of the grid container
    grid_start = content.rfind('<div class="grid', 0, first_prod_idx)
    if grid_start == -1:
        continue
        
    grid_end = content.find('</main>', grid_start)
    if grid_end == -1:
        continue
        
    # Inside the grid container, we replace all content. But the grid container itself needs closing `</div>`.
    # Let's just find the exact grid container start, keep it, replace inner products, and close the grid and container.
    
    # Actually, we can just replace the entire <main>...</main> section of these category pages
    # because they all follow the same simple layout!
    
    category = filepath.split('.')[0]
    
    title = category.capitalize()
    if category == 'colchoes': title = 'Colchões'
    elif category == 'escritorio': title = 'Escritório'
    
    new_main = f"""    <main class="bg-white py-16">
      <div class="container mx-auto px-4 max-w-7xl">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-5xl font-light mb-4 tracking-tight text-black" data-aos="fade-down">{title}</h1>
          <p class="text-xl text-gray-500 max-w-2xl mx-auto font-light" data-aos="fade-up" data-aos-delay="200">Explore a nossa seleção de produtos de excelência.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
{generate_products(category, 8)}
        </div>
      </div>
    </main>"""
    
    # Replace everything between <main...> and </main>
    main_start = content.find('<main')
    main_end = content.find('</main>') + 7
    
    if main_start != -1 and main_end != -1:
        new_content = content[:main_start] + new_main + content[main_end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Balanced all category pages to have exactly 8 products each!")
