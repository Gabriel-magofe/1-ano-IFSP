import pygame as pg
import time

pg.init()

screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Cronômetro")

font = pg.font.SysFont(None, 55)

clock = pg.time.Clock()

start_ticks = pg.time.get_ticks()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    seconds = (pg.time.get_ticks() - start_ticks) // 1000
    text = font.render(f"Tempo: {seconds} segundos", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (100, 100))
    pg.display.flip()
    clock.tick(60)

pg.quit()