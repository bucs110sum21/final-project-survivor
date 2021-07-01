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
	#self.speed = 2

    def update():
        pass
        #random_x = random.randrange(-2,4)
	#random_y = random.randrange(-2,4)
	#self.rect.x = random_x
	#self.rect.y = random_y
	
