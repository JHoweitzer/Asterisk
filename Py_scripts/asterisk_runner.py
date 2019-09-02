import os
import tutorial

if os.path.exists("../Save_Files"):
    # Returning player! Go to planet selection and game
    print("Welcome back!")
    # os.rmdir("../Save_Files") -- Used for testing purposes
else:
    try:
        os.mkdir("../Save_Files")
    except OSError:
        print("File initialization failed. Please reinstall the game ( sorry I'm bad programmer :< )")
    else:
        # NEW PLAYER! Run the intro and tutorial!
        tutorial.runTutorial()