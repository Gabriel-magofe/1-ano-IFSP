#    4) Para um salário informado pelo usuário, calcular o desconto do INSS de acordo com a tabela a seguir:

# SALÁRIO (R$)                     % DESCONTO INSS
# Até 420,00                                           8%
# Acima de 420,00 até 1.350,00            9%
# Acima de 1.350,00                              10%
s=float(input("Digite o salário: R$ "))
if s <= 420:
    inss = s * 0.08
elif s <= 1350:
    inss = s * 0.09
else:
    inss = s * 0.10

print("O desconto do INSS é: R$ {:.2f}".format(inss))