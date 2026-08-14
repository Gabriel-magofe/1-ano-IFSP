# 11) Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota.
a = [4]
for i in range(4): 
    a.append(int(input("Digite a ", i+1, "° nota: ")))
maior = max(a)
menor = min(a)
media = sum(a) / len(a)

print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média: nota", media)