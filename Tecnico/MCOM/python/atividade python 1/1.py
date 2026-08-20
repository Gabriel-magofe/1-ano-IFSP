import numpy as np
s1= np.array([210, 205, 190, 185, 220, 240])
s2= np.array([250, 260, 230, 210, 195, 200])
month=np.arange(start=1, stop=13, step=1)
a= np.concatenate((s1, s2))
ma= np.array([month, a])
b= np.sum(a)
c= np.mean(a)
print(ma, "\n", "Total: ", b, "\n", "Média: ", c)


