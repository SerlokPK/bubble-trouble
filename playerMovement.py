import pygame


class PlayerMovement:
    def __init__(self):
        pass

    @staticmethod
    def UpdatePlayer(player):
        keys = pygame.key.get_pressed()
        if keys[player.left_key] and player.xPosition > player.velocity:
            player.xPosition -= player.velocity
            player.walkingLeft = True
            player.walkingRight = False
        if keys[player.right_key] and player.xPosition < 900 - player.playerWidth - player.velocity:
            player.xPosition += player.velocity
            player.walkingLeft = False
            player.walkingRight = True
