'''
Created on Nov 20, 2011

@author: hunvil
'''
from common.Constants import Constants
from main.MainLobby.World.World3D.Species import Species
from main.MainLobby.World.World3D.Animal3D import Animal3D
from direct.task import Task

import random, sys, os, math
from panda3d.ai import *

class Animal(Species):
    def __init__(self, animalID, animalType, avatarID, zoneID, biomass,terrain):
        Species.__init__(self,avatarID, zoneID, biomass)
        if Constants.DEBUG:
            print "Adding Animal Object animalID = ",animalID," animalType = ",animalType
        self.animalID   = animalID
        self.animalType = animalType
        self.avatarID   = avatarID
        self.zoneID     = zoneID
        self.biomass    = biomass
        self.xCoor      = None
        self.yCoor      = None
        self.zCoor      = None
        self.animal3DObject = None
        self.animalInstance = None
        self.setAnimalInstance()
        self.modelPath = None
        self.modelAnimation = None
        self.scaleValue = None        
        self.terrain = terrain
        self.previousZ = 0        
        self.actor = None
        self.zoneObj = None
        
    def setAnimalInstance(self):
        self.animalInstance = self.animalType + str(self.animalID)
    
    def getAnimalInstance(self):
        return self.animalInstance
                
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
    
    def getAnimalID(self):
        return self.animalID
    
    def getAnimalType(self):
        return self.animalType
    
    def getScale(self):
        return self.scaleValue
    
    def createAnimal3D(self,zoneObject,modelPathAndAnimation,scaleValue):
        self.modelPath = modelPathAndAnimation[0]
        self.modelAnimation = modelPathAndAnimation[1]
        self.scaleValue = scaleValue
        self.animal3DObject  = Animal3D()
        self.animal3DObject.animal(zoneObject, self.xCoor, self.yCoor,self.modelPath,self.modelAnimation,self.scaleValue)

    def get3DAnimalActor(self):
        self.actor = self.animal3DObject.getActor()
        return self.actor
    
    def getAnimalWalk(self):
        self.walk = self.animalType+"-walk"
        return self.walk

    def getAnimalDie(self):
        self.die = self.animalType+"-die"
        return self.die
    
    def getAnimalEat(self):
        self.eat = self.animalType+"-eat"
        return self.eat
        
    def sentZoneObj(self,zoneObj):
        self.zoneObj = zoneObj
        return None
    
    def move(self,task):
        elapsed = globalClock.getDt()
        self.actor.setY(self.actor, -elapsed*25)

        x = self.actor.getX()
        y = self.actor.getY()
        z = self.terrain.getElevation(x,y)*self.terrain.getRoot().getSz()
#        print x,y
        if self.zoneObj.getX(x)>500:
#            print "x exceeded 500"
            self.actor.setX(x-10)
            h = self.actor.getH()
            newh = h +90
#            print "h - ",h,newh
            self.actor.setHpr(newh,0,0)              
        if self.zoneObj.getX(x)<2:
#            print "x less than 2"
            self.actor.setX(x+10)
            h = self.actor.getH()
            newh = h +180
#            print "h - ",h,newh
            self.actor.setHpr(newh,0,0)            
        if self.zoneObj.getY(y)>500:
#            print "y exceeded 500"
            self.actor.setY(y-10)
            h = self.actor.getH()
            newh = h +90
#            print "h - ",h,newh
            self.actor.setHpr(newh,0,0)            
        if self.zoneObj.getY(y)<2:
#            print "y less then 2"
            self.actor.setY(y-10)
            h = self.actor.getH()
            newh = h +180
#            print "h - ",h,newh
            self.actor.setHpr(newh,0,0)            

                  
        
        diff = self.previousZ - z
        diff40 = diff * 40
#Uncomment for debugging purposes        
        if diff40 <= 0.0 and diff40>=-15.0:
            #print "prevZ-",self.previousZ," z-",z," diff-",diff," diff*40-",diff*40
            diff40=5.0
        else:
            #print "diff40- ",diff40
            diff40 = 11.0
        #Multiplication factor for uphill and downhill
        self.actor.setP(diff40)
        #print "z-",z
        self.actor.setZ(z)
        self.previousZ = z
        
        return Task.cont    