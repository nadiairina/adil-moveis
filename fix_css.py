with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex-wrap and justify-content to floating-contact-bar
content = content.replace('display: flex; /* Show on all devices */', 'display: flex; flex-wrap: wrap; justify-content: center; /* Show on all devices */')

# Make the wrapper slightly wider on mobile to accommodate a 2x2 grid nicely
content = content.replace('max-width: 90vw;', 'max-width: 95vw;')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

