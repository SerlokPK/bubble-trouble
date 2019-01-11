import pygame


class PlayerMovement:
    @staticmethod
    def update_player_position(player):
        keys = pygame.key.get_pressed()
        if keys[player.left_key] and player.xPosition > player.velocity:
            player.xPosition -= player.velocity
        if keys[player.right_key] and player.xPosition < 900 - player.playerWidth - player.velocity:
            player.xPosition += player.velocity
