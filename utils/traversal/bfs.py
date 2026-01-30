from struct.graph import RootedGraph

def bfs(graph: RootedGraph, on_entry = None, opaque = None) -> tuple:
    """Parcours en profondeur 

    Args:
        graph (RootedGraph): entry graph (is a RootedGraph, so the starting nodes are known)
        on_entry (lambda func): lambda function applied to each node (must return tuple bool,opaque)
    """
    queue = []  # List[Tuple[state, parent]]
    
    # Check if states are hashable using the first root
    roots = graph.roots()
    if not roots:
        return ([], opaque) # Or ({}, opaque)

    use_dict = True
    try:
        hash(roots[0])
        marked = {} # Dict[state, parent]
    except TypeError:
        use_dict = False
        marked = [] # List[Tuple[state, parent]]

    # add all initial states
    for node in roots:
        queue.append((node, None))
    
    while len(queue) > 0:
        v, parent = queue.pop(0)
        
        is_marked = False
        if use_dict:
            if v in marked:
                is_marked = True
        else:
            # Linear search for unhashable states
            # marked is a list here
            for state, _ in marked:
                if state == v:
                    is_marked = True
                    break
        
        if not is_marked:
            # marquer v
            if use_dict:
                marked[v] = parent # type: ignore
            else:
                marked.append((v, parent)) # type: ignore
            
            # process v, eventually
            if on_entry is not None:
                retour, out = on_entry(v,opaque)
                if retour:
                    return(marked, out)
            
            # prendre ses voisins 
            for voisin in graph.neighbors(v):
                queue.append((voisin, v))
                
    return (marked, opaque)

def get_trace(marked, target):
    """Reconstruct path from marked structure"""
    path = []
    curr = target
    
    if isinstance(marked, dict):
        while curr is not None:
            path.insert(0, curr)
            if curr in marked:
                curr = marked[curr]
            else:
                break
    elif isinstance(marked, list):
        # Handle list of (state, parent) tuples
        while curr is not None:
            path.insert(0, curr)
            found_parent = None
            found = False
            for state, parent in marked:
                if state == curr:
                    found_parent = parent
                    found = True
                    break
            
            if found:
                curr = found_parent
            else:
                break
                
    return path