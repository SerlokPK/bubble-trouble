import pygame

pygame.init()

x=50
y=50
playerWidth = 40
playerHeight = 60
vel = 15
running = True

window = pygame.display.set_mode((900, 700))

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

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (x, y, playerWidth, playerHeight)) #za iscrtavanje naseg lika
    pygame.display.update()  #da bi se on pojavio na ekranu

pygame.quit()