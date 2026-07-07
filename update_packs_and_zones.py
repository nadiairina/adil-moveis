import os
import glob
import re

# 1. UPDATE GLOBAL PROMO BANNER IN ALL HTML FILES
OLD_BANNER_1 = '🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS!'
OLD_BANNER_2 = '🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS em Todo o Lado!'
NEW_BANNER = '🚚 Entrega, Montagem e Recolha Grátis num Raio de 50km (Lisboa e Setúbal)!'

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(OLD_BANNER_1, NEW_BANNER)
    content = content.replace(OLD_BANNER_2, NEW_BANNER)
    
    # Also update any text that explicitly says "Totalmente Grátis" without the banner
    content = content.replace('sem custos adicionais na nossa zona', 'gratuitamente num raio de 50km')
    
    # In Apple style index.html:
    content = content.replace('Levamos a sua encomenda até si sem taxas surpresa.', 'Entrega gratuita num raio de 50km (Lisboa e Setúbal).')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. UPDATE CONJUNTOS.HTML WITH THE 5 APPROVED PACKS
PACKS_HTML = """
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          
          <!-- Pack 1 -->
          <div class="group flex flex-col h-full bg-white border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300">
            <div class="relative overflow-hidden bg-[#f5f5f7] aspect-[4/3]">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" alt="Sala" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Sala</div>
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <h3 class="text-2xl font-semibold text-black mb-2 tracking-tight">Pack Sala de Sonho</h3>
              <p class="text-gray-500 mb-6 font-light">Sofá + Móvel de TV</p>
              
              <button class="snipcart-add-item mt-auto w-full bg-black text-white py-4 font-semibold hover:bg-gray-800 transition-colors"
                data-item-id="pack-sala-sonho"
                data-item-price="0.00"
                data-item-name="Pack Sala de Sonho"
                data-item-image="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp">
                Configurar Pack
              </button>
            </div>
          </div>

          <!-- Pack 2 -->
          <div class="group flex flex-col h-full bg-white border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300 relative">
            <!-- Badge -->
            <div class="absolute -top-3 -right-3 bg-red-600 text-white w-14 h-14 rounded-full flex items-center justify-center font-bold text-xs shadow-lg z-20 transform rotate-12">VIP</div>
            <div class="relative overflow-hidden bg-[#f5f5f7] aspect-[4/3]">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" alt="Sala Premium" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" style="filter: contrast(1.1) brightness(1.05);">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Sala Premium</div>
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <h3 class="text-2xl font-semibold text-black mb-2 tracking-tight">Pack Sala de Sonho Premium</h3>
              <p class="text-gray-500 mb-6 font-light">Sofá + Mesa de Centro + Móvel de TV</p>
              
              <button class="snipcart-add-item mt-auto w-full bg-black text-white py-4 font-semibold hover:bg-gray-800 transition-colors"
                data-item-id="pack-sala-premium"
                data-item-price="0.00"
                data-item-name="Pack Sala de Sonho Premium">
                Configurar Pack
              </button>
            </div>
          </div>

          <!-- Pack 3 -->
          <div class="group flex flex-col h-full bg-white border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300">
            <div class="relative overflow-hidden bg-[#f5f5f7] aspect-[4/3]">
              <img src="images/Lourini-Majestic.jpg" alt="Quarto" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Quarto</div>
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <h3 class="text-2xl font-semibold text-black mb-2 tracking-tight">Pack Aconchego Essencial</h3>
              <p class="text-gray-500 mb-6 font-light">Cama + Colchão + Almofadas</p>
              
              <button class="snipcart-add-item mt-auto w-full bg-black text-white py-4 font-semibold hover:bg-gray-800 transition-colors"
                data-item-id="pack-aconchego"
                data-item-price="0.00"
                data-item-name="Pack Aconchego Essencial">
                Configurar Pack
              </button>
            </div>
          </div>

          <!-- Pack 4 -->
          <div class="group flex flex-col h-full bg-white border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300">
            <div class="relative overflow-hidden bg-[#f5f5f7] aspect-[4/3]">
              <img src="https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp" alt="Sala Jantar" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Refeição</div>
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <h3 class="text-2xl font-semibold text-black mb-2 tracking-tight">Pack À Mesa</h3>
              <p class="text-gray-500 mb-6 font-light">Mesa de Refeição + Cadeiras</p>
              
              <button class="snipcart-add-item mt-auto w-full bg-black text-white py-4 font-semibold hover:bg-gray-800 transition-colors"
                data-item-id="pack-mesa"
                data-item-price="0.00"
                data-item-name="Pack À Mesa">
                Configurar Pack
              </button>
            </div>
          </div>

          <!-- Pack 5 -->
          <div class="group flex flex-col h-full bg-white border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300">
            <div class="relative overflow-hidden bg-[#f5f5f7] aspect-[4/3]">
              <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" alt="Sommier" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" style="object-position: top;">
              <div class="absolute top-4 left-4 bg-black text-white px-3 py-1 text-xs font-bold tracking-widest uppercase">Descanso</div>
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <h3 class="text-2xl font-semibold text-black mb-2 tracking-tight">Pack Sonhos Tranquilos</h3>
              <p class="text-gray-500 mb-6 font-light">Sommier Casal + Cabeceira + Colchão</p>
              
              <button class="snipcart-add-item mt-auto w-full bg-black text-white py-4 font-semibold hover:bg-gray-800 transition-colors"
                data-item-id="pack-sonhos"
                data-item-price="0.00"
                data-item-name="Pack Sonhos Tranquilos">
                Configurar Pack
              </button>
            </div>
          </div>

        </div>
"""

with open('conjuntos.html', 'r', encoding='utf-8') as f:
    conj_content = f.read()

# Replace the grid in conjuntos.html
grid_start = conj_content.find('<div class="grid grid-cols-1 md:grid-cols-3 gap-10">')
if grid_start != -1:
    grid_end = conj_content.find('</section>', grid_start) # find next section end, or </main>
    if grid_end == -1:
        grid_end = conj_content.find('</main>', grid_start)
    
    # Actually just replace the `<div class="grid ...` and all its children up to `</main>`
    main_end = conj_content.find('</main>')
    
    new_conj = conj_content[:grid_start] + PACKS_HTML + "\n      </div>\n    </main>" + conj_content[main_end+7:]
    
    # Fix the missing tailwind specific heights
    new_conj = new_conj.replace('h-[450px]', 'h-96')
    new_conj = new_conj.replace('aspect-[4/3]', '')
    
    with open('conjuntos.html', 'w', encoding='utf-8') as f:
        f.write(new_conj)
    
print("Updated packs and delivery zones!")

# 3. Update dashboard
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

if "<!-- Adicionar items -->" in dash or "Lisboa e Setúbal" not in dash:
    dash = dash.replace('<span class="check-desc">Definir raio de entrega grátis e política de montagem (Pai e Sara)</span>', '<span class="check-desc" style="text-decoration: line-through; color: var(--success-color);">Definir raio de entrega: Lisboa e Setúbal (50km). Resto do país com taxa ou recolha em loja.</span>')
    dash = dash.replace('<span class="check-desc">Aprovar lista final de Packs de poupança (Sara)</span>', '<span class="check-desc" style="text-decoration: line-through; color: var(--success-color);">Aprovar lista de 5 Packs: Sala de Sonho, Premium, Aconchego, Mesa, Sonhos Tranquilos.</span>')

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(dash)
