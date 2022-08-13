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

        self.selected_chess_piece = None
        self.teams_turn = constants.WHITE

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

    def get_coordinates_from_position(self, click_position):
        return click_position[0] // constants.TILE_SIZE, click_position[1] // constants.TILE_SIZE

    def get_chess_piece(self, x, y):
        for chess_piece in self.chess_pieces:
            if chess_piece.x == x and chess_piece.y == y:
                return chess_piece 

    def handle_click(self, click_position):
        x, y = self.get_coordinates_from_position(click_position)

        if self.selected_chess_piece:
            self.handle_movement(x, y)
        else:
            self.handle_selection(x, y)

    def handle_selection(self, x, y):
        chess_piece = self.get_chess_piece(x, y)

        if not chess_piece:
            return 

        if chess_piece.team != self.teams_turn:
            return 

        self.selected_chess_piece = chess_piece


    def handle_movement(self, x, y):
        pass