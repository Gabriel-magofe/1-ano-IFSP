programa
{
    funcao inicio()
    {
        real altura1, altura2
        cadeia nome1, nome2
        
        escreva("Digite o nome do primeiro amigo: ")
        leia(nome1)
        escreva("Digite a altura de ", nome1, ": ")
        leia(altura1)
        
        escreva("Digite o nome do segundo amigo: ")
        leia(nome2)
        escreva("Digite a altura de ", nome2, ": ")
        leia(altura2)
        
        se (altura1 > altura2)
        {
            escreva(nome1, " é mais alto(a) com ", altura1, " metros.")
        }
        senao se (altura2 > altura1)
        {
            escreva(nome2, " é mais alto(a) com ", altura2, " metros.")
        }
        senao
        {
            escreva(nome1, " e ", nome2, " têm a mesma altura de ", altura1, " metros.")
        }
    }
}