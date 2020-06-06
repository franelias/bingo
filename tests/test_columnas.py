from tests.cartones import *
from src.bingo import columnas_con_una_celda_ocupada
from src.bingo import columnas_llenas
from src.bingo import posicion_numeros_izquierda_a_derecha
from src.bingo import posicion_numeros_en_columna
from src.bingo import columnas_vacias
from src.bingo import revisar_columnas_ocupadas

def test_columnas_con_una_celda_ocupada():
    assert columnas_con_una_celda_ocupada(carton_valido)
    assert not columnas_con_una_celda_ocupada(carton_invalido3)

def test_columnas_llenas():
    assert columnas_llenas(carton_valido)
    assert not columnas_llenas(carton_invalido3)

def test_posicion_numeros_izquierda_a_derecha():
    assert posicion_numeros_izquierda_a_derecha(carton_valido)
    assert not posicion_numeros_izquierda_a_derecha(carton_invalido3)

def test_posicion_numeros_en_columna():
    assert posicion_numeros_en_columna(carton_valido)
    assert not posicion_numeros_en_columna(carton_invalido3)

def test_columnas_vacias():
    assert columnas_vacias(carton_valido)
    assert not columnas_vacias(carton_invalido3)

#Test que revisa si hay al menos una celda ocupada en cada columna del carton
def test_revisar_columnas_ocupadas():
    assert revisar_columnas_ocupadas(carton_valido)
    assert not revisar_columnas_ocupadas(carton_invalido3)
