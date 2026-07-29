import re
import glob
from bs4 import BeautifulSoup

def process_file(filepath, category_filter):
    with open(filepath, 'r') as f:
        html = f.read()
    
    # We want to replace the content of the div with class "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8"
    soup = BeautifulSoup(html, 'html.parser')
    grid = soup.find('div', class_='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8')
    if not grid:
        # Fallback for kids.html which might not have the exact class
        grid = soup.find('div', class_=lambda x: x and 'grid' in x and 'gap-8' in x)
        if not grid:
            print(f"Could not find grid in {filepath}")
            return
            
    # Clear the grid and add an ID
    grid.clear()
    grid['id'] = 'products-grid'
    
    # We also need to inject products.js and script to render
    # Find the end of body
    body = soup.find('body')
    
    script_html = f"""
    <script src="products.js"></script>
    <script>
      document.addEventListener('DOMContentLoaded', () => {{
        const grid = document.getElementById('products-grid');
        if(!grid) return;
        
        let html = '';
        for (const key in window_products) {{
          const p = window_products[key];
          if ("{category_filter}" !== "all" && p.url !== "{category_filter}.html" && p.category !== "{category_filter}") continue;
          
          html += `
            <a href="produto-detalhe.html?id=${{p.id}}" class="product bg-white rounded overflow-hidden block border border-[#E8E3DC] hover:shadow-md transition-shadow relative" data-aos="fade-up" style="text-decoration:none; color:inherit;">
              <div class="relative w-full" style="aspect-ratio: 1 / 1; overflow:hidden; background:#F7F4F0;">
                <img src="${{p.image}}" alt="${{p.name}}" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 hover:scale-105" />
              </div>
              <div class="p-4 text-center" style="background:#FDFCFA; border-top:1px solid #E8E3DC;">
                <h3 style="font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:0.05em; text-transform:uppercase; color:#1a1a1a; margin-bottom:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{p.name}}</h3>
                <p style="font-family:'Inter',sans-serif; font-size:11px; margin:0;">
                  <span class="price-discounted" style="font-weight:600; color:#c8b598;">Preço Sob Consulta</span>
                </p>
              </div>
            </a>
          `;
        }}
        grid.innerHTML = html;
      }});
    </script>
    """
    
    # Append to body
    script_soup = BeautifulSoup(script_html, 'html.parser')
    body.append(script_soup)
    
    with open(filepath, 'w') as f:
        f.write(str(soup))
    print(f"Updated {filepath}")

process_file('quartos.html', 'Quartos')
process_file('salas.html', 'Salas')
process_file('kids.html', 'Quartos') # Kids are in quartos in our products.js

