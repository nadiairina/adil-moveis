import glob, re

# Pages that have the inner hero section affected
hero_pages = {
    'quartos.html': {
        'title': 'Quartos',
        'subtitle': 'Crie o quarto dos seus sonhos com a nossa coleção.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'salas.html': {
        'title': 'Salas',
        'subtitle': 'Elegância e conforto para o coração da sua casa.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'colchoes.html': {
        'title': 'Colchões',
        'subtitle': 'Durma melhor. Viva melhor.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'cozinha.html': {
        'title': 'Cozinhas',
        'subtitle': 'Design funcional e intemporal para a sua cozinha.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'escritorio.html': {
        'title': 'Escritórios',
        'subtitle': 'Espaços de trabalho que inspiram produtividade.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'kids.html': {
        'title': 'Crianças & Kids',
        'subtitle': 'Quartos onde a imaginação não tem limites.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'complementos.html': {
        'title': 'Complementos',
        'subtitle': 'Os detalhes que fazem a diferença.',
        'img': "images/Lourini-Majestic.jpg"
    },
    'conjuntos.html': {
        'title': 'Packs & Conjuntos',
        'subtitle': 'Tudo o que precisa, num só pack.',
        'img': "images/Lourini-Majestic.jpg"
    },
}

NEW_HERO_TEMPLATE = """<!-- Slim Hero -->
  <section class="relative h-[280px] md:h-[360px] bg-[#111111] flex items-center justify-center overflow-hidden">
    <div class="absolute inset-0 bg-cover bg-center opacity-30" style="background-image: url('{img}');"></div>
    <div class="relative container mx-auto px-4 h-full flex flex-col justify-center items-center text-center text-white">
      <p class="text-[10px] font-bold tracking-[0.3em] uppercase text-[#C8B598] mb-4">Adil Móveis</p>
      <h1 class="text-4xl md:text-6xl font-light mb-4 tracking-widest uppercase">{title}</h1>
      <div class="w-12 h-px bg-[#C8B598] mb-4"></div>
      <p class="text-sm text-white/70 font-light max-w-lg mx-auto tracking-wide">{subtitle}</p>
    </div>
  </section>"""

OLD_HERO_PATTERN = re.compile(
    r'<!-- Slim Hero -->\s*<section class="relative aspect-\[4/5\][^"]*"[^>]*>(.*?)</section>',
    re.DOTALL
)

for fn, info in hero_pages.items():
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<!-- Slim Hero -->' not in content:
            print(f'No hero found in {fn}')
            continue
        
        new_hero = NEW_HERO_TEMPLATE.format(
            title=info['title'],
            subtitle=info['subtitle'],
            img=info['img']
        )
        
        new_content = OLD_HERO_PATTERN.sub(new_hero, content)
        
        if new_content == content:
            print(f'Pattern not matched in {fn} - trying fallback')
            # Fallback: find the line with the aspect ratio class in the hero section
            old = re.search(r'<!-- Slim Hero -->\s*<section[^>]+>', content)
            if old:
                section_start = old.start()
                # find the closing </section>
                section_end = content.find('</section>', section_start) + len('</section>')
                new_content = content[:section_start] + new_hero + content[section_end:]
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed hero in: {fn}')
    except Exception as e:
        print(f'Error in {fn}: {e}')

print('All done!')
