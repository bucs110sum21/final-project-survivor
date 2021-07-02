import pygame


class Segment(pygame.sprite.Sprite):
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
        self.head = Segment(10, 10, 'assets/new_snake.png')
        self.body = pygame.sprite.Group()
        self.direction = "move_down"
        starting = 2
        for i in range(2):
            self.body.add(Segment(10 * starting, 10, 'assets/new_snake.png'))
            starting += 1

    def move_up(self):
        x = self.head.rect.x
        y = self.head.rect.y
        for bsegment in self.body:
            xtemp = bsegment.rect.x
            ytemp = bsegment.rect.y
            bsegment.rect.x = x
            bsegment.rect.y = y
            x = xtemp
            y = ytemp
        self.head.rect.y -= 10
        self.direction = "move_up"

    def move_down(self):
        x = self.head.rect.x
        y = self.head.rect.y
        for bsegment in self.body:
            xtemp = bsegment.rect.x
            ytemp = bsegment.rect.y
            bsegment.rect.x = x
            bsegment.rect.y = y
            x = xtemp
            y = ytemp
        self.head.rect.y += 10
        self.direction = "move_down"

    def move_left(self):
        x = self.head.rect.x
        y = self.head.rect.y
        for bsegment in self.body:
            xtemp = bsegment.rect.x
            ytemp = bsegment.rect.y
            bsegment.rect.x = x
            bsegment.rect.y = y
            x = xtemp
            y = ytemp
        self.head.rect.x -= 10
        self.direction = "move_left"

    def move_right(self):
        x = self.head.rect.x
        y = self.head.rect.y
        for bsegment in self.body:
            xtemp = bsegment.rect.x
            ytemp = bsegment.rect.y
            bsegment.rect.x = x
            bsegment.rect.y = y
            x = xtemp
            y = ytemp
        self.head.rect.x += 10
        self.direction = "move_right"


    def collision(self):  
        return pygame.sprite.spritecollide(self.head, self.body, False)


    def snake_grow(self):
        # TODO which side to add the tail on
        body_list = self.body.sprites()
        x = body_list[-1].rect.x
        y = body_list[-1].rect.y
        if body_list[-1].rect.x < body_list[-2].rect.x:
            x = body_list[-1].rect.x - 10
        elif body_list[-1].rect.x > body_list[-2].rect.x:
            x = body_list[-1].rect.x + 10
        elif body_list[-1].rect.y < body_list[-2].rect.y:
            y = body_list[-1].rect.y + 10
        elif body_list[-1].rect.y > body_list[-2].rect.y:
            y = body_list[-1].rect.y - 10

        tail = Segment(x, y, 'assets/new_snake.png')
        self.body.add(tail)
        

    def update(self):
        if self.direction == "move_up":
            self.move_up()
        elif self.direction == "move_down":
            self.move_down()
        elif self.direction == "move_left":
            self.move_left()
        else:
            self.move_right()
