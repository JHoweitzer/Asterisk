from memoryParser import parseMemories

class Player():

    def __init__(self, lSiteX, lSiteY, lSiteZ, newPlanet):
        self.x = lSiteX
        self.y = lSiteY
        self.z = lSiteZ
        self.planet = newPlanet
        self.memories = parseMemories()
        self.status = "HEALTHY"
        self.injuries = []
        self.inventory = ["DALE", "Blaster"]
        self.explored = []


    def updateUnexplored(self, pDict):
        if (self.x, self.y, self.z) not in self.explored:
            if pDict[(self.x, self.y, self.z)] != 'L':
                pDict[(self.x, self.y, self.z)] = '?'
        else:
            if pDict[(self.x, self.y, self.z)] != 'L':
                pDict[(self.x, self.y, self.z)] = ' '
    
    def updateCurLocation(self, pDict):
        if pDict[(self.x, self.y, self.z)] != 'L':
            pDict[(self.x, self.y, self.z)] = 'X'
    
    def travelN(self, pDict):
        if (self.x, self.y + 1, self.z) in pDict:
            self.updateUnexplored(pDict)
            self.y = self.y + 1
            self.updateCurLocation(pDict)
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")

    def travelS(self, pDict):
        if (self.x, self.y - 1, self.z) in pDict:
            self.updateUnexplored(pDict)
            self.y = self.y - 1
            self.updateCurLocation(pDict)
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")

    def travelE(self, pDict):
        if (self.x + 1, self.y, self.z) in pDict:
            self.updateUnexplored(pDict)
            self.x = self.x + 1
            self.updateCurLocation(pDict)
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")

    
    def travelW(self, pDict):
        if (self.x - 1, self.y, self.z) in pDict:
            self.updateUnexplored(pDict)
            self.x = self.x - 1
            self.updateCurLocation(pDict)
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")
