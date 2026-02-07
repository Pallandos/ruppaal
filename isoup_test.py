# from struct.Isoup import Isoup, Ipiece, Isoupsemantics
# from struct.soup import Piece, Soup, Soupsemantics

# To1 = Piece(lambda c:1, lambda c:c==0,"To1")
# To2 = Piece(lambda c:0, lambda c:c==1,"To2")
# To3 = Piece(lambda c:1, lambda c:c==0,"To3")
# To4 = Piece(lambda c:0, lambda c:c==1,"To4")

# sou1 = Soup([To1,To2],0)
# sou2 = Soup([To3,To4],0)

# def f1():
#     pass

# def f2():
#     pass

# ipotage1 = Ipiece(f1, f2,"Ip1")
# ipotage2 = Ipiece(f2, f1,"Ip2")

# clock1 = Isoup([ipotage1, ipotage2],0)

# clocksematntics = Isoupsemantics(ipotage1)
# print(clocksematntics.actions)


from struct.Isoup import Ipiece, Isoup, Isoupsemantics

To1 = Ipiece(lambda c:1, lambda c:c==0,"To1")
To2 = Ipiece(lambda c:0, lambda c:c==1,"To2")

clock1 = Isoup([To1,To2],0)
clocksemantics= Isoupsemantics(clock1)
print(clocksemantics.actions(0)[0].nom)