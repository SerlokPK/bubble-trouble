import pygame
import math

from bubble_movement import BubbleMovement

class Bubble:
	def __init__(self,positionOfBall,screen,running,window_size,bubble_size):
		self.positionOfBall = positionOfBall
		self.screen = screen
		(self.width,self.height) = window_size
		self.bubble_size = bubble_size
		self.running = running

		self.background_colour = (255, 255, 255)  # white color
		self.img = pygame.image.load('Images/transparentBall.png')
		self.img = pygame.transform.scale(self.img, (self.bubble_size, self.bubble_size))
		self.my_bubbles = []

	def init_ball(self, numOfBubbles):
		number_of_bubbles = numOfBubbles

		for n in range(number_of_bubbles):
			bubble = BubbleMovement(self.positionOfBall, self.screen,(self.width,self.height), self.bubble_size)
			bubble.speed = 15.8
			bubble.angle = 2

			self.my_bubbles.append(bubble)

	def move_ball(self):
		for bubble in self.my_bubbles:
			bubble.move()
			bubble.bounce()
			bubble.display(self.img)

		pygame.display.flip()