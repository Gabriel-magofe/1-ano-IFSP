// 11) Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota.
programa {
    funcao inicio() {
        real notas[4]
        real soma = 0
        real media
        real maiorNota
        real menorNota

        para (inteiro i = 0; i < 4; i++) {
            escreva("Digite a nota ", i + 1, ": ")
            leia(notas[i])
            soma = soma + notas[i]
        }

        media = soma / 4

        maiorNota = notas[0]
        menorNota = notas[0]

        para (i = 1; i < 4; i++) {
            se (notas[i] > maiorNota) {
                maiorNota = notas[i]
            }
            se (notas[i] < menorNota) {
                menorNota = notas[i]
            }
        }

        escreva("Média final: ", media, "\n")
        escreva("Maior nota: ", maiorNota, "\n")
        escreva("Menor nota: ", menorNota, "\n")
    }
}