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

class Computer:
    """Handles the fitness calculations for the computer."""
    moves = 0
    
    def __init__(self, grid, player):
        self.grid = grid
        self.player = player
    
    def fitness(self, level, row, column, player):
        level  = int(level) - 1
        row    = int(row) - 1
        column = int(column) - 1
        if self.grid.get(level, row, column) != " ":
            return 0
        
        # Get the surrounding spaces
        u   = self.grid.get( level     , (row+1)%4,  column     )
        d   = self.grid.get( level     , (row-1)%4,  column     )
        l   = self.grid.get( level     ,  row     , (column-1)%4)
        r   = self.grid.get( level     ,  row     , (column+1)%4)
        ul  = self.grid.get( level     , (row+1)%4, (column-1)%4)
        ur  = self.grid.get( level     , (row+1)%4, (column+1)%4)
        dl  = self.grid.get( level     , (row-1)%4, (column-1)%4)
        dr  = self.grid.get( level     , (row-1)%4, (column+1)%4)
        
        # Get the surrounding spaces on the other level
        a   = self.grid.get((level+1)%2,  row     ,  column     )
        au  = self.grid.get((level+1)%2, (row+1)%4,  column     )
        ad  = self.grid.get((level+1)%2, (row-1)%4,  column     )
        al  = self.grid.get((level+1)%2,  row     , (column-1)%4)
        ar  = self.grid.get((level+1)%2,  row     , (column+1)%4)
        aul = self.grid.get((level+1)%2, (row+1)%4, (column-1)%4)
        aur = self.grid.get((level+1)%2, (row+1)%4, (column+1)%4)
        adl = self.grid.get((level+1)%2, (row-1)%4, (column-1)%4)
        adr = self.grid.get((level+1)%2, (row-1)%4, (column+1)%4)
        
        # Get final boxes necessary for other quads
        rr  = self.grid.get( level     , row      , (column+2)%4)
        dd  = self.grid.get( level     , (row-2)%4,  column     )
        
        # Create the quads
        q0 = [u, l, ul]
        q1 = [u, r, ur]
        q2 = [d, l, dl]
        q3 = [d, r, dr]
        q4 = [a, u, au]
        q5 = [a, d, ad]
        q6 = [a, l, al]
        q7 = [a, r, ar]
        q8 = [l, r, rr]
        q9 = [u, d, dd]
        quads  = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9]
        scores = []
        
        # Calculate the individual scores
        otherplayer = (player - 1) % 2
        for q in quads:
            i = 1
            if otherplayer in q:
                scores.append(0)
            else:
                if q[0] == str(player):
                    i += 1
                if q[1] == str(player):
                    i += 1
                if q[2] == str(player):
                    i += 1
                i = pow(i,2)
                scores.append(i)
        # Put together final fitness score
        return sum(scores)
        
    def move(self):
        """Get the fitness for each square and make a move."""
        flevel = frow = fcolumn = fscore = 0
        otherplayer = (self.player - 1) % 2
        for level in range(1,3):
            for row in range(1,5):
                for column in range(1,5):
                    score1 = self.fitness(level, row, column, self.player)
                    score2 = self.fitness(level, row, column, otherplayer  )
                    score  = score1 + score2
                    if score > fscore:
                        flevel  = level
                        frow    = row
                        fcolumn = column
                        fscore  = score
        return self.grid.move(flevel, frow, fcolumn, self.player)

class Human:
    grid = 0
    
    def __init__(self, grid, player):
        self.grid = grid
        self.player = player
    
    def move(self):
        position = cin("Where do you want to go? ")
        if len(position) != 3:
            return False
        level  = position[0]
        row    = position[1]
        column = position[2]
        return self.grid.move(level, row, column, self.player)
