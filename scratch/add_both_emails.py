import os
import glob
import re

html_files = glob.glob('*.html')
replaced_count = 0

footer_pattern_1 = """<a href="mailto:geral@adilmoveis.pt" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">✉️ geral@adilmoveis.pt</a>"""
footer_replacement_1 = """<a href="mailto:geral@adilmoveis.pt" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">✉️ geral@adilmoveis.pt</a><br><a href="mailto:adil.moveis@hotmail.com" style="color:inherit; text-decoration:none; transition:color 0.2s; margin-top: 4px; display: inline-block;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#aaa'">✉️ adil.moveis@hotmail.com</a>"""

footer_pattern_2 = """<a href="mailto:geral@adilmoveis.pt" onmouseout="this.style.color='#aaa'" onmouseover="this.style.color='#fff'" style="color:inherit; text-decoration:none; transition:color 0.2s;">✉️ geral@adilmoveis.pt</a>"""
footer_replacement_2 = """<a href="mailto:geral@adilmoveis.pt" onmouseout="this.style.color='#aaa'" onmouseover="this.style.color='#fff'" style="color:inherit; text-decoration:none; transition:color 0.2s;">✉️ geral@adilmoveis.pt</a><br><a href="mailto:adil.moveis@hotmail.com" onmouseout="this.style.color='#aaa'" onmouseover="this.style.color='#fff'" style="color:inherit; text-decoration:none; transition:color 0.2s; margin-top: 4px; display: inline-block;">✉️ adil.moveis@hotmail.com</a>"""

contacts_pattern = """✉️ <a href="mailto:geral@adilmoveis.pt" style="color:#1a1a1a; text-decoration:none;" class="hover:underline">geral@adilmoveis.pt</a>"""
contacts_replacement = """✉️ <a href="mailto:geral@adilmoveis.pt" style="color:#1a1a1a; text-decoration:none;" class="hover:underline">geral@adilmoveis.pt</a><br><span style="margin-left: 24px;">✉️ <a href="mailto:adil.moveis@hotmail.com" style="color:#1a1a1a; text-decoration:none;" class="hover:underline">adil.moveis@hotmail.com</a></span>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if footer_pattern_1 in content:
        content = content.replace(footer_pattern_1, footer_replacement_1)
        modified = True
        
    if footer_pattern_2 in content:
        content = content.replace(footer_pattern_2, footer_replacement_2)
        modified = True
        
    if contacts_pattern in content:
        content = content.replace(contacts_pattern, contacts_replacement)
        modified = True
        
    # Also change all form actions back to hotmail so they get the emails directly!
    form_pattern = 'action="https://formsubmit.co/geral@adilmoveis.pt"'
    if form_pattern in content:
        content = content.replace(form_pattern, 'action="https://formsubmit.co/adil.moveis@hotmail.com"')
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Added both emails to {filepath}")
        replaced_count += 1

print(f"Done! Updated email display in {replaced_count} HTML files.")
