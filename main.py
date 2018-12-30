import pygame,turtle

from bubble import Bubble


class Program:
    def __init__(self):
        self.running = True
        (self.width, self.height) = (900, 700)              #size of screen
        self.bubbleSize = 81                                #size of bubble
        self.positionOfBall = (400, 50)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bubble = Bubble(self.positionOfBall,self.screen,self.running,(self.width, self.height),self.bubbleSize)      #check later, it will always be true (?)
       
        self.initializeWindow()
        

    def initializeWindow(self):
        pygame.display.set_caption('Bubble trouble')
        self.bubble.move_ball(1)
        

   

if __name__ == '__main__':
    Program()