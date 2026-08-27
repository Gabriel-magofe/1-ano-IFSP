//  8) Dada uma sequência de 10 números inteiros, imprimi-la na ordem inversa à da leitura.

programa
{
    funcao inicio()
    {
        inteiro numeros[10]
        inteiro i

        para (i = 0; i < 10; i++)
        {
            escreva("Digite o ", i + 1, "º número: ")
            leia(numeros[i])
        }

        escreva("Números na ordem inversa: ")
        para (i = 9; i >= 0; i--)
        {
            escreva(numeros[i], " ")
        }
    }
}