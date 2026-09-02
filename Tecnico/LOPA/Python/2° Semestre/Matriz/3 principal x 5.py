# 3) Desenvolva um programa que leia uma matriz 3x3 e escreva-a após multiplicar a sua diagonal principal por 5.
A=[[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        A[i][j] = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))

for i in range(3):
    A[i][i] *= 5

print("Matriz após multiplicar a diagonal principal por 5:")
for i in range(3):
    for j in range(3):
        print(A[i][j], "\t", end="")
    print()