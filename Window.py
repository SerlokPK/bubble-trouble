import pygame

from Player import *

pygame.init()
windowWidth = 900
windowHeight = 700
running = True

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Bubble trouble')
player = Player(16, 630, 'player.png')


def redrawWindow():
    window.fill((255, 255, 255))
    window.blit(player.image, (player.xPosition, player.yPosition))  #iscrtavanje naseg lika
    pygame.display.update()  # da bi se on pojavio na ekranu


while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Update(player)
    redrawWindow()

pygame.quit()