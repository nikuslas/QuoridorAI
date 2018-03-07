from Pion import Pion
from Plateforme import Plateforme
from Barre import Barre
import tkinter as tk
from tkinter import *
import sys, termios, tty

root = Tk()
pion = Pion(4,4)
board = Plateforme(root, pion)
board.placePiece()
barreList = []

def callback(event):
    print "clicked at", event.x, event.y

def key(event):
    k=event.keysym
    if k == 'Up':
        board.deleteCircle()
        board.pion.setPositionVetc((board.pion.x_pos-1), (board.pion.y_pos), barreList)
        board.placePiece()
        board.update()
    elif k=='Down':
        board.deleteCircle()
        board.pion.setPositionVetc((board.pion.x_pos+1), (board.pion.y_pos), barreList)
        board.placePiece()
        board.update()
    elif k=='Right':
        board.deleteCircle()
        board.pion.setPositionHorz((board.pion.x_pos), (board.pion.y_pos+1), barreList)
        board.placePiece()
        board.update()
    elif k=='Left':
        board.deleteCircle()
        board.pion.setPositionHorz((board.pion.x_pos), (board.pion.y_pos-1), barreList)
        board.placePiece()
        board.update()


def main():
    """board = Plateforme(root, pion)"""
    barre = Barre(((3,4),(3,5)),((4,4),(4,5)))
    barre2 = Barre(((4,3),(5,3)),((4,4),(5,4)))
    barre3 = Barre(((1,6),(1,7)),((2,6),(2,7)))
    barre4 = Barre(((5,0),(5,1)),((6,0),(6,1)))
    barre3.setBarre()
    barre2.setBarre()
    barre.setBarre()
    barre4.setBarre()

    barreList.append(barre2)
    barreList.append(barre3)
    barreList.append(barre)
    barreList.append(barre4)

    board.drawBarre(barre3.barreCoord)
    board.drawBarre(barre2.barreCoord)
    board.drawBarre(barre.barreCoord)
    board.drawBarre(barre4.barreCoord)

    board.focus_set()
    board.bind("<Button-1>", callback)
    board.bind("<Key>", key)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()


if __name__ == "__main__":
    main()
