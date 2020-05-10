from src.bingo import carton
from src.bingo import numeros_sin_repetir

def test_numeros_repetidos():
    mi_carton = carton()
    assert numeros_sin_repetir(mi_carton)
