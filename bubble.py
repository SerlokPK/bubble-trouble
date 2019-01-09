import pygame
from bubble_movement import BubbleMovement


class Bubble:
    def __init__(self, positionOfBall, screen, running, window_size):
        self.positionOfBall = positionOfBall
        self.screen = screen
        (self.width, self.height) = window_size
        self.running = running

        self.background_colour = (255, 255, 255)  # white color
        self.my_bubbles = []

    def init_ball(self, numOfBubbles, collisionTime, bubble_size, amplitude, img):
        number_of_bubbles = numOfBubbles
        img = pygame.transform.scale(img, (bubble_size, bubble_size))

        for n in range(number_of_bubbles):
            if n % 2 == 0:
                pathPointer = 1  # when bubble is split, angles are different
            else:
                pathPointer = -1

            bubble = BubbleMovement(self.positionOfBall, self.screen, (self.width, self.height), bubble_size, amplitude,
                                    collisionTime, img)
            bubble.speed = 15.8
            bubble.angle = 2 * pathPointer

            self.my_bubbles.append(bubble)

    def move_ball(self, projectile1, projectile2):
        for (index, bubble) in enumerate(self.my_bubbles):
            bubble.move()
            bubble.bounce()
            isCollision = bubble.collision(projectile1, projectile2)
            img = bubble.img

            if isCollision[0] == True and bubble.collisionTime > 0:
                collisionTime = bubble.collisionTime
                bubble_size = bubble.bubble_size
                amplitude = bubble.amplitude
                self.positionOfBall = (bubble.x, bubble.y)

                self.check_player_collision(isCollision[1], index, projectile1, projectile2)
                self.init_ball(2, collisionTime, bubble_size, amplitude, img)
                self.move_ball(projectile1, projectile2)
            elif isCollision[0] == True and bubble.collisionTime == 0:
                self.check_player_collision(isCollision[1], index, projectile1, projectile2)

            bubble.display(img)

        pygame.display.flip()

    def remove_ball(self, index):
        del self.my_bubbles[index]

    def check_player_collision(self, collisionOnPlayer, index, projectile1, projectile2):
        self.remove_ball(index)

        if collisionOnPlayer == 1:
            projectile1.alive = False
            projectile1.xPosition = -20
            projectile1.yPosition = 0
            projectile1.hitbox = (projectile1.xPosition, projectile1.yPosition, 8, 480)
        else:
            projectile2.alive = False
            projectile2.xPosition = -20
            projectile2.yPosition = 0
            projectile2.hitbox = (projectile2.xPosition, projectile2.yPosition, 8, 480)
