programa {
            funcao mais10(inteiro &x){
                x=x+10
                escreva("x na função: ",x)
            }
        funcao inicio() {
        inteiro x
        enquanto(verdadeiro){
        escreva("\n","digite o x: ")
        leia (x)
        mais10(x)}
    }
}