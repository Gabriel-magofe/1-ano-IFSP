import matplotlib.pyplot as plt
o=float(input("valor original do produto: "))
a=float(input("porcentagem de acrescimo: "))
vf=a+a/100*o
print("valor final: ",vf)
v=[o,vf]
label=["valor de custo", "valor de venda"]
plt.bar(label, v)
plt.title("valor de custo x valor de venda")
plt.ylabel("valor(R$:)")
plt.show()
