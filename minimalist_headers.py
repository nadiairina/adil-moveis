import glob
import re

html_files = [
    "quartos.html", "salas.html", "cozinha.html", "colchoes.html", 
    "conjuntos.html", "kids.html", "escritorio.html", "complementos.html"
]

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We need to extract the title and paragraph from the old hero
        # Example: <h1 ...>QUARTOS</h1>
        # <p ...>Crie o quarto dos seus sonhos...</p>
        
        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
        p_match = re.search(r'<p class="text-white[^>]*>([^<]+)</p>', content)
        
        if title_match and p_match:
            title = title_match.group(1)
            desc = p_match.group(1)
            
            # Create the new minimalist hero
            new_hero = f"""  <!-- Minimalist Hero -->
  <section class="py-24 md:py-32 bg-[#FDFBF7] flex flex-col items-center justify-center text-center px-4 border-b border-[#EAE6DF] mt-20">
    <div data-aos="fade-up" data-aos-duration="1000">
      <h1 class="text-black text-5xl md:text-7xl font-light tracking-widest mb-6 uppercase">{title}</h1>
      <p class="text-gray-500 text-lg md:text-xl font-light max-w-2xl mx-auto">{desc}</p>
    </div>
  </section>"""
            
            # Replace the old hero block
            # The old hero block starts with `<!-- Hero -->` or `<section class="relative bg-black` 
            # and ends with `</section>` before `<!-- Filters -->` or similar.
            
            old_hero_pattern = r'(?:<!-- Hero -->\s*)?<section class="relative bg-black.*?</section>'
            
            content = re.sub(old_hero_pattern, new_hero, content, count=1, flags=re.DOTALL)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath} to minimalist header.")
        else:
            print(f"Could not find title/desc in {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
