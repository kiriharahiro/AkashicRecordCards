import codecs

fname = 'v.03/build_html_en.py'
with codecs.open(fname, 'r', 'utf-8') as f:
    text = f.read()
text = text.replace('"../index_en.html",\n"../index_en.html"', '"../index_en.html",\n"index_en.html"')
with codecs.open(fname, 'w', 'utf-8') as f:
    f.write(text)

fname = 'v.03/build_html.py'
with codecs.open(fname, 'r', 'utf-8') as f:
    text = f.read()
text = text.replace('"../index.html",\n"../index.html"', '"../index.html",\n"index.html"')
with codecs.open(fname, 'w', 'utf-8') as f:
    f.write(text)
