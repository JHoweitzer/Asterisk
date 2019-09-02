import os
from utilities import clear
import tutorial
import planet_selector

import YUA_NI4
import J4U_R3N

# A List of all the possible planets in the current iteration of the game.
GAME_Planets = {"YUA-NI4": YUA_NI4.explore, "J4U-R3N": J4U_R3N.explore}

# Welcome the player to the game
clear()
welcomeMessage = """
Welcome.

You are floating in a small metal pod in deep space.
Soon, you'll be landing on a planet.
You will explore. Learn. Your fate, ulitmately, is uncertain.
You are alone. Except for DALE.
"""
print(welcomeMessage)
input("<Enter to Continue>")
clear()

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
            planetFile.write("J4U-R3N:\tA dense, mountanous planet wracked with storms\n")
            #planetFile.write("Planet 3: KU5-PR1\tA frosty, desolate planet\n")
    except OSError:
        print("Save File initialization failed. Please \"reinstall\" the game ( sorry I'm bad programmer :< )")
        exit
    else:
        tutorial.run()

# The player then selects a planet available to them, based on their progress in the game.
explore = GAME_Planets.get(planet_selector.run())
explore()