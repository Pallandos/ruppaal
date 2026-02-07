class Isoup :
    """
    Isoup is similar to soup
    """

    def __init__(self, ipieces, init_value):
        self.ipieces = ipieces
        self.init_value = init_value

    def extend(self, b):
        if isinstance(b, Ipiece):
            self.ipieces.append(b)
        else:
            self.ipieces.extend(b)

    def add(self, name, guard, generator):
        self.extend(Ipiece(name, guard,generator))

class Ipiece:
    """
    Ipiece is a part of a Isoup. 

    self.garde and self.effet are lambda functions
    """
    def __init__(self, effet, garde, nom):
        self.effet = effet
        self.garde = garde
        self.nom = nom

    def __eq__(self, other):
        if not isinstance(other, Ipiece):
            return False
        return self.nom == other.nom and self.gard == other.garde and self.effet == other.effet
