import game

class Menu:
    """Base class for the game. Shows the menu."""
    
    def execute(self, previous = False):
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
    
    def play(self, multiplayer = False):
        newgame = game.Game(multiplayer)
        newgame.play()
        winner = newgame.winner()
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
