import pandas as pd
from pathlib import Path
import numpy as np

pasta_entrada = Path(__file__).parent / "Entrada"
Saída = Path(__file__).parent / "Saída"
pasta_saida = Saída / "Matrizes"
pasta_saida_Q = Saída / "Matrizes Q"
pasta_saida_R = Saída / "Matrizes R"
pasta_saida_B = Saída / "Probabilidade limite"
pasta_saida_T = Saída / "Tempo médio de absorção"
files = list(pasta_entrada.glob("*.csv"))

for file in files:
    m = pd.read_csv(file, header=None)
    l_abs = []
    l_trs = []
    ordem = []
    
    for li, l in m.iterrows():
        v = l.tolist()
        if l[li] == 1:
            l_abs.append((li, l))
        else:
            l_trs.append((li, l))
            ordem.append(li)
            
    for i in range(len(l_abs)):
        ordem.append(l_abs[i][0])
        
    mr=m.iloc[ordem, ordem]
    pasta_saida.mkdir(parents=True, exist_ok=True)
    mr.to_csv(pasta_saida / file.name, index=False, header=False)
    
    Q = mr.iloc[:len(l_trs), :len(l_trs)]
    pasta_saida_Q.mkdir(parents=True, exist_ok=True)
    Q.to_csv(pasta_saida_Q / file.name, index=False, header=False)
    
    R = mr.iloc[:len(l_trs), len(l_trs):]
    pasta_saida_R.mkdir(parents=True, exist_ok=True)
    R.to_csv(pasta_saida_R / file.name, index=False, header=False)
    
    B = np.linalg.solve(np.eye(len(l_trs)) - Q.to_numpy(dtype=float), R.to_numpy(dtype=float))
    print(f"\n{'=' * 60}\nArquivo: {file.name}\n{'=' * 60}")
    print("Probabilidades de absorção (B):")
    print(np.array2string(B, precision=4, suppress_small=True))
    
    B = pd.DataFrame(B)
    pasta_saida_B.mkdir(parents=True, exist_ok=True)
    B.to_csv(pasta_saida_B / file.name, index=False, header=False)
    
    T = np.linalg.solve(np.eye(len(l_trs)) - Q.to_numpy(dtype=float), np.eye(len(l_trs)))
    print("\nMatriz fundamental (T):")
    print(np.array2string(T, precision=4, suppress_small=True))
    
    T = pd.DataFrame(T)
    pasta_saida_T.mkdir(parents=True, exist_ok=True)
    T.to_csv(pasta_saida_T / file.name, index=False, header=False)