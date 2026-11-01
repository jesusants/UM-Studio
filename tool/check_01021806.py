# -*- coding: utf-8 -*-
import re

content = open(r'C:\Users\ESTUDIANTE\OneDrive\U Studio\db\ingenieria_energetica.md', encoding='utf-8').read()
start = content.index('codigo: "01021806"')
end = content.index('codigo: "04021823"')
block = content[start:end]

matches = re.findall(r'numero_tema:\s*(\d+)\s*\n\s*corte:\s*\d+\s*\n\s*modalidad:\s*"([^"]+)"', block)
for m in matches:
    print(f"Tema {m[0]}: {m[1]}")
print(f"Total: {len(matches)}")
