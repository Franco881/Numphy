import numpy as np
from scipy import linalg

# 1. Definir matrices de ejemplo
A = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 5]])
B = np.array([[1, 4, 2], [3, 1, 5], [6, 2, 8]])

print("=== Operaciones con Matrices ===")
print("\nMatriz A:")
print(A)
print("\nMatriz B:")
print(B)

# 2. Multiplicación de matrices
mult = np.dot(A, B)
print("\nMultiplicación A*B:")
print(mult)

# 3. Matriz inversa
try:
    inv_A = linalg.inv(A)
    print("\nInversa de A:")
    print(inv_A)
except np.linalg.LinAlgError:
    print("\nLa matriz A no tiene inversa (es singular)")

# 4. Resolver sistema de ecuaciones (Ax = b)
b = np.array([8, 5, 7])
print("\nSistema de ecuaciones Ax = b, donde b =", b)
x = linalg.solve(A, b)
print("Solución x:", x)

# 5. Verificación de la solución
print("\nVerificación (A*x debería ser igual a b):")
print("A*x =", np.dot(A, x))

# 6. Determinante
det_A = linalg.det(A)
print("\nDeterminante de A:", det_A)

# 7. Autovalores y autovectores
eigenvalues, eigenvectors = linalg.eig(A)
print("\nAutovalores de A:", eigenvalues)
print("\nAutovectores de A:")
print(eigenvectors)