import pygame

from Player import *
from playerMovement import PlayerMovement
from Projectile import *
from bubble import Bubble


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
        self.projectile = Projectile(self.player1)

        self.bubbleSize = 81  # size of bubble
        self.positionOfBall = (400, 50)
        self.bubble = Bubble(self.positionOfBall, self.window, self.running, (self.windowWidth, self.windowHeight),
                             self.bubbleSize)  # check later, it will always be true (?)

    def redrawWindow(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.player1.image,
                         (self.player1.xPosition, self.player1.yPosition))  # iscrtavanje naseg player1
        self.window.blit(self.player2.image,
                         (self.player2.xPosition, self.player2.yPosition))  # iscrtavanje naseg player2
        self.window.blit(self.projectile.image, (self.projectile.xPosition, self.projectile.yPosition))
        self.bubble.move_ball()
        pygame.display.update()  # da bi se oni pojavili na ekranu

    def runGame(self):
        self.bubble.init_ball(1)
        while self.running:
            self.clock.tick(40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            PlayerMovement.UpdatePlayer(self, self.player1)
            PlayerMovement.UpdatePlayer(self, self.player2)
            UpdateProjectile(self.projectile)
            self.redrawWindow()

    pygame.quit()
