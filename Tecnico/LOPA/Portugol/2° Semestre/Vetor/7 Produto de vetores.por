// 7) Dados dois vetores A e B, ambos com 5 elementos, determinar o produto desses vetores.

programa
{
	
	funcao inicio()
	{
        inteiro A[5], B[5], C[5]
        inteiro i
        para(i=0; i<5;i++){
            escreva ("Digite o ", i+1, "° valor de A: ")
            leia(A[i])
        }
        escreva("\n\n")
        para(i=0; i<5;i++){
            escreva ("Digite o ", i+1, "° valor de B: ")
            leia(B[i])
        }
        para(i=0; i<5;i++){
                C[i]=A[i]*B[i]
            }
        escreva("\n\nProduto de A e B= ", C)
	}
}