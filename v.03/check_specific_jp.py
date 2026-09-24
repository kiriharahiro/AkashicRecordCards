import re

with open('build_html_en.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if re.search(r'霊的|今日|意味', line):
        print(f"Line {i+1}: {line.strip()}")
