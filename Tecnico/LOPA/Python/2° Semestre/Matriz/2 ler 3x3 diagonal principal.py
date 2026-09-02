# 2) Desenvolva um programa que leia uma matriz 3x3 e apresente os valores da sua diagonal principal.

A = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        A[i][j] = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))

print("Diagonal principal:")
for i in range(3):
    print(f"[{i+1}][{i+1}]: {A[i][i]}")