import pygame, random, math

from bubble import Bubble


class Program:
    def __init__(self):
        self.running = True
        self.number_of_bubble = 1
        self.my_bubbles = []
        self.background_colour = (255, 255, 255)        #white color
        (self.width, self.height) = (900, 700)          #size of screen
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.initializeWindow()


    def initializeWindow(self):
        pygame.display.set_caption('Bubble trouble')
        self.move_ball()

    def move_ball(self):
        for n in range(self.number_of_bubble):
            bubble = Bubble((400, 50), self.screen)
            bubble.speed = 0.1
            bubble.angle = (math.pi / 2)

            self.my_bubbles.append(bubble)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.background_colour)

            for bubble in self.my_bubbles:
                bubble.move()
                bubble.display()

            pygame.display.flip()


if __name__ == '__main__':
    Program()