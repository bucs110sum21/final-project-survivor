import pygame
import sys
import random
from src import Snake
from src import fruit

class Controller:
    def __init__(self, width=500, height=500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()

        self.fruits = pygame.sprite.Group()
        num_fruits = 2
        for i in range(num_fruits):
            x = random.randrange(1,500)
            y = random.randrange(1,500)
            self.fruits.add(fruit.Fruit("Apple", x, y, 'assets/apple.png' ))

        self.snake = Snake.Snake("Snake", 250, 250, "assets/snake.png")
        self.state = "GAME"



    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        # pygame.key.set_repeat(1,50)
        while self.state == "GAME":
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.snake.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.snake.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.snake.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.snake.move_right()

            if self.snake.collision():
                self.state = "GAMEOVER"
            self.screen.blit(self.snake.head.image, self.snake.head.rect)
            self.snake.body.draw(self.screen)
            pygame.display.flip()
            	

    def gameOver(self):
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0,0,0))
        self.screen.blit(message, (self.width/2,self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
