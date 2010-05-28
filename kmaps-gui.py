#!/usr/local/bin/python     
from Tkinter import *
from copy import deepcopy
import kmaps.game, kmaps.common

class KmapsGui(Frame, kmaps.game.Grid):
    widgets = []
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.printtable()

    def printtable(self):
        for level in range(0,2):
            frame = Frame(self)
            frame.grid(row = level)
            for mrow in range(0,4):
                for mcol in range(0,4):
                    box    = StringVar()
                    box.set(' ')
                    command = lambda: self.move(level+1, mrow+1, mcol+1, 0)
                    self.mgrid[level][mrow][mcol] = box
                    self.widgets.append(Button(frame,\
                                    textvariable = box,\
                                    command      = command\
                                    ).grid(row = mrow, column = mcol))
            frame.pack()
            if level == 0:
                separator = Frame(self, height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)
        print command
    
    def move(self, level, row, column, player):
        print level,row,column
        level  = int(level)
        row    = int(row)
        column = int(column)
        player = int(player)
        if not level  in [  1,2]     or \
           not row    in [  1,2,3,4] or \
           not column in [  1,2,3,4] or \
           not player in [0,1]:
            return False
        elif self.mgrid[level-1][row-1][column-1].get() != " ":
            return False
        else:
            self.mgrid[level-1][row-1][column-1].set(player)
        return True
        
app = KmapsGui()                    
app.master.title("Kmaps")
app.mainloop()
