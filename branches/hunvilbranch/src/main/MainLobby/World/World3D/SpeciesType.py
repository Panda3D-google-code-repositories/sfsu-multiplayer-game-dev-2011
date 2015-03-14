'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants

class SpeciesType():
    def __init__(self,speciesType,desc,cost,maxBiomass,waterNeedFreq,waterBiomassLoss,healChance, growthRate):
        if Constants.DEBUG:
            print "Adding Species Type-",speciesType        
        self.speciesType     = speciesType;
        self.description    = desc;
        self.cost           = cost;
        self.maxBiomass     = maxBiomass;
        self.waterNeedFrequency = waterNeedFreq;
        self.waterBiomassLoss   = waterBiomassLoss;
        self.healChance         = healChance;
        self.growthRate         = growthRate;
        
    def getSpeciesType(self):
        return self.speciesType
    
    def getDescription(self):
        return self.description
    
    def getCost(self):
        return self.cost
    
    def getMaxBiomass(self):
        return self.maxBiomass
    
    def getWaterNeedfrequency(self):
        return self.waterNeedFrequency
    
    def getWaterBioMassLoss(self):
        return self.waterBiomassLoss
    
    def getHealChance(self):
        return self.healChance
    
    def getGrowthRate(self):
        return self.growthRate