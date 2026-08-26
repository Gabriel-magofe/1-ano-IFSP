// 16) Construir um programa que calcule a tabuada de um valor qualquer de 1 até 10 e armazene os resultados em uma matriz A de uma dimensão. Apresentar os elementos da matriz A.

programa {
    funcao inicio() {
        inteiro i, T[10], l
        funcao tabuada(inteiro n) {
            para (i=0; i<10; i++) {
                T[i] = n * (i + 1)
            }
            retorne T
        }
        escreva("Digite um número para calcular a tabuada: ")
        leia(l)
        T = tabuada(l)
        escreva("Resultados da tabuada:\n")
        para (i=0; i<10; i++) {
            escreva(l, " x ", (i + 1), " = ", T[i], "\n")
        } 
    }
}