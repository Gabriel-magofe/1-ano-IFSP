#  5) Construa um algoritmo que, para uma matriz 4 x 3, calcule a soma dos elementos de cada uma das linhas e escreva as somas obtidas. O algoritmo deve mostrar também o número da linha que apresentou a maior soma.
import random as r

matriz = [[r.randint(0, 100) for i in range(3)] for j in range(4)]

somas = []
print(matriz)
for i in range(4):
    soma = sum(matriz[i])
    somas.append(soma)
    print(f"Soma da linha {i + 1}: {soma}")

linha_maior_soma = somas.index(max(somas)) + 1
print(f"Linha com maior soma: {linha_maior_soma}")