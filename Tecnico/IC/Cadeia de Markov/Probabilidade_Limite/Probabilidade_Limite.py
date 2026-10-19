import numpy as np
import pandas as pd
import os

def resolver(P):
    try:
        n, n2 = P.shape
        if n != n2:
            print("Matriz não quadrada\n")
            return
        I = np.eye(n)
        a=(P-I).T
        b=np.zeros(n)
        a[-1]=1
        b[-1]=1
        pi = np.linalg.solve(a, b)
        print("Probabilidade limite:", pi, "\n")
    except np.linalg.LinAlgError:
        print("Erro na resolução\n")

def csv(q):
    try:
        f = pd.read_csv(q)
        P = f.iloc[:, 1:].to_numpy(dtype=float)
        print("\n", P, "\n")
        resolver(P)
    except:
        print("Erro na leitura do arquivo\n")

if __name__ == "__main__":
    os.chdir(r"C:\Users\gabri\OneDrive\Documents\1° ano IF\Tecnico\IC\Cadeia de Markov\Probabilidade Limite")
    while True:
        q=input("Encontrar a probabilidade limite de qual arquivo?\n")

        if q == "sair":
            break
        else:
            csv(q)
    