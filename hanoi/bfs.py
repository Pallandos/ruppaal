from rootedGraph import RootedGraph
from rootedGraph import DictionaryGraph

def bfs(graph: RootedGraph, on_entry = None, opaque = None):
    """Parcours en profondeur 

    Args:
        graph (dict): graphe en entrée 
        initial (str): noeud initial
        on_entry (lambda func): lambda function applied to each node (must return tuple bool,opaque)
    """
    marked = []
    queue = []
    
    # add all initial states
    for node in graph.roots():
        queue.append(node)
    
    while len(queue) > 0:
        v = queue.pop(0)
        if not v in marked:
            # marquer v
            marked.append(v)
            
            # process v, eventually
            if on_entry is not None:
                retour, out = on_entry(v,opaque)
                if retour:
                    return(marked, out)
            
            # prendre ses voisins 
            for voisin in graph.neighbors(v):
                queue.append(voisin)
    
    return (marked, opaque)

if __name__ == "__main__":
    
    graph = DictionaryGraph({ 1 : [2, 3], 2 : [], 3 : [1]}, [1])
    on_entry = lambda x,opaque : (x == 3, x == 3)
    retour = bfs(graph, on_entry, False)
    print(retour)
