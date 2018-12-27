import pygame


class Bubble:
    def __init__(self, position, size,screen):
        self.x, self.y = position
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.screen = screen

    def display(self):
        img = pygame.image.load('rball6.bmp')
        self.screen.blit(img,(400,40))