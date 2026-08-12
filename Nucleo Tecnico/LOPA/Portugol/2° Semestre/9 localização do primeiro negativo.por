// 9) Dado um vetor de N números, imprimir a localização do primeiro número negativo, se houver.
programa
{
    funcao inicio()
    {
        inteiro R
        inteiro A[100]
        inteiro posicao = -1

        escreva("Digite a quantidade de números: ")
        leia(R)

        para (inteiro i = 0; i < R; i++)
        {
            escreva("Digite o ", i + 1, "º número: ")
            leia(A[i])

            se (A[i] < 0 e posicao == -1)
            {
                posicao = i
            }
        }

        se (posicao != -1)
        {
            escreva("O primeiro número negativo está na posição: ", posicao)
        }
        senao
        {
            escreva("Não há números negativos no vetor.")
        }
    }
}