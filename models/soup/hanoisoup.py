from models.soup.soup_langage import Soup, Piece, Soupsemantics

def is_transfert_valid(origin, dest) :
    #[topA, topB, topC]
    return (origin<dest)

def is_transfert_valid_12(state) :
    #[topA, topB, topC]
    return (state[1]>state[0])


def transfert(todo : str):
    source = todo[1]
    dest = todo[2]

    if source not in ["1","2","3"] or dest not in ["1","2","3"]:
        raise TypeError
    
    


T11 = Piece(transfert, is_transfert_valid,"T11")
T12 = Piece(transfert, is_transfert_valid,"T12")
T13 = Piece(transfert, is_transfert_valid,"T13")
T21 = Piece(transfert, is_transfert_valid,"T21")
T22 = Piece(transfert, is_transfert_valid,"T22")
T23 = Piece(transfert, is_transfert_valid,"T23")
T31 = Piece(transfert, is_transfert_valid,"T31")
T32 = Piece(transfert, is_transfert_valid,"T32")
T33 = Piece(transfert, is_transfert_valid,"T33")



class HanoiSoup(Soup):
    def __init__(self, pieces, init_value):
        self.pieces = pieces
        self.init_value = init_value


