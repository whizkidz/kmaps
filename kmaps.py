import sys,getopt
from kmaps.menu import *

# Start of script
try:
    menu = Menu()
    menu.execute()
except KeyboardInterrupt:
    print
