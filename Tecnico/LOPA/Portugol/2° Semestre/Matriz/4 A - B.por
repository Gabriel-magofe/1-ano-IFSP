// 4) Ler duas matrizes A e B, cada uma de duas dimensões com quatro linhas e três colunas. Construir uma matriz C de mesma dimensão, a qual é formada pela subtração dos elementos da matriz A com os elementos da matriz B. Apresentar a matriz C.
programa {
    inclua biblioteca util --> u
    funcao inicio() {
        inteiro A[4][3], B[4][3], C[4][3], i, j
        para (i = 0; i < 4; i++) {
            para (j = 0; j < 3; j++) {
                u.sorteia(A[i][j], 1, 10)
                u.sorteia(B[i][j], 1, 10)
                C[i][j] = A[i][j] - B[i][j]
            }
        }
        para (i = 0; i < 4; i++) {
            para (j = 0; j < 3; j++) {
                escreva(C[i][j], "\t")
            }
            escreva("\n")
        }
    }
}