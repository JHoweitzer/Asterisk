class Player():

    def __init__(self, lSiteX, lSiteY, newPlanet):
        self.x = lSiteX
        self.y = lSiteY
        self.planet = newPlanet
        self.status = "HEALTHY"
        self.injuries = ["Mild Headache", "Mild Nausea"]
        self.inventory = []
    
    def travelN(self, pDict):
        if (self.x, self.y + 1) in pDict:
            if (pDict[(self.x, self.y)] != 'L'):
                pDict[(self.x, self.y)] = ' '
            self.y = self.y + 1
            pDict[(self.x, self.y)] = 'X'
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")

    def travelS(self, pDict):
        if (self.x, self.y - 1) in pDict:
            if (pDict[(self.x, self.y)] != 'L'):
                pDict[(self.x, self.y)] = ' '
            self.y = self.y - 1
            pDict[(self.x, self.y)] = 'X'
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")

    def travelE(self, pDict):
        if (self.x + 1, self.y) in pDict:
            if (pDict[(self.x, self.y)] != 'L'):
                pDict[(self.x, self.y)] = ' '
            self.x = self.x + 1
            pDict[(self.x, self.y)] = 'X'
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")

    
    def travelW(self, pDict):
        if (self.x - 1, self.y) in pDict:
            if (pDict[(self.x, self.y)] != 'L'):
                pDict[(self.x, self.y)] = ' '
            self.x = self.x - 1
            pDict[(self.x, self.y)] = 'X'
        else:
            print("ERROR. CANNOT TRAVEL IN THAT DIRECTION")
