import glob

def main():
    html_files = glob.glob("*.html")
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            content = content.replace('data-category="Todos"', 'data-category="all"')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    print("Fixed data-category='Todos' to 'all'")

if __name__ == "__main__":
    main()
