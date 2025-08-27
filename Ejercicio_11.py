import numpy as np
import matplotlib.pyplot as plt

Q0, R, C = 1000.0, 10000.0, 100e-6  # tau = 1 s
tau = R*C
t = np.linspace(0, 10*tau, 400)
Q = Q0*np.exp(-t/tau)

plt.figure()
plt.plot(t, Q)
plt.title("Descarga de capacitor: Q(t)")
plt.xlabel("t [s]")
plt.ylabel("Q(t) [C]")
plt.grid(True)
plt.show()
