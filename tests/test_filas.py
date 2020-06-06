from tests.cartones import *
from src.bingo import fila_5_celdas_ocupadas
from src.bingo import filas_2_celdas_consecutivas_vacias
from src.bingo import revisar_filas_ocupadas
from src.bingo import filas_2_celdas_consecutivas_ocupadas

def test_fila_5_celdas_ocupadas():
    assert fila_5_celdas_ocupadas(carton_valido)
    assert not fila_5_celdas_ocupadas(carton_invalido4)

def test_filas_celdas_consecutivas_vacias():
    assert filas_2_celdas_consecutivas_vacias(carton_valido)
    assert not filas_2_celdas_consecutivas_vacias(carton_invalido4)

#Test que valida que hay por lo menos una celda ocupada por fila
def test_revisar_filas_ocupadas():
    assert revisar_filas_ocupadas(carton_valido)
    assert not revisar_filas_ocupadas(carton_invalido4)

def test_filas_2_celdas_consecutivas_ocupadas():
    assert filas_2_celdas_consecutivas_ocupadas(carton_valido)
    assert not filas_2_celdas_consecutivas_ocupadas(carton_invalido4)
