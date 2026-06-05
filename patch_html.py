import os
import glob

# The changes we want to make
HEAD_ADD = """    <link rel="preconnect" href="https://app.snipcart.com" />
    <link rel="preconnect" href="https://cdn.snipcart.com" />
    <link rel="stylesheet" href="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.css" />"""

NAV_TARGET = """            <a href="tel:212582788" class="flex items-center hover:text-gray-300">
              <i data-feather="phone" class="w-4 h-4 mr-3"></i> 212 582 788
            </a>
          </div>"""

NAV_REPLACE = """            <a href="tel:212582788" class="flex items-center hover:text-gray-300">
              <i data-feather="phone" class="w-4 h-4 mr-3"></i> 212 582 788
            </a>
            <!-- Snipcart Button -->
            <button class="snipcart-checkout flex items-center font-bold bg-white text-black px-4 py-1 rounded shadow hover:bg-gray-200 transition-colors">
              <i data-feather="shopping-cart" class="w-4 h-4 mr-2"></i>
              <span class="snipcart-total-price">0.00€</span>
            </button>
          </div>"""

BODY_END_ADD = """    <!-- Snipcart Configuration -->
    <script async src="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js"></script>
    <div id="snipcart" data-api-key="ODE4MjNlYWYtZGViOS00OGY3LWJhZWEtODU1OTE5OTYzMzQxNjM5MTYyMDI2OTM2NjA0MTY3" hidden></div>
  </body>"""

for filepath in glob.glob("*.html"):
    if filepath == "index.html":
        continue # Already patched
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Check if already patched to avoid double patching
    if "app.snipcart.com" in content:
        continue
        
    # 1. Patch Head
    content = content.replace('    <script src="https://unpkg.com/feather-icons"></script>\n  </head>', f'{HEAD_ADD}\n    <script src="https://unpkg.com/feather-icons"></script>\n  </head>')
    
    # 2. Patch Nav
    content = content.replace(NAV_TARGET, NAV_REPLACE)
    
    # 3. Patch Body End
    content = content.replace('  </body>', f'\n{BODY_END_ADD}')
    
    with open(filepath, 'w') as f:
        f.write(content)

print("All HTML files patched!")
