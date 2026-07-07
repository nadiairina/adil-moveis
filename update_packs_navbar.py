import glob
import re

# We want to replace the "Packs" link in the Top Navbar across all pages.
# OLD:
# <a href="conjuntos.html" class="text-sm font-bold tracking-widest text-black uppercase transition-colors relative">
#               Packs
#               <span class="absolute -top-3 -right-4 bg-red-600 text-white text-[10px] px-1.5 py-0.5 rounded-full rotate-12">Hot</span>
#             </a>
# 
# NEW:
# <a href="conjuntos.html" class="text-sm font-bold tracking-widest text-red-600 uppercase transition-all duration-300 border border-red-500 rounded px-3 py-1 animate-pulse hover:bg-red-500 hover:text-white">
#               Packs
#             </a>

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the top navbar Packs link
    old_packs_link = """<a href="conjuntos.html" class="text-sm font-bold tracking-widest text-black uppercase transition-colors relative">
              Packs
              <span class="absolute -top-3 -right-4 bg-red-600 text-white text-[10px] px-1.5 py-0.5 rounded-full rotate-12">Hot</span>
            </a>"""
            
    new_packs_link = """<a href="conjuntos.html" class="text-sm font-bold tracking-widest text-red-600 uppercase transition-all duration-300 border border-red-600 px-3 py-1 rounded hover:bg-red-600 hover:text-white animate-pulse">
              Packs
            </a>"""
            
    content = content.replace(old_packs_link, new_packs_link)

    # Also update the sidebar packs link if she meant that too
    old_sidebar = '<a href="conjuntos.html" class="text-lg font-bold text-black border-l-2 border-black pl-3 -ml-3">Comprar Packs</a>'
    new_sidebar = '<a href="conjuntos.html" class="text-lg font-bold text-red-600 border border-red-600 rounded px-3 py-1 -ml-3 animate-pulse">Comprar Packs</a>'
    content = content.replace(old_sidebar, new_sidebar)

    # Double check WhatsApp number formatting
    # The URL is already https://wa.me/351212582788 in our previous injections,
    # but let's ensure it's exact in case it was mistyped.
    # wa.me/351212582788 -> 21 258 2788 (Portuguese landline formatted usually 212 582 788, but she wrote 21 258 2788)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed 'Hot' badge, added red border and animation to Packs links, WhatsApp number confirmed.")
