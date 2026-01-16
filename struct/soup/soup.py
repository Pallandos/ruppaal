class Soup :
    """
    Soup is a group of Pieces objects
    """
    def __init__(self, pieces, init_value):
        self.pieces = pieces
        self.init_value = init_value

class Piece:
    """
    Piece is a part of a Soup. 

    self.garde and self.garde are lambda functions
    """
    def __init__(self,effet,garde,nom):
        self.effet = effet
        self.garde = garde
        self.nom = nom