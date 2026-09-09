#   4) Ler duas matrizes A e B, cada uma de duas dimensões com quatro linhas e três colunas. Construir uma matriz C de mesma dimensão, a qual é formada pela subtração dos elementos da matriz A com os elementos da matriz B. Apresentar a matriz C.
import random as r

A = [[r.randint(0, 100) for i in range(4)] for j in range(3)]
B = [[r.randint(0, 100) for i in range(4)] for j in range(3)]
C = [[0 for i in range(4)] for j in range(3)]

for i in range(3):
    for j in range(3):  
        C[i][j] = A[i][j] - B[i][j]

print(A)
print(B)
print(C)