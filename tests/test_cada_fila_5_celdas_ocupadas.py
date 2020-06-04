from src.bingo import carton
from src.bingo import fila_5_celdas_ocupadas

def test_fila_5_celdas_ocupadas():
    mi_carton = carton()
    assert fila_5_celdas_ocupadas(mi_carton)
