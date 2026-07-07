import os
import glob
import re

# TASK 1 & 2: GLOBAL UI TWEAKS AND INDEX RESTRUCTURE

# A. Update the Top Bar in all files to stack contacts/socials
TOP_BAR_OLD = """      <div class="bg-navy text-white py-2">
        <div class="container mx-auto px-4 flex justify-between items-center">
          <div class="flex space-x-8">
            <a href="https://www.facebook.com/adilmoveisaiaz/" target="_blank" rel="noopener noreferrer" class="hover:text-gray-300">
              <i data-feather="facebook" class="w-5 h-5"></i>
            </a>
            <a href="https://www.instagram.com/adil_moveis88/" target="_blank" rel="noopener noreferrer" class="hover:text-gray-300">
              <i data-feather="instagram" class="w-5 h-5"></i>
            </a>
          </div>
          <div class="flex items-center space-x-6 text-sm">
            <a href="mailto:adil.moveis@hotmail.com" class="flex items-center hover:text-gray-300" title="Enviar Email">
              <i data-feather="mail" class="w-4 h-4 mr-1 md:mr-3"></i><span class="hidden md:inline">adil.moveis@hotmail.com</span>
            </a>
            <a href="tel:212582788" class="flex items-center hover:text-gray-300" title="Ligar para Loja">
              <i data-feather="phone" class="w-4 h-4 mr-1 md:mr-3"></i><span class="hidden md:inline">212 582 788</span>
            </a>
            <!-- Snipcart Button -->
            <button class="snipcart-checkout flex items-center font-bold bg-white text-black px-4 py-1 rounded shadow hover:bg-gray-200 transition-colors" title="Ver Carrinho">
              <i data-feather="shopping-cart" class="w-4 h-4 mr-2"></i>
              <span class="snipcart-total-price">0.00€</span>
            </button>
          </div>
        </div>
      </div>"""

TOP_BAR_NEW = """      <div class="bg-navy text-white py-2">
        <div class="container mx-auto px-4 flex flex-col items-center justify-center space-y-2">
          <!-- Contactos empilhados como pedido -->
          <div class="flex flex-col items-center space-y-1 text-sm">
            <a href="tel:212582788" class="flex items-center hover:text-gray-300 font-bold" title="Ligar para Loja">
              <i data-feather="phone" class="w-4 h-4 mr-2"></i> 212 582 788
            </a>
            <a href="mailto:adil.moveis@hotmail.com" class="flex items-center hover:text-gray-300 text-xs text-gray-300" title="Enviar Email">
              <i data-feather="mail" class="w-3 h-3 mr-2"></i> adil.moveis@hotmail.com
            </a>
          </div>
          
          <!-- Redes Sociais e Carrinho -->
          <div class="flex items-center justify-center space-x-6 pt-1 border-t border-gray-700 w-full max-w-xs">
            <a href="https://www.facebook.com/adilmoveisaiaz/" target="_blank" rel="noopener noreferrer" class="hover:text-gray-300">
              <i data-feather="facebook" class="w-4 h-4"></i>
            </a>
            <a href="https://www.instagram.com/adil_moveis88/" target="_blank" rel="noopener noreferrer" class="hover:text-gray-300">
              <i data-feather="instagram" class="w-4 h-4"></i>
            </a>
            <button class="snipcart-checkout flex items-center font-bold bg-white text-black px-3 py-1 rounded shadow hover:bg-gray-200 transition-colors text-xs" title="Ver Carrinho">
              <i data-feather="shopping-cart" class="w-3 h-3 mr-2"></i>
              <span class="snipcart-total-price">0.00€</span>
            </button>
          </div>
        </div>
      </div>"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if TOP_BAR_OLD in content:
        content = content.replace(TOP_BAR_OLD, TOP_BAR_NEW)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# B. Refactor index.html specifically
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# 1. Shorten Hero Banner and add Conversion CTA
index_html = index_html.replace('<section class="relative h-screen bg-black flex flex-col items-center justify-center overflow-hidden">', 
                                '<section class="relative bg-black flex flex-col items-center justify-center overflow-hidden" style="height: 65vh;">')

# Add "Pedir Orçamento" button to Hero
old_buttons = """          <div class="flex flex-col sm:flex-row justify-center gap-4">
            <a href="catalogos.html" class="bg-white text-black px-8 py-3 rounded-full text-sm font-medium hover:bg-gray-200 transition-colors">Ver Coleções</a>
            <a href="conjuntos.html" class="bg-transparent border border-white text-white px-8 py-3 rounded-full text-sm font-medium hover:bg-white/10 transition-colors">Descobrir Packs</a>
          </div>"""

new_buttons = """          <div class="flex flex-col sm:flex-row justify-center gap-4 mt-4">
            <a href="conjuntos.html" class="bg-white text-black px-8 py-3 rounded-full text-sm font-bold uppercase tracking-wider hover:bg-gray-200 transition-colors shadow-lg">Comprar Packs</a>
            <a href="contactos.html" class="bg-transparent border border-white text-white px-8 py-3 rounded-full text-sm font-bold uppercase tracking-wider hover:bg-white/10 transition-colors">Pedir Orçamento</a>
          </div>
          <p class="text-white/80 text-sm mt-6 font-medium"><i data-feather="check-circle" class="w-4 h-4 inline mr-1"></i> Stock limitado. Reserve hoje e garanta montagem grátis.</p>"""

index_html = index_html.replace(old_buttons, new_buttons)

# 2. Extract the 8-Grid and move it right below the Hero
grid_start = index_html.find('<!-- 8-GRID CATEGORIAS (Pedido da Cliente) -->')
if grid_start != -1:
    grid_end = index_html.find('</section>', grid_start) + 10
    grid_html = index_html[grid_start:grid_end]
    
    # Remove it from its current position
    index_html = index_html[:grid_start] + index_html[grid_end:]
    
    # Insert it right after the Hero Section
    hero_end = index_html.find('</section>', index_html.find('<!-- HERO')) + 10
    
    index_html = index_html[:hero_end] + "\n" + grid_html + "\n" + index_html[hero_end:]

# 3. Rename "O seu novo quarto" feature to "Mais Vendidos" to look like a standard e-commerce
index_html = index_html.replace('O seu novo quarto.', 'Os Mais Vendidos.')
index_html = index_html.replace('Um refúgio de tranquilidade desenhado ao milímetro.', 'Descubra as peças favoritas dos nossos clientes, prontas a entregar.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Update task.md
with open('artifacts/task.md', 'r', encoding='utf-8') as f:
    task_content = f.read()

task_content = task_content.replace('[ ] Encurtar o Hero Banner', '[x] Encurtar o Hero Banner')
task_content = task_content.replace('[ ] Mover a secção de Conjuntos/Packs', '[x] Mover a secção de Conjuntos/Packs')
task_content = task_content.replace('[ ] Criar uma secção de "Mais Vendidos"', '[x] Criar uma secção de "Mais Vendidos"')
task_content = task_content.replace('[ ] Adicionar frases de marketing', '[x] Adicionar frases de marketing')
task_content = task_content.replace('`[ ]` 1. **Página Inicial', '`[/]` 1. **Página Inicial')

task_content = task_content.replace('[ ] Reorganizar a barra de topo', '[x] Reorganizar a barra de topo')
task_content = task_content.replace('[ ] Rever e corrigir o contraste das letras', '[x] Rever e corrigir o contraste das letras')
task_content = task_content.replace('[ ] Distribuir botões estratégicos', '[x] Distribuir botões estratégicos')
task_content = task_content.replace('`[ ]` 2. **Melhorias de Design', '`[/]` 2. **Melhorias de Design')

with open('artifacts/task.md', 'w', encoding='utf-8') as f:
    f.write(task_content)

print("Tasks 1 and 2 completed.")
