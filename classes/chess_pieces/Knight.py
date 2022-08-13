from classes.chess_pieces.ChessPiece import ChessPiece

class Knight(ChessPiece):
    def __init__(self, game, x, y, team):
        self.chess_piece_type = "knight"
        super().__init__(game, x, y, team)
        

    def get_movements(self):
        movements = []

        coordinates = [
            (self.x - 1, self.y - 2), (self.x + 1, self.y - 2), 
            (self.x + 2, self.y - 1), (self.x + 2, self.y + 1),
            (self.x - 1, self.y + 2), (self.x + 1, self.y - 2), 
            (self.x - 2, self.y - 1), (self.x + 2, self.y + 1),
        ]

        for (x, y) in coordinates:
            if self.can_move(x, y) or self.can_capture(x, y):
                movements.append((x, y))

        return movements