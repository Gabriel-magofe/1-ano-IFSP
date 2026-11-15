import numpy as np
import uno
import sys
import os

caminho_numpy = r"C:\Program Files\LibreOffice\program\python-core-3.12.14\Lib\site-packages"
if caminho_numpy not in sys.path:
    sys.path.append(caminho_numpy)

# como usei o numpy, precisei rodar o comando 
# "C:\Program Files\LibreOffice\program\python-core-3.12.14\python.exe" -m pip install numpy
# para instalar o numpy no python do LibreOffice, que é diferente do python do sistema operacional
# dpois ainda precisei colocar o caminho do numpy no sys.path, para que o LibreOffice consiga encontrar o numpy

def resolver(P):
    try:
        n, n2 = P.shape
        if n != n2:
            return "Matriz não quadrada"
        I = np.eye(n)
        a = (P-I).T
        b=np.zeros(n)
        a[-1] =  1
        b[-1] = 1
        pi = np.linalg.solve(a, b)
        return pi.tolist()
    except np.linalg.LinAlgError:
        return "Erro na resolução"

def MARKOV_PROB_LIM(M):
    try:
        P = np.array(M, dtype=float)
        r = resolver(P)
        return r
    except Exception as e:
        return f"Erro ao executar: {str(e)}"
    
g_exportedScripts = (MARKOV_PROB_LIM,)