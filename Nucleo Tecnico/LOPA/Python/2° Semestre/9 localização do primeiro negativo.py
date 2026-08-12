# 9) Dado um vetor de N números, imprimir a localização do primeiro número negativo, se houver.
import random

A = []
R= random.randint(1,100)
for i in range(R):
    A.append(random.randint(-100, 100))

print("Vetor A:", A)

for i in range(len(A)):
    if A[i] < 0:
        print("Localização do primeiro número negativo:", i)
        break
else:
    print("Nenhum número negativo encontrado.")