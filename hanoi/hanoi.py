from __future__ import annotations
from rootedGraph import RootedGraph
from copy import deepcopy
from bfs import bfs

class HanoiTower():
    
    def __init__(self, n_disk : int) -> None:
        self._n_disk = n_disk   
        self.state = [[n_disk - i for i in range(n_disk)], [], []]

    def __eq__(self, other) -> bool:
        if not isinstance(other, HanoiTower):
            return False
        return self.state == other.state
    
    def move(self, source : int, dest : int) -> tuple[HanoiTower, bool]:
        
        if source not in [1,2,3] or dest not in [1,2,3]:
            raise ValueError("source and dest must be within {1,2,3}")
        
        if len(self.state[source - 1]) == 0:
            # invalid move
            return(deepcopy(self), False)
        elif len(self.state[dest - 1]) > 0 and self.state[source - 1][-1] > self.state[dest - 1][-1]:
            # invalid move
            return(deepcopy(self), False)
        else:
            # valid move
            new_tower = deepcopy(self)
            puck = new_tower.state[source - 1].pop(-1)
            new_tower.state[dest - 1].append(puck)
            return (new_tower, True)

class HanoiGraph(RootedGraph):
    
    def __init__(self, tower : HanoiTower):
        self.tower = tower
        
    def roots(self):
        return [self.tower]
    
    def neighbors(self, vertex) -> list:
        out = []
        
        # test and create all future moves
        possible = []
        possible.append(vertex.move(1,2))
        possible.append(vertex.move(1,3))
        possible.append(vertex.move(2,1))
        possible.append(vertex.move(2,3))
        possible.append(vertex.move(3,1))
        possible.append(vertex.move(3,2))
        
        for (tower, test) in possible:
            if test:
                out.append(tower)
        
        return out

if __name__ == "__main__":
    hanoiTower = HanoiTower(3)
    hanoiGraph = HanoiGraph(hanoiTower)

    on_entry = lambda x,opaque : (x.state[2] == [3,2,1], opaque)

    retour, out = bfs(hanoiGraph, on_entry, 0)
    
    # print all states
    for tower in retour:
        print(tower.state)