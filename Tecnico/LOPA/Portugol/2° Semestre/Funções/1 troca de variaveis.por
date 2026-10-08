programa {
    funcao troca(inteiro x, inteiro y) {
        inteiro aux
        aux = x
        x = y
        y = aux
    }
    funcao inicio() {
        inteiro a = 67, b = 42
        troca(a, b)
        escreva(a, b)
    }
}