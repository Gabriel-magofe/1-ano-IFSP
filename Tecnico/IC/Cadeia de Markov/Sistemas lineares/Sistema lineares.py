# cd '.\tecnico\IC\Cadeia de Markov\Sistemas lineares\'

import numpy as np
import pandas as pd

def resolve(a,b):
    try:
        x = np.linalg.solve(a, b)
        print("Solução:", x, "\n")
    except np.linalg.LinAlgError:
        print("Erro\n")

while True:
    q=input("Resolver qual Sistema linear?\n")

    if q == "sair":
        break

    if q == "16 a":
        a=[[1, 3, 1],[3, -3, 1],[0, 2, 1]]
        b=[0, 8, 0]

    elif q == "16 b":
        a=[[1, 2, 4],[2, 3, -1],[1, 0, -14]]
        b=[0, 8, 0]

    elif q == "16 c":
        a=[[1, 1, 1],[2, 1, -1],[2, -1, -7]]
        b=[4, 10, 0]

    elif q == "17":
        a=[[1, 1, 0],[2, 2, 0],[3, 3, 0]]
        b=[3, 6, 8]

    elif q == "18":
        a=[[1, 4, 7],[2, 3, 6],[5, 1, -1]]
        b=[2, 2, 8]

    elif q == "19":
        a=[[2, 1, 1, 1],[1, 2, 1, 1],[1, 1, 2, 1],[1, 1, 1, 2]]
        b=[1, 2, 3, 4]

    elif q == "meu":
        l=int(input("Digite a quantidade de equações e incognitas:\n"))
        a=[]
        b=[]
        for i in range(l):
            g=[]
            for j in range(l):
                g.append(int(input(f"Digite o {j+1}º a da {i+1} equação:\n")))
            a.append(g)
        for i in range(l):
            b.append(int(input(f"Digite o {i+1}º termo independente:\n")))
    elif q == "arquivo":
        nome=input("Digite o nome do arquivo:\n")
        matriz = pd.read_csv(nome, header=None)
        print("\n", matriz, "\n")
        a = matriz.iloc[:, 0:-1].values
        b = matriz.iloc[:, -1].values 
        print("\n", a, "\n")
        print(b, "\n")
    else:    
        print("Opção inválida\n")
    resolve(a,b)