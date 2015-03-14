'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants

class Species():
    def __init__(self,avatarID, zoneID, biomass):
        if Constants.DEBUG:
            print "Calling Parent Species Object"        
        self.avatarID = avatarID
        self.zoneID   = zoneID
        self.biomass  = biomass
        
    #to be called if server confirms the server has changed zoneID
    def setZoneID(self,newZoneID):
        self.zoneID = newZoneID
        
    def getZoneID(self):
        return self.zoneID
    
    #to be called when you set new Owner for the animal
    def setAvatarID(self,newOwner):
        self.avatarID = newOwner
        
    def getAvatarID(self):
        return self.avatarID
    
    #depending upon the new biomass 3D rendering has to be changed.
    #animal should look healthy,thin,medium,set the scale values accordingly
    def setBiomass(self,newBiomass):
        self.biomass = newBiomass

    def getBiomass(self):
        return self.biomass