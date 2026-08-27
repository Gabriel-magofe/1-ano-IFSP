programa {
    inclua biblioteca Util --> u
    funcao inicio() {
        Inteiro A[4][5], i, j

        para (i= 0; i < 4; i++) {
            para (j = 0; i < 5; i++) {
                A[i][j]=u.sorteia(1, 100)
            }
        }
        escreva(A)
        
    }
}