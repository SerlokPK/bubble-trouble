import pygame

from Player import *
from level import Level
from playerMovement import PlayerMovement
from Projectile import *
from bubble import Bubble
from level import *

class Window:
	def __init__(self):
		pygame.init()
		self.windowWidth = 900
		self.windowHeight = 700
		self.running = True
		self.clock = pygame.time.Clock()
		self.players = []

		self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
		pygame.display.set_caption('Bubble trouble')
		self.player1 = Player(16, 663, 'Images/player.png',pygame.K_a,pygame.K_d)
		self.player2 = Player(860, 663, 'Images/player2.png',pygame.K_LEFT,pygame.K_RIGHT)
		self.projectile = Projectile(self.player1)

		self.bubbleSize = 81                                #size of bubble
		self.positionOfBall = (400, 50)
		self.bubbleAmplitude = 8
		self.bubble = Bubble(self.positionOfBall,self.window,self.running,(self.windowWidth, self.windowHeight),self.bubbleSize,self.bubbleAmplitude)     
		self.levelImage = pygame.image.load('Images/level1.png')
		self.level = Level()

		self.lives1Image = pygame.image.load('Images/lives1.png')
		self.lives2Image = pygame.image.load('Images/lives2.png')

	def redrawWindow(self):
		self.window.fill((255, 255, 255))
		self.window.blit(self.levelImage, (0, 0))
		self.window.blit(self.lives1Image, (0, 0))
		self.window.blit(pygame.image.load('Images/number' + str(self.player1.lives) + '.png'), (100, 0))
		self.window.blit(self.lives2Image, (765, 0))
		self.window.blit(pygame.image.load('Images/number' + str(self.player2.lives) + '.png'), (865, 0))
		if self.player1.lives > 0:
			self.window.blit(self.player1.projectile.image, (self.player1.projectile.xPosition, self.player1.projectile.yPosition))
			self.window.blit(self.player1.image, (self.player1.xPosition, self.player1.yPosition))  # show player1
		if self.player2.lives > 0:
			self.window.blit(self.player2.projectile.image, (self.player2.projectile.xPosition, self.player2.projectile.yPosition))
			self.window.blit(self.player2.image, (self.player2.xPosition, self.player2.yPosition))  # show player2
		self.bubble.move_ball()
		self.updateHitboxes()
		pygame.display.update()  # show all on screen

	def updateHitboxes(self):
		self.player1.hitbox = (self.player1.xPosition, self.player1.yPosition, 23, 37)  #updating the hitboxes as players move
		self.player2.hitbox = (self.player2.xPosition, self.player2.yPosition, 23, 37)
		self.bubble.my_bubbles[0].hitbox = (self.bubble.my_bubbles[0].x, self.bubble.my_bubbles[0].y, 80, 80)  #we can use for loop to update all bubbles

	def playeAndBallCollision(self):
		for player in self.players:
			for bubble in self.bubble.my_bubbles:
				if bubble.y + 74 > player.hitbox[1]:  # 74 is ball diameter, hitbox[1] is Y coordinate for player
					if bubble.x + 74 > player.hitbox[0] and bubble.x < player.hitbox[0] + player.hitbox[2]:  # hitbox[0] - players X coordinate, [2] - players width
						player.lives -= 1
						if player.lives == 0:
							player.xPosition = -100
							player.yPosition = -100
						image = self.level.restart_level(self.player1, self.player2, self.bubble)
						self.levelImage = pygame.image.load(image)
						break

	def runGame(self):
		self.bubble.init_ball(1)
		self.players.append(self.player1)
		self.players.append(self.player2)
		while self.running:
			self.clock.tick(40)
			self.playeAndBallCollision()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				keys = pygame.key.get_pressed()
				if keys[pygame.K_SPACE]:
					self.player1.fire()
				elif keys[pygame.K_KP_ENTER]:
					self.player2.fire()
				elif keys[pygame.K_r]:
					self.player1.lives = 0
					self.player2.lives = 0
					image = self.level.restart_level(self.player1, self.player2, self.bubble)
					self.levelImage = pygame.image.load(image)
				elif keys[pygame.K_n]:
					image = self.level.start_next_level(self.player1, self.player2, self.bubble)
					self.levelImage = pygame.image.load(image)

			if self.player1.lives > 0:
				PlayerMovement.UpdatePlayer(self, self.player1)
				Projectile.UpdateProjectile(self.player1.projectile)

			if self.player2.lives > 0:
				PlayerMovement.UpdatePlayer(self, self.player2)
				Projectile.UpdateProjectile(self.player2.projectile)

			self.redrawWindow()

	pygame.quit()