import codecs
import re

files = ['v.03/build_html_en.py', 'v.03/build_html.py']
for fname in files:
    with codecs.open(fname, 'r', 'utf-8') as f:
        text = f.read()
    
    text = re.sub(r'r"g:\\共有ドライブ\\[^"]+\\index_en\.html"', r'"../index_en.html"', text, flags=re.IGNORECASE)
    text = re.sub(r'r"g:\\共有ドライブ\\[^"]+\\v\.03\\index_en\.html"', r'"index_en.html"', text, flags=re.IGNORECASE)
    
    text = re.sub(r'r"g:\\共有ドライブ\\[^"]+\\index\.html"', r'"../index.html"', text, flags=re.IGNORECASE)
    text = re.sub(r'r"g:\\共有ドライブ\\[^"]+\\v\.03\\index\.html"', r'"index.html"', text, flags=re.IGNORECASE)
    
    with codecs.open(fname, 'w', 'utf-8') as f:
        f.write(text)
