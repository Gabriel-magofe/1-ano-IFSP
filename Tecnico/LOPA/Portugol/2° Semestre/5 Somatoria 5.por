// 5) Considerando 5 números reais digitados pelo usuário e armazenados em um vetor, exibir o valor da somatória dos mesmos.
programa
{
	
	funcao inicio()
	{
        inteiro A[5]
        inteiro B=0, i
        para(i=0; i<5;i++){
            escreva ("Digite o ", i+1, "° valor: ")
            leia(A[i])
        }
        para(i=0; i<5;i++){
                B= B + A[i]
            }
        escreva("\n\n Somatoria= ", B)
	}
}