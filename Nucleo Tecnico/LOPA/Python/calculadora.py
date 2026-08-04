while True:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    n3 = int(input("Digite  a operação que deseja realizar: 1-soma, 2-subtração, 3-multiplicação, 4-divisão \n"))

    if n3==1:
        r=n1+n2
        print("O resultado da soma é: ",r)
        break
    if n3==2:
        r=n1-n2
        print("O resultado da subtração é: ",r)
        break
    if n3==3:
        r=n1*n2
        print("O resultado da multiplicação é: ",r)
        break
    if n3==4:
        if n2 == 0:
            print("Erro: divisão por zero.")
            break
        r=n1/n2
        print("O resultado da divisão é: ",r)
        break
    else:
        print("Valor invalido.")
