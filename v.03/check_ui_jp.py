import re

with open('build_html_en.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    stripped = line.strip()
    if not stripped or stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*') or stripped.startswith('#') or stripped.startswith('<!--'):
        continue
    # Remove inline comments for checking
    clean = re.sub(r'//.*', '', stripped)
    clean = re.sub(r'/\*.*\*/', '', clean)
    clean = re.sub(r'<!--.*-->', '', clean)
    
    if re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', clean):
        print(f"Line {i+1}: {clean}")
