from utl import clear

startMessage = """
Welcome.

You are floating in a small metal pod in deep space.
Soon, you'll be landing on a planet.
The planet is lush, alive, and dangerous.
You are alone. Except for DALE.
"""
commandsMessage = """
To navigate the planet, enter cardinal directions (NORTH, SOUTH, EAST, WEST) when prompted.
To learn more about your status, enter STATUS
To consult your Digital-Arm-Linked-Escort, enter DALE
To explore an area, enter EXPLORE

To review these commands, enter HELP
"""

def run():
    print(startMessage)
    input("<Enter to Continue>")
    print(commandsMessage)
    input("<Enter to Continue>")
    clear()