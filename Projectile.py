import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, Player1):
        self.image = pygame.image.load("arrow.png")
        self.xPosition = Player1.xPosition
        self.yPosition = Player1.yPosition
        self.velocity = 10
        self.alive = False
        super().__init__()

def UpdateProjectile(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:  #ako je stisnut space
        self.alive = True  #aktiviramo projektil
        if self.alive:
            if self.yPosition > self.velocity:
                self.yPosition -= self.velocity
            else:
                self.alive = False
                self.kill()
