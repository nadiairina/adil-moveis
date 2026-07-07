import os

# Filter tecidos list to keep only the ones that have "amostras" in their name
tecidos_dir = "images/tecidos"
fabric_swatches = [f for f in sorted(os.listdir(tecidos_dir)) if "amostras" in f and f.endswith(".jpg")]

print(f"Found {len(fabric_swatches)} actual swatch files (no info cards)")

with open('tecidos.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Locate top and bottom boundaries
header_marker = '</header>'
header_idx = html_content.find(header_marker)
if header_idx != -1:
    replace_start = header_idx + len(header_marker)
else:
    replace_start = -1

replace_end = html_content.rfind('style="background-color:#F5F0E8; border-top:1px solid #E8E3DC;')
if replace_end == -1:
    replace_end = html_content.rfind("<footer")

if replace_start != -1 and replace_end != -1 and replace_start < replace_end:
    # 1. Page Header (solid minimalist Zara Style)
    header_html = """
    <main class="bg-[#FDFCFA]">
      <!-- Minimalist Page Header (Zara Home Style) -->
      <section style="background-color:#F5F0E8; border-bottom:1px solid #E8E3DC; padding:4.5rem 0; text-align:center;">
        <div style="max-width:800px; margin:0 auto; padding:0 1.5rem;">
          <h1 style="font-family:'Playfair Display',serif; font-size:clamp(2rem,4vw,3.25rem); font-weight:400; color:#1a1a1a; letter-spacing:0.05em; margin-bottom:1rem; text-transform:uppercase;">Guia de Tecidos</h1>
          <p style="font-family:'Inter',sans-serif; font-size:0.9rem; color:#6b6b6b; line-height:1.7; max-width:620px; margin:0 auto; font-weight:300;">
            Conheça as nossas texturas, malhas e tons exclusivos. Personalize o seu sofá, cadeiras ou sommiers com qualquer amostra abaixo.
          </p>
        </div>
      </section>
    """
    
    # 2. Grid of swatches only
    grid_html = """
      <!-- Swatches Grid Section -->
      <section style="background:#FDFCFA; padding:5rem 0;">
        <div class="container mx-auto px-4" style="max-width:1200px;">
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">"""
          
    fabric_types = [
        ("Veludo Concept", "Toque extremamente macio, brilho discreto e alta densidade. Ideal para sofás de luxo e cabeceiras."),
        ("Linho Rústico Natura", "Fibras naturais entrelaçadas, aspeto orgânico e altamente respirável. Clássico e intemporal."),
        ("Microfibra Protect", "Tratamento anti-mancha e repelente a líquidos. Alta durabilidade, ideal para casas com animais."),
        ("Chenille Comfort", "Textura rica em relevo, toque acolhedor e resistente ao desgaste diário. Conforto tradicional."),
        ("Pele Sintética Nobre", "Visual clássico e elegante, de fácil limpeza e manutenção. Elevada resistência a riscos."),
        ("Lona Algodão Slim", "Aspeito mate, toque suave e natural. Uma escolha moderna, minimalista e muito resistente.")
    ]
    
    for idx, filename in enumerate(fabric_swatches):
        filepath_img = f"images/tecidos/{filename}"
        name, desc = fabric_types[idx % len(fabric_types)]
        fabric_number = idx + 1
        name_display = f"{name} — Amostra {fabric_number:02d}"
        
        grid_html += f"""
            <!-- Fabric Card -->
            <div style="background:#EDF4F8; border:1px solid #E8E3DC; border-radius:4px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 4px 15px rgba(0,0,0,0.02); transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-4px)';" onmouseout="this.style.transform='translateY(0)';" data-aos="fade-up">
              <div style="position:relative; padding-top:100%; overflow:hidden; background:#F7F4F0; border-bottom:1px solid #E8E3DC;">
                <img src="{filepath_img}" alt="{name_display}" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 hover:scale-105" />
              </div>
              <div style="padding:1.5rem; text-align:center; display:flex; flex-direction:column; flex:1; justify-content:space-between;">
                <div>
                  <h3 style="font-family:'Inter',sans-serif; font-size:12px; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; color:#1a1a1a; margin-bottom:8px;">{name_display}</h3>
                  <p style="font-family:'Inter',sans-serif; font-size:11px; color:#6b6b6b; line-height:1.6; margin:0 0 1rem 0; font-weight:300;">{desc}</p>
                </div>
                <div style="font-family:'Inter',sans-serif; font-size:9px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#C8B598; border-top:1px solid #E8E3DC; padding-top:10px; margin-top:auto;">
                  Disponível em Loja
                </div>
              </div>
            </div>"""
            
    grid_html += """
          </div>
        </div>
      </section>
    """
    
    new_content = html_content[:replace_start] + "\n" + header_html + "\n" + grid_html + "\n      " + html_content[replace_end:]
    
    with open('tecidos.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✓ Successfully rebuilt tecidos.html with ONLY swatches sheets (no info cards)")
else:
    print("✗ Failed to locate boundaries for tecidos.html")
