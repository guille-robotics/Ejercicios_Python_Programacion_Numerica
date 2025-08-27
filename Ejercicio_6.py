import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y1, y2, y3 = np.sin(x), np.cos(x), np.tan(x)

plt.figure()
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.plot(x, y3, label="tan(x)")
plt.ylim(-10, 10)  # acota la tangente para visualizar
plt.title("Funciones trigonométricas")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.show()
