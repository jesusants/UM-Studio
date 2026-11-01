# -*- coding: utf-8 -*-
for path in ['db/ingenieria_energetica.md', 'assets/data/ingenieria_energetica.md']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    bad = '"Harmonic Notation 30 min • Euler\'s identity & complex conjugate power"          - numero_tema: 22'
    good = '"Harmonic Notation 30 min • Euler\'s identity & complex conjugate power"\n          - numero_tema: 22'
    assert bad in c, f'bad not in {path}'
    c = c.replace(bad, good)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(c)
print('Fixed newline successfully.')
