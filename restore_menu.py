import os
import glob
import re

# We will replace the current menuOverlay block entirely.
MENU_START_REGEX = r'      <!-- Menu Overlay.*?-->'
MENU_END_REGEX = r'      </div>\s*</header>'

NEW_MENU = """      <!-- Menu Overlay -->
      <div id="menuOverlay" class="fixed inset-0 bg-white z-50 overflow-y-auto hidden h-screen text-black flex-col justify-start items-center pt-20">
        <button id="closeMenuButton" class="absolute top-6 right-6 text-black hover:text-gray-500 transition-colors">
          <i data-feather="x" class="w-8 h-8"></i>
        </button>
        
        <div class="w-full max-w-md px-6 flex flex-col space-y-4">
          <a href="index.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">INÍCIO</a>
          <a href="quartos.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">QUARTOS</a>
          <a href="colchoes.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">COLCHÕES</a>
          <a href="salas.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">SALAS</a>
          <a href="escritorio.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">ESCRITÓRIO</a>
          <a href="cozinha.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">COZINHA</a>
          <a href="complementos.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">COMPLEMENTOS</a>
          <a href="kids.html" class="text-xl font-medium border-b border-gray-100 pb-2 hover:text-gray-500">KIDS</a>
          <a href="conjuntos.html" class="text-xl font-bold pb-2 hover:text-gray-500">PACKS / CONJUNTOS</a>
          
          <div class="h-4"></div> <!-- Espaçador -->
          
          <a href="tecidos.html" class="text-lg text-gray-600 hover:text-black">TECIDOS</a>
          <a href="servicos.html" class="text-lg text-gray-600 hover:text-black">SERVIÇOS</a>
          <a href="testemunhos.html" class="text-lg text-gray-600 hover:text-black">TESTEMUNHOS</a>
          <a href="parceiros.html" class="text-lg text-gray-600 hover:text-black">PARCEIROS</a>
          <a href="catalogos.html" class="text-lg text-gray-600 hover:text-black">CATÁLOGOS</a>
          <a href="contactos.html" class="text-lg font-bold text-black mt-4 hover:text-gray-500">CONTACTOS & LOJAS</a>
        </div>
"""

def restore_menu(content):
    # Regex to find the start of the menu
    match_start = re.search(MENU_START_REGEX, content)
    if not match_start: return content
    
    idx_start = match_start.start()
    
    # We need to find the </header> and replace up to there
    # since we know the menu is the last thing inside <header>
    idx_end = content.find('</header>', idx_start)
    if idx_end == -1: return content
    
    return content[:idx_start] + NEW_MENU + content[idx_end:]

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = restore_menu(content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Menu restored with all pages and normal fonts!")
