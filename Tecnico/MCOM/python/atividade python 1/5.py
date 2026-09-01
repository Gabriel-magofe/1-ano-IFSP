import numpy as np
import matplotlib.pyplot as plt

zn= np.array([1.2, 1.5, 2.0, 1.8, 2.5, 1.1, 1.4, 3.0, 2.2, 1.7])
zs= np.array([3.5, 4.2, 2.8, 5.0, 1.9, 3.1, 6.5, 4.0, 3.8, 2.9])
h= np.concatenate((zn, zs))
m= np.mean(h)
s= np.sum(h)
print("Média: ", m, "\n", "Soma: ", s)
r = np.empty(zn.size + zs.size, dtype=zn.dtype)
r[0::2] = zn
r[1::2] = zs
g=len(r)
plt.figure(figsize=(8, 6))
plt.bar(range(g), r, color=['blue', 'red'], width=1, edgecolor='black')
plt.title("realidade socioeconômica")
plt.xlabel("Municípios")
plt.ylabel("Salários minimos")
plt.show()