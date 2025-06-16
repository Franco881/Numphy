
import numpy as np
import matplotlib.pyplot as plt

x = [np.linspace(-2, 2), np.linspace(-2, 4), np.linspace(1, 10)]
f = [np.sin, lambda x: np.exp(3*x), lambda x: 1/x]

plt.figure(figsize=(12, 4))
for i, (xi, fi) in enumerate(zip(x, f), 1):
    plt.subplot(1, 3, i)
    plt.plot(xi, fi(xi))
    plt.grid(True)
plt.tight_layout()
plt.show()