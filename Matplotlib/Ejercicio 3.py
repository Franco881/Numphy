import numpy as np
import matplotlib.pyplot as plt

# Verificar estilos disponibles y usar uno compatible
print("Estilos disponibles:", plt.style.available)
plt.style.use('ggplot')  # Usamos 'ggplot' que es comúnmente disponible

# 1. Generar datos aleatorios
np.random.seed(42)  # Para reproducibilidad
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(10, 500, size=50)  # Tamaños aleatorios
colors = np.random.rand(50)  # Valores para el mapa de colores

# 2. Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    x, y, 
    s=sizes,          # Tamaño de los puntos
    c=colors,         # Valores para el color
    cmap='viridis',   # Mapa de colores
    alpha=0.7,        # Transparencia
    edgecolors='black' # Borde de los puntos
)

# 3. Personalizar el gráfico
plt.title('Gráfico de Dispersión con Tamaño y Color Variables', fontsize=14)
plt.xlabel('Eje X', fontsize=12)
plt.ylabel('Eje Y', fontsize=12)

# 4. Añadir barra de colores
cbar = plt.colorbar(scatter)
cbar.set_label('Intensidad del Color', fontsize=12)

# 5. Mostrar el gráfico
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()