pm1 = float(input("Digite o valor da placa de mãe do pc 1: R$: "))
gpu1 = float(input("digite o valor da placa de video do pc 1: R$: "))
ram1 = float(input("Digite o valor da memoria ram do pc 1: R$: "))
ssd1 = float(input("Digite o valor do ssd do pc 1: R$:"))
pro1 = float(input("Digite o valor do processador do pc 1: R$: "))

t1 = pm1 + gpu1 + ram1 + ssd1 + pro1
if (pm1>=579.99 and gpu1>=1469.99 and ram1>=1238 and ssd1>=429.90 and pro1>=899.99):
    print("\n\nO seu pc roda gta V Liso\n\n")
else:
    print("\n\nO seu pc é fraco para rodar gta V\n\n")

pm2 = float(input("Digite o valor da placa de mãe do pc 2: R$: "))
gpu2 = float(input("digite o valor da placa de video do pc 2: R$: "))
ram2 = float(input("Digite o valor da memoria ram do pc 2: R$: "))
ssd2 = float(input("Digite o valor do ssd do pc 2: R$: "))
pro2 = float(input("Digite o valor do processador do pc 2: R$: "))

t2 = pm2 + gpu2 + ram2 + ssd2 + pro2
if (pm2>=579.99 and gpu2>=1469.99 and ram2>=1238 and ssd2>=429.90 and pro2>=899.99):
    print("\n\nO seu pc roda CS 2 liso\n\n")
else:
    print("\n\nO seu pc é fraco para rodar CS 2\n\n")

pm3 = float(input("Digite o valor da placa de mãe do pc 3: R$: "))
gpu3 = float(input("digite o valor da placa de video do pc 3: R$: "))
ram3 = float(input("Digite o valor da memoria ram do pc 3: R$: "))
ssd3 = float(input("Digite o valor do ssd do pc 3: R$: "))
pro3 = float(input("Digite o valor do processador do pc 3: R$: "))

t3 = pm3 + gpu3 + ram3 + ssd3 + pro3
if (pm3>=369.99 and gpu3>=2699.99 and ram3>=1238 and ssd3>=429.90 and pro3>=2699.99):
    print("\n\nO seu pc roda Minecraft Liso\n\n")
else:
    print("\n\nO seu pc é fraco para rodar Minecraft\n\n")

print("///////////////////////////////////////////////////////////////////\n\n")

tp1 = t1+(t1/100*15)
tp2 = t2+(t2/100*15)
tp3 = t3+(t3/100*15)

if (t1 < t2 and t1 < t3): 
    print("O pc 1 é o mais barato a vista com o valor de: R$: ", t1)
elif (t2 < t1 and t2 < t3):
    print("O pc 2 é o mais barato a vista com o valor de: R$: ", t2) 
elif (t3 < t1 and t3 < t2):
    print("O pc 3 é o mais barato a vista com o valor de: R$: ", t3)
else:
    print("Os pcs tem o mesmo valor a vista: R$: ", t1)

if (tp1 < tp2 and tp1 < tp3):
    print("\n\nO pc 1 é o mais barato parcelado com o valor de: R$: ", tp1)
elif (tp2 < tp1 and tp2 < tp3):
    print("\n\nO pc 2 é o mais barato parcelado com o valor de: R$: ", tp2)
elif (tp3 < tp1 and tp3 < tp2):
    print("\n\nO pc 3 é o mais barato parcelado com o valor de: R$: ", tp3)
else:
    print("\n\nOs pcs tem o mesmo valor parcelado: R$: ", tp1)

if (t1>t2 and t1>t3):
    print("\n\nO pc 1 é o mais caro a vista com o valor de: R$: ", t1)
elif (t2>t1 and t2>t3):
    print("\n\nO pc 2 é o mais caro a vista com o valor de: R$: ", t2)
elif (t3>t1 and t3>t2):
    print("\n\nO pc 3 é o mais caro a vista com o valor de: R$: ", t3)
else:
    print("\n\nOs pcs tem o mesmo valor a vista: R$: ", t1)

if (tp1>tp2 and tp1>tp3):
    print("\n\nO pc 1 é o mais caro parcelado com o valor de: R$: ", tp1)
elif (tp2>tp1 and tp2>tp3):
    print("\n\nO pc 2 é o mais caro parcelado com o valor de: R$: ", tp2)
elif (tp3>tp1 and tp3>tp2):
    print("\n\nO pc 3 é o mais caro parcelado com o valor de: R$: ", tp3)
else:
    print("\n\nOs pcs tem o mesmo valor parcelado: R$: ", tp1)

m=(t1+t2+t3)/3
print("\n\nO valor médio dos pcs a vista é: R$: ", m)
mp=(tp1+tp2+tp3)/3
print("\n\nO valor médio dos pcs parcelados é: R$: ", mp)
