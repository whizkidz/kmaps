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
import players

class Game:
    grid = 0
    __players = [0,1]
    
    def __init__(self, multiplayer=False):
        self.grid = Grid()
        self.__players[0] = players.Human(self.grid, 0)
        if not multiplayer:
            self.__players[1] = players.Computer(self.grid, 1)
        else:
            self.__players[1] = players.Human(self.grid, 1)
    
    def play(self):
        current = 0
        status  = 1
        for move in range(0,32):
            if status:
                self.grid.printtable()
            status = self.__players[current].move()
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
	if key[0] != 'g':
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
        elif self.grid[level-1][row-1][column-1] != " ":
           return False
        else:
            self.grid[level-1][row-1][column-1] = player
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
