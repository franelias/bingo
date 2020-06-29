from jinja2 import Template
from src.bingo import *

print('Para visualizar el cartón creado en una pagina web, abra el archivo bingo_salida.html')

template = Template(open('src/plantilla.j2').read())

carton_creado = template.render(tablero=carton())

file = open("bingo_salida.html","w")

file.write(carton_creado)

file.close()
