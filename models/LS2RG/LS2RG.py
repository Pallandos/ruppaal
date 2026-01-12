from ...hanoi.rootedGraph import RootedGraph

class LS2RG(RootedGraph):
    """
    Adaptateur : transforme une LanguageSemantics
    en RootedGraph compatible avec bfs
    """

    def __init__(self, ls):
        self._ls = ls

    def roots(self):
        return self._ls.initials()

    def neighbors(self, state):
        successors = []

        for action in self._ls.actions(state):
            next_states = self._ls.execute(state, action)
            successors.extend(next_states)

        return successors
