import re

with open('latelier.js', 'r', encoding='utf-8') as f:
    content = f.read()

cases = re.findall(r'case\s+["\'](\w+)["\']:', content)
print("Router cases in latelier.js:", cases)

functions = re.findall(r'function\s+(render\w+)', content)
print("Render functions in latelier.js:", functions)
