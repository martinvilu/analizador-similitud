import os
from pprint import pprint
from difflib import unified_diff
from itertools import combinations

directorio = 'ej2'
ejercicios = os.listdir(directorio)
revisar = combinations(ejercicios,2)

for uno, dos in revisar:
    nombre_reporte = uno.removesuffix(".py") + "_" +\
                     dos.removesuffix(".py") + ".diff"
    archivo_1 = os.path.join(directorio, uno)
    archivo_2 = os.path.join(directorio, dos)
    with open(archivo_1, 'r', encoding="utf-8") as src,\
         open(archivo_2, 'r', encoding="utf-8") as dst:
        texto_1 = src.readlines()
        texto_2 = dst.readlines()
        
        difference = unified_diff(texto_1, texto_2, fromfile=uno, tofile=dos)
        with open(nombre_reporte, "w", encoding="utf-8") as rpt:
            print(f"{archivo_1} vs {archivo_2}")
            for item in difference:
                rpt.write(item)

