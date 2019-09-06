# DALE is a useful tool for the player to get additional information 
# on their status and the world around them
playerStatusHeader = """
Current Status:
~~~~~~~~~~~~~~~~~~~"""

playerStatusFooter = """~~~~~~~~~~~~~~~~~~~"""
def printStatus(player):
    print(playerStatusHeader)
    print("| Status: " + player.status)
    print("| Injuries: ")
    for injury in player.injuries:
        print("| \t"+ injury)
    print(playerStatusFooter)

def dale(player, curMap):

    text = input("\nHey bud! How can I help? ")
    while text != "EXIT" and text != "NO":

        if text == "MAP":
            print(curMap)
        elif text == "STATUS":
            printStatus(player)
#        elif text == "INVENTORY":
#            printInventory(player)
        else:
            print("Uhhh... wut? ")

        text = input("All right! Anything else? ")

    print("\nAll right! See ya later!")    