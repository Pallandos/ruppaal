from struct.graph import RootedGraph

class LS2RG(RootedGraph):
    """
    Adaptateur : transforme une LanguageSemantics
    en RootedGraph compatible avec bfs
    """

    def __init__(self, ls):
        self._ls = ls

    def roots(self):
        return self._ls.initials()

    def neighbors(self, vertex):
        successors = []

        for action in self._ls.actions(vertex):
            next_vertexs = self._ls.execute(vertex, action)
            successors.extend(next_vertexs)

        return successors
