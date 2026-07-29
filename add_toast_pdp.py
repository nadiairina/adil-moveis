import re

files = [
    '/Users/nadiairina/Desktop/adil móveis/adil-moveis/produto-detalhe.html',
    '/Users/nadiairina/Desktop/adil móveis/adil-moveis/pack-detalhe.html'
]

toast_html = """
    <!-- TOAST NOTIFICATION -->
    <div id="pdp-toast" style="position:fixed; bottom:20px; right:20px; background:#1a1a1a; color:#fff; padding:15px 25px; border-radius:4px; font-size:13px; font-family:'Inter',sans-serif; transform:translateY(100px); opacity:0; transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index:9999; display:flex; align-items:center; gap:10px; box-shadow:0 10px 30px rgba(0,0,0,0.15); pointer-events:none;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#25D366" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
      <span id="pdp-toast-msg">Adicionado com sucesso!</span>
    </div>
    
    <script>
      function showPdpToast(msg) {
        var toast = document.getElementById('pdp-toast');
        var text = document.getElementById('pdp-toast-msg');
        text.innerText = msg;
        toast.style.transform = 'translateY(0)';
        toast.style.opacity = '1';
        setTimeout(function() {
          toast.style.transform = 'translateY(100px)';
          toast.style.opacity = '0';
        }, 4000);
      }
      
      document.addEventListener('DOMContentLoaded', function() {
        var waBtn = document.getElementById('quoteWhatsAppBtn');
        if (waBtn) {
          waBtn.addEventListener('click', function() {
            showPdpToast("Redirecionando para o WhatsApp...");
          });
        }
        
        // Listen to Snipcart added event
        document.addEventListener('snipcart.ready', function() {
          Snipcart.events.on('item.added', function (cartItem) {
             showPdpToast("Produto adicionado ao carrinho!");
          });
        });
      });
    </script>
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="pdp-toast"' not in content:
        content = content.replace('</body>', toast_html + '\n  </body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Toast to {filepath}")
