import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y - t
h = 0.1
t = np.arange(0, 1+h, h)
y = np.zeros_like(t)
y[0] = 1.0

for n in range(len(t)-1):
    # Predictor (Euler)
    y_tilde = y[n] + h*f(t[n], y[n])
    # Corrector (promedio pendientes)
    y[n+1] = y[n] + (h/2)*(f(t[n], y[n]) + f(t[n+1], y_tilde))

plt.figure()
plt.plot(t, y, 'o-')
plt.title("Método de Heun: y' = y - t")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.show()
