#  6) Escreva um programa para ler uma matriz A de duas dimensões com 4 linhas e 3 colunas. Mostre a quantidade de valores pares e impares.
a=[]
m=[]
for i in range(4):
    for j in range(3):
        a.append(int(input(f"Digite o valor [{i+1}][{j+1}] da matriz: ")))
    m.append(a)
    a=[]

print("Matriz:\n", m, "\n")
p=0
im=0
z=0
for i in range(4):
    for j in range(3):
        if m[i][j]==0:
            z+=1
        elif m[i][j]%2 == 0:
            p+=1
        else:
            im+=1
print("Quantidade de valores pares:", p)
print("Quantidade de valores impares:", im)
print("Quantidade de zeros:", z)