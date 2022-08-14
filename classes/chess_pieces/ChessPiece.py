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
        self.game.board.set_chess_piece(None, self.x, self.y)
        self.game.board.set_chess_piece(self, x, y)
        self.x = x
        self.y = y
        self.moved = True

    def can_move(self, x, y):
        board = self.game.board
        return self.is_valid_tile(x, y) and not board.get_chess_piece(x, y) 

    def can_capture(self, x, y):
        board = self.game.board
        if not self.is_valid_tile(x, y):
            return False
        chess_piece = board.get_chess_piece(x, y) 
        if chess_piece:
            return chess_piece.team != self.team

    def is_valid_tile(self, x, y):
        return x >= 0 and y >= 0 and x < constants.BOARD_SIZE and y < constants.BOARD_SIZE

    def get_direction(self):
        return 1 if self.team == constants.WHITE else -1

    def get_movements(self):
        pass 

    def draw_selected(self):
        self.draw_highlight(self.x, self.y, constants.GREEN)

    def draw_movements(self):
        for (x, y) in self.get_movements():
            if self.can_capture(x, y):
                self.draw_highlight(x, y, constants.RED)
            else:
                self.draw_highlight(x, y, constants.BLUE)

    def draw_highlight(self, x, y, highlight_color):
        rect = (
            x * constants.TILE_SIZE, 
            y * constants.TILE_SIZE,
            constants.TILE_SIZE,
            constants.TILE_SIZE
        )

        pygame.draw.rect(
            self.game.screen, 
            highlight_color,
            rect
        )

    def draw(self):
        position = (
            self.x * constants.TILE_SIZE, 
            self.y * constants.TILE_SIZE,
        )

        self.game.screen.blit(self.image, position)