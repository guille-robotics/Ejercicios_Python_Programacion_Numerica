import numpy as np
import matplotlib.pyplot as plt

a, b, c = 2, -3, 1
x = np.arange(-5, 5.1, 0.1)
y = a*x**2 + b*x + c

plt.figure()
plt.plot(x, y)
plt.title("f(x) = 2x^2 - 3x + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
