import re

filepath = '/Users/nadiairina/Desktop/adil móveis/adil-moveis/packs.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Filters block
old_filters = """      <!-- Subcategories Section -->
<section class="py-12 bg-white">
  <div class="container mx-auto px-4">
    <div class="filters flex flex-wrap justify-center gap-4 max-w-4xl mx-auto">
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1 active" data-category="all">Todos</button>
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1" data-category="sofas">Sofás</button>
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1" data-category="moveis">Móveis</button>
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1" data-category="mesasEcadeiras">Mesas e Cadeiras</button>
    </div>
  </div>
</section>"""

new_filters = """      <!-- Subcategories Section -->
<section class="py-12 bg-white">
  <div class="container mx-auto px-4">
    <div class="filters flex flex-wrap justify-center gap-4 max-w-4xl mx-auto">
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1 active" data-category="all">Todos</button>
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1" data-category="quarto">Packs Quarto</button>
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1" data-category="sala">Packs Sala</button>
      <button class="filter-button px-6 py-3 transition-all duration-300 rounded-full font-medium tracking-wide shadow-sm hover:shadow-md hover:bg-[#C8B598] hover:text-white hover:-translate-y-1" data-category="casal">Packs de Casal</button>
    </div>
  </div>
</section>"""

content = content.replace(old_filters, new_filters)

# 2. Rebuild product boxes section.
# Let's locate the main grid section. It looks like:
# <section style="background:#FDFCFA; padding:5rem 0;">
#   <div style="max-width:1280px; margin:0 auto; padding:0 1.5rem;">
#     <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
#       ... many boxes ...
#     </div>
#   </div>
# </section>

# Let's replace the grid content with exactly 20 stylized Pack boxes.
boxes_html = ""
categories = ["quarto", "sala", "casal"]

for i in range(1, 21):
    cat = categories[(i-1) % len(categories)]
    cat_label = "Quarto" if cat == "quarto" else "Sala de Estar" if cat == "sala" else "Casal Completo"
    boxes_html += f"""            <!-- Product Box {i} -->
            <a href="produto-detalhe.html?id=pack-{i}" class="product bg-white rounded overflow-hidden block border border-[#E8E3DC] hover:shadow-md transition-shadow relative" data-category="{cat}" style="text-decoration:none; color:inherit;">
              <div class="relative" style="padding-top:100%; overflow:hidden; background:#F7F4F0;">
                <img src="images/sem-imagem.svg" alt="Pack Especial {cat_label} Ref. {i}" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 hover:scale-105" />
                <div style="position:absolute; top:12px; left:12px; background:#C8B598; color:#fff; font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:4px 10px; border-radius:20px; z-index:2;">
                  Pack Especial
                </div>
              </div>
              <div class="p-4 text-center" style="background:#FDFCFA; border-top:1px solid #E8E3DC;">
                <h3 style="font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:0.05em; text-transform:uppercase; color:#1a1a1a; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Pack {cat_label} Ref. {i}</h3>
                <p style="font-family:'Inter',sans-serif; font-size:11px; margin:0;">
                  <span class="price-discounted" style="font-weight:600; color:#c8b598;">Sob Consulta</span>
                </p>
              </div>
            </a>\n"""

# Regex to find the whole grid and replace it
grid_pattern = r'<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">[\s\S]*?</div>\s*</div>\s*</section>'
replacement_grid = f'<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">\n{boxes_html}            </div>\n        </div>\n      </section>'

content = re.sub(grid_pattern, replacement_grid, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Packs page fully rebuilt with correct pack categories and links.")
