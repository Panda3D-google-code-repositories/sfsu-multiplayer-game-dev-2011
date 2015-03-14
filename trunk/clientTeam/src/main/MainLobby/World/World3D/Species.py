'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants

class Species:

    def __init__(self, name, avatarID, zoneID, biomass):

        self.name = name
        self.avatarID = avatarID
        self.zoneID   = zoneID
        self.biomass  = biomass
        self.type = None
        self.description = None
        self.cost = None
        self.maxBiomass = None
        self.waterNeedFrequency = None
        self.waterBiomassLoss = None
        self.healChance = None
        self.growthRate = None
        self.groupSize = 1
        self.isDead = False
        self.numDead = 0
        self.organism_type = 0
        self.lifeStatus = Constants.LIFE_STATUS_ALIVE

    def getName(self):
        return self.name

    def setName(self, name):
        return self.name

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

    def getGroupSize(self):
        return self.groupSize

    def setGroupSize(self, group_size):
        self.groupSize = group_size

        if group_size == 0:
            self.lifeStatus = Constants.LIFE_STATUS_DEAD

    def getOrganismType(self):
        return self.organism_type

    def setOrganismType(self, organism_type):
        self.organism_type = organism_type

    def getLifeStatus(self):
        return self.lifeStatus

    def setLifeStatus(self, lifeStatus):
        self.lifeStatus = lifeStatus
