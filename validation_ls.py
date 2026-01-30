from models.LS2RG import HanoiLanguageSemantics
from struct.lang_semantics import LS2RG
from utils.traversal import bfs
from struct.soup.soup_semantics import Soupsemantics
from models.hanoi.hanoisoup import HanoiSoup


def hanoi_solver_ls(n):
    ls = HanoiLanguageSemantics(n)
    rg = LS2RG(ls)

    def on_entry(state, opaque):
        if ls.is_solution(state):
            opaque.append(state)
            return True, opaque   # stop = True
        return False, opaque     # continue BFS

    return bfs(rg, on_entry, [])

def hanoi_solver_soup(n):
    # 1. Instancier la Soupe (Données + Règles locales)
    soup = HanoiSoup(n)
    
    # 2. Instancier la Sémantique (Moteur d'exécution)
    soup_sem = Soupsemantics(soup)
    
    # 3. Adapter pour le Graphe (Interface pour le BFS)
    rg = LS2RG(soup_sem)

    # Définition de l'état cible : [n, n-1, ..., 1]
    target_peg = list(range(n, 0, -1))

    def on_entry(state, opaque):
        # state est une liste de 3 listes : [[...], [...], [...]]
        # On vérifie si la tige 1 ou 2 est pleine
        if state[1] == target_peg or state[2] == target_peg:
            opaque.append(state)
            return True, opaque   # Stop = True (on a trouvé)
        return False, opaque      # Stop = False (on continue)

    # Lancement du BFS
    return bfs(rg, on_entry, [])


# ======================================
# TEST du Hanoi avec Language Semantics
# ======================================
print("=== Résolution de Hanoi avec Language Semantics ===")
opaque, visited = hanoi_solver_ls(3)

print(f"Nombre d'états explorés : {len(visited)}")
print(f"Solution trouvée : {opaque}")

# ======================================
# TEST du Hanoi avec Soup Semantics 
# ======================================
print("=== Résolution de Hanoi avec Soup Semantics ===")
solution_soup, visited_soup = hanoi_solver_soup(3)
print(f"Nombre d'états explorés : {len(visited_soup[0])}")

if solution_soup:
    print("Solution trouvée : ")
    for state in solution_soup:
        print(state)
else:
    print("Aucune solution trouvée.")
