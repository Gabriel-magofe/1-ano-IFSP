import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*2 +1

def g(x):
    return -x +3

a = plt.axes()
a.set_xlabel("X")
a.set_ylabel("Y")
a.set(xlim=(-2,2), ylim=(-4,4))

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.axis("equal")


x=np.linspace(-10,10,100)
y=f(x)
plt.plot(x, y)
y=g(x)
plt.plot(x, y)
plt.show()