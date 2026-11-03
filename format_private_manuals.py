"""Build encrypted, source-faithful page views. No private plaintext is deployed."""
import base64
import hashlib
import io
import json
import os
import sys
from pathlib import Path
import pymupdf
from PIL import Image
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent
AAD = b'latelier-vault-v1'

def ordered_words(words):
    lines=[]
    for word in sorted(words, key=lambda w: (w[1], w[0])):
        center=(word[1]+word[3])/2
        line=next((line for line in lines if abs(line[0]-center) < max(2, (word[3]-word[1])*.35)),None)
        if line is None:
            line=[center,[]];lines.append(line)
        line[1].append(word)
    return '\n'.join(' '.join(w[4] for w in sorted(line[1],key=lambda w:w[0])) for line in sorted(lines,key=lambda line:line[0]))

def build(password, render_previews=True):
    vault = ROOT / 'private-vault'
    config = json.loads((vault / 'config.json').read_text(encoding='utf-8'))
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                    salt=base64.b64decode(config['salt']), iterations=config['iterations']).derive(password.encode())
    cipher = AESGCM(key)
    def unseal(path):
        raw = path.read_bytes()
        return cipher.decrypt(raw[:12], raw[12:], AAD)
    def seal(raw, path):
        nonce = os.urandom(12)
        path.write_bytes(nonce + cipher.encrypt(nonce, raw, AAD))
    data = json.loads(unseal(vault / 'index.bin'))
    inventory = []
    # Verify all sources before changing the collection.
    for m in data['manuals']:
        source = Path.home() / 'Downloads' / m['name']
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != m['sha256']:
            raise ValueError('A source PDF has changed; reconcile the source before formatting: ' + m['name'])
        inventory.append({'name': m['name'], 'sha256': digest, 'manualId': m['id'], 'pages': len(m['pages']), 'duplicate': False})
    for alias in data['aliases']:
        source = Path.home() / 'Downloads' / alias['name']
        match = next(m for m in data['manuals'] if m['id'] == alias['sameAs'])
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != match['sha256']:
            raise ValueError('Duplicate now differs: ' + alias['name'])
        inventory.append({'name': alias['name'], 'sha256': digest, 'manualId': match['id'], 'pages': len(match['pages']), 'duplicate': True})
    pages_dir = vault / 'pages'
    pages_dir.mkdir(exist_ok=True)
    table_count = 0
    for m in data['manuals']:
        doc = pymupdf.open(stream=unseal(vault / (m['id'] + '.bin')), filetype='pdf')
        for page, record in zip(doc, m['pages'], strict=True):
            tables = page.find_tables().tables
            elements = []
            bounds = []
            for table in tables:
                cells = [[ordered_words(page.get_text('words',clip=pymupdf.Rect(cell))) if cell else None for cell in row.cells] for row in table.rows]
                if not cells or not any(any(cell for cell in row) for row in cells):
                    continue
                bounds.append(pymupdf.Rect(table.bbox))
                elements.append({'kind': 'table', 'y': table.bbox[1], 'rows': cells})
                table_count += 1
            for block in page.get_text('blocks', sort=True):
                if block[6] != 0 or not block[4].strip():
                    continue
                rect = pymupdf.Rect(block[:4])
                # Only omit a block if it is entirely represented by a table.
                if any(b.contains(rect) for b in bounds):
                    continue
                words=page.get_text('words',clip=rect)
                outside=[w for w in words if not any(b.contains(pymupdf.Point((w[0]+w[2])/2,(w[1]+w[3])/2)) for b in bounds)]
                text=ordered_words(outside)
                if text:elements.append({'kind': 'text', 'y': block[1], 'text': text})
            record['content'] = sorted(elements, key=lambda x: x['y'])
            record['hasIngredientTable'] = any(
                'ingredient' in str(cell).lower()
                for item in elements if item['kind'] == 'table'
                for row in item['rows'] for cell in row if cell)
            record['imageCount'] = len(page.get_images())
            record['width'], record['height'] = page.rect.width, page.rect.height
            filename = f"{m['id']}-{record['number']}.bin"
            record['preview'] = 'pages/' + filename
            if render_previews or not (pages_dir / filename).exists():
                pix = page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False)
                image = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
                buf = io.BytesIO()
                image.save(buf, format='WEBP', quality=88, method=4)
                seal(buf.getvalue(), pages_dir / filename)
        print(f"Formatted {len(m['pages'])} pages", flush=True)
        doc.close()
    data['inventory'] = inventory
    data['formatVersion'] = 2
    seal(json.dumps(data, ensure_ascii=False).encode('utf-8'), vault / 'index.bin')
    print(json.dumps({'files': len(inventory), 'uniqueManuals': len(data['manuals']),
                      'pages': sum(len(m['pages']) for m in data['manuals']), 'tables': table_count,
                      'encryptedPreviewBytes': sum(p.stat().st_size for p in pages_dir.glob('*.bin'))}))

if __name__ == '__main__':
    build(sys.stdin.readline().rstrip('\r\n'), render_previews='--tables-only' not in sys.argv)
