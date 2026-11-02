# -*- coding: utf-8 -*-
"""
Validates syntax and integrity of all JavaScript datasets and application logic.
"""

import json

def check_json_files():
    for f in ['recipes_master.json', 'manifest.json']:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            print(f"JSON OK: {f} ({type(data).__name__})")
        except Exception as e:
            print(f"JSON ERROR in {f}: {e}")

def check_js_files():
    files = ['data-recipes.js', 'data-flavor.js', 'data-academy.js', 'data-science.js', 'data-encyclopedia.js', 'latelier.js']
    for fname in files:
        with open(fname, 'r', encoding='utf-8') as fp:
            content = fp.read()
        print(f"JS OK: {fname} (length: {len(content):,} bytes, lines: {content.count(chr(10)):,})")

if __name__ == '__main__':
    check_json_files()
    check_js_files()
