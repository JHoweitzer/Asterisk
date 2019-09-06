from _utilities import *
from _player import Player
from _dale import dale
import YUA_NI4_Adventures

# The ASCII format for this planet's map display, used by DALE
mapLayout = """
Planet: YUA_NI4
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

#mapAdventures = {(0,0): '?', (1,0): '?', (2,0): '?', (3,0): '?', 
#                 (0,1): '?', (1,1): '?', (2,1): '?', (3,1): '?',
#                 (0,2): '?', (1,2): '?', (2,2): '?', (3,2): '?',
#                 (0,3): '?', (1,3): '?', (2,3): '?', (3,3): '?'}

# Returns a formatted map based on the map dictionary as a string
def getMap():
    return(mapLayout.format(A=mapDict[(0,3)], B=mapDict[(1,3)], C=mapDict[(2,3)], D=mapDict[(3,3)],
                            E=mapDict[(0,2)], F=mapDict[(1,2)], G=mapDict[(2,2)], H=mapDict[(3,2)],
                            I=mapDict[(0,1)], J=mapDict[(1,1)], K=mapDict[(2,1)], L=mapDict[(3,1)],
                            M=mapDict[(0,0)], N=mapDict[(1,0)], O=mapDict[(2,0)], P=mapDict[(3,0)],))

# Explore the planet YUA-NI4
def explore():

    # Clear the screen, give the Intro
    clear()
    print("Traveling to YUA_NI4 \n")

    # Set the stage
    lSiteX = 2
    lSiteY = 2
    player = Player( lSiteX, lSiteY,"YUA_NI4")
    mapDict[(lSiteX, lSiteY)] = 'L'
    playerMove = {"NORTH": player.travelN, "EAST": player.travelE, 
                    "SOUTH": player.travelS, "WEST": player.travelW}

    # Begin game loop
    text = input("What would you like to do? ")
    while text != "QUIT":
        if playerMove.get(text):
            action = playerMove[text]
            action(mapDict)
        elif text == "DALE":
            dale(player, getMap())
        elif text == "HELP":
            printHelp()
        elif text == "EXPLORE":
            pass
        else:
            pass

        text = input("\nWhat would you like to do? ")