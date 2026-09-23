// 5) Construa um algoritmo que, para uma matriz 4 x 3, calcule a soma dos elementos de cada uma das linhas e escreva as somas obtidas. O algoritmo deve mostrar também o número da linha que apresentou a maior soma.
programa {
    funcao inicio() {
        inteiro m[4][3], s[4]
        inteiro s1 = 0, ma = 0, l=0, i, j
        para (i=0;i<4;i++){
            para (j=0;j<3;j++){
                escreva("Digite o [",i+1,"][",j+1,"] valor da matriz: ")
                leia(m[i][j])
            }
        }
        escreva("Matriz: ")
        para (i=0;i<4;i++){
        	  escreva("\n")
            escreva("[",m[i][0],",",m[i][1],",",m[i][2],"]")
        }
        para (i=0;i<4;i++){
            para (j=0;j<3;j++){
                s1=s1+m[i][j]
            }
            s[i]=s1
            s1=0
        }
        escreva("\n")
        para (i=0;i<4;i++){
        	escreva("Soma da ",i+1,"º linha: ",s[i],"\n")
        	}
        	para (i=0;i<4;i++){
        		se (s[i]>ma){
        			ma=s[i]
        			l=i
        			}
        		}
        	escreva("maior soma foi ",ma," na linha ", l+1)
        }
    }