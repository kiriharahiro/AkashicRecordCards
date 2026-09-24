import re

with open('build_html_en.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', line):
        print(f"{i+1}: {line.strip()}")
