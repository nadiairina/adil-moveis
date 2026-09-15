with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the mobile query
old_media = """@media (max-width: 480px) {
  .floating-contact-bar {
    gap: 6px;
    padding: 6px 10px;
  }
  .floating-btn {
    padding: 5px 8px;
    font-size: 7.5px;
  }
}"""

new_media = """@media (max-width: 480px) {
  .floating-contact-bar {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    padding: 12px;
    border-radius: 24px;
    width: 92vw;
  }
  .floating-btn {
    display: flex;
    justify-content: center;
    padding: 8px 4px;
    font-size: 8.5px;
    width: 100%;
  }
}"""

content = content.replace(old_media, new_media)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

