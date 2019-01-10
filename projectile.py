import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        self.image = pygame.image.load("Images/arrow.png")
        self.xPosition = player.xPosition + 6
        self.yPosition = player.yPosition + 36  # head of projectile
        self.velocity = 10
        self.alive = False
        self.hitbox = (self.xPosition, self.yPosition, 8, 480)

    def update_projectile(self):
        if self.alive:
            if self.yPosition > self.velocity:
                self.yPosition -= self.velocity
                self.hitbox = (self.xPosition, self.yPosition, 8, 480)
            else:
                self.alive = False
                self.xPosition = -20
                self.hitbox = (self.xPosition, self.yPosition, 8, 480)
