import glob
import re

# 1. Update global sidebar menu to include Kids, Escritório, and Complementos
old_sidebar_links = r'<a href="colchoes\.html" class="text-lg font-medium text-gray-800 hover:text-black">Colchões</a>'
new_sidebar_links = """<a href="colchoes.html" class="text-lg font-medium text-gray-800 hover:text-black">Colchões</a>
                    <a href="kids.html" class="text-lg font-medium text-gray-800 hover:text-black">Crianças / Kids</a>
                    <a href="escritorio.html" class="text-lg font-medium text-gray-800 hover:text-black">Escritórios</a>
                    <a href="complementos.html" class="text-lg font-medium text-gray-800 hover:text-black">Complementos</a>"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "Crianças / Kids" not in content:
        content = re.sub(old_sidebar_links, new_sidebar_links, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. Redesign the Hero sections for Kids, Escritório, and Complementos
def update_hero(filename, title, subtitle, image_url):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the <main> block or old hero section and replace it with the new Hero layout
    # The old hero is typically: <section class="relative bg-gray-200">...</section>
    old_hero_pattern = r'<section class="relative bg-gray-200">.*?(?:</section>\s*<main|<main)'
    
    new_hero = f"""<main class="bg-[#FDFBF7] pt-0">
      <section class="relative h-80 md:h-[50vh] bg-black overflow-hidden flex flex-col items-center justify-center">
        <div class="absolute inset-0 z-0">
          <img src="{image_url}" class="w-full h-full object-cover scale-105 transform origin-center opacity-70" alt="{title}" data-aos="zoom-out" data-aos-duration="2000">
          <div class="absolute inset-0 bg-black/50 z-10"></div>
        </div>
        <div class="relative z-20 text-center px-4" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="text-white text-4xl md:text-6xl font-light tracking-widest mb-4 uppercase drop-shadow-2xl">{title}</h1>
          <p class="text-white/90 text-lg md:text-xl font-light max-w-2xl mx-auto">{subtitle}</p>
        </div>
      </section>
      <div class="container mx-auto px-4 max-w-7xl py-16">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">"""

    # We also need to fix the products grid to make sure it matches the new styling, but since it's already a grid, we can just replace everything up to the grid start
    # Let's use a simpler approach: just find <main> and the text center block
    text_center_pattern = r'<main class="bg-\[#FDFBF7\] py-16">\s*<div class="container mx-auto px-4 max-w-7xl">\s*<div class="text-center mb-16">.*?</div>\s*<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">'
    
    content = re.sub(r'<section class="relative bg-gray-200">.*?</section>\s*<main class="bg-\[#FDFBF7\] py-16">\s*<div class="container mx-auto px-4 max-w-7xl">\s*<div class="text-center mb-16">.*?</div>\s*<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">', new_hero, content, flags=re.DOTALL)
    
    # Just in case the old hero wasn't there
    if new_hero not in content:
        content = re.sub(text_center_pattern, new_hero, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_hero('kids.html', 'Kids & Juvenil', 'Quartos desenhados para crescer e inspirar.', 'https://lourini.pt/app/uploads/2024/07/quarto-juvenil-1200x1200.png')
update_hero('escritorio.html', 'Escritório', 'Ambientes de trabalho funcionais e elegantes.', 'https://lourini.pt/app/uploads/2024/07/mesa-extensivel-1200x1200.webp')
update_hero('complementos.html', 'Complementos', 'O detalhe que faz a diferença no seu espaço.', 'https://lourini.pt/app/uploads/2024/09/bona-sala-1200x1200.webp')

print("Updated the 3 missing categories and injected them into the sidebar menu.")
