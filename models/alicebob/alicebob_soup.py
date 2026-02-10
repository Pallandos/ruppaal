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

class AliceBobISoup(Isoup):
    def __init__(self, soup_instance):
        # The ISoup takes the state of the soup as input for its guards
        # We initialize it with the same initial value as the soup
        init_value = soup_instance.init_value
        
        ipieces = []
        
        # Characteristic: Alice Critical
        ipieces.append(Ipiece(
            lambda s: s, # Identity effect
            lambda s: s[0] == 1,
            "Alice_is_Critical"
        ))
        
        # Characteristic: Bob Critical
        ipieces.append(Ipiece(
            lambda s: s,
            lambda s: s[1] == 1,
            "Bob_is_Critical"
        ))
        
        # Characteristic: Exclusion Violation (Collision)
        ipieces.append(Ipiece(
            lambda s: s,
            lambda s: s[0] == 1 and s[1] == 1,
            "Collision_Occurred"
        ))
        
        super().__init__(ipieces, init_value)
