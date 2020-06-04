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
            if celda != 0 and (celda > 90 or celda < 0):
                return False

    return True

def posicion_numeros_izquierda_a_derecha(carton):
    numeros =  [
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0]
    ]

    pos = [0] * 15

    for x in range(9):
        for y in range(3):
            numeros[x][y] = carton[y][x]
        numeros[x] = sorted(numeros[x])

    con = 0

    for x in range(9):
        for y in range(3):
            if numeros[x][y] != 0:
                pos[con] = numeros[x][y]
                con += 1

    for x in range(14):
        if pos[x] > pos[x+1]:
            return False

    return True

def posicion_numeros_en_columna(carton):
    for x in range(9):
        if ((carton[0][x] != 0 and carton[1][x] != 0) and (carton[0][x] > carton[1][x])) or ((carton[1][x] != 0 and carton[2][x] != 0) and (carton[1][x] > carton[2][x])) or ((carton[0][x] != 0 and carton[2][x] != 0) and (carton[0][x] > carton[2][x])):
            return False

    return True

def numeros_sin_repetir(carton):
    repe = [0] * 91
    for fila in carton:
        for celda in fila:
            if celda != 0:
                if repe[celda] == 0:
                    repe[celda] += 1
                else:
                    return False

    return True

def matriz_3x9(carton):
    filas = len(carton)

    for fila in range(3):
        columnas = 0
        columnas += len(carton[fila])
        if columnas != 9:
            return False

    return filas == 3 and columnas == 9

def fila_5_celdas_ocupadas(carton):
    for fila in carton:
        con = 0
        for celda in fila:
            if celda != 0:
                con += 1
        if con != 5:
            return False

    return True

def columnas_vacias(carton):
    for x in range(9):
        if carton[0][x] == 0 and carton[1][x] == 0 and carton[2][x] == 0:
            return False

    return True

posicion_numeros_izquierda_a_derecha(carton())
