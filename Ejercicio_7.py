import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
y1 = np.exp(x)
y2 = np.exp(2*x)
y3 = np.exp(-x)

plt.figure()
plt.plot(x, y1, label="e^x")
plt.plot(x, y2, label="e^{2x}")
plt.plot(x, y3, label="e^{-x}")
plt.title("Comparación exponenciales")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.show()

print("La que crece más rápido para x→+∞ es e^{2x}.")
