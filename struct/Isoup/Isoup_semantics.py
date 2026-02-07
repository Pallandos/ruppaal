from struct.lang_semantics import LanguageSemantics
from .isoup import Isoup, Ipiece

class Isoupsemantics(LanguageSemantics) :
    def __init__(self, isoup: Isoup):
        self.isoup = isoup

    def initials(self):
        # Le BFS attend une liste d'états, on enveloppe donc la valeur initiale
        return [self.isoup.init_value]
    
    def actions(self, input):       #  l'input contient un pas d'exécution de Soup avec : état courant, état futut et transition vers cet état
        set_of_actions = []
        for ipiece in self.isoup.ipieces:
            # On vérifie si l'action est légale
            if ipiece.garde(input) :
                 set_of_actions.append(ipiece)
        return set_of_actions
    
    def execute(self, input, action: Ipiece) ->list:
        out = action.effet(input)
        return [out]