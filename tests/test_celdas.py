from tests.cartones import *
from src.bingo import validar_quince_numeros
from src.bingo import validar_menos_quince_numeros
from src.bingo import validar_mas_quince_numeros
from src.bingo import numeros_sin_repetir
from src.bingo import matriz_3x9
from src.bingo import validar_numeros_carton

#Test que revisa si la cantidad de celda ocupadas es 15
def test_contar_celdas_ocupadas():
    assert validar_quince_numeros(carton_valido)
    assert not validar_quince_numeros(carton_invalido1)

#Test que revisa si la cantidad de celdas ocupadas no es mayor a 15
def test_menos_de_15_celdas_ocupadas():
    assert validar_menos_quince_numeros(carton_valido)
    assert not validar_menos_quince_numeros(carton_invalido1)

#Test que revisa si la cantidad de celdas ocupadas no es menor a 15
def test_mas_de_15_celdas_ocupadas():
    assert validar_mas_quince_numeros(carton_valido)
    assert not validar_mas_quince_numeros(carton_invalido2)

#Revisa si no hay numeros repetidos en el cartón
def test_numeros_repetidos():
    assert numeros_sin_repetir(carton_valido)
    assert not numeros_sin_repetir(carton_invalido1)

#Revisa que el cartón sea de 3 x 9
def test_matrix_3x9():
    assert matriz_3x9(carton_valido)
    assert not matriz_3x9(carton_invalido1)

#Revisa que los números del cartón vayan del 1 al 90
def test_validar_uno_a_noventa():
    assert validar_numeros_carton(carton_valido)
    assert not validar_numeros_carton(carton_invalido1)
