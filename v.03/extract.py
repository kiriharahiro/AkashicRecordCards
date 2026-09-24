import sys
import re

with open('index_en.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if match:
    with open('test_en.js', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
    print('extracted script')
else:
    print('no script found')
