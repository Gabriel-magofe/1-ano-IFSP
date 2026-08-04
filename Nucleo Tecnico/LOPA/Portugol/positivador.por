//  5) Escreva um programa para efetuar a leitura	 de um valor numérico inteiro positivo ou negativo representado pela variável N e apresentar o valor como sendo positivo. Dica: se o valor lido for menor que zero, ele deve ser multiplicado por -1
programa
{
    funcao inicio()
    {
        inteiro N

        escreva("Digite um número inteiro: ")
        leia(N)

        se (N < 0)
        {
            N = N * -1
            escreva("O valor positivo é: ", N)
        }
        senao
        {
            escreva("O valor é positivo: ", N)
        }
    }
}