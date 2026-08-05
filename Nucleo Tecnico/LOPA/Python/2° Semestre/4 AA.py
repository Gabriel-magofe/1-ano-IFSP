# 4) Elabore um programa que leia 15 elementos inteiros de uma matriz A do tipo vetor. Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação: “todo elemento da matriz B deve ser o quadrado do elemento da matriz A correspondente”. Apresentar os elementos das matrizes A e B.	

A=[]
B=[]
for i in range(15):
    A.append(int(input(f"Digite o {i+1}º elemento da matriz A: ")))
for i in range(15):
    B.append(A[i] ** 2)
print("\n\n\nElementos da matriz A:")
for i in range(15):
    print(f"{i+1}° elemento da matriz A = {A[i]}")
print("\n\n\nElementos da matriz B:")
for i in range(15):
    print(f"{i+1}° elemento da matriz B = {B[i]}")