from classes.chess_pieces.ChessPiece import ChessPiece
from classes.Movement import Movement

class Queen(ChessPiece):
    def __init__(self, game, x, y, team):
        self.chess_piece_type = "queen"
        super().__init__(game, x, y, team)
        

    def get_movements(self):
        movements = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        for direction in directions:
            x_direction, y_direction = direction
            move_range = 0

            while True:
                move_range += 1
                x = self.x + move_range * x_direction
                y = self.y + move_range * y_direction * self.direction

                if self.can_move(x, y):
                    movements.append(Movement(x, y))
                else:
                    if self.can_capture(x, y):
                        movements.append(Movement(x, y))
                    break

        return movements