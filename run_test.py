import re
import os

def check_swedish():
    swedish_chars = re.compile(r'[\xe5\xe4\xf6\xc5\xc4\xd6]')
    found = False
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'images' in root or 'run_test.py' in root:
            continue
        for file in files:
            if file == 'run_test.py': continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if swedish_chars.search(content):
                        print(f"Found Swedish characters in {filepath}")
                        found = True
            except UnicodeDecodeError:
                pass
    return found

if check_swedish():
    print("Swedish text found!")
    exit(1)
else:
    print("No Swedish text found.")
    exit(0)
