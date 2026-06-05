import os
import re
import glob

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def get_price(name, filename):
    name_lower = name.lower()
    file_lower = filename.lower()
    
    # Check cushions/pillows/bedding
    if any(k in name_lower for k in ["almofada", "resguardo", "edredão", "edredao"]):
        return "39.00"
        
    # Check tables/chairs/hangers
    if any(k in name_lower for k in ["mesa", "cadeira", "banco", "cabide"]):
        return "89.00"
        
    # Check chests/comodas/shoe racks
    if any(k in name_lower for k in ["cómoda", "comoda", "camiseiro", "sapateira", "bengaleiro", "secretária", "secretaria"]):
        return "149.00"
        
    # Check mattresses/sommiers
    if any(k in name_lower for k in ["colchão", "colchao", "sommier", "colchões"]):
        return "299.00"
        
    # Check beds/wardrobes/sofas/major sets
    if any(k in name_lower for k in ["cama", "roupeiro", "quarto", "sofa", "sofá", "bona", "amazonia", "sala"]):
        return "399.00"
        
    # File-based defaults if name doesn't match
    if "colchoes" in file_lower:
        return "299.00"
    if "quartos" in file_lower or "salas" in file_lower:
        return "399.00"
    if "escritorio" in file_lower or "complementos" in file_lower:
        return "149.00"
        
    return "199.00"

target_files = ["quartos.html", "colchoes.html", "salas.html", "escritorio.html", "cozinha.html", "complementos.html", "kids.html"]

for filepath in target_files:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Let's check if the file is already processed
    if "snipcart-add-item" in content:
        print(f"Skipping {filepath} (already contains snipcart buttons)")
        continue
        
    # Match the product footer block:
    # <div class="py-4 text-center">
    #   <h3 class="text-lg font-medium">...</h3>
    # </div>
    pattern = re.compile(
        r'(<div class="py-4 text-center">)\s*<h3 class="text-lg font-medium">([^<]+)</h3>\s*(</div>)',
        re.MULTILINE
    )
    
    def replacer(match):
        h3_class = 'text-lg font-medium mb-3'
        name = match.group(2).strip()
        item_id = slugify(name)
        price_str = get_price(name, filepath)
        price_val = float(price_str)
        price_display = f"{int(price_val)}€"
        
        replacement = f'''<div class="py-4 text-center flex flex-col items-center justify-between h-full">
          <h3 class="{h3_class}">{name}</h3>
          <button class="snipcart-add-item bg-black text-white px-4 py-2 text-xs font-semibold uppercase tracking-wider hover:bg-gray-800 transition-colors mt-auto mb-2"
            data-item-id="{item_id}"
            data-item-name="{name}"
            data-item-price="{price_str}"
            data-item-url="{filepath}"
            data-item-description="Mobiliário de alta qualidade. Cores, acabamentos e medidas personalizáveis após a encomenda.">
            Adicionar — {price_display}
          </button>
        </div>'''
        return replacement

    new_content, count = pattern.subn(replacer, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched {filepath} (added {count} snipcart buttons)")
    else:
        print(f"No product footer matches found in {filepath}")

print("Done processing products!")
