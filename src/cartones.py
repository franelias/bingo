import random
import math

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

    for x in range(3):
        huecos = 0
        for y in range(9):
            if carton[x][y] == 0:
                huecos += 1
        if huecos == 3:
            return intentoCarton()

    return carton

def imprimirCarton(carton):
    print('\n')
    for fila in range(3):
        for columna in range(9):
            print(carton[fila][columna],end=' ')
        print('\n')

imprimirCarton(intentoCarton())
