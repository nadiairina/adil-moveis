import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. FIX BROKEN DOUBLE CLASSES
content = re.sub(r'class="([^"]+)"\s*class="text-gray-900"', r'class="\1 text-gray-800"', content)
content = re.sub(r'class="([^"]+)"\s*class="border-gray-900"', r'class="\1 border-gray-800"', content)

# 2. EXTRACT SECTIONS
# Newsletter
news_start = content.find('<!-- Newsletter Section -->')
if news_start == -1:
    news_start = content.find('<section class="bg-gray-100 py-12')
news_end = content.find('</section>', news_start) + 10
newsletter_block = content[news_start:news_end]

# Sobre Nos
sobre_start = content.find('<!-- Secção Sobre Nós')
sobre_end = content.find('</section>', sobre_start) + 10
sobre_block = content[sobre_start:sobre_end]

# Remove them from content
content = content.replace(newsletter_block, '')
content = content.replace(sobre_block, '')

# Let's clean up the newsletter block to make it more fancy/premium
refined_newsletter = """
    <!-- Newsletter Section -->
    <section class="py-20 bg-gray-50 border-t border-gray-200">
      <div class="container mx-auto px-4 max-w-3xl">
        <div class="bg-white p-10 md:p-14 rounded-2xl shadow-sm border border-gray-100 text-center relative overflow-hidden">
          <!-- Decorativo -->
          <div class="absolute top-0 left-0 w-full h-1 bg-black"></div>
          
          <h2 class="text-3xl md:text-4xl font-bold mb-4 tracking-tight">OFERTA ESPECIAL</h2>
          <p class="text-gray-600 mb-8 text-lg">Subscreva a nossa newsletter e receba <strong>10% de desconto extra</strong> na sua primeira encomenda.</p>
          
          <div class="ml-embedded w-full" data-form="oCm4cl"></div>
          
          <p class="text-xs text-gray-400 mt-6 uppercase tracking-widest">Sem spam, prometemos. Apenas móveis bonitos.</p>
        </div>
      </div>
    </section>
"""

# Let's clean up the sobre_block to fix any residual weirdness
refined_sobre = """
    <!-- Secção Sobre Nós (Confiança e Negócio Local) -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-4 max-w-6xl">
        <div class="flex flex-col md:flex-row items-center gap-16">
          <div class="md:w-1/2">
            <div class="relative">
              <img src="images/Lourini-Majestic.jpg" alt="A nossa loja no Feijó" class="w-full h-auto rounded-xl shadow-2xl object-cover">
              <div class="absolute -bottom-8 -right-8 bg-black text-white p-6 rounded-lg shadow-xl hidden md:block border-l-4 border-gray-400">
                <p class="font-bold text-xl mb-1 tracking-wide">Família & Tradição</p>
                <p class="text-sm text-gray-300">Há décadas no Feijó</p>
              </div>
            </div>
          </div>
          <div class="md:w-1/2 space-y-8">
            <div>
              <h2 class="text-sm font-bold tracking-widest uppercase text-gray-500 mb-2">A Nossa História</h2>
              <h3 class="text-3xl md:text-5xl font-bold text-black leading-tight tracking-tight">O compromisso da nossa família para com a sua casa.</h3>
            </div>
            
            <p class="text-gray-600 text-lg leading-relaxed">
              A <strong>Adil Móveis</strong> não é apenas uma loja; é o projeto de uma vida. Nascidos e criados no coração do Feijó (Almada), sabemos que a confiança de um cliente conquista-se com honestidade, serviço e durabilidade.
            </p>
            
            <p class="text-gray-600 text-lg leading-relaxed">
              Não queremos apenas "vender caixas". O nosso foco é garantir que o cliente não tem dores de cabeça. Por isso oferecemos o serviço premium: <strong>entregamos e montamos tudo com o máximo cuidado, e recolhemos os usados gratuitamente na nossa zona.</strong>
            </p>
            
            <div class="pt-6 border-t border-gray-100">
              <ul class="space-y-4">
                <li class="flex items-center text-gray-800 font-medium text-lg">
                  <span class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center mr-4"><i data-feather="map-pin" class="w-4 h-4 text-black"></i></span>
                  Lojas Físicas com aconselhamento direto
                </li>
                <li class="flex items-center text-gray-800 font-medium text-lg">
                  <span class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center mr-4"><i data-feather="heart" class="w-4 h-4 text-black"></i></span>
                  Atendimento próximo e de confiança
                </li>
                <li class="flex items-center text-gray-800 font-medium text-lg">
                  <span class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center mr-4"><i data-feather="tool" class="w-4 h-4 text-black"></i></span>
                  Qualidade e montagem profissional garantidas
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# Re-insert them in the correct order before footer
# Search for footer
footer_idx = content.find('<footer class="bg-black')

if footer_idx != -1:
    new_content = content[:footer_idx] + refined_sobre + "\n" + refined_newsletter + "\n" + content[footer_idx:]
else:
    new_content = content + "\n" + refined_sobre + "\n" + refined_newsletter

# Clean up multiple empty lines
new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Index fixed, swapped, and refined.")
