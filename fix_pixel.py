import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all onclick="if(typeof gtag==='function'){gtag(...);}" and append fbq('track', 'Lead');
    def replacer(match):
        original = match.group(0)
        # Only inject if not already there
        if "fbq('track', 'Lead')" not in original:
            # We insert it right before the closing brace of the if statement
            return original.replace('}', "; if(typeof fbq==='function'){fbq('track', 'Lead');}}")
        return original

    # We need a robust regex to find the gtag if statements inside onclick
    content = re.sub(r'onclick="if\s*\(typeof gtag\s*===\s*\'function\'\)\s*\{[^\}]+\}', replacer, content)

    # For the product pages, the click is handled in JS (addEventListener)
    if filepath in ['pack-detalhe.html', 'produto-detalhe.html']:
        js_click_block = r"if \(typeof gtag === 'function'\) \{(.*?)\}"
        def js_replacer(match):
            inner = match.group(1)
            if "fbq('track', 'Lead')" not in inner:
                return f"if (typeof gtag === 'function') {{{inner}\n            if (typeof fbq === 'function') fbq('track', 'Lead');\n          }}"
            return match.group(0)
        content = re.sub(js_click_block, js_replacer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Meta Pixel Leads injected.")
