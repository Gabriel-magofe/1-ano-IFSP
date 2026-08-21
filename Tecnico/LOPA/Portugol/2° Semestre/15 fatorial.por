//15) Elaborar um programa que leia uma matriz A do tipo vetor com 15 elementos inteiros. Construir uma matriz B de mesmo tipo, e cada elemento da matriz B deve ser o resultado da fatorial correspondente de cada elemento da matriz A. Apresentar as matrizes A e B.
programa {
    funcao inicio() {
        inteiro a[15], b[15], i, j

         para(i =0; i <= 14; i++){
            escreva("Digite o", i+1, "° elemento de A: ")
            leia(a[i])
        }

        para(i = 0; i <= 14; i++){
            para(j = 1; j <= i; j++){
                b[i] = b[i] * j
            }
        }

        para(i = 0; i <= 14; i++){
            escreva("A[", i+1,"]: ", a[i], " |B[", i+1, "]: ", b[i], "\n")
        }
    }
}