from src.bingo import carton

#Carton valido generado por el programa
carton_valido = carton()

#Carton invalido generado a mano, en donde hay numeros repetidos,
#no hay 15 celdas ocupadas, no hay 27 celdas en total y donde los numeros no van del 1 al 90.
#Solo se usa para verificar que las funciones que verifican las celdas funcionan correctamente.
carton_invalido1 = [
    [0,0,23,34,0,55,61,0,93],
    [1,0,23,38,41,0,0,0,83],
    [0,16,0,0,40,0,63,0]
    ]

#Carton invalido con mas de 15 celdas ocupadas, solo se usa para verificar la funcion que verifica esta condición.
carton_invalido2 = [
    [0,0,23,34,0,55,61,0,93],
    [1,0,23,38,41,0,0,0,83],
    [0,16,23,16,40,82,63,0]
    ]

#Carton invalido que posee columnas totalmente vacias y llenas y numeros mal ordenarios.
carton_invalido3 = [
    [0,0,29,33,0,53,0,0,87],
    [1,0,21,34,44,57,0,0,86],
    [9,14,0,0,40,58,0,0,0]
]

#Carton invalido que posee filas con mas de dos celdas consecutivas vacias y ocupadas y filas vacias
carton_invalido4 = [
    [0,0,0,0,0,0,0,0,0],
    [7,11,25,0,0,0,0,77,87],
    [0,0,26,39,49,50,0,0,0]
]
