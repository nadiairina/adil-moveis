import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. FIX MENU
# Find the absolute inset-0 z-0 in the Hero
hero_insert_point = content.find('<div class="absolute inset-0 z-0">')
if hero_insert_point != -1 and 'id="menuButton"' not in content:
    # We need to insert the menu before the background image but inside the hero section.
    # Actually, let's insert it inside the <section class="relative h-screen...">
    
    menu_html = """
        <!-- Logo and Menu positioning container -->
        <div class="absolute top-0 left-0 w-full z-20 flex justify-between items-center p-6">
          <a href="index.html">
            <img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-10 md:h-14 w-auto bg-white/90 rounded-md p-1 shadow-sm hover:scale-105 transition-transform">
          </a>
          
          <button 
            class="flex items-center space-x-2 text-black bg-white/90 hover:bg-white backdrop-blur-md py-2 px-4 rounded-full shadow-lg transition-all"
            id="menuButton"
          >
            <span class="uppercase font-semibold tracking-widest text-xs">MENU</span>
            <i data-feather="menu" class="w-5 h-5"></i>
          </button>
        </div>
    """
    content = content[:hero_insert_point] + menu_html + "\n        " + content[hero_insert_point:]

# 2. FIX TEXT LEGIBILITY
# Hero overlay needs to be darker
content = content.replace('opacity-60 scale-105 transform origin-center"', 'opacity-40 scale-105 transform origin-center"')

# 3. BRING BACK THE 8-GRID
# We will replace the "NOVO GRID" section with the 8-grid she wants.
# Let's find the "NOVO GRID" section:
grid_start = content.find('<!-- NOVO GRID (Mais Imagens) -->')
grid_end = content.find('<!-- SERVIÇO APPLE STYLE -->')

if grid_start != -1 and grid_end != -1:
    EIGHT_GRID = """
      <!-- 8-GRID CATEGORIAS (Pedido da Cliente) -->
      <section class="py-24 bg-white">
        <div class="container mx-auto px-4 max-w-7xl">
           <div class="text-center mb-16" data-aos="fade-up">
            <h2 class="text-4xl font-semibold text-black tracking-tight mb-4">Explore por divisão.</h2>
          </div>
          
           <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
            <!-- 1 -->
            <a href="quartos.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="0">
              <img src="https://nadiairina.github.io/adil-moveis/images/Lourini-Majestic.jpg" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Quartos</span>
              </div>
            </a>
            <!-- 2 -->
            <a href="colchoes.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="100">
              <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Colchões</span>
              </div>
            </a>
            <!-- 3 -->
            <a href="salas.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="200">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Salas</span>
              </div>
            </a>
            <!-- 4 -->
            <a href="escritorio.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="300">
              <img src="https://lourini.pt/app/uploads/2024/09/escritorio-nizza-1200x1200.png" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Escritório</span>
              </div>
            </a>
            <!-- 5 -->
            <a href="cozinha.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="0">
              <img src="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Cozinha</span>
              </div>
            </a>
            <!-- 6 -->
            <a href="complementos.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="100">
              <img src="https://lourini.pt/app/uploads/2024/07/camiseiro-1200x1200.png" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Complementos</span>
              </div>
            </a>
            <!-- 7 -->
            <a href="kids.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="200">
              <img src="https://lourini.pt/app/uploads/2024/07/quarto-juvenil-1200x1200.png" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Kids</span>
              </div>
            </a>
            <!-- 8 -->
            <a href="tecidos.html" class="group relative block aspect-square bg-black overflow-hidden rounded-2xl" data-aos="fade-up" data-aos-delay="300">
              <img src="https://lourini.pt/app/uploads/2024/07/tecido-amostra.jpg" class="w-full h-full object-cover opacity-60 group-hover:opacity-80 group-hover:scale-105 transition-all duration-700" onerror="this.src='https://lourini.pt/app/uploads/2024/07/cadeira-estofada-1200x1200.webp'">
              <div class="absolute inset-0 flex items-center justify-center">
                 <span class="text-white text-lg md:text-xl font-bold tracking-widest uppercase drop-shadow-lg">Tecidos</span>
              </div>
            </a>
           </div>
        </div>
      </section>
"""
    content = content[:grid_start] + EIGHT_GRID + "\n      " + content[grid_end:]

# 4. FIX TEXT LEGIBILITY ON APPLE SPLIT GRIDS
# Left block (Dark) - Make image opacity 30%
content = content.replace('opacity-40 group-hover:opacity-50 transition-opacity', 'opacity-30 group-hover:opacity-40 transition-opacity')
# Right block (Light) - The text is black, it's fine.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu restored, grid recreated, legibility fixed.")
