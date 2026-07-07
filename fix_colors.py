import os

directory = "/Users/nadiairina/Desktop/adil móveis/adil-moveis"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Promo banner to BLUE
    # Currently: background-color:#C8B598;color:#ffffff;padding:14px 0;font-size:16px;font-weight:700;letter-spacing:0.15em;z-index:50;position:relative;border-bottom:1px solid #b09e85;
    content = content.replace(
        'background-color:#C8B598;color:#ffffff;',
        'background-color:#EDF4F8;color:#1a1a1a;'
    ).replace(
        'border-bottom:1px solid #b09e85;',
        'border-bottom:1px solid #D4E4EE;'
    )
    
    # 2. Buttons to BEIGE
    # Currently: background:#EDF4F8;color:#1a1a1a;border:1px solid #D4E4EE;
    # hover: onmouseover="this.style.background='#C2D6E4';this.style.borderColor='#A4C2D6';"
    # hover out: onmouseout="this.style.background='#EDF4F8';this.style.borderColor='#D4E4EE';"
    
    # PACKS Button
    content = content.replace(
        "background:#EDF4F8;color:#1a1a1a;border:1px solid #D4E4EE;padding:6px 16px;transition:all 0.3s;border-radius:2px;text-decoration:none;\" onmouseover=\"this.style.background='#C2D6E4';this.style.borderColor='#A4C2D6';\" onmouseout=\"this.style.background='#EDF4F8';this.style.borderColor='#D4E4EE';\"",
        "color:#C8B598;border:1px solid #C8B598;padding:6px 16px;transition:all 0.3s;border-radius:2px;text-decoration:none;\" onmouseover=\"this.style.background='#C8B598';this.style.color='#ffffff';\" onmouseout=\"this.style.background='transparent';this.style.color='#C8B598';\""
    )
    
    # AGENDAR VISITA Button
    content = content.replace(
        "background:#EDF4F8;color:#1a1a1a;border:1px solid #D4E4EE;padding:7px 18px;transition:all 0.3s;border-radius:20px;text-decoration:none;\" onmouseover=\"this.style.background='#C2D6E4';this.style.borderColor='#A4C2D6';\" onmouseout=\"this.style.background='#EDF4F8';this.style.borderColor='#D4E4EE';\"",
        "background:#C8B598;color:#ffffff;border:1px solid #C8B598;padding:7px 18px;transition:all 0.3s;border-radius:20px;text-decoration:none;\" onmouseover=\"this.style.background='#b09e85';this.style.borderColor='#b09e85';\" onmouseout=\"this.style.background='#C8B598';this.style.borderColor='#C8B598';\""
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Colors flipped back correctly!")
