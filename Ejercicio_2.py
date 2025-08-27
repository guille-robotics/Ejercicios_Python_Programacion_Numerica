import numpy as np

arr = np.arange(1, 101)
suma_for = 0
for x in arr:
    suma_for += x

suma_np = np.sum(arr)
print("Suma con for:", suma_for)
print("Suma con np.sum:", suma_np)
