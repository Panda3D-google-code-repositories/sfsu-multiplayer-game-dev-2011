'''
Created on Nov 20, 2011

@author: hunvil
'''
from common.Constants import Constants

from main.MainLobby.World.World3D.Species import Species

class Plant(Species):

    def __init__(self, plantID, name, plantType, avatarID, zoneID, biomass):

        Species.__init__(self, name, avatarID, zoneID, biomass)

        self.organism_type = Constants.ORGANISM_TYPE_PLANT

        self.plantID = plantID
        self.plantType = plantType
        self.avatarID = avatarID
        self.zoneID = zoneID
        self.biomass = biomass
        self.plantInstance = str(self.plantType) + '-' + str(self.plantID)
        self.plantModel = None
        self.noWaterCount = None
        self.noLightCount = None
        self.growRadius = None
        self.lightNeedFrequency = None
        self.zone = None
        self.type = plantType

    def getID(self):
        return self.plantID
    
    def getPlantType(self):
        return self.plantType
    
    def setNoWaterCount(self,noWaterCount):
        self.noWaterCount = noWaterCount
        if self.noWaterCount > 1:
            scalePercentage = self.noWaterCount * 10/100
            self.plantModel.setScale(self.scaleValue - scalePercentage*self.scaleValue)
            print "Plant scaled to ",self.scaleValue - scalePercentage*self.scaleValue

    def setNoLightCount(self,noLightCount):
        self.noLightCount = noLightCount
        if self.noLightCount > 1:
            scalePercentage = self.noWaterCount * 10/100
            self.plantModel.setScale(self.scaleValue - scalePercentage*self.scaleValue)
            print "Plant scaled to ",self.scaleValue - scalePercentage*self.scaleValue            

#getNoWaterCount() may not be required
    def getNoWaterCount(self):
        return self.noWaterCount

#getNoLightCount() may not be required    
    def getNoLightCount(self):
        return self.noLightCount
    
    def setPlantBiomass(self,biomass,scalePercentage):
        self.biomass = biomass
        self.plantModel.setScale(self.scaleValue + scalePercentage*self.scaleValue)
        print "Plant scaled to ",self.scaleValue + scalePercentage*self.scaleValue
        return None

    def setZone(self,zone):
        self.zone = zone
