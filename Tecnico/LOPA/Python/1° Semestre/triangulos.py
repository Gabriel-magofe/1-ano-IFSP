A=float(input("Digite o valor do lado A do triângulo: "))
B=float(input("Digite o valor do lado B do triângulo: "))
C=float(input("Digite o valor do lado C do triângulo: "))

if A <= 0 or B <= 0 or C <= 0:
    print("Os lados devem ser maiores que zero.")
elif A < (B + C) and B < (A + C) and C < (A + B):
    if A == B == C:
        print("O triângulo é equilátero.")
    elif A == B or A == C or B == C:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os lados não formam um triângulo.")