from struct.soup import Soup, Piece
from struct.Isoup import Isoup, Ipiece

class AliceBobSoup(Soup):
    def __init__(self):
        # State: [alice_state, bob_state]
        # 0: Idle, 1: CS
        init_state = [0, 0]
        
        pieces = []
        
        # Alice Transitions
        # Idle -> CS
        pieces.append(Piece(
            lambda s: [1, s[1]],
            lambda s: s[0] == 0,
            "Alice_Enter"
        ))
        # CS -> Idle
        pieces.append(Piece(
            lambda s: [0, s[1]],
            lambda s: s[0] == 1,
            "Alice_Leave"
        ))

        # Bob Transitions
        # Idle -> CS
        pieces.append(Piece(
            lambda s: [s[0], 1],
            lambda s: s[1] == 0,
            "Bob_Enter"
        ))
        # CS -> Idle
        pieces.append(Piece(
            lambda s: [s[0], 0],
            lambda s: s[1] == 1,
            "Bob_Leave"
        ))
        
        super().__init__(pieces, init_state)


