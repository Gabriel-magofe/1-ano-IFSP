// 18) Elaborar um programa que leia 15 elementos reais para uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmos tipo e dimensão, observando a seguinte lei de formação: “topo elemento da matriz A que possuir índice par deve ter seu elemento dividido por 2; caso contrário, o elemento da matriz A deve multiplicado por 1.5”. Apresentar os elementos da matriz B.
programa {
    inclua biblioteca Util --> u 
    funcao inicio() {
        inteiro A[16], B[16]
        para (inteiro i = 0; i < 15; i++) {
            A[i]=u.sorteia(1, 100)
            se (A[i]%2==0) {
                B[i]=A[i/2]
            }senao{
                B[i]=A[i]*1.5
            }
        para (i = 0; i < 20; i++) {
            escreva("A[", i+1, "] = ", A[i], " | B[", i, "] = ", B[i], "\n")
        }
        }
    }
}