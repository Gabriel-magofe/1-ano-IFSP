programa {
    funcao bis(inteiro a){se(a%400==0){escreva("\n", "o ano é bissexto")}senao{escreva("\n", "o ano não é bissexto")}}
    funcao inicio(){
    	   inteiro a
        escreva("digite o ano: ")
        leia(a)
        bis(a)
  }
}