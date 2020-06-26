import os
from bingo import carton
from bingo import carton_creado
from jinja2 import Template

print('Para visualizar el cartón creado en una pagina web, abra el archivo bingo_salida.html')

if os.path.isfile('./bingo_salida.html'):
    os.remove("bingo_salida.html")

file = open("bingo_salida.html","x")

template = Template(open('plantilla.j2').read())

file.write(template.render(tablero=carton_creado))

file.close()
