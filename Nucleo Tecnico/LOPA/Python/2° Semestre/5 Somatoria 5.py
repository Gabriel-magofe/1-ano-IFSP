# 5) Considerando 5 números reais digitados pelo usuário e armazenados em um vetor, exibir o valor da somatória dos mesmos.

A=[]
B= 0
for i in range(5):
    A.append(float(input(f"Digite o {i+1}° valor: ")))
for i in range(5):
    B=B+A[i]
print("Somatoria= ", B)