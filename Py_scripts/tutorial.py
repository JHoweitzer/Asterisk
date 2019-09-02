from utilities import clear

commandsMessage = """
To navigate the planet, enter cardinal directions (NORTH, SOUTH, EAST, WEST) when prompted.
To learn more about your status, enter STATUS
To consult your Digital-Arm-Linked-Escort, enter DALE
To explore an area, enter EXPLORE

To review these commands, enter HELP
"""

def run():
    print(commandsMessage)
    input("<Enter to Continue>")
    clear()