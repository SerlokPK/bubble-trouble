import pygame


class Bonus(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition, image):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.image = pygame.image.load(image)
        self.bonusWidth = 35
        self.bonusHeight = 35
        self.enabled = False
        self.hitbox = (self.xPosition, self.yPosition, 23, 37)