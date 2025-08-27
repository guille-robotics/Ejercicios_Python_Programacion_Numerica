import numpy as np
import matplotlib.pyplot as plt

theta0, L, g = 0.2, 1.0, 9.81
w0 = np.sqrt(g/L)
T = 2*np.pi/np.sqrt(g/L)

t = np.linspace(0, 3*T, 800)
theta = theta0*np.cos(w0*t)

print(f"Período aproximado: T = {T:.4f} s")

plt.figure()
plt.plot(t, theta)
plt.title("Péndulo simple (aprox. pequeños ángulos)")
plt.xlabel("t [s]")
plt.ylabel("θ(t) [rad]")
plt.grid(True)
plt.show()
