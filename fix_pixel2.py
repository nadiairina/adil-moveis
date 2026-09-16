import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath in ['dashboard.html', 'dashboard-estrategias.html', 'search.html']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The broken syntax is:
    # {'event_category': '...', 'event_label': '...'; if(typeof fbq==='function'){fbq('track', 'Lead');}});}
    # I need to fix it back to:
    # {'event_category': '...', 'event_label': '...'}); if(typeof fbq==='function'){fbq('track', 'Lead');}}
    
    broken_pattern = r"\{'event_category': '(.*?)', 'event_label': '(.*?)'; if\(typeof fbq==='function'\}\{fbq\('track', 'Lead'\);\}\}\);\}"
    
    # Wait, the string is exactly:
    # {'event_category': 'contacto_flutuante', 'event_label': 'Pedir Orcamento WhatsApp'; if(typeof fbq==='function'){fbq('track', 'Lead');}});}
    
    def fixer(match):
        category = match.group(1)
        label = match.group(2)
        return f"{{'event_category': '{category}', 'event_label': '{label}'}}); if(typeof fbq==='function'){{fbq('track', 'Lead');}}}}"
        
    content = re.sub(r"\{'event_category': '(.*?)', 'event_label': '(.*?)'; if\(typeof fbq==='function'\}\{fbq\('track', 'Lead'\);\}\}\);\w*\}", fixer, content)

    # Let's just use string replacement because it's easier and safer
    content = content.replace("'; if(typeof fbq==='function'){fbq('track', 'Lead');}});}", "'}); if(typeof fbq==='function'){fbq('track', 'Lead');}}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Meta Pixel Leads fixed.")
