from src.bingo import carton
from src.bingo import matriz_3x9

def test_matrix_3x9():
    mi_carton = carton()
    assert matriz_3x9(mi_carton)
