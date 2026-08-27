import os

filepath = 'pack-detalhe.html'
if not os.path.exists(filepath):
    print('File not found:', filepath)
    exit(1)

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update HTML heading title
old_heading = '<h2 style="font-family:\'Playfair Display\',serif;font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400;color:#1a1a1a;" data-aos="fade-up">Poderá gostar também</h2>'
new_heading = '<h2 style="font-family:\'Playfair Display\',serif;font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400;color:#1a1a1a;" data-aos="fade-up">Mais Packs Em Destaque</h2>'

if old_heading in html:
    html = html.replace(old_heading, new_heading)
    print('Updated heading to "Mais Packs Em Destaque"')
else:
    # Try finding with double quotes
    old_heading_double = '<h2 style="font-family:\'Playfair Display\',serif;font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400;color:#1a1a1a;\" data-aos=\"fade-up\">Poderá gostar também</h2>'
    if old_heading_double in html:
        html = html.replace(old_heading_double, new_heading)
        print('Updated heading (double quotes variant)')
    else:
        # Fallback search
        html = html.replace('Poderá gostar também</h2>', 'Mais Packs Em Destaque</h2>')
        print('Updated heading using fallback string replacement')

# 2. Update JavaScript logic
old_js_start = '// Related products'
old_js_end = '// Re-init feather for dynamically added icons'

start_idx = html.find(old_js_start)
end_idx = html.find(old_js_end)

if start_idx != -1 and end_idx != -1:
    new_js = r'''// Related packs (Mais Packs Em Destaque)
        var allPacks = Object.values(window.officialPacks);
        var related = allPacks.filter(function(pk) {
          return pk.id !== p.id;
        });
        
        if (related.length > 0) {
          document.getElementById('related-products-section').style.display = 'block';
          var grid = document.getElementById('related-products-grid');
          grid.innerHTML = '';
          related.forEach(function(pk) {
            var card = document.createElement('div');
            card.className = 'related-card';
            
            var imgHtml = (pk.image && pk.image !== 'images/logo_sem_fundo.png')
              ? '<img src="' + pk.image + '" alt="' + pk.name + '" style="width:100%;height:100%;object-fit:cover;transition:transform 0.5s ease;">'
              : '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;color:#ccc;background:#f7f4f0;font-size:12px;">Imagem brevemente</div>';

            card.innerHTML = '<a href="pack-detalhe.html?id=' + pk.id + '" style="text-decoration:none;display:block;">'
              + '<div class="img-wrap">' + imgHtml + '</div>'
              + '<div style="padding:1.25rem;">'
              + '<p style="font-size:9px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;color:#C8B598;margin-bottom:4px;">Packs Especiais</p>'
              + '<h3 style="font-family:\'Playfair Display\',serif;font-size:1.1rem;font-weight:400;color:#1a1a1a;margin-bottom:6px;line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' + pk.name + '</h3>'
              + '<p style="font-size:11px;font-weight:600;color:#c8b598;margin:0;">Preço Sob Consulta</p>'
              + '</div>'
              + '</a>';
            grid.appendChild(card);
          });
        }
        
        '''
    html = html[:start_idx] + new_js + html[end_idx:]
    print('Updated JavaScript related packs logic successfully!')
else:
    print('Error: Failed to locate JavaScript logic boundaries!')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
