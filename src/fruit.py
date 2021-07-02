import pygame
import random

class Fruit(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.origin = x
        self.bounce = 1

    def update():
        self.bounce = (self.bounce + 1) % 3
        if self.bounce:
            self.rect.x += 1
        else:
            self.rect.x = self.bounce
