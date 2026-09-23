# 10) Elaborar um programa que leia uma matriz A de duas dimensões com 15 linhas e 15 colunas. Apresentar o somatório dos elementos pares situados na diagonal principal da referida matriz.
import random as ra
a, m, r=[], [], []
m = [[ra.randint(0, 10) for _ in range(15)] for _ in range(15)]
print("Matriz:\n", m, "\n")
for i in range(15):
    if m[i][i]%2==0:
        r.append(m[i][i])
print("Diagonal principal:", r)
print("Soma dos elementos pares da diagonal principal:", sum(r))