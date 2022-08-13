import pygame
import constants

class Board():
    def __init__(self, game):
        self.game = game

    def draw(self):
        for row in range(constants.BOARD_SIZE):
            for col in range(constants.BOARD_SIZE):
                tile_color = constants.BLACK if (row + col) % 2 else constants.WHITE

                pygame.draw.rect(
                    self.game.screen, 
                    tile_color,
                    (
                        row * constants.TILE_SIZE, 
                        col * constants.TILE_SIZE,
                        constants.TILE_SIZE,
                        constants.TILE_SIZE
                    )
                )

    def update(self):
        pass

    def handle_inputs(self):
        pass
