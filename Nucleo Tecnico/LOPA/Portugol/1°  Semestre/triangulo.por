programa
{
	funcao inicio()
	{
		real A, B, C
		
		escreva("Digite o valor do lado A do triângulo: ")
		leia(A)
		escreva("Digite o valor do lado B do triângulo: ")
		leia(B)
		escreva("Digite o valor do lado C do triângulo: ")
		leia(C)

		se (A <= 0 ou B <= 0 ou C <= 0)
		{
			escreva("Os lados devem ser maiores que zero.")
		}
		senao
		{
			se (A < B + C e B < A + C e C < A + B)
			{
				se (A == B e B == C)
				{
					escreva("O triângulo é equilátero.")
				}
				senao se (A == B ou A == C ou B == C)
				{
					escreva("O triângulo é isósceles.")
				}
				senao
				{
					escreva("O triângulo é escaleno.")
				}
			}
			senao
			{
				escreva("Os lados fornecidos não formam um triângulo.")
			}
		}
	}
}
