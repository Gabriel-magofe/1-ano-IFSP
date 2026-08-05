// 2) Elaborar um programa que leia oito elementos inteiros em uma matriz A do tipo vetor. Construir uma matriz B de mesma dimensão com os elementos da matriz A multiplicados por 3. O elemento B[1] deve ser implicado pelo elemento A[1] * 3, o elemento B[2] implicado pelo elemento A[2] * 3, e assim por diante, até 8. Apresentar a matriz B.
programa{
    funcao inicio(){
        inteiro A[8], B[8], i
        escreva("Digite 8 elementos inteiros para a matriz A:")
        para(i = 0; i < 8; i++){
            leia(A[i])
        }
        
        para(i = 0; i < 8; i++){
            B[i] = A[i] * 3
        }
        
        escreva("Os elementos da matriz B são:")
        para(i = 0; i < 8; i++){
            escreva((i+1) + "° elemento: " + B[i])
        }
    }
}