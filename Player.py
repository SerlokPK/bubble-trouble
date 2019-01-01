import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition, image,left_key,right_key):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.image = pygame.image.load(image)
        self.playerWidth = 23
        self.playerHeight = 37
        self.walkingLeft = False
        self.walkingRight = False
        self.velocity = 10
        self.left_key = left_key
        self.right_key = right_key

    



