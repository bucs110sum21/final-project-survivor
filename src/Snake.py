import pygame


class Segement(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Snake:
    def __init__(self, name, x, y, img_file):

        # set other attributes
        self.name = name
        self.head = Segment(10, 10, 'assets/snakehead.png')
        self.body = pygame.sprite.Group()
        starting = 2
        for i in range(2):
            self.body.add(Segment(10 * starting, 10, 'assets/snakebody.png'))
            starting += 1

    def move_up(self):
        x = self.head.rect.x
        y = self.head.rect.y
        for index, bsegment in enumerate(self.body):
            xtemp = self.body[index].rect.x
            ytemp = self.body[index].rect.y
            self.body[index].rect.x = x
            self.body[index].rect.y = y
            x = xtemp
            y = ytemp
        self.head.rect.y -= 10

    def move_down(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed


        

    def collision(self):  # ,food):
        return pygame.sprite.spritecollide(self.head, self.body)


    def snake_grow(self):
        # TODO which side to add the tail on
        x = self.body[-1].rect.x + offset  # offset is whatever your gridsixze is
        y = self.body[-1].rect.y + offset
        tail = Segment(x, y, 'assets/snakebody.png')
        self.body.add(tail)
