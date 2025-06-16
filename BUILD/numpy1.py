import numpy as np

# Crear un array 7x8 lleno de ceros de tipo entero
array_zeros = np.zeros((7, 8), dtype=int)
print("Array de ceros:\n", array_zeros)

# Crear un array 7x8 lleno de ceros salvo la primera fila que serán todo unos
array_primera_fila_unos = np.zeros((7, 8), dtype=int)
array_primera_fila_unos[0] = 1
print("\nPrimera fila unos:\n", array_primera_fila_unos)

# Crear un array 7x8 lleno de ceros salvo la última fila que será el rango entre 5 y 8
# Nota: El rango entre 5 y 8 tiene 8 elementos si consideramos np.linspace(5, 8, 8)
# Pero si queremos números enteros consecutivos, usamos np.arange(5, 13)
array_ultima_fila_rango = np.zeros((7, 8), dtype=int)
array_ultima_fila_rango[-1] = np.arange(5, 13)  # Desde 5 hasta 12 inclusive
print("\nÚltima fila con rango 5 a 12:\n", array_ultima_fila_rango)