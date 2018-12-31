import pygame

from Player import *
from playerMovement import PlayerMovement
from Projectile import *

pygame.init()
windowWidth = 900
windowHeight = 700
running = True
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Bubble trouble')
player1 = Player(16, 630, 'player.png',pygame.K_a,pygame.K_d)
player2 = Player(860, 630, 'player2.png',pygame.K_LEFT,pygame.K_RIGHT)
projectile = Projectile(player1)


def redrawWindow():
    window.fill((255, 255, 255))
    window.blit(player1.image, (player1.xPosition, player1.yPosition))  #iscrtavanje naseg player1
    window.blit(player2.image, (player2.xPosition, player2.yPosition))  # iscrtavanje naseg player2
    window.blit(projectile.image, (projectile.xPosition, projectile.yPosition))
    pygame.display.update()  # da bi se oni pojavili na ekranu


while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    PlayerMovement.UpdatePlayer(player1)
    PlayerMovement.UpdatePlayer(player2)
    UpdateProjectile(projectile)
    redrawWindow()

pygame.quit()