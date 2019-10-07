# DALE is a useful tool for the player to get additional information 
# on their status and the world around them
header = """~~~~~~~~~~~~~~~~~~~"""

footer = """~~~~~~~~~~~~~~~~~~~"""

def printStatus(player):
    print(header)
    print("| Status: " + player.status)
    print("| Injuries: ")
    for injury in player.injuries:
        print("|\t"+ injury)
    print(footer)

def printInventory(player):
    print(header)
    print("| Current Inventory: ")
    for item in player.inventory:
        print("|\t"+ item)
    print(footer)


def dale(player, curMap):

    text = input("\nHey bud! How can I help? ").upper()
    while text != "EXIT" and text != "NO":

        if text == "MAP":
            print(curMap)
        elif text == "STATUS":
            printStatus(player)
        elif text == "INVENTORY":
            printInventory(player)
        else:
            print("Uhhh... wut? ")

        text = input("All right! Anything else? ")

    print("\nAll right! See ya later!")