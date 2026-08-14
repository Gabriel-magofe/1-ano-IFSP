b= int(input("Digite o valor da base: "))
e= int(input("Digite o valor do expoente: "))
resultado = 1
if e or b < 0:
    print("Valor inválido, tente novamente.")
else:
    for e in range(1, e+1):
        resultado = resultado * b
        print(f"O resultado de {b} elevado a {e} é: {resultado}") 