N=int(input("Digite um número inteiro: "))
if N < 0:
    N = N * -1
    print("O valor positivo é:", N)
else:
    print("O valor é positivo:", N)