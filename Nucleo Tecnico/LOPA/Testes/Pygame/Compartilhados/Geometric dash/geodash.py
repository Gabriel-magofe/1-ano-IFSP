import pygame as game


game.init()
saida = 0
morte = 0
while True:


    TELA = game.display.set_mode((800, 520))
    game.display.set_caption("['_']")
    font = game.font.SysFont(None, 55)
   
    vida = 1


    square = game.Rect(100, 400, 80, 80)
    chao = game.Rect(0, 480, 800, 40)


    d_obs = game.Rect(800, 420, 60, 60)


    plataformas = [chao]
    dano = [d_obs]
   
    gravidade = 0
    peso = 0
    pulo = 0
    sauto = -0.65
    pos_y = 0


    vel_x = -0.2


    relogio = game.time.Clock()


    evento = game.event.poll()


    if saida == 1:
            break




    while True and vida == 1:
        dt = relogio.tick(40)




        evento = game.event.poll()


        if evento.type == game.QUIT:
            saida = 1
            break
        #quadrado
        if square.collidelist(plataformas) >= 0:
            gravidade = 0
            peso = 0
            pulo = 0
            sauto = -0.65
            '''if square.colliderect(chao) >= 0:
                square.center = (140, 440)'''
        else:
            gravidade = 1


        if  evento.type == game.KEYDOWN:
            if evento.key == game.K_SPACE:
                if gravidade == 0:
                    pulo = 1
                    pos_y = square.center[1]


        if pulo == 1:
            square.move_ip(0, sauto * dt)
            sauto += 0.025


        if  square.center[1] <= pos_y  - 240:
            pulo = 0
            sauto = -0.65


        if gravidade == 1:
            square.move_ip(0, peso * dt)
            peso += 0.005




        #obstaculo
        d_obs.move_ip(vel_x * dt, 0)
        if d_obs.center[0] <= -30:
            d_obs.x = 800
       
        if square.collidelist(dano) >= 0:
            vida -= 1
            morte += 1


        TELA.fill((48, 50, 164))
        text = font.render(f'mortes: {morte}', True, (255, 255, 255))
   
        game.draw.rect(TELA, (255, 255, 255), chao)
        game.draw.rect(TELA, (240, 240, 240), square)
        game.draw.polygon(TELA, (200, 200, 200), [[d_obs.center[0], d_obs.center[1] - 30], [d_obs.center[0] + 30, d_obs.center[1] + 30], [d_obs.center[0] - 30, d_obs.center[1] + 30]])
        TELA.blit(text, [10, 30])


        game.display.flip()


   
   
game.quit()
