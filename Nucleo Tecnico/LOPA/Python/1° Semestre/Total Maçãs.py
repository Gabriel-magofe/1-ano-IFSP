m=int(input("Quantas Maçãs você quer comprar?\n"))
if m<12:
    r=m*1.30
    print("O valor total a ser pago é: R$",r)
else:
    r=m*1.00
    print("O valor total a ser pago é: R$",r)