// 2) Desenvolva um programa que leia uma matriz 3x3 e apresente os valores da sua diagonal principal.

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
            escreva("Diagonal principal [", i+1, "][", i+1, "]: ", A[i][i], "\n")
        }
    }
}