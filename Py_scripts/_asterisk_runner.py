import os
from _utilities import clear

import planet_selector
import YUA_NI4
import J4U_R3N

# A List of all the possible planets in the current iteration of the game.
GAME_Planets = {"YUA-NI4": YUA_NI4.explore, "J4U-R3N": J4U_R3N.explore}
logo = r"""
     _    ____ _____ _____ ____  ___ ____  _  __
    / \  / ___|_   _| ____|  _ \|_ _/ ___|| |/ /
   / _ \ \___ \ | | |  _| | |_) || |\___ \| ' / 
  / ___ \ ___) || | | |___|  _ < | | ___) | . \ 
 /_/   \_\____/ |_| |_____|_| \_\___|____/|_|\_\

"""

welcomeMessage = """
You are floating in a small metal pod in deep space.
Soon, you'll be landing on a planet.
You will explore. Learn. Your fate, ulitmately, is uncertain.
You are alone. Except for DALE.
"""

# Welcome the player to the game
clear()
print(logo)
input("<Enter to Continue>")
clear()
print(welcomeMessage)
input("<Enter to Continue>")

# Detect if the player has run the game before. 
# If not, create a save file folder and run the tutorial

if os.path.exists("../Save_Files"):
    # Returning player! Go to planet selection and game
    pass
else:
    # NEW PLAYER! Run the intro and tutorial!
    try:
        os.mkdir("../Save_Files")
        #Initial planets available to the first-time player:
        with open("../Save_Files/Planets.txt", 'w') as planetFile:
            planetFile.write("YUA-NI4:\tA verdant, marshy planet.\n")
            # ADDITIONAL PLANETS
            # ADDITIONAL PLANETS
        with open("../Save_Files/Memories.txt", 'w') as memoryFile:
            memoryFile.write("Memories:\n")
            memoryFile.write("001: You remember a bright light\n")
    except OSError:
        print("Save File initialization failed. Please \"reinstall\" the game ( sorry I'm bad programmer :< )")
        exit
    else:
        pass

# The player then selects a planet available to them, based on their progress in the game.
clear()
explore = GAME_Planets.get(planet_selector.run())
explore()

# FOR TESTING PURPOSES - UNLOCK A NEW PLANET
#print("You have unlocked a new planet")
#with open("../Save_Files/Planets.txt", 'a') as planetFile:
#    planetFile.write("J4U-R3N:\tA dense, mountanous planet wracked with storms\n")