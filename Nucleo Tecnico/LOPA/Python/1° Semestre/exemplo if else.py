n1=float(input("digite a primeira nota: "))
n2=float(input("digite a segunda nota: "))
n3=float(input("digite a terceira nota: "))
n4=float(input("digite a quarta nota: "))

m= (n1+n2+n3+n4)/4

if m >= 6:
    print("aprovado \n média: ",m)
else:
    print("reprovado \n média: ",m)