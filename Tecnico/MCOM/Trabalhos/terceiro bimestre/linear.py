import numpy as np
import matplotlib.pyplot as plt

T = np.array([
    [109, 138],
    [113, 145],
    [115, 137],
    [116, 141],
    [119, 135],
    [120, 145],
    [121, 135],
    [124, 140],
    [126, 149],
    [129, 148],
    [130, 148],
    [133, 149],
    [134, 144],
    [135, 149],
    [137, 152],
    [139, 151],
    [141, 155],
    [142, 150]
])
x = np.array([109, 113, 115, 116, 119, 120, 121, 124, 126, 129, 130, 133, 134, 135, 137, 139, 141, 142])
y = np.array([138, 145, 137, 141, 135, 145, 135, 140, 149, 148, 148, 149, 144, 149, 152, 151, 155, 150])

a,b = np.polyfit(x,y, deg=1)
y_pred = a * x + b 
delta = y - y_pred
sq_res=np.sum(delta**2)
sq_tot=np.sum((y-np.mean(y))**2)
r2=1-(sq_res/sq_tot)
texto=f"$y={a:.2f}x + {b:.2f}$\n$R^2 = {r2:.4f}$"
plt.text(a,b, texto, fontsize=18, bbox=dict(facecolor='white'))
plt.scatter(x, y)
plt.plot(x, y_pred, "-", label=texto,color="black")
plt.legend(loc="lower right", framealpha=0.9)
plt.show()

"""O R ao quadrado de 0,6288 não é bom, aprendemos em aula que quanto mais proximo de
1 mais proxima de uma aproximação perfeita ela é. 1 é perfeita, 0,8 é ok, o 0,6 já é ruim."""