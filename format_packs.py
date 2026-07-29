import re

with open('packs.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find all the packs and replace their wrapper
def replace_pack(match):
    pack_inner = match.group(0)
    
    # Extract data-category
    cat_match = re.search(r'data-category="([^"]+)"', pack_inner)
    category = cat_match.group(1) if cat_match else "sala"
    
    # Extract image src and alt
    img_match = re.search(r'<img src="([^"]+)" alt="([^"]+)"', pack_inner)
    img_src = img_match.group(1) if img_match else "images/sem-imagem.svg"
    img_alt = img_match.group(2) if img_match else "Pack"
    
    # Extract ref
    ref_match = re.search(r'Ref: ([^<]+)</span>', pack_inner)
    ref_id = ref_match.group(1) if ref_match else "pack-X"
    
    # Extract title
    title_match = re.search(r'<h2[^>]*>([^<]+)</h2>', pack_inner)
    title = title_match.group(1) if title_match else "Pack Title"
    
    # Extract description
    desc_match = re.search(r'<p style="font-family:\'Inter\',sans-serif; font-size:0.9rem; color:#6b6b6b; line-height:1.6; margin-bottom:1.5rem;">([\s\S]*?)</p>', pack_inner)
    desc = desc_match.group(1).strip() if desc_match else "Descrição"
    
    # Extract list items
    list_items = re.findall(r'<li>(.*?)</li>', pack_inner)
    list_html = "\n".join([f'                      <li style="display:flex; align-items:flex-start; gap:8px;"><span style="color:#C8B598; font-weight:bold;">✓</span> <span>{li.replace("✔ ", "").strip()}</span></li>' for li in list_items])
    
    # Extract price
    price_match = re.search(r'<span[^>]*>(Sob Consulta|[\d,€\s]+)</span>', pack_inner)
    price = price_match.group(1) if price_match else "Sob Consulta"
    
    new_html = f"""<div class="product flex flex-col bg-white border border-[#E8E3DC] rounded-xl overflow-hidden hover:shadow-2xl transition-all duration-700 hover:-translate-y-2" data-category="{category}">
              <a href="produto-detalhe.html?id={ref_id}" class="block relative w-full group overflow-hidden" style="padding-top:45%; background:#F7F4F0;">
                <img src="{img_src}" alt="{img_alt}" class="absolute inset-0 w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" />
                <div style="position:absolute; top:20px; left:20px; background:#C8B598; color:#fff; font-size:10px; font-weight:800; letter-spacing:0.15em; text-transform:uppercase; padding:6px 16px; border-radius:30px; z-index:2; box-shadow:0 4px 10px rgba(0,0,0,0.1);">CAMPANHA</div>
                <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-10 transition-all duration-500"></div>
              </a>
              <div class="p-8 md:p-12 flex flex-col md:flex-row gap-8 md:gap-12">
                <div class="md:w-2/3">
                  <span style="font-size:10px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#C8B598; margin-bottom:0.75rem; display:block;">Ref: {ref_id}</span>
                  <h2 style="font-family:'Playfair Display',serif; font-size:clamp(1.75rem,3vw,2.5rem); font-weight:400; color:#1a1a1a; margin-bottom:1.25rem; line-height:1.2;">{title}</h2>
                  <p style="font-family:'Inter',sans-serif; font-size:1rem; color:#6b6b6b; line-height:1.7; margin-bottom:0;">
                    {desc}
                  </p>
                </div>
                <div class="md:w-1/3 flex flex-col justify-between border-t md:border-t-0 md:border-l border-[#E8E3DC] pt-6 md:pt-0 md:pl-10">
                  <div>
                    <h4 style="font-size:10px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#1a1a1a; margin-bottom:1rem;">O que está incluído:</h4>
                    <ul style="font-size:0.9rem; color:#6b6b6b; list-style-type:none; padding-left:0; margin:0; line-height:1.6;" class="space-y-2">
{list_html}
                    </ul>
                  </div>
                  <div class="mt-8 pt-6 border-t border-[#E8E3DC] flex flex-col gap-4">
                    <span style="font-size:1.5rem; font-weight:600; color:#C8B598;">{price}</span>
                    <a href="produto-detalhe.html?id={ref_id}" style="text-align:center; background:#1a1a1a; color:#fff; font-size:10px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; padding:16px 24px; text-decoration:none; border-radius:4px; transition:all 0.3s;" onmouseover="this.style.background='#333'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='#1a1a1a'; this.style.transform='translateY(0)';">Explorar Opções →</a>
                  </div>
                </div>
              </div>
            </div>"""
    return new_html

# We need to replace all `<div class="product ..."> ... </div>` (up to the next pack)
# It's better to just use a regular expression that captures the whole pack block.
# Assuming each pack block ends before `<!-- Pack` or `</div>` for space-y-16
pattern = re.compile(r'<div class="product flex flex-col md:flex-row[^"]*" data-category="[^"]*">.*?</a>\s*</div>\s*</div>\s*</div>', re.DOTALL)

def replace_all(content):
    # Actually, the regex above might be tricky since the structure changed slightly. Let's do it simply:
    # Split by `<!-- Pack `
    parts = content.split('<!-- Pack ')
    new_parts = [parts[0]]
    
    for part in parts[1:]:
        if 'class="product' in part:
            # part contains a pack. Let's extract the number/name and then the HTML
            num_name = part.split('-->')[0]
            html = part.split('-->', 1)[1]
            
            # extract the product div
            product_match = re.search(r'<div class="product.*?</p>\s*</div>\s*</a>\s*</div>\s*</div>\s*</div>', html, re.DOTALL)
            # Wait, the structure in the file ends with:
            # </a>\n                </div>\n              </div>\n            </div>
            if not product_match:
                product_match = re.search(r'<div class="product.*?(?:<a href="produto-detalhe.html[^>]*>.*?</a>\s*</div>\s*</div>\s*</div>)', html, re.DOTALL)
            
            if product_match:
                new_html = replace_pack(product_match)
                part = f"{num_name}-->\n            " + html.replace(product_match.group(0), new_html)
            
            new_parts.append(part)
        else:
            new_parts.append(part)
            
    return '<!-- Pack '.join(new_parts)

new_content = replace_all(content)

with open('packs.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done replacing packs layout.")
