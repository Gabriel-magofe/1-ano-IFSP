#  7) Elaborar um programa que leia uma matriz A de duas dimensões com cinco linhas e quatro colunas. Construir uma matriz B de mesma dimensão, em que elemento seja o fatorial de cada elemento correspondente armazenado na matriz A. Apresentar ao final as matrizes A e B.
import random as r
from math import factorial
A = [[r.randint(0, 10) for _ in range(4)] for _ in range(5)]
B = [[0]*4 for _ in range(5)]
for i in range(5):
    for j in range(4):
        B[i][j] = factorial(A[i][j])
print("\nMatriz A=\n")
print(A, "\n\n")
print("Matriz B=\n")
print(B, "\n")