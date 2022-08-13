import pygame
import constants
from classes.chess_pieces.Pawn import Pawn
from classes.chess_pieces.Rook import Rook
from classes.chess_pieces.Knight import Knight
from classes.chess_pieces.Bishop import Bishop
from classes.chess_pieces.King import King
from classes.chess_pieces.Queen import Queen



class Board():
    def __init__(self, game):
        self.game = game
        self.chess_pieces = []

        self.selected_chess_piece = None
        self.teams_turn = constants.WHITE
        self.set_window_caption()

        self.init_chess_pieces()

    def set_window_caption(self):
        team_name = "White" if self.teams_turn == constants.WHITE else "Black"
        pygame.display.set_caption(f'Chess - {team_name}\'s turn')

    def init_chess_pieces(self):
        for col in range(constants.TILE_SIZE):
            self.chess_pieces.append(Pawn(self.game, col, 1, constants.BLACK))

            self.chess_pieces.append(Pawn(self.game, col, 6, constants.WHITE))

        self.chess_pieces.append(Rook(self.game, 0, 0, constants.BLACK))
        self.chess_pieces.append(Knight(self.game, 1, 0, constants.BLACK))
        self.chess_pieces.append(Bishop(self.game, 2, 0, constants.BLACK))
        self.chess_pieces.append(Queen(self.game, 3, 0, constants.BLACK))
        self.chess_pieces.append(King(self.game, 4, 0, constants.BLACK))
        self.chess_pieces.append(Bishop(self.game, 5, 0, constants.BLACK))
        self.chess_pieces.append(Knight(self.game, 6, 0, constants.BLACK))
        self.chess_pieces.append(Rook(self.game, 7, 0, constants.BLACK))

        self.chess_pieces.append(Rook(self.game, 0, 7, constants.WHITE))
        self.chess_pieces.append(Knight(self.game, 1, 7, constants.WHITE))
        self.chess_pieces.append(Bishop(self.game, 2, 7, constants.WHITE))
        self.chess_pieces.append(King(self.game, 3, 7, constants.WHITE))
        self.chess_pieces.append(Queen(self.game, 4, 7, constants.WHITE))
        self.chess_pieces.append(Bishop(self.game, 5, 7, constants.WHITE))
        self.chess_pieces.append(Knight(self.game, 6, 7, constants.WHITE))
        self.chess_pieces.append(Rook(self.game, 7, 7, constants.WHITE))

    def draw(self):
        self.draw_board()
        if self.selected_chess_piece:
            self.selected_chess_piece.draw_movements()
            self.selected_chess_piece.draw_highlight()
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
            chess_piece = self.get_chess_piece(x, y)
            if chess_piece and chess_piece.team == self.teams_turn:
                self.handle_selection(x, y)
            else:
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
        self.teams_turn = constants.BLACK if self.teams_turn == constants.WHITE else constants.WHITE
        self.set_window_caption()

    def movement_exists(self, x, y, movements):
        for movement in movements:
            if x == movement.x and y == movement.y:
                return True

    def handle_movement(self, x, y):
        if self.selected_chess_piece.x == x and self.selected_chess_piece.y == y:
            self.selected_chess_piece = None
        else:
            movements = self.selected_chess_piece.get_movements()

            if len(movements) == 0:
                return

            if not self.movement_exists(x, y, movements):
                return
            
            existing_chest_piece = self.get_chess_piece(x, y)
            if existing_chest_piece:
                existing_chest_piece.become_captured()
            
            self.selected_chess_piece.move(x, y)
            self.selected_chess_piece = None
            self.switch_teams_turn()