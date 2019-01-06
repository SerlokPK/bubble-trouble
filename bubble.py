import pygame
import math

from bubble_movement import BubbleMovement

class Bubble:
	def __init__(self,positionOfBall,screen,running,window_size,bubble_size,amplitude):
		self.positionOfBall = positionOfBall
		self.screen = screen
		(self.width,self.height) = window_size
		self.bubble_size = bubble_size
		self.running = running
		self.amplitude = amplitude

		self.background_colour = (255, 255, 255)  # white color
		self.img = pygame.image.load('Images/transparentBall.png')
		self.img = pygame.transform.scale(self.img, (self.bubble_size, self.bubble_size))
		self.my_bubbles = []

	def init_ball(self, numOfBubbles):
		number_of_bubbles = numOfBubbles

		for n in range(number_of_bubbles):
			bubble = BubbleMovement(self.positionOfBall, self.screen,(self.width,self.height), self.bubble_size,self.amplitude)
			bubble.speed = 15.8
			bubble.angle = 2

			self.my_bubbles.append(bubble)

	def move_ball(self,projectile1,projectile2):
		for (index, bubble) in enumerate(self.my_bubbles):
			bubble.move()
			bubble.bounce()
			isCollision = bubble.collision(projectile1,projectile2)

			if isCollision[0] == True and self.bubble_size >= 20:
				self.remove_ball(index)
				self.positionOfBall = (bubble.x,bubble.y)
				self.bubble_size -= 20
				self.amplitude -= 2

				if isCollision[1] == 1:
					projectile1.alive = False
					projectile1.xPosition = -20
					projectile1.hitbox = (projectile1.xPosition, projectile1.yPosition, 8, 480)
				else:
					projectile2.alive = False
					projectile2.xPosition = -20
					projectile2.hitbox = (projectile1.xPosition, projectile1.yPosition, 8, 480)

				isCollision = (False,1)
				self.init_ball(2)
			bubble.display(self.img)

		pygame.display.flip()

	def remove_ball(self,index):
		del self.my_bubbles[index]