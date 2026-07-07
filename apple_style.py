import os

NEW_MAIN = """
    <main class="bg-[#f5f5f7]">
      <!-- HERO (Apple Style - Edge to edge, clean text) -->
      <section class="relative h-screen bg-black flex flex-col items-center justify-center overflow-hidden">
        <div class="absolute inset-0 z-0">
          <img src="https://lourini.pt/app/uploads/2024/07/dennis-32-1200x1200.webp" class="w-full h-full object-cover opacity-60 scale-105 transform origin-center" alt="Hero" data-aos="zoom-out" data-aos-duration="2000">
        </div>
        <div class="relative z-10 text-center px-4 mt-20" data-aos="fade-up" data-aos-duration="1000">
          <h2 class="text-white text-5xl md:text-7xl font-semibold tracking-tight mb-4">Adil Móveis.</h2>
          <h3 class="text-white/80 text-2xl md:text-3xl font-light mb-8">A excelência mora aqui.</h3>
          <p class="text-white/60 text-lg md:text-xl font-light max-w-2xl mx-auto mb-10">Conforto absoluto, design intemporal. Entregue e montado em sua casa, sem complicações.</p>
          <div class="flex flex-col sm:flex-row justify-center gap-4">
            <a href="catalogos.html" class="bg-white text-black px-8 py-3 rounded-full text-sm font-medium hover:bg-gray-200 transition-colors">Ver Coleções</a>
            <a href="conjuntos.html" class="bg-transparent border border-white text-white px-8 py-3 rounded-full text-sm font-medium hover:bg-white/10 transition-colors">Descobrir Packs</a>
          </div>
        </div>
      </section>

      <!-- FEATURE 1 (Massive Product Showcase) -->
      <section class="py-24 bg-white text-center overflow-hidden">
        <div class="container mx-auto px-4 max-w-4xl" data-aos="fade-up">
          <h2 class="text-4xl md:text-6xl font-semibold text-black tracking-tight mb-6">O seu novo quarto.</h2>
          <p class="text-xl md:text-2xl text-gray-500 font-light mb-12">Um refúgio de tranquilidade desenhado ao milímetro.</p>
        </div>
        <div class="w-full max-w-6xl mx-auto px-4" data-aos="fade-up" data-aos-delay="200">
          <img src="images/Lourini-Majestic.jpg" class="w-full h-auto rounded-3xl shadow-2xl object-cover aspect-video" alt="Quarto Showcase">
        </div>
      </section>

      <!-- FEATURE GRID (Split layout like Apple) -->
      <section class="px-4 pb-24 bg-white">
        <div class="container mx-auto max-w-7xl">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <!-- Left Block (Dark) -->
            <div class="bg-black rounded-3xl overflow-hidden relative group aspect-square flex flex-col items-center justify-start pt-16 text-center" data-aos="fade-right">
              <div class="absolute inset-0 z-0">
                <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover opacity-40 group-hover:opacity-50 transition-opacity duration-700 mt-32 scale-110">
              </div>
              <div class="relative z-10 px-8">
                <h3 class="text-white text-3xl md:text-4xl font-semibold mb-3 tracking-tight">Coleção Sala.</h3>
                <p class="text-white/70 text-lg md:text-xl font-light mb-6">Receba a família com elegância.</p>
                <a href="salas.html" class="text-blue-400 hover:text-blue-300 font-medium text-lg flex items-center justify-center gap-1">Comprar <i data-feather="chevron-right" class="w-5 h-5"></i></a>
              </div>
            </div>

            <!-- Right Block (Light) -->
            <div class="bg-[#f5f5f7] rounded-3xl overflow-hidden relative group aspect-square flex flex-col items-center justify-start pt-16 text-center" data-aos="fade-left">
              <div class="absolute inset-0 z-0 flex items-end">
                <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-[70%] object-cover object-top opacity-90 group-hover:scale-105 transition-transform duration-700">
              </div>
              <div class="relative z-10 px-8">
                <h3 class="text-black text-3xl md:text-4xl font-semibold mb-3 tracking-tight">Sono Profundo.</h3>
                <p class="text-gray-500 text-lg md:text-xl font-light mb-6">Colchões ortopédicos de alta densidade.</p>
                <a href="colchoes.html" class="text-blue-600 hover:text-blue-700 font-medium text-lg flex items-center justify-center gap-1">Saber mais <i data-feather="chevron-right" class="w-5 h-5"></i></a>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- NOVO GRID (Mais Imagens) -->
      <section class="px-4 pb-24 bg-white">
        <div class="container mx-auto max-w-7xl">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <div class="bg-gray-100 rounded-3xl overflow-hidden relative group aspect-video flex items-center justify-center" data-aos="fade-up">
              <img src="https://lourini.pt/app/uploads/2024/07/camiseiro-1200x1200.png" class="w-full h-full object-cover opacity-80 mix-blend-multiply group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex flex-col justify-end p-10">
                 <h3 class="text-white text-3xl font-semibold mb-2">Complementos.</h3>
                 <a href="complementos.html" class="text-white/80 hover:text-white font-medium flex items-center gap-1">Ver coleção <i data-feather="arrow-right" class="w-4 h-4"></i></a>
              </div>
            </div>

            <div class="bg-gray-100 rounded-3xl overflow-hidden relative group aspect-video flex items-center justify-center" data-aos="fade-up" data-aos-delay="100">
              <img src="https://lourini.pt/app/uploads/2024/10/modulo2P3P-lado-1200x1200.png" class="w-full h-full object-cover opacity-80 mix-blend-multiply group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex flex-col justify-end p-10">
                 <h3 class="text-white text-3xl font-semibold mb-2">Arrumação.</h3>
                 <a href="quartos.html" class="text-white/80 hover:text-white font-medium flex items-center gap-1">Roupeiros <i data-feather="arrow-right" class="w-4 h-4"></i></a>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- SERVIÇO APPLE STYLE -->
      <section class="py-32 bg-[#1d1d1f] text-white text-center">
        <div class="container mx-auto px-4 max-w-4xl" data-aos="zoom-in">
          <h2 class="text-4xl md:text-5xl font-semibold mb-8 tracking-tight">Tudo incluído.<br>Como deve ser.</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mt-20">
            <div>
              <i data-feather="truck" class="w-12 h-12 mx-auto mb-6 text-gray-400"></i>
              <h3 class="text-xl font-medium mb-3">Entrega Grátis</h3>
              <p class="text-gray-400 font-light">Levamos a sua encomenda até si sem taxas surpresa.</p>
            </div>
            <div>
              <i data-feather="tool" class="w-12 h-12 mx-auto mb-6 text-gray-400"></i>
              <h3 class="text-xl font-medium mb-3">Montagem Grátis</h3>
              <p class="text-gray-400 font-light">Equipa técnica especializada monta tudo no local.</p>
            </div>
            <div>
              <i data-feather="refresh-cw" class="w-12 h-12 mx-auto mb-6 text-gray-400"></i>
              <h3 class="text-xl font-medium mb-3">Recolha de Usados</h3>
              <p class="text-gray-400 font-light">Levamos os seus móveis velhos para reciclar.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- NEWSLETTER APPLE STYLE -->
      <section class="py-24 bg-white">
        <div class="container mx-auto px-4 max-w-2xl text-center" data-aos="fade-up">
          <h2 class="text-4xl font-semibold text-black tracking-tight mb-4">Mantenha-se inspirado.</h2>
          <p class="text-xl text-gray-500 font-light mb-10">Registe-se e receba 10% de desconto na primeira compra.</p>
          <div class="bg-[#f5f5f7] p-8 md:p-12 rounded-3xl">
            <div class="ml-embedded w-full" data-form="oCm4cl"></div>
          </div>
        </div>
      </section>
    </main>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_start = content.find('<main>')
if main_start == -1:
    main_start = content.find('<main class')

footer_start = content.find('<footer')

if main_start != -1 and footer_start != -1:
    header_part = content[:main_start]
    footer_part = content[footer_start:]
    
    new_content = header_part + NEW_MAIN + footer_part
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Apple style applied.")
else:
    print("Error applying style.")
