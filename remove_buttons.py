import os
import re

html_files = ["quartos.html", "salas.html", "cozinha.html", "colchoes.html", "kids.html", "escritorio.html", "complementos.html", "conjuntos.html"]

for file in html_files:
    if not os.path.exists(file): continue
    with open(file, "r") as f:
        content = f.read()
    
    # Pattern to match the specific "Ver Detalhes" button we generated
    pattern = r'\s*<a href="produto-detalhe\.html\?id=[^"]+" class="mt-auto[^>]+>\s*<i[^>]+></i>\s*Ver Detalhes\s*</a>'
    new_content = re.sub(pattern, '', content)
    
    with open(file, "w") as f:
        f.write(new_content)
        
print("Removed 'Ver Detalhes' buttons.")
