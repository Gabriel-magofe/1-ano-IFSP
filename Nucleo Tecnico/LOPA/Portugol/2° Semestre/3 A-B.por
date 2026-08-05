// 3) Escrever um programa que leia duas matrizes (denominadas A e B) do tipo vetor com 20 elementos reais. Construir uma matriz C, sendo cada elemento da matriz C a subtração de um elemento correspondente da matriz A com um elemento correspondente da matriz B, ou seja, a operação de processamento deve estar baseada na operação C[I] ← A[1] – B[1]. Ao final, apresentar os elementos da matriz C.

programa{
    funcao inicio(){
        real A[20], B[20], C[20]
        inteiro i

        para(i = 0; i < 20; i++){
            escreva("Digite o ", i + 1, "º elemento da matriz A: ")
            leia(A[i])
        }
        escreva("\n\n\n")
        para(i = 0; i < 20; i++){
            escreva("Digite o ", i + 1, "º elemento da matriz B: ")
            leia(B[i])
        }
        para(i = 0; i < 20; i++){
            C[i] = A[i] - B[i]
        }
        escreva("\n\n\nElementos da matriz C: ")
        para(i = 0; i < 20; i++){
            escreva(i+1, "° elemento da matriz C:", C[i], "\n")
        }
    }
}