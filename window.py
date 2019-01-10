import points
from player import *
from player_movement import PlayerMovement
from projectile import *
from level import *
from random import Random
from bonus import *
from multiprocessing import Process, Queue
import time


class Window:
    def __init__(self):
        pygame.init()
        self.windowWidth = 900
        self.windowHeight = 700
        self.running = True
        self.clock = pygame.time.Clock()
        self.players = []
        self.slowed = False

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption('Bubble trouble')

        self.player1 = Player(16, 663, 'Images/player.png', pygame.K_a, pygame.K_d)
        self.player2 = Player(860, 663, 'Images/player2.png', pygame.K_LEFT, pygame.K_RIGHT)

        self.bubbleSize = 74  # size of bubble
        self.positionOfBall = (400, 50)
        self.bubbleAmplitude = 8
        self.bubble_service = BubbleService(self.positionOfBall, self.window, self.running, (self.windowWidth, self.windowHeight))

        self.levelImage = pygame.image.load('Images/level1.png')
        self.level = Level()

        self.lives1Image = pygame.image.load('Images/lives1.png')
        self.lives2Image = pygame.image.load('Images/lives2.png')

        self.bonus = Bonus(0, 0, 'Images/bonus.png')
        self.negativeBonus = Bonus(0, 0, 'Images/negativeBonus.png')

        self.queue = Queue()
        self.returnQueue = Queue()

    def redraw_window(self):
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

        self.bubble_service.move_ball(self.player1.projectile, self.player2.projectile, self.queue)

        if len(self.bubble_service.my_bubbles) == 0:
            image = self.level.start_next_level(self.player1, self.player2, self.bubble_service)
            self.levelImage = pygame.image.load(image)

        if self.bonus.enabled:
            self.window.blit(self.bonus.image, (self.bonus.xPosition, self.bonus.yPosition))

        if self.negativeBonus.enabled:
            self.window.blit(self.negativeBonus.image, (self.negativeBonus.xPosition, self.negativeBonus.yPosition))

        self.update_hitboxes()

        pygame.display.update()  # show all on screen

    def update_hitboxes(self):
        self.player1.hitbox = (self.player1.xPosition, self.player1.yPosition, 23, 37)  # updating the hitboxes as players move
        self.player2.hitbox = (self.player2.xPosition, self.player2.yPosition, 23, 37)
        self.bubble_service.my_bubbles[0].hitbox = (self.bubble_service.my_bubbles[0].x, self.bubble_service.my_bubbles[0].y, 80, 80)  # we can use for loop to update all bubbles
        self.bonus.hitbox = (self.bonus.xPosition, self.bonus.yPosition, 23, 37)
        self.negativeBonus.hitbox = (self.negativeBonus.xPosition, self.negativeBonus.yPosition, 23, 37)

    def check_player_and_ball_collision(self):
        for player in self.players:
            for bubble in self.bubble_service.my_bubbles:
                if bubble.y + bubble.bubble_size > player.hitbox[1]:  # 74 is ball diameter, hitbox[1] is Y coordinate for player
                    if bubble.x + bubble.bubble_size > player.hitbox[0] and bubble.x < player.hitbox[0] + player.hitbox[2]:  # hitbox[0] - players X coordinate, [2] - players width
                        player.lives -= 1
                        if player.lives == 0:
                            player.xPosition = -100
                            player.yPosition = -100

                        if self.players[0].lives == 0 and self.players[1].lives == 0:
                            self.queue.put('all_players_died')
                            player1_score, player2_score = self.returnQueue.get()
                            black = (0, 0, 0)
                            myFont = pygame.font.SysFont("Times New Roman", 30)
                            player1_score_text = myFont.render(('Player 1 scored: %d' % player1_score), 1, black)
                            player2_score_text = myFont.render(('Player 2 scored: %d' % player2_score), 1, black)

                            self.window.blit(player1_score_text, (50, 463))
                            self.window.blit(player2_score_text, (450, 463))
                            pygame.display.update()
                            time.sleep(3)

                        image = self.level.restart_level(self.player1, self.player2, self.bubble_service)
                        self.levelImage = pygame.image.load(image)
                        break

    def check_player_and_bonus_collision(self):
        for player in self.players:
            if self.bonus.xPosition + self.bonus.bonusWidth > player.hitbox[0] and self.bonus.xPosition < player.hitbox[0] + player.hitbox[2]:
                if player.lives < 5 and self.bonus.enabled:
                    player.lives += 1
                self.bonus.enabled = False

    def check_player_and_negative_bonus_collision(self):
        for player in self.players:
            if self.negativeBonus.xPosition + self.negativeBonus.bonusWidth > player.hitbox[0] and self.negativeBonus.xPosition < player.hitbox[0] + player.hitbox[2]:
                if self.negativeBonus.enabled:
                    player.velocity = 5
                    self.slowed = True
                self.negativeBonus.enabled = False

    def run_game(self):
        p1 = Process(target=points.increase_points, args=[self.queue, self.returnQueue])
        p1.start()
        img = pygame.image.load('Images/transparentBall.png')
        self.bubble_service.init_ball(1, 4, 74, 10, img)  # at start we have 1 ball and collision is 0, bubble size and amplitude
        self.players.append(self.player1)
        self.players.append(self.player2)
        bonusTimer = 0
        negativeBonusTimer = 0
        slowReset = 0

        while self.running:
            self.clock.tick(40)
            self.check_player_and_ball_collision()
            self.check_player_and_bonus_collision()
            self.check_player_and_negative_bonus_collision()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.queue.put('quit')
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.player1.fire()
                elif keys[pygame.K_KP_ENTER]:
                    self.player2.fire()
                elif keys[pygame.K_ESCAPE]:
                    self.running = False
                    self.queue.put('quit')
                    break

            if self.player1.lives > 0:
                PlayerMovement.update_player_position(self.player1)
                Projectile.update_projectile(self.player1.projectile)

            if self.player2.lives > 0:
                PlayerMovement.update_player_position(self.player2)
                Projectile.update_projectile(self.player2.projectile)

            rand = Random()
            if rand.randint(0, 1000) <= 1 and self.bonus.enabled is False:
                self.bonus.yPosition = 663
                self.bonus.xPosition = rand.randint(16, 860)
                self.bonus.enabled = True
            elif self.bonus.enabled:
                if bonusTimer >= 80:
                    self.bonus.enabled = False
                    bonusTimer = 0
                else:
                    bonusTimer += 1

            if rand.randint(0, 1000) <= 1 and self.negativeBonus.enabled is False and self.slowed is False:
                self.negativeBonus.yPosition = 663
                self.negativeBonus.xPosition = rand.randint(16, 860)
                self.negativeBonus.enabled = True
            elif self.negativeBonus.enabled:
                if negativeBonusTimer >= 80:
                    self.negativeBonus.enabled = False
                    negativeBonusTimer = 0
                else:
                    negativeBonusTimer += 1

            if self.slowed:
                if slowReset >= 200:
                    for player in self.players:
                        if player.velocity == 5:
                            player.velocity = 10
                    self.slowed = False
                    slowReset = 0
                else:
                    slowReset += 1

            self.redraw_window()

    pygame.quit()
