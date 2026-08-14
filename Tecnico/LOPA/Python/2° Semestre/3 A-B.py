# 3) Escrever um programa que leia duas matrizes (denominadas A e B) do tipo vetor com 20 elementos reais. Construir uma matriz C, sendo cada elemento da matriz C a subtração de um elemento correspondente da matriz A com um elemento correspondente da matriz B, ou seja, a operação de processamento deve estar baseada na operação C[I] ← A[1] – B[1]. Ao final, apresentar os elementos da matriz C.

A=[]
B=[]
C=[]
for i in range(20):
    A.append(float(input(f"Digite o {i+1}º elemento da matriz A: ")))
print("\n\n\n")
for i in range(20):
    B.append(float(input(f"Digite o {i+1}º elemento da matriz B: ")))
for i in range(20):
    C.append(A[i] - B[i])
print("\n\n\nElementos da matriz C:")
for i in range(20):
    print(f"{i+1}° elemento da matriz C = {C[i]}")