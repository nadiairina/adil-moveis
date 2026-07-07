import re

fabrics = [
    {
        "name": "Primo", "class": "A", "desc": "Water Repellent",
        "comp": "100% PES", "weight": "330g/m²", "resistance": "≥35.000 Ciclos", "care": "Water Repellent, fácil limpeza.",
        "ids": ["6383", "6384", "6385"]
    },
    {
        "name": "Guilty", "class": "A", "desc": "Resistente a cigarros, Easy Clean",
        "comp": "100% PES", "weight": "-", "resistance": "-", "care": "Fácil limpeza.",
        "ids": ["6387", "6386", "6388"]
    },
    {
        "name": "Barrel", "class": "A", "desc": "Pet Friendly, Resistente a cigarros",
        "comp": "100% Poliéster", "weight": "270g/m²", "resistance": "45-55k Ciclos", "care": "Easy Clean",
        "ids": ["6389", "6390", "6391"]
    },
    {
        "name": "Terra", "class": "B", "desc": "Water Repellent, Pet Friendly",
        "comp": "100% Poliéster", "weight": "330g/m²", "resistance": "≥35.000 Ciclos", "care": "Water Repellent",
        "ids": ["6392", "6393", "6394"]
    },
    {
        "name": "Letto", "class": "B", "desc": "Easy Clean, Pet Friendly",
        "comp": "100% PES", "weight": "380g/m²", "resistance": "90-100k Ciclos", "care": "Easy Clean",
        "ids": ["6395", "6396", "6397"]
    },
    {
        "name": "Selena", "class": "B", "desc": "Instalimp Treatment",
        "comp": "100% PES", "weight": "360g/m²", "resistance": ">30.000 Ciclos", "care": "Instalimp®",
        "ids": ["6398", "6399", "6400"]
    },
    {
        "name": "Idris", "class": "B", "desc": "Resistente a cigarros, Easy Clean",
        "comp": "100% Poliéster", "weight": "325g/m²", "resistance": "40.000 Ciclos", "care": "Anti-Stain",
        "ids": ["6401", "6402", "6403"]
    },
    {
        "name": "Diosa", "class": "B", "desc": "Pet Friendly, Easy Clean",
        "comp": "100% PES", "weight": "350g/m²", "resistance": "60-70k Ciclos", "care": "Easy Clean",
        "ids": ["6404", "6405", "6406"]
    },
    {
        "name": "Sintra", "class": "B", "desc": "Water Repellent, Resistente a cigarros",
        "comp": "100% Poliéster", "weight": "427g/m²", "resistance": ">50.000 Ciclos", "care": "Water Repellent",
        "ids": ["6407", "6408", "6409"]
    },
    {
        "name": "Denver", "class": "C", "desc": "Chenille de alta qualidade",
        "comp": "100% Poliéster", "weight": "414g/m²", "resistance": ">50.000 Ciclos", "care": "Limpeza profissional",
        "ids": ["6410", "6411", "6412"]
    },
    {
        "name": "Logan", "class": "A", "desc": "Resistente a cigarros, Veludo",
        "comp": "100% Poliéster", "weight": "329g/m²", "resistance": ">60.000 Ciclos", "care": "Lavar a 30°",
        "ids": ["6413", "6414", "6415"]
    }
]

html_blocks = []
html_blocks.append('<!-- Circular Swatch Grid Section -->\n<section style="background:#FDFCFA; padding:5rem 0;">\n  <div class="container mx-auto px-4" style="max-width:1100px;">\n    <div style="display:flex; flex-direction:column; gap:4rem;">')

for f in fabrics:
    cover_id = f['ids'][0]
    crop_id = f['ids'][1]
    tech_id = f['ids'][2]
    
    import os
    img_dir = '/Users/nadiairina/Desktop/adil móveis/adil-moveis/images/tecidos'
    all_imgs = os.listdir(img_dir)
    
    crop_img = next((i for i in all_imgs if crop_id in i and 'crop' in i), f"tecido_crop_{crop_id}.jpg")
    cover_img = next((i for i in all_imgs if cover_id in i and 'capa' in i), f"tecido_capa_{cover_id}.jpg")
    tech_img = next((i for i in all_imgs if tech_id in i and ('capa' in i or 'amostras' in i)), f"tecido_capa_{tech_id}.jpg")
    
    if f['name'] == 'Guilty':
        crop_img = "tecido_crop_6388.jpg"
        cover_img = "tecido_capa_6387.jpg"
        tech_img = "tecido_amostras_6386.jpg"

    card = f"""
      <div style="background:#EDF4F8; border:1px solid #E8E3DC; border-radius:8px; padding:2rem; display:flex; flex-direction:column; md:flex-row; align-items:start; gap:2rem; box-shadow:0 4px 15px rgba(0,0,0,0.02); transition:transform 0.3s;" data-aos="fade-up">
        <!-- Swatch Circle -->
        <div style="width:160px; height:160px; border-radius:50%; overflow:hidden; border:4px solid #fff; box-shadow:0 4px 12px rgba(0,0,0,0.08); flex-shrink:0; position:relative; background:#F7F4F0; align-self:center; md:align-self:start;">
          <img src="images/tecidos/{crop_img}" alt="{f['name']}" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transform:scale(1.5);" />
        </div>
        
        <!-- Fabric Info Panel -->
        <div style="flex:1; display:flex; flex-direction:column; gap:0.5rem; text-align:left; width:100%;">
          <span style="font-family:'Inter',sans-serif; font-size:9px; font-weight:700; color:#C8B598; letter-spacing:0.15em; text-transform:uppercase;">Classe {f['class']}</span>
          <h3 style="font-family:'Playfair Display',serif; font-size:1.45rem; font-weight:400; color:#1a1a1a; margin:0 0 0.5rem 0;">{f['name']}</h3>
          <p style="font-family:'Inter',sans-serif; font-size:0.85rem; color:#6b6b6b; line-height:1.6; font-weight:300; margin:0 0 0.75rem 0;">{f['desc']}</p>
          
          <div style="display:grid; grid-template-columns:1fr; sm:grid-template-columns:repeat(3,1fr); gap:1rem; border-top:1px solid #D4E4EE; padding-top:1rem; margin-top:auto; margin-bottom:1.5rem;">
            <div>
              <h4 style="font-family:'Inter',sans-serif; font-size:9px; font-weight:700; text-transform:uppercase; color:#C8B598; margin-bottom:2px; letter-spacing:0.1em;">Composição</h4>
              <p style="font-family:'Inter',sans-serif; font-size:11px; color:#1a1a1a; margin:0; font-weight:400;">{f['comp']}</p>
            </div>
            <div>
              <h4 style="font-family:'Inter',sans-serif; font-size:9px; font-weight:700; text-transform:uppercase; color:#C8B598; margin-bottom:2px; letter-spacing:0.1em;">Gramagem / Resistência</h4>
              <p style="font-family:'Inter',sans-serif; font-size:11px; color:#1a1a1a; margin:0; font-weight:400;">{f['weight']} | {f['resistance']}</p>
            </div>
            <div>
              <h4 style="font-family:'Inter',sans-serif; font-size:9px; font-weight:700; text-transform:uppercase; color:#C8B598; margin-bottom:2px; letter-spacing:0.1em;">Instruções</h4>
              <p style="font-family:'Inter',sans-serif; font-size:11px; color:#1a1a1a; margin:0; font-weight:400;">{f['care']}</p>
            </div>
          </div>
          
          <div style="display:flex; flex-direction:column; gap:1rem; width:100%; border-top:1px solid #D4E4EE; padding-top:1.5rem;">
            <img src="images/tecidos/{cover_img}" style="width:100%; max-width:600px; border-radius:4px; box-shadow:0 2px 8px rgba(0,0,0,0.05); align-self:center;" alt="Catálogo {f['name']}">
            <img src="images/tecidos/{tech_img}" style="width:100%; max-width:600px; border-radius:4px; box-shadow:0 2px 8px rgba(0,0,0,0.05); align-self:center;" alt="Ficha Técnica {f['name']}">
          </div>

        </div>
      </div>
    """
    html_blocks.append(card)

html_blocks.append('    </div>\n  </div>\n</section>')
new_section = "\n".join(html_blocks)

with open('/Users/nadiairina/Desktop/adil móveis/adil-moveis/tecidos.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<!-- Circular Swatch Grid Section -->')
end_idx = content.find('</main>')

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_section + "\n\n      " + content[end_idx:]
    with open('/Users/nadiairina/Desktop/adil móveis/adil-moveis/tecidos.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Tecidos fixed!")
else:
    print("Could not find sections!")

