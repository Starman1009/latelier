with open('latelier.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_fn(name, max_lines=40):
    for i, l in enumerate(lines):
        if f'function {name}' in l:
            print(f"=== {name} ===")
            for j in range(i, min(len(lines), i + max_lines)):
                print(lines[j].rstrip().encode('ascii', 'replace').decode('ascii'))
            break

print_fn('renderMiseEnPlaceView')
print_fn('renderToolsView')
