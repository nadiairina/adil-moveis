import re

with open('/Users/nadiairina/Desktop/adil móveis/adil-moveis/testemunhos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see what's at the end of the file.
end_part = content[-1000:]
print("--- End of file ---")
print(end_part)
