# -*- coding: utf-8 -*-
DB_PATH = r'C:\Users\ESTUDIANTE\OneDrive\U Studio\db\ingenieria_energetica.md'
ASSETS_PATH = r'C:\Users\ESTUDIANTE\OneDrive\U Studio\assets\data\ingenieria_energetica.md'

for path in [DB_PATH, ASSETS_PATH]:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    start_marker = '          - numero_tema: 10\n            corte: 2\n            modalidad: "teorico"\n            titulo: "Descomposición en Valores Singulares'
    end_marker = '      - codigo: "06011837"'
    
    idx1 = c.find(start_marker)
    idx2 = c.find(end_marker, idx1)
    if idx1 != -1 and idx2 != -1:
        c = c[:idx1] + c[idx2:]
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(c)
        print(f"Reverted Álgebra Lineal injection in {path}")
    else:
        print(f"Markers not found in {path}")
