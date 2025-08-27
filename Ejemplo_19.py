import numpy as np
import matplotlib.pyplot as plt

w = 2.0
h = 0.01
t = np.arange(0, 2*np.pi + h, h)

x = np.zeros_like(t)
v = np.zeros_like(t)
x[0], v[0] = 1.0, 0.0

def fx(t, x, v):  # dx/dt = v
    return v

def fv(t, x, v):  # dv/dt = -w^2 x
    return -w**2 * x

for n in range(len(t)-1):
    # Predictor
    x_t = x[n] + h*fx(t[n], x[n], v[n])
    v_t = v[n] + h*fv(t[n], x[n], v[n])
    # Corrector
    x[n+1] = x[n] + (h/2)*(fx(t[n], x[n], v[n]) + fx(t[n+1], x_t, v_t))
    v[n+1] = v[n] + (h/2)*(fv(t[n], x[n], v[n]) + fv(t[n+1], x_t, v_t))

plt.figure()
plt.plot(t, x, label="x(t)")
plt.plot(t, v, label="v(t)")
plt.title("Oscilador armónico (Heun)")
plt.xlabel("t")
plt.legend()
plt.grid(True)
plt.show()
