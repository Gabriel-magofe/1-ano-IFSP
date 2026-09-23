// 6) Escreva um programa para ler uma matriz A de duas dimensões com 4 linhas e 3 colunas. Mostre a quantidade de valores pares e impares.

programa {
    funcao inicio() {
        inteiro m[4][3]
        inteiro p=0, im=0, z=0
        para (inteiro i=0;i<4;i++){
            para (inteiro j=0;j<3;j++){
                escreva("Digite o [",i+1,"][",j+1,"] valor da matriz: ")
                leia(m[i][j])
            }
        }
        escreva("Matriz: ")
        para (inteiro i=0;i<4;i++){
        	  escreva("\n")
            escreva("[",m[i][0],",",m[i][1],",",m[i][2],",","]")
        }
        para (inteiro i=0;i<4;i++){
            para (inteiro j=0;j<3;j++){
                se(m[i][j]==0){z=z+1}
                senao se(m[i][j]%2==0){p=p+1}
                senao{im=im+1}
            }
        }
          escreva("\nQuantidade de valores pares:", p,"\n")
		escreva("Quantidade de valores impares:", im,"\n")
		escreva("Quantidade de zeros:", z,"\n")
  }
}