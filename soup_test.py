from struct.soup import Piece, Soup, Soupsemantics

To1 = Piece(lambda c:1, lambda c:c==0,"To1")
To2 = Piece(lambda c:0, lambda c:c==1,"To2")

clock1 = Soup([To1,To2],0)
clocksemantics= Soupsemantics(clock1)
print(clocksemantics.actions(0)[0].nom)