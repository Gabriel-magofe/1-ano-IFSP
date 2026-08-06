# 7) Dados dois vetores A e B, ambos com 5 elementos, determinar o produto desses vetores.

A=[]
B=[]
C=[]
for i in range(5):
    A.append(float(input(f"Digite o {i+1}° valor de A: ")))
print("\n\n")
for i in range(5):
    B.append(float(input(f"Digite o {i+1}° valor de B: ")))
for i in range(5):
    C.append(A[i]*B[i])
print("\n\nProduto de A e B= ", C)