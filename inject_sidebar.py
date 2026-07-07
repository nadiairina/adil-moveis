import glob, re

SIDEBAR_HTML = """
    <!-- SLIDE-IN RIGHT SIDEBAR MENU -->
    <div id="menuOverlay" class="fixed inset-0 bg-black/50 z-[999] hidden transition-opacity duration-300 opacity-0">
      <!-- Sidebar container -->
      <div id="menuSidebar" class="absolute top-0 right-0 w-80 max-w-[85vw] h-full bg-[#FDFBF7] shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col">
          <!-- Header -->
          <div class="px-6 py-6 border-b border-[#EAE6DF] flex justify-between items-center bg-white">
              <span class="text-xs font-bold tracking-widest uppercase text-gray-500">Menu</span>
              <button id="closeMenuBtn" class="text-black hover:text-red-500 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
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
                  <a href="kids.html" class="text-lg font-medium text-gray-800 hover:text-black">Crianças / Kids</a>
                  <a href="escritorio.html" class="text-lg font-medium text-gray-800 hover:text-black">Escritórios</a>
                  <a href="complementos.html" class="text-lg font-medium text-gray-800 hover:text-black">Complementos</a>
                  <a href="conjuntos.html" class="text-lg font-bold text-[#C8B598] hover:text-[#b09e85]">✦ Comprar Packs</a>
                  <a href="catalogos.html" class="text-sm font-medium text-gray-500 hover:text-black pt-2">Catálogos PDF</a>
              </nav>
              
              <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-4 border-t border-[#EAE6DF] pt-8">Empresa</h3>
              <nav class="flex flex-col space-y-4">
                  <a href="empresa.html" class="text-sm font-medium text-gray-600 hover:text-black">A Nossa História</a>
                  <a href="testemunhos.html" class="text-sm font-medium text-gray-600 hover:text-black">Testemunhos</a>
                  <a href="servicos.html" class="text-sm font-medium text-gray-600 hover:text-black">Serviços</a>
                  <a href="tecidos.html" class="text-sm font-medium text-gray-600 hover:text-black">Guia de Tecidos</a>
                  <a href="contactos.html" class="text-sm font-medium text-gray-600 hover:text-black">Contactos & Lojas</a>
              </nav>
          </div>
          
          <!-- Footer -->
          <div class="p-6 bg-gray-50 border-t border-[#EAE6DF]">
              <a href="conjuntos.html" class="flex items-center justify-center w-full py-3 mb-3 bg-[#C8B598] text-white font-bold uppercase tracking-widest text-[11px] hover:bg-[#b09e85] transition-colors">
                Comprar Packs
              </a>
              <a href="contactos.html" class="flex items-center justify-center w-full py-3 mb-6 border border-black text-black font-bold uppercase tracking-widest text-[11px] hover:bg-black hover:text-white transition-colors">
                Agendar Visita à Loja
              </a>
              <div class="flex justify-between items-center">
                  <div>
                      <a href="tel:212582788" class="flex items-center text-sm font-bold text-black mb-1 hover:text-gray-600">
                        📞 212 582 788
                      </a>
                      <a href="https://wa.me/351960209396" target="_blank" class="flex items-center text-xs font-medium text-gray-500 hover:text-[#25D366] transition-colors">
                        💬 960 209 396
                      </a>
                  </div>
                  <div class="flex space-x-2">
                      <a href="https://www.facebook.com/p/Adil-M%C3%B3veis-100063641348118/" target="_blank" class="text-[#1877F2] bg-white p-2 rounded-full shadow-sm border border-gray-200 hover:scale-110 transition-transform">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                      </a>
                      <a href="https://www.instagram.com/adilmoveis/" target="_blank" class="text-[#E1306C] bg-white p-2 rounded-full shadow-sm border border-gray-200 hover:scale-110 transition-transform">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                      </a>
                  </div>
              </div>
          </div>
      </div>
    </div>

    <!-- Sidebar JS -->
    <script>
      (function() {
        document.addEventListener('DOMContentLoaded', function() {
          var hamburgerBtn = document.getElementById('hamburgerBtn');
          var closeMenuBtn = document.getElementById('closeMenuBtn');
          var menuOverlay = document.getElementById('menuOverlay');
          var menuSidebar = document.getElementById('menuSidebar');
          
          function openMenu() {
              menuOverlay.classList.remove('hidden');
              setTimeout(function() {
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
              setTimeout(function() {
                  menuOverlay.classList.add('hidden');
              }, 300);
              document.body.style.overflow = '';
          }

          if(hamburgerBtn) hamburgerBtn.addEventListener('click', openMenu);
          if(closeMenuBtn) closeMenuBtn.addEventListener('click', closeMenu);
          if(menuOverlay) {
              menuOverlay.addEventListener('click', function(e) {
                  if(e.target === menuOverlay) closeMenu();
              });
          }
        });
      })();
    </script>
"""

# Target pages - all that have hamburgerBtn but no sidebar panel
target_pages = [
    'catalogos.html','colchoes.html','complementos.html','conjuntos.html','contactos.html',
    'cozinha.html','empresa.html','escritorio.html','index.html','kids.html',
    'parceiros.html','produto-detalhe.html','quartos.html','salas.html',
    'servicos.html','tecidos.html','testemunhos.html'
]

for fn in target_pages:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any OLD sidebar scripts that reference menuOverlay/menuSidebar
        # but are orphaned (the ones right after </header>)
        content = re.sub(
            r'\s*<script>\s*//\s*Sidebar Menu Logic.*?</script>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Check if sidebar panel already injected
        if 'id="menuSidebar"' in content:
            print(f'Already has sidebar: {fn} - skipping')
            continue
        
        # Insert after the </header> tag
        content = content.replace('</header>', '</header>' + SIDEBAR_HTML, 1)
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Injected sidebar in: {fn}')
    except Exception as e:
        print(f'Error in {fn}: {e}')

print("Done!")
