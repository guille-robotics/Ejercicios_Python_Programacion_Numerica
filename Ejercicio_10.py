import numpy as np
import matplotlib.pyplot as plt

h0, g = 100.0, 9.81
t_fin = np.sqrt(2*h0/g)
t = np.linspace(0, t_fin, 400)
h = h0 - 0.5*g*t**2
v = -g*t

plt.figure(figsize=(7,6))
plt.subplot(2,1,1)
plt.plot(t, h)
plt.title("Caída libre")
plt.ylabel("h(t) [m]")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, v)
plt.xlabel("t [s]")
plt.ylabel("v(t) [m/s]")
plt.grid(True)
plt.show()
