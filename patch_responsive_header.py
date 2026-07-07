import glob

TARGET = """          <div class="flex items-center space-x-6 text-sm">
            <a href="mailto:adil.moveis@hotmail.com" class="flex items-center hover:text-gray-300">
              <i data-feather="mail" class="w-4 h-4 mr-3"></i> adil.moveis@hotmail.com
            </a>
            <a href="tel:212582788" class="flex items-center hover:text-gray-300">
              <i data-feather="phone" class="w-4 h-4 mr-3"></i> 212 582 788
            </a>
            <!-- Snipcart Button -->
            <button class="snipcart-checkout flex items-center font-bold bg-white text-black px-4 py-1 rounded shadow hover:bg-gray-200 transition-colors">
              <i data-feather="shopping-cart" class="w-4 h-4 mr-2"></i>
              <span class="snipcart-total-price">0.00€</span>
            </button>
          </div>"""

REPLACEMENT = """          <div class="flex items-center space-x-6 text-sm">
            <a href="mailto:adil.moveis@hotmail.com" class="flex items-center hover:text-gray-300" title="Enviar Email">
              <i data-feather="mail" class="w-4 h-4 mr-1 md:mr-3"></i><span class="hidden md:inline">adil.moveis@hotmail.com</span>
            </a>
            <a href="tel:212582788" class="flex items-center hover:text-gray-300" title="Ligar para Loja">
              <i data-feather="phone" class="w-4 h-4 mr-1 md:mr-3"></i><span class="hidden md:inline">212 582 788</span>
            </a>
            <!-- Snipcart Button -->
            <button class="snipcart-checkout flex items-center font-bold bg-white text-black px-4 py-1 rounded shadow hover:bg-gray-200 transition-colors" title="Ver Carrinho">
              <i data-feather="shopping-cart" class="w-4 h-4 mr-2"></i>
              <span class="snipcart-total-price">0.00€</span>
            </button>
          </div>"""

files_patched = 0
for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if TARGET in content:
        content = content.replace(TARGET, REPLACEMENT)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched header in {filepath}")
        files_patched += 1

print(f"Total files patched: {files_patched}")
