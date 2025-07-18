from _utilities import clear
from _utilities import printHelp
from _player import Player
from _dale import dale
from YUA_NI4_Adventures import adventures

canopyLayout = """
Planet: YUA_NI4
Current zone: Canopy
~~~~~~~~~~~~~~~~~~~         ^
|     [{A}] [{B}]               N
| [{C}] [{D}]                <W + E>
| [{E}]     [{F}]               S
~~~~~~~~~~~~~~~~~~~         V
L = Landing Site
X = Current Location
? = Not yet explored
"""
mireLayout = """
Planet: YUA_NI4
Current zone: Mire
~~~~~~~~~~~~~~~~~~~       ^
| [{A}] [{B}] [{C}]             N
| [{D}] [{E}] [{F}]          <W + E>
| [{G}] [{H}] [{I}]             S  
~~~~~~~~~~~~~~~~~~~       V
L = Landing Site
X = Current Location
? = Not yet explored
"""

worldMap = {(1,2,1): 'L', (2,2,1): '?',
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

visitDict = {(1,2,1): adventures.vc_12, (2,2,1): adventures.vc_22, 
               (0,1,1): adventures.vc_01, (1,1,1): adventures.vc_11,            
               (0,0,1): adventures.vc_00, (2,0,1): adventures.vc_20,
               (0,2,0): adventures.vm_02, (1,2,0): adventures.vm_12, (2,2,0): adventures.vm_22, 
               (0,1,0): adventures.vm_01, (1,1,0): adventures.vm_11, (2,1,0): adventures.vm_21,
               (0,0,0): adventures.vm_00, (1,0,0): adventures.vm_10, (2,0,0): adventures.vm_20}

exploreDict = {(1,2,1): adventures.exc_12, (2,2,1): adventures.exc_22, 
               (0,1,1): adventures.exc_01, (1,1,1): adventures.exc_11,            
               (0,0,1): adventures.exc_00, (2,0,1): adventures.exc_20,
               (0,2,0): adventures.exm_02, (1,2,0): adventures.exm_12, (2,2,0): adventures.exm_22, 
               (0,1,0): adventures.exm_01, (1,1,0): adventures.exm_11, (2,1,0): adventures.exm_21,
               (0,0,0): adventures.exm_00, (1,0,0): adventures.exm_10, (2,0,0): adventures.exm_20}

# Explore the planet YUA-NI4
def explore():

    # Clear the screen, give the Intro
    clear()
    #adventures.planetIntro() COMMENTED OUT FOR FASTER TESTING

    # Set the stage
    player = Player( 1, 2, 1, "YUA_NI4")
    print(maps[1]())
    input("<Enter to Continue>")
    adventures.vc_12(player)
    player.visited.append((player.x, player.y, player.z))

    # A dictionary of available move actions of the player
    playerMove = {"NORTH": player.travelN, "EAST": player.travelE, 
                    "SOUTH": player.travelS, "WEST": player.travelW}

    # Begin game loop
    cont = True
    while cont:

        choice = input("What would you like to do? ").upper()

        # Parse input from the player
        if playerMove.get(choice):

            action = playerMove[choice]
            action(worldMap)

            if (player.x, player.y, player.z) not in player.visited:
                player.visited.append((player.x, player.y, player.z))
                visit = visitDict[(player.x, player.y, player.z)]
                cont = visit(player)

        elif choice == "DALE":
            dale(player, maps[player.z]())

        elif choice == "HELP":
            printHelp()

        # TEMPORARY USED FOR TESTING
        elif choice == "MAP":
            print(maps[player.z]())
            print("")
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        elif choice == "EXPLORE":
            
            # Append the zone in the player's eplored area.
            # Explore the current area
            if (player.x, player.y, player.z) not in player.explored:

                #player.explored.append((player.x, player.y, player.z))

                worldMap[(player.x, player.y, player.z)] = ' '
                explore = exploreDict[(player.x, player.y, player.z)]
                cont = explore(player)

                # Update the map to accomodate for any movement the player may have had during the adventure
                # Append Explored to player.explored (if necessary)

                worldMap[(player.x, player.y, player.z)] = 'X'

            else:
                print("Area already explored\n")

        elif choice == "QUIT":

            return 

# Used for quick testing purposes
explore()