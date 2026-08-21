    # 15) Elaborar um programa que leia uma matriz A do tipo vetor com 15 elementos inteiros. Construir uma matriz B de mesmo tipo, e cada elemento da matriz B deve ser o resultado da fatorial correspondente de cada elemento da matriz A. Apresentar as matrizes A e B.

# def fatorial(n):
#     r = 1
#     i = n
#     if n == 0: 
#         return 1
#     else:
#         while i>=1:
#             r *= i
#             i-=1
#     return r
# print(fatorial(5))
import random as r

def fatorial(n):
    if n == 0: 
        return 1
    else:
        n1=n    
        r=1
        nn = []
        nn.append(n)
        while n!=0:
            n=n-1
            nn.append(n)

        for i in range(n1):
            r=r*nn[i]

        return r
A=[]
B=[0]*15
for i in range(15):
    A.append(r.randint(0, 10))
for i in range(15):
    B[i]=fatorial(A[i])
print("Vetor A= \n\n")
print(A, "\n\n")
print("Vetor A fatorial=\n\n")
print(B, "\n\n")
