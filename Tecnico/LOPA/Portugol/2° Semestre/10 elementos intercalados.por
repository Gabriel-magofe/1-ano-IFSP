// 10) Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
programa {
    funcao inicio() {
        inteiro a[10], b[10], c[20], i, n
        para (i = 0; i <= 9; i++) {
            escreva("Digite o ", i+1, "° valor de A: ")
            leia(a[i])
        }
        para (i = 0; i <= 9; i++) {
            escreva("Digite o ", i+1, "° valor de B: ")
            leia(b[i])
        }
        n=0
        para (i = 0; i < 10; i++) {
            c[n]=a[i]
            c[n+1]=b[i]
            n=n+2
        }
        escreva("\nVetor A: ")
        para (i = 0; i < 10; i++) {
            escreva(a[i], " ")
        }
        escreva("\nVetor B: ")
        para (i = 0; i < 10; i++) {
            escreva(b[i], " ")
        }
        escreva("\nVetores intercalados: ")
        para (i = 0; i < 20; i++) {
            escreva(c[i], " ")
        }
    }
}