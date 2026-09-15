import os, glob, re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the standalone discount button
    discount_block = r'<!-- ══════════════════════════════════════════════════════\s*FLOATING DISCOUNT BUTTON & MODAL.*?</div>\s*<!--'
    content = re.sub(discount_block, '<!--', content, flags=re.DOTALL)
    # also try another pattern if the comment block is slightly different
    content = re.sub(r'<div id="discountFloatingBtnWrap".*?</div>', '', content, flags=re.DOTALL)

    # 2. Add the discount button inside floating-contact-bar
    old_bar = r'<div class="floating-contact-bar">(.*?)💬 Orçamento\s*</a>\s*</div>'
    new_bar = r'<div class="floating-contact-bar">\1💬 Orçamento\n      </a>\n      <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20receber%20o%20meu%20cup%C3%A3o%20de%2010%25%20de%20desconto." target="_blank" rel="noopener" class="floating-btn" style="background:#EBF2F7; color:#1E3A8A; border:1px solid #1E3A8A;" onclick="if(typeof gtag===\'function\'){gtag(\'event\', \'click_botao_desconto\', {\'event_category\': \'cupao\', \'event_label\': \'WhatsApp Cupao\'});}">\n        🎁 10% Desconto\n      </a>\n    </div>'
    
    content = re.sub(old_bar, new_bar, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

