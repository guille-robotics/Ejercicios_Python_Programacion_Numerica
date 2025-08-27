import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: -2*y
h = 0.1
t = np.arange(0, 2+h, h)
y = np.zeros_like(t)
y[0] = 1.0

for n in range(len(t)-1):
    y[n+1] = y[n] + h*f(t[n], y[n])

y_exacta = np.exp(-2*t)

plt.figure()
plt.plot(t, y, 'o-', label="Euler")
plt.plot(t, y_exacta, label="Exacta e^{-2t}")
plt.title("Euler vs Exacta (y'=-2y)")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
