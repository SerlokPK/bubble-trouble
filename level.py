from level_constants import *


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

        if self.currentLevel == 1:
            player1.xPosition = L1_P1_xPOSITION
            player1.yPosition = L1_P1_yPOSITION
            player2.xPosition = L1_P2_xPOSITION
            player2.yPosition = L1_P2_yPOSITION
            bubble.positionOfBall = L1_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS)
            image = L1_IMAGE
        elif self.currentLevel == 2:
            player1.xPosition = L2_P1_xPOSITION
            player1.yPosition = L2_P1_yPOSITION
            player2.xPosition = L2_P2_xPOSITION
            player2.yPosition = L2_P2_yPOSITION
            bubble.positionOfBall = L2_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS)
            image = L2_IMAGE
        elif self.currentLevel == 3:
            player1.xPosition = L3_P1_xPOSITION
            player1.yPosition = L3_P1_yPOSITION
            player2.xPosition = L3_P2_xPOSITION
            player2.yPosition = L3_P2_yPOSITION
            bubble.positionOfBall = L3_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS)
            image = L3_IMAGE
        elif self.currentLevel == 4:
            player1.xPosition = L4_P1_xPOSITION
            player1.yPosition = L4_P1_yPOSITION
            player2.xPosition = L4_P2_xPOSITION
            player2.yPosition = L4_P2_yPOSITION
            bubble.positionOfBall = L4_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS)
            image = L4_IMAGE
        else:  # self.currentLevel == 5:
            player1.xPosition = L5_P1_xPOSITION
            player1.yPosition = L5_P1_yPOSITION
            player2.xPosition = L5_P2_xPOSITION
            player2.yPosition = L5_P2_yPOSITION
            bubble.positionOfBall = L5_BUBBLE_POSITION
            bubble.init_ball(L1_NUMBER_OF_BALLS)
            image = L5_IMAGE

        return image
