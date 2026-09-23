import glob
import re

global_script = """
<!-- Global Event Tracking Scripts -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    // 1. WhatsApp / Contact Leads
    document.querySelectorAll('a[href*="wa.me"]').forEach(function(link) {
        if(!link.hasAttribute('data-tracked')) {
            link.addEventListener('click', function() {
                if(typeof fbq === 'function') fbq('track', 'Contact');
                if(typeof gtag === 'function') gtag('event', 'generate_lead', { event_category: 'whatsapp', event_label: link.innerText.trim() || 'WhatsApp Global' });
            });
            link.setAttribute('data-tracked', 'true');
        }
    });

    // 2. Google Maps / Find Location
    document.querySelectorAll('a[href*="maps.google.com"], a[href*="google.com/maps"]').forEach(function(link) {
        if(!link.hasAttribute('data-tracked')) {
            link.addEventListener('click', function() {
                if(typeof fbq === 'function') fbq('track', 'FindLocation');
                if(typeof gtag === 'function') gtag('event', 'click_maps', { event_category: 'loja', event_label: 'Google Maps Global' });
            });
            link.setAttribute('data-tracked', 'true');
        }
    });

    // 3. Formulários de Contacto
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            if(typeof fbq === 'function') fbq('track', 'Lead');
            if(typeof gtag === 'function') gtag('event', 'form_submit', { event_category: 'formulario', event_label: 'Formulario Global' });
        });
    });
});
</script>
</body>
"""

html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid injecting multiple times
    if "<!-- Global Event Tracking Scripts -->" in content:
        continue

    # Replace </body> with the script + </body>
    content = content.replace("</body>", global_script)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected global tracking into {filepath}")

# ViewContent explicitly in produto-detalhe.html
with open('produto-detalhe.html', 'r', encoding='utf-8') as f:
    pdp_content = f.read()

view_content_code = """
          // Evento Meta Pixel - ViewContent
          if (typeof fbq === 'function') {
            fbq('track', 'ViewContent', {
              content_name: p.name,
              content_category: p.category || 'Geral',
              content_ids: [productId],
              content_type: 'product',
              value: p.price > 0 ? p.price : 0.00,
              currency: 'EUR'
            });
          }
"""

# Insert right before gtag('event', 'page_view'
if "fbq('track', 'ViewContent'" not in pdp_content:
    pdp_content = pdp_content.replace("gtag('event', 'page_view', {", view_content_code + "\n          gtag('event', 'page_view', {")
    with open('produto-detalhe.html', 'w', encoding='utf-8') as f:
        f.write(pdp_content)
    print("Added ViewContent to produto-detalhe.html")

print("Tracking injection complete!")
