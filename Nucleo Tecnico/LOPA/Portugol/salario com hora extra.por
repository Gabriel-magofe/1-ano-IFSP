programa
{
	
	funcao inicio()
	{
		real h, r, o, i, l, q
		escreva("Horas trabalhadas: ")
		leia(h)
		se(h<=176){
		r=h*10
		escreva("salario: ",r )
		}senao{
			o=176*10
			i=h-176
			l=i*20
			q=o+l
			escreva("salario: ",q )
			}
		
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 138; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */