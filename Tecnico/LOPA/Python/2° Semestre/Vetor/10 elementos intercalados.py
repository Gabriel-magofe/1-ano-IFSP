# 10) Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
import random as r
A=[]
R= r.randint(1,100)
for i in range(R):
    A.append(r.randint(1, 100))
B=[]
for i in range(R):
    B.append(r.randint(1, 100))
C=[]
for i in range(R):
    C.append(A[i])
    C.append(B[i])

print("A:", A)
print("B:", B)
print("A e B intercalados:", C)