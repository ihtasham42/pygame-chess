from classes.chess_pieces.ChessPiece import ChessPiece
from classes.Movement import Movement

class Rook(ChessPiece):
    def __init__(self, game, x, y, team):
        self.chess_piece_type = "rook"
        super().__init__(game, x, y, team)
        

    def get_movements(self):
        movements = []

        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x_direction, y_direction = direction
            x_diff, y_diff = 0, 0

            while True:
                x_diff += 1
                y_diff += 1
                x = self.x + x_diff * x_direction
                y = self.y + y_diff * y_direction * self.direction

                if self.can_move(x, y):
                    movements.append(Movement(x, y))
                else:
                    if self.can_capture(x, y):
                        movements.append(Movement(x, y))
                    break

        return movements