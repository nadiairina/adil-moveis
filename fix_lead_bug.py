import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # REMOVE fbq lead from view_item arrays
    broken_block1 = """              item_category: 'Packs Especiais'
            
            if (typeof fbq === 'function') fbq('track', 'Lead');
          }]"""
    fixed_block1 = """              item_category: 'Packs Especiais'
            }]"""
    content = content.replace(broken_block1, fixed_block1)

    broken_block2 = """              item_category: window_products[productId].category
            
            if (typeof fbq === 'function') fbq('track', 'Lead');
          }]"""
    fixed_block2 = """              item_category: window_products[productId].category
            }]"""
    content = content.replace(broken_block2, fixed_block2)

    # Make sure we didn't inject it in page_view
    content = content.replace("'page_location': window.location.href\n              \n            if (typeof fbq === 'function') fbq('track', 'Lead');\n          });", "'page_location': window.location.href\n            });")


    # NOW properly inject fbq lead ONLY on the WhatsApp button click event
    if filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
        click_event_block = """          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
            if (typeof gtag === 'function') {
              var pName = document.getElementById('dynamic-title') ? document.getElementById('dynamic-title').textContent : 'Produto';
              gtag('event', 'click_whatsapp_pdp', {
                'event_category': 'contacto_produto',
                'event_label': pName
              });
            }
          });"""
        
        fixed_click_event_block = """          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
            if (typeof gtag === 'function') {
              var pName = document.getElementById('dynamic-title') ? document.getElementById('dynamic-title').textContent : 'Produto';
              gtag('event', 'click_whatsapp_pdp', {
                'event_category': 'contacto_produto',
                'event_label': pName
              });
            }
            if (typeof fbq === 'function') fbq('track', 'Lead');
          });"""
        
        # also handle the pack-detalhe 'Pack' fallback name
        click_event_block_pack = click_event_block.replace("'Produto'", "'Pack'")
        fixed_click_event_block_pack = fixed_click_event_block.replace("'Produto'", "'Pack'")
        
        content = content.replace(click_event_block, fixed_click_event_block)
        content = content.replace(click_event_block_pack, fixed_click_event_block_pack)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed the false Lead tracking bug.")
