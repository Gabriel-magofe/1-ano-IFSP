#  8) Dada uma sequência de 10 números inteiros, imprimi-la na ordem inversa à da leitura.
import random
A = []
for i in range(10):
    n = random.randint(1, 100)
    A.append(n)
print("Sequência original:")
print(A)
print("Sequência inversa:")
A.reverse()
print(A)