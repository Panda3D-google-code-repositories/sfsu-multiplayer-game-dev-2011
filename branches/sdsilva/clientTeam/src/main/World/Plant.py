'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants
from main.World.Species import Species

class Plant(Species):
    def __init__(self, plantTypeID, speciesType, desc, cost, maxBiomass, waterNeedFreq, waterBiomassLoss, healChance, growthRate, growRadius,lightNeedFreq):
        super(self).__init__(speciesType,desc,cost,maxBiomass,waterNeedFreq,waterBiomassLoss,healChance, growthRate)
        if Constants.DEBUG:
            print "Adding Plant Species Type"
            
        self.plantTypeID = plantTypeID;
        self.growRadius = growRadius;
        self.lightNeedFrequency = lightNeedFreq;
        
        self.plantPrey        = {};
        self.plantPredators   = {};
            
    def getPlantTypeId(self):
        return self.plantTypeID
    
    def getGrowRadius(self):
        return self.growRadius
    
    def getLightNeedfrequency(self):
        return self.lightNeedFrequency