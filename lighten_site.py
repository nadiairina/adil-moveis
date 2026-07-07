import os
import glob

OLD_BANNER = """    <!-- Global Promo Banner -->
    <div class="bg-black text-white text-center py-3 text-sm font-bold tracking-wide z-50 relative">
      🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS em Todo o Lado!
    </div>"""

NEW_BANNER = """    <!-- Global Promo Banner -->
    <div class="bg-[#f8f5f0] text-gray-800 text-center py-3 text-sm font-semibold tracking-wide z-50 relative border-b border-gray-200">
      🚚 Entrega, Montagem e Recolha de Usados Totalmente GRÁTIS!
    </div>"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Lighten banner
    if OLD_BANNER in content:
        content = content.replace(OLD_BANNER, NEW_BANNER)
    # Also catch slight variations of the banner if they exist
    content = content.replace('bg-black text-white text-center py-3 text-sm font-bold tracking-wide z-50 relative', 'bg-[#f8f5f0] text-gray-800 text-center py-3 text-sm font-semibold tracking-wide z-50 relative border-b border-gray-200')
    
    # Specific fixes for index.html benefits section
    if filepath == "index.html":
        # Invert benefits section from black to warm off-white
        content = content.replace('class="py-24 bg-black text-white relative"', 'class="py-24 bg-[#faf9f6] text-gray-900 relative"')
        
        # Subtitles (gray-400 -> gray-600)
        content = content.replace('text-sm font-bold tracking-widest uppercase text-gray-400 mb-6', 'text-sm font-bold tracking-widest uppercase text-gray-500 mb-6')
        
        # Descriptions (gray-400 text-xl -> gray-600 text-xl)
        content = content.replace('class="text-gray-400 text-xl leading-relaxed"', 'class="text-gray-600 text-xl leading-relaxed"')
        
        # Icon circles (white bg, black icon -> white bg with shadow, dark gray icon)
        content = content.replace('class="w-24 h-24 bg-white text-black rounded-full flex items-center justify-center mb-8 transform group-hover:-translate-y-2 transition-transform duration-300"', 'class="w-24 h-24 bg-white text-gray-800 shadow-md rounded-full flex items-center justify-center mb-8 transform group-hover:-translate-y-2 transition-transform duration-300"')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Site lightened successfully.")
