import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Cargar datos (asumiendo estructura: primera columna días, segunda columna casos)
# data = np.loadtxt('covid.txt')  # Descomentar cuando tengas el archivo
# Para este ejemplo, crearé datos sintéticos
dias = np.linspace(0, 100, 50)
casos = 50 * np.exp(0.05 * dias) + np.random.normal(0, 20, size=len(dias))

# 2. Definir función polinómica para el ajuste
def polinomio(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

# 3. Ajuste polinómico de grado 3
params, cov = curve_fit(polinomio, dias, casos)

# 4. Generar curva ajustada
dias_ajuste = np.linspace(min(dias), max(dias), 100)
casos_ajuste = polinomio(dias_ajuste, *params)

# 5. Visualización
plt.figure(figsize=(10, 6))
plt.scatter(dias, casos, label='Datos reales', color='blue')
plt.plot(dias_ajuste, casos_ajuste, label='Ajuste polinómico', color='red')
plt.title('Ajuste Polinómico a Datos COVID', fontsize=14)
plt.xlabel('Días desde inicio', fontsize=12)
plt.ylabel('Número de casos', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Coeficientes del polinomio
print(f"Polinomio ajustado: {params[0]:.4f}x³ + {params[1]:.4f}x² + {params[2]:.4f}x + {params[3]:.4f}")