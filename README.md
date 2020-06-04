# Bingo
[![Build Status](https://travis-ci.com/franelias/bingo.svg?branch=master)](https://travis-ci.com/franelias/bingo)
[![Coverage Status](https://coveralls.io/repos/github/franelias/bingo/badge.svg?branch=master)](https://coveralls.io/github/franelias/bingo?branch=master)

Proyecto realizado para la materia Adaptación del ambiente de trabajo, de la Tecnicatura en Informatica Profesional y Personal, del 6to año del Instituto Politecnico Superior de Rosario.

## Descripción general

El mismo se basa en el juego de bingo tradicional de 90 bolas. A través del uso de Python, se genera un cartón válido para su uso, según las siguientes condiciones:
- Los números del carton se encuentran en el rango 1 a 90.
- No hay números repetidos en el carton.
- Cada fila de un carton tiene exactamente 5 celdas ocupadas.
- Cada carton es una matrix de 3 x 9.
- Cada carton tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
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

## Testeo
El proyecto cuenta con una serie de tests que validan cada una de las condiciones antes mencionadas que debe cumplir un cartón. os mismos se encuentran en la carpeta `tests` del repositorio.

Para ejecutarlos, se requiere la herramienta `pytest`. La instalación del mismo se hace a través de la herramienta `pip`
```
pip install -U pytest
```
Ya instalado, basta con correrlo para ver la ejecución de los tests con el comando
```
pytest
```
