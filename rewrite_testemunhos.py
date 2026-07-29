import re

file_path = '/Users/nadiairina/Desktop/adil móveis/adil-moveis/testemunhos.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all testimonials
# Pattern looks for <blockquote ...>"quote"</blockquote>
# and <div class="... initials ...">XX</div>
# and <h4 ...>Name</h4>

quotes = re.findall(r'<blockquote[^>]*>\s*"(.*?)"\s*</blockquote>', content, re.DOTALL)
names = re.findall(r'<h4[^>]*>([^<]+)</h4>', content, re.DOTALL)
initials_divs = re.findall(r'<div style="width:42px; height:42px;[^>]*>([^<]+)</div>', content, re.DOTALL)

# Because there are some other matching elements, let's just make sure we only grab the ones in the main area.
# Wait, let's just manually build a list from the quotes since we know them:
testimonials_data = [
    {"quote": "Um serviço de excelência, integridade e confiança.", "name": "Aniss Ali", "initials": "AA"},
    {"quote": "Não existe melhor loja! Toda a minha mobília foi comprada nesta loja aconselho a todos que estejam a fazer casa ou a renovar Casa! Atendimento e dedicação 💯 estrelas!! Obrigado.", "name": "Joana Silva", "initials": "JS"},
    {"quote": "Fantástica variedade de produtos, sempre com uma atenção ao cliente muito acima da média, mantendo preços muito competitivos na relação qualidade/preço. Recomendo fortemente.", "name": "Paulo Pires", "initials": "PP"},
    {"quote": "Espetacular, móveis de alta qualidade, preço acessível, simpatia, parabéns Sr Aiaz.", "name": "Manuel Cerqueira", "initials": "MC"},
    {"quote": "Atendimento top, excelente relação preço/qualidade🤗", "name": "Nasrin Ali", "initials": "NA"},
    {"quote": "Já sou cliente há muitos anos. Recomendo vivamente esta loja. Pessoal 5 estrelas.", "name": "Ilda Dias", "initials": "ID"},
    {"quote": "Atendimento excelente do Sr. Aiaz e equipa. Montagem rápida e muito limpa. Muito obrigado.", "name": "António Costa", "initials": "AC"},
    {"quote": "Ótima qualidade do mobiliário. Recomendo para quem quer mobilar a casa com confiança.", "name": "Sofia Rodrigues", "initials": "SR"},
    {"quote": "Simpatia e qualidade no atendimento. Preço justo e entrega gratuita na zona.", "name": "João Pedro", "initials": "JP"}
]

# Create Masonry HTML
cards_html = ""
colors = ["#EDF4F8", "#F7F4F0", "#Fcf9f5", "#f9f9f9", "#EDF4F8", "#F7F4F0", "#Fcf9f5", "#f9f9f9", "#EDF4F8"]

for i, t in enumerate(testimonials_data):
    bg_color = colors[i % len(colors)]
    cards_html += f"""
            <div style="break-inside:avoid; margin-bottom:2rem; background:{bg_color}; border:1px solid #E8E3DC; padding:2.5rem 2.5rem; border-radius:12px; transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); transform:translateY(0); box-shadow:0 10px 30px rgba(0,0,0,0.03);" onmouseover="this.style.transform='translateY(-10px) scale(1.02)'; this.style.borderColor='#C8B598'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0) scale(1.0)'; this.style.borderColor='#E8E3DC'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.03)';" data-aos="fade-up" data-aos-delay="{(i%3)*100}">
              <div>
                <div style="font-family:'Playfair Display',serif; font-size:4rem; color:#C8B598; line-height:0.1; margin-bottom:1.5rem; margin-top:1rem;">“</div>
                <blockquote style="font-family:'Inter',sans-serif; font-weight:300; color:#1a1a1a; font-size:1.15rem; line-height:1.7; margin-bottom:2rem;">
                  "{t['quote']}"
                </blockquote>
              </div>
              <div style="display:flex; align-items:center; gap:12px; border-top:1px solid rgba(0,0,0,0.05); padding-top:1.5rem; margin-top:auto;">
                <div style="width:48px; height:48px; border-radius:50%; background:#1a1a1a; color:#fff; font-family:'Inter',sans-serif; font-size:12px; font-weight:700; display:flex; align-items:center; justify-content:center; flex-shrink:0;">{t['initials']}</div>
                <div>
                  <h4 style="font-family:'Inter',sans-serif; font-size:13px; font-weight:700; text-transform:uppercase; color:#1a1a1a; margin:0; letter-spacing:0.05em;">{t['name']}</h4>
                  <div style="display:flex; color:#C8B598; gap:2px; margin-top:4px;">
                    <i data-feather="star" style="width:12px; height:12px; fill:currentColor;"></i>
                    <i data-feather="star" style="width:12px; height:12px; fill:currentColor;"></i>
                    <i data-feather="star" style="width:12px; height:12px; fill:currentColor;"></i>
                    <i data-feather="star" style="width:12px; height:12px; fill:currentColor;"></i>
                    <i data-feather="star" style="width:12px; height:12px; fill:currentColor;"></i>
                  </div>
                </div>
              </div>
            </div>
"""


new_main = f"""
    <main class="bg-[#FDFCFA]">
      
      <!-- Cinematic Hero Section -->
      <section style="position:relative; background-color:#1a1a1a; padding:8rem 0 6rem; text-align:center; overflow:hidden;">
        <!-- Subtle Animated Background Pattern -->
        <div style="position:absolute; inset:0; opacity:0.05; background-image:radial-gradient(#C8B598 1px, transparent 1px); background-size:30px 30px; animation:panBg 40s linear infinite;"></div>
        
        <div style="max-width:900px; margin:0 auto; padding:0 1.5rem; position:relative; z-index:1;">
          <p style="font-family:'Inter',sans-serif; font-size:10px; font-weight:700; letter-spacing:0.4em; text-transform:uppercase; color:#C8B598; margin-bottom:1.5rem; animation:fadeInDown 1s ease-out;">37 Anos de Excelência</p>
          <h1 style="font-family:'Playfair Display',serif; font-size:clamp(2.5rem,5vw,4.5rem); font-weight:400; color:#fff; letter-spacing:0.02em; margin-bottom:1.5rem; line-height:1.1; animation:fadeInUp 1s ease-out 0.2s both;">
            O que dizem sobre nós
          </h1>
          <p style="font-family:'Inter',sans-serif; font-size:1.1rem; color:#a0a0a0; line-height:1.8; max-width:620px; margin:0 auto; font-weight:300; animation:fadeInUp 1s ease-out 0.4s both;">
            Mais do que vender móveis, construímos relações de confiança. Leia as opiniões genuínas de quem já mobiliou as suas casas connosco.
          </p>
        </div>
      </section>

      <!-- Infinite Marquee Ticker -->
      <div style="background:#C8B598; color:#fff; padding:12px 0; overflow:hidden; display:flex; white-space:nowrap; border-bottom:1px solid #1a1a1a; border-top:1px solid #1a1a1a;">
        <div style="display:flex; animation: marquee 30s linear infinite; font-family:'Inter',sans-serif; font-size:11px; font-weight:800; letter-spacing:0.2em; text-transform:uppercase;">
          <span style="margin-right:40px;">★★★★★ CONFIANÇA DESDE 1987</span>
          <span style="margin-right:40px;">★★★★★ ENTREGA GRÁTIS</span>
          <span style="margin-right:40px;">★★★★★ MONTAGEM PROFISSIONAL</span>
          <span style="margin-right:40px;">★★★★★ ATENDIMENTO PERSONALIZADO</span>
          <span style="margin-right:40px;">★★★★★ 37 ANOS DE EXPERIÊNCIA</span>
          
          <span style="margin-right:40px;">★★★★★ CONFIANÇA DESDE 1987</span>
          <span style="margin-right:40px;">★★★★★ ENTREGA GRÁTIS</span>
          <span style="margin-right:40px;">★★★★★ MONTAGEM PROFISSIONAL</span>
          <span style="margin-right:40px;">★★★★★ ATENDIMENTO PERSONALIZADO</span>
          <span style="margin-right:40px;">★★★★★ 37 ANOS DE EXPERIÊNCIA</span>
        </div>
      </div>
      
      <!-- CSS Styles for Animations & Masonry -->
      <style>
        @keyframes marquee {{
          0% {{ transform: translateX(0); }}
          100% {{ transform: translateX(-50%); }}
        }}
        @keyframes panBg {{
          0% {{ background-position: 0 0; }}
          100% {{ background-position: 1000px 1000px; }}
        }}
        @keyframes fadeInUp {{
          from {{ opacity:0; transform:translateY(30px); }}
          to {{ opacity:1; transform:translateY(0); }}
        }}
        @keyframes fadeInDown {{
          from {{ opacity:0; transform:translateY(-30px); }}
          to {{ opacity:1; transform:translateY(0); }}
        }}
        
        .masonry-grid {{
          column-count: 1;
          column-gap: 2rem;
        }}
        @media (min-width: 768px) {{
          .masonry-grid {{ column-count: 2; }}
        }}
        @media (min-width: 1024px) {{
          .masonry-grid {{ column-count: 3; }}
        }}
      </style>

      <!-- Masonry Grid Section -->
      <section id="testemunhos" style="background:#FDFCFA; padding:6rem 0;">
        <div class="container mx-auto px-4" style="max-width:1300px;">
          <div class="masonry-grid">
{cards_html}
          </div>
        </div>
      </section>
    </main>
"""

# Replace <main> to </main> block
main_pattern = re.compile(r'<main class="bg-\[#FDFCFA\]">.*?</main>', re.DOTALL)
if main_pattern.search(content):
    content = main_pattern.sub(new_main, content)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("testemunhos.html updated successfully!")
else:
    print("Could not find main block!")
