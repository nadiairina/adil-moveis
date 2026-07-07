import re

with open('kids.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the inner hero section (the one with aspect-[4/5])
OLD = '''      <section class="relative aspect-[4/5] bg-[#f9f6f0] flex items-center justify-center overflow-hidden border-b border-[#EAE6DF]">
        <div class="absolute inset-0 z-0">
          <img src="https://lourini.pt/app/uploads/2024/07/quarto-juvenil-1200x1200.png" class="w-full h-full object-cover scale-105 transform origin-center opacity-70" alt="Kids &amp; Juvenil" data-aos="zoom-out" data-aos-duration="2000">
          <div class="absolute inset-0 bg-black/50 z-10"></div>
        </div>
        <div class="relative z-20 text-center px-4" data-aos="fade-up" data-aos-duration="1000">
          <h1 class="text-white text-4xl md:text-6xl font-light tracking-widest mb-4 uppercase drop-shadow-2xl">Kids &amp; Juvenil</h1>
          <p class="text-white/90 text-lg md:text-xl font-light max-w-2xl mx-auto">Quartos desenhados para crescer e inspirar.</p>
        </div>
      </section>'''

NEW = '''<!-- Slim Hero -->
  <section class="relative h-[280px] md:h-[360px] bg-[#111111] flex items-center justify-center overflow-hidden">
    <div class="absolute inset-0 bg-cover bg-center opacity-30" style="background-image: url('images/Lourini-Majestic.jpg');"></div>
    <div class="relative container mx-auto px-4 h-full flex flex-col justify-center items-center text-center text-white">
      <p class="text-[10px] font-bold tracking-[0.3em] uppercase text-[#C8B598] mb-4">Adil Móveis</p>
      <h1 class="text-4xl md:text-6xl font-light mb-4 tracking-widest uppercase">Kids &amp; Juvenil</h1>
      <div class="w-12 h-px bg-[#C8B598] mb-4"></div>
      <p class="text-sm text-white/70 font-light max-w-lg mx-auto tracking-wide">Quartos desenhados para crescer e inspirar.</p>
    </div>
  </section>'''

# Also remove the wrapper sections that became empty
content = content.replace(
    '''    <!-- Hero Section with Logo and Menu Button -->
<section class="relative bg-gray-200">
  <!-- Logo and Menu positioning container -->
  

        <main class="bg-[#FDFBF7] pt-0">''',
    '\n  <main class="bg-[#FDFBF7] pt-0">'
)

# Replace the aspect-ratio hero
if OLD in content:
    content = content.replace(OLD, NEW)
    print("Replaced kids hero")
else:
    print("Pattern not found exactly — trying regex")
    pattern = re.compile(r'<section class="relative aspect-\[4/5\][^"]*"[^>]*>.*?</section>', re.DOTALL)
    content = pattern.sub(NEW, content, count=1)
    print("Done with regex")

with open('kids.html', 'w', encoding='utf-8') as f:
    f.write(content)
    
print("kids.html saved")
