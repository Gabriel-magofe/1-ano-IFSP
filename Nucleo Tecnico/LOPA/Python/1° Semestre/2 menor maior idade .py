ano= int(input("Digite o ano que você nasceu: "))
nome= str(input("Digite o nome: "))
idade= 2026-ano
if idade>=18:
        print(nome,"é maior de idade")
else:
        print(nome,"é menor de idade")