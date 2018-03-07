class Pion(object):
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def setPositionVetc(self, x, y, barre):
        tup = (self.x_pos, self.y_pos)
        tupRel = (x, y)
        if (0 <= x <= 8):
            for b in barre:
                if(x<self.x_pos):
                    if ((tup == b.otherSide[0]) and (tupRel == b.oneSide[0])):
                        return None
                    elif ((tup == b.otherSide[1]) and (tupRel == b.oneSide[1])):
                        return None
                    else:
                        continue


                if(x>self.x_pos):
                    if ((tup == b.oneSide[0]) and (tupRel == b.otherSide[0])):
                        return None
                    elif ((tup == b.oneSide[1]) and (tupRel == b.otherSide[1])):
                        return None
                    else:
                        continue
            self.x_pos = x

    def setPositionHorz(self, x, y, barre):
        tup = (self.x_pos, self.y_pos)
        tupRel = (x, y)

        if (0 <= y <= 8):
            for b in barre:
                if(y<self.y_pos):
                    if ((tup == b.otherSide[0]) and (tupRel == b.oneSide[0])):
                        return None
                    elif ((tup == b.otherSide[1]) and (tupRel == b.oneSide[1])):
                        return None
                    else:
                        continue

                if(y>self.y_pos):
                    if ((tup == b.oneSide[0]) and (tupRel == b.otherSide[0])):
                        return None
                    elif ((tup == b.oneSide[1]) and (tupRel == b.otherSide[1])):
                        return None
                    else:
                        continue
            self.y_pos = y
