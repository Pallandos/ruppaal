from struct.graph import RootedGraph

class Ab1(RootedGraph):
    """Alice and Bob Model 1
    """
    
    def __init__(self):
        print("AB1 model initialized")
    
    def roots(self) -> list:
        return [("I", "I")]
    
    def neighbors(self, vertex) -> list:
        if vertex == ("I", "I"):
            return [("CS", "I"), ("I", "CS")]
        elif vertex == ("CS", "I"):
            return [("I", "I"), ("CS", "CS")]
        elif vertex == ("I", "CS"):
            return [("I", "I"), ("CS", "CS")]
        elif vertex == ("CS", "CS"):
            return [("I", "CS"), ("CS", "I")]
        else:
            return []