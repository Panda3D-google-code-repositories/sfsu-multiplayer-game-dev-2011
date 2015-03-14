'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants

class AnimalType:

    def __init__(self, animalTypeID, animalType,desc, cost, maxBiomass, mass, movementForce, maxForce,predatorList,preyList,model_id,animalCategory):

        self.animalTypeID    = animalTypeID
        self.animalType      = animalType
        self.desc            = desc
        self.cost            = cost
        self.maxBiomass      = maxBiomass
        self.animalPrey      = preyList
        self.animalPredators = predatorList
        self.model_id        = model_id
        self.animalCategory  = animalCategory
        
    def getAnimalCategory(self):
        return self.animalCategory
        
    def getAnimalTypeID(self):
        return self.animalTypeID
    
    def getAnimalType(self):
        return self.animalType
    
    def getDescription(self):
        return self.desc
    
    def getCost(self):
        return self.cost
    
    def getmaxBiomass(self):
        return self.maxBiomass
    
    def getAnimalPreyList(self):
        return self.animalPrey
    
    def getAnimalPredatorList(self):
        return self.animalPredators

    def getModelID(self):
        return self.model_id
