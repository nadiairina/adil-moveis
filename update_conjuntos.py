with open('conjuntos.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

content_to_insert = """    <!-- Hero Section with Logo and Menu Button -->
    <section class="relative bg-gray-200">
      <!-- Logo and Menu positioning container -->
      <div class="absolute top-0 left-0 w-full z-10 flex justify-between items-center p-4">
        <a href="index.html">
          <img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-12 w-auto bg-white rounded">
        </a>
        <button class="flex items-center space-x-2 text-white bg-black bg-opacity-50 py-2 px-3 rounded" id="menuButton">
          <span class="uppercase font-bold">MENU</span>
          <i data-feather="menu" class="w-6 h-6"></i>
        </button>
      </div>
      
      <section class="relative h-80 md:h-96 bg-gray-200">
        <div class="absolute inset-0 bg-cover" style="background-image: url('images/Lourini-Majestic.jpg'); background-position: center 30%;"></div>
        <div class="absolute inset-0 bg-black bg-opacity-50"></div>
        <div class="relative container mx-auto px-4 h-full flex flex-col justify-center items-center text-center text-white">
          <h1 class="text-4xl md:text-5xl font-light mb-4 text-shadow" style="font-family: 'Playfair Display', serif; font-style: italic;">Conjuntos & Packs</h1>
          <p class="text-xl max-w-2xl text-shadow">
            Compre os nossos conjuntos pré-selecionados e poupe. Tudo desenhado para combinar na perfeição, com entrega e montagem gratuita!
          </p>
        </div>
      </section>
    </section>

    <main class="bg-gray-50 py-16">
      <div class="container mx-auto px-4 max-w-6xl">
        <div class="space-y-16">
          
          <!-- PACK 1: Quarto Completo -->
          <div class="bg-white rounded-xl shadow-xl overflow-hidden flex flex-col md:flex-row border border-gray-100 transform transition-all hover:shadow-2xl">
            <div class="md:w-1/2 relative">
              <img src="https://nadiairina.github.io/adil-moveis/images/Lourini-Majestic.jpg" alt="Pack Quarto" class="w-full h-full object-cover min-h-[300px]">
              <div class="absolute top-4 left-4 bg-red-600 text-white px-4 py-1 font-bold rounded shadow uppercase text-sm">-15% DESCONTO</div>
            </div>
            <div class="md:w-1/2 p-8 md:p-12 flex flex-col justify-center">
              <h2 class="text-3xl font-bold mb-2" style="font-family: 'Playfair Display', serif;">Pack "Quarto de Sonho"</h2>
              <p class="text-gray-500 mb-6 uppercase text-sm tracking-wider font-semibold">Cama + Mesas Cabeceira + Colchão</p>
              
              <ul class="space-y-3 mb-8 text-gray-700">
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> Cama de Casal Estofada (várias cores)</li>
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> 2 Mesinhas de Cabeceira com 2 Gavetas</li>
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> Colchão Ortopédico (195x140cm)</li>
                <li class="flex items-center"><i data-feather="check" class="mr-3 w-5 h-5" style="color: #b3923b;"></i> Entrega e Montagem Grátis</li>
              </ul>
              
              <div class="flex items-end mb-6">
                <span class="text-gray-400 line-through text-xl mr-3">850.00€</span>
                <span class="text-4xl font-bold text-black">720.00€</span>
              </div>
              
              <button class="snipcart-add-item bg-black text-white py-3 px-6 rounded font-bold uppercase tracking-wide hover:bg-gray-800 transition-colors flex items-center justify-center w-full md:w-auto"
                data-item-id="pack-quarto-01"
                data-item-price="720.00"
                data-item-url="/conjuntos.html"
                data-item-name="Pack Quarto de Sonho"
                data-item-image="https://nadiairina.github.io/adil-moveis/images/Lourini-Majestic.jpg">
                <i data-feather="shopping-cart" class="mr-2 w-5 h-5"></i> Adicionar Pack
              </button>
            </div>
          </div>

          <!-- PACK 2: Colchão Saudável -->
          <div class="bg-white rounded-xl shadow-xl overflow-hidden flex flex-col md:flex-row-reverse border border-gray-100 transform transition-all hover:shadow-2xl">
            <div class="md:w-1/2 relative">
              <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" alt="Pack Colchão" class="w-full h-full object-cover min-h-[300px]">
              <div class="absolute top-4 right-4 bg-red-600 text-white px-4 py-1 font-bold rounded shadow uppercase text-sm">-10% DESCONTO</div>
            </div>
            <div class="md:w-1/2 p-8 md:p-12 flex flex-col justify-center">
              <h2 class="text-3xl font-bold mb-2" style="font-family: 'Playfair Display', serif;">Pack "Dormir Bem"</h2>
              <p class="text-gray-500 mb-6 uppercase text-sm tracking-wider font-semibold">Colchão Premium + Estrado + Almofadas</p>
              
              <ul class="space-y-3 mb-8 text-gray-700">
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> Colchão Viscoelástico de Alta Densidade</li>
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> Estrado Metálico Reforçado</li>
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> 2 Almofadas Cervicais Incluídas</li>
                <li class="flex items-center"><i data-feather="check" class="mr-3 w-5 h-5" style="color: #b3923b;"></i> Recolha Grátis do seu Colchão Velho</li>
              </ul>
              
              <div class="flex items-end mb-6">
                <span class="text-gray-400 line-through text-xl mr-3">390.00€</span>
                <span class="text-4xl font-bold text-black">350.00€</span>
              </div>
              
              <button class="snipcart-add-item bg-black text-white py-3 px-6 rounded font-bold uppercase tracking-wide hover:bg-gray-800 transition-colors flex items-center justify-center w-full md:w-auto"
                data-item-id="pack-colchao-01"
                data-item-price="350.00"
                data-item-url="/conjuntos.html"
                data-item-name="Pack Dormir Bem"
                data-item-image="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp">
                <i data-feather="shopping-cart" class="mr-2 w-5 h-5"></i> Adicionar Pack
              </button>
            </div>
          </div>

          <!-- PACK 3: Sala Completa -->
          <div class="bg-white rounded-xl shadow-xl overflow-hidden flex flex-col md:flex-row border border-gray-100 transform transition-all hover:shadow-2xl">
            <div class="md:w-1/2 relative">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" alt="Pack Sala" class="w-full h-full object-cover min-h-[300px]">
              <div class="absolute top-4 left-4 bg-red-600 text-white px-4 py-1 font-bold rounded shadow uppercase text-sm">-20% DESCONTO</div>
            </div>
            <div class="md:w-1/2 p-8 md:p-12 flex flex-col justify-center">
              <h2 class="text-3xl font-bold mb-2" style="font-family: 'Playfair Display', serif;">Pack "Sala de Jantar"</h2>
              <p class="text-gray-500 mb-6 uppercase text-sm tracking-wider font-semibold">Mesa + 4 Cadeiras + Aparador</p>
              
              <ul class="space-y-3 mb-8 text-gray-700">
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> Mesa Extensível (Carvalho ou Nogueira)</li>
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> 4 Cadeiras Estofadas com Tecido Lavável</li>
                <li class="flex items-center"><i data-feather="check" class="text-green-500 mr-3 w-5 h-5"></i> Aparador de 3 Portas com Gavetas Ocultas</li>
                <li class="flex items-center"><i data-feather="check" class="mr-3 w-5 h-5" style="color: #b3923b;"></i> Entrega e Montagem Grátis</li>
              </ul>
              
              <div class="flex items-end mb-6">
                <span class="text-gray-400 line-through text-xl mr-3">1250.00€</span>
                <span class="text-4xl font-bold text-black">999.00€</span>
              </div>
              
              <button class="snipcart-add-item bg-black text-white py-3 px-6 rounded font-bold uppercase tracking-wide hover:bg-gray-800 transition-colors flex items-center justify-center w-full md:w-auto"
                data-item-id="pack-sala-01"
                data-item-price="999.00"
                data-item-url="/conjuntos.html"
                data-item-name="Pack Sala de Jantar"
                data-item-image="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp">
                <i data-feather="shopping-cart" class="mr-2 w-5 h-5"></i> Adicionar Pack
              </button>
            </div>
          </div>

        </div>
      </div>
    </main>
"""

new_lines = lines[:125] + [content_to_insert + "\n"] + lines[1327:]

with open('conjuntos.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
