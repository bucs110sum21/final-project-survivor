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
        self.name = name
        self.head = Segment(10, 10, 'assets/new_snake.png')
        self.body = pygame.sprite.Group()
        self.direction = "move_down"
        starting = 2
        for i in range(2):
            self.body.add(Segment(10 * starting, 10, 'assets/new_snake.png'))
            starting += 1

    def move_up(self):
        '''
        Moves the snake upwards
        Args:
          self
        Return:
          None
        '''
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
        '''
        Moves the snake downwards
        Args:
          self
        Return:
          None
        '''
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
        '''
        Moves the snake to the left
        Args:
          self
        Return:
          None
        '''
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
        '''
        Moves the snake to the right
        Args:
          self
        Return:
          None
        '''
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
        '''
        Returns true or false bassed on if the snake collides with itself
        Args:
          self
        Return:
          True if the snake head collides with its body
        '''
        return pygame.sprite.spritecollide(self.head, self.body, False)


    def snake_grow(self):
        '''
        Adds a segment to the snake based on its direction
        Args:
          self
        Return:
          None
        '''
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
        '''
        Updates the snake to move constanly based on its current direction
        Args:
          self
        Return:
          None
        '''
        if self.direction == "move_up":
            self.move_up()
        elif self.direction == "move_down":
            self.move_down()
        elif self.direction == "move_left":
            self.move_left()
        else:
            self.move_right()
