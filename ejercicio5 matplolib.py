import numpy as np
import matplotlib.pyplot as plt

def graficar_dos_frecuencias(f1=10, f2=100):
    t = np.linspace(0, 0.5, 1000)
    y = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    plt.style.use('ggplot')  # Estilo con fondo gris
    plt.plot(t * 1000, y, label='Señal', color='brown')  # Convertimos a milisegundos
    plt.title('Dos frecuencias')
    plt.xlabel('Tiempo (t)')
    plt.legend()
    plt.show()

graficar_dos_frecuencias()
