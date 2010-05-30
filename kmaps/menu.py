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
                cout(open("README").read())
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
