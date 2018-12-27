import pygame


class Program():
    def __init__(self):
        background_colour = (255, 255, 255)
        (width, height) = (900, 700)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Bubble trouble')
        screen.fill(background_colour)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


if __name__ == '__main__':
    Program()