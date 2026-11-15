import sys
import os

caminho_numpy = r"C:\Program Files\LibreOffice\program\python-core-3.12.14\Lib\site-packages"
if caminho_numpy not in sys.path:
    sys.path.append(caminho_numpy)
    
# como usei o numpy, precisei rodar o comando 
# "C:\Program Files\LibreOffice\program\python-core-3.12.14\python.exe" -m pip install numpy
# para instalar o numpy no python do LibreOffice, que é diferente do python do sistema operacional
# dpois ainda precisei colocar o caminho do numpy no sys.path, para que o LibreOffice consiga encontrar o numpy

import numpy as np
import uno

# Resolve só se a matriz for 2x2 e estiver de A1 a B2
def MARKOV_PROB_LIM():
    try:
        oDoc = XSCRIPTCONTEXT.getDocument()
        oSheet = oDoc.getCurrentController().getActiveSheet()
        
        oCell_A1 = oSheet.getCellRangeByName("A1").getValue()
        oCell_B1 = oSheet.getCellRangeByName("B1").getValue()
        oCell_A2 = oSheet.getCellRangeByName("A2").getValue()
        oCell_B2 = oSheet.getCellRangeByName("B2").getValue()
        
        P = np.array([
            [oCell_A1, oCell_B1],
            [oCell_A2, oCell_B2]
        ])
        
        n, n2 = P.shape
        I = np.eye(n)
        a = (P - I).T
        b = np.zeros(n)
        a[-1] = 1
        b[-1] = 1
        
        pi = np.linalg.solve(a, b)
        
        oSheet.getCellRangeByName("C1").setValue(pi[0])
        oSheet.getCellRangeByName("C2").setValue(pi[1])
    
    except Exception as e:
        oSheet.getCellRangeByName("C1").setString(f"Erro: {str(e)}")
        oSheet.getCellRangeByName("C2").setString(f"Erro: {str(e)}")

g_exportedScripts = (MARKOV_PROB_LIM,)