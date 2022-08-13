from ast import Constant
import pygame
import constants
from classes.chess_pieces.Pawn import Pawn

class Board():
    def __init__(self, game):
        self.game = game
        self.chess_pieces = []

        self.selected_chess_piece = None
        self.teams_turn = constants.WHITE

        self.init_chess_pieces()

    def init_chess_pieces(self):
        for col in range(constants.TILE_SIZE):
            self.chess_pieces.append(Pawn(self.game, col, 0, constants.BLACK))
            self.chess_pieces.append(Pawn(self.game, col, 1, constants.BLACK))

            self.chess_pieces.append(Pawn(self.game, col, 6, constants.WHITE))
            self.chess_pieces.append(Pawn(self.game, col, 7, constants.WHITE))

    def draw(self):
        self.draw_board()
        if self.selected_chess_piece:
            self.selected_chess_piece.draw_movements()
        self.draw_chess_pieces()

    def draw_chess_pieces(self):
        for chess_piece in self.chess_pieces:
            chess_piece.draw()

    def draw_board(self):
        for row in range(constants.BOARD_SIZE):
            for col in range(constants.BOARD_SIZE):
                tile_color = constants.BLACK if (row + col) % 2 else constants.WHITE
                rect = (
                    row * constants.TILE_SIZE, 
                    col * constants.TILE_SIZE,
                    constants.TILE_SIZE,
                    constants.TILE_SIZE
                )

                pygame.draw.rect(
                    self.game.screen, 
                    tile_color,
                    rect
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

    def switch_teams_turn(self):
        if self.teams_turn == constants.BLACK:
            self.teams_turn = constants.WHITE
        else:
            self.teams_turn = constants.BLACK

    def handle_movement(self, x, y):
        if self.selected_chess_piece.x == x and self.selected_chess_piece.y == y:
            self.selected_chess_piece = None
        else:
            movements = self.selected_chess_piece.get_movements()

            if len(movements) == 0:
                return

            for movement in movements:
                if x != movement.x and y != movement.y:
                    return 
            
            existing_chest_piece = self.get_chess_piece(x, y)
            if existing_chest_piece:
                existing_chest_piece.become_captured()
            
            self.selected_chess_piece.move(x, y)

            self.selected_chess_piece = None
            self.switch_teams_turn()