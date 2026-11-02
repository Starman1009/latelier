import os

files = ['latelier.js', 'index.html', 'data-mastery.js', 'vault.html', 'data-recipes.js', 'data-prep-manual.js']
for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        diamond_q = content.count('\ufffd')
        print(f"{fn}: length={len(content)}, replacement_chars(\\ufffd)={diamond_q}")
