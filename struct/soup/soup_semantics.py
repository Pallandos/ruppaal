from struct.lang_semantics import LanguageSemantics
from .soup import Soup, Piece

class Soupsemantics(LanguageSemantics):
    def __init__(self, soup: Soup):
        self.soup = soup

    def initials(self):
        # Le BFS attend une liste d'états, on enveloppe donc la valeur initiale
        return [self.soup.init_value]

    def actions(self, state):
        set_of_actions = []
        for piece in self.soup.pieces:
            # On passe l'état à la garde pour voir si l'action est activable
            if piece.garde(state):
                set_of_actions.append(piece)
        return set_of_actions

    def execute(self, state, action: Piece) -> list:
        # On exécute l'effet qui doit renvoyer le nouvel état
        out = action.effet(state)
        return [out]