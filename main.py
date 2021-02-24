from sprite import Player, Enemy, Cloud, Bullet

import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_SPACE

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

running = True
player = Player()
    
clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
# bullet = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            elif event.key == K_SPACE:
                new_bullet = Bullet()
                bullet.add(new_bullet)
                all_sprites.add(new_bullet)
                                
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    screen.fill((135, 206, 250))

    pressed_key = pygame.key.get_pressed()
    player.update(pressed_key)

    enemies.update()
    clouds.update()
    bullet.update()    

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
    
    pygame.display.flip()

    clock.tick(30)