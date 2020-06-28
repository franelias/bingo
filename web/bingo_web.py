from jinja2 import Template
import os
import sys
sys.path.append(os.getcwd())
from src.bingo import *

print('Para visualizar el cartón creado en una pagina web, abra el archivo bingo_salida.html')

template = Template(open('./web/plantilla.j2').read())

carton = template.render(tablero=carton_creado)

file = open("bingo_salida.html","w")

file.write(carton)

file.close()
