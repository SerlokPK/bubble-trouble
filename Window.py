import pygame

from Player1 import *
from Player2 import *

pygame.init()
windowWidth = 900
windowHeight = 700
running = True
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Bubble trouble')
player1 = Player1(16, 630, 'player.png')
player2 = Player2(860, 630, 'player2.png')


def redrawWindow():
    window.fill((255, 255, 255))
    window.blit(player1.image, (player1.xPosition, player1.yPosition))  #iscrtavanje naseg player1
    window.blit(player2.image, (player2.xPosition, player2.yPosition))  # iscrtavanje naseg player2
    pygame.display.update()  # da bi se oni pojavili na ekranu


while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    UpdatePlayer1(player1)
    UpdatePlayer2(player2)
    redrawWindow()

pygame.quit()