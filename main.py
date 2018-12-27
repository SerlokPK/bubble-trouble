import pygame

from bubble import Bubble


class Program:
    def __init__(self):
        self.background_colour = (255, 255, 255)
        (self.width,self.height) = (900, 700)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bubble = Bubble((150, 50), 15, self.screen)

        self.initializeWindow()


    def initializeWindow(self):
        pygame.display.set_caption('Bubble trouble')
        self.screen.fill(self.background_colour)
        self.bubble.display()
        pygame.display.flip()

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


if __name__ == '__main__':
    Program()