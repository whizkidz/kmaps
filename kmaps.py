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

import cgi, cgitb
import kmaps.common
from kmaps.menu import *

cgitb.enable()

print "<program>  Copyright (C) <year>  <name of author>"
print "This program comes with ABSOLUTELY NO WARRANTY; for details run with -w."
print "This is free software, and you are welcome to redistribute it"
print "under certain conditions; select License in the menu for details."

# Start of script
try:
    kmaps.common.KMAPS_NS = "terminal"
    if __name__ == "__main__":
        menu = Menu()
        menu.execute()
except KeyboardInterrupt:
    print
