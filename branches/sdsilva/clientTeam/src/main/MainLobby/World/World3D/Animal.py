'''
        Created on Nov 13, 2011
        
        @author: lloyd
        '''
        #@PydevCodeAnalysisIgnore
'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants
from main.MainLobby.World.World3D.Species import Species

import random, sys, os, math
from panda3d.ai import *

class Animal(Species):
    def __init__(self,animalTypeID,speciesType,xCoor,yCoor):
        Species.__init__(self,speciesType)
    #def __init__(self, animalTypeID, speciesType, desc, cost, maxBiomass, biomass, zoneId, envId, xCoor, yCoor, waterNeedFreq, waterBiomassLoss, healChance, growthRate, loyalty, maxTravelPerSec):
        #super(self).__init__(speciesType,desc,cost,maxBiomass,waterNeedFreq,waterBiomassLoss,healChance, growthRate)
        if Constants.DEBUG:
            print "Adding Animal Species"
        self.animalTypeID     = animalTypeID;
        self.loyalty          =None#= loyalty;
        self.maxTravelPerSec  =None#= maxTravelPerSec;
        self.biomass          =None#= biomass
        self.zoneId           =2#= zoneId
        self.envId            =0#= envId
        self.xCoor            = xCoor
        self.yCoor            = yCoor
        
        self.animalPrey      = [];
        self.animalPredators = [];
        
        self.AICharacterList = {}
            
            
    def getAnimalTypeId(self):
        return self.animalTypeID
    
    def setLoyalty(self,loyalty):
        self.loyalty = loyalty  #for every 7 gamescale days if animal is in others environment, loyalty increases by 1
        
    def getLoyalty(self):
        return self.loyalty
    
    def getMaxTravelPerSec(self):
        return self.maxTravelPerSec
    
    def setBiomass(self,biomass):
        self.biomass = biomass  #every game scale day the biomass of animal is recalculated and updated
        
    def getBiomass(self):
        return self.biomass     

    def setZoneId(self,zoneId): #if animal moves to another zone when user changes environment   
        self.zoneId =zoneId
        
    def getZoneId(self):
        return self.zoneId
    
    def setEnvId(self,envId):   #when user moves animal to another environment change the envId for animal
        self.envId = envId
        
    def getEnvId(self):
        return self.envId
    
    def setXCoor(self,xCoor):
        self.xCoor = xCoor      #we just need animals x & y coordinates in world, z to be computed from x,y

    def getXCoor(self):
        return self.xCoor
    
    def setYCoor(self,yCoor):
        self.yCoor = yCoor
        
    def getYCoor(self):
        return self.yCoor