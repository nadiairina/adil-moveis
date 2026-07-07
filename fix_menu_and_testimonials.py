import glob
import os
import re

# 1. REMOVE TESTIMONIALS FROM INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

test_start = index_content.find('<!-- TESTEMUNHOS REAIS -->')
test_end = index_content.find('<!-- NEWSLETTER APPLE STYLE -->')

if test_start != -1 and test_end != -1:
    index_content = index_content[:test_start] + index_content[test_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)


# 2. UPDATE TESTEMUNHOS.HTML WITH REAL QUOTES
TESTEMUNHOS_HTML = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testemunhos | Adil Móveis</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/feather-icons"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-[#FDFBF7] text-[#2c2a29] font-sans antialiased">

    <!-- MASTER HEADER WILL BE INJECTED HERE -->
    <header class="sticky top-0 z-50 bg-[#FDFBF7] shadow-sm border-b border-[#EAE6DF]">
      <!-- Placeholder, will be overwritten by consistency script below -->
    </header>

    <main class="py-24">
      <div class="container mx-auto px-4 max-w-7xl">
        <div class="text-center mb-16" data-aos="fade-up">
          <h1 class="text-4xl md:text-5xl font-semibold mb-6 tracking-tight text-[#2c2a29]">Testemunhos Reais.</h1>
          <p class="text-xl text-gray-500 max-w-2xl mx-auto font-light">A opinião de quem já confia no serviço e na qualidade da Adil Móveis.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Review 1 -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="0">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Excelente atendimento, muita simpatia e profissionalismo. Fui à loja do Feijó e ajudaram-me a escolher a mobília inteira para a sala. A qualidade preço é fantástica."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">M</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Maria Silva</h4>
                <p class="text-xs text-gray-500">Cliente Loja Almada</p>
              </div>
            </div>
          </div>

          <!-- Review 2 -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="100">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Recomendo vivamente. Precisávamos de um sofá à medida e eles trataram de tudo. A equipa de entregas foi super cuidadosa a montar o sofá lá em casa."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">J</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">João Martins</h4>
                <p class="text-xs text-gray-500">Cliente Online</p>
              </div>
            </div>
          </div>

          <!-- Review 3 -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="200">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"A melhor loja de móveis da margem sul. O colchão ortopédico que comprei mudou a minha vida. Produtos modernos a preços justos, sem complicações."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">A</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Ana Costa</h4>
                <p class="text-xs text-gray-500">Cliente Loja Feijó</p>
              </div>
            </div>
          </div>
          
          <!-- Review 4 -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="300">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Comprei o quarto do meu filho aqui. O processo foi simples e eles explicaram todas as opções de tecidos e madeiras disponíveis. Muito satisfeito."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">P</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Pedro Gomes</h4>
                <p class="text-xs text-gray-500">Cliente Loja Almada</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- MASTER FOOTER WILL BE INJECTED HERE -->
    <footer></footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
      AOS.init({ once: true });
      feather.replace();
    </script>
</body>
</html>
"""

with open('testemunhos.html', 'w', encoding='utf-8') as f:
    f.write(TESTEMUNHOS_HTML)


# 3. RE-INTRODUCE GLOBAL HAMBURGER MENU / DRAWER TO NAVBAR
NEW_NAVBAR = """    <!-- STICKY NAVBAR -->
    <header class="sticky top-0 z-50 bg-[#FDFBF7] shadow-sm border-b border-[#EAE6DF]">
      <div class="container mx-auto px-4 lg:px-8">
        <div class="flex items-center justify-between h-20">
          
          <!-- Logo -->
          <a href="index.html" class="flex-shrink-0">
            <img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-auto">
          </a>
          
          <!-- Desktop Menu (Centered - Primary Links Only) -->
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
          </nav>
          
          <!-- Right Side: Cart & Hamburger -->
          <div class="flex items-center space-x-6">
            <button class="snipcart-checkout flex items-center space-x-2 text-black hover:text-gray-600 transition-colors group">
              <div class="relative">
                <i data-feather="shopping-bag" class="w-6 h-6"></i>
                <span class="snipcart-items-count absolute -top-1 -right-2 bg-black text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold">0</span>
              </div>
              <span class="snipcart-total-price hidden sm:block text-sm font-semibold">0.00€</span>
            </button>
            
            <!-- Global Hamburger Menu Toggle (Desktop & Mobile) -->
            <button class="text-black hover:text-gray-600 transition-colors" id="hamburgerBtn">
              <i data-feather="menu" class="w-8 h-8"></i>
            </button>
          </div>
          
        </div>
      </div>
      
      <!-- FULL SCREEN MENU OVERLAY (Side Drawer) -->
      <div id="menuOverlay" class="fixed inset-0 bg-[#FDFBF7] z-[60] flex flex-col justify-between hidden transition-opacity duration-300 opacity-0 overflow-y-auto">
        <!-- Close Button & Top Bar -->
        <div class="container mx-auto px-4 py-6 flex justify-between items-center border-b border-[#EAE6DF]">
            <span class="text-sm font-bold tracking-widest uppercase text-black">Menu de Navegação</span>
            <button id="closeMenuBtn" class="text-black hover:text-gray-600 transition-colors">
                <i data-feather="x" class="w-8 h-8"></i>
            </button>
        </div>
        
        <!-- Main Links Grid -->
        <div class="container mx-auto px-4 py-12 grid grid-cols-1 md:grid-cols-2 gap-12">
            <!-- Col 1: Produtos Principais -->
            <div>
                <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-6 border-b border-[#EAE6DF] pb-2">Catálogo</h3>
                <nav class="flex flex-col space-y-4">
                    <a href="quartos.html" class="text-2xl md:text-4xl font-light hover:text-gray-500 transition-colors">Quartos</a>
                    <a href="salas.html" class="text-2xl md:text-4xl font-light hover:text-gray-500 transition-colors">Salas</a>
                    <a href="cozinha.html" class="text-2xl md:text-4xl font-light hover:text-gray-500 transition-colors">Cozinhas</a>
                    <a href="colchoes.html" class="text-2xl md:text-4xl font-light hover:text-gray-500 transition-colors">Colchões</a>
                    <a href="conjuntos.html" class="text-2xl md:text-4xl font-bold hover:text-gray-500 transition-colors">Comprar Packs</a>
                    <a href="catalogos.html" class="text-2xl md:text-4xl font-light text-gray-500 hover:text-black transition-colors">Ver Catálogos PDF</a>
                </nav>
            </div>
            
            <!-- Col 2: Páginas Secundárias e Empresa -->
            <div>
                <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-6 border-b border-[#EAE6DF] pb-2">A Empresa</h3>
                <nav class="flex flex-col space-y-4">
                    <a href="testemunhos.html" class="text-2xl md:text-3xl font-light hover:text-gray-500 transition-colors">Testemunhos</a>
                    <a href="servicos.html" class="text-2xl md:text-3xl font-light hover:text-gray-500 transition-colors">Serviços</a>
                    <a href="tecidos.html" class="text-2xl md:text-3xl font-light hover:text-gray-500 transition-colors">Guia de Tecidos</a>
                    <a href="contactos.html" class="text-2xl md:text-3xl font-light hover:text-gray-500 transition-colors">Contactos & Lojas</a>
                </nav>
            </div>
        </div>

        <!-- Footer Info inside Drawer -->
        <div class="bg-black text-white py-8 mt-auto">
            <div class="container mx-auto px-4 text-center">
                <p class="text-sm mb-2"><i data-feather="phone" class="w-4 h-4 inline-block mr-2"></i> 212 582 788</p>
                <p class="text-sm text-gray-400">Rua do Feijó, 123 - Almada</p>
            </div>
        </div>
      </div>
    </header>
    
    <script>
      // Drawer Menu Logic
      document.addEventListener('DOMContentLoaded', () => {
        const hamburgerBtn = document.getElementById('hamburgerBtn');
        const closeMenuBtn = document.getElementById('closeMenuBtn');
        const menuOverlay = document.getElementById('menuOverlay');
        
        function openMenu() {
            menuOverlay.classList.remove('hidden');
            // small delay to allow display:block to apply before animating opacity
            setTimeout(() => {
                menuOverlay.classList.remove('opacity-0');
                menuOverlay.classList.add('opacity-100');
            }, 10);
            document.body.style.overflow = 'hidden'; // prevent background scrolling
        }
        
        function closeMenu() {
            menuOverlay.classList.remove('opacity-100');
            menuOverlay.classList.add('opacity-0');
            setTimeout(() => {
                menuOverlay.classList.add('hidden');
            }, 300); // match duration-300
            document.body.style.overflow = '';
        }

        if(hamburgerBtn) hamburgerBtn.addEventListener('click', openMenu);
        if(closeMenuBtn) closeMenuBtn.addEventListener('click', closeMenu);
      });
    </script>
"""

# Apply the NEW_NAVBAR to index.html master header
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

h_start = idx_content.find('<header')
h_end = idx_content.find('</header>') + 9
if h_start != -1 and h_end != -1:
    idx_content = idx_content[:h_start] + NEW_NAVBAR + idx_content[h_end:]
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

# We will run fix_consistency.py again to propagate the new Navbar and Footer to ALL pages including the updated testemunhos.html
import subprocess
subprocess.run(["python3", "fix_consistency.py"])

print("Testimonials removed from index, updated on testemunhos.html, and global Hamburger menu restored to Navbar!")
