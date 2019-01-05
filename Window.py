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
		self.bubble = Bubble(self.positionOfBall,self.window,self.running,(self.windowWidth, self.windowHeight),self.bubbleSize)      #check later, it will always be true (?)
		self.levelImage = pygame.image.load('Images/level1.png')
		self.level = Level()

	def redrawWindow(self):
		self.window.fill((255, 255, 255))
		self.window.blit(self.levelImage, (0, 0))
		self.window.blit(self.player1.projectile.image, (self.player1.projectile.xPosition, self.player1.projectile.yPosition))
		self.window.blit(self.player2.projectile.image, (self.player2.projectile.xPosition, self.player2.projectile.yPosition))
		self.window.blit(self.player1.image, (self.player1.xPosition, self.player1.yPosition))  # iscrtavanje naseg player1
		self.window.blit(self.player2.image, (self.player2.xPosition, self.player2.yPosition))  # iscrtavanje naseg player2
		self.bubble.move_ball()
		self.updatehitboxes()
		pygame.draw.rect(self.window, (255, 0, 0), self.bubble.my_bubbles[0].hitbox, 2)
		pygame.draw.rect(self.window, (255,0,0), self.player1.hitbox, 2)
		pygame.draw.rect(self.window, (255,0,0), self.player2.hitbox, 2)
		pygame.display.update()  # da bi se oni pojavili na ekranu

	def updatehitboxes(self):
		self.player1.hitbox = (self.player1.xPosition, self.player1.yPosition, 23, 37)  #updating the hitboxes as players move
		self.player2.hitbox = (self.player2.xPosition, self.player2.yPosition, 23, 37)
		self.bubble.my_bubbles[0].hitbox = (self.bubble.my_bubbles[0].x, self.bubble.my_bubbles[0].y, 80, 80)  #we can use for loop to update all bubbles

	def playerandballcollision(self):
		for player in self.players:
			for bubble in self.bubble.my_bubbles:
				if bubble.y - 40 < player.hitbox[1] + player.hitbox[3] and bubble.y + 40 > player.hitbox[1] - player.hitbox[3]:
					if bubble.x + 40 > player.hitbox[0] - player.hitbox[2] and bubble.x - 40 < player.hitbox[0] + player.hitbox[2]:
						self.level.restart_level(self.player1, self.player2, self.bubble)

	def runGame(self):
		self.bubble.init_ball(1)
		self.players.append(self.player1)
		self.players.append(self.player2)
		while self.running:
			self.clock.tick(40)
			self.playerandballcollision()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				keys = pygame.key.get_pressed()
				if keys[pygame.K_SPACE]:
					self.player1.fire()
				elif keys[pygame.K_KP_ENTER]:
					self.player2.fire()
				elif keys[pygame.K_r]:
					self.level.restart_level(self.player1, self.player2, self.bubble)
				elif keys[pygame.K_n]:
					image = self.level.start_next_level(self.player1, self.player2, self.bubble)
					self.levelImage = pygame.image.load(image)

			PlayerMovement.UpdatePlayer(self, self.player1)
			PlayerMovement.UpdatePlayer(self, self.player2)
			Projectile.UpdateProjectile(self.player1.projectile)
			Projectile.UpdateProjectile(self.player2.projectile)
			self.redrawWindow()

	pygame.quit()