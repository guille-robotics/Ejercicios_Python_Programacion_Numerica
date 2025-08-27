import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: -np.cos(t) + np.sin(y)
h = 0.1
t = np.arange(0, 5+h, h)

# Euler
y_e = np.zeros_like(t)
y_e[0] = 1.0
for n in range(len(t)-1):
    y_e[n+1] = y_e[n] + h*f(t[n], y_e[n])

# Heun
y_h = np.zeros_like(t)
y_h[0] = 1.0
for n in range(len(t)-1):
    y_t = y_h[n] + h*f(t[n], y_h[n])                           # predictor
    y_h[n+1] = y_h[n] + (h/2)*(f(t[n], y_h[n]) + f(t[n+1], y_t))  # corrector

plt.figure()
plt.plot(t, y_e, 'o-', label="Euler")
plt.plot(t, y_h, 's-', label="Heun")
plt.title("Comparación Euler vs Heun")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()

# Comentario simple:
err_aprox = np.linalg.norm(y_h - y_e, ord=np.inf)
print(f"Diferencia máx. (Heun vs Euler): {err_aprox:.4e} (Heun suele ser más preciso).")
