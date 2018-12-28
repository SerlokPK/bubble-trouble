import pygame

from Player import *

pygame.init()
windowWidth = 900
windowHeight = 700
running = True
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Bubble trouble')
player = Player(16, 630, 'player.png')


def redrawWindow():
    window.fill((255, 255, 255))
    window.blit(player.image, (player.xPosition, player.yPosition))  #iscrtavanje naseg lika
    pygame.display.update()  # da bi se on pojavio na ekranu


while running:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Update(player)
    redrawWindow()

pygame.quit()