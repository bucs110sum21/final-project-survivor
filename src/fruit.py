import pygame
import random

class Fruit(pygame.sprite.Sprite):
    def __init(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name

    def update():
        pass
