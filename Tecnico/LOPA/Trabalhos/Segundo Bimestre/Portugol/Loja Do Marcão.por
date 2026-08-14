programa {
    inclua biblioteca Graficos --> g
    inclua biblioteca Mouse --> m
    inclua biblioteca Teclado --> t
    inclua biblioteca Util --> u
    inclua biblioteca Texto --> tx

    funcao inicio() {
        g.iniciar_modo_grafico(verdadeiro)
        g.definir_dimensoes_janela(400, 400)
        g.definir_titulo_janela("Loja do Marcão.exe")
        g.carregar_fonte("./Avianz Trial.ttf")

        cadeia usuario = "", senha = "", usuarios[3], senhas[3]
        logico caixa_usuario = falso, caixa_senha = falso, mostrar_mensagem = falso
        inteiro tecla, mx, my
        caracter letra

        enquanto (verdadeiro) {

            g.limpar()

            se (caixa_usuario) {
                g.definir_cor(g.COR_AZUL)
            } senao {
                g.definir_cor(g.COR_VERMELHO)
            }
            g.desenhar_retangulo(60, 170, 300, 20, verdadeiro, falso)
            g.definir_cor(g.COR_BRANCO)
            g.desenhar_retangulo(61, 171, 298, 18, verdadeiro, verdadeiro)

            se (caixa_senha) {
                g.definir_cor(g.COR_AZUL)
            } senao {
                g.definir_cor(g.COR_VERMELHO)
            }
            g.desenhar_retangulo(60, 220, 300, 20, verdadeiro, falso)
            g.definir_cor(g.COR_BRANCO)
            g.desenhar_retangulo(61, 221, 298, 18, verdadeiro, verdadeiro)
            g.definir_cor(g.COR_PRETO)
            g.desenhar_texto(61, 171, usuario)
            g.desenhar_texto(61, 221, senha)

            g.definir_cor(g.COR_VERMELHO)
            g.desenhar_retangulo(120, 265, 160, 50, falso, verdadeiro)

            g.definir_tamanho_texto(30.0)
            g.definir_fonte_texto("Avianz Trial")
            g.definir_cor(g.COR_VERMELHO)
            g.desenhar_texto(131, 21, "Loja")
            g.desenhar_texto(161, 51, "do")
            g.desenhar_texto(81, 81, "Marcão")
            g.definir_tamanho_texto(29.0)
            g.definir_fonte_texto("Avianz Trial")
            g.definir_cor(g.COR_BRANCO)
            g.desenhar_texto(130, 20, "Loja")
            g.desenhar_texto(160, 50, "do")
            g.desenhar_texto(80, 80, "Marcão")

            g.definir_fonte_texto("impact")
            g.definir_tamanho_texto(18.0)
            g.definir_cor(g.COR_BRANCO)
            g.desenhar_texto(180, 280, "Entrar")

            g.definir_cor(g.COR_BRANCO)
            g.desenhar_texto(60, 150, "Usuario: ")
            g.desenhar_texto(60, 200, "Senha: ")

            se (mostrar_mensagem) {
                g.definir_cor(g.COR_VERDE)
                g.desenhar_texto(60, 340, "Cadastrado com sucesso! Faça login.")
            }

            se (m.botao_pressionado(m.BOTAO_ESQUERDO)) {
                mx = m.posicao_x()
                my = m.posicao_y()

                se (mx >= 61 e mx <= 359 e my >= 265 e my <= 315) {
                    se (usuario != "" e senha != "" e ((usuarios[0] == usuario e senhas[0] == senha) ou (usuarios[1] == usuario e senhas[1] == senha) ou (usuarios[2] == usuario e senhas[2] == senha))) {
                        g.encerrar_modo_grafico()
                        g.iniciar_modo_grafico(verdadeiro)
                        g.definir_dimensoes_janela(800, 600)
                        g.definir_titulo_janela("Compras")

                        inteiro est_bomba = 10, est_motor = 3, est_oleo = 20, est_super = 5
                        inteiro qtd_bomba = 0, qtd_motor = 0, qtd_oleo = 0, qtd_super = 0
                        real preco_bomba = 180.0, preco_motor = 4500.0, preco_oleo = 45.0, preco_super = 2800.0
                        inteiro img_bomba = g.carregar_imagem("./bomba d_agua.png")
                        inteiro img_motor = g.carregar_imagem("./motor.png")
                        inteiro img_oleo = g.carregar_imagem("./óleo.png")
                        inteiro img_super = g.carregar_imagem("./Supercharger.png")
                        inteiro img_marcao = g.carregar_imagem("./Marcão.png")
                        inteiro mx2 = 0, my2 = 0
                        logico tela_resumo = falso, tela_obrigado = falso, pagamento_debito = falso, mouse_solto = verdadeiro

                        enquanto (verdadeiro) {
                            g.limpar()

                            se (tela_obrigado) {
                                g.definir_cor(g.COR_PRETO)
                                g.desenhar_retangulo(0, 0, 800, 600, falso, verdadeiro)
                                g.desenhar_imagem(250, 100, img_marcao)
                                g.definir_fonte_texto("impact")
                                g.definir_tamanho_texto(32.0)
                                g.definir_cor(g.COR_VERDE)
                                g.desenhar_texto(200, 420, "Obrigado pela compra!")
                                g.definir_tamanho_texto(18.0)
                                se (pagamento_debito) {
                                    g.desenhar_texto(280, 460, "Pagamento: Debito")
                                } senao {
                                    g.desenhar_texto(280, 460, "Pagamento: Credito")
                                }
                            } senao se (tela_resumo) {
                                g.definir_cor(g.COR_PRETO)
                                g.desenhar_retangulo(0, 0, 800, 600, falso, verdadeiro)
                                g.definir_fonte_texto("impact")
                                g.definir_tamanho_texto(24.0)
                                g.definir_cor(g.COR_BRANCO)
                                g.desenhar_texto(350, 30, "Resumo")

                                g.definir_tamanho_texto(16.0)
                                inteiro y_linha = 80
                                real total = 0.0

                                se (qtd_bomba > 0) {
                                    g.desenhar_texto(50, y_linha, "Bomba d agua x" + qtd_bomba + "  R$" + (preco_bomba * qtd_bomba))
                                    y_linha = y_linha + 30
                                    total = total + preco_bomba * qtd_bomba
                                }
                                se (qtd_motor > 0) {
                                    g.desenhar_texto(50, y_linha, "Motor x" + qtd_motor + "  R$" + (preco_motor * qtd_motor))
                                    y_linha = y_linha + 30
                                    total = total + preco_motor * qtd_motor
                                }
                                se (qtd_oleo > 0) {
                                    g.desenhar_texto(50, y_linha, "Oleo x" + qtd_oleo + "  R$" + (preco_oleo * qtd_oleo))
                                    y_linha = y_linha + 30
                                    total = total + preco_oleo * qtd_oleo
                                }
                                se (qtd_super > 0) {
                                    g.desenhar_texto(50, y_linha, "Supercharger x" + qtd_super + "  R$" + (preco_super * qtd_super))
                                    y_linha = y_linha + 30
                                    total = total + preco_super * qtd_super
                                }

                                g.definir_tamanho_texto(20.0)
                                g.definir_cor(g.COR_AMARELO)
                                g.desenhar_texto(50, y_linha + 20, "Total: R$" + total)

                                g.definir_cor(g.COR_AZUL)
                                g.desenhar_retangulo(150, 480, 180, 50, falso, verdadeiro)
                                g.definir_cor(g.COR_VERDE)
                                g.desenhar_retangulo(470, 480, 180, 50, falso, verdadeiro)
                                g.definir_fonte_texto("impact")
                                g.definir_tamanho_texto(18.0)
                                g.definir_cor(g.COR_BRANCO)
                                g.desenhar_texto(215, 497, "Debito")
                                g.desenhar_texto(530, 497, "Credito")


                                se (m.botao_pressionado(m.BOTAO_ESQUERDO) e mouse_solto) {
                                    mouse_solto = falso
                                    mx2 = m.posicao_x()
                                    my2 = m.posicao_y()
                                    
                                    se (mx2 >= 150 e mx2 <= 330 e my2 >= 480 e my2 <= 530) {
                                        pagamento_debito = verdadeiro
                                        tela_resumo = falso
                                        tela_obrigado = verdadeiro
                                    }
                                    se (mx2 >= 470 e mx2 <= 650 e my2 >= 480 e my2 <= 530) {
                                        pagamento_debito = falso
                                        tela_resumo = falso
                                        tela_obrigado = verdadeiro
                                    }
                                }
                                	 se (nao m.botao_pressionado(m.BOTAO_ESQUERDO)) {
                                    	mouse_solto = verdadeiro
                                }
                            } senao {
                                g.definir_cor(g.COR_PRETO)
                                g.desenhar_retangulo(0, 0, 800, 600, falso, verdadeiro)

						  g.definir_fonte_texto("Avianz Trial")
                                g.definir_tamanho_texto(22.0)
                                g.definir_cor(g.COR_VERMELHO)
                                g.desenhar_texto(226, 11, "Loja do Marcao")
                                g.definir_fonte_texto("Avianz Trial")
                                g.definir_tamanho_texto(22.0)
                                g.definir_cor(g.COR_BRANCO)
                                g.desenhar_texto(225, 10, "Loja do Marcao")

                                g.desenhar_imagem(30, 60, img_bomba)
                                g.desenhar_imagem(30, 180, img_motor)
                                g.desenhar_imagem(30, 300, img_oleo)
                                g.desenhar_imagem(30, 420, img_super)

						  g.definir_fonte_texto("impact")
                                g.definir_tamanho_texto(14.0)
                                g.definir_cor(g.COR_BRANCO)
                                g.desenhar_texto(160, 70, "Bomba d agua - R$180,00")
                                g.desenhar_texto(160, 85, "Estoque: " + est_bomba + "  Qtd: " + qtd_bomba)
                                g.desenhar_texto(160, 190, "Motor - R$4500,00")
                                g.desenhar_texto(160, 205, "Estoque: " + est_motor + "  Qtd: " + qtd_motor)
                                g.desenhar_texto(160, 310, "Oleo - R$45,00")
                                g.desenhar_texto(160, 325, "Estoque: " + est_oleo + "  Qtd: " + qtd_oleo)
                                g.desenhar_texto(160, 430, "Supercharger - R$2800,00")
                                g.desenhar_texto(160, 445, "Estoque: " + est_super + "  Qtd: " + qtd_super)

                                g.definir_cor(g.COR_VERDE)
                                g.desenhar_retangulo(160, 105, 100, 30, falso, verdadeiro)
                                g.desenhar_retangulo(160, 225, 100, 30, falso, verdadeiro)
                                g.desenhar_retangulo(160, 345, 100, 30, falso, verdadeiro)
                                g.desenhar_retangulo(160, 465, 100, 30, falso, verdadeiro)
                                g.definir_cor(g.COR_PRETO)
                                g.definir_tamanho_texto(14.0)
                                g.desenhar_texto(185, 112, "Comprar")
                                g.desenhar_texto(185, 232, "Comprar")
                                g.desenhar_texto(185, 352, "Comprar")
                                g.desenhar_texto(185, 472, "Comprar")

                                g.definir_cor(g.COR_VERMELHO)
                                g.desenhar_retangulo(300, 540, 200, 40, falso, verdadeiro)
                                g.definir_cor(g.COR_BRANCO)
                                g.definir_tamanho_texto(16.0)
                                g.desenhar_texto(345, 552, "Finalizar Compra")

                                se (nao m.botao_pressionado(m.BOTAO_ESQUERDO)) {
                                    mouse_solto = verdadeiro
                                }
                                se (m.botao_pressionado(m.BOTAO_ESQUERDO) e mouse_solto) {
                                    mouse_solto = falso
                                    mx2 = m.posicao_x()
                                    my2 = m.posicao_y()

                                    se (mx2 >= 160 e mx2 <= 260 e my2 >= 105 e my2 <= 135) {
                                        se (est_bomba > 0) {
                                            qtd_bomba = qtd_bomba + 1
                                            est_bomba = est_bomba - 1
                                        }
                                    }
                                    se (mx2 >= 160 e mx2 <= 260 e my2 >= 225 e my2 <= 255) {
                                        se (est_motor > 0) {
                                            qtd_motor = qtd_motor + 1
                                            est_motor = est_motor - 1
                                        }
                                    }
                                    se (mx2 >= 160 e mx2 <= 260 e my2 >= 345 e my2 <= 375) {
                                        se (est_oleo > 0) {
                                            qtd_oleo = qtd_oleo + 1
                                            est_oleo = est_oleo - 1
                                        }
                                    }
                                    se (mx2 >= 160 e mx2 <= 260 e my2 >= 465 e my2 <= 495) {
                                        se (est_super > 0) {
                                            qtd_super = qtd_super + 1
                                            est_super = est_super - 1
                                        }
                                    }
                                    se (mx2 >= 300 e mx2 <= 500 e my2 >= 540 e my2 <= 580) {
                                        se (qtd_bomba > 0 ou qtd_motor > 0 ou qtd_oleo > 0 ou qtd_super > 0) {
                                            tela_resumo = verdadeiro
                                        }
                                    }
                                }
                            }

                            g.renderizar()
                            u.aguarde(10)
                        }
                    } senao {
                        se (usuarios[0] == "" e senhas[0] == "") {
                            usuarios[0] = usuario
                            senhas[0] = senha
                            usuario = ""
                            senha = ""
                            mostrar_mensagem = verdadeiro
                        } senao se (usuarios[1] == "" e senhas[1] == "") {
                            usuarios[1] = usuario
                            senhas[1] = senha
                            usuario = ""
                            senha = ""
                            mostrar_mensagem = verdadeiro
                        } senao se (usuarios[2] == "" e senhas[2] == "") {
                            usuarios[2] = usuario
                            senhas[2] = senha
                            usuario = ""
                            senha = ""
                            mostrar_mensagem = verdadeiro
                        }
                    }
                }

                se (mx >= 61 e mx <= 359 e my >= 171 e my <= 189) {
                    caixa_usuario = verdadeiro
                    caixa_senha = falso
                }

                se (mx >= 61 e mx <= 359 e my >= 221 e my <= 239) {
                    caixa_usuario = falso
                    caixa_senha = verdadeiro
                }

                tecla = t.ler_tecla()
                se (tecla > 0) {
                    se (tecla == t.TECLA_BACKSPACE) {
                        se (caixa_usuario e tx.numero_caracteres(usuario) > 0) {
                            usuario = tx.extrair_subtexto(usuario, 0, tx.numero_caracteres(usuario) - 1)
                        }
                        se (caixa_senha e tx.numero_caracteres(senha) > 0) {
                            senha = tx.extrair_subtexto(senha, 0, tx.numero_caracteres(senha) - 1)
                        }
                    } senao {
                        letra = t.caracter_tecla(tecla)
                        se (caixa_usuario) {
                            usuario = usuario + letra
                        }
                        se (caixa_senha) {
                            senha = senha + letra
                        }
                    }
                }
            }

            g.renderizar()
            u.aguarde(10)
        }
    }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 17021; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */