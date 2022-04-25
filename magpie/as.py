def __init__(self):
    self.color = WHITE
    self.field = []
    for row in range(8):
        self.field.append([None] * 8)
    self.field[0] = [
        Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
        King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
    ]
    self.field[1] = [
        Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
        Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
    ]
    self.field[6] = [
        Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
        Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
    ]
    self.field[7] = [
        Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
        King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
    ]
