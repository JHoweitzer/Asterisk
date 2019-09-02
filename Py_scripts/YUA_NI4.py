from utilities import clear

def explore():
    clear()
    print("Traveling to YUA_NI4 \n")
    
    # FOR TESTING PURPOSES - UNLOCK A NEW PLANET
    print("You have unlocked a new planet")
    with open("../Save_Files/Planets.txt", 'a') as planetFile:
        planetFile.write("J4U-R3N:\tA dense, mountanous planet wracked with storms\n")