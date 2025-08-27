import numpy as np
import matplotlib.pyplot as plt

Tamb, T0, k = 20.0, 100.0, 0.1  # min^-1
# tiempo cuando T(t)=25
t25 = -np.log((25 - Tamb)/(T0 - Tamb))/k
t = np.linspace(0, t25, 400)
T = Tamb + (T0 - Tamb)*np.exp(-k*t)

print(f"Alcanza 25°C en t ≈ {t25:.2f} min")

plt.figure()
plt.plot(t, T)
plt.axhline(25, linestyle="--")
plt.title("Ley de enfriamiento de Newton")
plt.xlabel("t [min]")
plt.ylabel("T(t) [°C]")
plt.grid(True)
plt.show()
