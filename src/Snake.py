import pygame

class Snake(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.speed = 1
        self.health = 1

    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def collision(self):#,food):
        # Need to add what to do when the snake collides with the wall or itself
        pass
        # self.health -= 1
        

    def snake_grow(self):
        # Need to add how to add onto snake when it eats food
        pass
        #growth_x = 3
        #growth_y = 3
        #self.rect.x += growth_x
        #self.rect.y += growth_y
	
