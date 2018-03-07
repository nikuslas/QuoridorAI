"""import numpy as np"""
import tkinter as tk
from Barre import Barre
from Pion import Pion

class Plateforme(tk.Frame):
    def __init__(self, parent, pion, rows=9, columns=9, rectSize=75):
        self.width = columns * rectSize
        self.height = rows * rectSize
        """self.gamePlateform = np.zeros((rows,columns))"""

        self.rows = rows
        self.columns = columns
        self.size = rectSize
        self.color1 = "SlateGray1"
        self.color2 = "bisque2"
        self.pieces = {}
        self.pion = pion

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=self.width, height=self.height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''

        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)

        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        self.deleteCircle()
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color != self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        """for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])"""
        self.placePiece()
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def placePiece2(self):
        self.canvas.create_line(296, 296, 444, 296, width=4, fill="black")
        self.canvas.create_line(296, 296, 296, 444, width=4, fill="black")

    def drawBarre(self, barre):
        self.canvas.create_line(barre[0], barre[1], barre[2], barre[3], width=4, fill="black")

    def placePiece(self):
        x = (15 * self.size)/74
        y = (60 * self.size)/74
        self.circle = self.canvas.create_oval(x + (self.size*self.pion.y_pos), x + (self.size*self.pion.x_pos), y + (self.size*self.pion.y_pos), y + (self.size*self.pion.x_pos), outline="gray", fill="black", width=2)

    def deleteCircle(self):
        self.canvas.delete(self.circle)

    def checkIntersection(self, b1, b2):
        for l in b1.intersect:
            for t in b2.intersect:
                if cmp(l,t) == 0:
                    print ("intersection")
