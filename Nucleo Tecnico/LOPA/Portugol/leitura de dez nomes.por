// 1) Elaborar um programa que efetue a leitura de dez nomes de pessoas em uma matriz A do tipo vetor e apresentá-los em seguida.
programa
{
    funcao inicio()
    {
        cadeia a[10]
        inteiro i

        para(i = 0; i < 10; i++)
        {
            escreva("Digite o nome da pessoa ", i + 1, ": ")
            leia(a[i])
        }

        escreva("Os nomes digitados foram:\n")
        para(i = 0; i < 10; i++)
        {
            escreva(a[i], "\n")
        }
    }
}