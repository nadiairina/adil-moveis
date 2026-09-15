import re

with open('contactos.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = """<!-- Contact Form + Calendly Scheduler -->
            <div id="agendar-visita-form" class="bg-white p-8 rounded border border-[#E8E3DC] text-center" data-aos="fade-left">
              <h3 style="font-family:'Playfair Display',serif; font-size:1.8rem; color:#1a1a1a; font-weight:500; margin-bottom:1rem;">Fale Connosco no WhatsApp</h3>
              <p class="text-sm text-gray-600 mb-8" style="line-height: 1.6;">
                Diga adeus aos formulários aborrecidos! O nosso atendimento é 100% humano, rápido e feito diretamente pelo telemóvel. Clique numa das opções abaixo:
              </p>
              
              <div class="space-y-4">
                <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20pedir%20um%20or%C3%A7amento%20ou%20fazer%20uma%20pergunta." target="_blank" rel="noopener" style="background-color: #25D366; color: white; border: none; font-size: 14px; font-weight: bold; text-decoration:none; display:flex;" class="w-full py-4 px-6 rounded shadow items-center justify-center gap-3 hover:bg-green-500 transition-colors">
                  <span style="font-size:20px;">💬</span> PEDIR ORÇAMENTO / DÚVIDAS
                </a>
                
                <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Quero%20agendar%20uma%20visita%20%C3%A0%20loja%3A%0A%0ANome%3A%0ADia%20e%20Hora%3A%0AProcuro%20por%3A" target="_blank" rel="noopener" style="background-color: #C8B598; color: white; border: none; font-size: 14px; font-weight: bold; text-decoration:none; display:flex;" class="w-full py-4 px-6 rounded shadow items-center justify-center gap-3 hover:bg-[#b09e85] transition-colors">
                  <span style="font-size:20px;">📅</span> AGENDAR VISITA À LOJA
                </a>
              </div>
            </div>"""

content = re.sub(r'<!-- Contact Form \+ Calendly Scheduler -->.*?</div>\s*</div>\s*</div>', new_content + "\n          </div>\n        </div>", content, flags=re.DOTALL)

with open('contactos.html', 'w', encoding='utf-8') as f:
    f.write(content)

