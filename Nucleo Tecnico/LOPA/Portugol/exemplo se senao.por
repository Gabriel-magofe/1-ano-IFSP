programa
{
	
	funcao inicio()
	{
		real n1, n2,n3, n4,  m
		
		escreva("digite a primeira nota: ")
		leia(n1)
		escreva("digite a segunda nota: ")
		leia(n2)
		escreva("digite a terceira nota: ")
		leia(n3)
		escreva("digite a quarta nota: ")
		leia(n4)

		m= (n1+n2+n3+n4)/4
		
		se(m>=6){
		escreva("aprovado ", "\n", "Média: ",m)
		}senao{
		escreva("reprovado ", "\n", "Média: ")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 393; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */