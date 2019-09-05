from _utilities import clear
from _player import Player
from _dale import dale
import YUA_NI4_Adventures

# The ASCII format for this planet's map display, used by DALE
mapLayout = """
~~~~~~~~~~~~~~~~~~~
| [{A}] [{B}] [{C}] [{D}] |
| [{E}] [{F}] [{G}] [{H}] |
| [{I}] [{J}] [{K}] [{L}] |
| [{M}] [{N}] [{O}] [{P}] |
~~~~~~~~~~~~~~~~~~~
"""
# The Map Dictionary object will change over time
mapDict = {(0,0): '?', (1,0): '?', (2,0): '?', (3,0): '?', 
           (0,1): '?', (1,1): 'L', (2,1): '?', (3,1): '?',
           (0,2): '?', (1,2): '?', (2,2): '?', (3,2): '?',
           (0,3): '?', (1,3): '?', (2,3): '?', (3,3): '?'}

#mapAdventures = {(0,0): '?', (1,0): '?', (2,0): '?', (3,0): '?', 
#                 (0,1): '?', (1,1): '?', (2,1): '?', (3,1): '?',
#                 (0,2): '?', (1,2): '?', (2,2): '?', (3,2): '?',
#                 (0,3): '?', (1,3): '?', (2,3): '?', (3,3): '?'}

# Returns a formatted map based on the map dictionary as a string
def getMap():
    return(mapLayout.format(A=mapDict[(0,0)], B=mapDict[(1,0)], C=mapDict[(2,0)], D=mapDict[(3,0)],
                            E=mapDict[(0,1)], F=mapDict[(1,1)], G=mapDict[(2,1)], H=mapDict[(3,1)],
                            I=mapDict[(0,2)], J=mapDict[(1,2)], K=mapDict[(2,2)], L=mapDict[(3,2)],
                            M=mapDict[(0,3)], N=mapDict[(1,3)], O=mapDict[(2,3)], P=mapDict[(3,3)],))


# Explore the planet YUA-NI4
def explore():

    clear()
    print("Traveling to YUA_NI4 \n")

    player = Player(1,1,"YUA_NI4")
    dale(player, getMap())