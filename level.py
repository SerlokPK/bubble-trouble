from level_constants import *
import pygame


class Level:
    def __init__(self):
        self.currentLevel = 1

    def restart_level(self, player1, player2, bubble):
        return self.set_positions(player1, player2, bubble)

    def start_next_level(self, player1, player2, bubble):
        self.currentLevel += 1
        return self.set_positions(player1, player2, bubble)

    def set_positions(self, player1, player2, bubble):
        bubble.my_bubbles = []
        player1.projectile.alive = False
        player1.projectile.xPosition = -20
        player2.projectile.alive = False
        player2.projectile.xPosition = -20

        if self.currentLevel > 5:
            self.currentLevel = 1

        if player1.lives == 0 and player2.lives == 0:
            self.currentLevel = 1
            player1.lives = 3
            player2.lives = 3

        if self.currentLevel == 1:
            if player1.lives > 0:
                player1.xPosition = L1_P1_xPOSITION
                player1.yPosition = L1_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L1_P2_xPOSITION
                player2.yPosition = L1_P2_yPOSITION
            bubble.positionOfBall = L1_BUBBLE_POSITION
            img = pygame.image.load('Images/transparentBall.png')
            bubble.init_ball(L1_NUMBER_OF_BALLS,0,81, 8,img)
            image = L1_IMAGE
        elif self.currentLevel == 2:
            if player1.lives > 0:
                player1.xPosition = L2_P1_xPOSITION
                player1.yPosition = L2_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L2_P2_xPOSITION
                player2.yPosition = L2_P2_yPOSITION
            bubble.positionOfBall = L2_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS,0,81, 8,L2_IMAGE)
            image = L2_IMAGE
        elif self.currentLevel == 3:
            if player1.lives > 0:
                player1.xPosition = L3_P1_xPOSITION
                player1.yPosition = L3_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L3_P2_xPOSITION
                player2.yPosition = L3_P2_yPOSITION
            bubble.positionOfBall = L3_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS,0,81, 8,L3_IMAGE)
            image = L3_IMAGE
        elif self.currentLevel == 4:
            if player1.lives > 0:
                player1.xPosition = L4_P1_xPOSITION
                player1.yPosition = L4_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L4_P2_xPOSITION
                player2.yPosition = L4_P2_yPOSITION
            bubble.positionOfBall = L4_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS,0,81, 8,L4_IMAGE)
            image = L4_IMAGE
        else:  # self.currentLevel == 5:
            if player1.lives > 0:
                player1.xPosition = L5_P1_xPOSITION
                player1.yPosition = L5_P1_yPOSITION
            if player2.lives > 0:
                player2.xPosition = L5_P2_xPOSITION
                player2.yPosition = L5_P2_yPOSITION
            bubble.positionOfBall = L5_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS,0,81, 8,L5_IMAGE)
            image = L5_IMAGE

        return image
