from ast import Dict
import unittest
from struct.graph import DictionaryGraph
from utils.traversal import bfs

class TestBFS(unittest.TestCase):
    def test_edge_case_empty(self):
        """Edge case 1 from https://teodorov.github.io/z2mc/book/01_traversals.html
        """
        graph = DictionaryGraph()
        try:
            out, opaque = bfs(graph)
            self.assertEqual(out, [])
        except Exception as e:
            self.fail(f"bfs raised an exception on edge case: {e}")
    
    def test_edge_case_empty_null_roots(self):
        """Edge case 2 fro https://teodorov.github.io/z2mc/book/01_traversals.html
        """
        graph = DictionaryGraph({}, None)
        try:
            out, opaque = bfs(graph)
            self.assertEqual(out, [])
        except Exception as e:
            self.fail(f"bfs raised an exception on edge case with null: {e}")

    def test_edge_case_empty_null_graph(self):
        """Edge case 3 from https://teodorov.github.io/z2mc/book/01_traversals.html
        """
        graph = DictionaryGraph(None, [])
        try:
            out, opaque = bfs(graph)
            self.assertEqual(out, [])
        except Exception as e:
            self.fail(f"bfs raised an exception on edge case with null graph: {e}")
    
    def test_edge_case_null_dict(self):
        """Edge case 4 from https://teodorov.github.io/z2mc/book/01_traversals.html
        """
        graph = DictionaryGraph({1: None}, [])
        try:
            out, opaque = bfs(graph)
            self.assertEqual(out, [1])
        except Exception as e:
            self.fail(f"bfs raised an exception on edge case with null dict: {e}")
            
if __name__ == '__main__':
    unittest.main()