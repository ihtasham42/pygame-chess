import pygame
import constants
from classes.chess_pieces.ChessPiece import ChessPiece

class Board():
    def __init__(self, game):
        self.game = game
        self.chess_pieces = [
            ChessPiece(game, 0, 0, constants.BLACK),
            ChessPiece(game, 1, 0, constants.WHITE)
        ]

    def draw(self):
        self.draw_board()
        self.draw_chess_pieces()

    def draw_chess_pieces(self):
        for chess_piece in self.chess_pieces:
            chess_piece.draw()

    def draw_board(self):
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
