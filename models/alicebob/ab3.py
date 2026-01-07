from struct.graph import RootedGraph

class Ab3(RootedGraph):
    """Alice and Bob Model 3
    """
    
    def __init__(self):
        pass
    
    def roots(self) -> list:
        return [("I", "I", "down", "down")]
    
    def neighbors(self, vertex) -> list:
        alice_state, bob_state, alice_flag, bob_flag = vertex
        neighbors = []
        
        if alice_state == "I":
            neighbors.append(("W", bob_state, "up", bob_flag))
        
        if bob_state == "I":
            neighbors.append((alice_state, "W", alice_flag, "up"))
        
        if alice_state == "W" and bob_flag == "down":
            neighbors.append(("CS", bob_state, "up", "down"))
        
        if bob_state == "W" and alice_flag == "down":
            neighbors.append((alice_state, "CS", "down", "up"))
        
        if bob_state == "W" and alice_flag == "up":
            neighbors.append((alice_state, "I", "up", "down"))
        
        if alice_state == "CS":
            neighbors.append(("I", bob_state, "down", bob_flag))
        
        if bob_state == "CS":
            neighbors.append((alice_state, "I", alice_flag, "down"))
                    
        return neighbors