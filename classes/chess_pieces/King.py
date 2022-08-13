from classes.chess_pieces.ChessPiece import ChessPiece

class King(ChessPiece):
    def __init__(self, game, x, y, team):
        self.chess_piece_type = "king"
        super().__init__(game, x, y, team)
        

    def get_movements(self):
        movements = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        for direction in directions:
            x_direction, y_direction = direction

            x = self.x + 1 * x_direction
            y = self.y + 1 * y_direction * self.direction

            if self.can_move(x, y):
                movements.append((x, y))
            else:
                if self.can_capture(x, y):
                    movements.append((x, y))
                

        return movements