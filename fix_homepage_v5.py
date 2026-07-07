import os
import glob
import re

# 1. UPDATE TAILWIND TO V3 CDN GLOBALLY
OLD_TAILWIND = '<link rel="stylesheet" href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" />'
NEW_TAILWIND = '<script src="https://cdn.tailwindcss.com"></script>'

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if OLD_TAILWIND in content:
        content = content.replace(OLD_TAILWIND, NEW_TAILWIND)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. REWRITE "MAIS VENDIDOS" AND REMOVE SPLIT GRIDS IN INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Find the start of "Mais Vendidos" section
mv_start = index_html.find('<!-- FEATURE 1 (Massive Product Showcase) -->')
# Find the end of the Apple split grids
grids_end = index_html.find('</section>', index_html.find('<!-- FEATURE GRID (Split layout like Apple) -->')) + 10

if mv_start != -1 and grids_end != -1:
    NEW_MAIS_VENDIDOS = """
      <!-- MAIS VENDIDOS (GRID DE E-COMMERCE) -->
      <section class="py-24 bg-[#fafafa]">
        <div class="container mx-auto px-4 max-w-7xl">
          <div class="text-center mb-16" data-aos="fade-up">
            <h2 class="text-4xl font-semibold text-black tracking-tight mb-4">Os Mais Vendidos.</h2>
            <p class="text-xl text-gray-500 font-light">As peças favoritas dos nossos clientes, prontas a entregar.</p>
          </div>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
            <!-- Produto 1 -->
            <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col" data-aos="fade-up" data-aos-delay="0">
              <div class="relative aspect-square overflow-hidden bg-[#f0f0f0]">
                <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                <div class="absolute top-3 left-3 bg-black text-white text-xs font-bold px-2 py-1 rounded uppercase tracking-wider">Top 1</div>
              </div>
              <div class="p-6 flex flex-col flex-grow text-center">
                <h3 class="text-lg font-bold text-black mb-1">Sofá Canto Amazónia</h3>
                <p class="text-gray-500 text-sm mb-4">Tecido Antimancha</p>
                <div class="mt-auto">
                    <button class="text-sm font-bold uppercase tracking-widest text-black border-b-2 border-black pb-1 hover:text-gray-600 hover:border-gray-600 transition-colors">Configurar e Comprar</button>
                </div>
              </div>
            </div>

            <!-- Produto 2 -->
            <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col" data-aos="fade-up" data-aos-delay="100">
              <div class="relative aspect-square overflow-hidden bg-[#f0f0f0]">
                <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
              </div>
              <div class="p-6 flex flex-col flex-grow text-center">
                <h3 class="text-lg font-bold text-black mb-1">Colchão Greysoft</h3>
                <p class="text-gray-500 text-sm mb-4">Ortopédico Alta Densidade</p>
                <div class="mt-auto">
                    <button class="text-sm font-bold uppercase tracking-widest text-black border-b-2 border-black pb-1 hover:text-gray-600 hover:border-gray-600 transition-colors">Configurar e Comprar</button>
                </div>
              </div>
            </div>

            <!-- Produto 3 -->
            <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col" data-aos="fade-up" data-aos-delay="200">
              <div class="relative aspect-square overflow-hidden bg-[#f0f0f0]">
                <img src="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
              </div>
              <div class="p-6 flex flex-col flex-grow text-center">
                <h3 class="text-lg font-bold text-black mb-1">Mesa Extensível Paris</h3>
                <p class="text-gray-500 text-sm mb-4">Acabamento Carvalho</p>
                <div class="mt-auto">
                    <button class="text-sm font-bold uppercase tracking-widest text-black border-b-2 border-black pb-1 hover:text-gray-600 hover:border-gray-600 transition-colors">Configurar e Comprar</button>
                </div>
              </div>
            </div>

            <!-- Produto 4 -->
            <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col" data-aos="fade-up" data-aos-delay="300">
              <div class="relative aspect-square overflow-hidden bg-[#f0f0f0]">
                <img src="https://lourini.pt/app/uploads/2024/09/escritorio-nizza-1200x1200.png" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
              </div>
              <div class="p-6 flex flex-col flex-grow text-center">
                <h3 class="text-lg font-bold text-black mb-1">Secretária Nizza</h3>
                <p class="text-gray-500 text-sm mb-4">Design Minimalista</p>
                <div class="mt-auto">
                    <button class="text-sm font-bold uppercase tracking-widest text-black border-b-2 border-black pb-1 hover:text-gray-600 hover:border-gray-600 transition-colors">Configurar e Comprar</button>
                </div>
              </div>
            </div>

          </div>
          
          <div class="text-center mt-12">
            <a href="catalogos.html" class="inline-block bg-black text-white px-8 py-4 rounded-full text-sm font-bold uppercase tracking-wider hover:bg-gray-800 transition-colors shadow-lg">Ver Todos os Produtos</a>
          </div>
        </div>
      </section>
"""
    index_html = index_html[:mv_start] + NEW_MAIS_VENDIDOS + index_html[grids_end:]

# 3. FIX TEXTOS EM AZUL (If any remain)
index_html = index_html.replace('text-blue-600', 'text-black border-b-2 border-black')
index_html = index_html.replace('text-blue-400', 'text-white border-b border-white')

# 4. ADD SNIPCART ANIMATION LISTENER
SNIPCART_ANIMATION = """
<style>
@keyframes popIn {
  0% { transform: scale(0.8) translateY(20px); opacity: 0; }
  50% { transform: scale(1.05) translateY(-5px); }
  100% { transform: scale(1) translateY(0); opacity: 1; }
}
.cart-toast {
  animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}
</style>
<script>
document.addEventListener('snipcart.ready', function() {
    Snipcart.events.on('item.added', (cartItem) => {
        // Criar elemento de notificação
        const toast = document.createElement('div');
        toast.className = 'cart-toast fixed bottom-24 right-4 md:right-8 bg-green-500 text-white px-6 py-4 rounded-xl shadow-2xl z-50 flex items-center gap-3 font-medium';
        toast.innerHTML = `<i data-feather="check-circle" class="w-6 h-6"></i> <span>Adicionado ao carrinho!</span>`;
        document.body.appendChild(toast);
        if (typeof feather !== 'undefined') feather.replace();
        
        // Fazer a notificação desaparecer
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.5s ease';
            setTimeout(() => toast.remove(), 500);
        }, 3000);
    });
});
</script>
"""

if "Snipcart.events.on('item.added'" not in index_html:
    index_html = index_html.replace('</body>', SNIPCART_ANIMATION + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Homepage redesign, footer fix, and animations applied!")
