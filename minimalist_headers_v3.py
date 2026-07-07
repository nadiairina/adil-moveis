import glob
import re

pages = {
    "quartos.html": {"title": "Quartos", "desc": "Crie o quarto dos seus sonhos com a nossa coleção de mobiliário elegante e funcional. Personalize cores, medidas e acabamentos para o seu espaço perfeito."},
    "salas.html": {"title": "Salas", "desc": "Móveis elegantes e confortáveis para a sua sala de estar e jantar. Personalize cores, medidas e estofos para que encaixem perfeitamente na sua casa."},
    "cozinha.html": {"title": "Cozinhas", "desc": "Soluções funcionais e elegantes para o coração da sua casa. Móveis de cozinha que combinam praticidade com estilo."},
    "conjuntos.html": {"title": "Conjuntos & Packs", "desc": "Compre os nossos conjuntos pré-selecionados e poupe. Tudo desenhado para combinar na perfeição, com entrega e montagem gratuita!"},
    "complementos.html": {"title": "Complementos", "desc": "Descubra a nossa gama de complementos que darão o toque final à sua decoração."}
}

for filepath, data in pages.items():
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_hero = f"""  <!-- Minimalist Hero -->
  <section class="py-24 md:py-32 bg-[#FDFBF7] flex flex-col items-center justify-center text-center px-4 border-b border-[#EAE6DF] mt-20">
    <div data-aos="fade-up" data-aos-duration="1000">
      <h1 class="text-black text-5xl md:text-7xl font-light tracking-widest mb-6 uppercase">{data["title"]}</h1>
      <p class="text-gray-500 text-lg md:text-xl font-light max-w-2xl mx-auto">{data["desc"]}</p>
    </div>
  </section>"""
        
        # In these older category pages, the hero is enclosed between 
        # <!-- Hero Section with Logo and Menu Button --> (or similar)
        # and <!-- Subcategories Section --> or <!-- Filters --> or <section class="py-12
        
        # Let's match from <!-- Hero Section with Logo and Menu Button --> up to the next <section> which is usually the filters.
        # It's safer to just find the <section> that contains the background image and title, and replace it.
        # A good pattern: `<!-- Hero Section with Logo and Menu Button -->\s*<section.*?</section>\s*(?:<section.*?</section>)?`
        # Because there might be two sections (one outer, one inner like in quartos.html)
        
        pattern = r'<!-- Hero Section with Logo and Menu Button -->.*?<!-- Subcategories Section -->'
        
        if "Minimalist Hero" not in content:
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, new_hero + "\n\n<!-- Subcategories Section -->", content, flags=re.DOTALL)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {filepath} using Subcategories Section pattern.")
            else:
                # If Subcategories Section doesn't exist, maybe it's just before <section class="py-16
                pattern2 = r'<!-- Hero Section with Logo and Menu Button -->.*?(?=<section class="py-16)'
                if re.search(pattern2, content, re.DOTALL):
                    content = re.sub(pattern2, new_hero + "\n\n", content, flags=re.DOTALL)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated {filepath} using py-16 pattern.")
                else:
                    print(f"FAILED to match patterns in {filepath}")
        else:
            print(f"{filepath} already has Minimalist Hero.")
            
    except Exception as e:
        print(f"Error {filepath}: {e}")
