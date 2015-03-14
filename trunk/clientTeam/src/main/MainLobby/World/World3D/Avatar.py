'''
Created on Nov 21, 2011

@author: hunvil
'''
from common.Constants import Constants
class Avatar():
    def __init__(self):
        if Constants.DEBUG:
            print 'Creating Avatar'
        self.gold = None
        self.XP = None
        self.level = None
        self.avatarType = None
        self.worldType = 1  #1 = PvP, 0 = PvE
        self.charName = main.charName
        #2D needs list of all zones, speciesName, speciesCount, biomass
        # eg : self.listOfZone0[speciesName = 'elephant'] = {speciesCount = 20, biomass = 40}
        #self.listOdZone0[speciesName = 'giraffe'] = {speciesCount = 5,biomass = 30}
        self.listOfZones = []
        
    def updateAvatarType(self,avatarType):
        self.avatarType = avatarType
 
    def getAvatarType(self):
        return self.avatarType

    def updateGold(self,gold):
        self.gold = gold
 
    def getGold(self):
        return self.gold
               
    def updateXP(self,xp):
        self.XP = xp

    def getXP(self):
        return self.XP
    
    def updateLevel(self,level):
        self.level = level

    def getLevel(self):
        return self.level    
          
    def getWorldType(self):
        return self.worldType
    
 
    
