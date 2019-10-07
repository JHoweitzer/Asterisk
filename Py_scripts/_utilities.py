import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def printHelp():
    print("""
To navigate the planet, enter a cardinal direction, ex: NORTH, when prompted.
To consult your Digital-Arm-Linked-Escort, enter DALE.
To explore an area, enter EXPLORE.
Other commands will be available, depending on your situation.

To review these commands, enter HELP
""")

def filterInput(playerInput, *argv, confirmationMessage):
    """
    Searches a given input for one of many possible "interpretations", 
    returns true if found and validated by player.

    If confirmation message is not NONE, the player will be prompted to
    authenticate their decision.
    """
    for arg in argv:
        if arg in playerInput:
            if (confirmationMessage == "NONE"):
                return True
            approve = input(confirmationMessage + " Y/N: ").upper()
            return (approve == "Y")
    return False