    # 1) Elaborar um programa que efetue a leitura de dez nomes de pessoas em uma matriz A do tipo vetor e apresentá-los em seguida.
a = []
for i in range(10):
    nome = input("Digite o nome da pessoa {}: ".format(i+1))
    a.append(nome)
print("Os nomes digitados foram:")
for nome in a:
    print(nome)