import glob
import re

# 1. Update the sidebar footer globally to include "Agendar Visita" and colorful social media buttons.
sidebar_footer_pattern = r'<!-- Footer -->\s*<div class="p-6 bg-gray-50 border-t border-\[#EAE6DF\]">.*?</div>\s*</div>'

NEW_SIDEBAR_FOOTER = """<!-- Footer -->
            <div class="p-6 bg-gray-50 border-t border-[#EAE6DF]">
                <!-- Marcar Visita Button -->
                <a href="contactos.html" class="flex items-center justify-center w-full py-3 mb-6 border border-black text-black font-bold uppercase tracking-widest text-[11px] rounded hover:bg-black hover:text-white transition-colors shadow-sm">
                    <i data-feather="map-pin" class="w-4 h-4 mr-2"></i> Agendar Visita à Loja
                </a>
                
                <div class="flex justify-between items-center">
                    <div>
                        <a href="tel:212582788" class="flex items-center text-sm font-bold text-black mb-1 hover:text-gray-600">
                            <i data-feather="phone" class="w-4 h-4 mr-2"></i> 212 582 788
                        </a>
                        <p class="text-xs text-gray-500">Rua do Feijó, 123 - Almada</p>
                    </div>
                    
                    <!-- Social Media (Colored) -->
                    <div class="flex space-x-2">
                        <a href="https://www.facebook.com/p/Adil-M%C3%B3veis-100063641348118/" target="_blank" class="text-[#1877F2] hover:bg-[#1877F2] hover:text-white transition-colors bg-white p-2 rounded-full shadow-sm border border-gray-200">
                            <i data-feather="facebook" class="w-4 h-4"></i>
                        </a>
                        <a href="https://www.instagram.com/adilmoveis/" target="_blank" class="text-[#E1306C] hover:bg-[#E1306C] hover:text-white transition-colors bg-white p-2 rounded-full shadow-sm border border-gray-200">
                            <i data-feather="instagram" class="w-4 h-4"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>"""


# 2. Update the main footer social icons globally.
main_footer_social_pattern = r'<div class="flex space-x-6">\s*<a href="#" class="hover:text-white transition-colors"><i data-feather="facebook" class="w-5 h-5"></i></a>\s*<a href="#" class="hover:text-white transition-colors"><i data-feather="instagram" class="w-5 h-5"></i></a>\s*</div>'

NEW_MAIN_FOOTER_SOCIAL = """<div class="flex space-x-4">
              <a href="https://www.facebook.com/p/Adil-M%C3%B3veis-100063641348118/" target="_blank" class="flex items-center space-x-2 text-white hover:text-[#1877F2] transition-colors group">
                <i data-feather="facebook" class="w-5 h-5"></i>
              </a>
              <a href="https://www.instagram.com/adilmoveis/" target="_blank" class="flex items-center space-x-2 text-white hover:text-[#E1306C] transition-colors group ml-2">
                <i data-feather="instagram" class="w-5 h-5"></i>
              </a>
            </div>"""


for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace sidebar footer
    content = re.sub(sidebar_footer_pattern, NEW_SIDEBAR_FOOTER, content, flags=re.DOTALL)
    
    # Replace main footer social
    content = re.sub(main_footer_social_pattern, NEW_MAIN_FOOTER_SOCIAL, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# 3. Update `produto-detalhe.html` to add the "Ver na Loja" button next to the WhatsApp button.
with open('produto-detalhe.html', 'r', encoding='utf-8') as f:
    produto = f.read()

whatsapp_btn_pattern = r'<!-- WhatsApp Helper -->.*?</a>'
TWO_BUTTONS = """<!-- Helpers -->
            <div class="grid grid-cols-2 gap-3 mb-6">
              <a href="contactos.html" class="w-full flex items-center justify-center space-x-2 py-3 border border-black text-black hover:bg-black hover:text-white transition-colors rounded text-[11px] font-bold uppercase tracking-wider">
                <i data-feather="map-pin" class="w-4 h-4"></i>
                <span>Ver na Loja</span>
              </a>
              <a href="https://wa.me/351212582788" target="_blank" class="w-full flex items-center justify-center space-x-2 py-3 border border-gray-300 text-gray-700 hover:bg-[#25D366] hover:text-white hover:border-[#25D366] transition-colors rounded text-[11px] font-bold uppercase tracking-wider group">
                <i data-feather="message-circle" class="w-4 h-4 text-[#25D366] group-hover:text-white"></i>
                <span>Dúvidas?</span>
              </a>
            </div>"""

produto = re.sub(whatsapp_btn_pattern, TWO_BUTTONS, produto, flags=re.DOTALL)

with open('produto-detalhe.html', 'w', encoding='utf-8') as f:
    f.write(produto)

print("Added Marcar Visita buttons and updated social media colors globally.")
