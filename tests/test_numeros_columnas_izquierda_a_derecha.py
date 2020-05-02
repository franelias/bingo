from src.bingo import carton
from src.bingo import posicion_numeros_izquierda_a_derecha

def test_posicion_numeros_izquierda_a_derecha():
    mi_carton = carton()
    assert posicion_numeros_izquierda_a_derecha(mi_carton)
