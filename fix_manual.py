for filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. REMOVE the bad fbq from view_item
    broken1 = """              item_category: 'Packs Especiais'\n            \n            if (typeof fbq === 'function') fbq('track', 'Lead');\n          }]"""
    fixed1 = """              item_category: 'Packs Especiais'\n            }]"""
    content = content.replace(broken1, fixed1)

    broken2 = """              item_category: window_products[productId].category\n            \n            if (typeof fbq === 'function') fbq('track', 'Lead');\n          }]"""
    fixed2 = """              item_category: window_products[productId].category\n            }]"""
    content = content.replace(broken2, fixed2)

    # Make sure we didn't inject it in page_view
    content = content.replace("'page_location': window.location.href\n              \n            if (typeof fbq === 'function') fbq('track', 'Lead');\n          });", "'page_location': window.location.href\n            });")

    # 2. Add fbq to the button click properly
    # In pack-detalhe.html:
    broken_click_pack = """          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
            if (typeof gtag === 'function') {
              var pName = document.getElementById('dynamic-title') ? document.getElementById('dynamic-title').textContent : 'Pack';
              gtag('event', 'click_whatsapp_pack', {
                'event_category': 'contacto_pack',
                'event_label': pName,
                'page_location': window.location.href
              });
            }
          });"""
    fixed_click_pack = """          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
            if (typeof gtag === 'function') {
              var pName = document.getElementById('dynamic-title') ? document.getElementById('dynamic-title').textContent : 'Pack';
              gtag('event', 'click_whatsapp_pack', {
                'event_category': 'contacto_pack',
                'event_label': pName,
                'page_location': window.location.href
              });
            }
            if (typeof fbq === 'function') fbq('track', 'Lead');
          });"""
    content = content.replace(broken_click_pack, fixed_click_pack)

    # In produto-detalhe.html:
    broken_click_prod = """          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
            if (typeof gtag === 'function') {
              var pName = document.getElementById('dynamic-title') ? document.getElementById('dynamic-title').textContent : 'Produto';
              gtag('event', 'click_whatsapp_pdp', {
                'event_category': 'contacto_produto',
                'event_label': pName,
                'page_location': window.location.href
              });
            }
          });"""
    fixed_click_prod = """          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
            if (typeof gtag === 'function') {
              var pName = document.getElementById('dynamic-title') ? document.getElementById('dynamic-title').textContent : 'Produto';
              gtag('event', 'click_whatsapp_pdp', {
                'event_category': 'contacto_produto',
                'event_label': pName,
                'page_location': window.location.href
              });
            }
            if (typeof fbq === 'function') fbq('track', 'Lead');
          });"""
    content = content.replace(broken_click_prod, fixed_click_prod)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

