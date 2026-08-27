# 12) Elaborar um programa que efetue a leitura de dez valores para uma matriz A do tipo vetor. Mostre a quantidade de valores positivos e negativos.
A = []
n=0
p=0
zeros=0
for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    A.append(valor)
for i in range(10):
    if A[i]>0:
        p=p+1
    elif A[i]<0:
        n=n+1
    else:
        zeros=zeros+1

print(f"Quantidade de positivos: {p}")
print(f"Quantidade de negativos: {n}")
print(f"Quantidade de zeros: {zeros}")