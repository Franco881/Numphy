import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
f = np.exp(-x**2)

plt.plot(x, f, 'r--', linewidth=2, label=r'$e^{-x^2}$')
plt.title('Función ')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend()

plt.show()