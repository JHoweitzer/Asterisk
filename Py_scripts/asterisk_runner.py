import os
import utilities
import tutorial

# Detect if the player has run the game before. 
# If not, create a save file folder and run the tutorial

if os.path.exists("../Save_Files"):
    # Returning player! Go to planet selection and game
    print("Welcome back!")
else:
    try:
        os.mkdir("../Save_Files")
    except OSError:
        print("File initialization failed. Please reinstall the game ( sorry I'm bad programmer :< )")
    else:
        # NEW PLAYER! Run the intro and tutorial!
        tutorial.run()
