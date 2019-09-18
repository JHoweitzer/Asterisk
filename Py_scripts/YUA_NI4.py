from _utilities import clear
from _player import Player
from _dale import dale
from YUA_NI4_Adventures import *

canopyLayout = """
Planet: YUA_NI4
Current zone: Canopy
~~~~~~~~~~~~~~~~~~~
|     [A] [B] [C] 
| [D] [E] [F] [G] 
|     [H]     [I] 
| [J] [K]     [L] 
~~~~~~~~~~~~~~~~~~~
L = Landing Site
X = Current Location
? = Not yet explored
"""

mireLayout = """
Planet: YUA_NI4
Current zone: Mire
~~~~~~~~~~~~~~~~~~~
| [{A}] [{B}] [{C}] [{D}] 
| [{E}] [{F}] [{G}] [{H}] 
| [{I}] [{J}] [{K}] [{L}] 
| [{M}] [{N}] [{O}] [{P}] 
~~~~~~~~~~~~~~~~~~~
L = Landing Site
X = Current Location
? = Not yet explored
"""

# The Map Dictionary object will change over time
mapDict = {(0,3): '?', (1,3): '?', (2,3): '?', (3,3): '?', 
           (0,2): '?', (1,2): '?', (2,2): '?', (3,2): '?',
           (0,1): '?', (1,1): '?', (2,1): '?', (3,1): '?',
           (0,0): '?', (1,0): '?', (2,0): '?', (3,0): '?'}

exploreDict = {(0,0): ex_00, (1,0): ex_10, (2,0): ex_20, (3,0): ex_30, 
               (0,1): ex_01, (1,1): ex_11, (2,1): ex_21, (3,1): ex_31,
               (0,2): ex_02, (1,2): ex_12, (2,2): ex_22, (3,2): ex_32,
               (0,3): ex_03, (1,3): ex_13, (2,3): ex_23, (3,3): ex_33}

# Returns a formatted map based on the map dictionary as a string
def getMap():
    return(mireLayout.format(A=mapDict[(0,3)], B=mapDict[(1,3)], C=mapDict[(2,3)], D=mapDict[(3,3)],
                             E=mapDict[(0,2)], F=mapDict[(1,2)], G=mapDict[(2,2)], H=mapDict[(3,2)],
                             I=mapDict[(0,1)], J=mapDict[(1,1)], K=mapDict[(2,1)], L=mapDict[(3,1)],
                             M=mapDict[(0,0)], N=mapDict[(1,0)], O=mapDict[(2,0)], P=mapDict[(3,0)],))

# Explore the planet YUA-NI4
def explore():

    # Clear the screen, give the Intro
    clear()
    planetIntro()

    # Set the stage
    lSiteX = 2
    lSiteY = 2
    player = Player( lSiteX, lSiteY, "YUA_NI4")
    player.zone = "Canopy"
    mapDict[(lSiteX, lSiteY)] = 'L'

    playerMove = {"NORTH": player.travelN, "EAST": player.travelE, 
                    "SOUTH": player.travelS, "WEST": player.travelW}

    # Begin game loop
    cont = True
    text = input("What would you like to do? ")
    while cont and text != "QUIT":
        if playerMove.get(text):
            action = playerMove[text]
            action(mapDict)
        elif text == "DALE":
            dale(player, getMap())
        elif text == "HELP":
            printHelp()
        elif text == "EXPLORE":
            explore = exploreDict[(player.x, player.y)]
            cont = explore(player)
        
        # JANKY FIX. REFACTOR LOOP SOMEHOW
        if cont:
            text = input("\nWhat would you like to do? ")

