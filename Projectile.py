import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, Player1):
        self.image = pygame.image.load("Images/arrow.png")
        self.xPosition = Player1.xPosition + 6
        self.yPosition = Player1.yPosition + 34     # head of projectile
        self.velocity = 10
        self.alive = False
        self.hitbox = (self.xPosition, self.yPosition, 8, 480)

    def UpdateProjectile(self):
        if self.alive:
            if self.yPosition > - self.hitbox[3]:
                self.yPosition -= self.velocity
                self.hitbox = (self.xPosition, self.yPosition, 8, 480)
            else:
                self.alive = False
                self.xPosition = -20
                self.hitbox = (self.xPosition, self.yPosition, 8, 480)

