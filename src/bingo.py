
def carton():
    carton = (
        (5,10,0,0,44,0,62,70,0),
        (0,16,0,37,47,0,0,76,81),
        (7,0,21,39,0,58,0,0,90)
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
    for x in range(9):
        if carton[0][x] == 0 and carton[1][x] == 0 and carton[2][x] == 0:
            return False

    return True

def revisar_filas_ocupadas(carton):
    for x in range(3):
        if contar_celdas_por_fila(carton,x) == 0:
            return False

    return True

def validar_numeros_carton(carton):
    for fila in carton:
        for celda in fila:
            if celda <> 0 and (celda > 90 or celda < 0):
                return False

    return True

def posicion_numeros_izquierda_a_derecha(carton):
    for x in range(3):
        posicion1 = 0
        posicion2 = 9
        for y in range(9):
            if carton [x][y] <> 0:
                if not(carton[x][y] >= posicion1 and carton[x][y] <= posicion2):
                    return False
            posicion1 += 10
            posicion2 += 10
            if posicion2 == 89:
                posicion2 += 1

    return True
