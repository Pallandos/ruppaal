from struct.lang_semantics import LanguageSemantics
from .isoup import Isoup, Piece

class Isoupsemantics(LanguageSemantics) :
    def __init__(self, isoup: Isoup):
        self.isoup = isoup

    def initials(self):
        # Le BFS attend une liste d'états, on enveloppe donc la valeur initiale
        return [self.isoup.init_value]
    
    def actions(self, state):
        set_of_actions = []
        for piece in self.isoup.pieces:
            # On vérifie si l'action est légale
            if piece.garde(state) :
                 set_of_actions.append(piece)
        return set_of_actions
    
    def execute(self, state, action: Piece) ->list:
        out = action.effet(state)
        return [out]