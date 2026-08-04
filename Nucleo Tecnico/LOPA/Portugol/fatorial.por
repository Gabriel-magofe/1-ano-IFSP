programa
{
    funcao inicio()
    {
        inteiro n, f = 1, fat
        escreva("Digite um número: ")
        leia(n)
        fat = n


        faca
        {
            se (fat > 0)
            {
                f = f * fat
                fat = fat - 1
            }
        } enquanto (fat > 0)

        escreva("O fatorial de ", n, " é ", f)
    }
}