import numpy as np
import matplotlib.pyplot as plt

K, A, r = 100, 10, 0.5
t = np.linspace(0, 20, 400)
P = K / (1 + A*np.exp(-r*t))

plt.figure()
plt.plot(t, P)
plt.title("Función logística")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.grid(True)
plt.show()
