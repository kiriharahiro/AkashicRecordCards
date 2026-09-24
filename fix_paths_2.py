import codecs
import re

fname = 'v.03/build_html_en.py'
with codecs.open(fname, 'r', 'utf-8') as f:
    text = f.read()
text = re.sub(r'"\.\./index_en\.html",\s*"\.\./index_en\.html"', r'"../index_en.html",\n"index_en.html"', text)
with codecs.open(fname, 'w', 'utf-8') as f:
    f.write(text)

fname = 'v.03/build_html.py'
with codecs.open(fname, 'r', 'utf-8') as f:
    text = f.read()
text = re.sub(r'"\.\./index\.html",\s*"\.\./index\.html"', r'"../index.html",\n"index.html"', text)
with codecs.open(fname, 'w', 'utf-8') as f:
    f.write(text)
