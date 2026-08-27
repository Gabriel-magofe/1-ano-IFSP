// 17) Elaborar um programa que leia uma matriz A do tipo vetor com 20 elementos inteiros. Construir uma matriz B dos mesmos tipos e dimensão da matriz A, sendo cada elemento da matriz B o somatório de 1 até o valor do elemento correspondente armazenado na matriz A. Se o valor do elemento da matriz A[1] for 5, o elemento correspondente da matriz B[1] deve ser 15, pois o somatório do elemento da matriz A é 1 + 2 + 3 + 4 + 5. Apresentar os elementos da matriz B.
programa {
    inclua biblioteca Util --> u 
    inteiro B[20], i
    funcao somatoria(inteiro n, inteiro j) {
    	inteiro soma=0, i
        para (i = 1; i < n+1; i++) {
                soma=soma+i
            }
        B[j]=soma
        }
    funcao inicio() {
        inteiro A[20]   
        para (i = 0; i < 20; i++) {
            A[i]=u.sorteia(1, 10)
            somatoria(A[i], i)
        }
        para (i = 0; i < 20; i++) {
            escreva("A[", i+1, "] = ", A[i], " | B[", i+1, "] = ", B[i], "\n")
        }
    }
}