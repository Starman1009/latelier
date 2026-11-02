with open('latelier.js', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'switch' in line:
            print(f"Line {i+1}: {line.strip()}")
