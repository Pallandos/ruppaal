from models.alicebob import AliceBobSoup
from struct.soup.soup_semantics import Soupsemantics
from struct.lang_semantics import LS2RG
from utils.traversal import bfs, get_trace

def alicebob_solver_soup():
    # 1. Instancier la Soupe (Données + Règles locales)
    soup = AliceBobSoup()
    
    # 2. Instancier la Sémantique (Moteur d'exécution)
    soup_sem = Soupsemantics(soup)
    
    # 3. Adapter pour le Graphe (Interface pour le BFS)
    rg = LS2RG(soup_sem)

    def on_entry(state, opaque):
        # state est une liste de 2 éléments : [alice_state, bob_state]
        # On vérifie si les deux sont dans la section critique
        if state[0] == 1 and state[1] == 1:
            opaque.append(state)
            return True, opaque   # Stop = True (on a trouvé)
        return False, opaque      # Stop = False (on continue)

    # Lancement du BFS
    return bfs(rg, on_entry, [])


# ======================================
# TEST de Alice et bob avec Soup Semantics
# ======================================
print("=== Résolution de Alice et Bob avec Soup Semantics ===")
marked, solution = alicebob_solver_soup()

print(f"Nombre d'états explorés (Soup Semantics) : {len(marked)}")
if solution:
    print("Erreur trouvée (État final) :", solution[0])
    trace = get_trace(marked, solution[0])
    print(f"Trace (longueur {len(trace)}):")
    for s in trace:
        print(s)

