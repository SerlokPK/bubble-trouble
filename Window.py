import pygame

from Player import *
from playerMovement import PlayerMovement
from Projectile import *

class Window:
    def __init__(self):
        pygame.init()
        self.windowWidth = 900
        self.windowHeight = 700
        self.running = True
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption('Bubble trouble')
        self.player1 = Player(16, 630, 'player.png', pygame.K_a, pygame.K_d)
        self.player2 = Player(860, 630, 'player2.png', pygame.K_LEFT, pygame.K_RIGHT)


    def redrawWindow(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.player1.projectile.image, (self.player1.projectile.xPosition, self.player1.projectile.yPosition))
        self.window.blit(self.player2.projectile.image, (self.player2.projectile.xPosition, self.player2.projectile.yPosition))
        self.window.blit(self.player1.image, (self.player1.xPosition, self.player1.yPosition))  #iscrtavanje naseg player1
        self.window.blit(self.player2.image, (self.player2.xPosition, self.player2.yPosition))  # iscrtavanje naseg player2
        pygame.display.update()  # da bi se oni pojavili na ekranu


    def runPlayers(self):
        while self.running:
            self.clock.tick(40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.player1.fire()
                elif keys[pygame.K_KP_ENTER]:
                    self.player2.fire()

            PlayerMovement.UpdatePlayer(self, self.player1)
            PlayerMovement.UpdatePlayer(self, self.player2)
            Projectile.UpdateProjectile(self.player1.projectile)
            Projectile.UpdateProjectile(self.player2.projectile)
            self.redrawWindow()

    pygame.quit()