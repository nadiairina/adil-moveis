import os

html_content = """<!DOCTYPE html>
<html lang="pt">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Adil Móveis - Detalhe do Produto</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="styles.css" />
    <link rel="preconnect" href="https://app.snipcart.com" />
    <link rel="preconnect" href="https://cdn.snipcart.com" />
    <link rel="stylesheet" href="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.css" />
    <script src="https://unpkg.com/feather-icons"></script>
    <!-- Load Products Database -->
    <script src="products.js"></script>
    <!-- MailerLite Universal -->
    <script>
        (function(w,d,e,u,f,l,n){w[f]=w[f]||function(){(w[f].q=w[f].q||[])
        .push(arguments);},l=d.createElement(e),l.async=1,l.src=u,
        n=d.getElementsByTagName(e)[0],n.parentNode.insertBefore(l,n);})
        (window,document,'script','https://assets.mailerlite.com/js/universal.js','ml');
        ml('account', '2412294');
    </script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="icon" type="image/png" href="images/logo.png">
    <link rel="icon" type="image/x-icon" href="favicon.ico">
  </head>
  <body class="bg-[#FDFBF7] text-[#2c2a29] font-sans antialiased">
    <!-- Global Promo Banner -->
    <div class="bg-[#f8f5f0] text-gray-800 text-center py-3 text-sm font-semibold tracking-wide z-50 relative border-b border-gray-200">
      🚚 Entrega, Montagem e Recolha Grátis num Raio de 50km (Lisboa e Setúbal)
    </div>
    
    <!-- STICKY NAVBAR -->
    <header class="sticky top-0 z-50 bg-white/90 backdrop-blur-md transition-all duration-300 shadow-sm border-b border-[#EAE6DF]">
      <div class="container mx-auto px-4 lg:px-8">
        <div class="flex items-center justify-between h-20 relative">
          <!-- Logo -->
          <a href="index.html" class="flex-shrink-0">
            <img src="images/logo.png" alt="Adil Móveis" class="h-12 md:h-14 w-12 md:w-14 object-contain bg-white rounded-full border-2 border-[#C8B598] shadow-sm p-0.5">
          </a>
          <!-- Desktop Menu -->
          <nav class="hidden lg:flex items-center space-x-8 absolute left-1/2 transform -translate-x-1/2 z-10">
            <a href="index.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Início</a>
            <a href="quartos.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Quartos</a>
            <a href="salas.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Salas</a>
            <a href="cozinha.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Cozinhas</a>
            <a href="colchoes.html" class="text-sm font-medium tracking-widest text-gray-800 hover:text-black uppercase transition-colors">Colchões</a>
            <a href="conjuntos.html" class="text-sm font-bold tracking-widest text-[#C8B598] uppercase transition-all duration-300 border border-[#C8B598] px-3 py-1 rounded hover:bg-[#C8B598] hover:text-white animate-pulse">Packs</a>
          </nav>
          <!-- Right Side -->
          <div class="flex items-center space-x-6">
            <div class="hidden lg:flex items-center mr-2">
              <a href="contactos.html" class="flex items-center text-[10px] font-bold uppercase tracking-widest border border-gray-300 px-4 py-1.5 rounded-full hover:border-black hover:bg-black hover:text-white transition-all shadow-sm">Agendar Visita</a>
            </div>
            <button class="snipcart-checkout flex items-center space-x-2 text-black hover:text-gray-600 transition-colors group">
              <div class="relative">
                <i data-feather="shopping-bag" class="w-6 h-6"></i>
                <span class="snipcart-items-count absolute -top-1 -right-2 bg-black text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold">0</span>
              </div>
            </button>
            <button class="text-black hover:text-gray-600 transition-colors" id="hamburgerBtn">
              <i data-feather="menu" class="w-8 h-8"></i>
            </button>
          </div>
        </div>
      </div>
      
      <!-- SLIDE-IN RIGHT SIDEBAR MENU -->
      <div id="menuOverlay" class="fixed inset-0 bg-black/50 z-[999] hidden transition-opacity duration-300 opacity-0">
        <div id="menuSidebar" class="absolute top-0 right-0 w-80 max-w-[85vw] h-full bg-[#FDFBF7] shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col">
            <div class="px-6 py-6 border-b border-[#EAE6DF] flex justify-between items-center bg-white">
                <span class="text-xs font-bold tracking-widest uppercase text-gray-500">Menu</span>
                <button id="closeMenuBtn" class="text-black hover:text-red-500 transition-colors"><i data-feather="x" class="w-6 h-6"></i></button>
            </div>
            <div class="flex-1 overflow-y-auto px-6 py-8">
                <nav class="flex flex-col space-y-4 mb-8">
                    <a href="quartos.html" class="text-lg font-medium text-gray-800 hover:text-black">Quartos</a>
                    <a href="salas.html" class="text-lg font-medium text-gray-800 hover:text-black">Salas</a>
                    <a href="cozinha.html" class="text-lg font-medium text-gray-800 hover:text-black">Cozinhas</a>
                    <a href="colchoes.html" class="text-lg font-medium text-gray-800 hover:text-black">Colchões</a>
                    <a href="kids.html" class="text-lg font-medium text-gray-800 hover:text-black">Crianças / Kids</a>
                    <a href="escritorio.html" class="text-lg font-medium text-gray-800 hover:text-black">Escritórios</a>
                    <a href="complementos.html" class="text-lg font-medium text-gray-800 hover:text-black">Complementos</a>
                    <a href="conjuntos.html" class="text-lg font-bold text-[#C8B598]">Comprar Packs</a>
                </nav>
            </div>
        </div>
      </div>
    </header>

    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const hamburgerBtn = document.getElementById('hamburgerBtn');
        const closeMenuBtn = document.getElementById('closeMenuBtn');
        const menuOverlay = document.getElementById('menuOverlay');
        const menuSidebar = document.getElementById('menuSidebar');
        function openMenu() {
            menuOverlay.classList.remove('hidden');
            setTimeout(() => { menuOverlay.classList.remove('opacity-0'); menuOverlay.classList.add('opacity-100'); menuSidebar.classList.remove('translate-x-full'); }, 10);
            document.body.style.overflow = 'hidden';
        }
        function closeMenu() {
            menuSidebar.classList.add('translate-x-full');
            menuOverlay.classList.remove('opacity-100'); menuOverlay.classList.add('opacity-0');
            setTimeout(() => { menuOverlay.classList.add('hidden'); }, 300);
            document.body.style.overflow = '';
        }
        if(hamburgerBtn) hamburgerBtn.addEventListener('click', openMenu);
        if(closeMenuBtn) closeMenuBtn.addEventListener('click', closeMenu);
        if(menuOverlay) menuOverlay.addEventListener('click', (e) => { if(e.target === menuOverlay) closeMenu(); });
      });
    </script>

    <main class="bg-[#FDFBF7] py-12 md:py-24">
      <div class="container mx-auto px-4 max-w-7xl">
        <!-- Breadcrumbs -->
        <nav class="flex text-sm text-gray-500 mb-8" aria-label="Breadcrumb">
          <ol class="inline-flex items-center space-x-1 md:space-x-3">
            <li class="inline-flex items-center"><a href="index.html" class="hover:text-black">Início</a></li>
            <li aria-current="page">
              <div class="flex items-center">
                <i data-feather="chevron-right" class="w-4 h-4 mx-1"></i>
                <span class="text-black font-medium" id="breadcrumb-name">Carregando Produto...</span>
              </div>
            </li>
          </ol>
        </nav>

        <!-- Product Layout -->
        <div class="flex flex-col lg:flex-row gap-12 lg:gap-20" id="product-container" style="display: none;">
          
          <!-- Left: Image -->
          <div class="w-full lg:w-[60%] flex flex-col gap-4">
            <div class="w-full aspect-[4/3] md:aspect-video bg-[#f0ede6] rounded-xl overflow-hidden group border border-gray-200">
               <img src="images/logo.png" id="mainImage" class="w-full h-full object-contain md:object-cover transition-transform duration-700 group-hover:scale-105" alt="Produto">
            </div>
          </div>

          <!-- Right: Product Info -->
          <div class="w-full lg:w-[40%]">
             <div class="sticky top-32">
                <h1 class="text-3xl md:text-4xl font-light text-black mb-2 tracking-tight" id="dynamic-title">Nome do Produto</h1>
                <p class="text-gray-500 text-sm mb-6 uppercase tracking-widest">Adil Móveis Premium</p>
                <div class="text-2xl md:text-3xl font-medium text-black mb-8" id="productPrice">0,00 €</div>

                <!-- Descrição -->
                <div class="mb-8" id="dynamic-desc-container">
                  <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest mb-3">Descrição</h3>
                  <p class="text-gray-600 text-sm font-light leading-relaxed" id="dynamic-desc"></p>
                </div>

                <!-- Custom 1 -->
                <div class="mb-8" id="custom1-container" style="display: none;">
                  <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest mb-3" id="custom1-title">Opção 1</h3>
                  <div class="flex flex-wrap gap-3" id="custom1-options"></div>
                </div>

                <!-- Custom 2 -->
                <div class="mb-8" id="custom2-container" style="display: none;">
                  <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest mb-3 flex justify-between">
                    <span id="custom2-title">Opção 2</span>
                    <a href="tecidos.html" class="text-gray-400 hover:text-black underline font-medium text-[10px]">Ver Catálogo</a>
                  </h3>
                  <div class="flex flex-wrap gap-3" id="custom2-options"></div>
                </div>

                <!-- Add to Cart -->
                <button id="addToCartBtn" class="w-full bg-black text-white py-4 rounded font-bold uppercase tracking-widest hover:bg-gray-800 transition-colors mb-6 shadow-lg flex items-center justify-center space-x-2 snipcart-add-item">
                  <i data-feather="shopping-bag" class="w-5 h-5"></i>
                  <span>Adicionar ao Carrinho</span>
                </button>

                <!-- Helpers -->
                <div class="grid grid-cols-2 gap-3 mb-6">
                  <a href="contactos.html" class="w-full flex items-center justify-center space-x-2 py-3 border border-black text-black hover:bg-black hover:text-white transition-colors rounded text-[11px] font-bold uppercase tracking-wider">
                    <i data-feather="map-pin" class="w-4 h-4"></i>
                    <span>Ver na Loja</span>
                  </a>
                  <a href="https://wa.me/351960209396" target="_blank" class="w-full flex items-center justify-center space-x-2 py-3 border border-gray-300 text-gray-700 hover:bg-[#25D366] hover:text-white hover:border-[#25D366] transition-colors rounded text-[11px] font-bold uppercase tracking-wider group">
                    <i data-feather="message-circle" class="w-4 h-4 text-[#25D366] group-hover:text-white"></i>
                    <span>Dúvidas?</span>
                  </a>
                </div>
                
                <div class="mt-8 border-t border-gray-200 py-6 text-xs text-gray-400 font-light text-center">
                    Garantia de 3 anos incluída. Transporte e montagem gratuita na zona da Grande Lisboa e Setúbal num raio de 50km.
                </div>
             </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="bg-[#2c2a29] text-[#d1ccc5] py-16">
      <div class="container mx-auto px-4 max-w-7xl text-center">
         <p class="text-xs text-gray-500">&copy; 2026 Adil Móveis. Todos os direitos reservados.</p>
      </div>
    </footer>

    <script>
      document.addEventListener('DOMContentLoaded', () => {
        if (typeof feather !== 'undefined') feather.replace();
        
        const params = new URLSearchParams(window.location.search);
        const productId = params.get('id');
        
        if (!productId || !window.produtos || !window.produtos[productId]) {
            // Se não encontrar o produto, volta à página inicial ou avisa
            document.getElementById('breadcrumb-name').textContent = "Produto não encontrado";
            return;
        }
        
        // Show container
        document.getElementById('product-container').style.display = 'flex';
        
        const p = window.produtos[productId];
        
        document.title = p.name + " - Adil Móveis";
        document.getElementById('dynamic-title').textContent = p.name;
        document.getElementById('productPrice').textContent = p.price > 0 ? p.price.toFixed(2).replace('.', ',') + " €" : "Preço sob consulta";
        
        // Disable snipcart if price is 0
        const btn = document.getElementById('addToCartBtn');
        if (p.price === 0) {
            btn.innerHTML = '<i data-feather="phone" class="w-5 h-5 mr-2"></i><span>Pedir Orçamento</span>';
            btn.classList.remove('snipcart-add-item');
            btn.classList.add('bg-[#C8B598]');
            btn.onclick = () => { window.location.href = "https://wa.me/351960209396?text=Olá, gostaria de saber o preço do produto: " + p.name; };
        } else {
            btn.dataset.itemId = p.id;
            btn.dataset.itemName = p.name;
            btn.dataset.itemPrice = p.price;
            btn.dataset.itemImage = p.image;
            btn.dataset.itemUrl = "produto-detalhe.html?id=" + p.id; // Important for Snipcart validation
            if (p.description) btn.dataset.itemDescription = p.description;
        }
        
        document.getElementById('mainImage').src = p.image;
        document.getElementById('breadcrumb-name').textContent = p.name;
        
        // Description
        if (p.description) {
            document.getElementById('dynamic-desc').innerHTML = p.description;
        } else {
            document.getElementById('dynamic-desc-container').style.display = 'none';
        }
        
        // Custom Options Helpers
        function buildOptions(containerId, titleId, optionsId, customName, customOptionsRaw, customIndex) {
            const container = document.getElementById(containerId);
            if (!customName || !customOptionsRaw) {
                container.style.display = 'none';
                return;
            }
            
            container.style.display = 'block';
            document.getElementById(titleId).textContent = customName;
            
            if (p.price > 0) {
                btn.dataset[`itemCustom${customIndex}Name`] = customName;
                btn.dataset[`itemCustom${customIndex}Options`] = customOptionsRaw;
            }
            
            const opts = customOptionsRaw.split('|');
            if (p.price > 0) btn.dataset[`itemCustom${customIndex}Value`] = opts[0].split('[')[0];
            
            const flexDiv = document.getElementById(optionsId);
            opts.forEach((opt, idx) => {
                let val = opt.split('[')[0]; // Remove Snipcart price modifier visually
                let button = document.createElement('button');
                
                const activeClass = "border-black bg-black text-white";
                const inactiveClass = "border-gray-300 text-gray-600 hover:border-black";
                const baseClass = "border py-2 px-4 rounded text-xs font-bold uppercase tracking-wider transition-colors size-btn";
                
                button.className = baseClass + " " + (idx === 0 ? activeClass : inactiveClass);
                button.textContent = val;
                
                button.onclick = () => {
                    Array.from(flexDiv.children).forEach(b => {
                        b.className = baseClass + " " + inactiveClass;
                    });
                    button.className = baseClass + " " + activeClass;
                    if (p.price > 0) btn.dataset[`itemCustom${customIndex}Value`] = val;
                };
                flexDiv.appendChild(button);
            });
        }
        
        buildOptions('custom1-container', 'custom1-title', 'custom1-options', p.custom1_name, p.custom1_options, 1);
        buildOptions('custom2-container', 'custom2-title', 'custom2-options', p.custom2_name, p.custom2_options, 2);
        
        if (typeof feather !== 'undefined') feather.replace();
      });
    </script>
    <script async src="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js"></script>
    <div id="snipcart" data-api-key="ODE4MjNlYWYtZGViOS00OGY3LWJhZWEtODU1OTE5OTYzMzQxNjM5MTYyMDI2OTM2NjA0MTY3" hidden></div>
  </body>
</html>"""

with open("produto-detalhe.html", "w") as f:
    f.write(html_content)

print("produto-detalhe.html rebuild complete!")
