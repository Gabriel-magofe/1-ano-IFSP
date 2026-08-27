    // 12) Elaborar um programa que efetue a leitura de dez valores para uma matriz A do tipo vetor. Mostre a quantidade de valores positivos e negativos.
programa {
    funcao inicio() {
        inteiro a[10], p= 0, n= 0, z= 0
        para (inteiro i = 0; i < 10; i++) {
            escreva("digite o ", i+1, "º valor:")
            leia(a[i])
        }
        para (i = 0; i < 9; i++) {
            se(a[i]>0){
                p++
            }
            senao se(a[i]<0){
                n++
            }
            senao{
                z++
            }
        }
        escreva("Quantidade de valores positivos: ", p)
        escreva("\nQuantidade de valores negativos: ", n)
        escreva("\nQuantidade de valores zero: ", z)

    }
}