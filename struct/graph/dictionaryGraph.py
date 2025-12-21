from rootedGraph import RootedGraph

class DictionaryGraph(RootedGraph):
    """Implementation of a Rooted Graph using a dictionary
    """
    def __init__(self, graph = None, roots = None):
        self.graph = graph if graph is not None else {}
        self._roots = roots if roots is not None else []
        
    def roots(self):
        """Returns the roots of the graoh

        Returns:
            list: list of the roots
        """
        return self._roots
    
    def neighbors(self,vertex):
        """Returns all the neighbors of a a given vertex

        Args:
            vertex (Vertex type): target vertex

        Returns:
            list: list of the neighbors 
        """
        return self.graph.get(vertex, [])