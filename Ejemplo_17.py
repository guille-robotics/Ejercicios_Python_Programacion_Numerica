import numpy as np
import matplotlib.pyplot as plt

r, K = 0.1, 1000.0
f = lambda t, P: r*P*(1 - P/K)

h = 0.5
t = np.arange(0, 50+h, h)
P = np.zeros_like(t)
P[0] = 10.0

for n in range(len(t)-1):
    P[n+1] = P[n] + h*f(t[n], P[n])

plt.figure()
plt.plot(t, P)
plt.title("Crecimiento logístico (Euler)")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.grid(True)
plt.show()
