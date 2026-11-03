"""Verify every encrypted original, page text and preview; password comes from stdin."""
import base64
import hashlib
import io
import json
import math
import sys
from pathlib import Path
import pymupdf
from PIL import Image
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parent / 'private-vault'
config = json.loads((root / 'config.json').read_text(encoding='utf-8'))
password = sys.stdin.readline().rstrip('\r\n')
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=base64.b64decode(config['salt']), iterations=config['iterations']).derive(password.encode())
del password

def decrypt(name):
    raw = (root / name).read_bytes()
    return AESGCM(key).decrypt(raw[:12], raw[12:], b'latelier-vault-v1')

data = json.loads(decrypt('index.bin'))
assert data['formatVersion'] == 2
assert len(data['inventory']) == 13
assert len(data['manuals']) == 12
pages = tables = 0
for manual in data['manuals']:
    original = decrypt(manual['id'] + '.bin')
    assert hashlib.sha256(original).hexdigest() == manual['sha256']
    source = Path.home() / 'Downloads' / manual['name']
    assert hashlib.sha256(source.read_bytes()).hexdigest() == manual['sha256']
    doc = pymupdf.open(stream=original, filetype='pdf')
    assert len(doc) == len(manual['pages'])
    for n, page in enumerate(manual['pages'], 1):
        assert page['number'] == n
        assert page['text'] == doc[n-1].get_text(sort=True), (manual['id'], n, 'text mismatch')
        with Image.open(io.BytesIO(decrypt(page['preview']))) as preview:
            assert preview.format == 'WEBP'
            assert preview.size == (math.ceil(page['width']*1.5), math.ceil(page['height']*1.5))
            preview.load()
        assert 'content' in page
        tables += sum(c['kind'] == 'table' for c in page['content'])
        pages += 1
    doc.close()
for item in data['inventory']:
    assert hashlib.sha256((Path.home() / 'Downloads' / item['name']).read_bytes()).hexdigest() == item['sha256']
assert pages == 757
blob = (root / 'index.bin').read_bytes()
try:
    AESGCM(bytes(32)).decrypt(blob[:12], blob[12:], b'latelier-vault-v1')
    raise AssertionError('Wrong key accepted')
except InvalidTag:
    pass
print(f'PASS: 13 supplied files, 12 byte-identical originals, {pages} complete page texts and readable encrypted previews, {tables} tables, wrong-key rejection.')
