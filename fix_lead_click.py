import re

for filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the waBtn click listener and inject fbq
    def replacer(match):
        inner = match.group(1)
        if "fbq('track'" not in inner:
            return f"waBtn.addEventListener('click', function() {{\n{inner}\n            if (typeof fbq === 'function') fbq('track', 'Lead');\n          }});"
        return match.group(0)
        
    content = re.sub(r"waBtn\.addEventListener\('click',\s*function\(\)\s*\{(.*?)\}\);", replacer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

