from struct.soup import Soup, Piece
from copy import deepcopy

class HanoiSoup(Soup):
    def __init__(self, n_disks):
        # État initial : [[n, ..., 1], [], []]
        # Attention : on utilise des listes (mutables), donc deepcopy sera vital
        init_state = [list(range(n_disks, 0, -1)), [], []]
        
        # On génère les 6 mouvements possibles (source -> destination)
        pieces = []
        for src in range(3):
            for dst in range(3):
                if src != dst:
                    pieces.append(self.create_move_piece(src, dst))
        
        # On initialise la classe parente
        super().__init__(pieces, init_state)

    def create_move_piece(self, source, dest):
        """Crée une pièce pour déplacer un disque de source vers dest"""
        
        # 1. La Garde : Peut-on déplacer de source vers dest ?
        def guard(state):
            # Il faut un disque à prendre
            if not state[source]:
                return False
            # La destination doit être vide OU avoir un disque plus grand
            if state[dest] and state[dest][-1] < state[source][-1]:
                return False
            return True

        # 2. L'Effet : Appliquer le mouvement
        def effect(state):
            # On copie l'état pour ne pas modifier l'ancien (programmation fonctionnelle pour le BFS)
            new_state = deepcopy(state)
            disk = new_state[source].pop()
            new_state[dest].append(disk)
            return new_state

        # Nom de la pièce (ex: "Move 0->1")
        name = f"Move {source}->{dest}"
        
        return Piece(effect, guard, name)