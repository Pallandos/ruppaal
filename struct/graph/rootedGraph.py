from abc import ABC, abstractmethod 

class RootedGraph(ABC):
    """Abstract class of a rooted graph
    """
    @abstractmethod
    def roots(self) -> list:
        """Return list of the roots of the graoh

        Returns:
            list: list of the roots
        """
        pass

    @abstractmethod
    def neighbors(self, vertex) -> list:
        """Return list of all neighbors from a given vertex

        Args:
            vertex (Any): The vertex to get neighbors for.

        Returns:
            list: List of all neighbors of the vertex.
        """
        pass
