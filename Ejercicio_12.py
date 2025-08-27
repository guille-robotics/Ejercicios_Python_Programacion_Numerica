import numpy as np
import matplotlib.pyplot as plt

Q0, R, C = 1000.0, 10000.0, 100e-6
tau = R*C
t = np.linspace(0, 10*tau, 400)
Q = Q0*np.exp(-t/tau)
I = -(Q0/tau)*np.exp(-t/tau)

plt.figure(figsize=(7,6))
plt.subplot(2,1,1)
plt.plot(t, Q)
plt.title("Descarga RC")
plt.ylabel("Q(t) [C]")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, I)
plt.xlabel("t [s]")
plt.ylabel("I(t) [A]")
plt.grid(True)
plt.show()
