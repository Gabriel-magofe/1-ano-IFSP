    // 14) Escreva um programa que leia uma matriz A do tipo vetor com 5 elementos e apresentar esses elementos por meio de uma pesquisa.
programa {
    funcao inicio() {
        inteiro a[5]

        para (inteiro i = 0; i < 5; i++) {
            escreva("Digite o elemento ", i + 1, ": ")
            leia(a[i])
        }
        enquanto(verdadeiro){
            escreva("Digite o elemento que deseja pesquisar: ")
            inteiro pesquisa
            leia(pesquisa)

            logico encontrado = falso
            para (i = 0; i < 5; i++) {
                se (a[i] == pesquisa) {
                    escreva("Elemento ", pesquisa, " encontrado na posição ", i + 1, "\n")
                    encontrado = verdadeiro
                }
            }

            se (!encontrado) {
                escreva("Elemento ", pesquisa, " não encontrado na matriz.\n")
            }

            escreva("Deseja pesquisar outro elemento? (s/n): ")
            caracter resposta
            leia(resposta)
            se(resposta != 's' e resposta != 'S') {
                pare
            }
            
        }
    }
}