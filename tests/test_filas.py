from tests.cartones import *
from src.bingo import fila_5_celdas_ocupadas
from src.bingo import revisar_filas_ocupadas
from src.bingo import filas_2_celdas_consecutivas_vacias_o_ocupadas

#Revisa que por fila haya solo 5 celdas ocupadas
def test_fila_5_celdas_ocupadas():
    assert fila_5_celdas_ocupadas(carton_valido)
    assert not fila_5_celdas_ocupadas(carton_invalido4)

#Revisa que no haya celdas con más de 2 celdas consecutivas vacías
def test_filas_celdas_consecutivas_vacias():
    assert filas_2_celdas_consecutivas_vacias_o_ocupadas(carton_valido)
    assert not filas_2_celdas_consecutivas_vacias_o_ocupadas(carton_invalido4)

#Revisa que haya por lo menos una celda ocupada por fila
def test_revisar_filas_ocupadas():
    assert revisar_filas_ocupadas(carton_valido)
    assert not revisar_filas_ocupadas(carton_invalido4)

#Revisa que no haya celdas con más de 2 celdas consecutivas ocupadas
def test_filas_2_celdas_consecutivas_ocupadas():
    assert filas_2_celdas_consecutivas_vacias_o_ocupadas(carton_valido)
    assert not filas_2_celdas_consecutivas_vacias_o_ocupadas(carton_invalido4)
