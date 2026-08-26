    # 18) Elaborar um programa que leia 15 elementos reais para uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmos tipo e dimensão, observando a seguinte lei de formação: “topo elemento da matriz A que possuir índice par deve ter seu elemento dividido por 2; caso contrário, o elemento da matriz A deve multiplicado por 1.5”. Apresentar os elementos da matriz B.

import random as r

A = [0] * 15
B = [0] * 15
for i in range(15):
    A[i] = r.randint(1, 100)
    if A[i]%2==0:
        B[i]=A[i]/2
    else:
        B[i]=A[i]*1.5
print("Matriz A= ", A, "\nMatriz B= ", B)