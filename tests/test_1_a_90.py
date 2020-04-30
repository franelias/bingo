from src.bingo import carton

def test_validar_uno_a_noventa():
    mi_carton = carton()
    for fila in mi_carton:
        for celda in fila:
            if celda <> 0 and (celda > 90 or celda < 0):
                assert False

    assert True
