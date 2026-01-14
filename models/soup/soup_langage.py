from struct.lang_semantics.languagesemantics import LanguageSemantics

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

class Soupsemantics(LanguageSemantics) :
    def __init__(self, soup: Soup):
        self.soup = soup

    def initials(self) :
        return(self.soup.init_value)

    #une piece pour un mouvement
    def actions(self, state):
        set_of_actions = []
        for piece in self.soup.pieces :
            if piece.garde(state) :
                set_of_actions.append(piece)
        return(set_of_actions)
        # Faut trouver toutes les branches(=pièces) qui sont exécutables pour un état donné.
        

    def execute(self, state, action : Piece) -> list :
        # ici le action c'est une branche et le state c'est le x
        out = action.effet(state)
        return [out]


