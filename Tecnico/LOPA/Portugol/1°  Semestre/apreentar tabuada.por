programa {
    funcao inicio() {
        inteiro n, i, resultado
        escreva("Digite o número para a tabuada: ")
        leia(n)
        para (i = 1; i <= 10; i++) {
            resultado = n * i
            escreva(n + " x " + i + " = " + resultado + "\n")
        }
    }
}