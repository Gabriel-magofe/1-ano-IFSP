n1=float(input("Digite a nota da primeira avaliação: "))
n2=float(input("Digite a nota da segunda avaliação: "))
m=(n1+n2)/2
if m>=6:
	print("Aprovado com media: ", m)
else:
	print("Reprovado com media: ", m)