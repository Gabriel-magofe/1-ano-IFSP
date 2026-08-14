programa
{
    funcao inicio()
    {
        real pm1, gpu1, ram1, ssd1, pro1, t1, tp1
        real pm2, gpu2, ram2, ssd2, pro2, t2, tp2
        real pm3, gpu3, ram3, ssd3, pro3, t3, tp3
        real m, mp

        escreva("Digite o valor da placa mãe do pc 1: R$: ")
        leia(pm1)
        escreva("Digite o valor da placa de vídeo do pc 1: R$: ")
        leia(gpu1)
        escreva("Digite o valor da memoria RAM do pc 1: R$: ")
        leia(ram1)
        escreva("Digite o valor do armazenamento do pc 1: R$: ")
        leia(ssd1)
        escreva("Digite o valor do processador do pc 1: R$: ")
        leia(pro1)

        t1 = pm1 + gpu1 + ram1 + ssd1 + pro1
        se (pm1 >= 579.99 e gpu1 >= 1469.99 e ram1 >= 1238 e ssd1 >= 429.90 e pro1 >= 899.99) {
            escreva("\n\nO seu pc roda GTA V Liso\n\n")
        } senao {
            escreva("\n\nO seu pc é fraco para rodar GTA V\n\n")
        }

        escreva("Digite o valor da placa mãe do pc 2: R$: ")
        leia(pm2)
        escreva("Digite o valor da placa de vídeo do pc 2: R$: ")
        leia(gpu2)
        escreva("Digite o valor da memoria RAM do pc 2: R$: ")
        leia(ram2)
        escreva("Digite o valor do armazenamento do pc 2: R$: ")
        leia(ssd2)
        escreva("Digite o valor do processador do pc 2: R$: ")
        leia(pro2)

        t2 = pm2 + gpu2 + ram2 + ssd2 + pro2
        se (pm2 >= 579.99 e gpu2 >= 1469.99 e ram2 >= 1238 e ssd2 >= 429.90 e pro2 >= 899.99) {
            escreva("\n\nO seu pc roda CS 2 liso\n\n")
        } senao {
            escreva("\n\nO seu pc é fraco para rodar CS 2\n\n")
        }

        escreva("Digite o valor da placa mãe do pc 3: R$: ")
        leia(pm3)
        escreva("Digite o valor da placa de vídeo do pc 3: R$: ")
        leia(gpu3)
        escreva("Digite o valor da memoria RAM do pc 3: R$: ")
        leia(ram3)
        escreva("Digite o valor do armazenamento do pc 3: R$: ")
        leia(ssd3)
        escreva("Digite o valor do processador do pc 3: R$: ")
        leia(pro3)

        t3 = pm3 + gpu3 + ram3 + ssd3 + pro3
        se (pm3 >= 369.99 e gpu3 >= 2699.99 e ram3 >= 1238 e ssd3 >= 429.90 e pro3 >= 2699.99) {
            escreva("\n\nO seu pc roda Minecraft Liso\n\n")
        } senao {
            escreva("\n\nO seu pc é fraco para rodar Minecraft\n\n")
        }

        escreva("///////////////////////////////////////////////////////\n\n")

        tp1 = t1 + (t1 * 0.15)
        tp2 = t2 + (t2 * 0.15)
        tp3 = t3 + (t3 * 0.15)

        se (t1 < t2 e t1 < t3) {
            escreva("O pc 1 é o mais barato a vista com o valor de: R$: ", t1, "\n")
        } senao {
            se (t2 < t1 e t2 < t3) {
                escreva("O pc 2 é o mais barato a vista com o valor de: R$: ", t2, "\n")
            } senao {
                se (t3 < t1 e t3 < t2) {
                    escreva("O pc 3 é o mais barato a vista com o valor de: R$: ", t3, "\n")
                } senao {
                    escreva("Os pcs tem o mesmo valor a vista: R$: ", t1, "\n")
                }
            }
        }

        se (tp1 < tp2 e tp1 < tp3) {
            escreva("\n\nO pc 1 é o mais barato parcelado com o valor de: R$: ", tp1, "\n")
        } senao {
            se (tp2 < tp1 e tp2 < tp3) {
                escreva("\n\nO pc 2 é o mais barato parcelado com o valor de: R$: ", tp2, "\n")
            } senao {
                se (tp3 < tp1 e tp3 < tp2) {
                    escreva("\n\nO pc 3 é o mais barato parcelado com o valor de: R$: ", tp3, "\n")
                } senao {
                    escreva("\n\nOs pcs tem o mesmo valor parcelado: R$: ", tp1, "\n")
                }
            }
        }

        se (t1 > t2 e t1 > t3) {
            escreva("\n\nO pc 1 é o mais caro a vista com o valor de: R$: ", t1, "\n")
        } senao {
            se (t2 > t1 e t2 > t3) {
                escreva("\n\nO pc 2 é o mais caro a vista com o valor de: R$: ", t2, "\n")
            } senao {
                se (t3 > t1 e t3 > t2) {
                    escreva("\n\nO pc 3 é o mais caro a vista com o valor de: R$: ", t3, "\n")
                } senao {
                    escreva("\n\nOs pcs tem o mesmo valor a vista: R$: ", t1, "\n")
                }
            }
        }

        se (tp1 > tp2 e tp1 > tp3) {
            escreva("\n\nO pc 1 é o mais caro parcelado com o valor de: R$: ", tp1, "\n")
        } senao {
            se (tp2 > tp1 e tp2 > tp3) {
                escreva("\n\nO pc 2 é o mais caro parcelado com o valor de: R$: ", tp2, "\n")
            } senao {
                se (tp3 > tp1 e tp3 > tp2) {
                    escreva("\n\nO pc 3 é o mais caro parcelado com o valor de: R$: ", tp3, "\n")
                } senao {
                    escreva("\n\nOs pcs tem o mesmo valor parcelado: R$: ", tp1, "\n")
                }
            }
        }

        m = (t1 + t2 + t3) / 3
        escreva("\n\nO valor médio dos pcs a vista é: R$: ", m, "\n")
        mp = (tp1 + tp2 + tp3) / 3
        escreva("\n\nO valor médio dos pcs parcelados é: R$: ", mp, "\n")

    }
}