from src.bingo import carton
from src.bingo import columnas_llenas

def test_columnas_llenas():
    mi_carton = carton()
    assert columnas_llenas(mi_carton)
