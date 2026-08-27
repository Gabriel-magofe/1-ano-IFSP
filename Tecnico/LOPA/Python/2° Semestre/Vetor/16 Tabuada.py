    # 16) Construir um programa que calcule a tabuada de um valor qualquer de 1 até 10 e armazene os resultados em uma matriz A de uma dimensão. Apresentar os elementos da matriz A.

def tabuada(n):
    T = [0] * 10
    for i in range(10):
        T[i] = n * (i + 1)
    return T

n=int(input("Digite um número para calcular a tabuada: "))
resultado = tabuada(n)
print("Resultados da tabuada:")
for i in range(10):
    print(f"{n} x {i + 1} = {resultado[i]}")