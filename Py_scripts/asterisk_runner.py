import os
from utilities import clear
import tutorial


# Welcome the player to the game
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
    try:
        os.mkdir("../Save_Files")
        #Initial planets available to the first-time player:
        with open("../Save_Files/Planets.txt", 'w') as planets:
            planets.write("Planet 1: Y0A-NI4\tA verdant, marshy planet.\n")
            #planets.write("Planet 2: J4U-R3N\tA dense, mountanous planet wracked with storms\n")
            #planets.write("Planet 3: KU5-PR1\tA frosty, desolate planet\n")
    except OSError:
        print("File initialization failed. Please \"reinstall\" the game ( sorry I'm bad programmer :< )")
    else:
        # NEW PLAYER! Run the intro and tutorial!
        tutorial.run()

