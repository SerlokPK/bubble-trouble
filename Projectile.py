import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, Player1):
        self.image = pygame.image.load("arrow.png")
        self.xPosition = Player1.xPosition + 6
        self.yPosition = Player1.yPosition + 34
        self.velocity = 10
        self.alive = False
        self.rect = self.image.get_rect()

    def UpdateProjectile(self):

        if self.alive:
            if self.yPosition > self.velocity:
                self.yPosition -= self.velocity
            else:
                self.alive = False
                self.xPosition = -20

