# -*- coding: utf-8 -*-
import os
import sys

DB_PATH = r'C:\Users\ESTUDIANTE\OneDrive\U Studio\db\ingenieria_energetica.md'
ASSETS_PATH = r'C:\Users\ESTUDIANTE\OneDrive\U Studio\assets\data\ingenieria_energetica.md'

def escape_yaml_str(s):
    if not s:
        return ""
    # In YAML double quotes, backslash must be escaped as \\ and double quote as \"
    return s.replace('\\', '\\\\').replace('"', '\\"')

def format_topic_yaml(t):
    lines = []
    lines.append(f"          - numero_tema: {t['numero_tema']}")
    lines.append(f"            corte: {t['corte']}")
    lines.append(f"            modalidad: \"{t.get('modalidad', 'tecnica')}\"")
    if 'verbalizacion_ingles' in t and t['verbalizacion_ingles']:
        verb = escape_yaml_str(t['verbalizacion_ingles'])
        lines.append(f"            verbalizacion_ingles: \"{verb}\"")
    titulo = escape_yaml_str(t['titulo'])
    lines.append(f"            titulo: \"{titulo}\"")
    objetivo = escape_yaml_str(t['objetivo'])
    lines.append(f"            objetivo: \"{objetivo}\"")
    latex = escape_yaml_str(t.get('concepto_clave_latex', ''))
    lines.append(f"            concepto_clave_latex: \"{latex}\"")
    
    ejemplo = t.get('ejemplo', '').strip()
    if '\n' in ejemplo:
        lines.append("            ejemplo: |")
        for eline in ejemplo.split('\n'):
            lines.append(f"              {eline.strip()}")
    else:
        ej_escaped = escape_yaml_str(ejemplo)
        lines.append(f"            ejemplo: \"{ej_escaped}\"")
        
    bloque = escape_yaml_str(t.get('bloque_sugerido', ''))
    lines.append(f"            bloque_sugerido: \"{bloque}\"")
    
    if 'slides' in t and t['slides']:
        lines.append("            slides:")
        for s in t['slides']:
            lines.append(f"              - numero: {s['numero']}")
            lines.append(f"                seccion: \"{escape_yaml_str(s.get('seccion', 'TEORÍA'))}\"")
            stitle = escape_yaml_str(s.get('titulo', ''))
            lines.append(f"                titulo: \"{stitle}\"")
            if 'puntos' in s and s['puntos']:
                lines.append("                puntos:")
                for p in s['puntos']:
                    p_esc = escape_yaml_str(p)
                    lines.append(f"                  - \"{p_esc}\"")
            if 'tabla' in s and s['tabla']:
                lines.append("                tabla:")
                lines.append("                  columnas:")
                for col in s['tabla']['columnas']:
                    col_esc = escape_yaml_str(col)
                    lines.append(f"                    - \"{col_esc}\"")
                lines.append("                  filas:")
                for fila in s['tabla']['filas']:
                    lines.append("                    -")
                    for cell in fila:
                        c_esc = escape_yaml_str(cell)
                        lines.append(f"                      - \"{c_esc}\"")
            if 'ejemplo' in s and s['ejemplo']:
                lines.append(f"                ejemplo: \"{escape_yaml_str(s['ejemplo'])}\"")
    return '\n'.join(lines) + '\n'

def format_topics_yaml(topics_list):
    return ''.join(format_topic_yaml(t) for t in topics_list)

def inject_topics_after(marker, topics_yaml):
    content = open(DB_PATH, 'r', encoding='utf-8').read()
    if marker not in content:
        print(f"ERROR: Marker '{marker}' not found in DB.")
        sys.exit(1)
    
    new_content = content.replace(marker, topics_yaml + marker, 1)
    open(DB_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    open(ASSETS_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    print("Injected successfully into both files.")

if __name__ == '__main__':
    print("Injector ready.")
