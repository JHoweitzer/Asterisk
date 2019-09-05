# DALE is a useful tool for the player to get additional information 
# on their status and the world around them
def dale(player, curMap):

    text = input("Hey bud! How can I help? ")
    while text != "EXIT" and text != "NO":

        if text == "MAP":
            print(curMap)

        text = input("All right! Anything else? ")

    print("\nAll right! See ya later!")    