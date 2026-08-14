import pygame as gam


gam.init()


TELA = gam.display.set_mode([660, 500])
gam.display.set_caption("flapy zóio")


class Player(gam.sprite.Sprite):
    def __init__(self):
        gam.sprite.Sprite.__init__(self)
        self.quadros = []
        self.quadros.append(gam.image.load("flapy/zóio_d.png"))
        self.quadros.append(gam.image.load("flapy/zóio 2_d.png"))
        self.quadros.append(gam.image.load("flapy/zóio_e.png"))
        self.quadros.append(gam.image.load("flapy/zóio 2_e.png"))
        self.atual = 0
        self.image = self.quadros[self.atual]
        self.image = gam.transform.scale(self.image, (29*1.8, 27*1.8))
       
        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 220


        self.direction = 1
        self.vida = 1
        self.tiros = 0




    def jump(self,sauto, dt, direcao):
        if direcao == 1:
            self.atual = 1
        else:
            self.atual = 3
        self.rect.move_ip(0, sauto * dt)
    def queda(self, direcao, sauto, dow):
        if direcao == 1 and sauto == 0:
            self.atual = 0
        elif direcao == 0 and sauto == 0:
            self.atual = 2
        self.rect.move_ip(0, dow * dt)
    def move(self, dir, dt, pulo):
        if dir == 0:
            self.rect.move_ip(-0.16 * dt, 0)
            if pulo == 1:
                self.atual = 3
            else:
               self.atual = 2


        else:
            self.rect.move_ip(0.16 * dt, 0)
            if pulo == 1:
                self.atual = 1
               
            else:
                self.atual = 0
    def inicio(self):
        self.rect.topleft = 300, 220
               




    def update(self):
        self.image = self.quadros[self.atual]
        self.image = gam.transform.scale(self.image, (29*1.8, 27*1.8))
       


class Damege(gam.sprite.Sprite):
    def __init__(self, tipo):
        gam.sprite.Sprite.__init__(self)
        self.espinhos_e = []
        self.espinhos_d = []
        self.espinhos_dow = []
        self.espinhos_up = []


        self.espinhos_d.append(gam.image.load("flapy/espinho_d.png"))
        self.espinhos_e.append(gam.image.load("flapy/espinho_e.png"))
        self.espinhos_dow.append(gam.image.load("flapy/espinho_dow.png"))
        self.espinhos_up.append(gam.image.load("flapy/espinho_up.png"))
        self.atual = 0
        self.image = 0


        self.tipo = tipo


        if self.tipo == 1:
            self.atual = 0
            self.image = self.espinhos_d[self.atual]
            self.image = gam.transform.scale(self.image, (26*1.8, 23*1.8))
        elif self.tipo == 2:
            self.atual = 0
            self.image = self.espinhos_e[self.atual]
            self.image = gam.transform.scale(self.image, (26*1.8, 23*1.8))
        elif self.tipo == 3:
            self.atual = 0
            self.image = self.espinhos_dow[self.atual]
            self.image = gam.transform.scale(self.image, (353*1.8, 26*1.8))
           
        elif self.tipo == 4:
            self.atual = 0
            self.image = self.espinhos_up[self.atual]
            self.image = gam.transform.scale(self.image, (353*1.8, 26*1.8))
           
        self.rect = self.image.get_rect()
        self.rect.topleft = -50, -50


    def position(self, x, y):
        self.rect.topleft = x, y


    def animar(self):
        pass


    def update(self):
        if self.tipo == 1:
            self.image = self.espinhos_d[self.atual]
        elif self.tipo == 2:
            self.image = self.espinhos_e[self.atual]
        elif self.tipo == 3:
            self.image = self.espinhos_dow[self.atual]  
        elif self.tipo == 4:
            self.image = self.espinhos_up[self.atual]
           
        if self.tipo == 1 or self.tipo == 2:
            self.image = gam.transform.scale(self.image, (26*1.8, 23*1.8))
        if self.tipo == 3:
            self.image = gam.transform.scale(self.image, (353*1.8, 26*1.8))
            self.rect.topleft = 10, 453
        if self.tipo == 4:
            self.image = gam.transform.scale(self.image, (353*1.8, 26*1.8))
            self.rect.topleft = 10, 0


class Coin(gam.sprite.Sprite):
    def __init__(self):
        gam.sprite.Sprite.__init__(self)
        self.quadros = []
        self.quadros.append(gam.image.load("flapy/gota 1.png"))
        self.quadros.append(gam.image.load("flapy/gota 2.png"))
        self.quadros.append(gam.image.load("flapy/gota 3.png"))
        self.quadros.append(gam.image.load("flapy/gota 4.png"))
        self.quadros.append(gam.image.load("flapy/gota 5.png"))
        self.atual = 2
        self.vel_anm = 0.25
        self.image = self.quadros[self.atual]
        self.image = gam.transform.scale(self.image, (13*1.85, 19*1.85))


        self.rect = self.image.get_rect()
        self.rect.topleft = -50, -50


    def position(self, x, y):
        self.rect.topleft = x, y


    def animation(self):
        self.atual += self.vel_anm
        if self.atual > 4 or self.atual < 0:
            self.vel_anm = -self.vel_anm


   
    def update(self):
       
        self.image = self.quadros[int(self.atual)]
        if int(self.atual) == 0 or int(self.atual) == 4:
            self.image = gam.transform.scale(self.image, (13*1.85, 18*1.85))
        else:
            self.image = gam.transform.scale(self.image, (13*1.85, 19*1.85))






zoio = Player()


gota = Coin()


espinho_d1 = Damege(1)
espinho_e1 = Damege(2)
espinho_d2 = Damege(1)
espinho_e2 = Damege(2)
espinho_dow = Damege(3)
espinho_up = Damege(4)


all_quadros = gam.sprite.Group()
all_quadros.add(zoio)
all_quadros.add(espinho_dow)
all_quadros.add(espinho_up)
all_quadros.add(espinho_d1)
all_quadros.add(espinho_e1)
all_quadros.add(espinho_d2)
all_quadros.add(espinho_e2)
all_quadros.add(gota)


font = gam.font.SysFont(None, 45)
font0 = gam.font.SysFont(None, 35)
font1 = gam.font.SysFont(None, 80)


dano = [espinho_dow.rect, espinho_up.rect, espinho_d1.rect, espinho_e1.rect, espinho_d2.rect, espinho_e2.rect]


mortes = 0


clock = gam.time.Clock()


temp = 0


saida = 0


pulo = 0
sauto = -0.65
gravidade = 0
direction = 1
play = 0


T = 0
rod = 0


som_morte = gam.mixer.Sound("flapy/freesound_community-videogame-death-sound-43894 (mp3cut.net).mp3")


musica_fundo = gam.mixer.music.load("flapy/Sans.oga")
gam.mixer.music.play(-1)


while True:
    espinho_d1.position(-50,-50)
    espinho_e1.position(-50,-50)
    espinho_d2.position(-50,-50)
    espinho_e2.position(-50,-50)
    gota.position(-50,-50)
    zoio.tiros = 0
    rod = 0
    dt = clock.tick(30)


    event = gam.event.poll()
    if saida == 1 or event.type == gam.QUIT:
        saida = 1
        break
    if event.type == gam.KEYDOWN:
        if event.key == gam.K_SPACE:
            play = 1
            musica_fundo = gam.mixer.music.load("flapy/lofiewme-pixel-fantasia-355123.mp3")
            gam.mixer.music.play(-1)
            rod = 0
            gravidade = 0
            direction = 1
            zoio.inicio()


    TELA.fill((23, 143, 176))
    T_inicio = font1.render('FLAPY ZÓIO', True, (32, 37, 105))
    T_start1 = font.render('Press Start', True, (75, 85, 242))
    T_start2 = font.render('Press Start', True, (77, 226, 242))
    T_start = [T_start1, T_start2]
    T_opicao = font0.render('Aperte espaço', True, (95, 15, 100))
   
    T += 0.1
    if T >= 2:
        T = 0


    TELA.blit(T_inicio, [180, 110])
    TELA.blit(T_start[int(T)], [250, 170])
    TELA.blit(T_opicao, [250,255])
    gam.display.flip()


    while play == 1 and zoio.vida >= 1:
        dt = clock.tick(30)


        for event in gam.event.get():
            if event.type == gam.QUIT:
                saida = 1
                break
            if event.type == gam.KEYDOWN:
                if event.key == gam.K_SPACE:
                    gravidade = 0
                    pulo = 1




        if pulo == 1:
            zoio.jump(sauto, dt, direction)
            sauto += 0.05
         
        if sauto >= 0:
            pulo = 0
            sauto = -0.65
       
        gravidade += 0.01
        zoio.queda(direction, sauto, gravidade)


        zoio.move(direction, dt, pulo)


        if rod == 1:
            espinho_d1.position(612, 340)
            if gam.time.get_ticks() - temp >= 500:
                espinho_e1.position(0, 120)
        if rod == 2:
            espinho_d1.position(612, 320)
            espinho_d2.position(612, 260)
            if gam.time.get_ticks() - temp >= 500:
                espinho_e1.position(0, 130)
                espinho_e2.position(0, 190)
           


        if zoio.rect.center[0] > 632:
            direction = 0
        elif zoio.rect.center[0] < 28:
            temp = gam.time.get_ticks()
           
            rod+=1
            direction = 1
       
        if zoio.rect.collidelist(dano) >= 0:
            som_morte.play()
            zoio.vida = 0


       


        TELA.fill((22, 25, 74))
        #gam.draw.rect(TELA, (240, 240, 240), gota.rect)
        '''gam.draw.rect(TELA, (240, 240, 240), espinho_up.rect)
        gam.draw.rect(TELA, (240, 240, 240), espinho_dow.rect)'''
        all_quadros.draw(TELA)
        all_quadros.update()


        if rod > 2:
            rod = 0
            play = 2
       
        gam.display.flip()


    while play == 2 and zoio.vida >= 1:
        dt = clock.tick(30)


        for event in gam.event.get():
            if event.type == gam.QUIT:
                saida = 1
                break
            if event.type == gam.KEYDOWN:
                if event.key == gam.K_SPACE:
                    gravidade = 0
                    pulo = 1




        if pulo == 1:
            zoio.jump(sauto, dt, direction)
            sauto += 0.05
         
        if sauto >= 0:
            pulo = 0
            sauto = -0.65
       
        gravidade += 0.01
        zoio.queda(direction, sauto, gravidade)


        zoio.move(direction, dt, pulo)


        if rod == 0:
            if zoio.tiros == 0:
                gota.position(100, 400)


            espinho_d1.position(612, 320)
            espinho_d2.position(612, 260)
            if gam.time.get_ticks() - temp >= 500:
                espinho_e1.position(0, 130)
                espinho_e2.position(0, 190)


        if rod == 1:
            if zoio.tiros == 1:
                gota.position(300, 60)


            espinho_d1.position(612, 130)
            espinho_d2.position(612, 330)
            if gam.time.get_ticks() - temp >= 500:
                espinho_e1.position(0, 130)
                espinho_e2.position(0, 330)
        if rod == 2:
            if zoio.tiros == 2:
                gota.position(300, 490)


            espinho_d1.position(612, 130)
            espinho_d2.position(612, 330)
            if gam.time.get_ticks() - temp >= 500:
                espinho_e1.position(0, 130)
                espinho_e2.position(0, 330)
       
   
           
           


        if zoio.rect.center[0] > 632:
            direction = 0
        elif zoio.rect.center[0] < 28:
            temp = gam.time.get_ticks()
            if rod != zoio.tiros:
                rod+=1
            direction = 1
       
        if zoio.rect.collidelist(dano) >= 0:
            som_morte.play()
            zoio.vida = 0
        if zoio.rect.colliderect(gota.rect):
            zoio.tiros += 1
            gota.position(-50, -50)


       


        gota.animation()
       
        tiro = font0.render(f'TIROS: {zoio.tiros}', True, (95, 15, 100))


        TELA.fill((22, 25, 74))
        '''gam.draw.rect(TELA, (240, 240, 240), gota.rect)
        gam.draw.rect(TELA, (240, 240, 240), espinho_up.rect)
        gam.draw.rect(TELA, (240, 240, 240), espinho_dow.rect)'''
        all_quadros.draw(TELA)
        all_quadros.update()
        TELA.blit(tiro, [10, 30])


        if rod > 3:
            rod = 0
            play = 3
       
        gam.display.flip()


    if zoio.vida == 0:
        # gam.mixer.music
        musica_fundo = gam.mixer.music.load("flapy/noahbroah-pixel-mist-473049 (mp3cut.net) (1).mp3")
        gam.mixer.music.play(-1)
    while zoio.vida < 1:
        dt = clock.tick(30)


        event = gam.event.poll()
        if saida == 1 or event.type == gam.QUIT:
            saida = 1
            break
        if event.type == gam.KEYDOWN:
            musica_fundo = gam.mixer.music.load("flapy/Sans.oga")
            gam.mixer.music.play(-1)
            zoio.vida = 1
            play = 0
            break
       
        T_start1 = font1.render('GAME OVER', True, (255, 255, 255))
        T_start2 = font1.render('GAME OVER', True, (180, 180, 180))
        T_start = [T_start1, T_start2]
       
        T += 0.1
        if T >= 2:
            T = 0
       
        zoio.vida += 0.005
        if zoio.vida >= 1:
            musica_fundo = gam.mixer.music.load("flapy/Sans.oga")
            gam.mixer.music.play(-1)
            play = 0


        TELA.fill((0,0,0))
        TELA.blit(T_start[int(T)], [180, 190])
        gam.display.flip()




           


gam.quit()
