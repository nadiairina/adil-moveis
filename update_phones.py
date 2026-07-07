import glob
import re

old_wa_pattern = r'href="https://wa\.me/351212582788"'
new_wa = 'href="https://wa.me/351960209396"'

old_footer_phone = r'<p class="mt-6 text-white">212 582 788</p>'
new_footer_phone = """<p class="mt-6 text-white"><i data-feather="phone" class="w-3 h-3 inline mr-1"></i> 212 582 788 (Loja)</p>
            <p class="mt-1 text-white"><i data-feather="message-circle" class="w-3 h-3 inline mr-1 text-[#25D366]"></i> 960 209 396 (WhatsApp)</p>"""

old_header_phone = r'<a href="tel:212582788" class="flex items-center hover:text-gray-300">\s*<i data-feather="phone" class="w-4 h-4 mr-3"></i> 212 582 788\s*</a>'
new_header_phone = """<a href="tel:212582788" class="flex items-center hover:text-gray-300" title="Telefone da Loja">
              <i data-feather="phone" class="w-4 h-4 mr-3"></i> 212 582 788
            </a>
            <a href="https://wa.me/351960209396" target="_blank" class="flex items-center hover:text-[#25D366] transition-colors" title="WhatsApp">
              <i data-feather="message-circle" class="w-4 h-4 mr-2"></i> 960 209 396
            </a>"""

old_sidebar_phone = r'<a href="tel:212582788" class="flex items-center text-sm font-bold text-black mb-1 hover:text-gray-600">\s*<i data-feather="phone" class="w-4 h-4 mr-2"></i> 212 582 788\s*</a>'
new_sidebar_phone = """<a href="tel:212582788" class="flex items-center text-sm font-bold text-black mb-1 hover:text-gray-600">
                            <i data-feather="phone" class="w-4 h-4 mr-2"></i> 212 582 788
                        </a>
                        <a href="https://wa.me/351960209396" target="_blank" class="flex items-center text-xs font-medium text-gray-500 hover:text-[#25D366] transition-colors">
                            <i data-feather="message-circle" class="w-3 h-3 mr-1"></i> 960 209 396
                        </a>"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update WhatsApp links
    content = re.sub(old_wa_pattern, new_wa, content)
    
    # Update Footer Phone
    content = re.sub(old_footer_phone, new_footer_phone, content)
    
    # Update Header Phone (only exists in index.html and maybe a few others if they have the old top bar, but we removed the top bar mostly? Let's check if it exists)
    content = re.sub(old_header_phone, new_header_phone, content)
    
    # Update Sidebar Phone
    content = re.sub(old_sidebar_phone, new_sidebar_phone, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated phones globally.")
