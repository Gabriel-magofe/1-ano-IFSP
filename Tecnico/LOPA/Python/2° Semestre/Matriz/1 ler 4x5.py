# 1) Ler 20 elementos para uma matriz qualquer, considerando que ela tenha o tamanho de quatro linhas por cinco colunas. Apresentar os valores.

import random as r
A=[]

for j in range(4):
    B=[]
    for i in range(5):
        B.append(r.randint(1, 100))
    A.append(B)
print(A)