'''
Created on Nov 21, 2011

@author: hunvil
'''
from common.Constants import Constants
class Avatar():
    def __init__(self,avatarID,cash,abilityPoints):
        if Constants.DEBUG:
            print 'Creating Avatar'
        self.avatarID = avatarID
        self.cash = cash
        self.abilityPoints = abilityPoints
        self.envScore = None
        self.avatarType = None
        self.worldType = 1  #1 = PvP, 0 = PvE
        self.charName = main.charName
        #2D needs list of all zones, speciesName, speciesCount, biomass
        # eg : self.listOfZone0[speciesName = 'elephant'] = {speciesCount = 20, biomass = 40}
        #self.listOdZone0[speciesName = 'giraffe'] = {speciesCount = 5,biomass = 30}
        self.listOfZone0 = {}    
        self.listOfZone1 = {}
        self.listOfZone2 = {}
        self.listOfZone3 = {}
        self.listOfZone4 = {}
        self.listOfZone5 = {}
        self.listOfZone6 = {}
        self.listOfZone7 = {}
        self.listOfZone8 = {}
        
    def updateAvatarType(self,avatarType):
        self.avatarType = avatarType
            
    def updateCash(self,cash):
        self.cash = cash
        
    def updateAbilityPoints(self,abilityPoints):
        self.abilityPoints = abilityPoints
        
    def updateEnvScore(self,envScore):
        self.envScore = envScore
        
    def getWorldType(self):
        return self.worldType