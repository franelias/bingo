from src.bingo import carton
from src.bingo import validar_quince_numeros
from src.bingo import validar_menos_quince_numeros
from src.bingo import validar_mas_quince_numeros
from src.bingo import contar_celdas_por_fila

#Test que revisa si la cantidad de celda ocupadas es 15
def test_contar_celdas_ocupadas():
    mi_carton = carton()
    assert validar_quince_numeros(mi_carton)

#Test que revisa si la cantidad de celdas ocupadas no es mayor a 15
def test_menos_de_15_celdas_ocupadas():
    mi_carton = carton()
    assert validar_menos_quince_numeros(mi_carton)

#Test que revisa si la cantidad de celdas ocupadas no es menor a 15
def test_mas_de_15_celdas_ocupadas():
    mi_carton = carton()
    assert validar_mas_quince_numeros(mi_carton)

#Test que revisa si hay al menos una celda ocupada en cada columna del carton
def test_revisar_columnas_ocupadas():
    mi_carton = carton()
    for x in range(9):
        if mi_carton[0][x] == 0 and mi_carton[1][x] == 0 and mi_carton[2][x] == 0:
            assert False

    assert True

#Test que valida que hay por lo menos una celda ocupada por fila
def test_revisar_filas_ocupadas():
    mi_carton = carton()
    for x in range(3):
        if contar_celdas_por_fila(mi_carton,x) == 0:
            assert False

    assert True
