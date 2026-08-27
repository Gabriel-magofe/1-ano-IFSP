// 6) Dada uma sequência de 5 números inteiros digitados pelo usuário, determinar e exibir a média.

programa
{
	
	funcao inicio()
	{
        inteiro A[5]
        inteiro i
        real B=0

        para(i=0; i<5;i++){
            escreva ("Digite o ", i+1, "° valor: ")
            leia(A[i])
        }
        para(i=0; i<5;i++){
                B= B + A[i]
            }
            B= B/5
        escreva("\n\n Média= ", B)
	}
}