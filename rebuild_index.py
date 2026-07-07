import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace everything from <main> down to the end of the file, except we must keep the trailing </body></html>.
# Actually, it's safer to just replace from <main> to </main> and then replace the <footer>.

NEW_MAIN = """
    <main>
      <!-- Hero Elegante -->
      <section class="relative h-[80vh] md:h-[90vh] bg-[#ebe7e0] flex items-center justify-center overflow-hidden">
        <!-- Overlay suave -->
        <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('https://lourini.pt/app/uploads/2024/07/dennis-32-1200x1200.webp');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/10 to-transparent"></div>
        
        <div class="relative z-10 text-center px-6 mt-20" data-aos="fade-up" data-aos-duration="1000">
          <p class="text-xs tracking-[0.2em] text-white/80 uppercase mb-4">Adil Móveis — Desde 1987</p>
          <h1 class="text-3xl md:text-5xl font-light text-white tracking-wide mb-6">A arte de viver bem.</h1>
          <a href="catalogos.html" class="inline-block border border-white/60 text-white px-8 py-3 text-sm tracking-widest uppercase hover:bg-white hover:text-black transition-colors duration-500">Descobrir Coleções</a>
        </div>
      </section>

      <!-- NOVO: Packs em Destaque (O que mais vende) -->
      <section class="py-24 bg-[#faf9f6]">
        <div class="container mx-auto px-4 max-w-6xl">
          <div class="text-center mb-16" data-aos="fade-up">
            <h2 class="text-xs font-bold tracking-[0.2em] text-gray-400 uppercase mb-3">Soluções Completas</h2>
            <h3 class="text-2xl md:text-3xl font-light text-[#3a3532]">Os nossos packs mais procurados.</h3>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Pack 1 -->
            <a href="conjuntos.html" class="group block" data-aos="fade-up" data-aos-delay="100">
              <div class="overflow-hidden aspect-[4/5] mb-6">
                <img src="images/Lourini-Majestic.jpg" class="w-full h-full object-cover transform transition-transform duration-1000 group-hover:scale-105" alt="Quartos">
              </div>
              <h4 class="text-lg font-medium text-[#3a3532] tracking-wide mb-1">Coleção Quarto</h4>
              <p class="text-sm text-gray-500">Cama, mesas e colchão. Desde 720€</p>
            </a>
            <!-- Pack 2 -->
            <a href="conjuntos.html" class="group block" data-aos="fade-up" data-aos-delay="200">
              <div class="overflow-hidden aspect-[4/5] mb-6">
                <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover transform transition-transform duration-1000 group-hover:scale-105" alt="Salas">
              </div>
              <h4 class="text-lg font-medium text-[#3a3532] tracking-wide mb-1">Coleção Sala</h4>
              <p class="text-sm text-gray-500">Mesa, cadeiras e móvel. Desde 999€</p>
            </a>
            <!-- Pack 3 -->
            <a href="conjuntos.html" class="group block" data-aos="fade-up" data-aos-delay="300">
              <div class="overflow-hidden aspect-[4/5] mb-6">
                <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-full object-cover transform transition-transform duration-1000 group-hover:scale-105" alt="Descanso">
              </div>
              <h4 class="text-lg font-medium text-[#3a3532] tracking-wide mb-1">Coleção Descanso</h4>
              <p class="text-sm text-gray-500">Colchão premium e estrado. Desde 350€</p>
            </a>
          </div>
          
          <div class="text-center mt-12" data-aos="fade-in">
             <a href="conjuntos.html" class="inline-block border-b border-[#3a3532] pb-1 text-sm tracking-widest text-[#3a3532] hover:text-gray-500 transition-colors uppercase">Ver todos os packs</a>
          </div>
        </div>
      </section>

      <!-- A Nossa História (Simplificada e Suave) -->
      <section class="py-24 bg-white">
        <div class="container mx-auto px-4 max-w-5xl">
          <div class="flex flex-col md:flex-row items-center gap-16">
            <div class="md:w-5/12" data-aos="fade-right">
              <img src="images/Lourini-Majestic.jpg" alt="Loja Feijó" class="w-full aspect-square object-cover" style="filter: sepia(0.1) grayscale(0.2);">
            </div>
            <div class="md:w-7/12" data-aos="fade-left">
              <h2 class="text-xs font-bold tracking-[0.2em] text-gray-400 uppercase mb-4">Negócio de Família</h2>
              <h3 class="text-2xl font-light text-[#3a3532] leading-relaxed mb-6">Mais de três décadas a entregar conforto no coração da Margem Sul.</h3>
              <p class="text-gray-500 text-sm md:text-base leading-relaxed mb-6 font-light">
                A Adil Móveis não é uma superfície anónima. Somos uma família do Feijó dedicada a simplificar a sua vida. O nosso compromisso é a ausência de dores de cabeça: escolhe o que gosta, e nós tratamos de tudo.
              </p>
              <div class="space-y-3">
                <div class="flex items-center text-[#3a3532] text-sm">
                  <i data-feather="check" class="w-4 h-4 mr-3 text-gray-400"></i> Entrega e montagem sempre grátis.
                </div>
                <div class="flex items-center text-[#3a3532] text-sm">
                  <i data-feather="check" class="w-4 h-4 mr-3 text-gray-400"></i> Recolha de móveis antigos incluída.
                </div>
                <div class="flex items-center text-[#3a3532] text-sm">
                  <i data-feather="check" class="w-4 h-4 mr-3 text-gray-400"></i> Atendimento que o trata pelo nome.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Categorias Simples -->
      <section class="py-24 bg-[#faf9f6]">
        <div class="container mx-auto px-4 max-w-7xl">
           <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-8">
            <a href="quartos.html" class="group relative block aspect-square bg-gray-200 overflow-hidden" data-aos="fade-up" data-aos-delay="0">
              <img src="https://nadiairina.github.io/adil-moveis/images/Lourini-Majestic.jpg" class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700">
              <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors duration-700"></div>
              <span class="absolute bottom-6 left-6 text-white text-sm tracking-widest uppercase font-medium">Quartos</span>
            </a>
            <a href="salas.html" class="group relative block aspect-square bg-gray-200 overflow-hidden" data-aos="fade-up" data-aos-delay="100">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700">
              <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors duration-700"></div>
              <span class="absolute bottom-6 left-6 text-white text-sm tracking-widest uppercase font-medium">Salas</span>
            </a>
            <a href="colchoes.html" class="group relative block aspect-square bg-gray-200 overflow-hidden" data-aos="fade-up" data-aos-delay="200">
              <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700">
              <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors duration-700"></div>
              <span class="absolute bottom-6 left-6 text-white text-sm tracking-widest uppercase font-medium">Descanso</span>
            </a>
            <a href="complementos.html" class="group relative block aspect-square bg-gray-200 overflow-hidden" data-aos="fade-up" data-aos-delay="300">
              <img src="https://lourini.pt/app/uploads/2024/07/camiseiro-1200x1200.png" class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700">
              <div class="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors duration-700"></div>
              <span class="absolute bottom-6 left-6 text-white text-sm tracking-widest uppercase font-medium">Complementos</span>
            </a>
           </div>
        </div>
      </section>

      <!-- Newsletter Fina -->
      <section class="py-24 bg-white border-t border-[#f0ede6]">
        <div class="container mx-auto px-4 max-w-2xl text-center" data-aos="zoom-in">
          <i data-feather="mail" class="w-6 h-6 mx-auto text-gray-300 mb-6"></i>
          <h2 class="text-xl font-light text-[#3a3532] mb-3">Junte-se a nós.</h2>
          <p class="text-sm text-gray-500 mb-8 font-light">Subscreva para receber 10% de desconto na sua primeira encomenda.</p>
          <div class="ml-embedded w-full" data-form="oCm4cl"></div>
        </div>
      </section>

    </main>
"""

NEW_FOOTER = """
    <footer class="bg-[#2c2a29] text-[#d1ccc5] py-16" data-aos="fade-in">
      <div class="container mx-auto px-4 max-w-7xl">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12 text-sm font-light">
          <!-- Col 1 -->
          <div>
            <h4 class="text-white tracking-widest uppercase mb-6 text-xs font-medium">Lojas</h4>
            <p class="mb-2">Rua do Feijó, 123</p>
            <p class="mb-2">2810-000 Almada</p>
            <p class="mt-6 text-white">212 582 788</p>
            <p>adil.moveis@hotmail.com</p>
          </div>
          <!-- Col 2 -->
          <div>
            <h4 class="text-white tracking-widest uppercase mb-6 text-xs font-medium">Apoio</h4>
            <ul class="space-y-3">
              <li><a href="servicos.html" class="hover:text-white transition-colors">Serviços e Entregas</a></li>
              <li><a href="contactos.html" class="hover:text-white transition-colors">Agendar Visita</a></li>
              <li><a href="testemunhos.html" class="hover:text-white transition-colors">Testemunhos</a></li>
            </ul>
          </div>
          <!-- Col 3 -->
          <div>
            <h4 class="text-white tracking-widest uppercase mb-6 text-xs font-medium">Siga-nos</h4>
            <div class="flex space-x-6">
              <a href="#" class="hover:text-white transition-colors"><i data-feather="facebook" class="w-5 h-5"></i></a>
              <a href="#" class="hover:text-white transition-colors"><i data-feather="instagram" class="w-5 h-5"></i></a>
            </div>
            <p class="mt-8 text-xs text-gray-500">&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>
          </div>
        </div>
      </div>
    </footer>
"""

# Extract the header and head parts safely
main_start = content.find('<main>')
if main_start == -1:
    main_start = content.find('<main class')

footer_start = content.find('<footer')
end_body = content.find('</body>')

if main_start != -1 and footer_start != -1 and end_body != -1:
    header_part = content[:main_start]
    scripts_part = content[end_body:]
    
    new_content = header_part + NEW_MAIN + NEW_FOOTER + scripts_part
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Redesigned main and footer of index.html")
else:
    print("Could not find delimiters.")
