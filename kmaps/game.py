# Copyright (C) 2010 Kevin Chung <kchungsp93@gmail.com>
#                    Tyler Romeo <tylerromeo@gmail.com>,
#                    Eugene Dobry <edobry@gmail.com>:
#
# This file is part of Kmaps.
#
# Kmaps is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Kmaps is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Kmaps.  If not, see <http://www.gnu.org/licenses/>.

from common import *
from Tkinter import *
import players

class Game:
    grid = 0
    players = [0,1]
    
    def __init__(self, multiplayer=False):
        self.grid = Grid()
        self.players[0] = players.Human(self.grid, 0)
        if not multiplayer:
            self.players[1] = players.Computer(self.grid, 1)
        else:
            self.players[1] = players.Human(self.grid, 1)
    
    def play(self):
        current = 0
        status  = 1
        for move in range(0,32):
            if status:
                self.grid.printtable()
            status = self.players[current].move()
            if status:
                current = (current + 1) % 2
            else:
                cout("Invalid move.")
        return True
     
    def winner(self):
        # Use grid to determine winner.
        return 0

class Grid:
    """The Kmaps grid."""
    
    grid = {0:\
               {0:{0:" ",1:" ",2:" ",3:" "},\
                1:{0:" ",1:" ",2:" ",3:" "},\
                2:{0:" ",1:" ",2:" ",3:" "},\
                3:{0:" ",1:" ",2:" ",3:" "}},\
            1:\
               {0:{0:" ",1:" ",2:" ",3:" "},\
                1:{0:" ",1:" ",2:" ",3:" "},\
                2:{0:" ",1:" ",2:" ",3:" "},\
                3:{0:" ",1:" ",2:" ",3:" "}}}
    
    def __getattr__(self, key):
        if not key[0] == 'g':
		    raise AttributeError
        level  = int(key[1]) - 1
        row    = int(key[2]) - 1
        column = int(key[3]) - 1
        
        if column == -1:
            return self.grid[level][row]
        elif row == -1:
            return [self.grid[level][0][column],\
                    self.grid[level][1][column],\
                    self.grid[level][2][column],\
                    self.grid[level][3][column]]
        else:
            return str(self.grid[level][row][column])
    
    def get(self, level, row, column):
        return self.grid[level][row][column]
    
    def set(self, level, row, column, player):
        self.grid[level][row][column] = player
    
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
        elif self.get(level-1, row-1, column-1) != " ":
           return False
        else:
            self.set(level-1, row-1, column-1, player)
        return True
    
    def printtable(self):
        a = self
        cout("-----------------"                                    )
        cout("| "+a.g111+" | "+a.g112+" | "+a.g113+" | "+a.g114+" |")
        cout("-----------------"                                    )
        cout("| "+a.g121+" | "+a.g122+" | "+a.g123+" | "+a.g124+" |")
        cout("-----------------"                                    )
        cout("| "+a.g131+" | "+a.g132+" | "+a.g133+" | "+a.g134+" |")
        cout("-----------------"                                    )
        cout("| "+a.g141+" | "+a.g142+" | "+a.g143+" | "+a.g144+" |")
        cout("-----------------"                                    )
        cout(""                                                     )
        cout(""                                                     )
        cout("-----------------"                                    )
        cout("| "+a.g211+" | "+a.g212+" | "+a.g213+" | "+a.g214+" |")
        cout("-----------------"                                    )
        cout("| "+a.g221+" | "+a.g222+" | "+a.g223+" | "+a.g224+" |")
        cout("-----------------"                                    )
        cout("| "+a.g231+" | "+a.g232+" | "+a.g233+" | "+a.g234+" |")
        cout("-----------------"                                    )
        cout("| "+a.g241+" | "+a.g242+" | "+a.g243+" | "+a.g244+" |")
        cout("-----------------"                                    )

class Game_Gui(Game):
    grid = 0
    
    def __init__(self, multiplayer=False):
        self.grid = Grid_Gui()
        self.computer = players.Computer(self.grid, 1)
    
    def play(self):
        self.current = 0
        self.status  = 1
        self.grid.printtable(self.callback)
        self.grid.master.title("Kmaps")
        self.grid.mainloop()

    def callback(self, level, row, column, player):
        self.grid.move(level, row, column, self.current)
        self.computer.move()

class Grid_Gui(Grid, Frame):
    widgets = []
    
    def __init__(self, master=None):
        self.mgrid = Grid.grid
        Frame.__init__(self, master)
        Frame.grid(self)

    def printtable(self, callback):
        commands = {0: {\
                0: {0:lambda: callback(1, 1, 1, 0),\
                    1:lambda: callback(1, 1, 2, 0),\
                    2:lambda: callback(1, 1, 3, 0),\
                    3:lambda: callback(1, 1, 4, 0)},\
                1: {0:lambda: callback(1, 2, 1, 0),\
                    1:lambda: callback(1, 2, 2, 0),\
                    2:lambda: callback(1, 2, 3, 0),\
                    3:lambda: callback(1, 2, 4, 0)},\
                2: {0:lambda: callback(1, 3, 1, 0),\
                    1:lambda: callback(1, 3, 2, 0),\
                    2:lambda: callback(1, 3, 3, 0),\
                    3:lambda: callback(1, 3, 4, 0)},\
                3: {0:lambda: callback(1, 4, 1, 0),\
                    1:lambda: callback(1, 4, 2, 0),\
                    2:lambda: callback(1, 4, 3, 0),\
                    3:lambda: callback(1, 4, 4, 0)}},\
            1: {\
                0: {0:lambda: callback(2, 1, 1, 0),\
                    1:lambda: callback(2, 1, 2, 0),\
                    2:lambda: callback(2, 1, 3, 0),\
                    3:lambda: callback(2, 1, 4, 0)},\
                1: {0:lambda: callback(2, 2, 1, 0),\
                    1:lambda: callback(2, 2, 2, 0),\
                    2:lambda: callback(2, 2, 3, 0),\
                    3:lambda: callback(2, 2, 4, 0)},\
                2: {0:lambda: callback(2, 3, 1, 0),\
                    1:lambda: callback(2, 3, 2, 0),\
                    2:lambda: callback(2, 3, 3, 0),\
                    3:lambda: callback(2, 3, 4, 0)},\
                3: {0:lambda: callback(2, 4, 1, 0),\
                    1:lambda: callback(2, 4, 2, 0),\
                    2:lambda: callback(2, 4, 3, 0),\
                    3:lambda: callback(2, 4, 4, 0)}}}
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
    
    def get(self, level, row, column):
        return self.mgrid[level][row][column].get()
    
    def set(self, level, row, column, player):
        self.mgrid[level][row][column].set(player)
