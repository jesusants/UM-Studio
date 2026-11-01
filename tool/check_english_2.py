# -*- coding: utf-8 -*-
with open(r'db/ingenieria_energetica.md', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('codigo: "01021803"')
idx2 = text.find('codigo: "03031818"')
block = text[idx1:idx2]

import re
items = re.findall(r'numero_tema:\s*(\d+)[\s\S]*?modalidad:\s*"([^"]+)"', block)
print(f"Total topics in 01021803: {len(items)}")
for num, mod in items:
    print(f"  Tema {num}: {mod}")
