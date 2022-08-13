import constants
import pygame

class ChessPiece():
    def __init__(self, game, x, y, team):
        self.game = game 
        self.x = x
        self.y = y
        self.team = team
        self.moved = False

        self.direction = self.get_direction()
        self.image = self.load_image()
        self.size = constants.TILE_SIZE / 2

    def load_image(self):
        directory = "sprites/"
        team_file_name = "_white" if self.team == constants.WHITE else "_black"
        file_name = directory + self.chess_piece_type + team_file_name + ".png"
        image = pygame.image.load(file_name)
        return pygame.transform.scale(image, (constants.TILE_SIZE, constants.TILE_SIZE))

    def move(self, x, y):
        self.x = x
        self.y = y
        self.moved = True

    def can_move(self, x, y):
        board = self.game.board
        return self.is_valid_tile(x, y) and not board.get_chess_piece(x, y) 

    def can_capture(self, x, y):
        board = self.game.board
        chess_piece = board.get_chess_piece(x, y) 
        if self.is_valid_tile(x, y) and chess_piece:
            return chess_piece.team != self.team

    def is_valid_tile(self, x, y):
        return x >= 0 and y >= 0 and x < constants.BOARD_SIZE and y < constants.BOARD_SIZE

    def get_direction(self):
        return 1 if self.team == constants.WHITE else -1

    def get_movements(self):
        pass

    def become_captured(self):
        chess_pieces = self.game.board.chess_pieces
        chess_pieces.remove(self)        

    def draw_movements(self):
        for movement in self.get_movements():
            tile_color = constants.RED if self.can_capture(movement.x, movement.y) else constants.BLUE 

            rect = (
                movement.x * constants.TILE_SIZE, 
                movement.y * constants.TILE_SIZE,
                constants.TILE_SIZE,
                constants.TILE_SIZE
            )

            pygame.draw.rect(
                self.game.screen, 
                tile_color,
                rect
            )

    def draw_highlight(self):
        tile_color = constants.GREEN
        rect = (
            self.x * constants.TILE_SIZE, 
            self.y * constants.TILE_SIZE,
            constants.TILE_SIZE,
            constants.TILE_SIZE
        )

        pygame.draw.rect(
            self.game.screen, 
            tile_color,
            rect
        )

    def draw(self):
        position = (
            self.x * constants.TILE_SIZE, 
            self.y * constants.TILE_SIZE,
        )

        self.game.screen.blit(self.image, position)