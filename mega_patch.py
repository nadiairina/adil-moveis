import os
import glob
import re

# 1. NEW MENU HTML
# We'll replace the existing menuOverlay block entirely.
MENU_START = '      <!-- Menu Overlay -->'
MENU_END_REGEX = r'</nav>\s*</div>\s*</div>'

NEW_MENU = """      <!-- Menu Overlay (Modern Fullscreen) -->
      <div id="menuOverlay" class="fixed inset-0 bg-black z-50 overflow-y-auto hidden h-screen text-white flex-col justify-center items-center">
        <button id="closeMenuButton" class="absolute top-8 right-8 text-white hover:text-gray-400 transition-colors">
          <i data-feather="x" class="w-10 h-10"></i>
        </button>
        <nav class="flex flex-col items-center space-y-6 mt-16 w-full max-w-lg mx-auto">
          <a href="index.html" class="text-3xl font-light hover:text-gray-400 transition-colors uppercase tracking-widest">Início</a>
          <a href="quartos.html" class="text-3xl font-light hover:text-gray-400 transition-colors uppercase tracking-widest">Quartos</a>
          <a href="salas.html" class="text-3xl font-light hover:text-gray-400 transition-colors uppercase tracking-widest">Salas</a>
          <a href="colchoes.html" class="text-3xl font-light hover:text-gray-400 transition-colors uppercase tracking-widest">Colchões</a>
          <a href="cozinha.html" class="text-3xl font-light hover:text-gray-400 transition-colors uppercase tracking-widest">Cozinhas</a>
          <a href="conjuntos.html" class="text-3xl font-bold hover:text-gray-400 transition-colors uppercase tracking-widest">Packs Especiais</a>
          <div class="w-16 h-px bg-gray-600 my-4"></div>
          <a href="contactos.html" class="text-xl font-light text-gray-400 hover:text-white transition-colors">Contactos e Lojas</a>
          <a href="contactos.html#agendar-visita" class="text-xl font-light text-gray-400 hover:text-white transition-colors">Agendar Visita</a>
        </nav>
      </div>"""

def patch_menu(content):
    # Find start
    idx_start = content.find(MENU_START)
    if idx_start == -1: return content
    
    # Find end
    match = re.search(MENU_END_REGEX, content[idx_start:])
    if not match: return content
    
    idx_end = idx_start + match.end()
    
    return content[:idx_start] + NEW_MENU + content[idx_end:]


# 2. GENERATE PLACEHOLDER PRODUCTS
def generate_placeholders(category_name, count):
    html = f'<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">\n'
    for i in range(1, count + 1):
        html += f"""
        <div class="product bg-white rounded-lg shadow-sm border border-gray-100 overflow-hidden flex flex-col group">
          <div class="relative h-64 bg-gray-100 flex items-center justify-center overflow-hidden">
            <span class="text-gray-400 font-medium">Foto {i}</span>
          </div>
          <div class="p-6 flex flex-col flex-grow text-center">
            <h3 class="text-lg font-bold text-black mb-2">{category_name} Modelo {i}</h3>
            <p class="text-gray-500 text-sm mb-4">Pendente de catálogo (Sara)</p>
            <button class="mt-auto bg-black text-white w-full py-3 text-xs font-bold uppercase tracking-wider hover:bg-gray-800 transition-colors rounded">
              Adicionar — 0.00€
            </button>
          </div>
        </div>
        """
    html += '</div>'
    return html

def replace_main_products(content, category_name, count):
    # Find the product grid container which is usually after <div class="grid grid-cols-1
    grid_start_regex = r'<div class="grid grid-cols-1 [^>]+>'
    
    # We will replace everything between `<div class="container mx-auto px-4">` in the `<section class="py-16 bg-white">`
    # and `</section>`
    
    section_match = re.search(r'<section class="py-16 bg-white">\s*<div class="container mx-auto px-4">\s*(?:<!-- Product grid container -->)?\s*<div class="grid', content)
    if not section_match:
        return content
        
    start_idx = section_match.start()
    
    # Find the closing section tag
    end_idx = content.find('</section>', start_idx)
    if end_idx == -1:
        return content
        
    new_section = f"""<section class="py-16 bg-white">
  <div class="container mx-auto px-4 max-w-7xl">
    <!-- PLACEHOLDERS: {count} Produtos -->
    {generate_placeholders(category_name, count)}
  </div>
"""
    return content[:start_idx] + new_section + content[end_idx:]


# 3. REDESIGN CONJUNTOS
NEW_CONJUNTOS_MAIN = """
    <main class="bg-white py-16">
      <div class="container mx-auto px-4 max-w-7xl">
        
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-5xl font-light mb-4 tracking-tight text-black">Coleções Completas</h1>
          <p class="text-xl text-gray-500 max-w-2xl mx-auto font-light">Espaços perfeitamente coordenados para a sua casa. Comprados em conjunto, entregues e montados gratuitamente.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
          
          <!-- PACK QUARTO -->
          <div class="group cursor-pointer">
            <div class="relative overflow-hidden bg-gray-100 rounded-sm mb-6 h-[450px]">
              <img src="images/Lourini-Majestic.jpg" alt="Quarto" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Packs Quarto</div>
            </div>
            <h3 class="text-2xl font-medium text-black mb-2">Coleção "Noite Tranquila"</h3>
            <p class="text-gray-600 mb-4 line-clamp-2">Cama estofada com arrumação, duas mesas de cabeceira elegantes e colchão ortopédico incluído.</p>
            <div class="flex justify-between items-center border-t border-gray-200 pt-4">
              <span class="text-xl font-bold">Desde 720€</span>
              <button class="snipcart-add-item border border-black px-6 py-2 text-sm font-bold uppercase tracking-wider hover:bg-black hover:text-white transition-colors">
                Adicionar
              </button>
            </div>
          </div>

          <!-- PACK SALA -->
          <div class="group cursor-pointer">
            <div class="relative overflow-hidden bg-gray-100 rounded-sm mb-6 h-[450px]">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" alt="Sala" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Packs Sala</div>
            </div>
            <h3 class="text-2xl font-medium text-black mb-2">Coleção "Jantar em Família"</h3>
            <p class="text-gray-600 mb-4 line-clamp-2">Mesa extensível em carvalho, quatro cadeiras estofadas confortáveis e um aparador minimalista.</p>
            <div class="flex justify-between items-center border-t border-gray-200 pt-4">
              <span class="text-xl font-bold">Desde 999€</span>
              <button class="snipcart-add-item border border-black px-6 py-2 text-sm font-bold uppercase tracking-wider hover:bg-black hover:text-white transition-colors">
                Adicionar
              </button>
            </div>
          </div>

          <!-- PACK COLCHAO -->
          <div class="group cursor-pointer">
            <div class="relative overflow-hidden bg-gray-100 rounded-sm mb-6 h-[450px]">
              <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" alt="Colchão" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Packs Descanso</div>
            </div>
            <h3 class="text-2xl font-medium text-black mb-2">Coleção "Sono Perfeito"</h3>
            <p class="text-gray-600 mb-4 line-clamp-2">Colchão viscoelástico premium, estrado metálico reforçado e duas almofadas cervicais.</p>
            <div class="flex justify-between items-center border-t border-gray-200 pt-4">
              <span class="text-xl font-bold">Desde 350€</span>
              <button class="snipcart-add-item border border-black px-6 py-2 text-sm font-bold uppercase tracking-wider hover:bg-black hover:text-white transition-colors">
                Adicionar
              </button>
            </div>
          </div>

        </div>
      </div>
    </main>
"""

def patch_conjuntos(content):
    start = content.find('<main')
    end = content.find('</main>') + 7
    if start != -1 and end != -1:
        return content[:start] + NEW_CONJUNTOS_MAIN + content[end:]
    return content

# Execute patches
for filepath in glob.glob("*.html"):
    if filepath == "carreira.html" or filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Patch Menu
    content = patch_menu(content)
    
    # 2. Patch Placeholders
    if filepath == "quartos.html":
        content = replace_main_products(content, "Quarto", 8)
    elif filepath == "salas.html":
        content = replace_main_products(content, "Sala", 8)
    elif filepath == "colchoes.html":
        content = replace_main_products(content, "Colchão", 4)
    elif filepath == "cozinha.html":
        content = replace_main_products(content, "Cozinha", 2)
    elif filepath == "escritorio.html":
        content = replace_main_products(content, "Escritório", 2)
        
    # 3. Patch Conjuntos
    if filepath == "conjuntos.html":
        content = patch_conjuntos(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All patches applied!")
