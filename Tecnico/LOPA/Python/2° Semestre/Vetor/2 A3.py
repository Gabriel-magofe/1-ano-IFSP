# 2) Elaborar um programa que leia oito elementos inteiros em uma matriz A do tipo vetor. Construir uma matriz B de mesma dimensão com os elementos da matriz A multiplicados por 3. O elemento B[1] deve ser implicado pelo elemento A[1] * 3, o elemento B[2] implicado pelo elemento A[2] * 3, e assim por diante, até 8. Apresentar a matriz B.
A = []
for i in range(8):
    elemento = int(input("Digite o {0:2}° elemento: ".format(i+1)))
    A.append(elemento)

B = []
for elemento in A:
    B.append(elemento * 3)

print("Os elementos da matriz B são:")
for i, elemento in enumerate(B):
    print("{0:2}° elemento: {1}".format(i+1, elemento))