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

    def is_king_in_check(self):
        board = self.game.board
        king_piece = board.get_king_piece(self.team)
        opposing_movements = board.get_all_opposing_movements()
        return (king_piece.x, king_piece.y) in opposing_movements