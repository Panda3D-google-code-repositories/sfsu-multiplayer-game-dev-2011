'''
Created on Nov 20, 2011

@author: hunvil
'''
from common.Constants import Constants

from main.MainLobby.World.World3D.Species import Species

class Animal(Species):

    def __init__(self, animalID, name, animalType, avatarID, zoneID, biomass):

        Species.__init__(self, name, avatarID, zoneID, biomass)

        self.organism_type = Constants.ORGANISM_TYPE_ANIMAL

        self.animalID   = animalID
        self.animalType = animalType
        self.avatarID   = avatarID
        self.zoneID     = zoneID
        self.biomass    = biomass
        self.loyalty = 0
        self.type = animalType

        self.animalInstance = str(self.animalType) + '-' + str(self.animalID)
        self.scaleValue = 0
        self.previousZ = 0
        self.zone = None
        self.object_id = animalID
        self.noWaterCount = None
        self.startPos = None
        self.boundaryRestrict = True

    def setAvatarID(self,newAvatarID):
        self.avatarID = newAvatarID

    def setZoneID(self, newZoneID):
        self.zoneID = newZoneID

    def setSoundMgr(self, soundMgr):
        self.soundMgr = soundMgr
        self.soundMgr.playSound(self.animalType, self.animalID)

    def setStartPos(self, position):
        self.startPos = position

    def getAnimalInstance(self):
        return self.animalInstance

    def getID(self):
        return self.animalID

    def getAnimalType(self):
        return self.animalType

    def setAnimalBiomass(self,biomass,scalePercentage):
        self.biomass = biomass
        self.setScale(self.scaleValue + scalePercentage*self.scaleValue)

    def setZone(self,zone):
        self.zone = zone

    def setNoWaterCount(self,noWaterCount):
        self.noWaterCount = noWaterCount
        if self.noWaterCount > 1:
            scalePercentage = self.noWaterCount * 10/100
            self.setScale(self.scaleValue - scalePercentage*self.scaleValue)

    def setBoundaryRestrict(self, flag):
        self.boundaryRestrict = flag