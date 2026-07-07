import glob
import re
import os

# 1. FIX SNIPCART PRICE FLASH AND ADD ACTIVE MENU UNDERLINE JS
ACTIVE_LINK_JS = """
    <!-- Active Link Underline Logic -->
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        let currentPath = window.location.pathname.split('/').pop() || 'index.html';
        
        // Find links in the top nav
        const topNavLinks = document.querySelectorAll('header nav a');
        topNavLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                // If it's the red Packs button, maybe don't underline, or use a red underline
                if (link.textContent.includes('Packs')) {
                    link.classList.add('underline', 'decoration-2', 'underline-offset-8');
                } else {
                    link.classList.add('underline', 'decoration-2', 'underline-offset-8', 'text-black');
                }
            }
        });
        
        // Find links in the sidebar nav
        const sideNavLinks = document.querySelectorAll('#menuSidebar nav a');
        sideNavLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('underline', 'decoration-2', 'underline-offset-4');
            }
        });
      });
    </script>
"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Empty the snipcart total price so it doesn't flash 0.00€ before Snipcart formats it
    content = content.replace('<span class="snipcart-total-price hidden sm:block text-sm font-semibold">0.00€</span>',
                              '<span class="snipcart-total-price hidden sm:block text-sm font-semibold"></span>')

    # Add active link JS right before </body>
    if 'Active Link Underline Logic' not in content:
        content = content.replace('</body>', ACTIVE_LINK_JS + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# 2. FORCE 8 PRODUCTS ON COZINHA.HTML
with open('cozinha.html', 'r', encoding='utf-8') as f:
    cozinha = f.read()

PRODUCTS_GRID_8 = """
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
"""
for i in range(1, 9):
    PRODUCTS_GRID_8 += f"""
        <div class="product " data-aos="fade-up" data-aos-delay="{i*50}" bg-[#FDFBF7] rounded-lg shadow-sm border border-gray-100 overflow-hidden flex flex-col group">
          <div class="relative h-64 bg-[#f0ede6] flex items-center justify-center overflow-hidden">
            <img src="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
          </div>
          <div class="p-6 flex flex-col flex-grow text-center">
            <h3 class="text-lg font-bold text-black mb-2">Cozinha Modelo {i}</h3>
            <p class="text-gray-500 text-sm mb-4">Pendente de catálogo</p>
            <button class="mt-auto bg-black text-white w-full py-3 text-xs font-bold uppercase tracking-wider hover:bg-gray-800 transition-colors rounded snipcart-add-item"
              data-item-id="cozinha-mod-{i}"
              data-item-price="0.00"
              data-item-name="Cozinha Modelo {i}"
              data-item-image="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp">
              Ver Mais
            </button>
          </div>
        </div>
"""
PRODUCTS_GRID_8 += "    </div>"

# Use regex to replace the entire <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">...</div>
# inside the <section class="py-16 bg-[#FDFBF7]">
pattern = r'<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">.*?</div>\s*</div>\s*</section>'
replacement = PRODUCTS_GRID_8 + "\n  </div>\n</section>"
cozinha = re.sub(pattern, replacement, cozinha, flags=re.DOTALL)

with open('cozinha.html', 'w', encoding='utf-8') as f:
    f.write(cozinha)


# 3. REDESIGN SERVICOS.HTML
with open('servicos.html', 'r', encoding='utf-8') as f:
    servicos = f.read()

# We completely overwrite the main block of servicos
servicos_main = """
    <main class="bg-[#FDFBF7]">
      <!-- Hero -->
      <section class="relative bg-black flex flex-col items-center justify-center overflow-hidden" style="height: 60vh;">
        <div class="absolute inset-0 z-0">
          <img src="https://lourini.pt/app/uploads/2024/09/dennis-32-1200x1200.webp" class="w-full h-full object-cover scale-105 transform origin-center opacity-60" alt="Serviços" data-aos="zoom-out" data-aos-duration="2000">
          <div class="absolute inset-0 bg-black/40 z-10"></div>
        </div>
        <div class="relative z-20 text-center px-4" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="text-white text-4xl md:text-6xl font-light tracking-widest mb-4 uppercase drop-shadow-2xl">O Nosso Compromisso</h1>
          <p class="text-white/90 text-lg md:text-xl font-light max-w-2xl mx-auto">Experiência premium desde a escolha até ao conforto da sua casa.</p>
        </div>
      </section>

      <!-- Services Grid -->
      <section class="py-24">
        <div class="container mx-auto px-4 max-w-6xl">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-16 text-center">
            
            <div data-aos="fade-up" data-aos-delay="0">
              <div class="w-20 h-20 mx-auto bg-[#F0EDE6] rounded-full flex items-center justify-center mb-8 border border-[#EAE6DF]">
                <i data-feather="truck" class="w-8 h-8 text-black"></i>
              </div>
              <h3 class="text-2xl font-semibold mb-4 text-black">Entrega Gratuita</h3>
              <p class="text-gray-500 font-light leading-relaxed">Garantimos transporte seguro e gratuito para todas as encomendas num raio de 50km da nossa loja em Almada (Lisboa e Setúbal).</p>
            </div>

            <div data-aos="fade-up" data-aos-delay="100">
              <div class="w-20 h-20 mx-auto bg-[#F0EDE6] rounded-full flex items-center justify-center mb-8 border border-[#EAE6DF]">
                <i data-feather="tool" class="w-8 h-8 text-black"></i>
              </div>
              <h3 class="text-2xl font-semibold mb-4 text-black">Montagem Especializada</h3>
              <p class="text-gray-500 font-light leading-relaxed">A nossa equipa de técnicos profissionais efetua a montagem completa dos seus móveis sem qualquer custo adicional no local de entrega.</p>
            </div>

            <div data-aos="fade-up" data-aos-delay="200">
              <div class="w-20 h-20 mx-auto bg-[#F0EDE6] rounded-full flex items-center justify-center mb-8 border border-[#EAE6DF]">
                <i data-feather="smile" class="w-8 h-8 text-black"></i>
              </div>
              <h3 class="text-2xl font-semibold mb-4 text-black">Atendimento Personalizado</h3>
              <p class="text-gray-500 font-light leading-relaxed">Ajudamos a desenhar o seu espaço ideal. Personalize medidas, cores e tecidos com a ajuda dos nossos consultores experientes.</p>
            </div>

          </div>
          
          <div class="text-center mt-20" data-aos="fade-up">
            <a href="contactos.html" class="inline-block bg-black text-white px-10 py-4 rounded font-bold uppercase tracking-widest text-sm hover:bg-gray-800 transition-colors shadow-lg">Fale com um Especialista</a>
          </div>
        </div>
      </section>
    </main>
"""
# Replace everything between </header> and the footer/newsletter
pattern = r'</header>.*?<section class="bg-\[#f0ede6\]'
servicos = re.sub(pattern, '</header>\n' + servicos_main + '\n<section class="bg-[#f0ede6]', servicos, flags=re.DOTALL)
with open('servicos.html', 'w', encoding='utf-8') as f:
    f.write(servicos)


# 4. REDESIGN TECIDOS.HTML
with open('tecidos.html', 'r', encoding='utf-8') as f:
    tecidos = f.read()

tecidos_main = """
    <main class="bg-[#FDFBF7]">
      <!-- Hero -->
      <section class="relative bg-black flex flex-col items-center justify-center overflow-hidden" style="height: 60vh;">
        <div class="absolute inset-0 z-0">
          <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover scale-105 transform origin-center opacity-70" alt="Tecidos" data-aos="zoom-out" data-aos-duration="2000">
          <div class="absolute inset-0 bg-black/40 z-10"></div>
        </div>
        <div class="relative z-20 text-center px-4" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="text-white text-4xl md:text-6xl font-light tracking-widest mb-4 uppercase drop-shadow-2xl">Guia de Tecidos</h1>
          <p class="text-white/90 text-lg md:text-xl font-light max-w-2xl mx-auto">Toque, durabilidade e elegância. O revestimento perfeito para o seu estofo.</p>
        </div>
      </section>

      <section class="py-24">
        <div class="container mx-auto px-4 max-w-6xl">
          
          <!-- Tipo 1 -->
          <div class="flex flex-col md:flex-row items-center gap-12 mb-20" data-aos="fade-up">
            <div class="w-full md:w-1/2 aspect-video bg-gray-200 rounded-xl overflow-hidden shadow-lg">
              <img src="https://lourini.pt/app/uploads/2024/07/dennis-32-1200x1200.webp" class="w-full h-full object-cover" alt="Tecido Veludo">
            </div>
            <div class="w-full md:w-1/2">
              <h2 class="text-3xl font-light text-black mb-4">Veludo Premium</h2>
              <p class="text-gray-500 font-light leading-relaxed mb-6">Um toque sumptuoso e uma aparência luxuosa. O nosso veludo reflete a luz de forma elegante, criando profundidade e sofisticação em qualquer peça de mobiliário. Ideal para salas de estar que procuram um ambiente mais requintado.</p>
              <ul class="space-y-2 text-sm text-gray-600">
                <li><i data-feather="check" class="w-4 h-4 inline text-black mr-2"></i> Toque ultra-suave</li>
                <li><i data-feather="check" class="w-4 h-4 inline text-black mr-2"></i> Aspeto sofisticado e brilhante</li>
                <li><i data-feather="check" class="w-4 h-4 inline text-black mr-2"></i> Excelente isolamento térmico</li>
              </ul>
            </div>
          </div>

          <!-- Tipo 2 -->
          <div class="flex flex-col md:flex-row-reverse items-center gap-12 mb-20" data-aos="fade-up">
            <div class="w-full md:w-1/2 aspect-video bg-gray-200 rounded-xl overflow-hidden shadow-lg">
              <img src="https://lourini.pt/app/uploads/2024/09/bona-sala-1200x1200.webp" class="w-full h-full object-cover" alt="Tecido AquaClean">
            </div>
            <div class="w-full md:w-1/2">
              <h2 class="text-3xl font-light text-black mb-4">Microfibra Anti-Mancha</h2>
              <p class="text-gray-500 font-light leading-relaxed mb-6">A tecnologia inovadora permite que a maioria das nódoas (tinta, café, vinho, comida) sejam limpas apenas com água. O tecido perfeito para famílias com crianças ou animais de estimação, combinando durabilidade com fácil manutenção.</p>
              <ul class="space-y-2 text-sm text-gray-600">
                <li><i data-feather="check" class="w-4 h-4 inline text-black mr-2"></i> Limpeza fácil apenas com água</li>
                <li><i data-feather="check" class="w-4 h-4 inline text-black mr-2"></i> Pet-friendly (resistente a arranhões)</li>
                <li><i data-feather="check" class="w-4 h-4 inline text-black mr-2"></i> Alta durabilidade contra fricção</li>
              </ul>
            </div>
          </div>

          <div class="text-center mt-12 p-10 bg-[#f8f5f0] rounded-xl border border-[#EAE6DF]" data-aos="fade-up">
            <h3 class="text-2xl font-light mb-4">Gostaria de ver as amostras reais?</h3>
            <p class="text-gray-500 mb-8 max-w-lg mx-auto">Temos catálogos físicos com dezenas de cores para cada tipo de tecido na nossa loja física.</p>
            <a href="https://wa.me/351212582788" target="_blank" class="inline-flex items-center justify-center bg-[#25D366] text-white px-8 py-3 rounded font-bold uppercase tracking-widest text-sm hover:bg-[#1ebd5a] transition-colors shadow-lg">
              <i data-feather="message-circle" class="w-5 h-5 mr-2"></i>
              Pedir mais informações
            </a>
          </div>

        </div>
      </section>
    </main>
"""
tecidos = re.sub(pattern, '</header>\n' + tecidos_main + '\n<section class="bg-[#f0ede6]', tecidos, flags=re.DOTALL)
with open('tecidos.html', 'w', encoding='utf-8') as f:
    f.write(tecidos)

print("Redesigns and fixes deployed successfully.")
