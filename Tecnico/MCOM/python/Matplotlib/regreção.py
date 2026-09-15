import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5,6,7,8])
y=np.array([37, 66, 83, 95, 103, 104, 110, 113])
a,b = np.polyfit(x,y, deg=1)
y_pred = a * x + b
delta = y - y_pred
sq_res=np.sum(delta**2)
sq_tot=np.sum((y-np.mean(y))**2)
r2=1-(sq_res/sq_tot)
texto=f"$y={a:.2f}x + {b:.2f}$\n$R^2 = {r2:.4f}$"
plt.text(x,y, texto, fontsize=18, bbox=dict(facecolor='white'))
plt.show()