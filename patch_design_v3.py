import os
import glob
import re

MENU_START_REGEX = r'      <!-- Menu Overlay.*?-->'
MENU_END_REGEX = r'      </div>\s*</header>'

NEW_MENU = """      <!-- Menu Overlay (Side Drawer) -->
      <div id="menuOverlay" class="fixed inset-0 z-50 hidden">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black bg-opacity-40" id="closeMenuBackdrop"></div>
        
        <!-- Drawer -->
        <div class="absolute top-0 right-0 w-full sm:w-[400px] h-screen bg-white shadow-2xl flex flex-col overflow-hidden">
          <!-- Header -->
          <div class="flex justify-between items-center p-8 border-b border-gray-100">
            <span class="text-xl font-bold tracking-widest uppercase">Menu</span>
            <button id="closeMenuButton" class="text-black hover:text-gray-500 transition-colors">
              <i data-feather="x" class="w-8 h-8"></i>
            </button>
          </div>
          
          <!-- Links -->
          <div class="flex-grow overflow-y-auto p-8">
            <nav class="flex flex-col space-y-5">
              <a href="index.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Início</a>
              <a href="quartos.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Quartos</a>
              <a href="colchoes.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Colchões</a>
              <a href="salas.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Salas</a>
              <a href="escritorio.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Escritório</a>
              <a href="cozinha.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Cozinha</a>
              <a href="complementos.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Complementos</a>
              <a href="kids.html" class="text-xl font-medium text-gray-800 hover:text-black hover:pl-2 transition-all">Kids</a>
              
              <div class="h-px bg-gray-200 my-4"></div>
              
              <a href="conjuntos.html" class="text-xl font-bold text-black uppercase tracking-wide hover:pl-2 transition-all">Packs / Conjuntos</a>
              
              <div class="h-px bg-gray-200 my-4"></div>
              
              <a href="tecidos.html" class="text-sm font-semibold tracking-wider text-gray-500 hover:text-black uppercase transition-colors">Tecidos</a>
              <a href="servicos.html" class="text-sm font-semibold tracking-wider text-gray-500 hover:text-black uppercase transition-colors">Serviços</a>
              <a href="testemunhos.html" class="text-sm font-semibold tracking-wider text-gray-500 hover:text-black uppercase transition-colors">Testemunhos</a>
              <a href="parceiros.html" class="text-sm font-semibold tracking-wider text-gray-500 hover:text-black uppercase transition-colors">Parceiros</a>
              <a href="catalogos.html" class="text-sm font-semibold tracking-wider text-gray-500 hover:text-black uppercase transition-colors">Catálogos</a>
            </nav>
          </div>
          
          <!-- Footer -->
          <div class="p-8 border-t border-gray-100">
            <a href="contactos.html" class="block w-full text-center bg-black text-white py-4 text-sm font-bold uppercase tracking-widest hover:bg-gray-800 transition-colors">
              Contactos & Lojas
            </a>
          </div>
        </div>
        
        <!-- Inline Script to make Backdrop close the menu -->
        <script>
          document.getElementById('closeMenuBackdrop')?.addEventListener('click', function() {
            document.getElementById('menuOverlay').classList.add('hidden');
          });
        </script>
      </div>
"""

def restore_menu(content):
    match_start = re.search(MENU_START_REGEX, content)
    if not match_start: return content
    
    idx_start = match_start.start()
    idx_end = content.find('</header>', idx_start)
    if idx_end == -1: return content
    
    return content[:idx_start] + NEW_MENU + content[idx_end:]


BENEFITS_SECTION = """
    <!-- Benefícios Premium -->
    <section class="py-24 bg-black text-white relative">
      <div class="container mx-auto px-4 max-w-7xl relative z-10">
        <div class="text-center mb-20">
          <h2 class="text-sm font-bold tracking-widest uppercase text-gray-400 mb-6">Porque nos escolher?</h2>
          <h3 class="text-4xl md:text-6xl font-bold leading-tight">O serviço premium que as<br>grandes superfícies não têm.</h3>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-16 text-center">
          <!-- Beneficio 1 -->
          <div class="flex flex-col items-center group">
            <div class="w-24 h-24 bg-white text-black rounded-full flex items-center justify-center mb-8 transform group-hover:-translate-y-2 transition-transform duration-300">
              <i data-feather="truck" class="w-12 h-12"></i>
            </div>
            <h4 class="text-3xl font-bold mb-6">Entrega Grátis</h4>
            <p class="text-gray-400 text-xl leading-relaxed">Sem taxas escondidas. Levamos as suas novas peças até si com todo o cuidado, de forma totalmente gratuita.</p>
          </div>
          
          <!-- Beneficio 2 -->
          <div class="flex flex-col items-center group">
            <div class="w-24 h-24 bg-white text-black rounded-full flex items-center justify-center mb-8 transform group-hover:-translate-y-2 transition-transform duration-300">
              <i data-feather="tool" class="w-12 h-12"></i>
            </div>
            <h4 class="text-3xl font-bold mb-6">Montagem Incluída</h4>
            <p class="text-gray-400 text-xl leading-relaxed">A nossa equipa de especialistas monta os móveis na divisão que escolher. Não precisa de se preocupar com ferramentas.</p>
          </div>
          
          <!-- Beneficio 3 -->
          <div class="flex flex-col items-center group">
            <div class="w-24 h-24 bg-white text-black rounded-full flex items-center justify-center mb-8 transform group-hover:-translate-y-2 transition-transform duration-300">
              <i data-feather="refresh-cw" class="w-12 h-12"></i>
            </div>
            <h4 class="text-3xl font-bold mb-6">Recolha de Usados</h4>
            <p class="text-gray-400 text-xl leading-relaxed">Levamos o seu colchão ou sofá velho para reciclar no mesmo dia em que lhe entregamos o novo. Problema resolvido.</p>
          </div>
        </div>
      </div>
    </section>
"""

def add_benefits_to_index(content):
    if "Benefícios Premium" in content:
        return content # already added
        
    # We want to insert it right after the Hero section
    # Let's find </section> after the hero. 
    # Usually it's after the div with 'VER CATÁLOGOS'
    
    match = re.search(r'</section>\s*<!-- Categories Section -->', content)
    if not match: return content
    
    insert_idx = match.start() + 10 # right after </section>
    
    return content[:insert_idx] + "\n" + BENEFITS_SECTION + "\n" + content[insert_idx:]

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = restore_menu(content)
    
    if filepath == "index.html":
        new_content = add_benefits_to_index(new_content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Menu redesigned to sidebar and benefits added to index!")
