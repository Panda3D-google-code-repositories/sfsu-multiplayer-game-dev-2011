from common.Constants import Constants
from main.MainLobby.World.World3D.SpeciesType import SpeciesType

import random, sys, os, math
from panda3d.ai import *

class PlantType(SpeciesType):
    def __init__(self, plantID, plantType, desc, cost, maxBiomass, waterNeedFreq, waterBiomassLoss, healChance, growthRate, growRadius,lightNeedFrequency):
        super(self).__init__(plantType,desc,cost,maxBiomass,waterNeedFreq,waterBiomassLoss,healChance, growthRate)
        if Constants.DEBUG:
            print "Adding Plant Type-",plantType,plantID
        self.plantID         = plantID;
        self.growRadius      = growRadius;
        self.lightNeedFrequency  = lightNeedFrequency;
        self.plantPredators = [];
        
    def getPlantID(self):
        return self.plantID
    
    def getGrowRadius(self):
        return self.growRadius
    
    def getGrowthRate(self):
        return self.getGrowthRate
    
#    def setPlantPredator(self,plantPredator):
#        self.plantPredators.append(plantPredator)
#        
#    def getPlantPredators(self):
#        return self.plantPredators
        