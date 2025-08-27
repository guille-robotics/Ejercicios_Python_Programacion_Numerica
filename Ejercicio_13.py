import numpy as np
import matplotlib.pyplot as plt

A, w, phi = 5.0, 2.0, np.pi/4
t = np.linspace(0, 10, 600)
x = A*np.cos(w*t + phi)
v = -A*w*np.sin(w*t + phi)

plt.figure()
plt.plot(t, x, label="x(t)")
plt.plot(t, v, label="v(t)")
plt.title("Movimiento Armónico Simple")
plt.xlabel("t [s]")
plt.legend()
plt.grid(True)
plt.show()
