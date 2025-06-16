import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Puntos conocidos (datos de ejemplo)
x = np.array([0, 2, 3, 5])
y = np.array([1, 4, 0, 3])

# Crear el polinomio de Lagrange
poly = lagrange(x, y)

# Evaluar el polinomio en nuevos puntos
x_new = np.linspace(min(x)-1, max(x)+1, 100)
y_new = poly(x_new)

# Graficar resultados
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Puntos conocidos')
plt.plot(x_new, y_new, label='Polinomio de Lagrange')
plt.title('Interpolación con polinomios de Lagrange')
plt.legend()
plt.grid(True)
plt.show()