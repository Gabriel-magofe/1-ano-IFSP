import pygame as gam
import random as R


gam.init()
saida = 0
A = 0
B = 0


TELA = gam.display.set_mode([680,460])
gam.display.set_caption("PONG")


fonte = gam.font.SysFont(None, 50)


pong = gam.Rect(323,213,17,17)
pad = gam.Rect(20,190,20,70)
pad2 = gam.Rect(640,190,20,70)
pads = [pad, pad2]


direcao = R.randint(1, 4)




relogio = gam.time.Clock()


vel_x = 0.1
vel_y = 0.1
p_vel_y = 0.27


while True:
    dt = relogio.tick(30)
   
    botao = gam.key.get_pressed()
    event = gam.event.poll()
    if event.type == gam.QUIT:
        saida = 1
        break
    if botao[gam.K_s] and pad.center[1] <= 415:
        pad.move_ip(0,p_vel_y*dt)
    if botao[gam.K_w] and pad.center[1] >= 45:
        pad.move_ip(0,-p_vel_y*dt)
    if botao[gam.K_DOWN] and pad2.center[1] <= 415:
        pad2.move_ip(0,p_vel_y*dt)
    if botao[gam.K_UP] and pad2.center[1] >= 45:
        pad2.move_ip(0,-p_vel_y*dt)
   


   
    if direcao == 1:
        pong.move_ip(vel_x*dt,vel_y*dt)
    if direcao == 2:
        pong.move_ip(-vel_x*dt,vel_y*dt)
    if direcao == 3:
        pong.move_ip(vel_x*dt,-vel_y*dt)
    if direcao == 4:
        pong.move_ip(-vel_x*dt,-vel_y*dt)


    if pong.center[1] >= 443:
        vel_y = -vel_y
    if pong.center[1] <= 0:
        vel_y = -vel_y


    if pong.collidelist(pads) >= 0:
        if vel_x > 0:
            vel_x += R.randint(0, 5)/100
        else:
            vel_x += -(R.randint(0, 5)/100)
        if vel_y > 0:
            vel_y += R.randint(0, 5)/100
        else:
            vel_y += -(R.randint(0, 5)/100)
        vel_x = -vel_x
        p_vel_y += 0.27


    if pong.center[0] >= 670:
        A += 1
        vel_x = 0.1
        vel_y = 0.1
        direcao = R.randint(1, 4)
        p_vel_y = 0.27
        pong.topleft = 323,213
    if pong.center[0] <= 10:
        B += 1
        vel_x = 0.1
        vel_y = 0.1
        direcao = R.randint(1, 4)
        p_vel_y = 0.27
        pong.topleft = 323,213
   


    text = fonte.render(f"{A} : {B}", True, (255,255,255))


    TELA.fill((10,10,10))
    gam.draw.rect(TELA, (245,245,245), pong)
    for i in pads:
        gam.draw.rect(TELA, (245,245,245), i)
   
    TELA.blit(text, [320, 30])
       
    gam.display.flip()


gam.quit()
