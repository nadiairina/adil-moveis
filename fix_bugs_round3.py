import glob
import re

# 1. FIX LOGO BORDER GLOBALLY
# Change `border-gray-200` on the logo to `border-[#C8B598]` (a fitting beige/gold color)
for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply the colored border
    old_logo_class = 'border border-gray-200'
    new_logo_class = 'border-2 border-[#D4C3B3]' # Slightly thicker, beautiful taupe/gold
    
    # We only want to replace it inside the logo img tag
    logo_pattern = r'(<img src="images/logo\.png"[^>]+)border border-gray-200([^>]*>)'
    content = re.sub(logo_pattern, r'\1border-2 border-[#C8B598]\2', content)

    # 2. FIX WHATSAPP Z-INDEX GLOBALLY
    # Find the WhatsApp button and lower its z-index from 50 to 40 so the Sidebar (999) covers it
    whatsapp_pattern = r'(href="https://wa\.me/351212582788"[^>]+)z-50([^>]*>)'
    content = re.sub(whatsapp_pattern, r'\1z-40\2', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. RESTORE HERO IMAGE IN COLCHOES.HTML
with open('colchoes.html', 'r', encoding='utf-8') as f:
    colchoes = f.read()

# Only add if it's missing (it currently is)
if 'Colchões</h1>' not in colchoes[:colchoes.find('<main')]:
    hero_section = """
    <!-- HERO SECTION RESTORED -->
    <section class="relative bg-black flex flex-col items-center justify-center overflow-hidden" style="height: 50vh;">
      <div class="absolute inset-0 z-0">
        <img src="https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp" class="w-full h-full object-cover scale-105 transform origin-center opacity-70" alt="Hero Colchões" data-aos="zoom-out" data-aos-duration="2000">
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent z-10"></div>
      </div>
      <div class="relative z-20 text-center px-4" data-aos="fade-up" data-aos-duration="1000">
        <h1 class="text-white text-5xl md:text-7xl font-light tracking-widest mb-4 drop-shadow-2xl uppercase">Colchões</h1>
        <p class="text-white/90 text-lg md:text-xl font-light max-w-2xl mx-auto drop-shadow-md">O descanso perfeito começa aqui. Descubra a nossa gama de conforto absoluto.</p>
      </div>
    </section>
    
    <main class="bg-[#FDFBF7] py-16">"""
    
    colchoes = colchoes.replace('<main class="bg-[#FDFBF7] py-16">', hero_section)
    
    with open('colchoes.html', 'w', encoding='utf-8') as f:
        f.write(colchoes)

print("Restored hero in colchoes, lowered WhatsApp z-index, added gold border to logo.")
