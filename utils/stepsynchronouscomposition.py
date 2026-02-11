class StepSynchronousComposition:
    def __init__(self, current_state, next_state, transition):
        self.current_state = current_state
        self.next_state = next_state
        self.transition = transition

# L'idée est de créer une classe qui prenne le I a transmettre à Isoup mais je n'arrive pas savoir ou l'intégrer dans la structure