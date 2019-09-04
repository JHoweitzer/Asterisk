# Based on the player's progress, allow them to select a planet. 
# Returns a valid planet name.
def run():
    PlanetsList = []
    with open("../Save_Files/Planets.txt", 'r') as planetFile:
        print("The following planets are within your pod's range:")
        for planet in planetFile.readlines():
            print(planet)
            PlanetsList.append(planet.split(':')[0])

    cont = False
    while not cont:
        selectedPlanet = input("Enter your selected planet: ")
        if PlanetsList.__contains__(selectedPlanet):
            return selectedPlanet
        else:
            print("Invalid planet entry \n")
