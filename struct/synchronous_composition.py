from struct.lang_semantics import LanguageSemantics

class SynchronousComposition(LanguageSemantics):
    """
    Implémente la composition synchrone de deux sémantiques (lhs || rhs).
    
    Règles :
    - Les états sont des paires (état_gauche, état_droit).
    - Si une action a le même nom dans les deux modèles, elle doit être exécutée simultanément (Synchronisation).
    - Sinon, elle peut s'exécuter seule (Entrelacement).
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initials(self):
        """Produit cartésien des états initiaux"""
        initials = []
        for l_state in self.lhs.initials():
            for r_state in self.rhs.initials():
                initials.append((l_state, r_state))
        return initials

    def actions(self, state):
        l_state, r_state = state
        
        # Récupérer les actions possibles pour chaque sous-état
        l_actions = self.lhs.actions(l_state)
        r_actions = self.rhs.actions(r_state)
        
        compound_actions = []
        
        # Dictionnaires pour faciliter la recherche par nom
        # On suppose que action.nom existe (comme dans Soup), sinon on utilise str(action)
        l_map = {self._get_name(a): a for a in l_actions}
        r_map = {self._get_name(a): a for a in r_actions}
        
        l_names = set(l_map.keys())
        r_names = set(r_map.keys())
        
        # 1. Actions synchronisées (intersection des noms)
        common_names = l_names.intersection(r_names)
        for name in common_names:
            # On crée une action composite (gauche, droite)
            compound_actions.append((l_map[name], r_map[name]))
            
        # 2. Actions de gauche indépendantes (seulement si non présentes à droite)
        for name in l_names - r_names:
            compound_actions.append((l_map[name], None))
            
        # 3. Actions de droite indépendantes
        for name in r_names - l_names:
            compound_actions.append((None, r_map[name]))
            
        return compound_actions

    def execute(self, state, action):
        l_state, r_state = state
        l_action, r_action = action # action est un tuple (act_G, act_D)
        
        # Exécution à gauche
        if l_action is not None:
            l_next_states = self.lhs.execute(l_state, l_action)
        else:
            l_next_states = [l_state] # Reste sur place
            
        # Exécution à droite
        if r_action is not None:
            r_next_states = self.rhs.execute(r_state, r_action)
        else:
            r_next_states = [r_state] # Reste sur place
            
        # Produit cartésien des états d'arrivée
        next_states = []
        for l_next in l_next_states:
            for r_next in r_next_states:
                next_states.append((l_next, r_next))
                
        return next_states

    def _get_name(self, action):
        """Helper pour récupérer le nom d'une action de manière robuste"""
        if hasattr(action, 'nom'):
            return action.nom
        if hasattr(action, 'name'):
            return action.name
        return str(action)