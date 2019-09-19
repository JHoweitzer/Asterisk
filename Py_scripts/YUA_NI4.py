from _utilities import clear
from _player import Player
from _dale import dale
from YUA_NI4_Adventures import *

canopyLayout = """
Planet: YUA_NI4
Current zone: Canopy
~~~~~~~~~~~~~~~~~~~
|     [{A}] [{B}]     
| [{C}] [{D}] 
| [{E}]     [{F}]      
~~~~~~~~~~~~~~~~~~~
L = Landing Site
X = Current Location
? = Not yet explored
"""
mireLayout = """
Planet: YUA_NI4
Current zone: Mire
~~~~~~~~~~~~~~~~~~~
| [{A}] [{B}] [{C}]
| [{D}] [{E}] [{F}] 
| [{G}] [{H}] [{I}]  
~~~~~~~~~~~~~~~~~~~
L = Landing Site
X = Current Location
? = Not yet explored
"""

worldMap = {(1,2,1): '?', (2,2,1): '?',
            (0,1,1): '?', (1,1,1): '?',
            (0,0,1): '?', (2,0,1): '?',
            (0,2,0): '?', (1,2,0): '?', (2,2,0): '?', 
            (0,1,0): '?', (1,1,0): '?', (2,1,0): '?',
            (0,0,0): '?', (1,0,0): '?', (2,0,0): '?'}

def getCanMap():
    return(canopyLayout.format(A=worldMap[(1,2,1)], B=worldMap[(2,2,1)],
                               C=worldMap[(0,1,1)], D=worldMap[(1,1,1)],
                               E=worldMap[(0,0,1)], F=worldMap[(2,0,1)]))

# Returns a formatted map based on the map dictionary as a string
def getMireMap():
    return(mireLayout.format(A=worldMap[(0,2,0)], B=worldMap[(1,2,0)], C=worldMap[(2,2,0)],
                             D=worldMap[(0,1,0)], E=worldMap[(1,1,0)], F=worldMap[(2,1,0)],
                             G=worldMap[(0,0,0)], H=worldMap[(1,0,0)], I=worldMap[(2,0,0)]))

maps = {1: getCanMap, 0: getMireMap}

exploreDict = {(1,2,1): exc_12, (2,2,1): exc_22, 
               (0,1,1): exc_01, (1,1,1): exc_11,            
               (0,0,1): exc_00, (2,0,1): exc_20,
               (0,2,0): exm_02, (1,2,0): exm_12, (2,2,0): exm_22, 
               (0,1,0): exm_01, (1,1,0): exm_11, (2,1,0): exm_21,
               (0,0,0): exm_00, (1,0,0): exm_10, (2,0,0): exm_20}


# Explore the planet YUA-NI4
def explore():

    # Clear the screen, give the Intro
    clear()
    planetIntro()

    # Set the stage
    lSiteX = 1
    lSiteY = 2
    lSiteZ = 1
    player = Player( lSiteX, lSiteY, lSiteZ, "YUA_NI4")
    worldMap[(lSiteX, lSiteY, lSiteZ)] = 'L'

    # A dictionary of available move actions of the player
    playerMove = {"NORTH": player.travelN, "EAST": player.travelE, 
                    "SOUTH": player.travelS, "WEST": player.travelW}

    # Begin game loop
    cont = True
    text = input("What would you like to do? ")
    while cont and text != "QUIT":

        # Parse input from the player
        if playerMove.get(text):
            action = playerMove[text]
            action(worldMap)
        elif text == "DALE":
            dale(player, maps[player.z]())
        elif text == "HELP":
            printHelp()

        # TEMPORARY USED FOR TESTING
        elif text == "MAP":
            print(maps[player.z]())
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        elif text == "EXPLORE":
            
            if (player.x, player.y, player.z) not in player.explored:
                player.explored.append((player.x, player.y, player.z))
                worldMap[(player.x, player.y, player.z)] = ' '
            
            # Explore the current area
            explore = exploreDict[(player.x, player.y, player.z)]
            cont = explore(player)

            # Update the map to accomodate for any movement the player may have had during the adventure
            worldMap[(player.x, player.y, player.z)] = 'X'
        
        # JANKY FIX. REFACTOR LOOP SOMEHOW
        if cont:
            text = input("\nWhat would you like to do? ")

explore()