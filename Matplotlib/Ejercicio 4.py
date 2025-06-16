import numpy as np
import matplotlib.pyplot as plt

# Configurar el estilo (opcional)
plt.style.use('ggplot')

# 1. Crear datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/5) * np.sin(x)
y4 = np.random.normal(size=100).cumsum()

# 2. Crear figura con subgráficos
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Ejemplo de Subgráficos', fontsize=16, y=1.02)

# 3. Primer subgráfico: Línea simple
axs[0, 0].plot(x, y1, color='royalblue', linewidth=2)
axs[0, 0].set_title('Función Seno')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')
axs[0, 0].grid(True)

# 4. Segundo subgráfico: Línea con marcadores
axs[0, 1].plot(x, y2, 'o-', color='crimson', markersize=4, label='cos(x)')
axs[0, 1].set_title('Función Coseno con Marcadores')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('cos(x)')
axs[0, 1].legend()
axs[0, 1].grid(True)

# 5. Tercer subgráfico: Función amortiguada
axs[1, 0].plot(x, y3, color='forestgreen', linestyle='--', linewidth=2)
axs[1, 0].set_title('Seno Amortiguado Exponencialmente')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('e^(-x/5)*sin(x)')
axs[1, 0].grid(True)

# 6. Cuarto subgráfico: Random walk
axs[1, 1].plot(y4, color='darkorange', linewidth=2)
axs[1, 1].set_title('Random Walk (Camino Aleatorio)')
axs[1, 1].set_xlabel('Paso')
axs[1, 1].set_ylabel('Valor Acumulado')
axs[1, 1].grid(True)

# 7. Ajustar espacio entre subgráficos
plt.tight_layout()

# 8. Mostrar la figura
plt.show()