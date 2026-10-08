programa {
    funcao real calcular(inteiro a, inteiro b, cadeia operador) {
        se (operador == "+") {
            retorne soma(a, b)
        } senao se (operador == "-") {
            retorne subtracao(a, b)
        } senao se (operador == "*") {
            retorne multiplicacao(a, b)
        } senao se (operador == "/") {
            retorne divisao(a, b)
        } senao {
            escreva("Operador inválido")
            retorne 0
        }
    }
    funcao inteiro soma(inteiro a, inteiro b) {
        retorne a + b
    }
    funcao inteiro subtracao(inteiro a, inteiro b) {
        retorne a - b
    }
    funcao inteiro multiplicacao(inteiro a, inteiro b) {
        retorne a * b
    }
    funcao inteiro divisao(inteiro a, inteiro b) {
        se (b == 0) {
            escreva("Erro: Divisão por zero")
            retorne 0
        }
        retorne a / b
    }
    funcao inicio() {
        inteiro n1 = 0, n2 = 0
        cadeia op = "+"
        enquanto (verdadeiro){
        escreva("Digite o primeiro número: ")
        leia(n1)
        escreva("Digite o segundo número: ")
        leia(n2)
        escreva("Digite o operador: ")
        leia(op)
        real r = calcular(n1, n2, op)
        escreva("Resultado: ", r, "\n")
        }
    }
}