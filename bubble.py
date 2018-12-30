import pygame,math

from bubble_movement import BubbleMovement

class Bubble:
	def __init__(self,positionOfBall,screen,running,window_size,bubble_size):
		self.positionOfBall = positionOfBall
		self.screen = screen
		(self.width,self.height) = window_size
		self.bubble_size = bubble_size
		self.running = running

		self.background_colour = (255, 255, 255)        #white color
		self.img = pygame.image.load('rball6.bmp')
		self.img = pygame.transform.scale(self.img, (self.bubble_size, self.bubble_size))

	def move_ball(self,numOfBubbles):
		number_of_bubbles = numOfBubbles
		my_bubbles = []

		for n in range(number_of_bubbles):
			bubble = BubbleMovement(self.positionOfBall, self.screen,(self.width,self.height), self.bubble_size)
			bubble.speed = 0.8
			bubble.angle = 2

			my_bubbles.append(bubble)

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill(self.background_colour)

			for bubble in my_bubbles:
				bubble.move()
				bubble.bounce()
				bubble.display(self.img)

			pygame.display.flip()