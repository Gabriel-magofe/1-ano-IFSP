programa
{
    funcao inicio()
    {
        real salario, desconto

        escreva("Informe o salário: ")
        leia(salario)

        se (salario <= 420.00)
        {
            desconto = salario * 0.08
           escreva("O desconto do INSS é: R$ ", desconto)
        }
        senao se ((salario > 420.00) e (salario <= 1350))
        {
            desconto = salario * 0.09 
            escreva("O desconto do INSS é: R$ ", desconto) 
        }
        senao
        {
            desconto = salario * 0.10
            escreva("O desconto do INSS é: R$ ", desconto)
        }       
    }
}