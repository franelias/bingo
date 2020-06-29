from src.bingo import *

#Función que imprime un cartón
def imprimirCarton(carton):
    for fila in range(3):
        for columna in range(9):
            print(carton[fila][columna],end=' ')
        print('\n')

imprimirCarton(carton())
