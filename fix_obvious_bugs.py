import glob
import os
import re

# 1. FIX THE DOUBLE MENU IN INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# The old floating menu block usually looks like:
# <div class="absolute top-0 left-0 w-full z-10 flex justify-between items-center p-4">
# ...
# </div>
start_idx = idx_content.find('<div class="absolute top-0 left-0 w-full z-10 flex justify-between items-center p-4">')
if start_idx != -1:
    # Find the closing div for this container. 
    # Since it contains the logo <a> and the button <button>, it should close right before the hero content starts.
    end_idx = idx_content.find('</div>\n      \n  <!-- Page Header', start_idx)
    if end_idx == -1:
        # Fallback to looking for the end of the button
        end_idx = idx_content.find('</button>\n  </div>', start_idx) + 17
        
    if end_idx != -1:
        idx_content = idx_content[:start_idx] + idx_content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)


# 2. REDESIGN THE MENU (From Full-Screen Overlay to a clean Right Sidebar Drawer)
NEW_SIDEBAR_MENU = """      <!-- SLIDE-IN RIGHT SIDEBAR MENU -->
      <div id="menuOverlay" class="fixed inset-0 bg-black/50 z-[60] hidden transition-opacity duration-300 opacity-0">
        <!-- Sidebar container -->
        <div id="menuSidebar" class="absolute top-0 right-0 w-80 max-w-[85vw] h-full bg-[#FDFBF7] shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col">
            <!-- Header -->
            <div class="px-6 py-6 border-b border-[#EAE6DF] flex justify-between items-center bg-white">
                <span class="text-xs font-bold tracking-widest uppercase text-gray-500">Menu</span>
                <button id="closeMenuBtn" class="text-black hover:text-red-500 transition-colors">
                    <i data-feather="x" class="w-6 h-6"></i>
                </button>
            </div>
            
            <!-- Links -->
            <div class="flex-1 overflow-y-auto px-6 py-8">
                <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-4">Loja</h3>
                <nav class="flex flex-col space-y-4 mb-8">
                    <a href="quartos.html" class="text-lg font-medium text-gray-800 hover:text-black">Quartos</a>
                    <a href="salas.html" class="text-lg font-medium text-gray-800 hover:text-black">Salas</a>
                    <a href="cozinha.html" class="text-lg font-medium text-gray-800 hover:text-black">Cozinhas</a>
                    <a href="colchoes.html" class="text-lg font-medium text-gray-800 hover:text-black">Colchões</a>
                    <a href="conjuntos.html" class="text-lg font-bold text-black border-l-2 border-black pl-3 -ml-3">Comprar Packs</a>
                    <a href="catalogos.html" class="text-sm font-medium text-gray-500 hover:text-black pt-2">Catálogos PDF</a>
                </nav>
                
                <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-4 border-t border-[#EAE6DF] pt-8">Empresa</h3>
                <nav class="flex flex-col space-y-4">
                    <a href="testemunhos.html" class="text-sm font-medium text-gray-600 hover:text-black">Testemunhos</a>
                    <a href="servicos.html" class="text-sm font-medium text-gray-600 hover:text-black">Serviços</a>
                    <a href="tecidos.html" class="text-sm font-medium text-gray-600 hover:text-black">Guia de Tecidos</a>
                    <a href="contactos.html" class="text-sm font-medium text-gray-600 hover:text-black">Contactos & Lojas</a>
                </nav>
            </div>
            
            <!-- Footer -->
            <div class="p-6 bg-gray-50 border-t border-[#EAE6DF]">
                <a href="tel:212582788" class="flex items-center text-sm font-bold text-black mb-2 hover:text-gray-600">
                    <i data-feather="phone" class="w-4 h-4 mr-2"></i> 212 582 788
                </a>
                <p class="text-xs text-gray-500">Rua do Feijó, 123 - Almada</p>
            </div>
        </div>
      </div>
    </header>
    
    <script>
      // Sidebar Menu Logic
      document.addEventListener('DOMContentLoaded', () => {
        const hamburgerBtn = document.getElementById('hamburgerBtn');
        const closeMenuBtn = document.getElementById('closeMenuBtn');
        const menuOverlay = document.getElementById('menuOverlay');
        const menuSidebar = document.getElementById('menuSidebar');
        
        function openMenu() {
            menuOverlay.classList.remove('hidden');
            setTimeout(() => {
                menuOverlay.classList.remove('opacity-0');
                menuOverlay.classList.add('opacity-100');
                menuSidebar.classList.remove('translate-x-full');
            }, 10);
            document.body.style.overflow = 'hidden';
        }
        
        function closeMenu() {
            menuSidebar.classList.add('translate-x-full');
            menuOverlay.classList.remove('opacity-100');
            menuOverlay.classList.add('opacity-0');
            setTimeout(() => {
                menuOverlay.classList.add('hidden');
            }, 300);
            document.body.style.overflow = '';
        }

        if(hamburgerBtn) hamburgerBtn.addEventListener('click', openMenu);
        if(closeMenuBtn) closeMenuBtn.addEventListener('click', closeMenu);
        if(menuOverlay) {
            menuOverlay.addEventListener('click', (e) => {
                if(e.target === menuOverlay) closeMenu();
            });
        }
      });
    </script>
"""

# 3. FIX LOGO AND APPLY NEW MENU
for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the old full screen menu with the slide-in sidebar
    menu_start = content.find('<!-- FULL SCREEN MENU OVERLAY (Side Drawer) -->')
    menu_end = content.find('</script>', menu_start) + 9
    
    if menu_start != -1 and menu_end != -1:
        content = content[:menu_start] + NEW_SIDEBAR_MENU + content[menu_end:]

    # Fix the Logo! She wants it rounded, with a border, and NO black background
    # Since it's white bg and black text, we just show it normally inside a nice circle.
    content = content.replace(
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-auto invert mix-blend-multiply opacity-90 hover:opacity-100 transition-opacity">',
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-14 md:w-16 object-cover bg-white rounded-full border-2 border-gray-200 shadow-sm p-1">'
    )
    # Also handle index.html where it might not have the classes exactly matching if modified differently
    content = content.replace(
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-auto">',
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-14 md:w-16 object-cover bg-white rounded-full border-2 border-gray-200 shadow-sm p-1">'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# 4. FIX COZINHA.HTML SPECIFICALLY
with open('cozinha.html', 'r', encoding='utf-8') as f:
    cozinha = f.read()

# Let's completely overwrite the <main> block for Cozinha so we guarantee it has 8 items
COZINHA_MAIN = """    <main class="bg-white py-16">
      <div class="container mx-auto px-4 max-w-7xl">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-5xl font-light mb-4 tracking-tight text-black" data-aos="fade-down">Cozinhas</h1>
          <p class="text-xl text-gray-500 max-w-2xl mx-auto font-light" data-aos="fade-up" data-aos-delay="200">Explore a nossa seleção de produtos de excelência para a sua cozinha.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">"""

for i in range(1, 9):
    COZINHA_MAIN += f"""
          <div class="product group cursor-pointer" data-category="all">
            <div class="relative overflow-hidden bg-[#f0f0f0] rounded-xl mb-4 aspect-square">
              <img src="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp" alt="Produto" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
            <h3 class="text-lg font-bold text-black mb-1">Mesa Cozinha Premium {i}</h3>
            <p class="text-gray-500 text-sm mb-3">Qualidade Adil Móveis</p>
            <button class="snipcart-add-item w-full py-3 border border-black text-black font-bold uppercase tracking-widest text-xs hover:bg-black hover:text-white transition-colors"
              data-item-id="prod-cozinha-{i}"
              data-item-price="0.00"
              data-item-name="Mesa Cozinha Premium {i}"
              data-item-image="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp">
              Ver Detalhes
            </button>
          </div>"""

COZINHA_MAIN += """
        </div>
      </div>
    </main>"""

main_start = cozinha.find('<main')
main_end = cozinha.find('</main>') + 7
if main_start != -1 and main_end != -1:
    cozinha = cozinha[:main_start] + COZINHA_MAIN + cozinha[main_end:]
    with open('cozinha.html', 'w', encoding='utf-8') as f:
        f.write(cozinha)

print("Obvious bugs fixed: Double menu removed, Logo rounded/visible, Sidebar menu implemented, Cozinha products forced to 8.")
