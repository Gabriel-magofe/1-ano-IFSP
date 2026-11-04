// primos até 100
programa {
    funcao logico primo(inteiro n){
        inteiro i
        se (n < 2) {
            retorne falso
        }
        para (i = 2; i <= n / 2; i++) {
            se (n % i == 0) {
                retorne falso
            }
        }
        retorne verdadeiro
    }
    funcao inicio() {
        inteiro num
        para (num = 2; num <= 100; num++) {
            se (primo(num)) {
                escreva(num, "\n")
            }
        }
    }
}