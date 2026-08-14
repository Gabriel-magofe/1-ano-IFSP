programa {
    funcao inicio() {
        
     inteiro a[5], i, pos = -1
		logico verifica = falso

		para(i = 0; i <= 4; i++){
			escreva("Digite o ", i+1, "° elemento de A: ")
			leia(a[i])
		}

		para(i = 0; i <= 4; i++){
			se(a[i] < 0){
				verifica = verdadeiro
				pos = i+1
				pare
			}
		}
		se(verifica == verdadeiro){
			escreva("Posição: ", pos)
		}senao{
			escreva(" Não há número negativo.")
		}
	}

        
    }
}