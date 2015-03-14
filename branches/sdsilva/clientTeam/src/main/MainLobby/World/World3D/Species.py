'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants

class Species():
    #def __init__(self,speciesType,desc,cost,maxBiomass,waterNeedFreq,waterBiomassLoss,healChance, growthRate):
    def __init__(self,speciesType):
        if Constants.DEBUG:
            print "Adding Species"        
        self.speciesType = speciesType;
        self.description =None#= desc;
        self.cost =None#= cost;
        self.maxBiomass =None#= maxBiomass;
        self.waterNeedFrequency =None#= waterNeedFreq;
        self.waterBiomassLoss =None#= waterBiomassLoss;
        self.healChance =None#= healChance;
        self.growthRate =None#= growthRate;
        
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