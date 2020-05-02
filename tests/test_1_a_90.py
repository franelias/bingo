from src.bingo import carton
from src.bingo import validar_numeros_carton

def test_validar_uno_a_noventa():
    mi_carton = carton()
    assert validar_numeros_carton(mi_carton)
