// 13) Escreva um programa que leia uma matriz A do tipo vetor com 5 elementos. Coloque-os em ordem crescente e apresente os elementos em ordem decrescente.
programa
{
    funcao inicio()
    {
        inteiro A[5], i, j, aux

        para (i = 0; i < 5; i++)
        {
            escreva("Digite o elemento ", i + 1, ": ")
            leia(A[i])
        }

        para (i = 0; i < 4; i++)
        {
            para (j = 0; j < 4 - i; j++)
            {
                se (A[j] > A[j + 1])
                {
                    aux = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = aux
                }
            }
        }

        escreva("\nElementos em ordem decrescente:")
        para (i = 4; i >= 0; i--)
        {
            escreva(A[i], " ")
        }
    }
}