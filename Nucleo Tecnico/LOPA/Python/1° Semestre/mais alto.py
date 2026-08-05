 # 3) Escreva um programa que determine quem é o mais alto dentre dois amigos com alturas e nomes informados pelo usuário.
n1 = input("Digite o nome do primeiro amigo: ")
h1 = float(input("Digite a altura do primeiro amigo (em metros): "))
n2 = input("Digite o nome do segundo amigo: ")
h2 = float(input("Digite a altura do segundo amigo (em metros): "))

if h1 > h2:
    print(n1, "é o mais alto.")
elif h2 > h1:
    print(n2, "é o mais alto.")
else:
    print("Ambos têm a mesma altura.")