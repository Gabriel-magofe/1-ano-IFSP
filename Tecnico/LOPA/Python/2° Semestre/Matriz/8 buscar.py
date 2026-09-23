# 8) Ler uma matriz D 5x5 (considere que não serão informados valores duplicados). A seguir ler um número X e escreva uma mensagem indicando se o valor de X existe ou NÃO na matriz.
import random as r
D = [[r.randint(0, 100) for _ in range(5)] for _ in range(5)]
while True:
    print("Matriz D:\n", D, "\n")
    X = int(input("Digite um número: "))
    if any(X in row for row in D):
        print("O valor", X, "existe na matriz.")
    else:
        print("O valor", X, "não existe na matriz.")