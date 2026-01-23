class Soup :
    """
    Soup is a group of Pieces objects
    """
    def __init__(self, pieces, init_value):
        self.pieces = pieces
        self.init_value = init_value
        
    def extend(self, b):
        if isinstance(b, Piece):
            self.pieces.append(b)
        else:
            self.pieces.extend(b)
    
    def add(self, name, guard, generator):
        self.extend(Piece(name, guard, generator))

class Piece:
    """
    Piece is a part of a Soup. 

    self.garde and self.garde are lambda functions
    """
    def __init__(self,effet,garde,nom):
        self.effet = effet
        self.garde = garde
        self.nom = nom
    
    def __eq__(self, other):
        if not isinstance(other, Piece):
            return False
        return self.nom == other.nom and self.garde == other.garde and self.effet == other.effet