import glob
import re

pages = {
    "quartos.html": {"title": "Quartos", "desc": "Crie o quarto dos seus sonhos com a nossa coleção de mobiliário elegante e funcional. Personalize cores, medidas e acabamentos para o seu espaço perfeito."},
    "salas.html": {"title": "Salas", "desc": "Móveis elegantes e confortáveis para a sua sala de estar e jantar. Personalize cores, medidas e estofos para que encaixem perfeitamente na sua casa."},
    "cozinha.html": {"title": "Cozinha", "desc": "Soluções funcionais e elegantes para o coração da sua casa. Móveis de cozinha que combinam praticidade com estilo."},
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
        
        old_hero_pattern = r'(?:<!-- Hero -->\s*)?<section class="relative bg-black.*?</section>'
        
        # In case the section didn't start exactly with relative bg-black, let's just find the first <section> inside <main> and replace it.
        # It's safer to use the pattern:
        content = re.sub(old_hero_pattern, new_hero, content, count=1, flags=re.DOTALL)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error {filepath}: {e}")
