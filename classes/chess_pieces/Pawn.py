from classes.chess_pieces.ChessPiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, game, x, y, team):
        self.chess_piece_type = "pawn"
        super().__init__(game, x, y, team)
        

    def get_movements(self):
        movements = []

        move_range = 1 if self.moved else 2

        for i in range(move_range):
            y = self.y - self.direction * (1 + i)
            if self.can_move(self.x, y):
                movements.append((self.x, y))
            else:
                break
        
        y = self.y - self.direction
        x = self.x + 1
        if self.can_capture(x, y):
            movements.append((x, y))

        x = self.x - 1
        if self.can_capture(x, y):
            movements.append((x, y))

        return movements
        