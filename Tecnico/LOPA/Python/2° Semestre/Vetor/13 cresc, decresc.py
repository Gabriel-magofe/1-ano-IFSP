# 13) Escreva um programa que leia uma matriz A do tipo vetor com 5 elementos. Coloque-os em ordem crescente e apresente os elementos em ordem decrescente.


A = [0] * 5

for i in range(5):
    A[i] = float(input(f"Digite o elemento A[{i}]: "))
for i in range(5):
    for j in range(4 - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print("\nElementos em ordem crescente:")
for i in range(5):
    print(A[i])
print("\nElementos em ordem decrescente:")
for i in range(4, -1, -1):
    print(A[i])