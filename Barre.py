class Barre(object):

    def __init__(self, oneS, otherS):
        self.intersect = []
        self.oneSide = oneS
        self.otherSide = otherS
        self.barreCoord = []

    def setBarre(self):
        if self.oneSide[0][1] == self.otherSide[0][1]:
            self.barreCoord.append(self.otherSide[0][1]*74)
            self.barreCoord.append(self.otherSide[0][0]*74)
            self.barreCoord.append((self.otherSide[0][1]+2)*74)
            self.barreCoord.append(self.otherSide[0][0]*74)
        else:
            self.barreCoord.append(self.otherSide[0][0]*74)
            self.barreCoord.append(self.otherSide[0][1]*74)
            self.barreCoord.append(self.otherSide[0][0]*74)
            self.barreCoord.append((self.otherSide[0][1]+2)*74)





    def getIntersect(self):
        inter1 = []
        inter2 = []
        inter3 = []

        if self.oneSide[0][1] == self.otherSide[0][1] and self.oneSide[1][1] == self.otherSide[1][1]:
            if self.oneSide[0][1] == 0:
                inter1.append((-1, -1))
                inter1.append(self.oneSide[0])
                inter1.append((-1, -1))
                inter1.append(self.otherSide[0])
            else:
                inter1.append((self.oneSide[0][0] , (self.oneSide[0][1]-1)))
                inter1.append(self.oneSide[0])
                inter1.append((self.otherSide[0][0] , (self.otherSide[0][1]-1)))
                inter1.append(self.otherSide[0])

            inter2.append(self.oneSide[0])
            inter2.append(self.oneSide[1])
            inter2.append(self.otherSide[0])
            inter2.append(self.otherSide[1])

            if self.oneSide[1][1] == 8:
                inter3.append(self.oneSide[1])
                inter3.append((-1, -1))
                inter3.append(self.otherSide[1])
                inter3.append((-1, -1))
            else:
                inter3.append(self.oneSide[1])
                inter3.append((self.oneSide[0][0] , (self.oneSide[1][1]+1)))
                inter3.append(self.otherSide[1])
                inter3.append((self.otherSide[0][0] , (self.otherSide[1][1]+1)))
        else:
            if self.oneSide[0][0] == 0:
                inter1.append((-1, -1))
                inter1.append((-1, -1))
                inter1.append(self.oneSide[0])
                inter1.append(self.otherSide[0])
            else:
                inter1.append(((self.oneSide[0][0]-1) , self.oneSide[0][1]))
                inter1.append(((self.otherSide[0][0]-1) , self.otherSide[0][1]))
                inter1.append(self.oneSide[0])
                inter1.append(self.otherSide[0])

            inter2.append(self.oneSide[0])
            inter2.append(self.otherSide[0])
            inter2.append(self.oneSide[1])
            inter2.append(self.otherSide[1])

            if self.otherSide[1][0] == 8:
                inter3.append(self.oneSide[1])
                inter3.append(self.otherSide[1])
                inter3.append((-1, -1))
                inter3.append((-1, -1))
            else:
                inter3.append(self.oneSide[1])
                inter3.append(self.otherSide[1])
                inter3.append(((self.oneSide[1][0]+1) , self.oneSide[1][1]))
                inter3.append(((self.otherSide[1][0]+1) , self.otherSide[1][1]))

        self.intersect.append(inter1)
        self.intersect.append(inter2)
        self.intersect.append(inter3)
