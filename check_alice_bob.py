from models.alicebob import Ab1, Ab2, Ab3
from utils.traversal import bfs

def check_exclusion(vertex, opaque):
    alice_state = vertex[0]
    bob_state = vertex[1]
    # Check if both Alice and Bob are in critical section
    if alice_state == "CS" and bob_state == "CS":
        opaque.append(vertex)
        print("Exclusion violation at vertex:", vertex)
        return (True, opaque)
    return (False, opaque)

def check_deadlock(vertex, opaque):
    neighbors = opaque.neighbors(vertex)
    # Check if there are no neighbors (deadlock)
    if len(neighbors) == 0:
        print("Deadlock detected at vertex:", vertex)
        return (True, opaque)
    return (False, opaque)


if __name__ == "__main__":
    # === Ab1 Model ===
    print("======== Testing Ab1 Model ======== ")
    ab1 = Ab1()
    marked, opaque_ab1 = bfs(ab1, check_exclusion, [])
    print("Ab1 Exclusion Violations:", opaque_ab1)
    
    marked_deadlock, deadlocks = bfs(ab1, check_deadlock, ab1)
    
    # === Ab2 Model ===
    print("======== Testing Ab2 Model ======== ")
    ab2 = Ab2()
    marked, opaque_ab2 = bfs(ab2, check_exclusion, [])
    print("Ab2 Exclusion Violations:", opaque_ab2)
    
    marked_deadlock, deadlocks = bfs(ab2, check_deadlock, ab2)
    
    # === Ab3 Model ===
    print("======== Testing Ab3 Model ======== ")
    ab3 = Ab3()
    marked, opaque_ab3 = bfs(ab3, check_exclusion, [])
    print("Ab3 Exclusion Violations:", opaque_ab3)
    
    marked_deadlock, deadlocks = bfs(ab3, check_deadlock, ab3)