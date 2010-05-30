#!/usr/local/bin/python     
from Tkinter import *
from copy import deepcopy
import kmaps.game, kmaps.common

class KmapsGui(Frame, kmaps.game.Grid, kmaps.game.Game):
    widgets = []
    
    def __init__(self, master=None):
	self.mgrid = kmaps.game.Grid.grid
        Frame.__init__(self, master)
        self.grid()
        self.printtable()

    def printtable(self):
        commands = {0: {\
                0: {0:lambda: self.move(1, 1, 1, 0),\
                    1:lambda: self.move(1, 1, 2, 0),\
                    2:lambda: self.move(1, 1, 3, 0),\
                    3:lambda: self.move(1, 1, 4, 0)},\
                1: {0:lambda: self.move(1, 2, 1, 0),\
                    1:lambda: self.move(1, 2, 2, 0),\
                    2:lambda: self.move(1, 2, 3, 0),\
                    3:lambda: self.move(1, 2, 4, 0)},\
                2: {0:lambda: self.move(1, 3, 1, 0),\
                    1:lambda: self.move(1, 3, 2, 0),\
                    2:lambda: self.move(1, 3, 3, 0),\
                    3:lambda: self.move(1, 3, 4, 0)},\
                3: {0:lambda: self.move(1, 4, 1, 0),\
                    1:lambda: self.move(1, 4, 2, 0),\
                    2:lambda: self.move(1, 4, 3, 0),\
                    3:lambda: self.move(1, 4, 4, 0)}},\
            1: {\
                0: {0:lambda: self.move(2, 1, 1, 0),\
                    1:lambda: self.move(2, 1, 2, 0),\
                    2:lambda: self.move(2, 1, 3, 0),\
                    3:lambda: self.move(2, 1, 4, 0)},\
                1: {0:lambda: self.move(2, 2, 1, 0),\
                    1:lambda: self.move(2, 2, 2, 0),\
                    2:lambda: self.move(2, 2, 3, 0),\
                    3:lambda: self.move(2, 2, 4, 0)},\
                2: {0:lambda: self.move(2, 3, 1, 0),\
                    1:lambda: self.move(2, 3, 2, 0),\
                    2:lambda: self.move(2, 3, 3, 0),\
                    3:lambda: self.move(2, 3, 4, 0)},\
                3: {0:lambda: self.move(2, 4, 1, 0),\
                    1:lambda: self.move(2, 4, 2, 0),\
                    2:lambda: self.move(2, 4, 3, 0),\
                    3:lambda: self.move(2, 4, 4, 0)}}}
        for level in range(0,2):
            frame = Frame(self)
            frame.grid(row = level)
            for mrow in range(0,4):
                for mcol in range(0,4):
                    box    = StringVar()
                    box.set(' ')
                    self.mgrid[level][mrow][mcol] = box
                    self.widgets.append(Button(frame,\
                                    textvariable = box,\
                                    command      = commands[level][mrow][mcol]\
                                    ).grid(row = mrow, column = mcol))
            frame.pack()
            if level == 0:
                separator = Frame(self, height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)
    
    def move(self, level, row, column, player):
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
