from src.bingo import carton
from src.bingo import filas_2_celdas_consecutivas_vacias

def test_filas_celdas_consecutivas_vacias():
    mi_carton = carton()
    assert filas_2_celdas_consecutivas_vacias(mi_carton)
