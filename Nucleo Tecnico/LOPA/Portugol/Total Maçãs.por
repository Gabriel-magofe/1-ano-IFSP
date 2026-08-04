programa{
    
    funcao inicio()
    {


        
        inteiro m
        real r
         escreva("Quantas Maçãs você quer comprar?\n")
          leia(m)
         se (m < 12){
             r = m * 1.30
             escreva("O valor total a ser pago é: R$", r)
         }senao{
             r = m * 1.00
             escreva("O valor total a ser pago é: R$", r)       
             }       
    }
}