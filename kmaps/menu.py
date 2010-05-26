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
                cout(open("LICENSE").read())
            elif int(choice) == 5:
                inmenu = False
            else:
                out("Invalid menu choice.", True)
                print
        return True
    
    def showmenu(self):
        cout("1. Player v. Computer")
        cout("2. Player v. Player"  )
        cout("3. Instruction"       )
        cout("4. License"           )
        cout("5. Quit"              )
        cout("---------------------")
        return cin("Select a choice: ")
    
    def play(self, multiplayer = False):
        newgame = game.Game(multiplayer)
        newgame.play()
        winner = newgame.winner()
        cout(winner+" is the winner!")
        cout("")
    
    def instructions(self):
         print "K-maps is a logic game developed long ago by teachers at Staten Island"
         print "Technical High School. It is a three dimensional spin on Tic-Tac-Toe, but"
         print "much harder. Instead of Xs and Os, the players are represented by 1s and"
         print "0s in honor of the base 2 number system used in electronics. K-maps"
         print "actually stands for Karnaugh maps, which are four-by-four grids used to"
         print "simplify boolean algebra problems."
         print
         print "Each game has two four-by-four grids. The game is three-dimensional, and in"
         print "the game those two grids are theoretically on top of each other, with the"
         print "corresponding squares lining up. Literally imagine taking the first"
         print "four-by-four grid and stacking it on top of the other one. Furthermore, each"
         print "grid has no real borders: the right-most square in a row is technically"
         print "adjacent to the left-most square in the same row, and the same goes for top"
         print "and bottom. So in other words, moving off the edge of the grid just lands"
         print "you on the other side."
         print
         print "The goal of the game is to get as many quads as possible. A quad is any four"
         print "boxes that are adjacent to each other, where each box in the quad must be"
         print "adjacent to two other boxes in the quad. For example, a two-by-two square of"
         print "boxes is a quad because each box is next to two other boxes. An entire row"
         print "or column of boxes is also considered a quad for the same reason (remember"
         print "that the two edges of the row or column are really next to each other since"
         print "the grids have no borders). Also keep in mind that the game is three-dimensional,"
         print "so if two adjacent boxes are on top of another two adjacent boxes in the other"
         print "grid, that is also considered a quad. But always remember that each block must"
         print "be touching two other blocks at all times."
         print
         print "Then there is the octet. An octect is similar to a quad, except this time each"
         print "box must be adjacent to three other boxes in the octect. An easier way to think"
         print "about an octet is two quads next to each other (or on top of each other),"
         print "because any time two quads are put next to each other an octect is formed. So an"
         print "example of an octet would be getting two entire rows of boxes right next to each"
         print "other. An octet means an automatic win for whoever gets it, so be careful."
         print
         print "In this electronic version of the game, begin playing by selecting either Player"
         print "v. Computer or Player v. Player back on the menu. For each turn, it asks you"
         print "where you want to go. Simply type a three digit number as your move, where the"
         print "first number is the grid (1 or 2), the second is the row (1, 2, 3, or 4) and the"
         print "third is the column (also 1, 2, 3, or 4). Don't worry, the script will catch"
         print "invalid moves."
         print
         print
