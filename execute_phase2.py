import os
import glob
import shutil

# 1. COPY LOGO TO WORKSPACE
logo_src = "/Users/nadiairina/.gemini/antigravity/brain/502f30d9-087b-4abb-aa43-5415751003ff/adil_moveis_logo_1781031440275.png"
logo_dest = "images/adil_moveis_new_logo.png"
if os.path.exists(logo_src):
    shutil.copy(logo_src, logo_dest)

# 2. UNIFIED NAVBAR HTML
NEW_NAVBAR = """    <!-- STICKY NAVBAR -->
    <header class="sticky top-0 z-50 bg-[#FDFBF7] shadow-sm border-b border-[#EAE6DF]">
      <div class="container mx-auto px-4 lg:px-8">
        <div class="flex items-center justify-between h-20">
          
          <!-- Logo -->
          <a href="index.html" class="flex-shrink-0">
            <img src="images/adil_moveis_new_logo.png" alt="Adil Móveis" class="h-16 w-auto mix-blend-multiply">
          </a>
          
          <!-- Desktop Menu (Centered) -->
          <nav class="hidden lg:flex items-center space-x-8">
            <a href="index.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Início</a>
            <a href="quartos.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Quartos</a>
            <a href="salas.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Salas</a>
            <a href="cozinha.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Cozinhas</a>
            <a href="colchoes.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Colchões</a>
            <a href="conjuntos.html" class="text-sm font-bold tracking-widest text-black uppercase transition-colors relative">
              Packs
              <span class="absolute -top-3 -right-4 bg-red-600 text-white text-[10px] px-1.5 py-0.5 rounded-full rotate-12">Hot</span>
            </a>
            <a href="catalogos.html" class="text-sm font-medium tracking-widest text-gray-500 hover:text-black uppercase transition-colors">Catálogos</a>
          </nav>
          
          <!-- Right Side: Cart & Mobile Menu -->
          <div class="flex items-center space-x-6">
            <a href="contactos.html" class="hidden md:inline-block text-xs font-bold tracking-widest uppercase border border-black px-4 py-2 hover:bg-black hover:text-white transition-colors">Contactos</a>
            
            <button class="snipcart-checkout flex items-center space-x-2 text-black hover:text-gray-600 transition-colors group">
              <div class="relative">
                <i data-feather="shopping-bag" class="w-6 h-6"></i>
                <span class="snipcart-items-count absolute -top-1 -right-2 bg-black text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold">0</span>
              </div>
              <span class="snipcart-total-price hidden sm:block text-sm font-semibold">0.00€</span>
            </button>
            
            <!-- Mobile Menu Toggle -->
            <button class="lg:hidden text-black" id="mobileMenuBtn">
              <i data-feather="menu" class="w-6 h-6"></i>
            </button>
          </div>
          
        </div>
      </div>
      
      <!-- Mobile Dropdown -->
      <div id="mobileDropdown" class="hidden lg:hidden bg-[#FDFBF7] border-t border-[#EAE6DF] px-4 py-6 space-y-4 shadow-lg absolute w-full">
        <a href="index.html" class="block text-sm font-medium tracking-widest text-gray-800 uppercase">Início</a>
        <a href="quartos.html" class="block text-sm font-medium tracking-widest text-gray-800 uppercase">Quartos</a>
        <a href="salas.html" class="block text-sm font-medium tracking-widest text-gray-800 uppercase">Salas</a>
        <a href="cozinha.html" class="block text-sm font-medium tracking-widest text-gray-800 uppercase">Cozinhas</a>
        <a href="colchoes.html" class="block text-sm font-medium tracking-widest text-gray-800 uppercase">Colchões</a>
        <a href="conjuntos.html" class="block text-sm font-bold tracking-widest text-black uppercase">Packs</a>
        <a href="catalogos.html" class="block text-sm font-medium tracking-widest text-gray-500 uppercase">Catálogos</a>
        <a href="contactos.html" class="block text-sm font-bold tracking-widest text-gray-500 uppercase pt-4 border-t border-[#EAE6DF]">Contactos & Lojas</a>
      </div>
    </header>
    
    <script>
      // Simple Mobile Menu Toggle
      document.addEventListener('DOMContentLoaded', () => {
        const btn = document.getElementById('mobileMenuBtn');
        const menu = document.getElementById('mobileDropdown');
        if(btn && menu) {
          btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
          });
        }
      });
    </script>
"""

# FLOATING WHATSAPP PILL
NEW_WPP = """    <!-- WhatsApp Floating Pill -->
    <a href="https://wa.me/351212582788" target="_blank" rel="noopener noreferrer" class="fixed bottom-6 right-6 z-50 bg-[#25D366] text-white px-5 py-3 rounded-full shadow-2xl flex items-center space-x-2 hover:bg-[#1ebd5a] hover:-translate-y-1 transition-all duration-300 group">
      <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor">
        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.514 2.266 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.504-5.731-1.464L0 24zm6.59-4.846c1.6.95 3.198 1.451 4.782 1.452 5.424 0 9.835-4.354 9.838-9.702.002-2.592-1.01-5.029-2.85-6.87C16.579 2.193 14.15 1.18 11.56 1.18 6.13 1.18 1.72 5.534 1.717 10.882c0 1.631.426 3.224 1.235 4.633L1.925 21.87l6.236-1.636zM17.154 14c-.284-.143-1.68-.829-1.94-.924-.259-.096-.448-.143-.637.143-.19.285-.733.924-.899 1.113-.165.19-.33.213-.614.072-2.012-1.01-3.136-1.785-4.385-3.928-.328-.564-.108-.874.116-1.096.2-.2.448-.523.673-.784.09-.105.15-.175.226-.245.075-.07.15-.14.226-.21.226-.226.376-.44.527-.722.15-.285.075-.544-.038-.722-.113-.178-.899-2.163-1.233-2.969-.328-.79-.663-.684-.899-.696-.23-.012-.495-.015-.756-.015-.262 0-.687.098-.946.381-.26.285-.99 1.012-.99 2.47 0 1.457 1.06 2.871 1.21 3.062.15.19 2.085 3.184 5.052 4.466.706.305 1.258.487 1.687.623.708.226 1.353.194 1.862.118.568-.084 1.681-.687 1.916-1.353.235-.667.235-1.238.165-1.353-.07-.115-.26-.19-.544-.332z"/>
      </svg>
      <span class="font-bold text-sm tracking-wide group-hover:block">Dúvidas ou Orçamentos?</span>
    </a>"""


for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # REMOVE OLD HEADER AND DRAWER
    header_start = content.find('<header>')
    header_end = content.find('</header>')
    if header_start != -1 and header_end != -1:
        # replace the entire <header>...</header> with NEW_NAVBAR
        content = content[:header_start] + NEW_NAVBAR + content[header_end+9:]

    # For index.html, remove the old floating logo/menu buttons inside the Hero section
    if filepath == 'index.html':
        old_hero_nav_start = content.find('<!-- Logo and Menu positioning container -->')
        if old_hero_nav_start != -1:
            old_hero_nav_end = content.find('</div>', content.find('id="menuButton"')) + 6
            if old_hero_nav_end != -1:
                content = content[:old_hero_nav_start] + content[old_hero_nav_end:]
    
    # REMOVE OLD WPP BUBBLE
    wpp_start = content.find('<!-- WhatsApp Floating Button -->')
    wpp_end = content.find('</a>', wpp_start) + 4
    if wpp_start != -1 and wpp_end != -1:
        content = content[:wpp_start] + content[wpp_end:]
    
    # ADD NEW WPP PILL right before </body>
    if '<!-- WhatsApp Floating Pill -->' not in content:
        content = content.replace('</body>', NEW_WPP + '\n</body>')

    # CHANGE GLOBAL BACKGROUND COLORS TO WARM BEIGE #FDFBF7
    content = content.replace('bg-white', 'bg-[#FDFBF7]')
    content = content.replace('bg-[#f5f5f7]', 'bg-[#F9F6F0]') # A slightly darker beige for contrast

    # Also apply the background color to the body
    content = content.replace('<body class="', '<body class="bg-[#FDFBF7] ')
    if '<body class="' not in content:
        content = content.replace('<body>', '<body class="bg-[#FDFBF7] text-[#2c2a29] font-sans antialiased">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update task.md
with open('artifacts/task.md', 'r', encoding='utf-8') as f:
    task_content = f.read()

task_content = task_content.replace('[ ] Remover a top bar', '[x] Remover a top bar')
task_content = task_content.replace('[ ] Criar uma Navbar', '[x] Criar uma Navbar')
task_content = task_content.replace('[ ] Substituir o botão', '[x] Substituir o botão')
task_content = task_content.replace('`[ ]` 1. **Header', '`[/]` 1. **Header')

task_content = task_content.replace('[ ] Mudar a cor de fundo global', '[x] Mudar a cor de fundo global')
task_content = task_content.replace('[ ] Gerar um novo logótipo', '[x] Gerar um novo logótipo')
task_content = task_content.replace('[ ] Inserir o novo logótipo na Navbar', '[x] Inserir o novo logótipo na Navbar')
task_content = task_content.replace('`[ ]` 2. **Cores', '`[/]` 2. **Cores')

task_content = task_content.replace('[ ] Criar um botão flutuante em formato "pílula"', '[x] Criar um botão flutuante em formato "pílula"')
task_content = task_content.replace('`[ ]` 3. **WhatsApp', '`[/]` 3. **WhatsApp')

with open('artifacts/task.md', 'w', encoding='utf-8') as f:
    f.write(task_content)

print("Phase 2 UI implemented: Navbar, Colors, Logo, and WhatsApp Pill!")
