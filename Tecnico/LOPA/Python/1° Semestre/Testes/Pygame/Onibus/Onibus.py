import pygame
from pygame.locals import *
from sys import exit

pygame.init()

x=640
y=480
px=0
py=0
vel_px=0.25
screen = pygame.display.set_mode((x, y), 0, 32)
pygame.display.set_caption("Teste")

clock = pygame.time.Clock()
while True:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    class onibus:
        pygame.draw.circle(screen, (100, 100, 100), (40+px, 450+py), 20)
        pygame.draw.circle(screen, (255, 255, 
        255), (220+px, 450+py), 20)
        pygame.draw.rect(screen, (255, 255, 255), (0+px, 300+py, 320, 180))
        pygame.draw.rect(screen, (45, 45, 45), (0+px, 300+py, 320, 150))
        pygame.draw.rect(screen, (0, 200, 255), (250+px, 325+py, 70, 40))
        pygame.draw.circle(screen, (0, 0, 0), (40+px, 450+py), 30)
        pygame.draw.circle(screen, (0, 0, 0), (220+px, 450+py), 30)

        
    px+=vel_px * dt
    if px >= 639:
        px = -320
        
    posicao_mouse = pygame.mouse.get_pos()
    print(f"Coordenadas do Mouse: X={posicao_mouse[0]}, Y={posicao_mouse[1]}")

    pygame.display.update()