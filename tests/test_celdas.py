from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador == 15

def test_menos_de_15_celdas_ocupadas():
    mi_carton = carton();
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador <= 15

def test_mas_de_15_celdas_ocupadas():
    mi_carton = carton();
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador >= 15

def test_revisar_columnas_ocupadas():
    mi_carton = carton()
    ban = 0
    for x in range(9):
        if mi_carton[0][x] == 0 and mi_carton[1][x] == 0 and mi_carton[2][x] == 0:
            ban = 1

    assert ban == 0

def contar_celdas_por_fila(carton, fila):
    contador = 0
    for x in range(9):
        contador = contador + carton[fila][x]

    return contador
#Test que valida que hay por lo menos una celda ocupada por fila
def test_revisar_filas_ocupadas():
    mi_carton = carton()
    for x in range(3):
        if contar_celdas_por_fila(mi_carton,x) == 0:
            assert False

    assert True
