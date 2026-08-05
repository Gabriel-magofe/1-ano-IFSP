programa
{
    funcao inicio()
    {
        inteiro ano
        
        escreva("Digite um ano: ")
        leia(ano)
        
        se (ano % 400 == 0)
        {
            escreva(ano, " é um ano bissexto.")
        }
        senao se (ano % 4 == 0 e ano % 100 != 0)
        {
            escreva(ano, " é um ano bissexto.")
        }
        senao
        {
            escreva(ano, " não é um ano bissexto.")
        }
    }
}