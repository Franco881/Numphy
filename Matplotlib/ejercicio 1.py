Ejercicio1.py
import numpy as np
import matplotlib.pyplot as plt

# 1. Definir el dominio (valores de x)
x = np.linspace(-3, 3, 500)  # 500 puntos entre -3 y 3

# 2. Evaluar la función en el dominio
f = np.exp(-x**2)

# 3. Crear la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, f, 'b-', linewidth=2, label=r'$f(x) = e^{-x^2}$')

# 4. Personalizar la gráfica
plt.title('grafica de la funcion')
plt.xlabel('Eje x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 5. Mostrar la gráfica
plt.show()