import os
import glob

# WhatsApp Floating Button HTML
WA_HTML = """    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/351212582788" class="whatsapp-float" target="_blank" rel="noopener noreferrer">
      <svg class="whatsapp-icon" viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.514 2.266 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.504-5.731-1.464L0 24zm6.59-4.846c1.6.95 3.198 1.451 4.782 1.452 5.424 0 9.835-4.354 9.838-9.702.002-2.592-1.01-5.029-2.85-6.87C16.579 2.193 14.15 1.18 11.56 1.18 6.13 1.18 1.72 5.534 1.717 10.882c0 1.631.426 3.224 1.235 4.633L1.925 21.87l6.236-1.636zM17.154 14c-.284-.143-1.68-.829-1.94-.924-.259-.096-.448-.143-.637.143-.19.285-.733.924-.899 1.113-.165.19-.33.213-.614.072-2.012-1.01-3.136-1.785-4.385-3.928-.328-.564-.108-.874.116-1.096.2-.2.448-.523.673-.784.09-.105.15-.175.226-.245.075-.07.15-.14.226-.21.226-.226.376-.44.527-.722.15-.285.075-.544-.038-.722-.113-.178-.899-2.163-1.233-2.969-.328-.79-.663-.684-.899-.696-.23-.012-.495-.015-.756-.015-.262 0-.687.098-.946.381-.26.285-.99 1.012-.99 2.47 0 1.457 1.06 2.871 1.21 3.062.15.19 2.085 3.184 5.052 4.466.706.305 1.258.487 1.687.623.708.226 1.353.194 1.862.118.568-.084 1.681-.687 1.916-1.353.235-.667.235-1.238.165-1.353-.07-.115-.26-.19-.544-.332z"/>
      </svg>
      <span>WhatsApp</span>
    </a>"""

for filepath in glob.glob("*.html"):
    if filepath == "dashboard.html":
        continue # Skip dashboard
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already added
    if "whatsapp-float" in content:
        print(f"Skipping {filepath} (already contains whatsapp button)")
        continue
        
    # Inject before </body>
    if "</body>" in content:
        content = content.replace("</body>", f"{WA_HTML}\n  </body>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added WhatsApp button to {filepath}")
    else:
        print(f"No </body> tag found in {filepath}")

print("WhatsApp floating button integrated successfully on all pages!")
