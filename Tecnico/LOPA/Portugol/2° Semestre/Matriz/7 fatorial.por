//  7) Elaborar um programa que leia uma matriz A de duas dimensões com cinco linhas e quatro colunas. Construir uma matriz B de mesma dimensão, em que elemento seja o fatorial de cada elemento correspondente armazenado na matriz A. Apresentar ao final as matrizes A e B.
programa {
    funcao inteiro fatorial(inteiro n) {
        inteiro r = 1
        para (inteiro i = 1; i <= n; i++) {
            r = r * i
        }
        retorne r
    }
    funcao inicio() {
        
    }
}