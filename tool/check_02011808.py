# -*- coding: utf-8 -*-
with open('db/ingenieria_energetica.md', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('codigo: "02011808"')
idx2 = text.find('codigo: "02021811"')
block = text[idx1:idx2]

import re
titles = re.findall(r'numero_tema:\s*(\d+)[\s\S]*?titulo:\s*"([^"]+)"', block)
print(f"02011808 Topics ({len(titles)}):")
for num, t in titles:
    print(f"  Tema {num}: {t}")
