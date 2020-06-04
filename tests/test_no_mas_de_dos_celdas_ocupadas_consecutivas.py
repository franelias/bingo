from src.bingo import carton
from src.bingo import filas_2_celdas_consecutivas_ocupadas

def test_filas_2_celdas_consecutivas_ocupadas():
    mi_carton = carton()
    assert filas_2_celdas_consecutivas_ocupadas(mi_carton)
