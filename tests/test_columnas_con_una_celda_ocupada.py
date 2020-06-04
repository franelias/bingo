from src.bingo import carton
from src.bingo import columnas_con_una_celda_ocupada

def test_columnas_con_una_celda_ocupada():
    mi_carton = carton()
    assert columnas_con_una_celda_ocupada(mi_carton)
