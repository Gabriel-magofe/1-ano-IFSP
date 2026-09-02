// 17) Elaborar um programa que leia uma matriz A do tipo vetor com 20 elementos inteiros. Construir uma matriz B dos mesmos tipos e dimensão da matriz A, sendo cada elemento da matriz B o somatório de 1 até o valor do elemento correspondente armazenado na matriz A. Se o valor do elemento da matriz A[1] for 5, o elemento correspondente da matriz B[1] deve ser 15, pois o somatório do elemento da matriz A é 1 + 2 + 3 + 4 + 5. Apresentar os elementos da matriz B.
programa {
    inclua biblioteca Util --> u
    funcao inicio() {
        inteiro A[4][3], B[4][3], C[4][3], i, j
        para (i = 0; i < 4; i++) {
            para (j = 0; j < 3; j++) {
                A[i][j] = u.sorteia(1, 10)
                B[i][j] = u.sorteia(1, 10)
                C[i][j] = A[i][j] - B[i][j]
            }
        }
        escreva("\n\n\n Matriz A: \n")
        para (i = 0; i < 4; i++) {
            para (j = 0; j < 3; j++) {
                escreva(A[i][j], "\t")
            }
            escreva("\n")
        }
        escreva("\n\n\n Matriz B: \n")
        para (i = 0; i < 4; i++) {
            para (j = 0; j < 3; j++) {
                escreva(B[i][j], "\t")
            }
            escreva("\n")
        }
        escreva("\n\n\n Matriz C: \n")
        para (i = 0; i < 4; i++) {
            para (j = 0; j < 3; j++) {
                escreva(C[i][j], "\t")
            }
            escreva("\n")
        }
    }
}