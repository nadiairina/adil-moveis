import glob

html_files = glob.glob("*.html")

snipcart_script = """    <!-- Snipcart Configuration -->
    <script async src="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js"></script>
    <div id="snipcart" data-api-key="ODE4MjNlYWYtZGViOS00OGY3LWJhZWEtODU1OTE5OTYzMzQxNjM5MTYyMDI2OTM2NjA0MTY3" hidden></div>
    <script>
      document.addEventListener('snipcart.ready', function() {
        Snipcart.api.session.setLanguage('pt-PT', {
          cart: {
            empty: "O seu carrinho está vazio.",
            back_to_store: "Voltar à loja"
          }
        });
      });
    </script>"""

old_snipcart = """    <!-- Snipcart Configuration -->
    <script async src="https://cdn.snipcart.com/themes/v3.4.1/default/snipcart.js"></script>
    <div id="snipcart" data-api-key="ODE4MjNlYWYtZGViOS00OGY3LWJhZWEtODU1OTE5OTYzMzQxNjM5MTYyMDI2OTM2NjA0MTY3" hidden></div>"""

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if old_snipcart in content and 'snipcart.ready' not in content:
            content = content.replace(old_snipcart, snipcart_script)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print("Translated cart in", f)
    except Exception as e:
        print("Error", f, e)
