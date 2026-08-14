import numpy as np

numeros = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)
print(numeros)
print(numeros.shape)   # formato
print(numeros.size)    # quantidade total
print(numeros.ndim)    # número de dimensões
print(numeros.dtype)   # tipo dos dados
print(np.zeros((2, 3)))
print(np.ones((3, 2)))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
soma = a + b
print(soma)
subtracao = a - b
print(subtracao)
multiplicacao = a * b
print(multiplicacao)
divisao = a / b
print(divisao)

a = np.array([10, 20, 30, 40])
b = np.array([1,  2,  3,  4])
# Adição elemento a elemento
print(a + b)  # Output: [11 22 33 44]
# Multiplicação escalar (Broadcasting básico)
print(a * 2)  # Output: [20 40 60 80]
# Elevação ao quadrado
print(b ** 2) # Output: [ 1  4  9 16]
# Expressões condicionais (Retorna booleanos)
print(a > 20) # Output: [False False  True  True]

array = np.array([10, 20, 30, 40])
print(array[0])
print(array[2])
print(array[1:3])

dados = np.array([10, 20, 30, 40, 50])
print(np.mean(dados))   # média
print(np.max(dados))    # maior valor
print(np.min(dados))    # menor valor
print(np.sum(dados))    # soma
print(np.std(dados))    # desvio padrão

dados = np.array([12, 15, 18, 22, 30, 45])
# Média: 23.67
print(f"Média: {np.mean(dados):.2f}") 
# Desvio Padrão: 11.16
print(f"Desvio Padrão: {np.std(dados):.2f}") 
# Maior valor: 45
print(f"Maior valor: {np.max(dados)}") 
# Índice do maior: 5
print(f"Índice do maior: {np.argmax(dados)}") 
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))