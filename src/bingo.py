
def carton():
    carton = (
        (5,10,0,0,44,0,62,70,0),
        (0,16,0,37,47,0,0,76,81),
        (7,0,21,39,0,58,0,0,89)
    )
    return carton

def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1

    return celdas_vacias == 12

def validar_menos_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1

    return celdas_vacias <= 12

def validar_mas_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1

    return celdas_vacias >= 12

#Funcion que cuenta las celdas ocupadas por fila
def contar_celdas_por_fila(carton, fila):
    contador = 0
    for x in range(9):
        contador = contador + carton[fila][x]

    return contador

def revisar_columnas_ocupadas(carton):
    ban = 0
    for x in range(9):
        if carton[0][x] == 0 and carton[1][x] == 0 and carton[2][x] == 0:
            return False

    return True

def validar_numeros_carton(carton):
    for fila in carton:
        for celda in fila:
            if celda <> 0 and (celda > 90 or celda < 0):
                return False

    return True
