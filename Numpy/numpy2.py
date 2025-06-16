import numpy as np

# Crear un vector de 10 elementos, siendo los impares (índices 1, 3, 5...) igual a 1 y los pares (índices 0, 2, 4...) igual a 2
vector = np.zeros(10, dtype=int)
vector[::2] = 2  # Posiciones pares: 0, 2, 4, 6, 8
vector[1::2] = 1  # Posiciones impares: 1, 3, 5, 7, 9
print("Vector con pares=2 e impares=1:\n", vector)

# Crear un tablero de ajedrez 8x8, con 1 en las casillas negras y 0 en las blancas
tablero = np.zeros((8, 8), dtype=int)
tablero[1::2, ::2] = 1  # Filas impares, columnas pares
tablero[::2, 1::2] = 1  # Filas pares, columnas impares
print("\nTablero de ajedrez 8x8:\n", tablero)