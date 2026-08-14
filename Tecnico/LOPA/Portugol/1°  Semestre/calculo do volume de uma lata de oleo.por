programa
{
	inclua biblioteca Matematica --> mat
	
	funcao inicio()
	{
		real R, H, V
		const real PI = 3.141592653589793
		escreva("digite o valor do raio da lata: ")
		leia(R)
		escreva("digite o valor da altura da lata: ")
		leia(H)
		V = PI * mat.potencia(R, 2.0) * H
		escreva("volume da lata de oleo: ",V)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 98; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */