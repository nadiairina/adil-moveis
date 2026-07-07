import glob
import re

# We will read `salas.html` to extract the layout skeleton (Header, Footer, Scripts)
with open('salas.html', 'r', encoding='utf-8') as f:
    skeleton = f.read()

# Extract everything before `<main...>`
head_pattern = r'^(.*?)<main'
head_match = re.search(head_pattern, skeleton, flags=re.DOTALL)
header_html = head_match.group(1) if head_match else ""

# Extract everything after `</main>`
tail_pattern = r'</main>(.*?)$'
tail_match = re.search(tail_pattern, skeleton, flags=re.DOTALL)
footer_html = tail_match.group(1) if tail_match else ""

# -------------------------------------------------------------
# 1. BUILD PRODUTO-DETALHE.HTML
# -------------------------------------------------------------

PRODUTO_MAIN = """
<main class="bg-[#FDFBF7] py-12 md:py-24">
  <div class="container mx-auto px-4 max-w-7xl">
    <!-- Breadcrumbs -->
    <nav class="flex text-sm text-gray-500 mb-8" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-3">
        <li class="inline-flex items-center">
          <a href="index.html" class="hover:text-black">Início</a>
        </li>
        <li>
          <div class="flex items-center">
            <i data-feather="chevron-right" class="w-4 h-4 mx-1"></i>
            <a href="salas.html" class="hover:text-black">Salas</a>
          </div>
        </li>
        <li aria-current="page">
          <div class="flex items-center">
            <i data-feather="chevron-right" class="w-4 h-4 mx-1"></i>
            <span class="text-black font-medium">Sofá Chaise Longue Florença</span>
          </div>
        </li>
      </ol>
    </nav>

    <!-- Product Layout -->
    <div class="flex flex-col lg:flex-row gap-12 lg:gap-20">
      
      <!-- Left: Image Gallery -->
      <div class="w-full lg:w-[60%] flex flex-col gap-4">
        <!-- Main Image -->
        <div class="w-full aspect-[4/3] md:aspect-video bg-[#f0ede6] rounded-xl overflow-hidden cursor-zoom-in group">
           <img src="https://lourini.pt/app/uploads/2024/09/dennis-32-1200x1200.webp" id="mainImage" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Sofá Principal">
        </div>
        <!-- Thumbnails -->
        <div class="grid grid-cols-4 gap-4">
           <button class="aspect-square bg-gray-200 rounded-lg overflow-hidden border-2 border-black thumb-btn">
             <img src="https://lourini.pt/app/uploads/2024/09/dennis-32-1200x1200.webp" class="w-full h-full object-cover">
           </button>
           <button class="aspect-square bg-gray-200 rounded-lg overflow-hidden border-2 border-transparent hover:border-gray-400 thumb-btn">
             <img src="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp" class="w-full h-full object-cover">
           </button>
           <button class="aspect-square bg-gray-200 rounded-lg overflow-hidden border-2 border-transparent hover:border-gray-400 thumb-btn">
             <img src="https://lourini.pt/app/uploads/2024/09/bona-sala-1200x1200.webp" class="w-full h-full object-cover">
           </button>
           <button class="aspect-square bg-gray-200 rounded-lg overflow-hidden border-2 border-transparent hover:border-gray-400 thumb-btn">
             <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover">
           </button>
        </div>
      </div>

      <!-- Right: Product Info -->
      <div class="w-full lg:w-[40%]">
         <div class="sticky top-32">
            <h1 class="text-3xl md:text-4xl font-light text-black mb-2 tracking-tight">Sofá Chaise Longue Florença</h1>
            <p class="text-gray-500 text-sm mb-6 uppercase tracking-widest">Lourini Premium</p>
            <div class="text-2xl md:text-3xl font-medium text-black mb-8" id="productPrice">899,00 €</div>

            <!-- Size Selection -->
            <div class="mb-8">
              <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest mb-3">Tamanho</h3>
              <div class="grid grid-cols-2 gap-3">
                 <button class="border border-black bg-black text-white py-3 px-4 rounded text-xs font-bold uppercase tracking-wider transition-colors size-btn" data-price="899,00 €" data-val="Chaise Longue">Chaise Longue</button>
                 <button class="border border-gray-300 text-gray-600 hover:border-black py-3 px-4 rounded text-xs font-bold uppercase tracking-wider transition-colors size-btn" data-price="699,00 €" data-val="3 Lugares">3 Lugares</button>
              </div>
            </div>

            <!-- Fabric Selection -->
            <div class="mb-8">
              <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest mb-3 flex justify-between">
                <span>Tecido e Cor</span>
                <a href="tecidos.html" class="text-gray-400 hover:text-black underline font-medium">Guia de Tecidos</a>
              </h3>
              <div class="flex flex-wrap gap-4">
                 <!-- Swatch 1 -->
                 <button class="relative w-12 h-12 rounded-full bg-gray-400 ring-2 ring-offset-2 ring-black flex items-center justify-center group fabric-btn" data-val="Veludo Cinza">
                   <span class="absolute -top-10 bg-black text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">Veludo Cinza</span>
                 </button>
                 <!-- Swatch 2 -->
                 <button class="relative w-12 h-12 rounded-full bg-[#D4C3B3] ring-1 ring-offset-2 ring-gray-300 hover:ring-black flex items-center justify-center group fabric-btn" data-val="Veludo Bege">
                   <span class="absolute -top-10 bg-black text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">Veludo Bege</span>
                 </button>
                 <!-- Swatch 3 -->
                 <button class="relative w-12 h-12 rounded-full bg-[#1c2e4a] ring-1 ring-offset-2 ring-gray-300 hover:ring-black flex items-center justify-center group fabric-btn" data-val="Microfibra Azul">
                   <span class="absolute -top-10 bg-black text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">Microfibra Azul</span>
                 </button>
              </div>
            </div>

            <!-- Add to Cart -->
            <button id="addToCartBtn" class="w-full bg-black text-white py-4 rounded font-bold uppercase tracking-widest hover:bg-gray-800 transition-colors mb-6 shadow-lg flex items-center justify-center space-x-2 snipcart-add-item"
              data-item-id="sofa-florenca"
              data-item-price="899.00"
              data-item-name="Sofá Chaise Longue Florença"
              data-item-image="https://lourini.pt/app/uploads/2024/09/dennis-32-1200x1200.webp"
              data-item-custom1-name="Tamanho"
              data-item-custom1-options="Chaise Longue|3 Lugares[-200.00]"
              data-item-custom1-value="Chaise Longue"
              data-item-custom2-name="Tecido"
              data-item-custom2-options="Veludo Cinza|Veludo Bege|Microfibra Azul"
              data-item-custom2-value="Veludo Cinza">
              <i data-feather="shopping-bag" class="w-5 h-5"></i>
              <span>Adicionar ao Carrinho</span>
            </button>

            <!-- WhatsApp Helper -->
            <a href="https://wa.me/351212582788" target="_blank" class="w-full flex items-center justify-center space-x-2 py-3 border border-gray-300 text-gray-700 hover:bg-gray-50 transition-colors rounded text-sm font-medium">
              <i data-feather="message-circle" class="w-4 h-4 text-[#25D366]"></i>
              <span>Dúvidas? Fale com um assistente</span>
            </a>

            <!-- Accordions -->
            <div class="mt-12 border-t border-gray-200">
              <!-- Accordion 1 -->
              <div class="border-b border-gray-200 py-4">
                <button class="flex justify-between items-center w-full text-left font-bold text-black uppercase tracking-widest text-sm hover:text-gray-600 accordion-btn">
                  <span>Dimensões & Montagem</span>
                  <i data-feather="plus" class="w-4 h-4 transition-transform duration-300"></i>
                </button>
                <div class="hidden pt-4 text-gray-500 font-light text-sm leading-relaxed accordion-content">
                  <p class="mb-2"><strong class="text-gray-700">Chaise Longue:</strong> 280cm (Largura) x 160cm (Profundidade) x 95cm (Altura)</p>
                  <p class="mb-2"><strong class="text-gray-700">3 Lugares:</strong> 220cm (Largura) x 90cm (Profundidade) x 95cm (Altura)</p>
                  <p class="mt-4"><i data-feather="tool" class="w-4 h-4 inline mr-1 text-black"></i> Este produto requer montagem, que será efetuada <strong>gratuitamente</strong> pela nossa equipa no momento da entrega.</p>
                </div>
              </div>
              <!-- Accordion 2 -->
              <div class="border-b border-gray-200 py-4">
                <button class="flex justify-between items-center w-full text-left font-bold text-black uppercase tracking-widest text-sm hover:text-gray-600 accordion-btn">
                  <span>Materiais e Cuidados</span>
                  <i data-feather="plus" class="w-4 h-4 transition-transform duration-300"></i>
                </button>
                <div class="hidden pt-4 text-gray-500 font-light text-sm leading-relaxed accordion-content">
                  <p>Estrutura em madeira maciça de pinho e aglomerado. Espumas de poliuretano de alta densidade para conforto duradouro. Pés metálicos com acabamento preto mate.</p>
                  <p class="mt-2">Recomendamos limpeza regular com aspirador e escova macia. Evite exposição direta à luz solar prolongada.</p>
                </div>
              </div>
              <!-- Accordion 3 -->
              <div class="border-b border-gray-200 py-4">
                <button class="flex justify-between items-center w-full text-left font-bold text-black uppercase tracking-widest text-sm hover:text-gray-600 accordion-btn">
                  <span>Entregas e Devoluções</span>
                  <i data-feather="plus" class="w-4 h-4 transition-transform duration-300"></i>
                </button>
                <div class="hidden pt-4 text-gray-500 font-light text-sm leading-relaxed accordion-content">
                  <p>Entrega <strong>gratuita</strong> num raio de 50km da nossa loja no Feijó. O prazo de entrega estimado para sofás personalizados é de 3 a 5 semanas.</p>
                </div>
              </div>
            </div>

         </div>
      </div>

    </div>
  </div>
</main>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // Gallery Thumbnails
    const mainImg = document.getElementById('mainImage');
    const thumbs = document.querySelectorAll('.thumb-btn');
    thumbs.forEach(thumb => {
        thumb.addEventListener('click', () => {
            // Remove active border from all
            thumbs.forEach(t => {
                t.classList.remove('border-black');
                t.classList.add('border-transparent');
            });
            // Add active border to clicked
            thumb.classList.remove('border-transparent');
            thumb.classList.add('border-black');
            // Update main image src
            mainImg.src = thumb.querySelector('img').src;
        });
    });

    // Size Selection
    const sizeBtns = document.querySelectorAll('.size-btn');
    const priceDisplay = document.getElementById('productPrice');
    const addToCartBtn = document.getElementById('addToCartBtn');
    
    sizeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Reset all size buttons
            sizeBtns.forEach(b => {
                b.className = "border border-gray-300 text-gray-600 hover:border-black py-3 px-4 rounded text-xs font-bold uppercase tracking-wider transition-colors size-btn";
            });
            // Active state
            btn.className = "border border-black bg-black text-white py-3 px-4 rounded text-xs font-bold uppercase tracking-wider transition-colors size-btn";
            // Update price
            priceDisplay.textContent = btn.getAttribute('data-price');
            // Update Snipcart attribute
            addToCartBtn.setAttribute('data-item-custom1-value', btn.getAttribute('data-val'));
        });
    });

    // Fabric Selection
    const fabricBtns = document.querySelectorAll('.fabric-btn');
    fabricBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Reset all rings
            fabricBtns.forEach(b => {
                b.classList.remove('ring-2', 'ring-black');
                b.classList.add('ring-1', 'ring-gray-300');
            });
            // Active state
            btn.classList.remove('ring-1', 'ring-gray-300');
            btn.classList.add('ring-2', 'ring-black');
            // Update Snipcart attribute
            addToCartBtn.setAttribute('data-item-custom2-value', btn.getAttribute('data-val'));
        });
    });

    // Accordions
    const accBtns = document.querySelectorAll('.accordion-btn');
    accBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const content = btn.nextElementSibling;
            const icon = btn.querySelector('svg');
            content.classList.toggle('hidden');
            if(content.classList.contains('hidden')){
                btn.innerHTML = btn.innerHTML.replace('minus', 'plus');
                if(typeof feather !== 'undefined') feather.replace();
            } else {
                btn.innerHTML = btn.innerHTML.replace('plus', 'minus');
                if(typeof feather !== 'undefined') feather.replace();
            }
        });
    });
});
</script>
"""

with open('produto-detalhe.html', 'w', encoding='utf-8') as f:
    f.write(header_html + PRODUTO_MAIN + footer_html)


# -------------------------------------------------------------
# 2. BUILD EMPRESA.HTML
# -------------------------------------------------------------

EMPRESA_MAIN = """
<main class="bg-[#FDFBF7]">
  <!-- Hero -->
  <section class="relative bg-black flex flex-col items-center justify-center overflow-hidden" style="height: 60vh;">
    <div class="absolute inset-0 z-0">
      <img src="images/historia1.jpg" class="w-full h-full object-cover scale-105 transform origin-center opacity-60" alt="A Nossa História" data-aos="zoom-out" data-aos-duration="2000">
      <div class="absolute inset-0 bg-black/60 z-10"></div>
    </div>
    <div class="relative z-20 text-center px-4" data-aos="fade-up" data-aos-duration="1000">
      <h1 class="text-white text-4xl md:text-6xl font-light tracking-widest mb-4 uppercase drop-shadow-2xl">A Nossa História</h1>
      <p class="text-white/90 text-lg md:text-xl font-light max-w-2xl mx-auto tracking-wide">30 anos de dedicação ao mobiliário e conforto da sua família.</p>
    </div>
  </section>

  <!-- Story Section -->
  <section class="py-24">
    <div class="container mx-auto px-4 max-w-4xl text-center">
      <h2 class="text-3xl font-light text-black mb-10 tracking-tight" data-aos="fade-up">UMA TRADIÇÃO FAMILIAR</h2>
      
      <div class="text-lg leading-loose text-gray-600 font-light space-y-8 text-left md:text-justify" data-aos="fade-up" data-aos-delay="100">
        <p>A <strong class="text-black font-medium">Adil Móveis</strong> é uma empresa de mobiliário composta por 3 lojas situadas no Feijó. Gerida por 3 irmãos, conta já com mais de 30 anos de experiência e disponibiliza desde mobiliário tradicional e clássico até ao design mais moderno, contemporâneo e arrojado.</p>
        
        <p>Temos uma grande exposição de combinações para quartos de casal e individuais, salas de estar e de jantar. Complementamos o seu espaço com secretárias, cadeiras, cadeirões e sofás, onde tem a total liberdade de escolher o modelo, o tecido e a cor que mais lhe agradam.</p>
        
        <p>Na nossa vasta gama de descanso, oferecemos colchões de excelência desenvolvidos em vários materiais: desde o núcleo de alta densidade, látex, viscoelástica, até às avançadas molas ensacadas independentes, desenhados para satisfazer todos os tipos de gosto e fisionomia!</p>
      </div>
    </div>
  </section>

  <!-- Classic Gallery -->
  <section class="py-12 bg-white border-y border-gray-100">
    <div class="container mx-auto px-4 max-w-7xl">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="overflow-hidden rounded-lg shadow-sm group" data-aos="fade-up" data-aos-delay="0">
          <img src="images/historia1.jpg" alt="Loja Adil Móveis 1" class="w-full h-auto object-cover transform transition-transform duration-700 group-hover:scale-105">
        </div>
        <div class="overflow-hidden rounded-lg shadow-sm group" data-aos="fade-up" data-aos-delay="100">
          <img src="images/historia2.jpg" alt="Loja Adil Móveis 2" class="w-full h-auto object-cover transform transition-transform duration-700 group-hover:scale-105">
        </div>
        <div class="overflow-hidden rounded-lg shadow-sm group" data-aos="fade-up" data-aos-delay="200">
          <img src="images/historia3.jpg" alt="Loja Adil Móveis 3" class="w-full h-auto object-cover transform transition-transform duration-700 group-hover:scale-105">
        </div>
      </div>
    </div>
  </section>

  <!-- Values & Brands -->
  <section class="py-24 bg-[#f8f5f0]">
    <div class="container mx-auto px-4 max-w-6xl text-center">
      <h2 class="text-3xl font-light text-black mb-16 tracking-tight" data-aos="fade-up">O QUE NOS DEFINE</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-16">
        <div data-aos="fade-up" data-aos-delay="0">
          <div class="w-16 h-16 mx-auto bg-black text-white rounded-full flex items-center justify-center mb-6">
            <i data-feather="star" class="w-6 h-6"></i>
          </div>
          <h3 class="text-xl font-bold mb-3 text-black">Grandes Marcas</h3>
          <p class="text-gray-500 font-light leading-relaxed text-sm">Colaboramos com marcas de excelência como a Lourini, Gioestofos, Móveis AF, Lar Ibérico e Vidal Lar. O nosso armazém está sempre repleto de produtos prontos para entrega.</p>
        </div>

        <div data-aos="fade-up" data-aos-delay="100">
          <div class="w-16 h-16 mx-auto bg-black text-white rounded-full flex items-center justify-center mb-6">
            <i data-feather="tool" class="w-6 h-6"></i>
          </div>
          <h3 class="text-xl font-bold mb-3 text-black">Serviço Completo</h3>
          <p class="text-gray-500 font-light leading-relaxed text-sm">Entregamos, montamos e recolhemos o seu mobiliário usado gratuitamente. Asseguramos um serviço atencioso e de enorme qualidade.</p>
        </div>

        <div data-aos="fade-up" data-aos-delay="200">
          <div class="w-16 h-16 mx-auto bg-black text-white rounded-full flex items-center justify-center mb-6">
            <i data-feather="heart" class="w-6 h-6"></i>
          </div>
          <h3 class="text-xl font-bold mb-3 text-black">Pós-Venda</h3>
          <p class="text-gray-500 font-light leading-relaxed text-sm">A nossa relação não termina na entrega. Garantimos durabilidade a preços acessíveis e um apoio pós-venda sempre próximo e resolutivo.</p>
        </div>
      </div>
      
      <div class="mt-16">
        <a href="contactos.html" class="inline-block border border-black text-black px-10 py-3 rounded font-bold uppercase tracking-widest text-xs hover:bg-black hover:text-white transition-colors" data-aos="fade-up">Visite-nos no Feijó</a>
      </div>
    </div>
  </section>

</main>
"""

with open('empresa.html', 'w', encoding='utf-8') as f:
    f.write(header_html + EMPRESA_MAIN + footer_html)


# -------------------------------------------------------------
# 3. UPDATE GLOBAL NAVIGATION TO ADD "A NOSSA HISTÓRIA"
# -------------------------------------------------------------

# We want to replace the old navigation block under "Empresa" in ALL files.
OLD_NAV_EMPRESA = """<nav class="flex flex-col space-y-4">
                    <a href="testemunhos.html" class="text-sm font-medium text-gray-600 hover:text-black">Testemunhos</a>
                    <a href="servicos.html" class="text-sm font-medium text-gray-600 hover:text-black">Serviços</a>
                    <a href="tecidos.html" class="text-sm font-medium text-gray-600 hover:text-black">Guia de Tecidos</a>
                    <a href="contactos.html" class="text-sm font-medium text-gray-600 hover:text-black">Contactos & Lojas</a>
                </nav>"""

NEW_NAV_EMPRESA = """<nav class="flex flex-col space-y-4">
                    <a href="empresa.html" class="text-sm font-medium text-gray-600 hover:text-black">A Nossa História</a>
                    <a href="testemunhos.html" class="text-sm font-medium text-gray-600 hover:text-black">Testemunhos</a>
                    <a href="servicos.html" class="text-sm font-medium text-gray-600 hover:text-black">Serviços</a>
                    <a href="tecidos.html" class="text-sm font-medium text-gray-600 hover:text-black">Guia de Tecidos</a>
                    <a href="contactos.html" class="text-sm font-medium text-gray-600 hover:text-black">Contactos & Lojas</a>
                </nav>"""

# Since spacing might differ slightly, we'll use regex to find the Empresa block and rewrite it.
# The Empresa section is preceded by: <h3 class="... pt-8">Empresa</h3>
empresa_block_pattern = r'(<h3[^>]*>Empresa</h3>\s*<nav[^>]*>)(.*?)(</nav>)'

def replacer(match):
    # Keep the heading and <nav> opening, replace the links, keep the </nav> closing
    # But to be safe, let's just inject `empresa.html` as the first link if it doesn't exist
    links = match.group(2)
    if 'empresa.html' not in links:
        links = '\n                    <a href="empresa.html" class="text-sm font-medium text-gray-600 hover:text-black">A Nossa História</a>' + links
    return match.group(1) + links + match.group(3)

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply the regex substitution for the sidebar
    content = re.sub(empresa_block_pattern, replacer, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Created produto-detalhe.html, empresa.html, and updated sidebar globally.")
