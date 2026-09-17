import os, glob, re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the floating discount button and remove modal
    discount_btn_new = """<div id="discountFloatingBtnWrap" style="position:fixed; bottom:24px; left:24px; z-index:9990;">
  <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20receber%20o%20meu%20cup%C3%A3o%20de%2010%25%20de%20desconto." target="_blank" rel="noopener" style="display:flex; align-items:center; gap:8px; background:#EBF2F7; color:#1E3A8A; border:1.5px solid #1E3A8A; padding:10px 20px; border-radius:30px; font-family:'Inter',sans-serif; font-size:12px; font-weight:800; letter-spacing:0.05em; box-shadow:0 4px 15px rgba(30,58,138,0.15); cursor:pointer; transition:all 0.3s ease; text-decoration:none;" onmouseover="this.style.transform='translateY(-3px) scale(1.03)'; this.style.background='#D6E4F0';" onmouseout="this.style.transform='none'; this.style.background='#EBF2F7';" onclick="if(typeof gtag==='function'){gtag('event', 'click_botao_desconto', {'event_category': 'cupao', 'event_label': 'WhatsApp Cupao'});}">
    <span style="font-size:14px;">🎁</span>
    <span style="text-transform:uppercase;">Ganhar 10% Desconto</span>
    <span style="font-size:12px; margin-left:2px;">➔</span>
  </a>
</div>"""
    
    # regex to find the old floating wrap
    content = re.sub(r'<div id="discountFloatingBtnWrap".*?</button>\s*</div>', discount_btn_new, content, flags=re.DOTALL)
    
    # remove the modal HTML and script
    content = re.sub(r'<!-- Modal 10% Desconto -->.*?</script>', '', content, flags=re.DOTALL)

    # 2. Update floating bar whatsapp link
    content = re.sub(r'https://wa\.me/351960209396', r'https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20pedir%20um%20or%C3%A7amento.', content)

    # 3. If index.html, update the bottom section
    if filepath == 'index.html':
        content = re.sub(r'<style>\.ml-form-embedContent.*?</div>', r'<a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Gostaria%20de%20receber%20o%20meu%20cup%C3%A3o%20de%2010%25%20de%20desconto." target="_blank" rel="noopener" style="display:inline-block; background:#1a1a1a; color:#fff; padding:15px 30px; font-weight:bold; letter-spacing:0.1em; text-transform:uppercase; font-size:13px; border-radius:4px; text-decoration:none; transition:background 0.3s;" onmouseover="this.style.background=\'#333\'" onmouseout="this.style.background=\'#1a1a1a\'">Pedir Cupão no WhatsApp ➔</a>', content, flags=re.DOTALL)
        content = re.sub(r'Registe o seu e-mail para ter acesso exclusivo a novidades, novas coleções e receber um vale de 10% de desconto na primeira compra na nossa loja física.', r'Envie-nos uma mensagem no WhatsApp para ter acesso a novidades exclusivas e receber um vale de 10% de desconto na sua primeira compra!', content)

    # 4. If contactos.html, replace the form
    if filepath == 'contactos.html':
        form_new = """<div class="text-center py-8">
  <p class="text-sm text-gray-600 mb-6">Para agendar a sua visita de forma rápida e sem complicações, basta enviar-nos uma mensagem no WhatsApp com o seu nome e o dia pretendido.</p>
  <a href="https://wa.me/351961253466?text=Ol%C3%A1%21%20Quero%20agendar%20uma%20visita%20%C3%A0%20loja%3A%0A%0ANome%3A%0ADia%20e%20Hora%3A" target="_blank" rel="noopener" style="background-color: #25D366; color: white; border: none; font-size: 13px; font-weight: bold; text-decoration:none; display:inline-flex;" class="w-full py-4 px-6 rounded shadow flex items-center justify-center gap-2 hover:bg-green-500 transition-colors">
    💬 AGENDAR VISITA PELO WHATSAPP →
  </a>
</div>"""
        content = re.sub(r'<form id="booking-form" onsubmit="enviaAgendamentoWhatsApp\(event\)".*?</form>', form_new, content, flags=re.DOTALL)
        # remove the JS function for the old form
        content = re.sub(r'<script>\s*function enviaAgendamentoWhatsApp\(e\) \{.*?</script>', '', content, flags=re.DOTALL)

    # 5. Pack detalhe and Produto detalhe might have quoteWhatsAppBtn with the old number!
    # Update quoteWhatsAppBtn assignment if it exists
    content = re.sub(r'https://wa\.me/351960209396\?text=', r'https://wa.me/351961253466?text=', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

