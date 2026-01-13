from models.LS2RG import HanoiLanguageSemantics
from struct.lang_semantics import LS2RG
from utils.traversal import bfs


def hanoi_solver_ls(n):
    ls = HanoiLanguageSemantics(n)
    rg = LS2RG(ls)

    def on_entry(state, opaque):
        if ls.is_solution(state):
            opaque.append(state)
            return True, opaque   # stop = True
        return False, opaque     # continue BFS

    return bfs(rg, on_entry, [])


# ===========================
# TEST
# ===========================
print("=== Résolution de Hanoi avec Language Semantics ===")
opaque, visited = hanoi_solver_ls(3)

print(f"Nombre d'états explorés : {len(visited)}")
print(f"Solution trouvée : {opaque}")
