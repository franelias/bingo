from src.bingo import carton
from src.bingo import posicion_numeros_en_columna

def test_posicion_numeros_en_columna():
    mi_carton = carton()
    assert posicion_numeros_en_columna(mi_carton)
