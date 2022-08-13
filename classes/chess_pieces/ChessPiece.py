import constants
import pygame

class ChessPiece():
    def __init__(self, game, x, y, team):
        pattern = [
            [0, 1, 0],
            [2, 1, 2],
            [0, 3, 0]
        ]

        self.game = game 
        self.x = x
        self.y = y
        self.team = team

        self.size = constants.TILE_SIZE / 2

    def draw(self):
        rect = (
            self.x * constants.TILE_SIZE + self.size / 2, 
            self.y * constants.TILE_SIZE + self.size / 2,
            self.size,
            self.size
        ),

        pygame.draw.rect(
            self.game.screen, 
            self.team,
            rect
        )

        pygame.draw.rect(
            self.game.screen, 
            constants.GRAY,
            rect,
            4
        )