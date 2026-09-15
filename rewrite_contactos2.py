import re

with open('contactos.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div id="agendar-visita-form"')
end_idx = content.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    old_section = content[start_idx:end_idx]
    
    right_col_new = """<div id="agendar-visita-form" class="flex flex-col justify-center h-full">
              <div class="text-left mb-8">
                <h3 style="font-family:'Playfair Display',serif; font-size:2.5rem; color:#1a1a1a; font-weight:400; margin-bottom:1rem; line-height:1.2;">Fale Connosco <br><span style="color:#C8B598; font-style:italic;">no WhatsApp</span></h3>
                <p class="text-base text-gray-600" style="line-height: 1.8; max-width:400px;">
                  O nosso atendimento é 100% humano, rápido e feito diretamente pelo seu telemóvel. Escolha uma das opções abaixo:
                </p>
              </div>
              
              <div class="space-y-4 max-w-md">
                <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20pedir%20um%20or%C3%A7amento%20para%20o%20produto%3A%20" target="_blank" rel="noopener" style="background-color: #25D366; color: white; border: none; font-size: 14px; font-weight: bold; text-decoration:none; display:flex;" class="w-full py-4 px-6 rounded shadow items-center justify-center gap-3 hover:bg-green-500 transition-colors">
                  <span style="font-size:20px;">💬</span> PEDIR ORÇAMENTO / DÚVIDAS
                </a>
                
                <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Quero%20agendar%20uma%20visita%20%C3%A0%20loja%3A%0A%0ANome%3A%0ADia%20e%20Hora%3A%0AProcuro%20por%3A" target="_blank" rel="noopener" style="background-color: #C8B598; color: white; border: none; font-size: 14px; font-weight: bold; text-decoration:none; display:flex;" class="w-full py-4 px-6 rounded shadow items-center justify-center gap-3 hover:bg-[#b09e85] transition-colors">
                  <span style="font-size:20px;">📅</span> AGENDAR VISITA À LOJA
                </a>
              </div>
            </div>
          </div>
        </div>
      """
    content = content[:start_idx] + right_col_new + content[end_idx:]

with open('contactos.html', 'w', encoding='utf-8') as f:
    f.write(content)

