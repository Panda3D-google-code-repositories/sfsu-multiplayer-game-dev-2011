'''
Created on Nov 20, 2011

@author: hunvil
'''
from common.Constants import Constants
from main.MainLobby.World.World3D.Species import Species
from main.MainLobby.World.World3D.Plant3D import Plant3D

import random, sys, os, math
from panda3d.ai import *

class Plant(Species):
    def __init__(self, plantID, plantType, avatarID, zoneID, biomass):
        Species.__init__(self,avatarID, zoneID, biomass)
        if Constants.DEBUG:
            print "Adding Plant Object plantID=",plantID," plantType = ",plantType
        self.plantID   = plantID
        self.plantType = plantType
        self.avatarID   = avatarID
        self.zoneID     = zoneID
        self.biomass    = biomass
        self.xCoor      = None
        self.yCoor      = None
        self.zCoor      = None
        self.plant3DObject = None
        self.plantInstance = None
        self.setPlantInstance()
        self.plantModel = None
    
    def setPlantInstance(self):
        self.plantInstance = self.plantType + str(self.plantID)
            
    def setXCoor(self,xCoor):
        self.xCoor = xCoor
        
    def setYCoor(self,yCoor):
        self.yCoor = yCoor

    def setZCoor(self,zCoor):
        self.zCoor = zCoor
        
    def getXCoor(self):
        return self.xCoor
    
    def getYCoor(self):
        return self.yCoor
     
    def getZCoor(self):
        return self.zCoor
    
    def getPlantID(self):
        return self.plantID
    
    def getPlantType(self):
        return self.plantType
    
    def createPlant3D(self,zoneObject,modelPath,scaleValue):
        self.scaleValue = scaleValue
        self.plant3DObject  = Plant3D()
        #since we know the plantType for this object we can extract the modelName from the Models.py file
        self.plant3DObject.tree(zoneObject, self.xCoor, self.yCoor,modelPath,self.scaleValue)

    def get3DPlantModel(self):
        self.plantModel = self.plant3DObject.getPlantModel()
        return self.plantModel