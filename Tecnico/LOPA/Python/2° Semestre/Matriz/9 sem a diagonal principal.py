# 9) Criar um algoritmo que leia os elementos de uma matriz inteira 4 x 4 e escreva todos os elementos, exceto os elementos da diagonal principal.
import random as r
A = [[r.randint(0, 10) for _ in range(4)] for _ in range(4)]
B = [[0 for _ in range(4)] for _ in range(4)]
print("Matriz:\n", A, "\n")
for i in range(4):
    for j in range(4):
        if i != j:
            B[i][j] = A[i][j]
        else:
            B[i][j] = "-"
print("Matriz sem a diagonal principal:\n", B, "\n")