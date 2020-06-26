# Bingo
[![Build Status](https://travis-ci.com/franelias/bingo.svg?branch=master)](https://travis-ci.com/franelias/bingo)
[![Coverage Status](https://coveralls.io/repos/github/franelias/bingo/badge.svg?branch=master)](https://coveralls.io/github/franelias/bingo?branch=master)

Proyecto realizado para la materia Adaptación del Ambiente de Trabajo, de la Tecnicatura en Informática Profesional y Personal, del 6to año del Instituto Politécnico Superior de Rosario.

## Descripción general

El mismo se basa en el juego de bingo tradicional de 90 bolas. A través del uso de Python, se genera un cartón válido para su uso, según las siguientes condiciones:
- Los números del cartón se encuentran en el rango 1 a 90.
- Cada columna de un cartón (contando de izquierda a derecha) contiene números que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
- No hay números repetidos en el cartón.
- Cada fila de un cartón tiene exactamente 5 celdas ocupadas.
- Cada cartón es una matriz de 3 x 9.
- Cada cartón tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacías.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada cartón debe tener 3 y solo 3 columnas con solo una celda ocupada.
- En una fila no existen más de dos celdas vacías consecutivas.
- En una fila no existen más de dos celdas ocupadas consecutivas.


## Uso
El programa utiliza para su ejecución `Python 3`, y para su ejecución, se requieren los siguientes pasos:
- Clonar el repositorio
```
git clone https://github.com/franelias/bingo.git
```
- Ejecutar el programa
```
python src/bingo.py
```
Aclaración: en distros basadas en `Debian`, vease `Ubuntu` por ejemplo, se debe ejecutar el programa usando `python3` en lugar de `python`, para usar la version 3.x del mismo.

## Resultado
El resultado de ejecutar el programa es un cartón valido como el siguiente:
```
5 10 0 30 0 51 61 0 0

8 14 0 32 0 0 67 0 84

0 0 21 0 48 55 0 71 85
```
En el, cada celda puede tener dos formas, una representada con un 0, celda vacía, o con un número mayor a este, que indica que no esta vacía y posee el valor que le corresponde.
