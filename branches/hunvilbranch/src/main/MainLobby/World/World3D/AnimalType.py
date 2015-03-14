'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants
from main.MainLobby.World.World3D.SpeciesType import SpeciesType

import random, sys, os, math
from panda3d.ai import *

class AnimalType(SpeciesType):
    def __init__(self, animalID, animalType, desc, cost, maxBiomass, waterNeedFreq, waterBiomassLoss, healChance, growthRate, loyalty, maxTravelPerSec):
        super(self).__init__(animalType,desc,cost,maxBiomass,waterNeedFreq,waterBiomassLoss,healChance, growthRate)
        if Constants.DEBUG:
            print "Adding Animal Type-",animalType,animalID
        self.animalID         = animalID;
        self.loyalty          = loyalty;
        self.maxTravelPerSec  = maxTravelPerSec;
        self.animalPrey      = [];
        self.animalPredators = [];

    def getAnimalID(self):
        return self.animalID
    
    def setLoyalty(self,loyalty):
        self.loyalty = loyalty  #for every 7 gamescale days if animal is in others environment, loyalty increases by 1
        
    def getLoyalty(self):
        return self.loyalty
    
    def getMaxTravelPerSec(self):
        return self.maxTravelPerSec

#    def setAnimalPrey(self,animalPrey):
#        self.animalPrey.append(animalPrey)
#        
#    def getAnimalPrey(self):
#        return self.getAnimalPrey
#    
#    def setAnimalPredator(self,animalPredator):
#        self.animalPredator.append(animalPredator)
#        
#    def getAnimalPredator(self):
#        return self.animalPredators
        