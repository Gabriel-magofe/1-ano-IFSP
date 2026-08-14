// 4) Elabore um programa que leia 15 elementos inteiros de uma matriz A do tipo vetor. Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação: “todo elemento da matriz B deve ser o quadrado do elemento da matriz A correspondente”. Apresentar os elementos das matrizes A e B.	

programa{
    funcao inicio(){
        inteiro A[15], B[15]
        inteiro i

        para(i = 0; i < 15; i++){
            escreva("Digite o ", i + 1, "º elemento da matriz A: ")
            leia(A[i])
        }
        para(i = 0; i < 15; i++){
            B[i] = A[i] * A[i]
        }
        escreva("\n\n\nElementos da matriz A: ")
        para(i = 0; i < 15; i++){
            escreva("\n", i+1, "° elemento da matriz A:", A[i])
        }
        escreva("\n\n\nElementos da matriz B: ")
        para(i = 0; i < 15; i++){
            escreva("\n", i+1, "° elemento da matriz B:", B[i])
        }
    }
}