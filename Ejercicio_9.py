import numpy as np
import matplotlib.pyplot as plt

h0, g = 100.0, 9.81
t_fin = np.sqrt(2*h0/g)
t = np.linspace(0, t_fin, 400)
h = h0 - 0.5*g*t**2

plt.figure()
plt.plot(t, h)
plt.title("Caída libre: altura vs tiempo")
plt.xlabel("t [s]")
plt.ylabel("h(t) [m]")
plt.grid(True)
plt.show()
