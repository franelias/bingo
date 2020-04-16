from src.bingo import carton
#Test que revisa si la cantidad de celda ocupadas es 15
def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador == 15
#Test que revisa si la cantidad de celdas ocupadas no es mayor a 15
def test_menos_de_15_celdas_ocupadas():
    mi_carton = carton();
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador <= 15
#Test que revisa si la cantidad de celdas ocupadas no es menor a 15
def test_mas_de_15_celdas_ocupadas():
    mi_carton = carton();
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador >= 15
#Test que revisa si hay al menos una celda ocupada en cada columna del carton
def test_revisar_columnas_ocupadas():
    mi_carton = carton()
    ban = 0
    for x in range(9):
        if mi_carton[0][x] == 0 and mi_carton[1][x] == 0 and mi_carton[2][x] == 0:
            ban = 1

    assert ban == 0
