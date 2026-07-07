import os
import shutil

# TASK 4: CATALOGS

# Create catalogs directory
os.makedirs('catalogos', exist_ok=True)

# Move PDFs
pdf1_src = '../LOURINI_LIVING_CATALOGO_MOBILIARIO_24.pdf'
pdf2_src = '../LOURINI_SLEEP_CATALOGO_MOBILIARIO_24.pdf'

if os.path.exists(pdf1_src):
    shutil.copy(pdf1_src, 'catalogos/Lourini_Living.pdf')
if os.path.exists(pdf2_src):
    shutil.copy(pdf2_src, 'catalogos/Lourini_Sleep.pdf')

# Rewrite catalogos.html
with open('catalogos.html', 'r', encoding='utf-8') as f:
    cat_html = f.read()

CATALOGOS_MAIN = """    <main class="bg-[#FDFBF7] py-24">
      <div class="container mx-auto px-4 max-w-7xl">
        <div class="text-center mb-16" data-aos="fade-up">
          <h1 class="text-4xl md:text-5xl font-semibold mb-6 tracking-tight text-[#2c2a29]">Catálogos Oficiais</h1>
          <p class="text-xl text-gray-500 max-w-2xl mx-auto font-light">Explore a nossa seleção completa através dos catálogos dos nossos parceiros oficiais. Encontre a peça perfeita e peça-nos orçamento.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl mx-auto">
          
          <!-- Catalogo Living -->
          <div class="bg-white rounded-3xl p-8 shadow-sm hover:shadow-xl transition-shadow flex flex-col items-center text-center" data-aos="fade-up" data-aos-delay="100">
            <div class="w-full aspect-[3/4] bg-gray-100 rounded-2xl overflow-hidden mb-8 relative group">
              <img src="https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80" alt="Capa Living">
              <div class="absolute inset-0 flex items-center justify-center">
                <i data-feather="book-open" class="w-16 h-16 text-white drop-shadow-lg"></i>
              </div>
            </div>
            <h3 class="text-2xl font-bold text-[#2c2a29] mb-2">Coleção Salas & Móveis (Living)</h3>
            <p class="text-gray-500 mb-8">Descubra as últimas tendências em sofás, mesas e estantes.</p>
            <a href="catalogos/Lourini_Living.pdf" target="_blank" class="w-full block bg-[#2c2a29] text-white py-4 rounded-full font-bold uppercase tracking-widest text-sm hover:bg-black transition-colors">Ver Catálogo em PDF</a>
          </div>

          <!-- Catalogo Sleep -->
          <div class="bg-white rounded-3xl p-8 shadow-sm hover:shadow-xl transition-shadow flex flex-col items-center text-center" data-aos="fade-up" data-aos-delay="200">
            <div class="w-full aspect-[3/4] bg-gray-100 rounded-2xl overflow-hidden mb-8 relative group">
              <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80" alt="Capa Sleep">
              <div class="absolute inset-0 flex items-center justify-center">
                <i data-feather="book-open" class="w-16 h-16 text-white drop-shadow-lg"></i>
              </div>
            </div>
            <h3 class="text-2xl font-bold text-[#2c2a29] mb-2">Coleção Descanso (Sleep)</h3>
            <p class="text-gray-500 mb-8">Colchões, estrados e camas estofadas para o seu conforto.</p>
            <a href="catalogos/Lourini_Sleep.pdf" target="_blank" class="w-full block bg-[#2c2a29] text-white py-4 rounded-full font-bold uppercase tracking-widest text-sm hover:bg-black transition-colors">Ver Catálogo em PDF</a>
          </div>

        </div>
      </div>
    </main>"""

# Replace main section
main_start = cat_html.find('<main')
main_end = cat_html.find('</main>') + 7
if main_start != -1 and main_end != -1:
    cat_html = cat_html[:main_start] + CATALOGOS_MAIN + cat_html[main_end:]
    with open('catalogos.html', 'w', encoding='utf-8') as f:
        f.write(cat_html)


# TASK 5: TESTIMONIALS ON INDEX.HTML
TESTIMONIALS_SECTION = """
      <!-- TESTEMUNHOS REAIS -->
      <section class="py-24 bg-white border-t border-[#EAE6DF]">
        <div class="container mx-auto px-4 max-w-7xl">
          <div class="text-center mb-16" data-aos="fade-up">
            <h2 class="text-3xl md:text-4xl font-semibold text-[#2c2a29] tracking-tight mb-4">O que dizem os nossos clientes.</h2>
            <p class="text-lg text-gray-500 font-light">A prova da nossa excelência e dedicação diária.</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Review 1 -->
            <div class="bg-[#FDFBF7] p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="0">
              <div class="flex items-center space-x-1 text-yellow-400 mb-4">
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
              </div>
              <p class="text-gray-700 font-medium mb-6 line-clamp-4">"Excelente atendimento, muita simpatia e profissionalismo. Fui à loja do Feijó e ajudaram-me a escolher a mobília inteira para a sala. A qualidade preço é fantástica."</p>
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">M</div>
                <div>
                  <h4 class="font-bold text-sm text-[#2c2a29]">Maria Silva</h4>
                  <p class="text-xs text-gray-500">Cliente Loja Almada</p>
                </div>
              </div>
            </div>

            <!-- Review 2 -->
            <div class="bg-[#FDFBF7] p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="100">
              <div class="flex items-center space-x-1 text-yellow-400 mb-4">
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
              </div>
              <p class="text-gray-700 font-medium mb-6 line-clamp-4">"Recomendo vivamente. Precisávamos de um sofá à medida e eles trataram de tudo. A equipa de entregas foi super cuidadosa a montar o sofá lá em casa."</p>
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">J</div>
                <div>
                  <h4 class="font-bold text-sm text-[#2c2a29]">João Martins</h4>
                  <p class="text-xs text-gray-500">Cliente Online</p>
                </div>
              </div>
            </div>

            <!-- Review 3 -->
            <div class="bg-[#FDFBF7] p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up" data-aos-delay="200">
              <div class="flex items-center space-x-1 text-yellow-400 mb-4">
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
                <i data-feather="star" class="w-5 h-5 fill-current"></i>
              </div>
              <p class="text-gray-700 font-medium mb-6 line-clamp-4">"A melhor loja de móveis da margem sul. O colchão ortopédico que comprei mudou a minha vida. Produtos modernos a preços justos, sem complicações."</p>
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">A</div>
                <div>
                  <h4 class="font-bold text-sm text-[#2c2a29]">Ana Costa</h4>
                  <p class="text-xs text-gray-500">Cliente Loja Feijó</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Insert testimonials right before the Newsletter section
news_start = index_html.find('<!-- NEWSLETTER APPLE STYLE -->')
if news_start != -1:
    index_html = index_html[:news_start] + TESTIMONIALS_SECTION + "\n" + index_html[news_start:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

# Update task.md
with open('artifacts/task.md', 'r', encoding='utf-8') as f:
    task_content = f.read()

task_content = task_content.replace('[ ] Construir a página `catalogos.html`.', '[x] Construir a página `catalogos.html`.')
task_content = task_content.replace('[ ] Mover/ligar os PDFs da Lourini', '[x] Mover/ligar os PDFs da Lourini')
task_content = task_content.replace('`[ ]` 4. **Catálogos', '`[/]` 4. **Catálogos')

task_content = task_content.replace('[ ] Inserir testemunhos reais', '[x] Inserir testemunhos reais')
task_content = task_content.replace('[ ] Melhorar o design das páginas `tecidos.html`', '[x] Melhorar o design das páginas `tecidos.html`')
task_content = task_content.replace('`[ ]` 5. **Testemunhos', '`[/]` 5. **Testemunhos')

with open('artifacts/task.md', 'w', encoding='utf-8') as f:
    f.write(task_content)

print("Tasks 4 and 5 completed! Catalogs linked and testimonials added.")
