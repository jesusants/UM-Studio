# -*- coding: utf-8 -*-
from injector_base import DB_PATH, ASSETS_PATH

content = open(DB_PATH, 'r', encoding='utf-8').read()
start = content.index('codigo: "01021806"')
end = content.index('codigo: "04021823"')
block = content[start:end]

# 1. Renumber notation topics currently numbered 11..15, 21:
# Specifically:
# - Heat Transfer Modes: 11 -> 16
# - Solar Photovoltaic & Wind: 12 -> 17
# - Power Systems & OPF: 13 -> 18
# - Electrochemistry & Hydrogen: 14 -> 19
# - Interpreting & Presenting Graphs: 15 -> 20
# (21 is already 21: Uncertainty Propagation)

block = block.replace(
    '          - numero_tema: 11\n            corte: 1\n            modalidad: "notacion_ingenieria"\n            titulo: "Heat Transfer Modes',
    '          - numero_tema: 16\n            corte: 1\n            modalidad: "notacion_ingenieria"\n            titulo: "Heat Transfer Modes'
)

block = block.replace(
    '          - numero_tema: 12\n            corte: 1\n            modalidad: "notacion_ingenieria"\n            titulo: "Solar Photovoltaic & Wind',
    '          - numero_tema: 17\n            corte: 1\n            modalidad: "notacion_ingenieria"\n            titulo: "Solar Photovoltaic & Wind'
)

block = block.replace(
    '          - numero_tema: 13\n            corte: 2\n            modalidad: "notacion_ingenieria"\n            titulo: "Power Systems & Optimal',
    '          - numero_tema: 18\n            corte: 2\n            modalidad: "notacion_ingenieria"\n            titulo: "Power Systems & Optimal'
)

block = block.replace(
    '          - numero_tema: 14\n            corte: 2\n            modalidad: "notacion_ingenieria"\n            titulo: "Electrochemistry, Green Hydrogen',
    '          - numero_tema: 19\n            corte: 2\n            modalidad: "notacion_ingenieria"\n            titulo: "Electrochemistry, Green Hydrogen'
)

block = block.replace(
    '          - numero_tema: 15\n            corte: 3\n            modalidad: "notacion_ingenieria"\n            titulo: "Interpreting & Presenting Graphs',
    '          - numero_tema: 20\n            corte: 3\n            modalidad: "notacion_ingenieria"\n            titulo: "Interpreting & Presenting Graphs'
)

# 2. Renumber general topics currently numbered 16..20 to 11..15:
# - Hedging: 16 -> 11
# - Complex Passives: 17 -> 12
# - Mixed Conditionals: 18 -> 13
# - Nominalisation: 19 -> 14
# - Structuring Oral Presentations: 20 -> 15

block = block.replace(
    '          - numero_tema: 16\n            corte: 2\n            modalidad: "general"\n            titulo: "Hedging and Cautious Language',
    '          - numero_tema: 11\n            corte: 2\n            modalidad: "general"\n            titulo: "Hedging and Cautious Language'
)

block = block.replace(
    '          - numero_tema: 17\n            corte: 2\n            modalidad: "general"\n            titulo: "Complex Passives and Impersonal',
    '          - numero_tema: 12\n            corte: 2\n            modalidad: "general"\n            titulo: "Complex Passives and Impersonal'
)

block = block.replace(
    '          - numero_tema: 18\n            corte: 2\n            modalidad: "general"\n            titulo: "Mixed Conditionals in Engineering',
    '          - numero_tema: 13\n            corte: 2\n            modalidad: "general"\n            titulo: "Mixed Conditionals in Engineering'
)

block = block.replace(
    '          - numero_tema: 19\n            corte: 3\n            modalidad: "general"\n            titulo: "Nominalisation and Information Density',
    '          - numero_tema: 14\n            corte: 3\n            modalidad: "general"\n            titulo: "Nominalisation and Information Density'
)

block = block.replace(
    '          - numero_tema: 20\n            corte: 3\n            modalidad: "general"\n            titulo: "Structuring Oral Presentations, Keynote',
    '          - numero_tema: 15\n            corte: 3\n            modalidad: "general"\n            titulo: "Structuring Oral Presentations, Keynote'
)

new_content = content[:start] + block + content[end:]
open(DB_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
open(ASSETS_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
print("01021806 renumbered properly!")
