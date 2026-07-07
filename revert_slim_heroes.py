import glob
import re

pages = {
    "quartos.html": {"title": "Quartos", "desc": "Crie o quarto dos seus sonhos com a nossa coleção.", "img": "images/Lourini-Majestic.jpg"},
    "salas.html": {"title": "Salas", "desc": "Móveis elegantes e confortáveis para a sua sala de estar.", "img": "images/Lourini-Chiado.jpg"},
    "cozinha.html": {"title": "Cozinhas", "desc": "Móveis de cozinha que combinam praticidade com estilo.", "img": "images/Lourini-Viena.jpg"},
    "conjuntos.html": {"title": "Conjuntos & Packs", "desc": "Tudo desenhado para combinar na perfeição, com entrega e montagem gratuita!", "img": "https://lourini.pt/app/uploads/2024/09/amazonia-canto-sala-1200x1200.webp"},
    "colchoes.html": {"title": "Colchões", "desc": "Explore a nossa seleção de descanso de excelência.", "img": "https://lourini.pt/app/uploads/2024/04/colchao-greysoft-sleep-1200x1200.webp"},
    "kids.html": {"title": "Kids & Bebé", "desc": "Quartos mágicos para os mais pequenos.", "img": "https://lourini.pt/app/uploads/2024/07/quarto-juvenil-1200x1200.png"},
    "escritorio.html": {"title": "Escritório", "desc": "Espaços de trabalho inspiradores e produtivos.", "img": "https://lourini.pt/app/uploads/2024/09/escritorio-nizza-1200x1200.png"},
    "complementos.html": {"title": "Complementos", "desc": "O toque final à sua decoração.", "img": "images/Lourini-Madrid.jpg"}
}

for filepath, data in pages.items():
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_hero = f"""  <!-- Slim Hero -->
  <section class="relative h-56 md:h-64 bg-gray-200 mt-20">
    <div class="absolute inset-0 bg-cover" style="background-image: url('{data['img']}'); background-position: center center;"></div>
    <div class="absolute inset-0 bg-black/60"></div>
    <div class="relative container mx-auto px-4 h-full flex flex-col justify-center items-center text-center text-white">
      <h1 class="text-4xl md:text-6xl font-light mb-2 tracking-widest uppercase">{data['title']}</h1>
      <p class="text-lg text-white/90 font-light max-w-2xl mx-auto">{data['desc']}</p>
    </div>
  </section>"""
        
        # Replace the minimalist hero
        pattern = r'<!-- Minimalist Hero -->.*?<!-- Subcategories Section -->'
        
        if "Minimalist Hero" in content:
            content = re.sub(r'<!-- Minimalist Hero -->.*?</section>', new_hero, content, flags=re.DOTALL)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath} to slim image hero.")
        else:
            print(f"{filepath} does not have Minimalist Hero.")
            
    except Exception as e:
        print(f"Error {filepath}: {e}")
