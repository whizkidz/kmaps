# Important instructions for developers:
# In order to use this script as a Kmaps API, do the
# following:
# 1) Always use the -n option when running the script
# 2) Give the script the -m option if multiplayer, and
#    use -c0 and -c1 to indicate the player whose turn it is.
# 3) Give the script the current grid using STDIN. If just
#    starting a game, copy the blank grid definition from the
#    Grid class.
# 3) The script will give back a string with the updated
#    grid. Use the STDOUT grid in the STDIN for the next turn.

import sys,getopt

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
    
#    def __init__(self, previous=False):
#        if previous:
#            self.grid = previous
    
    def __getattr__(self, key):
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
            return self.grid[level][row][column]       
    
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
    
    def printtable(self, readable = True):
        if not readable:
            print a.grid
        
        a = self
        print "-----------------"
        print "| "+str(a.g111)+" | "+str(a.g112)+" | "+str(a.g113)+" | "+str(a.g114)+" |"
        print "-----------------"
        print "| "+str(a.g121)+" | "+str(a.g122)+" | "+str(a.g123)+" | "+str(a.g124)+" |"
        print "-----------------"
        print "| "+str(a.g131)+" | "+str(a.g132)+" | "+str(a.g133)+" | "+str(a.g134)+" |"
        print "-----------------"
        print "| "+str(a.g141)+" | "+str(a.g142)+" | "+str(a.g143)+" | "+str(a.g144)+" |"
        print "-----------------"
        print ""
        print ""
        print "-----------------"
        print "| "+str(a.g211)+" | "+str(a.g212)+" | "+str(a.g213)+" | "+str(a.g214)+" |"
        print "-----------------"
        print "| "+str(a.g221)+" | "+str(a.g222)+" | "+str(a.g223)+" | "+str(a.g224)+" |"
        print "-----------------"
        print "| "+str(a.g231)+" | "+str(a.g232)+" | "+str(a.g233)+" | "+str(a.g234)+" |"
        print "-----------------"
        print "| "+str(a.g241)+" | "+str(a.g242)+" | "+str(a.g243)+" | "+str(a.g244)+" |"
        print "-----------------"

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
        scores = []
        
        # Create other strategy detections
        s1 = [u, l, r]
        s2 = [r, rr, ur]
        s3 = [l, rr, ul]
        s4 = [d, dl, dr]
        s5 = [d, l, r]
        s6 = [r, rr, dr]
        s7 = [l, rr, dl]
        s8 = [u, ul, ur]
        
        moves  = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, s1, s2, s3, s4]
        
        # Calculate the individual scores
        otherplayer = (player - 1) % 2
        for q in moves:
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

class Game:
    grid = 0
    __players = [0,1]
    
    def __init__(self, multiplayer=False, previous=False):
        self.grid = Grid()
        self.__players[0] = Human(self.grid, 0)
        if not multiplayer:
            self.__players[1] = Computer(self.grid, 1)
        else:
            self.__players[1] = Human(self.grid, 1)
    
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
                print "Invalid move."
        return True
    
    def turn(self, player, move):
        status = self.__players[int(player)].move()
        if not status:
            return False
     
    def winner(self):
        # Use grid to determine winner.
        return 0
    
class Menu:
    """Base class for the game. Shows the menu."""
    
    def execute(self, previous = False):
        if not previous == False:
            multiplayer = previous[0]
            return self.play(multiplayer, previous[1:])
        inmenu = True
        while inmenu:
            choice = self.showmenu()
            if int(choice) == 1:
                self.play(False)
            elif int(choice) == 2:
                self.play(True)
            elif int(choice) == 3:
                self.instructions()
            elif int(choice) == 4:
                inmenu = False
            else:
                print "Invalid menu choice."
                print
        return True
    
    def showmenu(self):
        print "1. Player v. Computer"
        print "2. Player v. Player"
        print "3. Instruction"
        print "4. Quit"
        print "---------------------"
        return raw_input("Select a choice: ")
    
    def play(self, multiplayer = False, previous = False):
        if not previous == False:
            game = Game(multiplayer, previous[4:])
            game.turn(previous[0], previous[1:4])
            game.grid.printtable()
        else:
            game = Game(multiplayer, False)
            game.play()
            winner = game.winner()
            print winner+" is the winner!"
            print
    
    def instructions(self):
        print "Kmaps is a logic game developed long ago by teachers"
        print "at Staten Island Technical High School. It is a 3D spin"
        print "on Tic-Tac-Toe, and much harder. Instead of Xs and Os,"
        print "the players are represented by 1s and 0s."
        print
        print "Each game has two four-by-four grids. The game is three-"
        print "dimensional, so when playing, imagine that the two grids"
        print "are actually on top of each other, with the corresponding"
        print "squares lining up. Furthermore, each grid has no real border:"
        print "the right-most square in a row is theoretically adjacent to"
        print "the left-most square in the same row, and the same goes for"
        print "top and bottom."
        print
        print "The goal of the game is to get as many quads as possible."
        print "A quad is any two-by-two block or an entire row or column"
        print "of four squares with your player symbol in it. Keep in mind"
        print "that the game is three-dimensional, so two adjacent squares"
        print "on top of another two adjacent squares in the other grid is"
        print "also considered a quad. Finally, remember the grid has no"
        print "borders, so having two left-most adjacent squares and two"
        print "right-most adjacent squares in the same rows is a quad. As an"
        print "example, getting the four corners of any grid is a quad."
        print
        raw_input("--MORE--")
        print
        print "Then there is the octet. This is where you get two quads on"
        print "top of each other in the two different levels. An octet means"
        print "an automatic win, so be careful."
        print
        print "In this electronic version of the game, begin playing by"
        print "selecting either Player v. Computer or Player v. Player back"
        print "on the menu. For each turn, it asks you where you want to go."
        print "Simply type a three digit number as your move, where the first"
        print "number is the grid (1 or 2), the second is the row (1, 2, 3, or 4)"
        print "and the third is the column (also 1, 2, 3, or 4). Don't worry,"
        print "the script will catch invalid moves."
        raw_input("Back to menu.")
        print
        print

# Start of script
try:
#    opts, args = getopt.getopt(sys.argv[1:], 'nhmc:')
#    noninteractive = multiplayer = currplayer = False
#    previous = False
#    for o, a in opts:
#        if o == "-n":
#            previous = sys.stdin.read()
#        elif o == "-h":
#            raise getopt.GetoptError("")
#        elif o == "-m":
#            multiplayer = True
#        elif o == "-c":
#            currplayer  = a
#    previous = str(int(multiplayer)) + str(currplayer) + str(int(previous))
    previous = False
    menu = Menu()
    menu.execute(previous)
except getopt.GetoptError, err:
    print str(err)
    menu = Menu()
    menu.instructions()
except KeyboardInterrupt:
    print
