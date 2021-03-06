import random
import math

#Función que genera un cartón, que puede ser valido o no
def intentoCarton():
    con = 0
    carton = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    numerosCarton = 0

    while numerosCarton < 15:
        con += 1
        if con == 50:
            return intentoCarton()

        numero = random.randint(1 , 90)
        columna = math.floor(numero / 10)

        if columna == 9:
            columna = 8

        huecos = 0

        for i in range(3):
            if carton[i][columna] == 0:
                huecos += 1

            if carton[i][columna] == numero:
                huecos = 0
                break

        if huecos < 2:
            continue

        fila = 0

        for j in range(3):
            huecos = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    huecos += 1

            if huecos < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break

        if fila == 3:
            continue

        carton[fila][columna] = numero
        numerosCarton += 1
        con = 0

    return carton

#Funcion que genera un cartón valido
def carton():
    while True:
        carton = intentoCarton()
        if validar_quince_numeros(carton) and validar_menos_quince_numeros(carton) and validar_mas_quince_numeros(carton) and revisar_columnas_ocupadas(carton) and revisar_filas_ocupadas(carton) and validar_numeros_carton(carton) and posicion_numeros_izquierda_a_derecha(carton) and posicion_numeros_en_columna(carton) and numeros_sin_repetir(carton) and matriz_3x9(carton) and fila_5_celdas_ocupadas(carton) and columnas_vacias(carton) and columnas_llenas(carton) and columnas_con_una_celda_ocupada(carton) and filas_2_celdas_consecutivas_vacias_o_ocupadas(carton):
            break

    return carton

#Valida si hay 15 celdas ocupadas
def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1

    return celdas_vacias == 12

#Valida si hay menos de 15 o 15 celdas ocupadas
def validar_menos_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1

    return celdas_vacias <= 12

#Valida si hay mas de 15 o 15 celdas ocupadas
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

#Valida si no hay columnas vacías en un cartón
def revisar_columnas_ocupadas(carton):
    for x in range(9):
        if carton[0][x] == 0 and carton[1][x] == 0 and carton[2][x] == 0:
            return False

    return True

#Valida que no haya filas vacías por cartón
def revisar_filas_ocupadas(carton):
    for x in range(3):
        if contar_celdas_por_fila(carton,x) == 0:
            return False

    return True

#Valida si los números del cartón estan entre 1 y 90
def validar_numeros_carton(carton):
    for fila in carton:
        for celda in fila:
            if celda > 91 or celda < 0:
                return False

    return True

#Valida si en cada columna, los numeros van aumentando por decenas
def posicion_numeros_izquierda_a_derecha(carton):
    posicion1 = [1,10,20,30,40,50,60,70,80]
    posicion2 = [9,19,29,39,49,59,69,79,90]

    for x in range(3):
        for y in range(9):
            if carton[x][y] != 0:
                if not (carton[x][y] >= posicion1[y] and carton[x][y] <= posicion2[y]):
                    return False
    return True

#Valida si los números de una columna aumentan de mayor a menor de arriba para abajo
def posicion_numeros_en_columna(carton):
    list = []
    for x in range(9):
        list = []
        for y in range(3):
            if carton[y][x] != 0:
                list.append(carton[y][x])

        if len(list) > 1 and list != sorted(list):
            return False

    return True

#Valida que no haya numeros repetidos en un cartón
def numeros_sin_repetir(carton):
    set = {0}
    for fila in carton:
        for celda in fila:
            set.add(celda)

    return len(set) == 16

#Valida que el cartón sea de 3 x 9
def matriz_3x9(carton):
    filas = len(carton)

    columnas = 0

    for fila in range(3):
        columnas = 0
        columnas += len(carton[fila])
        if columnas != 9:
            return False

    return filas == 3 and columnas == 9

#Valida que por fila, solo haya 5 celdas ocupadas
def fila_5_celdas_ocupadas(carton):
    for fila in carton:
        con = 0
        for celda in fila:
            if celda != 0:
                con += 1
        if con != 5:
            return False

    return True

#Valida que no haya columnas vacias en el cartón
def columnas_vacias(carton):
    for x in range(9):
        if carton[0][x] == 0 and carton[1][x] == 0 and carton[2][x] == 0:
            return False

    return True

#Valida que no haya columnas llenas en el cartón
def columnas_llenas(carton):
    for x in range(9):
        if carton[0][x] != 0 and carton[1][x] != 0 and carton[2][x] != 0:
            return False

    return True

#Valida que haya solo tres columnas con una celda ocupada
def columnas_con_una_celda_ocupada(carton):
    uno = 0

    for x in range(9):
        con = 0
        for y in range(3):
            if carton[y][x] != 0:
                con += 1
        if con == 1:
            uno += 1

    return uno == 3

#Valida que no haya filas con más de 2 celdas vacías consecutivas o con mas de 2 celdas ocupadas consecutivas
def filas_2_celdas_consecutivas_vacias_o_ocupadas(carton):
    set = {0}
    for x in range(3):
        for y in range(7):
            set = {0}
            set.add(carton[x][y])
            set.add(carton[x][y+1])
            set.add(carton[x][y+2])
            if len(set) == 1 or len(set) == 4:
                return False

    return True
