# 17) Elaborar um programa que leia uma matriz A do tipo vetor com 20 elementos inteiros. Construir uma matriz B dos mesmos tipos e dimensão da matriz A, sendo cada elemento da matriz B o somatório de 1 até o valor do elemento correspondente armazenado na matriz A. Se o valor do elemento da matriz A[1] for 5, o elemento correspondente da matriz B[1] deve ser 15, pois o somatório do elemento da matriz A é 1 + 2 + 3 + 4 + 5. Apresentar os elementos da matriz B.
import random as r
def somatorio(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma
A = [0] * 20
for i in range(20):
    A[i] = r.randint(1, 10)
print("Matriz A:", A)
B = [0] * 20
for i in range(20):
    B[i] = somatorio(A[i])
print("Somatória de cada valor:", B)