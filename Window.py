import pygame

pygame.init()

xPlayerPosition= 16
yPlayerPosition= 630
playerWidth = 40
playerHeight = 60
windowWidth = 900
windowHeight = 700
velocity = 15
running = True

window = pygame.display.set_mode((windowWidth, windowHeight))

background_colour = (255, 255, 255)
pygame.display.set_caption('Bubble trouble')

window.fill(background_colour)
pygame.display.flip()

while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and xPlayerPosition > velocity:
        xPlayerPosition -= velocity
    if keys[pygame.K_RIGHT] and xPlayerPosition < windowWidth - playerWidth - velocity:
        xPlayerPosition += velocity

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (xPlayerPosition, yPlayerPosition, playerWidth, playerHeight)) #za iscrtavanje naseg lika
    pygame.display.update()  #da bi se on pojavio na ekranu

pygame.quit()