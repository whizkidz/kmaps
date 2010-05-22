class Computer:
    """Handles the fitness calculations for the computer."""
    __moves = 0
    
    def __init__(self, grid, player):
        self.__grid = grid
        self.__player = player
    
    def fitness(self, level, row, column, player):
        level = level - 1
        row   = row - 1
        column = column - 1
        
        if self.__grid.grid[level][row][column] != " ":
            return 0
        
        # Get the surrounding spaces
        u   = self.__grid.grid[ level     ][(row+1)%4][ column     ]
        d   = self.__grid.grid[ level     ][(row-1)%4][ column     ]
        l   = self.__grid.grid[ level     ][ row     ][(column-1)%4]
        r   = self.__grid.grid[ level     ][ row     ][(column+1)%4]
        ul  = self.__grid.grid[ level     ][(row+1)%4][(column-1)%4]
        ur  = self.__grid.grid[ level     ][(row+1)%4][(column+1)%4]
        dl  = self.__grid.grid[ level     ][(row-1)%4][(column-1)%4]
        dr  = self.__grid.grid[ level     ][(row-1)%4][(column+1)%4]
        
        # Get the surrounding spaces on the other level
        a   = self.__grid.grid[(level+1)%2][ row     ][ column     ]
        au  = self.__grid.grid[(level+1)%2][(row+1)%4][ column     ]
        ad  = self.__grid.grid[(level+1)%2][(row-1)%4][ column     ]
        al  = self.__grid.grid[(level+1)%2][ row     ][(column-1)%4]
        ar  = self.__grid.grid[(level+1)%2][ row     ][(column+1)%4]
        aul = self.__grid.grid[(level+1)%2][(row+1)%4][(column-1)%4]
        aur = self.__grid.grid[(level+1)%2][(row+1)%4][(column+1)%4]
        adl = self.__grid.grid[(level+1)%2][(row-1)%4][(column-1)%4]
        adr = self.__grid.grid[(level+1)%2][(row-1)%4][(column+1)%4]
        
        # Get final boxes necessary for other quads
        rr  = self.__grid.grid[ level     ][ row     ][(column+2)%4]
        dd  = self.__grid.grid[ level     ][(row-2)%4][ column     ]
        
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
                if q[0] == player:
                    i += 1
                if q[1] == player:
                    i += 1
                if q[2] == player:
                    i += 1
                i = pow(i,2)
                scores.append(i)
        # Put together final fitness score
        return sum(scores)
        
    def move(self):
        """Get the fitness for each square and make a move."""
        flevel = frow = fcolumn = fscore = 0
        otherplayer = (self.__player - 1) % 2
        for level in range(1,3):
            for row in range(1,5):
                for column in range(1,5):
                    score1 = self.fitness(level, row, column, self.__player)
                    score2 = self.fitness(level, row, column, otherplayer  )
                    score  = score1 + score2
                    if score > fscore:
                        flevel  = level
                        frow    = row
                        fcolumn = column
                        fscore  = score
        return self.__grid.move(flevel, frow, fcolumn, self.__player)

class Human:
    __grid = 0
    
    def __init__(self, grid, player):
        self.__grid = grid
        self.__player = player
    
    def move(self):
        position = raw_input("Where do you want to go? ")
        if len(position) != 3:
            return False
        level  = position[0]
        row    = position[1]
        column = position[2]
        return self.__grid.move(level, row, column, self.__player)
