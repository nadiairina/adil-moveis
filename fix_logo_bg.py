import glob

# 1. ADD OLD REVIEWS TO TESTEMUNHOS.HTML
with open('testemunhos.html', 'r', encoding='utf-8') as f:
    content = f.read()

OLD_REVIEWS = """
          <!-- Review Aniss -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Um serviço de excelência, integridade e confiança."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">A</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Aniss Ali</h4>
                <p class="text-xs text-gray-500">Cliente</p>
              </div>
            </div>
          </div>

          <!-- Review Joana -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Não existe melhor loja! Toda a minha mobília foi comprada nesta loja aconselho a todos que estejam a fazer casa ou a renovar! Atendimento e dedicação 💯 estrelas!!"</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">J</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Joana Silva</h4>
                <p class="text-xs text-gray-500">Cliente</p>
              </div>
            </div>
          </div>

          <!-- Review Paulo -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Fantástica variedade de produtos, com uma atenção ao cliente muito acima da média, mantendo preços muito competitivos. Recomendo."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">P</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Paulo Pires</h4>
                <p class="text-xs text-gray-500">Cliente</p>
              </div>
            </div>
          </div>

          <!-- Review Manuel -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Espetacular, móveis de alta qualidade, preço acessível, simpatia, parabéns Sr Aiaz."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">M</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Manuel Cerqueira</h4>
                <p class="text-xs text-gray-500">Cliente</p>
              </div>
            </div>
          </div>

          <!-- Review Nasrin -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Atendimento toop, preço/qualidade 🤗"</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">N</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Nasrin Ali</h4>
                <p class="text-xs text-gray-500">Cliente</p>
              </div>
            </div>
          </div>

          <!-- Review Ilda -->
          <div class="bg-white p-8 rounded-2xl shadow-sm border border-[#EAE6DF]" data-aos="fade-up">
            <div class="flex items-center space-x-1 text-yellow-400 mb-4">
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
              <i data-feather="star" class="w-5 h-5 fill-current"></i>
            </div>
            <p class="text-gray-700 font-medium mb-6">"Já sou cliente há muitos anos. Recomendo esta loja. Pessoal 5 estrelas."</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-[#2c2a29] rounded-full flex items-center justify-center text-white font-bold">I</div>
              <div>
                <h4 class="font-bold text-sm text-[#2c2a29]">Ilda Dias</h4>
                <p class="text-xs text-gray-500">Cliente</p>
              </div>
            </div>
          </div>
"""

# Find where to inject the old reviews
inject_pos = content.find('</div>\n      </div>\n    </main>')
if inject_pos != -1:
    content = content[:inject_pos] + OLD_REVIEWS + content[inject_pos:]
    with open('testemunhos.html', 'w', encoding='utf-8') as f:
        f.write(content)

# 2. FIX LOGO BLACK BACKGROUND GLOBALLY
# By combining invert (black->white, white->black) and mix-blend-multiply (removes white background)
# We can make a black-background logo render as black text on transparent background!

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Target the logo
    html = html.replace(
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-auto">',
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-14 md:h-16 w-auto invert mix-blend-multiply opacity-90 hover:opacity-100 transition-opacity">'
    )
    # Target index.html logo inside the drawer menu just in case
    html = html.replace(
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-8 w-auto mr-3">',
        '<img src="images/adil-moveis-logo.png" alt="Adil Móveis" class="h-8 w-auto mr-3 invert mix-blend-multiply">'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Testimonials merged and logo black background removed via CSS inversion!")
