//15) Elaborar um programa que leia uma matriz A do tipo vetor com 15 elementos inteiros. Construir uma matriz B de mesmo tipo, e cada elemento da matriz B deve ser o resultado da fatorial correspondente de cada elemento da matriz A. Apresentar as matrizes A e B.
programa
{
	
	funcao inicio()
	{
		inteiro a[15], b[15], c=1, i, d, f

		para(i = 0; i <=14; i++){
			escreva("Digite o ", i + 1, "º elemento de A:")
			leia(a[i])
		}

		para(i = 0; i <=14; i++){
			b[i]=1
			d=a[i]
			f=a[i]
			enquanto(d>0){
				c=a[i]
				b[i]=b[i]*(c-(f-1))
				d--
				f--
			}
		}
		para(i=0;i<15;i++){
			escreva("A= ",a[i]," B= ",b[i])
		}
	}
}