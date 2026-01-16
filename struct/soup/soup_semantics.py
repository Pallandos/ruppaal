from struct.lang_semantics import LanguageSemantics
from .soup import Soup, Piece

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
