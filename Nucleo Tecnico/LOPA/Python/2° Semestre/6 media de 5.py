A=[]
B=0
for i in range(5):
    A.append(float(input(f"Digite o {i+1}° valor: ")))
for i in range(5):
    B=B+A[i]
B=B/len(A)
print("Média= ", B)