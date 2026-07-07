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
            
        # Fix the broken product classes
        # The broken pattern looks like: class="product " data-aos="fade-up" bg-[#FDFBF7] rounded...
        # We want to put all the class names back inside the class="product ..." string.
        
        # In complementos.html: class="product " data-aos="fade-up" bg-[#FDFBF7] rounded shadow-sm overflow-hidden"
        content = content.replace(
            'class="product " data-aos="fade-up" bg-[#FDFBF7] rounded shadow-sm overflow-hidden"',
            'class="product bg-[#FDFBF7] rounded shadow-sm overflow-hidden" data-aos="fade-up"'
        )
        
        # In salas.html: class="product " data-aos="fade-up" bg-[#FDFBF7] rounded-lg shadow-sm border border-gray-100 overflow-hidden flex flex-col group"
        content = content.replace(
            'class="product " data-aos="fade-up" bg-[#FDFBF7] rounded-lg shadow-sm border border-gray-100 overflow-hidden flex flex-col group"',
            'class="product bg-[#FDFBF7] rounded-lg shadow-sm border border-gray-100 overflow-hidden flex flex-col group" data-aos="fade-up"'
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed classes in {filepath}")
        
    except Exception as e:
        print(f"Error {filepath}: {e}")
