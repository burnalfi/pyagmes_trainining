from sprite import Player

import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
player = Player()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))
    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)

    screen.blit(player.surf , player.rect)
    
    pygame.display.flip()