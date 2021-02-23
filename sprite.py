import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_key):
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(1, 0)
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT