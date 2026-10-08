def calcular(a,b,o):
    if o == "+":
        return soma(a,b)
    elif o == "-":
        return subtrai(a,b)
    elif o == "*":
        return multiplica(a,b)
    elif o == "/":
        return dividi(a,b)
    else:
        return "Erro"
def soma(a,b):
    return a+b
def subtrai(a,b):
    return a-b
def multiplica(a,b):
    return a*b
def dividi(a,b):
    return a/b
a=float(input("Digite um número: "))
b=float(input("Digite outro número: "))
o=input("Digite o operador: ")
print(calcular(a,b,o))
