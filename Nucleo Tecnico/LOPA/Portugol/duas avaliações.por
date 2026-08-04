programa
{
	
	funcao inicio()
	{
		real n1, n2, m
		escreva("Digite a nota da primeira avaliação: ")
		leia(n1)
		escreva("Digite a nota da segunda avaliação: ")
		leia(n2)
		m=(n1+n2)/2
		se(m>=6){
			escreva("Aprovado com media: ", m)
		}senao{
			escreva("Reprovado com media: ", m)
			}

	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 186; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */