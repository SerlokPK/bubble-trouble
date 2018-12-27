import pygame,math


class Bubble:
    def __init__(self, position,screen):
        self.x, self.y = position
        self.screen = screen
        self.speed = 0
        self.angle = 0

    def display(self):
        img = pygame.image.load('rball6.bmp')
        self.screen.blit(img,(self.x,self.y))

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed