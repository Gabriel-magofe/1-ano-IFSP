    # 14) Escreva um programa que leia uma matriz A do tipo vetor com 5 elementos e apresentar esses elementos por meio de uma pesquisa.
a = []
for i in range(5):  
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    a.append(elemento)
while True:
    pesquisa = int(input("Digite o elemento que deseja pesquisar: "))
    if pesquisa in a:
        print(f"O elemento {pesquisa} foi encontrado na matriz na posição {a.index(pesquisa)+1}.")
    else:
        print(f"O elemento {pesquisa} não foi encontrado na matriz.")