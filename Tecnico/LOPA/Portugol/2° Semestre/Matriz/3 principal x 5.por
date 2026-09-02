// 3) Desenvolva um programa que leia uma matriz 3x3 e escreva-a após multiplicar a sua diagonal principal por 5.
programa {
    funcao inicio() {
        inteiro A[3][3], i, j
        para (i = 0; i < 3; i++) {
            para (j = 0; j < 3; j++) {
                escreva("Digite o valor da posição [", i+1, "][", j+1, "]: ")
                leia(A[i][j])
            }
        }
        para (i = 0; i < 3; i++) {
            A[i][i] = A[i][i] * 5
        }
        escreva("Matriz após multiplicar a diagonal principal por 5:\n")
        para (i = 0; i < 3; i++) {
            para (j = 0; j < 3; j++) {
                escreva(A[i][j], "\t")
            }
            escreva("\n")
        }
    }
}